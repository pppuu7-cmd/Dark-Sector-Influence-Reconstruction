#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, pathlib
import numpy as np

EDGES=[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]
EXPECTED_A_SHA='a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e'
PROBE_COLS=[0,29,30,272,309,967,3035,6508,10821,12287]

def chash(x):
    y=np.ascontiguousarray(np.asarray(x,dtype='<f8'))
    return hashlib.sha256(y.tobytes(order='C')).hexdigest()

def build_k(A):
    K=np.empty((39,39),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(39,dtype=np.float64)
        for ell in range(lo,hi):
            for r in range(39):
                acc[r]=float(acc[r]+A[r,ell])
        K[:,ib]=acc
    return K

def factor_fixed(K):
    LU=np.array(K,dtype=np.float64,copy=True,order='C')
    p=list(range(39))
    for k in range(38):
        best=k; bestv=abs(float(LU[k,k]))
        for r in range(k+1,39):
            v=abs(float(LU[r,k]))
            if v>bestv:
                best=r; bestv=v
        if not np.isfinite(bestv) or bestv==0.0:
            raise AssertionError(('singular pivot',k,bestv))
        if best!=k:
            tmp=LU[k].copy(); LU[k]=LU[best]; LU[best]=tmp
            p[k],p[best]=p[best],p[k]
        pivot=float(LU[k,k])
        for i in range(k+1,39):
            f=float(LU[i,k]/pivot); LU[i,k]=f
            for j in range(k+1,39):
                LU[i,j]=float(LU[i,j]-f*LU[k,j])
    if not np.isfinite(LU[38,38]) or float(LU[38,38])==0.0:
        raise AssertionError(('singular final pivot',float(LU[38,38])))
    return LU,p

def solve_fixed(LU,p,A):
    # Deliberately scalar fixed-operation order; no BLAS/LAPACK solve.
    nrhs=A.shape[1]
    X=np.empty((39,nrhs),dtype=np.float64)
    for c in range(nrhs):
        y=[0.0]*39
        for i in range(39):
            s=float(A[p[i],c])
            for j in range(i):
                s=float(s-float(LU[i,j])*y[j])
            y[i]=s
        for ii in range(39):
            i=38-ii
            s=y[i]
            for j in range(i+1,39):
                s=float(s-float(LU[i,j])*float(X[j,c]))
            X[i,c]=float(s/float(LU[i,i]))
    return np.ascontiguousarray(X,dtype='<f8')

def band_sums_fixed(W):
    out=np.empty((39,39),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        for r in range(39):
            s=0.0
            for ell in range(lo,hi): s=float(s+float(W[r,ell]))
            out[r,ib]=s
    return out

def probe_residual(K,W,A):
    mx=0.0; ss=0.0; aa=0.0
    for c in PROBE_COLS:
        for i in range(39):
            s=0.0
            for j in range(39): s=float(s+float(K[i,j])*float(W[j,c]))
            d=float(s-float(A[i,c])); mx=max(mx,abs(d)); ss=float(ss+d*d); aa=float(aa+float(A[i,c])*float(A[i,c]))
    return {'probe_cols':PROBE_COLS,'max_abs':mx,'relative_l2':float((ss/aa)**0.5) if aa>0 else None}

def cpu_model():
    txt=pathlib.Path('/proc/cpuinfo').read_text(errors='ignore')
    for line in txt.splitlines():
        if line.lower().startswith('model name'): return line.split(':',1)[1].strip()
    return 'unknown'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--outdir',required=True); ap.add_argument('--replica',required=True); a=ap.parse_args()
    od=pathlib.Path(a.outdir); od.mkdir(parents=True,exist_ok=True)
    d=np.load(a.input,allow_pickle=False); assert 'A' in d.files,d.files
    A=np.ascontiguousarray(d['A'],dtype='<f8'); assert A.shape==(39,12288) and np.all(np.isfinite(A)); assert chash(A)==EXPECTED_A_SHA
    K=build_k(A); LU,p=factor_fixed(K); W=solve_fixed(LU,p,A)
    WQ=band_sums_fixed(W)
    ident_max=0.0
    for i in range(39):
        for j in range(39): ident_max=max(ident_max,abs(float(WQ[i,j])-(1.0 if i==j else 0.0)))
    out={'experiment':'Exp073BL','replica':a.replica,'cpu_model':cpu_model(),'a_sha256':chash(A),'w_sha256':chash(W),'shape':[39,12288],'pivot_permutation':p,'wq_identity_max_abs':ident_max,'probe_residual':probe_residual(K,W,A),'numpy_version':np.__version__,'thread_env':{k:os.environ.get(k) for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS','OMP_DYNAMIC']},'authority':False,'scientific_pass_claimed':False,'scientific_readiness_increment':0,'draft_data_readiness_increment':0,'Exp073AQ_preserved_as_FAIL':True}
    np.save(od/f'W_{a.replica}.npy',W,allow_pickle=False)
    (od/f'exp073bl_replica_{a.replica}.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
