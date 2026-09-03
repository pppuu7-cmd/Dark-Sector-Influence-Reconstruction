#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path

import healpy as hp
import numpy as np
import pymaster as nmt

NSIDE=16
L=48
LMAX=47
EDGES=np.array([0,4,8,12,16,24,32,40,48],dtype=np.int64)
NB=8


def canon(x):
    return np.ascontiguousarray(np.asarray(x,dtype='<f8'))


def ahash(x):
    a=canon(x)
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def compress_general(G):
    if G.shape!=(L,L):
        raise AssertionError(('general shape',G.shape))
    A=np.empty((NB,L),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(L,dtype=np.float64)
        for ell in range(int(lo),int(hi)):
            acc += G[ell]
        A[ib]=acc/float(hi-lo)
    return canon(A)


def k_from_a(A):
    K=np.empty((NB,NB),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(NB,dtype=np.float64)
        for ell in range(int(lo),int(hi)):
            acc += A[:,ell]
        K[:,ib]=acc
    return K


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',required=True)
    a=ap.parse_args()

    version=importlib.metadata.version('pymaster')
    if not (version=='2.7' or version.startswith('2.7.')):
        raise AssertionError(('pymaster',version))

    npix=hp.nside2npix(NSIDE)
    theta,phi=hp.pix2ang(NSIDE,np.arange(npix),nest=False)
    lens=(0.65+0.25*np.cos(theta)+0.07*np.sin(2*phi))
    lens*=((theta>0.35)&(theta<2.72)&(phi>0.22)&(phi<5.91))
    source=(0.72+0.16*np.sin(theta)*np.cos(phi)+0.05*np.cos(3*phi))
    source*=((theta>0.27)&(theta<2.81)&(phi>0.31)&(phi<5.83))
    lens=canon(lens)
    source=canon(source)
    if not np.all(np.isfinite(lens)) or not np.all(np.isfinite(source)) or np.min(lens)<0 or np.min(source)<0:
        raise AssertionError('invalid synthetic masks')

    f0=nmt.NmtField(lens,None,spin=0,lmax=LMAX,lmax_mask=LMAX)
    f2=nmt.NmtField(source,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
    b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:])
    w=nmt.NmtWorkspace()
    w.compute_coupling_matrix(f0,f2,b)
    full=np.asarray(w.get_bandpower_windows())
    if full.shape!=(2,NB,2,L):
        raise AssertionError(('stock full shape',full.shape))
    stock=canon(full[0,:,0,:])

    aa=f0.get_mask_alms()
    ab=f2.get_mask_alms()
    pcl=canon(hp.alm2cl(aa,ab,lmax=LMAX))
    if pcl.shape!=(L,) or not np.all(np.isfinite(pcl)):
        raise AssertionError(('pcl',pcl.shape))
    G=nmt.get_general_coupling_matrix(pcl,0,2,0,2)
    A=compress_general(G)
    K=k_from_a(A)
    low=canon(np.linalg.solve(K,A))
    if low.shape!=(NB,L) or not np.all(np.isfinite(low)):
        raise AssertionError(('low',low.shape))

    exact_array=bool(np.array_equal(stock,low))
    stock_sha=ahash(stock); low_sha=ahash(low)
    exact_sha=stock_sha==low_sha
    max_abs=float(np.max(np.abs(stock-low)))
    if exact_array and exact_sha:
        status='Q1_EXACT_SELECTED_TE_EQUIVALENCE'
    elif max_abs<=1e-12:
        status='Q2_NUMERIC_ONLY_SELECTED_TE_EQUIVALENCE'
    else:
        status='Q3_SELECTED_TE_SEMANTIC_MISMATCH'

    out={
        'schema':'dsir.exp073bu.support_selected_te_semantic_equivalence.v0.1',
        'status':status,
        'accounting':'+0/+0',
        'science_gate_scored':False,
        'wm_s3_authority_created':False,
        'pymaster_version':version,
        'synthetic':{'nside':NSIDE,'lmax':LMAX,'edges':EDGES.tolist(),'mask_kind':'deterministic_nontrivial_weighted'},
        'stock_full_shape':list(full.shape),
        'selected_shape':list(stock.shape),
        'selected_dtype':stock.dtype.str,
        'stock_selected_sha256':stock_sha,
        'low_memory_selected_sha256':low_sha,
        'numpy_array_equal':exact_array,
        'sha_equal':exact_sha,
        'max_abs_difference':max_abs,
        'q2_threshold_only':1e-12,
        'q2_does_not_authorize_scientific_runtime_substitution':True,
        'historical_or_des_data_read':False,
    }
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(status)
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
