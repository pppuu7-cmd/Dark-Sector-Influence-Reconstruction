#!/usr/bin/env python3
from __future__ import annotations
import argparse, contextlib, glob, hashlib, io, json, os, pathlib, platform, subprocess, sys
from typing import Any
import numpy as np

EXPECTED_COMPACT_SHA='963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd'
EXPECTED_SHAPE=(39,12288)
EXPECTED_K_SHA='c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795'
HIST_A_W_SHA='fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84'
HIST_B_W_SHA='bed762740b625f932f016d0988be17500a2583daee08bee9a5da550de786193e'
REGIMES=('native','Nehalem','Sandybridge','Haswell')

def canon(x): return np.ascontiguousarray(x,dtype='<f8')
def ahash(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()

def find_compact(path:pathlib.Path)->pathlib.Path:
    if path.is_file(): return path
    hits=[pathlib.Path(p) for p in glob.glob(str(path/'**'/'*compact_a_v0_1.npz'),recursive=True)]
    if len(hits)!=1: raise AssertionError(('compact_hits',[str(x) for x in hits]))
    return hits[0]

def load_a(path:pathlib.Path):
    p=find_compact(path)
    with np.load(p,allow_pickle=False) as z:
        a=canon(z['A'])
    if a.shape!=EXPECTED_SHAPE or not np.isfinite(a).all(): raise AssertionError(('compact',a.shape))
    h=ahash(a)
    if h!=EXPECTED_COMPACT_SHA: raise AssertionError(('compact_sha',h,EXPECTED_COMPACT_SHA))
    return p,a

def solve(a):
    from exp073az_article3_low_memory_general_coupling_v0_1 import k_from_a
    k=canon(k_from_a(a)); w=canon(np.linalg.solve(k,a))
    if k.shape!=(39,39) or w.shape!=EXPECTED_SHAPE: raise AssertionError(('shape',k.shape,w.shape))
    if not np.isfinite(k).all() or not np.isfinite(w).all(): raise AssertionError('nonfinite')
    return k,w

def cap(fn):
    s=io.StringIO()
    try:
        with contextlib.redirect_stdout(s): fn()
        return s.getvalue()
    except Exception as e: return f'ERROR:{type(e).__name__}:{e}'

def run_text(cmd):
    try: return subprocess.run(cmd,check=False,text=True,capture_output=True,timeout=30).stdout
    except Exception as e: return f'ERROR:{type(e).__name__}:{e}'

def runtime_meta():
    cpuinfo=''
    try: cpuinfo=pathlib.Path('/proc/cpuinfo').read_text(errors='replace')
    except Exception as e: cpuinfo=f'ERROR:{type(e).__name__}:{e}'
    first={}
    for line in cpuinfo.splitlines():
        if ':' in line:
            k,v=line.split(':',1); kl=k.strip().lower()
            if kl in {'vendor_id','model name','flags'} and kl not in first: first[kl]=v.strip()
    return {
      'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),'machine':platform.machine(),
      'lscpu':run_text(['lscpu']),'cpu_vendor':first.get('vendor_id'),'cpu_model':first.get('model name'),'cpu_flags':first.get('flags'),
      'uname':run_text(['uname','-a']),'os_release':pathlib.Path('/etc/os-release').read_text(errors='replace') if pathlib.Path('/etc/os-release').exists() else None,
      'numpy_config':cap(np.__config__.show),'numpy_runtime':cap(np.show_runtime) if hasattr(np,'show_runtime') else 'UNAVAILABLE',
      'env':{k:os.environ.get(k) for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS','OMP_DYNAMIC','OPENBLAS_VERBOSE','OPENBLAS_CORETYPE']},
    }

def cmd_child(a):
    _,x=load_a(pathlib.Path(a.compact)); k,w=solve(x)
    print(json.dumps({'regime':a.regime,'compact_sha':ahash(x),'k_sha':ahash(k),'w_sha':ahash(w),'runtime':runtime_meta()},sort_keys=True))

def cmd_worker(a):
    out=pathlib.Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    compact,x=load_a(pathlib.Path(a.compact))
    records={}
    for regime in REGIMES:
        reps=[]
        for rep in range(3):
            env=os.environ.copy(); env['OPENBLAS_VERBOSE']='2'; env['OPENBLAS_NUM_THREADS']='1'
            if regime=='native': env.pop('OPENBLAS_CORETYPE',None)
            else: env['OPENBLAS_CORETYPE']=regime
            cp=subprocess.run([sys.executable,str(pathlib.Path(__file__).resolve()),'child','--compact',str(compact),'--regime',regime],text=True,capture_output=True,env=env,timeout=600)
            lines=[z.strip() for z in cp.stdout.splitlines() if z.strip().startswith('{')]
            rec={'rep':rep,'returncode':cp.returncode,'stderr':cp.stderr[-12000:],'stdout_nonjson':'\n'.join(z for z in cp.stdout.splitlines() if not z.strip().startswith('{'))[-4000:]}
            if cp.returncode==0 and len(lines)==1: rec['result']=json.loads(lines[0])
            else: rec['error']='unsupported_or_failed_regime'
            reps.append(rec)
        ok=[r['result'] for r in reps if 'result' in r]
        records[regime]={'repeats':reps,'successful_repeats':len(ok),'internally_exact':bool(len(ok)==3 and len({(r['k_sha'],r['w_sha']) for r in ok})==1),'k_sha':ok[0]['k_sha'] if len(ok)==3 else None,'w_sha':ok[0]['w_sha'] if len(ok)==3 else None,'runtime':ok[0]['runtime'] if ok else None}
    rec={'experiment':'Exp073CH','version':'v0_1','worker':a.worker,'input_artifact_id':9841348367,'compact_sha':ahash(x),'regimes':records,'historical_a_w_sha':HIST_A_W_SHA,'historical_b_w_sha':HIST_B_W_SHA,'no_tolerance_used':True,'scientific_authority':False,'readiness_delta':[0,0]}
    (out/f'exp073ch_worker_{a.worker}_v0_1.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'worker':a.worker,'summary':{k:{q:v[q] for q in ['successful_repeats','internally_exact','k_sha','w_sha']} for k,v in records.items()}},indent=2,sort_keys=True))

def cmd_compare(a):
    root=pathlib.Path(a.root); files=sorted(root.rglob('exp073ch_worker_*_v0_1.json'))
    if len(files)!=4: raise AssertionError(('workers',len(files),[str(x) for x in files]))
    rs=[json.loads(p.read_text()) for p in files]; by={r['worker']:r for r in rs}
    if set(by)!={'R1','R2','R3','R4'}: raise AssertionError(sorted(by))
    reproduced=[]; within=False; successful={}; regime_cross={}
    for regime in REGIMES:
        vals=[]; successful[regime]=0
        for worker,r in sorted(by.items()):
            x=r['regimes'][regime]
            if x['successful_repeats']==3:
                successful[regime]+=1; vals.append((worker,x['k_sha'],x['w_sha']))
                if x['w_sha']==HIST_B_W_SHA: reproduced.append({'worker':worker,'regime':regime,'k_sha':x['k_sha'],'w_sha':x['w_sha']})
                if not x['internally_exact']: within=True
        regime_cross[regime]={'values':vals,'cross_exact':bool(vals and len({(x[1],x[2]) for x in vals})==1)}
        if vals and not regime_cross[regime]['cross_exact']: within=True
    exact_regime_values={regime:vals['values'][0][2] for regime,vals in regime_cross.items() if vals['values'] and vals['cross_exact']}
    if reproduced: status='EXP073CH_DIAG_HISTORICAL_B_SHA_REPRODUCED_BY_DISPATCH'
    elif within: status='EXP073CH_DIAG_WITHIN_REGIME_NONDETERMINISM'
    elif len(set(exact_regime_values.values()))>=2: status='EXP073CH_DIAG_DISPATCH_SENSITIVE_B_NOT_REPRODUCED'
    elif exact_regime_values and all(v==HIST_A_W_SHA for v in exact_regime_values.values()): status='EXP073CH_DIAG_ENVIRONMENT_DISPATCH_EXACT_STABLE_NOT_REPRODUCED'
    else: status='EXP073CH_DIAG_OTHER_EXACT_DIFFERENTIAL'
    out={'experiment':'Exp073CH','version':'v0_1','status':status,'successful_workers_by_regime':successful,'regime_cross':regime_cross,'exact_regime_w_shas':exact_regime_values,'historical_b_reproductions':reproduced,'expected_k_sha':EXPECTED_K_SHA,'historical_a_w_sha':HIST_A_W_SHA,'historical_b_w_sha':HIST_B_W_SHA,'exp073cf_terminal_fail_preserved':True,'no_tolerance_used':True,'scientific_authority':False,'readiness_delta':[0,0]}
    p=pathlib.Path(a.out_json); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('child'); p.add_argument('--compact',required=True); p.add_argument('--regime',required=True); p.set_defaults(fn=cmd_child)
    p=sp.add_parser('worker'); p.add_argument('--compact',required=True); p.add_argument('--worker',choices=['R1','R2','R3','R4'],required=True); p.add_argument('--out-dir',required=True); p.set_defaults(fn=cmd_worker)
    p=sp.add_parser('compare'); p.add_argument('--root',required=True); p.add_argument('--out-json',required=True); p.set_defaults(fn=cmd_compare)
    a=ap.parse_args(); a.fn(a)
if __name__=='__main__': main()
