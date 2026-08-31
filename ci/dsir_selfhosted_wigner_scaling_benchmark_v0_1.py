#!/usr/bin/env python3
from __future__ import annotations
import ctypes, hashlib, json, os, pathlib, subprocess, sys, time
import numpy as np

THREADS=[1,2,4,6,8,10]
LMAX=308
EDGES=np.array([0,30,60,90,120,150,180,210,240,272,309],dtype=np.int32)
NB=len(EDGES)-1
EXPECTED_HELPER_COMMIT='9fb0ecb79986cf5f542760377533a685745b31e2'
BW_PASS='BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS'

def sha(x):
    y=np.ascontiguousarray(np.asarray(x,dtype='<f8'))
    return hashlib.sha256(y.tobytes(order='C')).hexdigest()

def main():
    od=pathlib.Path('benchmark_wigner'); od.mkdir(exist_ok=True)
    nmtlib=os.environ['NMTLIB_PATH']
    helper='build/dsir_selfhosted_bw_helper.so'
    pathlib.Path('build').mkdir(exist_ok=True)
    cmd=['gcc','-O2','-shared','-fPIC','-fopenmp','-fno-fast-math','-fno-associative-math','-ffp-contract=off','-fno-tree-vectorize','ci/exp073bw_stream_general_coupling_v0_1.c','-o',helper,'-ldl','-lm']
    subprocess.run(cmd,check=True)
    lib=ctypes.CDLL(str(pathlib.Path(helper).resolve()))
    fn=lib.exp073bw_stream_compress
    fn.argtypes=[ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.POINTER(ctypes.c_int),ctypes.c_int,ctypes.c_int,ctypes.POINTER(ctypes.c_double)]
    fn.restype=ctypes.c_int
    ell=np.arange(LMAX+1,dtype=np.int64)
    pcl=np.ascontiguousarray(((ell%11)-5)/np.exp2(3+(ell%5)),dtype='<f8')
    records=[]; reference=None; refsha=None
    for t in THREADS:
        out=np.zeros((NB,LMAX+1),dtype='<f8',order='C')
        start=time.perf_counter()
        rc=fn(nmtlib.encode(),pcl.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),LMAX,0,2,0,2,EDGES.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),NB,t,out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
        wall=time.perf_counter()-start
        if rc!=0: raise RuntimeError((t,rc))
        h=sha(out)
        if reference is None:
            reference=out.copy(); refsha=h
        exact=bool(np.array_equal(reference,out) and h==refsha)
        records.append({'threads':t,'wall_seconds':wall,'speedup_vs_1':None,'sha256':h,'exact_vs_1':exact})
        print(f'threads={t} wall_seconds={wall:.6f} sha={h} exact_vs_1={exact}',flush=True)
    one=records[0]['wall_seconds']
    for r in records: r['speedup_vs_1']=one/r['wall_seconds']
    best=min(records,key=lambda r:r['wall_seconds'])
    threshold=best['wall_seconds']/0.97
    efficient=min((r for r in records if r['wall_seconds']<=threshold),key=lambda r:r['threads'])
    result={'benchmark':'DSIR_SELFHOSTED_WIGNER_SCALING_V0_1','classification':'NONCLASSIFYING_PERFORMANCE_QA','bw_status_bound':BW_PASS,'bw_helper_commit':EXPECTED_HELPER_COMMIT,'signature':[0,2,0,2],'lmax':LMAX,'edges':EDGES.tolist(),'pcl_sha256':sha(pcl),'nmtlib_path':nmtlib,'results':records,'all_thread_outputs_exact':all(r['exact_vs_1'] for r in records),'peak_threads':best['threads'],'peak_wall_seconds':best['wall_seconds'],'peak_speedup_vs_1':best['speedup_vs_1'],'recommended_threads_97pct_peak':efficient['threads'],'scientific_readiness_increment':0,'draft_data_readiness_increment':0}
    (od/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
