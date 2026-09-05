#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, struct, subprocess
from pathlib import Path
import numpy as np
import pymaster as nmt
from astropy.io import fits

SCHEMA='dsir.exp073dy.ww_crossfield_saved_lu_exact_diagnostic.v0.1'
PASS='PASS_EXP073DY_SAVED_LU_CROSSFIELD_EXACT_V0_1'
LASTBIT='DIAG_EXP073DY_SAVED_LU_STILL_LASTBIT_MISMATCH'


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
    a=canon(a); b=canon(b)
    if np.array_equal(a,b): raise RuntimeError('synthetic masks collapsed')
    return a,b


def metrics(candidate,reference):
    c=np.asarray(candidate); r=np.asarray(reference); d=np.abs(c-r)
    return {'array_equal':bool(np.array_equal(c,r)),'sha_equal':sha_arr(c)==sha_arr(r),'max_abs_difference':float(np.max(d)),'nonzero_difference_count':int(np.count_nonzero(c!=r)),'finite':bool(np.all(np.isfinite(c)))}


def run(exe,inp,out,shape):
    p=subprocess.run([str(exe),str(inp),str(out)],check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if 'DSIR_OMP_TEAM=' not in p.stdout+'\n'+p.stderr: raise RuntimeError('missing OpenMP proof')
    expected=int(np.prod(shape))*8
    if out.stat().st_size!=expected: raise RuntimeError(f'bad output size {out.stat().st_size} != {expected}')
    return np.memmap(out,dtype='<f8',mode='r',shape=shape,order='C'),p.stdout.strip(),p.stderr.strip()


def write_control(path,mcm,edges,ncls,nl):
    x=canon(mcm); nr=ncls*nl
    if x.shape!=(nr,nr): raise RuntimeError('control mcm shape')
    with path.open('wb') as f:
        f.write(struct.pack('<iii',ncls,len(edges)-1,nl)); f.write(np.asarray(edges,dtype='<i4').tobytes()); f.write(x.tobytes(order='C'))


def write_saved_lu(path,mcm,lu,perm,edges,ncls,nl):
    x=canon(mcm); y=canon(lu); p=np.ascontiguousarray(np.asarray(perm,dtype='<i4').reshape(-1))
    nr=ncls*nl; nbr=ncls*(len(edges)-1)
    if x.shape!=(nr,nr): raise RuntimeError('mcm shape')
    if y.shape!=(nbr,nbr): raise RuntimeError(f'LU shape {y.shape} != {(nbr,nbr)}')
    if p.shape!=(nbr,): raise RuntimeError(f'perm shape {p.shape} != {(nbr,)}')
    if sorted(p.tolist())!=list(range(nbr)): raise RuntimeError('invalid permutation')
    with path.open('wb') as f:
        f.write(struct.pack('<iii',ncls,len(edges)-1,nl)); f.write(np.asarray(edges,dtype='<i4').tobytes()); f.write(x.tobytes(order='C')); f.write(y.tobytes(order='C')); f.write(p.tobytes(order='C'))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--control-exe',required=True); ap.add_argument('--saved-lu-exe',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--prereg-blob',required=True); args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    nside=16; nl=48; ncls=4; edges=np.array([0,6,12,18,24,30,36,42,48],dtype=np.int32); nb=len(edges)-1; shape=(ncls,nb,ncls,nl)

    s0,s1=masks(nside); f0=nmt.NmtField(s0,None,spin=2,lmax=nl-1,lmax_mask=nl-1); f1=nmt.NmtField(s1,None,spin=2,lmax=nl-1,lmax_mask=nl-1); b=nmt.NmtBin.from_edges(edges[:-1],edges[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,b)
    direct=canon(w.get_bandpower_windows()); direct_ee=canon(direct[0,:,0,:]); direct_mcm=canon(w.get_coupling_matrix())
    if direct.shape!=shape: raise RuntimeError(f'direct shape {direct.shape}')
    fp=out/'w01.fits'; w.write_to(str(fp))

    wr=nmt.NmtWorkspace(); wr.read_from(str(fp)); reloaded=canon(wr.get_bandpower_windows())
    reload_metrics=metrics(reloaded,direct)

    with fits.open(fp,mode='readonly',memmap=True,do_not_scale_image_data=True) as hdul:
        primary=canon(hdul['WSP_PRIMARY'].data)
        lu=canon(hdul['MCM_BINNED'].data)
        perm=np.ascontiguousarray(np.asarray(hdul['MCM_PERM'].data,dtype='<i4').reshape(-1))
    if not np.array_equal(primary,direct_mcm): raise RuntimeError('WSP_PRIMARY not exact direct MCM')

    control_in=out/'control.input.bin'; saved_in=out/'saved_lu.input.bin'; control_out=out/'control.full.bin'; saved_out=out/'saved_lu.full.bin'
    write_control(control_in,primary,edges,ncls,nl); write_saved_lu(saved_in,primary,lu,perm,edges,ncls,nl)
    control,cso,cse=run(Path(args.control_exe),control_in,control_out,shape); saved,sso,sse=run(Path(args.saved_lu_exe),saved_in,saved_out,shape)
    control_ee=canon(control[0,:,0,:]); saved_ee=canon(saved[0,:,0,:])
    cm=metrics(control,direct); cem=metrics(control_ee,direct_ee); sm=metrics(saved,direct); sem=metrics(saved_ee,direct_ee)

    saved_exact=(sm['array_equal'] and sm['sha_equal'] and sm['max_abs_difference']==0.0 and sem['array_equal'] and sem['sha_equal'] and sem['max_abs_difference']==0.0 and reload_metrics['array_equal'] and reload_metrics['sha_equal'])
    finite=sm['finite'] and sem['finite'] and cm['finite'] and cem['finite']
    token=PASS if saved_exact else (LASTBIT if finite else 'FAIL_EXP073DY_NONFINITE_OR_MALFORMED')
    rec={'schema':SCHEMA,'experiment':'Exp073DY','classification':'QUALIFIER_PASS' if saved_exact else 'DIAGNOSTIC_ONLY_PLUS_0_PLUS_0','token':token,'science_gate_scored':False,'ww_authority_created':False,'production_route_authorized':False,'accounting':'+0/+0','source_head':args.source_head,'prereg_blob':args.prereg_blob,'nside':nside,'nl':nl,'ncls':ncls,'band_edges':edges.tolist(),'full_shape':list(shape),'selected_shape':[nb,nl],'selected_semantics':'wins[0,:,0,:] = EE<-EE','workspace_reload_exact_direct':reload_metrics,'wsp_primary_exact_direct_mcm':True,'direct_full_sha256':sha_arr(direct),'direct_selected_ee_sha256':sha_arr(direct_ee),'workspace_fits_sha256':sha_file(fp),'mcm_binned_lu_shape':list(lu.shape),'mcm_perm_shape':list(perm.shape),'control_recomputed_lu':{'full':cm,'selected_ee':cem,'full_sha256':sha_file(control_out),'selected_ee_sha256':sha_arr(control_ee),'stdout':cso,'stderr':cse},'saved_lu_route':{'full':sm,'selected_ee':sem,'full_sha256':sha_file(saved_out),'selected_ee_sha256':sha_arr(saved_ee),'stdout':sso,'stderr':sse},'no_tolerance_rescue':True,'note':'MCM_BINNED is the LU-decomposed binned matrix stored by NaMaster; MCM_PERM is its saved GSL permutation. No re-binning or LU decomposition occurs in the saved-LU route.'}
    (out/'terminal_diagnostic_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(token)

if __name__=='__main__': main()
