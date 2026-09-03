#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures as cf
import ctypes
import hashlib
import importlib
import json
import os
import resource
import subprocess
import time
from pathlib import Path

import numpy as np

L = 12288
LMAX = L - 1
EDGES = np.array([0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288], dtype=np.int32)
SIGNATURE = (0, 2, 0, 2)
BANDS = tuple(range(16))
OUTER_WORKERS = 8
NESTED_THREADS = 1
CPU_FRACTION_MIN = 0.90
PREREG_COMMIT = '7a4c47a52204570abb5efbc04b583d66a93c26bf'
POLICY_COMMIT = 'f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427'
RANGE_HELPER_COMMIT = 'fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22'
SYNC_COMMIT = 'bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1'
UPSTREAM_CM_HEAD = 'd405a7a934bbd8caf464cd2a4bcb6052b8d205cd'
UPSTREAM_CM_FINGERPRINT = '9e10b26b57464cc70ce8cb0c5cfedbab118662619ea314beed2f854d9ed65978'
PCL_SHA = 'ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d'
REFERENCE_SHA = '36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf'
PASS = 'PASS_EXP073CN_WM_S3_8WORKER_BAND_CHECKPOINT_RESOURCE_V0_1'
FAIL_EXACT = 'FAIL_EXP073CN_WM_S3_8WORKER_EXACT_EQUIVALENCE_V0_1'
FAIL_SWAP = 'FAIL_EXP073CN_WM_S3_8WORKER_SWAP_SAFETY_V0_1'
FAIL_CPU = 'FAIL_EXP073CN_WM_S3_8WORKER_CPU_TARGET_V0_1'


def canon(x):
    return np.ascontiguousarray(np.asarray(x, dtype='<f8'))


