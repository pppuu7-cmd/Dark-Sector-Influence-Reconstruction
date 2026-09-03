#!/usr/bin/env python3
"""NON-AUTHORITATIVE Exp073CR persistent-worker scheduler prototype v0.2.

Resource/control refinement only. Numerical helper and shard boundaries are
unchanged from the research v0.1 lineage. No scientific/resource authority.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import time
from pathlib import Path

import numpy as np

import exp073cr_64shard_scheduler_v0_1 as v1

_WORKER_PCL = None
_WORKER_HELPER = None
_WORKER_DPTR = None
_WORKER_IPTR = None
_WORKER_NMTLIB = None
_WORKER_EDGES = None


def init_worker(pcl_path: str, helper_so: str):
    global _WORKER_PCL, _WORKER_HELPER, _WORKER_DPTR, _WORKER_IPTR, _WORKER_NMTLIB, _WORKER_EDGES
    for k in v1.THREAD_ENV:
        if os.environ.get(k) != '1':
            raise RuntimeError(f'nested thread pin violated in initializer: {k}={os.environ.get(k)!r}')
    _WORKER_PCL = v1.exact_array(Path(pcl_path), (v1.L,), 'persistent worker PCL')
    _WORKER_HELPER, _WORKER_DPTR, _WORKER_IPTR = v1.bind_helper(Path(helper_so))
    _WORKER_NMTLIB = v1.runtime_nmtlib()
    _WORKER_EDGES = np.ascontiguousarray(v1.EDGES, dtype=np.int32)


def worker(s: v1.Shard):
    if any(x is None for x in (_WORKER_PCL,_WORKER_HELPER,_WORKER_DPTR,_WORKER_IPTR,_WORKER_NMTLIB,_WORKER_EDGES)):
        raise RuntimeError('persistent worker initializer did not complete')
    out=np.zeros((s.ll3_hi-s.ll3_lo,),dtype=np.float64)
    s1,s2,n1,n2=v1.SIGNATURE
    start_ns=time.time_ns(); t0=time.monotonic(); c0=time.process_time()
    rc=_WORKER_HELPER(
        _WORKER_NMTLIB,
        _WORKER_PCL.ctypes.data_as(_WORKER_DPTR),
        v1.LMAX,s1,s2,n1,n2,
        _WORKER_EDGES.ctypes.data_as(_WORKER_IPTR),len(_WORKER_EDGES)-1,
        s.band,s.ll3_lo,s.ll3_hi,1,out.ctypes.data_as(_WORKER_DPTR),
    )
    end_ns=time.time_ns(); wall=time.monotonic()-t0; cpu=time.process_time()-c0
    if rc!=0: raise RuntimeError(f'shard {s}: helper rc={rc}')
    return s,v1.canon(out),{
        'numerical_start_epoch_ns':start_ns,
        'numerical_end_epoch_ns':end_ns,
        'worker_wall_seconds':wall,
        'worker_cpu_seconds':cpu,
        'scheduler_prototype':'exp073cr_64shard_scheduler_v0_2_persistent_worker',
    }


def compute(root: Path, candidate: Path, pcl: Path, helper: Path, branch: str, sync_script: Path):
    _,shards,candidate_sha=v1.load_candidate(candidate)
    v1.exact_array(pcl,(v1.L,),'prototype PCL')
    v1.bind_helper(helper)  # fail-fast ABI probe in coordinator
    missing=[s for s in shards if v1.load_shard(root,s,candidate_sha) is None]
    if not missing:
        print('all 64 shards already durable',flush=True); return
    pending=iter(missing); futs={}; admitted=[]
    ex=cf.ProcessPoolExecutor(
        max_workers=v1.OUTER_WORKERS,
        initializer=init_worker,
        initargs=(str(pcl),str(helper)),
    )
    try:
        for _ in range(min(v1.OUTER_WORKERS,len(missing))):
            s=next(pending); futs[ex.submit(worker,s)]=s
        while futs:
            done,_=cf.wait(tuple(futs),return_when=cf.FIRST_COMPLETED)
            for fut in done:
                expected=futs.pop(fut); got,a,tel=fut.result()
                if got!=expected: raise RuntimeError(f'worker identity mismatch expected={expected} got={got}')
                v1.store_shard(root,got,a,candidate_sha,tel)
                v1.sync(root,branch,sync_script,f'shard-b{got.band:02d}-l{got.ll3_lo:05d}-{got.ll3_hi:05d}')
                admitted.append(got)
                try:
                    nxt=next(pending); futs[ex.submit(worker,nxt)]=nxt
                except StopIteration: pass
        ex.shutdown(wait=True)
    except BaseException as e:
        try: ex.shutdown(wait=False,cancel_futures=True)
        except Exception: pass
        remaining=[s for s in shards if v1.load_shard(root,s,candidate_sha) is None]
        v1.diagnostic(root,'compute-v0.2-persistent-worker',e,admitted,remaining,branch,sync_script)
        raise


def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('validate-candidate'); p.add_argument('--candidate',required=True); p.add_argument('--helper')
    p=sp.add_parser('compute'); p.add_argument('--root',required=True); p.add_argument('--candidate',required=True); p.add_argument('--pcl',required=True); p.add_argument('--helper',required=True); p.add_argument('--branch',required=True); p.add_argument('--sync-script',required=True)
    p=sp.add_parser('assemble-band'); p.add_argument('--root',required=True); p.add_argument('--candidate',required=True); p.add_argument('--band',type=int,required=True); p.add_argument('--output',required=True)
    a=ap.parse_args()
    if a.cmd=='validate-candidate':
        c,s,h=v1.load_candidate(Path(a.candidate)); out={'candidate_sha256':h,'shards':len(s),'bands':c['bands'],'helper_symbol':v1.HELPER_SYMBOL,'scheduler_prototype':'v0.2-persistent-worker'}
        if a.helper: v1.bind_helper(Path(a.helper)); out['helper_abi']='PASS'
        print(json.dumps(out,sort_keys=True))
    elif a.cmd=='compute':
        compute(Path(a.root),Path(a.candidate),Path(a.pcl),Path(a.helper),a.branch,Path(a.sync_script))
    elif a.cmd=='assemble-band':
        out=v1.assemble_band(Path(a.root),Path(a.candidate),a.band); np.save(a.output,out,allow_pickle=False); print(v1.ahash(out))

if __name__=='__main__': main()
