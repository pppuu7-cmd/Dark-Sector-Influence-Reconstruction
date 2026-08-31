#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path
import numpy as np
import healpy as hp
import pymaster as nmt

EDGES=np.array([0,4,8,16,24,32,48],dtype=np.int64)
NSIDE=16
L=3*NSIDE

def chash(a):
    x=np.ascontiguousarray(a,dtype='<f8')
    return hashlib.sha256(x.tobytes()).hexdigest()

def compress_general(G):
    l=G.shape[1]
    A=np.empty((len(EDGES)-1,l),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(l,dtype=np.float64)
        for ell in range(int(lo),int(hi)):
            acc += G[ell]
        A[ib]=acc/float(hi-lo)
    return np.ascontiguousarray(A,dtype='<f8')

def k_from_a(A):
    nb=len(EDGES)-1
    K=np.empty((nb,nb),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(nb,dtype=np.float64)
        for ell in range(int(lo),int(hi)):
            acc += A[:,ell]
        K[:,ib]=acc
    return K

def deterministic_masks():
    npix=12*NSIDE*NSIDE
    th,ph=hp.pix2ang(NSIDE,np.arange(npix))
    m0=((th<2.35)&(ph>0.20)&(ph<5.85)).astype(float)
    m2=((th<2.10)&(ph>0.35)&(ph<5.55)).astype(float)
    return m0,m2

def one_window():
    m0,m2=deterministic_masks()
    f0=nmt.NmtField(m0,None,spin=0,lmax=L-1,lmax_mask=L-1)
    f2=nmt.NmtField(m2,None,spin=2,lmax=L-1,lmax_mask=L-1)
    pcl=hp.alm2cl(f0.get_mask_alms(),f2.get_mask_alms(),lmax=L-1)
    G=nmt.get_general_coupling_matrix(pcl,0,2,0,2)
    A=compress_general(G)
    W=np.linalg.solve(k_from_a(A),A)
    return np.ascontiguousarray(W,dtype='<f8')

def stock_window():
    m0,m2=deterministic_masks()
    f0=nmt.NmtField(m0,None,spin=0,lmax=L-1,lmax_mask=L-1)
    f2=nmt.NmtField(m2,None,spin=2,lmax=L-1,lmax_mask=L-1)
    b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f2,b)
    return np.ascontiguousarray(w.get_bandpower_windows()[0,:,0,:],dtype='<f8')

def child(path):
    np.save(path,one_window(),allow_pickle=False)

def main():
    if len(sys.argv)==3 and sys.argv[1]=='--child':
        child(Path(sys.argv[2])); return
    env=os.environ.copy()
    for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS']:
        env[k]='2'
    env['OMP_DYNAMIC']='FALSE'
    with tempfile.TemporaryDirectory() as td:
        pa=Path(td)/'a.npy'; pb=Path(td)/'b.npy'
        subprocess.run([sys.executable,__file__,'--child',str(pa)],check=True,env=env)
        subprocess.run([sys.executable,__file__,'--child',str(pb)],check=True,env=env)
        a=np.load(pa,allow_pickle=False); b=np.load(pb,allow_pickle=False)
    ref=stock_window()
    exact=bool(np.array_equal(a,b))
    max_abs=float(max(np.max(np.abs(a-ref)),np.max(np.abs(b-ref))))
    status='BI_Q1_PARALLEL_EXACT_QA_PASS' if exact and max_abs<1e-12 else 'BI_Q2_PARALLEL_EXACT_QA_FAIL'
    out={'experiment':'Exp073BI','status':status,'thread_policy':2,'shape':list(a.shape),'sha_a':chash(a),'sha_b':chash(b),'array_equal':exact,'stock_reference_max_abs':max_abs,'synthetic_threshold':1e-12,'scientific_readiness_increment':0,'draft_data_readiness_increment':0}
    Path('data/derived/g7').mkdir(parents=True,exist_ok=True)
    Path('data/derived/g7/exp073bi_parallel_execution_qa_v0_1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if status!='BI_Q1_PARALLEL_EXACT_QA_PASS':
        raise SystemExit(2)

if __name__=='__main__': main()
