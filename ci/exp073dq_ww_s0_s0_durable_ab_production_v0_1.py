#!/usr/bin/env python3
from __future__ import annotations
import argparse,gc,hashlib,importlib.metadata,json,os
from pathlib import Path
import numpy as np
import pymaster as nmt

from exp073aa_article3_des_angular_task_runner_v0_1 import BAND_EDGES, LMAX_PLUS_ONE, source_count_map, validate_r1
from exp073do_ww_s0_s0_production_exact_adapter_v0_1 import execute as execute_ww_adapter

SCHEMA='dsir.exp073dq.ww_s0_s0.durable_ab_production.v0.1'
CHECKPOINT_ORDER=['fresh_s0_mask_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
NAMESPACES={'A':'checkpoints/exp073dq-ww-s0-s0-a-v0-1','B':'checkpoints/exp073dq-ww-s0-s0-b-v0-1'}
THREAD_ENV={'OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1'}

def file_sha(path:Path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''): h.update(b)
 return h.hexdigest()
def canon_sha(a): return hashlib.sha256(memoryview(np.ascontiguousarray(np.asarray(a,dtype='<f8'))).cast('B')).hexdigest()
def atomic_json(p:Path,o):
 p.parent.mkdir(parents=True,exist_ok=True); t=p.with_suffix(p.suffix+'.tmp'); t.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n'); os.replace(t,p)
def atomic_npy(p:Path,a):
 p.parent.mkdir(parents=True,exist_ok=True); x=np.ascontiguousarray(np.asarray(a,dtype='<f8')); t=p.with_name(p.name+'.tmp.npy'); np.save(t,x,allow_pickle=False); os.replace(t,p); r=np.load(p,mmap_mode='r',allow_pickle=False)
 if r.dtype.str!='<f8' or tuple(r.shape)!=tuple(x.shape) or not np.array_equal(r,x): raise RuntimeError('fail-closed S0 persistence mismatch')
 s=canon_sha(r); del r; return s

def manifest(root,stage,replica,head,fp,payloads):
 if stage not in CHECKPOINT_ORDER: raise RuntimeError(stage)
 r={'schema':SCHEMA+'.checkpoint','stage':stage,'complete':True,'replica':replica,'checkpoint_namespace':NAMESPACES[replica],'source_head':head,'contract_fingerprint':fp,'payloads':payloads,'historical_ww_numerical_import':False,'other_replica_output_read':False}; atomic_json(root/(stage+'.json'),r); return r

def load_manifest(root,stage,replica,head,fp):
 p=root/(stage+'.json')
 if not p.exists(): return None
 r=json.loads(p.read_text()); ok=(r.get('complete') is True and r.get('stage')==stage and r.get('replica')==replica and r.get('checkpoint_namespace')==NAMESPACES[replica] and r.get('source_head')==head and r.get('contract_fingerprint')==fp and r.get('historical_ww_numerical_import') is False and r.get('other_replica_output_read') is False)
 if not ok: raise RuntimeError('fail-closed WW checkpoint identity mismatch')
 return r

def fresh_or_restore_s0(root,replica,r1_root,r1_digest,head,fp):
 st=load_manifest(root,'fresh_s0_mask_complete',replica,head,fp); sp=root/'s0_count_map.npy'
 if st is None:
  auth=validate_r1(r1_root,r1_digest); s0,meta=source_count_map(r1_root,0); sha=atomic_npy(sp,s0); manifest(root,'fresh_s0_mask_complete',replica,head,fp,{'s0_count_map':{'canonical_sha256':sha,'shape':list(s0.shape),'dtype':'<f8'},'r1_authority':auth,'s0_authority':meta,'reconstruction_count':1}); return s0,1
 if not sp.exists(): raise RuntimeError('fail-closed missing S0 checkpoint payload')
 s0=np.load(sp,mmap_mode='r',allow_pickle=False)
 if s0.dtype.str!='<f8' or canon_sha(s0)!=st['payloads']['s0_count_map']['canonical_sha256']: raise RuntimeError('fail-closed S0 restore SHA mismatch')
 return s0,0

def validated_finished(root,replica,head,fp):
 st=load_manifest(root,'replica_receipt_complete',replica,head,fp); rp=root/'replica_receipt.json'
 if st is None:return None
 if not rp.exists() or file_sha(rp)!=st['payloads']['replica_receipt']['sha256']: raise RuntimeError('fail-closed receipt restore mismatch')
 r=json.loads(rp.read_text()); ee=Path(r['selected_ee_path'])
 if not ee.exists() or file_sha(ee)!=r['selected_ee_sha256'] or r['selected_ee_sha256']!=st['payloads']['selected_ee']['sha256']: raise RuntimeError('fail-closed final EE restore mismatch')
 return r

def run_replica(replica,args):
 if replica not in NAMESPACES: raise RuntimeError(replica)
 v=importlib.metadata.version('pymaster')
 if not (v=='2.7' or v.startswith('2.7.')): raise RuntimeError('PyMaster 2.7 required')
 for k,val in THREAD_ENV.items():
  if os.environ.get(k,val)!=val: raise RuntimeError(f'{k} must be {val}')
  os.environ[k]=val
 root=Path(args.checkpoint_root)/replica; root.mkdir(parents=True,exist_ok=True)
 done=validated_finished(root,replica,args.source_head,args.contract_fingerprint)
 if done is not None:return done
 wp=root/'fresh_workspace.fits'; ws=load_manifest(root,'fresh_workspace_mcm_complete',replica,args.source_head,args.contract_fingerprint)
 if ws is None:
  s0,recon=fresh_or_restore_s0(root,replica,Path(args.r1_root),args.r1_artifact_digest,args.source_head,args.contract_fingerprint)
  f=nmt.NmtField(s0,None,spin=2); b=nmt.NmtBin.from_edges(BAND_EDGES[:-1],BAND_EDGES[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f,f,b); w.write_to(str(wp)); wsha=file_sha(wp)
  manifest(root,'fresh_workspace_mcm_complete',replica,args.source_head,args.contract_fingerprint,{'workspace_fits':{'sha256':wsha},'same_field_object_handoff':True,'field_object_ids':[id(f),id(f)],'reconstruction_count':recon})
  del w,b,f,s0; gc.collect()
 else:
  if not wp.exists() or file_sha(wp)!=ws['payloads']['workspace_fits']['sha256']: raise RuntimeError('fail-closed workspace restore SHA mismatch')
  wsha=ws['payloads']['workspace_fits']['sha256']; recon=0
 manifest(root,'mcm_fits_verified',replica,args.source_head,args.contract_fingerprint,{'workspace_fits':{'sha256':wsha}})
 ee_st=load_manifest(root,'selected_ee_complete',replica,args.source_head,args.contract_fingerprint); full_st=load_manifest(root,'full_window_complete',replica,args.source_head,args.contract_fingerprint); full=root/'exact_route'/'full_window.bin'; ee=root/'exact_route'/'selected_ee.bin'
 if ee_st is not None:
  if not ee.exists() or file_sha(ee)!=ee_st['payloads']['selected_ee']['sha256']: raise RuntimeError('fail-closed selected EE restore mismatch')
  if full_st is None or not full.exists() or file_sha(full)!=full_st['payloads']['full_window']['sha256']: raise RuntimeError('fail-closed full-window restore mismatch')
  adapter={'status':'RESTORED_FROM_VERIFIED_SELECTED_EE_CHECKPOINT','historical_ww_numerical_import':False}
 else:
  ep=root/'edges.json'; ep.write_text(json.dumps(BAND_EDGES.tolist())); ad=argparse.Namespace(workspace_fits=str(wp),edges_json=str(ep),ncls=4,nl=LMAX_PLUS_ONE,emulator=args.downstream_exe,out_dir=str(root/'exact_route'),source_head=args.source_head,contract_fingerprint=args.contract_fingerprint,checkpoint_namespace=NAMESPACES[replica],component_blobs_json=args.component_blobs_json); adapter=execute_ww_adapter(ad)
  manifest(root,'full_window_complete',replica,args.source_head,args.contract_fingerprint,{'full_window':{'sha256':file_sha(full),'shape':[4,39,4,12288]}}); manifest(root,'selected_ee_complete',replica,args.source_head,args.contract_fingerprint,{'selected_ee':{'sha256':file_sha(ee),'shape':[39,12288],'dtype':'<f8','semantics':'wins[0,:,0,:] = EE<-EE'}})
 rec={'schema':SCHEMA+'.replica','replica':replica,'selected_ee_sha256':file_sha(ee),'selected_ee_path':str(ee),'workspace_fits_sha256':wsha,'adapter_receipt':adapter,'reconstruction_count':recon,'source_head':args.source_head,'contract_fingerprint':args.contract_fingerprint,'checkpoint_namespace':NAMESPACES[replica],'historical_ww_numerical_import':False,'other_replica_output_read':False,'science_gate_scored':False}
 atomic_json(root/'replica_receipt.json',rec); manifest(root,'replica_receipt_complete',replica,args.source_head,args.contract_fingerprint,{'replica_receipt':{'sha256':file_sha(root/'replica_receipt.json')},'selected_ee':{'sha256':rec['selected_ee_sha256']}}); return rec

def compare(a,b,out):
 aa=np.memmap(a['selected_ee_path'],dtype='<f8',mode='r',shape=(39,12288)); bb=np.memmap(b['selected_ee_path'],dtype='<f8',mode='r',shape=(39,12288)); se=a['selected_ee_sha256']==b['selected_ee_sha256']; ae=bool(np.array_equal(aa,bb)); del aa,bb
 status='PASS_EXP073DQ_WW_S0_S0_DURABLE_AB_PROVISIONAL_EXACT_REPEATABILITY_V0_1' if se and ae else 'FAIL_EXP073DQ_WW_S0_S0_DURABLE_AB_PROVISIONAL_EXACT_REPEATABILITY_V0_1'; r={'schema':SCHEMA+'.ab_compare','status':status,'sha256_equal':se,'numpy_array_equal':ae,'a_sha256':a['selected_ee_sha256'],'b_sha256':b['selected_ee_sha256'],'no_tolerance_rescue':True,'science_gate_scored':False,'ww_authority_created':False}; atomic_json(out,r); return r

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--replica',choices=['A','B','AB'],default='AB'); ap.add_argument('--r1-root',required=True); ap.add_argument('--r1-artifact-digest',required=True); ap.add_argument('--checkpoint-root',required=True); ap.add_argument('--downstream-exe',required=True); ap.add_argument('--component-blobs-json',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--contract-fingerprint',required=True); ap.add_argument('--ab-out',required=True); a=ap.parse_args()
 if a.replica=='A':run_replica('A',a);return
 if a.replica=='B':run_replica('B',a);return
 ra=run_replica('A',a); rb=run_replica('B',a); print(compare(ra,rb,Path(a.ab_out))['status'])
if __name__=='__main__':main()
