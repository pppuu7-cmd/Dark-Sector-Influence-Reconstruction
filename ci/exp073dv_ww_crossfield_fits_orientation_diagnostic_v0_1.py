#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, struct, subprocess
from pathlib import Path
import numpy as np
import pymaster as nmt
from astropy.io import fits

SCHEMA='dsir.exp073dv.ww_crossfield_fits_orientation_diagnostic.v0.1'

def canon(a): return np.ascontiguousarray(np.asarray(a,dtype='<f8'))
def sha_arr(a): return hashlib.sha256(memoryview(canon(a)).cast('B')).hexdigest()
def sha_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def masks(nside):
    npix=12*nside*nside; p=np.arange(npix,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(np.float64); a*=1.0+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(np.float64); b*=1.0+(((p*19+2)%11)/11.0)
    assert not np.array_equal(a,b)
    return canon(a),canon(b)

def write_input(path,mcm,edges,ncls,nl):
    x=canon(mcm); nr=ncls*nl; assert x.shape==(nr,nr)
    with open(path,'wb') as f:
        f.write(struct.pack('<iii',ncls,len(edges)-1,nl))
        f.write(np.asarray(edges,dtype='<i4').tobytes())
        f.write(x.tobytes(order='C'))

def run(exe,inp,out,shape):
    p=subprocess.run([str(exe),str(inp),str(out)],check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if 'DSIR_OMP_TEAM=' not in p.stdout+'\n'+p.stderr: raise RuntimeError('missing OpenMP proof')
    a=np.memmap(out,dtype='<f8',mode='r',shape=shape,order='C')
    return a,p.stdout,p.stderr

def metrics(candidate,reference):
    c=np.asarray(candidate); r=np.asarray(reference)
    d=np.abs(c-r)
    return {'array_equal':bool(np.array_equal(c,r)),'sha_equal':sha_arr(c)==sha_arr(r),'max_abs_difference':float(np.max(d)),'nonzero_difference_count':int(np.count_nonzero(c!=r))}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--emulator',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--prereg-blob',required=True); a=ap.parse_args()
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    nside=16; nl=48; ncls=4; edges=np.array([0,6,12,18,24,30,36,42,48],dtype=np.int32); nb=8
    s0,s1=masks(nside); f0=nmt.NmtField(s0,None,spin=2,lmax=nl-1,lmax_mask=nl-1); f1=nmt.NmtField(s1,None,spin=2,lmax=nl-1,lmax_mask=nl-1)
    bins=nmt.NmtBin.from_edges(edges[:-1],edges[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,bins)
    direct_mcm=canon(w.get_coupling_matrix()); direct_window=canon(w.get_bandpower_windows()); direct_ee=canon(direct_window[0,:,0,:])
    fp=out/'w01.fits'; w.write_to(str(fp))
    with fits.open(fp,mode='readonly',memmap=True,do_not_scale_image_data=True) as hdul:
        raw=canon(hdul['WSP_PRIMARY'].data)
    raw_t=canon(raw.T)
    mcm_cmp={'fits_as_is_vs_direct':metrics(raw,direct_mcm),'fits_transpose_vs_direct':metrics(raw_t,direct_mcm),'direct_mcm_symmetric':bool(np.array_equal(direct_mcm,direct_mcm.T)),'fits_as_is_symmetric':bool(np.array_equal(raw,raw.T))}
    shape=(ncls,nb,ncls,nl); routes={}
    for name,m in [('direct_mcm',direct_mcm),('fits_as_is',raw),('fits_transpose',raw_t)]:
        inp=out/f'{name}.input.bin'; fout=out/f'{name}.full.bin'; write_input(inp,m,edges,ncls,nl); full,stdout,stderr=run(Path(a.emulator),inp,fout,shape); ee=canon(full[0,:,0,:]); routes[name]={'full':metrics(full,direct_window),'selected_ee':metrics(ee,direct_ee),'full_sha256':sha_file(fout),'selected_ee_sha256':sha_arr(ee),'stdout':stdout.strip(),'stderr':stderr.strip()}; del full
    direct_ok=routes['direct_mcm']['full']['array_equal'] and routes['direct_mcm']['full']['sha_equal'] and routes['direct_mcm']['selected_ee']['array_equal']
    asis_ok=mcm_cmp['fits_as_is_vs_direct']['array_equal'] and routes['fits_as_is']['full']['array_equal'] and routes['fits_as_is']['selected_ee']['array_equal']
    trans_ok=mcm_cmp['fits_transpose_vs_direct']['array_equal'] and routes['fits_transpose']['full']['array_equal'] and routes['fits_transpose']['selected_ee']['array_equal']
    if not direct_ok: token='DIAG_EXP073DV_DOWNSTREAM_ARITHMETIC_MISMATCH'
    elif asis_ok: token='DIAG_EXP073DV_FITS_AS_IS_EXACT'
    elif trans_ok: token='DIAG_EXP073DV_FITS_TRANSPOSE_REQUIRED'
    else: token='DIAG_EXP073DV_UNRESOLVED_INTERFACE_MISMATCH'
    rec={'schema':SCHEMA,'experiment':'Exp073DV','classification':'DIAGNOSTIC_ONLY_PLUS_0_PLUS_0','token':token,'science_gate_scored':False,'ww_authority_created':False,'home_execution_authorized':False,'source_head':a.source_head,'prereg_blob':a.prereg_blob,'nside':nside,'nl':nl,'ncls':ncls,'band_edges':edges.tolist(),'full_shape':list(shape),'selected_shape':[nb,nl],'selected_semantics':'wins[0,:,0,:] = EE<-EE','direct_mcm_sha256':sha_arr(direct_mcm),'fits_as_is_sha256':sha_arr(raw),'fits_transpose_sha256':sha_arr(raw_t),'direct_full_sha256':sha_arr(direct_window),'direct_selected_ee_sha256':sha_arr(direct_ee),'mcm_comparisons':mcm_cmp,'routes':routes,'no_tolerance_rescue':True,'production_materialization_authorized':False,'note':'get_coupling_matrix materialization is diagnostic-only at NSIDE=16 and is forbidden as a production route'}
    (out/'terminal_diagnostic_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(token)

if __name__=='__main__': main()
