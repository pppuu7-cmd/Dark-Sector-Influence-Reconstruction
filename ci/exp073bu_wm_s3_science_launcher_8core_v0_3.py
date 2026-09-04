#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json, os, subprocess, sys, traceback
from pathlib import Path
import numpy as np

SCHEMA='dsir.exp073bu.wm_s3.science_launcher.8core.v0.3'
PASS_TOKEN='PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3'
VALID_CLASSES={'PASS','SCIENTIFIC_REPEATABILITY_FAIL','INFRASTRUCTURE_INCOMPLETE','BLOCKED'}
SHAPE=(39,12288); FULL_SHAPE=(2,39,2,12288)
SELECTED_BYTES=39*12288*8; FULL_BYTES=2*39*2*12288*8
CHECKPOINT_ORDER=['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']
NAMESPACES={'A':'checkpoints/exp073bu-wm-s3-a-v0-1','B':'checkpoints/exp073bu-wm-s3-b-v0-1'}
THREAD_ENV={'OMP_NUM_THREADS':'8','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1'}
S3={'selected_rows':4196641,'record_bytes':16786564,'record_sha256':'3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec','unique_occupied_pixels':2943132,'occupancy_sha256':'21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094'}
LENS={'bytes':104595840,'sha256':'a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55'}

def sha_file(p:Path):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()

def atomic_json(p:Path,obj):
    p.parent.mkdir(parents=True,exist_ok=True); t=p.with_suffix(p.suffix+'.tmp'); t.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n'); os.replace(t,p)

def classify_exception(text:str):
    markers=('fail-closed checkpoint identity mismatch','historical_wm_s3_numerical_import','other_replica_output_read','source_head','contract_fingerprint','checkpoint_namespace','SHA256 mismatch','SHA mismatch','authority','OpenMP runtime proof')
    return 'BLOCKED' if any(x in text for x in markers) else 'INFRASTRUCTURE_INCOMPLETE'

def manifest(root:Path,stage:str,replica:str,head:str,fp:str):
    p=root/f'{stage}.json'
    if not p.is_file(): raise RuntimeError(f'missing checkpoint manifest: {p}')
    r=json.loads(p.read_text())
    ok=(r.get('complete') is True and r.get('stage')==stage and r.get('replica')==replica and r.get('checkpoint_namespace')==NAMESPACES[replica] and r.get('source_head')==head and r.get('contract_fingerprint')==fp and r.get('historical_wm_s3_numerical_import') is False and r.get('other_replica_output_read') is False)
    if not ok: raise RuntimeError(f'fail-closed checkpoint identity mismatch: {p}')
    return r

def validate_replica(checkpoint_root:Path,replica:str,head:str,fp:str):
    root=checkpoint_root/replica
    ms={s:manifest(root,s,replica,head,fp) for s in CHECKPOINT_ORDER}
    rp=root/'replica_receipt.json'
    if not rp.is_file(): raise RuntimeError(f'missing replica receipt: {rp}')
    r=json.loads(rp.read_text())
    ok=(r.get('replica')==replica and r.get('source_head')==head and r.get('contract_fingerprint')==fp and r.get('checkpoint_namespace')==NAMESPACES[replica] and r.get('historical_wm_s3_numerical_import') is False and r.get('other_replica_output_read') is False and r.get('science_gate_scored') is False and r.get('outer_compute_workers')==8 and r.get('nested_threads')==THREAD_ENV)
    if not ok: raise RuntimeError(f'fail-closed replica receipt identity mismatch: {replica}')
    par=(r.get('adapter_receipt') or {}).get('downstream_parallelism') or {}
    if not (par.get('workers')==8 and par.get('runtime_team_verified') is True and par.get('scalar_accumulation_order_preserved') is True): raise RuntimeError(f'fail-closed OpenMP runtime proof missing for {replica}')
    te=Path(r['selected_te_path'])
    if not te.is_file() or te.stat().st_size!=SELECTED_BYTES or sha_file(te)!=r.get('selected_te_sha256'): raise RuntimeError(f'fail-closed selected TE SHA mismatch for {replica}')
    a=np.memmap(te,dtype='<f8',mode='r',shape=SHAPE,order='C'); finite=bool(np.all(np.isfinite(a))); del a
    if not finite: raise RuntimeError(f'non-finite selected TE payload for {replica}')
    full=root/'exact_route'/'full_window.bin'
    if not full.is_file() or full.stat().st_size!=FULL_BYTES: raise RuntimeError(f'invalid full-window payload for {replica}')
    if ms['full_window_complete']['payloads']['full_window'].get('shape')!=list(FULL_SHAPE): raise RuntimeError('full-window shape provenance mismatch')
    sp=ms['selected_te_complete']['payloads']['selected_te']
    if sp.get('shape')!=list(SHAPE) or sp.get('dtype')!='<f8' or sp.get('semantics')!='wins[0,:,0,:] = TE<-TE': raise RuntimeError('selected-TE provenance mismatch')
    mp=ms['fresh_masks_complete']['payloads']; s3=mp.get('s3_authority',{}); lens=mp.get('lens_authority',{})
    if not (s3.get('selected_rows')==S3['selected_rows'] and s3.get('record_bytes')==S3['record_bytes'] and s3.get('record_sha256')==S3['record_sha256'] and s3.get('unique_occupied_pixels')==S3['unique_occupied_pixels'] and s3.get('occupancy_sha256')==S3['occupancy_sha256'] and lens.get('bytes')==LENS['bytes'] and lens.get('sha256')==LENS['sha256'] and lens.get('ordering')=='RING' and lens.get('coordinate')=='C'):
        raise RuntimeError(f'upstream authority mismatch for {replica}')
    ws=ms['fresh_workspace_mcm_complete']['payloads']
    if ws.get('same_field_object_handoff') is not True or ws.get('reconstruction_counts')!={'lens':1,'source':1}: raise RuntimeError(f'fresh reconstruction mismatch for {replica}')
    return {'replica':replica,'selected_te_path':str(te),'selected_te_sha256':r['selected_te_sha256'],'workspace_fits_sha256':r.get('workspace_fits_sha256'),'fresh_pcl_sha256':r.get('fresh_pcl_sha256')}

