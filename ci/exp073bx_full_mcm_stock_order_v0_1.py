#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json, struct, subprocess, tempfile
from pathlib import Path
import healpy as hp
import numpy as np
import pymaster as nmt

NSIDE=16; L=48; LMAX=47; NCLS=2
EDGES=np.array([0,4,8,12,16,24,32,40,48],dtype=np.int32); NB=8

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
    if min(float(lens.min()),float(source.min()))<0: raise AssertionError('negative mask')
    if not np.all(np.isfinite(lens)) or not np.all(np.isfinite(source)): raise AssertionError('nonfinite mask')
    return lens,source

def emulate(exe,mcm):
    mcm=canon(mcm)
    if mcm.shape!=(NCLS*L,NCLS*L): raise AssertionError(('mcm shape',mcm.shape))
    with tempfile.TemporaryDirectory() as td:
        inp=Path(td)/'in.bin'; out=Path(td)/'out.bin'
        payload=struct.pack('<iii',NCLS,NB,L)+EDGES.astype('<i4',copy=False).tobytes(order='C')+mcm.tobytes(order='C')
        inp.write_bytes(payload); subprocess.run([exe,str(inp),str(out)],check=True)
        raw=out.read_bytes(); expected=NCLS*NB*NCLS*L*8
        if len(raw)!=expected: raise AssertionError(('output bytes',len(raw),expected))
        arr=np.frombuffer(raw,dtype='<f8').reshape(NCLS,NB,NCLS,L)
        return canon(arr)

def one(case,exe):
    lens,source=masks(case)
    f0=nmt.NmtField(lens,None,spin=0,lmax=LMAX,lmax_mask=LMAX)
    f2=nmt.NmtField(source,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
    b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f2,b)
    stock=canon(w.get_bandpower_windows())
    if stock.shape!=(NCLS,NB,NCLS,L): raise AssertionError(('stock',stock.shape))
    mcm=canon(w.get_coupling_matrix())
    emu=emulate(exe,mcm)
    return {
      'case':case,'shape':list(stock.shape),'dtype':stock.dtype.str,
      'stock_sha256':ahash(stock),'emulator_sha256':ahash(emu),
      'numpy_array_equal':bool(np.array_equal(stock,emu)),'sha_equal':ahash(stock)==ahash(emu),
      'max_abs_difference':float(np.max(np.abs(stock-emu))),
      'selected_te_array_equal':bool(np.array_equal(stock[0,:,0,:],emu[0,:,0,:])),
      'selected_te_stock_sha256':ahash(stock[0,:,0,:]),'selected_te_emulator_sha256':ahash(emu[0,:,0,:]),
      'mcm_sha256':ahash(mcm),
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--emulator',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    version=importlib.metadata.version('pymaster')
    if not (version=='2.7' or version.startswith('2.7.')): raise AssertionError(version)
    rows=[one(i,a.emulator) for i in range(3)]
    status='F1_EXACT_FULL_STOCK_ORDER_EQUIVALENCE' if all(r['numpy_array_equal'] and r['sha_equal'] for r in rows) else 'F2_FULL_STOCK_ORDER_MISMATCH'
    receipt={'schema':'dsir.exp073bx.full_mcm_stock_order.v0.1','status':status,'accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'pymaster_version':version,'synthetic':{'nside':NSIDE,'lmax':LMAX,'edges':EDGES.tolist(),'cases':3,'ncls':NCLS},'cases':rows,'historical_or_des_data_read':False,'no_tolerance_rescue':True,'operation_route':'export stock full unbinned MCM -> source-order full ncls=2 binning -> GSL LU invert -> GSL BLAS dgemm -> stock raw ordering'}
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n'); print(status); print(json.dumps(receipt,indent=2,sort_keys=True))
if __name__=='__main__': main()
