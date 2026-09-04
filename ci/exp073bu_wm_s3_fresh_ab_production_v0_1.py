#!/usr/bin/env python3
from __future__ import annotations
import argparse, gc, hashlib, importlib.metadata, json, os
from pathlib import Path
import healpy as hp
import numpy as np
import pymaster as nmt

from exp073bu_fresh_wm_s3_pcl_v0_1 import (
    LMAX, NSIDE, PCL_SHAPE, canonical_f8_sha, reconstruct_lens_mask,
    reconstruct_s3_count_map,
)
from exp073cv_wm_s3_production_exact_adapter_v0_1 import execute as execute_exact_adapter

SCHEMA='dsir.exp073bu.wm_s3.fresh_ab_production.v0.1'
BAND_EDGES=np.asarray([0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288],dtype=np.int32)
CHECKPOINT_ORDER=['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']
NAMESPACES={'A':'checkpoints/exp073bu-wm-s3-a-v0-1','B':'checkpoints/exp073bu-wm-s3-b-v0-1'}
OUTER_COMPUTE_WORKERS=8
THREAD_ENV={'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1'}

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def file_sha(path:Path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()
def atomic_json(path:Path,obj):
    path.parent.mkdir(parents=True,exist_ok=True); tmp=path.with_suffix(path.suffix+'.tmp'); tmp.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n'); os.replace(tmp,path)
def atomic_npy(path:Path,a):
    path.parent.mkdir(parents=True,exist_ok=True); c=canon(a); tmp=path.with_name(path.name+'.tmp.npy'); np.save(tmp,c,allow_pickle=False); os.replace(tmp,path); r=np.load(path,mmap_mode='r',allow_pickle=False)
    if r.dtype.str!='<f8' or tuple(r.shape)!=tuple(c.shape) or not np.array_equal(r,c): raise RuntimeError('fail-closed array persistence mismatch')
    sha=canonical_f8_sha(r); del r; return sha

def stage_manifest(root:Path,stage:str,replica:str,source_head:str,contract_fingerprint:str,payloads:dict):
    if stage not in CHECKPOINT_ORDER: raise RuntimeError(stage)
    rec={'schema':SCHEMA+'.checkpoint','stage':stage,'complete':True,'replica':replica,'checkpoint_namespace':NAMESPACES[replica],'source_head':source_head,'contract_fingerprint':contract_fingerprint,'payloads':payloads,'historical_wm_s3_numerical_import':False,'other_replica_output_read':False}
    atomic_json(root/(stage+'.json'),rec); return rec

def load_manifest(root:Path,stage:str,replica:str,source_head:str,contract_fingerprint:str):
    p=root/(stage+'.json')
    if not p.exists(): return None
    rec=json.loads(p.read_text())
    required=(rec.get('complete') is True and rec.get('stage')==stage and rec.get('replica')==replica and rec.get('checkpoint_namespace')==NAMESPACES[replica] and rec.get('source_head')==source_head and rec.get('contract_fingerprint')==contract_fingerprint and rec.get('historical_wm_s3_numerical_import') is False and rec.get('other_replica_output_read') is False)
    if not required: raise RuntimeError('fail-closed checkpoint identity mismatch')
    return rec

def fresh_or_restore_masks(replica_root:Path,replica:str,r1_root:Path,lens_path:Path,source_head:str,contract_fingerprint:str):
    st=load_manifest(replica_root,'fresh_masks_complete',replica,source_head,contract_fingerprint)
    lp=replica_root/'lens_mask.npy'; sp=replica_root/'s3_mask.npy'
    if st is None:
        lens,lens_rec=reconstruct_lens_mask(lens_path); source,s3_rec=reconstruct_s3_count_map(r1_root)
        lsha=atomic_npy(lp,lens); ssha=atomic_npy(sp,source)
        stage_manifest(replica_root,'fresh_masks_complete',replica,source_head,contract_fingerprint,{'lens_mask':{'canonical_sha256':lsha,'shape':list(lens.shape)},'s3_mask':{'canonical_sha256':ssha,'shape':list(source.shape)},'lens_authority':lens_rec,'s3_authority':s3_rec,'reconstruction_counts':{'lens':1,'source':1}})
        return lens,source,{'lens':1,'source':1}
    lens=np.load(lp,mmap_mode='r',allow_pickle=False); source=np.load(sp,mmap_mode='r',allow_pickle=False)
    if canonical_f8_sha(lens)!=st['payloads']['lens_mask']['canonical_sha256'] or canonical_f8_sha(source)!=st['payloads']['s3_mask']['canonical_sha256']: raise RuntimeError('fail-closed mask restore SHA mismatch')
    return lens,source,{'lens':0,'source':0}

def run_replica(replica:str,args):
    if replica not in NAMESPACES: raise RuntimeError(replica)
    version=importlib.metadata.version('pymaster')
    if not (version=='2.7' or version.startswith('2.7.')): raise RuntimeError('PyMaster 2.7 required')
    for k,v in THREAD_ENV.items():
        if os.environ.get(k,v)!=v: raise RuntimeError(f'{k} must be {v}')
        os.environ[k]=v
    root=Path(args.checkpoint_root)/replica; root.mkdir(parents=True,exist_ok=True)
    lens,source,recon=fresh_or_restore_masks(root,replica,Path(args.r1_root),Path(args.lens_mask),args.source_head,args.contract_fingerprint)
    # Exactly one field pair per replica. The same Python objects feed PCL and workspace.
    f0=nmt.NmtField(lens,None,spin=0); f2=nmt.NmtField(source,None,spin=2)
    if int(f0.ainfo_mask.lmax)!=LMAX or int(f2.ainfo_mask.lmax)!=LMAX: raise RuntimeError('field lmax mismatch')
    lens_alm=f0.get_mask_alms(); source_alm=f2.get_mask_alms(); pcl=canon(hp.alm2cl(lens_alm,source_alm,lmax=LMAX)); del lens_alm,source_alm
    if pcl.shape!=PCL_SHAPE: raise RuntimeError('PCL shape mismatch')
    pcl_path=root/'fresh_mask_pcl.npy'; pcl_sha=atomic_npy(pcl_path,pcl)
    workspace_path=root/'fresh_workspace.fits'
    ws_manifest=load_manifest(root,'fresh_workspace_mcm_complete',replica,args.source_head,args.contract_fingerprint)
    if ws_manifest is None:
        b=nmt.NmtBin.from_edges(BAND_EDGES[:-1],BAND_EDGES[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f2,b); w.write_to(str(workspace_path)); del w,b; gc.collect()
        wsha=file_sha(workspace_path); stage_manifest(root,'fresh_workspace_mcm_complete',replica,args.source_head,args.contract_fingerprint,{'workspace_fits':{'sha256':wsha},'fresh_pcl':{'canonical_sha256':pcl_sha},'same_field_object_handoff':True,'field_object_ids':[id(f0),id(f2)],'reconstruction_counts':recon})
    else:
        if not workspace_path.exists() or file_sha(workspace_path)!=ws_manifest['payloads']['workspace_fits']['sha256']: raise RuntimeError('fail-closed workspace restore SHA mismatch')
    del f0,f2,lens,source,pcl; gc.collect()
    wsha=file_sha(workspace_path)
    stage_manifest(root,'mcm_fits_verified',replica,args.source_head,args.contract_fingerprint,{'workspace_fits':{'sha256':wsha}})
    edges_path=root/'edges.json'; edges_path.write_text(json.dumps(BAND_EDGES.tolist()))
    blobs_path=Path(args.component_blobs_json)
    ad=argparse.Namespace(workspace_fits=str(workspace_path),edges_json=str(edges_path),ncls=2,nl=12288,emulator=args.downstream_exe,out_dir=str(root/'exact_route'),source_head=args.source_head,contract_fingerprint=args.contract_fingerprint,checkpoint_namespace=NAMESPACES[replica],component_blobs_json=str(blobs_path))
    rec=execute_exact_adapter(ad)
    full_path=root/'exact_route'/'full_window.bin'; te_path=root/'exact_route'/'selected_te.bin'
    stage_manifest(root,'full_window_complete',replica,args.source_head,args.contract_fingerprint,{'full_window':{'sha256':file_sha(full_path),'shape':[2,39,2,12288]}})
    stage_manifest(root,'selected_te_complete',replica,args.source_head,args.contract_fingerprint,{'selected_te':{'sha256':file_sha(te_path),'shape':[39,12288],'dtype':'<f8','semantics':'wins[0,:,0,:] = TE<-TE'}})
    receipt={'schema':SCHEMA+'.replica','replica':replica,'selected_te_sha256':file_sha(te_path),'selected_te_path':str(te_path),'fresh_pcl_sha256':pcl_sha,'workspace_fits_sha256':wsha,'adapter_receipt':rec,'reconstruction_counts':recon,'outer_compute_workers':OUTER_COMPUTE_WORKERS,'nested_threads':THREAD_ENV,'source_head':args.source_head,'contract_fingerprint':args.contract_fingerprint,'checkpoint_namespace':NAMESPACES[replica],'historical_wm_s3_numerical_import':False,'other_replica_output_read':False,'science_gate_scored':False}
    atomic_json(root/'replica_receipt.json',receipt); stage_manifest(root,'replica_receipt_complete',replica,args.source_head,args.contract_fingerprint,{'replica_receipt':{'sha256':file_sha(root/'replica_receipt.json')},'selected_te':{'sha256':receipt['selected_te_sha256']}})
    return receipt

def compare_replicas(a:dict,b:dict,out_path:Path):
    ap=Path(a['selected_te_path']); bp=Path(b['selected_te_path']); aa=np.memmap(ap,dtype='<f8',mode='r',shape=(39,12288)); bb=np.memmap(bp,dtype='<f8',mode='r',shape=(39,12288))
    sha_equal=a['selected_te_sha256']==b['selected_te_sha256']; array_equal=bool(np.array_equal(aa,bb)); del aa,bb
    status='PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1' if sha_equal and array_equal else 'FAIL_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1'
    rec={'schema':SCHEMA+'.ab_compare','status':status,'sha256_equal':sha_equal,'numpy_array_equal':array_equal,'a_sha256':a['selected_te_sha256'],'b_sha256':b['selected_te_sha256'],'no_tolerance_rescue':True,'science_gate_scored':True}
    atomic_json(out_path,rec); return rec

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--replica',choices=['A','B','AB'],default='AB'); ap.add_argument('--r1-root',required=True); ap.add_argument('--lens-mask',required=True); ap.add_argument('--checkpoint-root',required=True); ap.add_argument('--downstream-exe',required=True); ap.add_argument('--component-blobs-json',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--contract-fingerprint',required=True); ap.add_argument('--ab-out',required=True); args=ap.parse_args()
    if args.replica=='A': run_replica('A',args); return
    if args.replica=='B': run_replica('B',args); return
    a=run_replica('A',args); b=run_replica('B',args); rec=compare_replicas(a,b,Path(args.ab_out)); print(rec['status']); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
