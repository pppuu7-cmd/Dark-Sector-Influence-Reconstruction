#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, struct, subprocess
from pathlib import Path
import numpy as np
import pymaster as nmt
from astropy.io import fits

SCHEMA='dsir.exp073ea.ww_crossfield_serialization_state_exactness.v0.1'
PASS='PASS_EXP073EA_SAVED_LU_EXACT_OFFICIAL_RELOAD_STATE_V0_1'

def canon(a): return np.ascontiguousarray(np.asarray(a,dtype='<f8'))
def sha_arr(a): return hashlib.sha256(memoryview(canon(a)).cast('B')).hexdigest()
def metrics(a,b):
    x=np.asarray(a); y=np.asarray(b); d=np.abs(x-y)
    return {'array_equal':bool(np.array_equal(x,y)),'sha_equal':sha_arr(x)==sha_arr(y),'max_abs_difference':float(np.max(d)),'nonzero_difference_count':int(np.count_nonzero(x!=y)),'finite':bool(np.all(np.isfinite(x)) and np.all(np.isfinite(y)))}
def masks(nside):
    npix=12*nside*nside; p=np.arange(npix,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(np.float64); a*=1.0+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(np.float64); b*=1.0+(((p*19+2)%11)/11.0)
    a=canon(a); b=canon(b); assert not np.array_equal(a,b); return a,b
def ext(path,name,dtype='<f8'):
    with fits.open(path,mode='readonly',memmap=True,do_not_scale_image_data=True) as h:
        if dtype=='<i4': return np.ascontiguousarray(np.asarray(h[name].data,dtype='<i4').reshape(-1))
        return canon(h[name].data)
def sha_i4(a): return hashlib.sha256(memoryview(np.ascontiguousarray(np.asarray(a,dtype='<i4'))).cast('B')).hexdigest()
def write_saved(path,mcm,lu,perm,edges,ncls,nl):
    nr=ncls*nl; nbr=ncls*(len(edges)-1); m=canon(mcm); l=canon(lu); p=np.ascontiguousarray(np.asarray(perm,dtype='<i4').reshape(-1))
    assert m.shape==(nr,nr) and l.shape==(nbr,nbr) and p.shape==(nbr,) and sorted(p.tolist())==list(range(nbr))
    with path.open('wb') as f:
        f.write(struct.pack('<iii',ncls,len(edges)-1,nl)); f.write(np.asarray(edges,dtype='<i4').tobytes()); f.write(m.tobytes()); f.write(l.tobytes()); f.write(p.tobytes())
def run(exe,inp,out,shape):
    p=subprocess.run([str(exe),str(inp),str(out)],check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    assert 'DSIR_OMP_TEAM=' in p.stdout+'\n'+p.stderr
    assert out.stat().st_size==int(np.prod(shape))*8
    return np.memmap(out,dtype='<f8',mode='r',shape=shape,order='C')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--saved-lu-exe',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--prereg-blob',required=True); a=ap.parse_args()
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    nside=16; nl=48; ncls=4; edges=np.array([0,6,12,18,24,30,36,42,48],dtype=np.int32); nb=8; shape=(4,8,4,48)
    s0,s1=masks(nside); f0=nmt.NmtField(s0,None,spin=2,lmax=nl-1,lmax_mask=nl-1); f1=nmt.NmtField(s1,None,spin=2,lmax=nl-1,lmax_mask=nl-1); b=nmt.NmtBin.from_edges(edges[:-1],edges[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,b)
    pre=out/'pre.fits'; post=out/'post.fits'; w.write_to(str(pre))
    d1=canon(w.get_bandpower_windows()); d2=canon(w.get_bandpower_windows()); w.write_to(str(post))
    wr=nmt.NmtWorkspace(); wr.read_from(str(pre)); rp1=canon(wr.get_bandpower_windows()); rp2=canon(wr.get_bandpower_windows())
    wr2=nmt.NmtWorkspace(); wr2.read_from(str(post)); rpost=canon(wr2.get_bandpower_windows())
    pre_m=ext(pre,'WSP_PRIMARY'); pre_lu=ext(pre,'MCM_BINNED'); pre_p=ext(pre,'MCM_PERM','<i4'); post_m=ext(post,'WSP_PRIMARY'); post_lu=ext(post,'MCM_BINNED'); post_p=ext(post,'MCM_PERM','<i4')
    inp=out/'saved.input.bin'; fout=out/'saved.full.bin'; write_saved(inp,pre_m,pre_lu,pre_p,edges,ncls,nl); saved=run(Path(a.saved_lu_exe),inp,fout,shape); saved_ee=canon(saved[0,:,0,:]); rp1_ee=canon(rp1[0,:,0,:]); d1_ee=canon(d1[0,:,0,:])
    num_ext_same=bool(np.array_equal(pre_m,post_m) and np.array_equal(pre_lu,post_lu) and np.array_equal(pre_p,post_p))
    direct_rep=metrics(d1,d2); reload_rep=metrics(rp1,rp2); prepost_reload=metrics(rp1,rpost); saved_reload=metrics(saved,rp1); saved_reload_ee=metrics(saved_ee,rp1_ee); direct_reload=metrics(d1,rp1); direct_reload_ee=metrics(d1_ee,rp1_ee)
    saved_reload_exact=saved_reload['array_equal'] and saved_reload['sha_equal'] and saved_reload['max_abs_difference']==0.0 and saved_reload_ee['array_equal'] and saved_reload_ee['sha_equal'] and saved_reload_ee['max_abs_difference']==0.0
    if not direct_rep['array_equal'] or not reload_rep['array_equal']:
        token='DIAG_EXP073EA_INPROCESS_NONREPEATABILITY_V0_1'
    elif not num_ext_same:
        token='DIAG_EXP073EA_SERIALIZATION_NUMERICAL_STATE_MUTATES_V0_1'
    elif prepost_reload['array_equal'] and saved_reload_exact:
        token=PASS
    elif prepost_reload['array_equal']:
        token='DIAG_EXP073EA_RELOAD_STATE_EXACT_BUT_SAVED_LU_MISMATCH_V0_1'
    else:
        token='DIAG_EXP073EA_UNRESOLVED_V0_1'
    rec={'schema':SCHEMA,'experiment':'Exp073EA','classification':'QUALIFIER_PASS' if token==PASS else 'DIAGNOSTIC_ONLY_PLUS_0_PLUS_0','token':token,'science_gate_scored':False,'ww_authority_created':False,'production_route_authorized':False,'accounting':'+0/+0','source_head':a.source_head,'prereg_blob':a.prereg_blob,'nside':nside,'nl':nl,'ncls':ncls,'band_edges':edges.tolist(),'full_shape':list(shape),'selected_shape':[nb,nl],'direct_repeatability':direct_rep,'reload_repeatability':reload_rep,'pre_post_reload':prepost_reload,'saved_lu_vs_reload_pre':saved_reload,'saved_lu_selected_ee_vs_reload_pre':saved_reload_ee,'direct_vs_reload_pre':direct_reload,'direct_selected_ee_vs_reload_pre':direct_reload_ee,'serialized_numerical_extensions_equal_pre_post':num_ext_same,'pre_post_extensions':{'wsp_primary_equal':bool(np.array_equal(pre_m,post_m)),'mcm_binned_equal':bool(np.array_equal(pre_lu,post_lu)),'mcm_perm_equal':bool(np.array_equal(pre_p,post_p)),'pre_wsp_sha256':sha_arr(pre_m),'post_wsp_sha256':sha_arr(post_m),'pre_lu_sha256':sha_arr(pre_lu),'post_lu_sha256':sha_arr(post_lu),'pre_perm_sha256':sha_i4(pre_p),'post_perm_sha256':sha_i4(post_p)},'direct_sha256':sha_arr(d1),'reload_pre_sha256':sha_arr(rp1),'saved_lu_sha256':sha_arr(saved),'no_tolerance_rescue':True}
    (out/'terminal_diagnostic_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(token)
if __name__=='__main__': main()
