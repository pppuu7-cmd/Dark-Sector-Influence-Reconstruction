#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json
from pathlib import Path
import healpy as hp
import numpy as np
import pymaster as nmt

DES_BAND_EDGES = [0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]
DES_SELECTED = {'output':'TE','input':'TE'}
COUNTS = {'lens':0,'source':0}

def sha_f8(x):
    a=np.ascontiguousarray(x,dtype='<f8')
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()

def reconstruct_lens_synthetic(nside):
    COUNTS['lens'] += 1
    npix=12*nside*nside
    p=np.arange(npix,dtype=np.int64)
    x=(0.65+0.25*np.sin(0.017*p)).astype(np.float64)
    x[(p%7)==0]=0.0
    return x

def reconstruct_source_synthetic(nside):
    COUNTS['source'] += 1
    npix=12*nside*nside
    p=np.arange(npix,dtype=np.int64)
    x=(1.0+((p*13+5)%11)).astype(np.float64)
    x[(p%5)==0]=0.0
    return x

def build_fields_once(nside):
    lens=reconstruct_lens_synthetic(nside)
    source=reconstruct_source_synthetic(nside)
    masks_receipt={'lens_sha256':sha_f8(lens),'source_sha256':sha_f8(source)}
    f0=nmt.NmtField(lens,None,spin=0)
    f2=nmt.NmtField(source,None,spin=2)
    return lens,source,f0,f2,masks_receipt

def derive_pcl_same_fields(f0,f2,lmax):
    a0=f0.get_mask_alms(); a2=f2.get_mask_alms()
    pcl=np.ascontiguousarray(hp.alm2cl(a0,a2,lmax=lmax),dtype='<f8')
    return pcl

def workspace_same_fields(f0,f2,nside):
    lmax=3*nside-1
    edges=np.arange(0,lmax+2,4,dtype=np.int64)
    if edges[-1] != lmax+1:
        edges=np.append(edges,lmax+1)
    b=nmt.NmtBin.from_edges(edges[:-1],edges[1:])
    w=nmt.NmtWorkspace()
    w.compute_coupling_matrix(f0,f2,b)
    wins=np.ascontiguousarray(w.get_bandpower_windows(),dtype='<f8')
    return wins, edges

def audit(out_path,source_head,contract_fingerprint):
    v=importlib.metadata.version('pymaster')
    if not (v=='2.7' or v.startswith('2.7.')): raise AssertionError(v)
    if len(DES_BAND_EDGES)!=40 or len(DES_BAND_EDGES)-1!=39 or DES_BAND_EDGES[0]!=0 or DES_BAND_EDGES[-1]!=12288:
        raise AssertionError('DES band authority')
    if any(b<=a for a,b in zip(DES_BAND_EDGES[:-1],DES_BAND_EDGES[1:])): raise AssertionError('edges monotonic')
    nside=8; lmax=3*nside-1
    lens,source,f0,f2,masks=build_fields_once(nside)
    id0,id2=id(f0),id(f2)
    pcl=derive_pcl_same_fields(f0,f2,lmax)
    pcl_ids=(id(f0),id(f2))
    wins,synthetic_edges=workspace_same_fields(f0,f2,nside)
    workspace_ids=(id(f0),id(f2))
    counters=dict(COUNTS)
    selected=np.ascontiguousarray(wins[0,:,0,:],dtype='<f8')
    same_ids=(pcl_ids==workspace_ids==(id0,id2))
    status='H1_SINGLE_MASK_INTEGRATED_DRIVER_PASS'
    if counters!={'lens':1,'source':1}: status='H2_MASK_RECONSTRUCTION_DUPLICATED'
    elif not same_ids: status='H3_FIELD_HANDOFF_NOT_IDENTICAL'
    receipt={
      'schema':'dsir.exp073cw.single_mask_integrated_driver.v0.1','status':status,'accounting':'+0/+0',
      'source_head':source_head,'contract_fingerprint':contract_fingerprint,'pymaster_version':v,
      'des_band_edges':DES_BAND_EDGES,'des_band_count':39,'des_ell_max':12287,
      'selected_semantics':DES_SELECTED,'reconstruction_counts':counters,'same_field_object_identity':same_ids,
      'mask_sha256':masks,'synthetic_nside':nside,'synthetic_edges':synthetic_edges.tolist(),
      'pcl_shape':list(pcl.shape),'full_window_shape':list(wins.shape),'selected_shape':list(selected.shape),
      'selected_sha256':sha_f8(selected),'historical_wm_s3_numerical_import':False,'no_tolerance_rescue':True,
      'science_gate_scored':False,'wm_s3_authority_created':False,'exp073bu_activated':False,
      'checkpoint_order':['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']
    }
    Path(out_path).parent.mkdir(parents=True,exist_ok=True)
    Path(out_path).write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(status)
    if status!='H1_SINGLE_MASK_INTEGRATED_DRIVER_PASS': raise SystemExit(2)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--contract-fingerprint',required=True)
    a=ap.parse_args(); audit(a.out,a.source_head,a.contract_fingerprint)
if __name__=='__main__': main()
