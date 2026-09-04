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
from pymaster import nmtlib as lib

NSIDE=16
L=48
LMAX=47
EDGES=np.array([0,4,8,12,16,24,32,40,48],dtype=np.int64)
NB=8
NCLS=2


def canon(x):
    return np.ascontiguousarray(np.asarray(x,dtype='<f8'))


def ahash(x):
    a=canon(x)
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def masks(case):
    npix=hp.nside2npix(NSIDE)
    theta,phi=hp.pix2ang(NSIDE,np.arange(npix),nest=False)
    if case==0:
        lens=(0.65+0.25*np.cos(theta)+0.07*np.sin(2*phi))*((theta>0.35)&(theta<2.72)&(phi>0.22)&(phi<5.91))
        source=(0.72+0.16*np.sin(theta)*np.cos(phi)+0.05*np.cos(3*phi))*((theta>0.27)&(theta<2.81)&(phi>0.31)&(phi<5.83))
    elif case==1:
        lens=(0.58+0.19*np.sin(theta)+0.08*np.cos(3*phi))*((theta>0.44)&(theta<2.60)&(phi>0.41)&(phi<5.64))
        source=(0.69+0.17*np.cos(theta)+0.06*np.sin(4*phi))*((theta>0.32)&(theta<2.74)&(phi>0.18)&(phi<5.72))
    elif case==2:
        lens=(0.61+0.14*np.cos(2*theta)+0.09*np.sin(phi))*((theta>0.28)&(theta<2.79)&(phi>0.37)&(phi<5.77))
        source=(0.66+0.21*np.sin(theta)*np.sin(2*phi)+0.04*np.cos(5*phi))*((theta>0.39)&(theta<2.67)&(phi>0.25)&(phi<5.88))
    else:
        raise ValueError(case)
    lens=canon(lens); source=canon(source)
    for x in (lens,source):
        if not np.all(np.isfinite(x)) or np.min(x)<0:
            raise AssertionError('invalid synthetic mask')
    return lens,source


def one(case):
    lens,source=masks(case)
    f0=nmt.NmtField(lens,None,spin=0,lmax=LMAX,lmax_mask=LMAX)
    f2=nmt.NmtField(source,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
    b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:])
    w=nmt.NmtWorkspace()
    w.compute_coupling_matrix(f0,f2,b)
    wrapper=canon(w.get_bandpower_windows())
    if wrapper.shape!=(NCLS,NB,NCLS,L):
        raise AssertionError(('wrapper shape',wrapper.shape))
    size=NCLS*NB*NCLS*L
    raw=np.asarray(lib.get_bandpower_windows(w.wsp,size))
    if raw.size!=size:
        raise AssertionError(('raw size',raw.size,size))
    direct=canon(np.transpose(raw.reshape([NB,NCLS,L,NCLS]),axes=[1,0,3,2]))
    if direct.shape!=wrapper.shape:
        raise AssertionError(('direct shape',direct.shape))
    return {
        'case':case,
        'wrapper_sha256':ahash(wrapper),
        'direct_raw_reshape_sha256':ahash(direct),
        'numpy_array_equal':bool(np.array_equal(wrapper,direct)),
        'sha_equal':ahash(wrapper)==ahash(direct),
        'max_abs_difference':float(np.max(np.abs(wrapper-direct))),
        'shape':list(wrapper.shape),
        'dtype':wrapper.dtype.str,
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); a=ap.parse_args()
    version=importlib.metadata.version('pymaster')
    if not (version=='2.7' or version.startswith('2.7.')):
        raise AssertionError(('pymaster',version))
    rows=[one(i) for i in range(3)]
    if all(r['numpy_array_equal'] and r['sha_equal'] for r in rows):
        status='R1_EXACT_WRAPPER_RAW_LAYOUT_EQUIVALENCE'
    else:
        status='R2_WRAPPER_RAW_LAYOUT_MISMATCH'
    out={
      'schema':'dsir.exp073bv.stock_wrapper_raw_layout_equivalence.v0.1',
      'status':status,
      'accounting':'+0/+0',
      'science_gate_scored':False,
      'wm_s3_authority_created':False,
      'pymaster_version':version,
      'synthetic':{'nside':NSIDE,'lmax':LMAX,'edges':EDGES.tolist(),'cases':3},
      'cases':rows,
      'historical_or_des_data_read':False,
      'interpretation':{
        'R1':'public Python wrapper is an exact reshape/transpose of the stock C/SWIG buffer for all frozen cases; the earlier Q2 discrepancy lies downstream of replacing the stock C/GSL computation, not in wrapper layout',
        'R2':'wrapper/raw-layout equivalence failed; inspect wrapper/runtime lineage before any emulator work',
      }
    }
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(status); print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
