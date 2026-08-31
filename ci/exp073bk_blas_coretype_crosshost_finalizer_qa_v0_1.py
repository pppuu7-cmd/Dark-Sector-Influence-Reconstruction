#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, subprocess, sys

EDGES=[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]
EXPECTED_A_SHA='a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e'
POLICIES={
    'default_t1':(None,'1'),
    'haswell_t1':('Haswell','1'),
    'default_t2':(None,'2'),
    'haswell_t2':('Haswell','2'),
}

def sha(x):
    import numpy as np
    y=np.ascontiguousarray(x,dtype='<f8')
    return hashlib.sha256(y.tobytes(order='C')).hexdigest()

def band_sums(x):
    import numpy as np
    out=np.empty((x.shape[0],39),dtype=np.float64)
    for j,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(x.shape[0],dtype=np.float64)
        for ell in range(lo,hi):
            acc += x[:,ell]
        out[:,j]=acc
    return out

def child(inp:str,outdir:str,policy:str):
    import numpy as np
    od=pathlib.Path(outdir); od.mkdir(parents=True,exist_ok=True)
    d=np.load(inp,allow_pickle=False)
    if 'A' not in d.files: raise AssertionError(d.files)
    A=np.ascontiguousarray(d['A'],dtype='<f8')
    if A.shape!=(39,12288) or not np.all(np.isfinite(A)) or sha(A)!=EXPECTED_A_SHA:
        raise AssertionError((A.shape,sha(A)))
    K=band_sums(A)
    W=np.ascontiguousarray(np.linalg.solve(K,A),dtype='<f8')
    WQ=band_sums(W)
    meta={
      'policy':policy,
      'openblas_coretype':os.environ.get('OPENBLAS_CORETYPE'),
      'openblas_num_threads':os.environ.get('OPENBLAS_NUM_THREADS'),
      'omp_num_threads':os.environ.get('OMP_NUM_THREADS'),
      'a_sha256':sha(A),
      'w_sha256':sha(W),
      'shape':[39,12288],
      'wq_identity_max_abs':float(np.max(np.abs(WQ-np.eye(39)))),
      'numpy_version':np.__version__,
    }
    np.save(od/f'W_{policy}.npy',W,allow_pickle=False)
    (od/f'{policy}.json').write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
    print(json.dumps(meta,sort_keys=True))

def cpu_model():
    for line in pathlib.Path('/proc/cpuinfo').read_text(errors='ignore').splitlines():
        if line.lower().startswith('model name'):
            return line.split(':',1)[1].strip()
    return 'unknown'

def parent(inp:str,outdir:str,replica:str):
    od=pathlib.Path(outdir); od.mkdir(parents=True,exist_ok=True)
    results={}
    for policy,(core,threads) in POLICIES.items():
        env=os.environ.copy()
        if core is None: env.pop('OPENBLAS_CORETYPE',None)
        else: env['OPENBLAS_CORETYPE']=core
        for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS']:
            env[k]=threads
        env['OMP_DYNAMIC']='FALSE'
        subprocess.run([sys.executable,__file__,'--child','--input',inp,'--outdir',str(od),'--policy',policy],check=True,env=env)
        results[policy]=json.loads((od/f'{policy}.json').read_text())
    rec={'experiment':'Exp073BK','replica':replica,'cpu_model':cpu_model(),'results':results,'scientific_readiness_increment':0,'draft_data_readiness_increment':0,'authority':False,'scientific_pass_claimed':False,'Exp073AQ_preserved_as_FAIL':True}
    (od/f'exp073bk_replica_{replica}.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(json.dumps(rec,indent=2,sort_keys=True))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--child',action='store_true')
    ap.add_argument('--input',required=True); ap.add_argument('--outdir',required=True)
    ap.add_argument('--policy'); ap.add_argument('--replica')
    a=ap.parse_args()
    if a.child: child(a.input,a.outdir,a.policy)
    else: parent(a.input,a.outdir,a.replica)
if __name__=='__main__': main()