def chash(x):
    a = canon(x)
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def jhash(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def atomic_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    os.replace(tmp, path)


def exact_array(path: Path, shape, label):
    a = np.load(path, allow_pickle=False)
    if a.dtype.str != '<f8' or not a.flags.c_contiguous or tuple(a.shape) != tuple(shape) or not np.all(np.isfinite(a)):
        raise RuntimeError(f'{label}: invalid canonical payload')
    return a


def contract(source_head: str, driver_commit: str):
    d = {
        'format': 'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1',
        'experiment': 'Exp073CN', 'version': 'v0.1', 'task': 'Wm_S3',
        'source_head': source_head, 'driver_commit': driver_commit,
        'prereg_commit': PREREG_COMMIT, 'policy_commit': POLICY_COMMIT,
        'range_helper_commit': RANGE_HELPER_COMMIT, 'checkpoint_sync_commit': SYNC_COMMIT,
        'checkpoint_namespace': 'checkpoints/exp073cn-wm-s3-8worker-resource-v0-1',
        'source_bin': 3, 'signature': list(SIGNATURE), 'lmax': LMAX, 'row_length': L,
        'bands': list(BANDS), 'outer_workers': OUTER_WORKERS, 'nested_threads': NESTED_THREADS,
        'cpu_fraction_min': CPU_FRACTION_MIN, 'dtype': '<f8',
        'upstream_cm_checkpoint_head': UPSTREAM_CM_HEAD,
        'upstream_cm_contract_fingerprint': UPSTREAM_CM_FINGERPRINT,
        'pcl_sha256': PCL_SHA, 'reference_sha256': REFERENCE_SHA,
        'checkpoint_boundary': 'complete_pcl_import_or_complete_band_or_final_only',
        'verified_delta': 0.0, 'draft_data_delta': 0.0,
    }
    d['fingerprint'] = jhash(d)
    return d


def load_contract(root: Path):
    p = root / 'contract.json'
    if not p.exists(): raise RuntimeError('contract absent')
    c = json.loads(p.read_text())
    fp = c.get('fingerprint'); x = dict(c); x.pop('fingerprint', None)
    if fp != jhash(x): raise RuntimeError('contract fingerprint mismatch')
    return c


def init(root: Path, source_head: str, driver_commit: str):
    root.mkdir(parents=True, exist_ok=True)
    want = contract(source_head, driver_commit)
    p = root / 'contract.json'
    if p.exists():
        got = json.loads(p.read_text())
        if got != want: raise RuntimeError('checkpoint contract mismatch; fail closed')
    else: atomic_json(p, want)
    print(want['fingerprint'], flush=True)


def validate_cm(cm: Path):
    cc = json.loads((cm/'contract.json').read_text())
    if cc.get('fingerprint') != UPSTREAM_CM_FINGERPRINT: raise RuntimeError('CM contract fingerprint mismatch')
    x = dict(cc); x.pop('fingerprint', None)
    if jhash(x) != UPSTREAM_CM_FINGERPRINT: raise RuntimeError('CM contract self-hash mismatch')
    pcl = exact_array(cm/'stages/pcl/payload.npy', (L,), 'CM PCL')
    pr = json.loads((cm/'stages/pcl/receipt.json').read_text())
    if pr.get('contract_fingerprint') != UPSTREAM_CM_FINGERPRINT or pr.get('payload_sha256') != PCL_SHA or chash(pcl) != PCL_SHA:
        raise RuntimeError('CM PCL provenance/SHA mismatch')
    ref = exact_array(cm/'stages/reference/payload.npy', (8,L), 'CM reference')
    rr = json.loads((cm/'stages/reference/receipt.json').read_text())
    if rr.get('contract_fingerprint') != UPSTREAM_CM_FINGERPRINT or rr.get('payload_sha256') != REFERENCE_SHA or chash(ref) != REFERENCE_SHA:
        raise RuntimeError('CM reference provenance/SHA mismatch')
    return pcl, ref


def import_upstream(root: Path, cm: Path):
    c = load_contract(root)
    pcl, ref = validate_cm(cm)
    d = root/'upstream'; d.mkdir(parents=True, exist_ok=True)
    np.save(d/'pcl.npy', pcl, allow_pickle=False); np.save(d/'reference_0_7.npy', ref, allow_pickle=False)
    rec = {'format':'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1','experiment':'Exp073CN','stage':'upstream','complete':True,
           'contract_fingerprint':c['fingerprint'],'upstream_cm_head':UPSTREAM_CM_HEAD,'upstream_cm_contract_fingerprint':UPSTREAM_CM_FINGERPRINT,
           'pcl_sha256':chash(pcl),'reference_sha256':chash(ref),'dtype':'<f8'}
    atomic_json(d/'receipt.json', rec); print(json.dumps(rec, sort_keys=True), flush=True)


def validate_upstream(root: Path):
    c = load_contract(root); d=root/'upstream'; r=json.loads((d/'receipt.json').read_text())
    if r.get('complete') is not True or r.get('contract_fingerprint') != c['fingerprint']: raise RuntimeError('upstream receipt mismatch')
    pcl=exact_array(d/'pcl.npy',(L,),'PCL'); ref=exact_array(d/'reference_0_7.npy',(8,L),'reference')
    if chash(pcl)!=PCL_SHA or chash(ref)!=REFERENCE_SHA: raise RuntimeError('upstream payload SHA mismatch')
    return pcl,ref


def runtime_nmtlib():
    ext=importlib.import_module('_nmtlib'); return str(Path(ext.__file__).resolve()).encode()


def worker(band: int, pcl_path: str, ca_so: str):
    for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','NUMEXPR_NUM_THREADS'):
        if os.environ.get(k) != '1': raise RuntimeError(f'nested thread pin violated {k}')
    pcl=exact_array(Path(pcl_path),(L,),f'worker pcl {band}')
    lib=ctypes.CDLL(str(Path(ca_so).resolve())); dptr=ctypes.POINTER(ctypes.c_double); iptr=ctypes.POINTER(ctypes.c_int)
    f=lib.exp073ca_stream_compress_range
    f.argtypes=[ctypes.c_char_p,dptr,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,iptr,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,dptr]
    f.restype=ctypes.c_int
    edges=np.ascontiguousarray(EDGES,dtype=np.int32); out=np.zeros((1,L),dtype=np.float64)
    s1,s2,n1,n2=SIGNATURE; t0=time.monotonic(); c0=time.process_time()
    rc=f(runtime_nmtlib(),pcl.ctypes.data_as(dptr),LMAX,s1,s2,n1,n2,edges.ctypes.data_as(iptr),len(edges)-1,band,band+1,1,out.ctypes.data_as(dptr))
    wall=time.monotonic()-t0; cpu=time.process_time()-c0
    if rc!=0: raise RuntimeError(f'band {band} range helper rc={rc}')
    a=canon(out[0]); return band,a,{'worker_wall_seconds':wall,'worker_cpu_seconds':cpu,'payload_sha256':chash(a)}


def band_dir(root: Path, band: int): return root/'bands'/f'band_{band:02d}'


def load_band(root: Path, band: int):
    c=load_contract(root); d=band_dir(root,band); p=d/'receipt.json'
    if not p.exists(): return None
    r=json.loads(p.read_text()); a=exact_array(d/'payload.npy',(L,),f'band {band}')
    if r.get('complete') is not True or r.get('contract_fingerprint')!=c['fingerprint'] or r.get('band')!=band or r.get('payload_sha256')!=chash(a):
        raise RuntimeError(f'band {band}: checkpoint mismatch')
    lo,hi=int(EDGES[band]),int(EDGES[band+1])
    if r.get('ell_interval') != [lo,hi]: raise RuntimeError(f'band {band}: ell interval mismatch')
    return r


def store_band(root: Path, band: int, a: np.ndarray, telemetry: dict):
    c=load_contract(root); d=band_dir(root,band); d.mkdir(parents=True,exist_ok=True); a=canon(a)
    np.save(d/'payload.npy',a,allow_pickle=False)
    r={'format':'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1','experiment':'Exp073CN','task':'Wm_S3','stage':'band','complete':True,
       'contract_fingerprint':c['fingerprint'],'band':band,'ell_interval':[int(EDGES[band]),int(EDGES[band+1])],
       'shape':[L],'dtype':'<f8','payload_sha256':chash(a),'pcl_sha256':PCL_SHA,'outer_workers':OUTER_WORKERS,'nested_threads':1,**telemetry}
    atomic_json(d/'receipt.json',r); return r


def swap_used_kib():
    vals={}
    for line in Path('/proc/meminfo').read_text().splitlines():
        if ':' in line:
            k,v=line.split(':',1); q=v.strip().split();
            if q and q[0].isdigit(): vals[k]=int(q[0])
    return max(0,vals.get('SwapTotal',0)-vals.get('SwapFree',0))


def process_tree_cpu():
    a=resource.getrusage(resource.RUSAGE_SELF); b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return float(a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime)


def sync(root: Path, branch: str, sync_script: Path, label: str):
    subprocess.run(['bash',str(sync_script),'push',str(root),branch,label],check=True)


def compute(root: Path, ca_so: Path, branch: str, sync_script: Path):
    validate_upstream(root)
    for b in BANDS: load_band(root,b)
    missing=[b for b in BANDS if load_band(root,b) is None]
    if not missing:
        print('all bands already checkpointed; no compute',flush=True); return
    if len(missing) < OUTER_WORKERS:
        print(f'resume with only {len(missing)} missing bands; exact completion allowed but CPU qualification will use persisted segment telemetry',flush=True)
    swap0=swap_used_kib(); cpu0=process_tree_cpu(); wall0=time.monotonic(); segment=os.environ.get('GITHUB_RUN_ID','local')+'-'+str(time.time_ns())
    segment_start_ns=time.time_ns(); done=[]
    with cf.ProcessPoolExecutor(max_workers=OUTER_WORKERS) as ex:
        futs={ex.submit(worker,b,str(root/'upstream/pcl.npy'),str(ca_so)):b for b in missing}
        for fut in cf.as_completed(futs):
            b,a,tel=fut.result(); tel['segment']=segment; tel['segment_start_epoch_ns']=segment_start_ns; tel['completed_epoch_ns']=time.time_ns()
            store_band(root,b,a,tel); sync(root,branch,sync_script,f'band-{b:02d}-complete'); done.append(b)
    wall=time.monotonic()-wall0; cpu=process_tree_cpu()-cpu0; swap1=swap_used_kib(); eff=cpu/wall if wall>0 else 0.0
    seg={'segment':segment,'bands_completed':sorted(done),'wall_seconds':wall,'process_tree_cpu_seconds':cpu,'effective_cpu_cores':eff,'cpu_fraction_of_8':eff/8.0,
         'swap_used_kib_before':swap0,'swap_used_kib_after':swap1,'swap_increase_kib':max(0,swap1-swap0)}
    atomic_json(root/'segments'/f'{segment}.json',seg); sync(root,branch,sync_script,'segment-telemetry'); print(json.dumps(seg,sort_keys=True),flush=True)


def finalize(root: Path):
    c=load_contract(root); _,ref=validate_upstream(root)
    rows=[]
    for b in BANDS:
        load_band(root,b); rows.append(exact_array(band_dir(root,b)/'payload.npy',(L,),f'band {b}'))
    target=canon(np.stack(rows,axis=0)); first8=canon(target[:8]); exact=bool(np.array_equal(first8,ref)) and chash(first8)==REFERENCE_SHA
    segs=[]
    sd=root/'segments'
    if sd.exists():
        for p in sorted(sd.glob('*.json')): segs.append(json.loads(p.read_text()))
    # Performance is fail-closed: at least one completed target segment must itself exercise >=8 bands.
    eligible=[s for s in segs if len(s.get('bands_completed',[]))>=8]
    if eligible:
        perf=eligible[0]
        cpu_fraction=float(perf['cpu_fraction_of_8']); swap_inc=int(perf['swap_increase_kib'])
    else:
        cpu_fraction=0.0; swap_inc=max([int(s.get('swap_increase_kib',0)) for s in segs],default=0)
    if not exact: status=FAIL_EXACT
    elif swap_inc>0: status=FAIL_SWAP
    elif cpu_fraction<CPU_FRACTION_MIN: status=FAIL_CPU
    else: status=PASS
    rec={'format':'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1','experiment':'Exp073CN','task':'Wm_S3','stage':'final','complete':True,
         'contract_fingerprint':c['fingerprint'],'target_shape':[len(BANDS),L],'dtype':'<f8','first8_sha256':chash(first8),
         'reference_sha256':REFERENCE_SHA,'array_equal_reference_0_7':bool(np.array_equal(first8,ref)),'sha_equal_reference_0_7':chash(first8)==REFERENCE_SHA,
         'cpu_fraction_of_8':cpu_fraction,'cpu_fraction_min':CPU_FRACTION_MIN,'swap_increase_kib':swap_inc,'status':status,
         'verified_delta':0.0,'draft_data_delta':0.0,'no_tolerance_rescue':True}
    atomic_json(root/'final/receipt.json',rec); print(json.dumps(rec,indent=2,sort_keys=True),flush=True); return status


def validate_all(root: Path):
    validate_upstream(root)
    for b in BANDS:
        if load_band(root,b) is None: raise RuntimeError(f'missing band {b}')
    p=root/'final/receipt.json'
    if p.exists():
        old=json.loads(p.read_text()); status=finalize(root)
        now=json.loads(p.read_text())
        if old!=now: raise RuntimeError('restored final receipt does not recompute exactly')
        return status
    return None


def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('init'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--source-head',required=True); p.add_argument('--driver-commit',required=True)
    p=sp.add_parser('import-upstream'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--cm-dir',required=True)
    p=sp.add_parser('compute'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--ca-so',required=True); p.add_argument('--branch',required=True); p.add_argument('--sync-script',required=True)
    p=sp.add_parser('finalize'); p.add_argument('--checkpoint-dir',required=True)
    p=sp.add_parser('validate'); p.add_argument('--checkpoint-dir',required=True)
    a=ap.parse_args(); root=Path(a.checkpoint_dir)
    if a.cmd=='init': init(root,a.source_head,a.driver_commit)
    elif a.cmd=='import-upstream': import_upstream(root,Path(a.cm_dir))
    elif a.cmd=='compute': compute(root,Path(a.ca_so),a.branch,Path(a.sync_script))
    elif a.cmd=='finalize':
        status=finalize(root)
        if status!=PASS: raise SystemExit(42)
    elif a.cmd=='validate': validate_all(root)

if __name__=='__main__': main()
