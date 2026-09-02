#!/usr/bin/env python3
from __future__ import annotations
import argparse, glob, hashlib, json, os, pathlib, subprocess, sys
import numpy as np

EXPECTED_COMPACT_SHA='963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd'
EXPECTED_K_SHA='c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795'
EXPECTED_W_SHA='96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087'
EXPECTED_SHAPE=(39,12288)
FIXED_CORE='Nehalem'
PASS='PASS_EXP073CI_WM_S2_DETERMINISTIC_FIXED_NEHALEM_FINALIZER_EXACT_V0_2'
FAIL='SCIENTIFIC_REPEATABILITY_FAIL_EXP073CI_WM_S2_DETERMINISTIC_FIXED_NEHALEM_FINALIZER_EXACT_V0_2'

def canon(x): return np.ascontiguousarray(x,dtype='<f8')
def ahash(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()

def find_npz(root:pathlib.Path)->pathlib.Path:
    hits=[pathlib.Path(p) for p in glob.glob(str(root/'**'/'*compact_*_v0_1.npz'),recursive=True)]
    if len(hits)!=1:
        hits=[pathlib.Path(p) for p in glob.glob(str(root/'**'/'*.npz'),recursive=True)]
    if len(hits)!=1: raise AssertionError(('npz_hits',str(root),[str(x) for x in hits]))
    return hits[0]

def load_compact(root:pathlib.Path):
    p=find_npz(root)
    with np.load(p,allow_pickle=False) as z: a=canon(z['A'])
    if a.shape!=EXPECTED_SHAPE or not np.isfinite(a).all(): raise AssertionError(('compact_shape',a.shape))
    h=ahash(a)
    if h!=EXPECTED_COMPACT_SHA: raise AssertionError(('compact_sha',h,EXPECTED_COMPACT_SHA))
    return p,a

def solve(a):
    from exp073az_article3_low_memory_general_coupling_v0_1 import k_from_a
    k=canon(k_from_a(a)); w=canon(np.linalg.solve(k,a))
    return k,w

def child(args):
    if os.environ.get('OPENBLAS_CORETYPE')!=FIXED_CORE: raise AssertionError(('OPENBLAS_CORETYPE',os.environ.get('OPENBLAS_CORETYPE')))
    _,a=load_compact(pathlib.Path(args.compact))
    k,w=solve(a)
    print(json.dumps({'lane':args.lane,'compact_sha':ahash(a),'k_sha':ahash(k),'w_sha':ahash(w),'pid':os.getpid()},sort_keys=True))

def worker(args):
    out=pathlib.Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    lanes={'A':pathlib.Path(args.compact_a),'B':pathlib.Path(args.compact_b)}
    rec={'experiment':'Exp073CI','version':'v0_2','worker':args.worker,'fixed_core':FIXED_CORE,'lanes':{},'no_tolerance_used':True,'exp073cf_fail_preserved':True,'readiness_delta':[0,0]}
    for lane,root in lanes.items():
        _,arr=load_compact(root)
        reps=[]
        for i in range(3):
            env=os.environ.copy(); env.update({'OPENBLAS_CORETYPE':FIXED_CORE,'OPENBLAS_VERBOSE':'2','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1','BLIS_NUM_THREADS':'1','OMP_DYNAMIC':'FALSE'})
            cp=subprocess.run([sys.executable,str(pathlib.Path(__file__).resolve()),'child','--compact',str(root),'--lane',lane],env=env,text=True,capture_output=True,timeout=600)
            js=[x for x in cp.stdout.splitlines() if x.strip().startswith('{')]
            cores=[x.strip() for x in cp.stderr.splitlines() if x.strip().startswith('Core:')]
            rr={'repeat':i,'returncode':cp.returncode,'stderr':cp.stderr[-4000:],'core_lines':cores}
            if cp.returncode==0 and len(js)==1:
                rr['result']=json.loads(js[0])
            reps.append(rr)
        ok=[]
        for r in reps:
            if r['returncode']!=0 or 'result' not in r: continue
            if not any(x=='Core: Nehalem' for x in r['core_lines']): continue
            z=r['result']
            if z['compact_sha']==EXPECTED_COMPACT_SHA and z['k_sha']==EXPECTED_K_SHA and z['w_sha']==EXPECTED_W_SHA: ok.append(z)
        exact_valid=(len(ok)==3 and len({(z['compact_sha'],z['k_sha'],z['w_sha']) for z in ok})==1)
        rec['lanes'][lane]={'repeats':reps,'exact_valid':exact_valid,'compact_sha':EXPECTED_COMPACT_SHA if exact_valid else None,'k_sha':EXPECTED_K_SHA if exact_valid else None,'w_sha':EXPECTED_W_SHA if exact_valid else None}
    rec['worker_exact_pass']=all(rec['lanes'][x]['exact_valid'] for x in ('A','B'))
    p=out/f'exp073ci_worker_{args.worker}_v0_2.json'; p.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'worker':args.worker,'worker_exact_pass':rec['worker_exact_pass'],'lane_A':rec['lanes']['A']['w_sha'],'lane_B':rec['lanes']['B']['w_sha']},sort_keys=True))
    if not rec['worker_exact_pass']: raise SystemExit(2)

def compare(args):
    files=sorted(pathlib.Path(args.root).rglob('exp073ci_worker_*_v0_2.json'))
    if len(files)!=4: raise AssertionError(('worker_files',len(files),[str(x) for x in files]))
    rows=[json.loads(p.read_text()) for p in files]
    by={r['worker']:r for r in rows}
    complete=set(by)=={'R1','R2','R3','R4'}
    all_pass=complete and all(r.get('worker_exact_pass') for r in by.values())
    hashes=[]
    if complete:
        for r in by.values():
            for lane in ('A','B'):
                x=r['lanes'][lane]
                hashes.append((x.get('compact_sha'),x.get('k_sha'),x.get('w_sha')))
    exact_cross=bool(all_pass and len(set(hashes))==1 and hashes[0]==(EXPECTED_COMPACT_SHA,EXPECTED_K_SHA,EXPECTED_W_SHA))
    status=PASS if exact_cross else FAIL
    out={'experiment':'Exp073CI','version':'v0_2','status':status,'classification':'EXACT_REPEATABILITY_PASS_NEW_VERSION' if exact_cross else 'SCIENTIFIC_REPEATABILITY_FAIL_NEW_VERSION','scientific_authority_for_exp073ci_v0_2':exact_cross,'exp073cf_fail_preserved':True,'fixed_core':FIXED_CORE,'workers':sorted(by),'expected_compact_sha':EXPECTED_COMPACT_SHA,'expected_k_sha':EXPECTED_K_SHA,'expected_w_sha':EXPECTED_W_SHA,'exact_cross_worker_lane_repeat_equality':exact_cross,'no_tolerance_used':True,'readiness_delta':[0,0]}
    p=pathlib.Path(args.out_json); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not exact_cross: raise SystemExit(3)

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('child'); p.add_argument('--compact',required=True); p.add_argument('--lane',required=True); p.set_defaults(fn=child)
    p=sp.add_parser('worker'); p.add_argument('--compact-a',required=True); p.add_argument('--compact-b',required=True); p.add_argument('--worker',choices=['R1','R2','R3','R4'],required=True); p.add_argument('--out-dir',required=True); p.set_defaults(fn=worker)
    p=sp.add_parser('compare'); p.add_argument('--root',required=True); p.add_argument('--out-json',required=True); p.set_defaults(fn=compare)
    a=ap.parse_args(); a.fn(a)
if __name__=='__main__': main()
