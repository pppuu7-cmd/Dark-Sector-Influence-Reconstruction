#!/usr/bin/env python3
from __future__ import annotations
import argparse, gc, hashlib, json
from pathlib import Path
import numpy as np
import healpy as hp
import pymaster as nmt

CASES=(64,128,256)

def chash_f8(x):
    a=np.ascontiguousarray(x,dtype='<f8')
    return hashlib.sha256(a.tobytes(order='C')).hexdigest()

def chash_c16(x):
    a=np.ascontiguousarray(x,dtype='<c16')
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

def sequential_oracle(nside):
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

def spill_candidate(nside,spill_path):
    lmax=3*nside-1
    a=lens_mask(nside)
    fa=nmt.NmtField(a,None,spin=0,lmax=lmax,lmax_mask=lmax)
    del a; gc.collect()
    aa=np.ascontiguousarray(fa.get_mask_alms(),dtype='<c16')
    del fa; gc.collect()
    pre_shape=aa.shape
    pre_dtype=aa.dtype.str
    pre_sha=chash_c16(aa)
    np.save(spill_path,aa,allow_pickle=False)
    del aa; gc.collect()

    b=source_mask(nside)
    fb=nmt.NmtField(b,None,spin=2,lmax=lmax,lmax_mask=lmax)
    del b; gc.collect()
    ab=fb.get_mask_alms()
    del fb; gc.collect()

    aa_reload=np.load(spill_path,mmap_mode='r',allow_pickle=False)
    reload_shape=aa_reload.shape
    reload_dtype=aa_reload.dtype.str
    reload_sha=chash_c16(aa_reload)
    identity=(pre_shape==reload_shape and pre_dtype==reload_dtype and pre_sha==reload_sha)
    if not identity:
        raise RuntimeError('saved/reloaded first-ALM exact identity failed')
    pcl=np.ascontiguousarray(hp.alm2cl(aa_reload,ab,lmax=lmax),dtype='<f8')
    receipt={'alm_pre_shape':list(pre_shape),'alm_reload_shape':list(reload_shape),'alm_pre_dtype':pre_dtype,'alm_reload_dtype':reload_dtype,'alm_pre_sha256':pre_sha,'alm_reload_sha256':reload_sha,'alm_sha_equal':pre_sha==reload_sha,'alm_exact_identity':identity}
    return pcl,receipt

def run(mode,nside,out,meta,spill_dir):
    if mode=='oracle':
        x=sequential_oracle(nside); rec={'experiment':'Exp073CD','mode':mode,'nside':nside}
    else:
        spill_dir=Path(spill_dir); spill_dir.mkdir(parents=True,exist_ok=True)
        x,srec=spill_candidate(nside,spill_dir/f'aa_{nside}.npy')
        rec={'experiment':'Exp073CD','mode':mode,'nside':nside,**srec}
    assert x.shape==(3*nside,) and np.isfinite(x).all()
    np.save(out,x,allow_pickle=False)
    rec.update({'shape':list(x.shape),'pcl_sha256':chash_f8(x),'finite':True})
    Path(meta).write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(json.dumps(rec,sort_keys=True))

def compare(root,out_json):
    root=Path(root); cases=[]; ok=True
    for nside in CASES:
        a=np.ascontiguousarray(np.load(root/f'oracle_{nside}.npy',allow_pickle=False),dtype='<f8')
        b=np.ascontiguousarray(np.load(root/f'spill_{nside}.npy',allow_pickle=False),dtype='<f8')
        sm=json.load(open(root/f'spill_meta_{nside}.json'))
        eq=bool(np.array_equal(a,b)); ha=chash_f8(a); hb=chash_f8(b)
        rec={'nside':nside,'shape_oracle':list(a.shape),'shape_spill':list(b.shape),'array_equal':eq,'sha_oracle':ha,'sha_spill':hb,'sha_equal':ha==hb,'finite_oracle':bool(np.isfinite(a).all()),'finite_spill':bool(np.isfinite(b).all()),'alm_exact_identity':bool(sm.get('alm_exact_identity')),'alm_pre_sha256':sm.get('alm_pre_sha256'),'alm_reload_sha256':sm.get('alm_reload_sha256'),'alm_sha_equal':bool(sm.get('alm_sha_equal'))}
        case_ok=(a.shape==b.shape==(3*nside,) and rec['finite_oracle'] and rec['finite_spill'] and rec['alm_exact_identity'] and rec['alm_sha_equal'] and eq and ha==hb)
        rec['case_pass']=bool(case_ok); ok &= case_ok; cases.append(rec)
    status='CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS' if ok else 'CD_Q2_COMPLETE_EXACT_MISMATCH_FAIL'
    d={'experiment':'Exp073CD','status':status,'cases':cases,'science_gate_scored':False,'verified_delta':0.0,'draft_data_delta':0.0}
    Path(out_json).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
    print(json.dumps(d,indent=2,sort_keys=True))
    raise SystemExit(0 if ok else 2)

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('run'); p.add_argument('--mode',choices=['oracle','spill'],required=True); p.add_argument('--nside',type=int,choices=CASES,required=True); p.add_argument('--out',required=True); p.add_argument('--meta',required=True); p.add_argument('--spill-dir',required=True)
    p=sp.add_parser('compare'); p.add_argument('--root',required=True); p.add_argument('--out-json',required=True)
    a=ap.parse_args()
    if a.cmd=='run': run(a.mode,a.nside,a.out,a.meta,a.spill_dir)
    else: compare(a.root,a.out_json)

if __name__=='__main__': main()
