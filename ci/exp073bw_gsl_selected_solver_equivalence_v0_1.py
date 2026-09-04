#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, importlib.metadata, json, struct, subprocess, tempfile
from pathlib import Path
import healpy as hp
import numpy as np
import pymaster as nmt

NSIDE=16; L=48; LMAX=47
EDGES=np.array([0,4,8,12,16,24,32,40,48],dtype=np.int64); NB=8

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def ahash(x):
    a=canon(x); return hashlib.sha256(memoryview(a).cast('B')).hexdigest()

def masks(case):
    npix=hp.nside2npix(NSIDE); theta,phi=hp.pix2ang(NSIDE,np.arange(npix),nest=False)
    if case==0:
        lens=(0.65+0.25*np.cos(theta)+0.07*np.sin(2*phi))*((theta>0.35)&(theta<2.72)&(phi>0.22)&(phi<5.91))
        source=(0.72+0.16*np.sin(theta)*np.cos(phi)+0.05*np.cos(3*phi))*((theta>0.27)&(theta<2.81)&(phi>0.31)&(phi<5.83))
    elif case==1:
        lens=(0.58+0.19*np.sin(theta)+0.08*np.cos(3*phi))*((theta>0.44)&(theta<2.60)&(phi>0.41)&(phi<5.64))
        source=(0.69+0.17*np.cos(theta)+0.06*np.sin(4*phi))*((theta>0.32)&(theta<2.74)&(phi>0.18)&(phi<5.72))
    elif case==2:
        lens=(0.61+0.14*np.cos(2*theta)+0.09*np.sin(phi))*((theta>0.28)&(theta<2.79)&(phi>0.37)&(phi<5.77))
        source=(0.66+0.21*np.sin(theta)*np.sin(2*phi)+0.04*np.cos(5*phi))*((theta>0.39)&(theta<2.67)&(phi>0.25)&(phi<5.88))
    else: raise ValueError(case)
    lens=canon(lens); source=canon(source)
    if min(float(lens.min()),float(source.min()))<0 or not np.all(np.isfinite(lens)) or not np.all(np.isfinite(source)): raise AssertionError('mask')
    return lens,source

def compress_general(G):
    if G.shape!=(L,L): raise AssertionError(G.shape)
    A=np.empty((NB,L),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(L,dtype=np.float64)
        for ell in range(int(lo),int(hi)): acc += G[ell]
        A[ib]=acc/float(hi-lo)
    return canon(A)

def k_from_a(A):
    K=np.empty((NB,NB),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(NB,dtype=np.float64)
        for ell in range(int(lo),int(hi)): acc += A[:,ell]
        K[:,ib]=acc
    return canon(K)

def gsl_solve(solver,K,A):
    with tempfile.TemporaryDirectory() as td:
        inp=Path(td)/'in.bin'; out=Path(td)/'out.bin'
        inp.write_bytes(struct.pack('<ii',NB,L)+canon(K).tobytes(order='C')+canon(A).tobytes(order='C'))
        subprocess.run([solver,str(inp),str(out)],check=True)
        raw=out.read_bytes()
        if len(raw)!=NB*L*8: raise AssertionError(('solver bytes',len(raw)))
        return canon(np.frombuffer(raw,dtype='<f8').reshape(NB,L))

def one(case,solver):
    lens,source=masks(case)
    f0=nmt.NmtField(lens,None,spin=0,lmax=LMAX,lmax_mask=LMAX); f2=nmt.NmtField(source,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
    b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f2,b)
    full=np.asarray(w.get_bandpower_windows());
    if full.shape!=(2,NB,2,L): raise AssertionError(full.shape)
    stock=canon(full[0,:,0,:])
    pcl=canon(hp.alm2cl(f0.get_mask_alms(),f2.get_mask_alms(),lmax=LMAX))
    G=nmt.get_general_coupling_matrix(pcl,0,2,0,2); A=compress_general(G); K=k_from_a(A)
    gsl=canon(gsl_solve(solver,K,A)); numpy=canon(np.linalg.solve(K,A))
    return {
      'case':case,'shape':list(stock.shape),'dtype':stock.dtype.str,
      'stock_sha256':ahash(stock),'gsl_selected_sha256':ahash(gsl),'numpy_selected_sha256':ahash(numpy),
      'stock_vs_gsl_array_equal':bool(np.array_equal(stock,gsl)),'stock_vs_gsl_sha_equal':ahash(stock)==ahash(gsl),
      'stock_vs_gsl_max_abs_difference':float(np.max(np.abs(stock-gsl))),
      'stock_vs_numpy_max_abs_difference':float(np.max(np.abs(stock-numpy))),
      'gsl_vs_numpy_array_equal':bool(np.array_equal(gsl,numpy)),
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--solver',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    version=importlib.metadata.version('pymaster');
    if not (version=='2.7' or version.startswith('2.7.')): raise AssertionError(version)
    rows=[one(i,a.solver) for i in range(3)]
    status='G1_EXACT_SELECTED_GSL_EQUIVALENCE' if all(r['stock_vs_gsl_array_equal'] and r['stock_vs_gsl_sha_equal'] for r in rows) else 'G2_SELECTED_CONSTRUCTION_NOT_EXACT'
    receipt={'schema':'dsir.exp073bw.gsl_selected_solver_equivalence.v0.1','status':status,'accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'pymaster_version':version,'gsl_solver':'gsl_linalg_LU_decomp + gsl_linalg_LU_solve, one frozen RHS column at a time','synthetic':{'nside':NSIDE,'lmax':LMAX,'edges':EDGES.tolist(),'cases':3},'cases':rows,'historical_or_des_data_read':False,'no_tolerance_rescue':True}
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n'); print(status); print(json.dumps(receipt,indent=2,sort_keys=True))
if __name__=='__main__': main()