def run_replica(driver:Path,replica:str,args):
    cmd=[sys.executable,str(driver),'--replica',replica,'--r1-root',str(Path(args.r1_root).resolve()),'--lens-mask',str(Path(args.lens_mask).resolve()),'--checkpoint-root',str(Path(args.checkpoint_root).resolve()),'--downstream-exe',str(Path(args.downstream_exe).resolve()),'--component-blobs-json',str(Path(args.component_blobs_json).resolve()),'--source-head',args.source_head,'--contract-fingerprint',args.contract_fingerprint,'--ab-out',str(Path(args.out).resolve().with_suffix('.driver_unused.json'))]
    env=os.environ.copy(); env.update(THREAD_ENV)
    return subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=env)

def main():
    ap=argparse.ArgumentParser()
    for x in ('driver','r1_root','lens_mask','checkpoint_root','downstream_exe','component_blobs_json','source_head','contract_fingerprint','out'): ap.add_argument('--'+x.replace('_','-'),dest=x,required=True)
    args=ap.parse_args(); out=Path(args.out); root=Path(args.checkpoint_root).resolve(); driver=Path(args.driver).resolve()
    rec={'schema':SCHEMA,'classification':None,'raw_token':None,'source_head':args.source_head,'contract_fingerprint':args.contract_fingerprint,'checkpoint_namespaces':NAMESPACES,'science_gate_scored':False,'wm_s3_authority_created':False,'historical_wm_s3_numerical_import':False,'no_tolerance_rescue':True,'execution_workers':8,'comparison':None,'replicas':{},'logs':{}}
    try:
        v=importlib.metadata.version('pymaster')
        if not (v=='2.7' or v.startswith('2.7.')): raise RuntimeError(f'PyMaster 2.7 required, got {v}')
        if not driver.is_file(): raise RuntimeError('production driver missing')
        for k,vv in THREAD_ENV.items():
            if os.environ.get(k,vv)!=vv: raise RuntimeError(f'{k} must be {vv}')
            os.environ[k]=vv
        rec['pymaster_version']=v
        for replica in ('A','B'):
            p=run_replica(driver,replica,args); rec['logs'][replica]={'returncode':p.returncode,'stdout_tail':p.stdout[-12000:]}
            if p.returncode!=0:
                rec['classification']=classify_exception(p.stdout); rec['error']=f'replica {replica} exited {p.returncode}'; atomic_json(out,rec); print(rec['classification']); return 4
            rec['replicas'][replica]=validate_replica(root,replica,args.source_head,args.contract_fingerprint)
        a=rec['replicas']['A']; b=rec['replicas']['B']; aa=np.memmap(a['selected_te_path'],dtype='<f8',mode='r',shape=SHAPE); bb=np.memmap(b['selected_te_path'],dtype='<f8',mode='r',shape=SHAPE)
        se=a['selected_te_sha256']==b['selected_te_sha256']; ae=bool(np.array_equal(aa,bb)); del aa,bb
        rec['comparison']={'whole_canonical_sha256_equal':se,'numpy_array_equal':ae,'shape':list(SHAPE),'dtype':'<f8','no_tolerance_rescue':True}; rec['science_gate_scored']=True
        if se and ae: rec['classification']='PASS'; rec['raw_token']=PASS_TOKEN; rec['wm_s3_authority_created']=True; rc=0
        else: rec['classification']='SCIENTIFIC_REPEATABILITY_FAIL'; rc=3
    except Exception as e:
        text=repr(e)+'\n'+traceback.format_exc(); rec['classification']=classify_exception(text); rec['error']=repr(e); rec['traceback']=traceback.format_exc(); rc=4
    if rec['classification'] not in VALID_CLASSES: rec['classification']='BLOCKED'; rc=4
    atomic_json(out,rec); print(rec['classification'])
    if rec.get('raw_token'): print(rec['raw_token'])
    print(json.dumps(rec.get('comparison'),indent=2,sort_keys=True)); return rc

if __name__=='__main__': raise SystemExit(main())
