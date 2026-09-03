#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures as cf
import ctypes
import hashlib
import importlib
import json
import os
import subprocess
import time
import traceback
from dataclasses import dataclass
from pathlib import Path

import numpy as np

L = 12288
LMAX = L - 1
EDGES = np.array([0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288], dtype=np.int32)
SIGNATURE = (0, 2, 0, 2)
OUTER_WORKERS = 8
NESTED_THREADS = 1
THREAD_ENV = ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS')

@dataclass(frozen=True, order=True)
class Shard:
    band: int
    ll3_lo: int
    ll3_hi: int


def canon(a):
    return np.ascontiguousarray(np.asarray(a, dtype='<f8'))


def ahash(a):
    a = canon(a)
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def fhash(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    os.replace(tmp, path)


def exact_array(path: Path, shape, label):
    a = np.load(path, allow_pickle=False)
    if a.dtype.str != '<f8' or not a.flags.c_contiguous or tuple(a.shape) != tuple(shape) or not np.all(np.isfinite(a)):
        raise RuntimeError(f'{label}: invalid canonical payload')
    return a


def runtime_nmtlib():
    ext = importlib.import_module('_nmtlib')
    return str(Path(ext.__file__).resolve()).encode()


def load_candidate(path: Path):
    raw = path.read_bytes()
    c = json.loads(raw)
    if c.get('status') != 'NON_AUTHORITATIVE_PREFLIGHT_ONLY':
        raise RuntimeError('prototype candidate status mismatch')
    if c.get('total_shards') != 64 or c.get('outer_workers') != 8 or c.get('nested_threads') != 1:
        raise RuntimeError('prototype candidate resource invariant mismatch')
    if c.get('bands') != list(range(29,39)) or c.get('ll3_domain') != [2,L]:
        raise RuntimeError('prototype candidate domain mismatch')
    shards=[]
    alloc=c['allocation_by_band']; bounds=c['ll3_boundaries_by_band']
    for b in range(29,39):
        k=str(b); bb=list(map(int,bounds[k])); n=int(alloc[k])
        if len(bb) != n+1 or bb[0] != 2 or bb[-1] != L or any(x>=y for x,y in zip(bb[:-1],bb[1:])):
            raise RuntimeError(f'band {b}: invalid shard partition')
        for lo,hi in zip(bb[:-1],bb[1:]): shards.append(Shard(b,lo,hi))
    if len(shards) != 64 or len(set(shards)) != 64:
        raise RuntimeError('candidate shard cardinality/uniqueness mismatch')
    return c, shards, hashlib.sha256(raw).hexdigest()


def shard_dir(root: Path, s: Shard):
    return root/'shards'/f'band_{s.band:02d}'/f'll3_{s.ll3_lo:05d}_{s.ll3_hi:05d}'


def load_shard(root: Path, s: Shard, candidate_sha: str):
    d=shard_dir(root,s); rp=d/'receipt.json'
    if not rp.exists(): return None
    r=json.loads(rp.read_text()); a=exact_array(d/'payload.npy',(s.ll3_hi-s.ll3_lo,),f'shard {s}')
    want={'band':s.band,'ll3_interval':[s.ll3_lo,s.ll3_hi],'candidate_sha256':candidate_sha,'complete':True}
    for k,v in want.items():
        if r.get(k)!=v: raise RuntimeError(f'shard {s}: receipt mismatch {k}')
    if r.get('payload_sha256')!=ahash(a): raise RuntimeError(f'shard {s}: SHA mismatch')
    return r


def store_shard(root: Path, s: Shard, a, candidate_sha: str, tel: dict):
    a=canon(a)
    if tuple(a.shape)!=(s.ll3_hi-s.ll3_lo,) or not np.all(np.isfinite(a)):
        raise RuntimeError(f'shard {s}: invalid worker payload')
    d=shard_dir(root,s); d.mkdir(parents=True,exist_ok=True); np.save(d/'payload.npy',a,allow_pickle=False)
    r={'format':'DSIR_LL3_SHARD_PROTOTYPE_V0_0','complete':True,'band':s.band,'ll3_interval':[s.ll3_lo,s.ll3_hi],
       'shape':[s.ll3_hi-s.ll3_lo],'dtype':'<f8','payload_sha256':ahash(a),'candidate_sha256':candidate_sha,
       'outer_workers':8,'nested_threads':1,**tel}
    atomic_json(d/'receipt.json',r); return r


def worker(s: Shard, pcl_path: str, helper_so: str):
    for k in THREAD_ENV:
        if os.environ.get(k) != '1': raise RuntimeError(f'nested thread pin violated: {k}={os.environ.get(k)!r}')
    pcl=exact_array(Path(pcl_path),(L,),f'worker PCL {s}')
    lib=ctypes.CDLL(str(Path(helper_so).resolve())); dptr=ctypes.POINTER(ctypes.c_double); iptr=ctypes.POINTER(ctypes.c_int)
    f=lib.exp073cr_stream_band_ll3_range
    f.argtypes=[ctypes.c_char_p,dptr,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,iptr,ctypes.c_int,
                ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,dptr]
    f.restype=ctypes.c_int
    edges=np.ascontiguousarray(EDGES,dtype=np.int32); out=np.zeros((s.ll3_hi-s.ll3_lo,),dtype=np.float64)
    s1,s2,n1,n2=SIGNATURE; start_ns=time.time_ns(); t0=time.monotonic(); c0=time.process_time()
    rc=f(runtime_nmtlib(),pcl.ctypes.data_as(dptr),LMAX,s1,s2,n1,n2,edges.ctypes.data_as(iptr),len(edges)-1,
         s.band,s.ll3_lo,s.ll3_hi,1,out.ctypes.data_as(dptr))
    end_ns=time.time_ns(); wall=time.monotonic()-t0; cpu=time.process_time()-c0
    if rc!=0: raise RuntimeError(f'shard {s}: helper rc={rc}')
    a=canon(out)
    return s,a,{'numerical_start_epoch_ns':start_ns,'numerical_end_epoch_ns':end_ns,
                'worker_wall_seconds':wall,'worker_cpu_seconds':cpu}


def sync(root: Path, branch: str, script: Path, label: str):
    p=subprocess.run(['bash',str(script),'push',str(root),branch,label],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if p.stdout: print(p.stdout,end='' if p.stdout.endswith('\n') else '\n',flush=True)
    if p.returncode: raise subprocess.CalledProcessError(p.returncode,p.args,output=p.stdout)


def diagnostic(root: Path, stage: str, exc: BaseException, admitted, remaining, branch=None, script=None):
    rec={'format':'DSIR_LL3_SHARD_DIAGNOSTIC_PROTOTYPE_V0_0','stage':stage,'complete':True,
         'exception_type':type(exc).__name__,'exception_string':str(exc),
         'traceback':''.join(traceback.format_exception(type(exc),exc,exc.__traceback__))[-16000:],
         'admitted_shards':[[x.band,x.ll3_lo,x.ll3_hi] for x in sorted(admitted)],
         'remaining_shards':[[x.band,x.ll3_lo,x.ll3_hi] for x in sorted(remaining)],
         'timestamp_ns':time.time_ns()}
    atomic_json(root/'diagnostics'/'first_failure.json',rec)
    if branch and script:
        try: sync(root,branch,script,'diagnostic-first-failure')
        except Exception as de: print(f'DIAGNOSTIC_SYNC_FAILED {type(de).__name__}: {de}',flush=True)
    print(json.dumps(rec,sort_keys=True),flush=True)


def compute(root: Path, candidate: Path, pcl: Path, helper: Path, branch: str, sync_script: Path, heavy_first: bool):
    _,shards,candidate_sha=load_candidate(candidate)
    exact_array(pcl,(L,),'prototype PCL')
    missing=[s for s in shards if load_shard(root,s,candidate_sha) is None]
    if not missing: print('all 64 shards already durable',flush=True); return
    # Production successor may freeze heavy-first order after preregistration. Prototype defaults to candidate order unless requested.
    if heavy_first:
        raise RuntimeError('heavy-first requires a prospectively frozen per-shard proxy table; prototype refuses implicit runtime reordering')
    pending=iter(missing); futs={}; admitted=[]; ex=cf.ProcessPoolExecutor(max_workers=OUTER_WORKERS)
    try:
        for _ in range(min(OUTER_WORKERS,len(missing))):
            s=next(pending); futs[ex.submit(worker,s,str(pcl),str(helper))]=s
        while futs:
            done,_=cf.wait(tuple(futs),return_when=cf.FIRST_COMPLETED)
            for fut in done:
                expected=futs.pop(fut); got,a,tel=fut.result()
                if got!=expected: raise RuntimeError(f'worker identity mismatch expected={expected} got={got}')
                store_shard(root,got,a,candidate_sha,tel)
                sync(root,branch,sync_script,f'shard-b{got.band:02d}-l{got.ll3_lo:05d}-{got.ll3_hi:05d}')
                admitted.append(got)
                try:
                    nxt=next(pending); futs[ex.submit(worker,nxt,str(pcl),str(helper))]=nxt
                except StopIteration: pass
        ex.shutdown(wait=True)
    except BaseException as e:
        try: ex.shutdown(wait=False,cancel_futures=True)
        except Exception: pass
        remaining=[s for s in shards if load_shard(root,s,candidate_sha) is None]
        diagnostic(root,'compute',e,admitted,remaining,branch,sync_script)
        raise


def assemble_band(root: Path, candidate: Path, band: int):
    _,shards,candidate_sha=load_candidate(candidate); ss=[s for s in shards if s.band==band]
    if not ss: raise RuntimeError(f'band {band}: no shards')
    out=np.zeros((L,),dtype='<f8'); covered=np.zeros((L,),dtype=np.uint8)
    for s in sorted(ss,key=lambda z:z.ll3_lo):
        r=load_shard(root,s,candidate_sha)
        if r is None: raise RuntimeError(f'band {band}: missing shard {s}')
        a=exact_array(shard_dir(root,s)/'payload.npy',(s.ll3_hi-s.ll3_lo,),f'assemble {s}')
        if np.any(covered[s.ll3_lo:s.ll3_hi]): raise RuntimeError(f'band {band}: overlap at {s}')
        out[s.ll3_lo:s.ll3_hi]=a; covered[s.ll3_lo:s.ll3_hi]=1
    if np.any(covered[2:]!=1) or np.any(covered[:2]!=0): raise RuntimeError(f'band {band}: ll3 coverage mismatch')
    if out[0]!=0.0 or out[1]!=0.0 or not np.all(np.isfinite(out)): raise RuntimeError(f'band {band}: assembled canonical invariant failed')
    return canon(out)


def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('validate-candidate'); p.add_argument('--candidate',required=True)
    p=sp.add_parser('compute'); p.add_argument('--root',required=True); p.add_argument('--candidate',required=True); p.add_argument('--pcl',required=True); p.add_argument('--helper',required=True); p.add_argument('--branch',required=True); p.add_argument('--sync-script',required=True); p.add_argument('--heavy-first',action='store_true')
    p=sp.add_parser('assemble-band'); p.add_argument('--root',required=True); p.add_argument('--candidate',required=True); p.add_argument('--band',type=int,required=True); p.add_argument('--output',required=True)
    a=ap.parse_args()
    if a.cmd=='validate-candidate':
        c,s,h=load_candidate(Path(a.candidate)); print(json.dumps({'candidate_sha256':h,'shards':len(s),'bands':c['bands']},sort_keys=True))
    elif a.cmd=='compute':
        compute(Path(a.root),Path(a.candidate),Path(a.pcl),Path(a.helper),a.branch,Path(a.sync_script),a.heavy_first)
    elif a.cmd=='assemble-band':
        out=assemble_band(Path(a.root),Path(a.candidate),a.band); np.save(a.output,out,allow_pickle=False); print(ahash(out))

if __name__=='__main__': main()
