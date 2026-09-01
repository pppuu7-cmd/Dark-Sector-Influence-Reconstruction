#!/usr/bin/env python3
from __future__ import annotations
import argparse, gc, hashlib, json, os, shutil, sys
from pathlib import Path
import numpy as np
import healpy as hp
import pymaster as nmt

CASES=(64,128,256)


def sha_file(path:Path,chunk=8<<20):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(chunk),b''):
            h.update(b)
    return h.hexdigest()


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


def runtime_lmax(field,nside):
    got=int(field.ainfo_mask.lmax)
    expected=3*nside-1
    if got!=expected:
        raise RuntimeError(f'runtime ainfo_mask.lmax mismatch: got={got} expected={expected}')
    return got


def oracle(nside):
    a=lens_mask(nside)
    fa=nmt.NmtField(a,None,spin=0)
    pcl_lmax=runtime_lmax(fa,nside)
    aa=fa.get_mask_alms()
    del fa,a
    gc.collect()

    b=source_mask(nside)
    fb=nmt.NmtField(b,None,spin=2)
    if int(fb.ainfo_mask.lmax)!=pcl_lmax:
        raise RuntimeError('source/lens runtime lmax mismatch')
    ab=fb.get_mask_alms()
    del fb,b
    gc.collect()
    pcl=np.ascontiguousarray(hp.alm2cl(aa,ab,lmax=pcl_lmax),dtype='<f8')
    return pcl,{'pcl_lmax':pcl_lmax}


def atomic_spill_c16(path:Path,aa):
    if sys.byteorder!='little':
        raise RuntimeError('Exp073CE requires little-endian X64 storage semantics')
    arr=np.ascontiguousarray(aa,dtype='<c16')
    shape=tuple(arr.shape)
    dtype=arr.dtype.str
    sha=chash_c16(arr)
    expected_bytes=int(arr.size*arr.dtype.itemsize)
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.tmp')
    try:
        with tmp.open('wb') as f:
            arr.tofile(f)
            f.flush()
            os.fsync(f.fileno())
        if tmp.stat().st_size!=expected_bytes:
            raise RuntimeError('temporary spill size mismatch')
        os.replace(tmp,path)
        try:
            dfd=os.open(str(path.parent),os.O_RDONLY)
            try: os.fsync(dfd)
            finally: os.close(dfd)
        except OSError:
            pass
        if path.stat().st_size!=expected_bytes:
            raise RuntimeError('final spill size mismatch')
        file_sha=sha_file(path)
        if file_sha!=sha:
            raise RuntimeError('final spill SHA mismatch before release')
        return {'shape':shape,'dtype':dtype,'sha256':sha,'bytes':expected_bytes}
    finally:
        if tmp.exists(): tmp.unlink()


def spill_candidate(nside,spill_path):
    a=lens_mask(nside)
    fa=nmt.NmtField(a,None,spin=0)
    pcl_lmax=runtime_lmax(fa,nside)
    aa=fa.get_mask_alms()
    receipt=atomic_spill_c16(spill_path,aa)
    del aa,fa,a
    gc.collect()

    b=source_mask(nside)
    fb=nmt.NmtField(b,None,spin=2)
    if int(fb.ainfo_mask.lmax)!=pcl_lmax:
        raise RuntimeError('source/lens runtime lmax mismatch')
    ab=fb.get_mask_alms()
    del fb,b
    gc.collect()

    if spill_path.stat().st_size!=receipt['bytes'] or sha_file(spill_path)!=receipt['sha256']:
        raise RuntimeError('spill identity changed before reload')
    aa_reload=np.memmap(spill_path,mode='r',dtype='<c16',shape=receipt['shape'])
    if aa_reload.dtype.str!='<c16' or aa_reload.flags.writeable:
        raise RuntimeError('reload dtype/writeability contract failed')
    reload_sha=chash_c16(aa_reload)
    if reload_sha!=receipt['sha256']:
        raise RuntimeError('reloaded first-ALM SHA mismatch')
    pcl=np.ascontiguousarray(hp.alm2cl(aa_reload,ab,lmax=pcl_lmax),dtype='<f8')
    meta={'pcl_lmax':pcl_lmax,'alm_shape':list(receipt['shape']),'alm_dtype':receipt['dtype'],'alm_bytes':receipt['bytes'],'alm_pre_sha256':receipt['sha256'],'alm_reload_sha256':reload_sha,'alm_sha_equal':reload_sha==receipt['sha256'],'reload_writeable':bool(aa_reload.flags.writeable)}
    del aa_reload,ab
    gc.collect()
    return pcl,meta


def run_case(nside,root):
    root=Path(root)
    root.mkdir(parents=True,exist_ok=True)
    spill=root/f'first_mask_alm_{nside}.c16'
    try:
        o,om=oracle(nside)
        s,sm=spill_candidate(nside,spill)
        eq=bool(np.array_equal(o,s))
        ho=chash_f8(o); hs=chash_f8(s)
        case_ok=(o.shape==s.shape==(3*nside,) and np.isfinite(o).all() and np.isfinite(s).all() and om['pcl_lmax']==sm['pcl_lmax']==3*nside-1 and sm['alm_sha_equal'] and not sm['reload_writeable'] and eq and ho==hs)
        return {'nside':nside,'runtime_lmax_oracle':om['pcl_lmax'],'runtime_lmax_spill':sm['pcl_lmax'],'shape_oracle':list(o.shape),'shape_spill':list(s.shape),'array_equal':eq,'sha_oracle':ho,'sha_spill':hs,'sha_equal':ho==hs,'finite_oracle':bool(np.isfinite(o).all()),'finite_spill':bool(np.isfinite(s).all()),**sm,'case_pass':bool(case_ok)}
    finally:
        if spill.exists(): spill.unlink()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',required=True)
    ap.add_argument('--out-json',required=True)
    a=ap.parse_args()
    root=Path(a.root)
    if root.exists(): shutil.rmtree(root)
    cases=[]
    try:
        for nside in CASES:
            cases.append(run_case(nside,root))
        ok=all(c['case_pass'] for c in cases)
        status='CE_Q1_MEMORY_STABLE_EXACT_EQUIVALENCE_PASS' if ok else 'CE_Q2_COMPLETE_EXACT_MISMATCH_FAIL'
        d={'experiment':'Exp073CE','status':status,'cases':cases,'science_gate_scored':False,'verified_delta':0.0,'draft_data_delta':0.0}
        Path(a.out_json).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
        print(json.dumps(d,indent=2,sort_keys=True))
        raise SystemExit(0 if ok else 2)
    except SystemExit:
        raise
    except Exception as e:
        d={'experiment':'Exp073CE','status':'CE_Q3_INFRASTRUCTURE_INCOMPLETE','error_type':type(e).__name__,'error':str(e),'cases_completed':cases,'science_gate_scored':False,'verified_delta':0.0,'draft_data_delta':0.0}
        Path(a.out_json).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
        print(json.dumps(d,indent=2,sort_keys=True))
        raise

if __name__=='__main__':
    main()
