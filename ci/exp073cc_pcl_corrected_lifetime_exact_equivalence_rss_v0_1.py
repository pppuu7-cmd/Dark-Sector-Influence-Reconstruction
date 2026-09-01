#!/usr/bin/env python3
from __future__ import annotations
import argparse, gc, hashlib, json
from pathlib import Path
import numpy as np
import healpy as hp
import pymaster as nmt

CASES=(64,128,256)

def chash(x):
    a=np.ascontiguousarray(x,dtype='<f8')
    return hashlib.sha256(a.tobytes(order='C')).hexdigest()

def lens_mask(nside):
    npix=12*nside*nside
    pix=np.arange(npix,dtype=np.int64)
    th,ph=hp.pix2ang(nside,pix)
    return ((th>0.31)&(th<2.67)&(ph>0.17)&(ph<5.91)).astype(np.float64)

def source_mask(nside):
    npix=12*nside*nside
    pix=np.arange(npix,dtype=np.int64)
    th,ph=hp.pix2ang(nside,pix)
    return (((np.sin(3.0*ph)+0.35*np.cos(2.0*th))>0.05)&(th>0.42)&(th<2.55)).astype(np.float64)

def simultaneous(nside):
    lmax=3*nside-1
    a=lens_mask(nside)
    b=source_mask(nside)
    fa=nmt.NmtField(a,None,spin=0,lmax=lmax,lmax_mask=lmax)
    fb=nmt.NmtField(b,None,spin=2,lmax=lmax,lmax_mask=lmax)
    aa=fa.get_mask_alms()
    ab=fb.get_mask_alms()
    return np.ascontiguousarray(hp.alm2cl(aa,ab,lmax=lmax),dtype='<f8')

def sequential(nside):
    lmax=3*nside-1
    a=lens_mask(nside)
    fa=nmt.NmtField(a,None,spin=0,lmax=lmax,lmax_mask=lmax)
    del a; gc.collect()
    aa=fa.get_mask_alms()
    del fa; gc.collect()
    b=source_mask(nside)
    fb=nmt.NmtField(b,None,spin=2,lmax=lmax,lmax_mask=lmax)
    del b; gc.collect()
    ab=fb.get_mask_alms()
    del fb; gc.collect()
    return np.ascontiguousarray(hp.alm2cl(aa,ab,lmax=lmax),dtype='<f8')

def run(mode,nside,out):
    x=simultaneous(nside) if mode=='simultaneous' else sequential(nside)
    assert x.shape==(3*nside,) and np.isfinite(x).all()
    np.save(out,x,allow_pickle=False)
    print(json.dumps({'experiment':'Exp073CC','mode':mode,'nside':nside,'shape':list(x.shape),'sha256':chash(x)},sort_keys=True))

def compare(root,out_json):
    root=Path(root); cases=[]; ok=True
    for nside in CASES:
        a=np.ascontiguousarray(np.load(root/f'sim_{nside}.npy',allow_pickle=False),dtype='<f8')
        b=np.ascontiguousarray(np.load(root/f'seq_{nside}.npy',allow_pickle=False),dtype='<f8')
        eq=bool(np.array_equal(a,b)); ha=chash(a); hb=chash(b)
        rec={'nside':nside,'shape_simultaneous':list(a.shape),'shape_sequential':list(b.shape),'array_equal':eq,'sha_simultaneous':ha,'sha_sequential':hb,'sha_equal':ha==hb,'finite_simultaneous':bool(np.isfinite(a).all()),'finite_sequential':bool(np.isfinite(b).all())}
        case_ok=(a.shape==b.shape==(3*nside,) and rec['finite_simultaneous'] and rec['finite_sequential'] and eq and ha==hb)
        rec['case_pass']=bool(case_ok); ok &= case_ok; cases.append(rec)
    status='CC_Q1_EXACT_EQUIVALENCE_PASS' if ok else 'CC_Q2_COMPLETE_EXACT_MISMATCH_FAIL'
    d={'experiment':'Exp073CC','status':status,'cases':cases,'science_gate_scored':False,'verified_delta':0.0,'draft_data_delta':0.0}
    Path(out_json).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
    print(json.dumps(d,indent=2,sort_keys=True))
    raise SystemExit(0 if ok else 2)

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('run'); p.add_argument('--mode',choices=['simultaneous','sequential'],required=True); p.add_argument('--nside',type=int,choices=CASES,required=True); p.add_argument('--out',required=True)
    p=sp.add_parser('compare'); p.add_argument('--root',required=True); p.add_argument('--out-json',required=True)
    a=ap.parse_args()
    if a.cmd=='run': run(a.mode,a.nside,a.out)
    else: compare(a.root,a.out_json)

if __name__=='__main__': main()
