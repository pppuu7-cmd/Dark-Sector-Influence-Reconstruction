#!/usr/bin/env python3
from __future__ import annotations
import argparse,gc,hashlib,importlib.metadata,json,os
from pathlib import Path
import numpy as np
import pymaster as nmt
from exp073aa_article3_des_angular_task_runner_v0_1 import BAND_EDGES, LMAX_PLUS_ONE, source_count_map, validate_r1

SCHEMA='dsir.exp073ey.ww_s0_s1.durable_ab_production.v0.1'
CHECKPOINT_ORDER=['fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
NAMESPACES={'A':'checkpoints/exp073ey-ww-s0-s1-a-v0-1','B':'checkpoints/exp073ey-ww-s0-s1-b-v0-1'}
THREAD_ENV={'OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1'}
FULL_SHAPE=(4,39,4,12288); EE_SHAPE=(39,12288)

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
 if r.dtype.str!='<f8' or tuple(r.shape)!=tuple(x.shape) or not np.array_equal(r,x): raise RuntimeError('fail-closed source persistence mismatch')
 s=canon_sha(r); del r; return s

def manifest(root,stage,replica,head,fp,payloads):
 if stage not in CHECKPOINT_ORDER: raise RuntimeError(stage)
 r={'schema':SCHEMA+'.checkpoint','stage':stage,'complete':True,'replica':replica,'checkpoint_namespace':NAMESPACES[replica],'source_head':head,'contract_fingerprint':fp,'payloads':payloads,'historical_ww_numerical_import':False,'other_replica_output_read':False}; atomic_json(root/(stage+'.json'),r); return r

def load_manifest(root,stage,replica,head,fp):
 p=root/(stage+'.json')
 if not p.exists(): return None
 r=json.loads(p.read_text()); ok=(r.get('schema')==SCHEMA+'.checkpoint' and r.get('complete') is True and r.get('stage')==stage and r.get('replica')==replica and r.get('checkpoint_namespace')==NAMESPACES[replica] and r.get('source_head')==head and r.get('contract_fingerprint')==fp and r.get('historical_ww_numerical_import') is False and r.get('other_replica_output_read') is False)
 if not ok: raise RuntimeError('fail-closed WW_S0_S1 checkpoint identity mismatch')
 return r

def fresh_or_restore_sources(root,replica,r1_root,r1_digest,head,fp):
 st=load_manifest(root,'fresh_sources_complete',replica,head,fp); p0=root/'s0_count_map.npy'; p1=root/'s1_count_map.npy'
 if st is None:
  auth=validate_r1(r1_root,r1_digest); s0,m0=source_count_map(r1_root,0); h0=atomic_npy(p0,s0); del s0; gc.collect(); s1,m1=source_count_map(r1_root,1); h1=atomic_npy(p1,s1); del s1; gc.collect()
  st=manifest(root,'fresh_sources_complete',replica,head,fp,{'s0_count_map':{'canonical_sha256':h0,'shape':[12*4096*4096],'dtype':'<f8'},'s1_count_map':{'canonical_sha256':h1,'shape':[12*4096*4096],'dtype':'<f8'},'r1_authority':auth,'s0_authority':m0,'s1_authority':m1,'ordered_source_indices':[0,1],'reconstruction_counts':{'s0':1,'s1':1}})
 for p,k in ((p0,'s0_count_map'),(p1,'s1_count_map')):
  if not p.exists(): raise RuntimeError('fail-closed missing source checkpoint payload')
  a=np.load(p,mmap_mode='r',allow_pickle=False)
  if a.dtype.str!='<f8' or tuple(a.shape)!=(12*4096*4096,) or canon_sha(a)!=st['payloads'][k]['canonical_sha256']: raise RuntimeError('fail-closed source restore SHA/shape mismatch')
  del a
 return p0,p1,st

def validated_finished(root,replica,head,fp):
 st=load_manifest(root,'replica_receipt_complete',replica,head,fp); rp=root/'replica_receipt.json'
 if st is None:return None
 if not rp.exists() or file_sha(rp)!=st['payloads']['replica_receipt']['sha256']: raise RuntimeError('fail-closed receipt restore mismatch')
 r=json.loads(rp.read_text()); ee=Path(r['selected_ee_path'])
 if not ee.exists() or file_sha(ee)!=r['selected_ee_sha256'] or r['selected_ee_sha256']!=st['payloads']['selected_ee']['sha256']: raise RuntimeError('fail-closed final EE restore mismatch')
 if r.get('ordered_source_indices')!=[0,1] or r.get('same_field_object_handoff') is not False or r.get('bpw_route')!='public_get_bandpower_windows_after_filebacked_fits_read': raise RuntimeError('fail-closed ordered public-route receipt mismatch')
 return r

def base_chain(obj):
 out=[]; cur=obj; seen=set()
 for _ in range(16):
  if id(cur) in seen: break
  seen.add(id(cur)); out.append(type(cur).__name__)
  nxt=getattr(cur,'base',None)
  if nxt is None: break
  cur=nxt
 return out

def public_bpw_from_serialized_workspace(wp:Path,out_dir:Path):
 out_dir.mkdir(parents=True,exist_ok=True)
 w2=nmt.NmtWorkspace(); w2.read_from(str(wp),read_unbinned_MCM=True)
 mcm=getattr(getattr(w2,'wsp',None),'mcm',None)
 if mcm is None: raise RuntimeError('fail-closed missing unbinned MCM after FITS read')
 chain=base_chain(mcm); mmap_backed=any(x in ('memmap','mmap') for x in chain)
 if not mmap_backed: raise RuntimeError('fail-closed MCM is not file-backed after FITS read')
 wins=np.asarray(w2.get_bandpower_windows())
 if tuple(wins.shape)!=FULL_SHAPE: raise RuntimeError(f'fail-closed public BPW shape {wins.shape}')
 full_arr=np.ascontiguousarray(wins,dtype='<f8'); ee_arr=np.ascontiguousarray(wins[0,:,0,:],dtype='<f8')
 if tuple(ee_arr.shape)!=EE_SHAPE or not np.isfinite(full_arr).all() or not np.isfinite(ee_arr).all(): raise RuntimeError('fail-closed public BPW geometry/finiteness')
 full=out_dir/'full_window.bin'; ee=out_dir/'selected_ee.bin'; full_arr.tofile(full); ee_arr.tofile(ee)
 receipt={'route':'public_get_bandpower_windows_after_filebacked_fits_read','read_unbinned_MCM':True,'mcm_base_chain':chain,'mcm_filebacked':True,'public_full_shape':list(FULL_SHAPE),'selected_semantics':'wins[0,:,0,:] = EE<-EE','selected_shape':list(EE_SHAPE),'full_sha256':file_sha(full),'selected_sha256':file_sha(ee),'historical_manual_reconstruction':False,'no_tolerance_rescue':True}
 atomic_json(out_dir/'public_bpw_receipt.json',receipt); del wins,full_arr,ee_arr,mcm,w2; gc.collect(); return full,ee,receipt

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
  p0,p1,src=fresh_or_restore_sources(root,replica,Path(args.r1_root),args.r1_artifact_digest,args.source_head,args.contract_fingerprint)
  s0=np.load(p0,mmap_mode='r',allow_pickle=False); f0=nmt.NmtField(s0,None,spin=2); del s0; gc.collect()
  s1=np.load(p1,mmap_mode='r',allow_pickle=False); f1=nmt.NmtField(s1,None,spin=2); del s1; gc.collect()
  if id(f0)==id(f1): raise RuntimeError('fail-closed distinct-field identity collision')
  ids=[id(f0),id(f1)]; b=nmt.NmtBin.from_edges(BAND_EDGES[:-1],BAND_EDGES[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,b); w.write_to(str(wp)); wsha=file_sha(wp)
  ws=manifest(root,'fresh_workspace_mcm_complete',replica,args.source_head,args.contract_fingerprint,{'workspace_fits':{'sha256':wsha},'same_field_object_handoff':False,'ordered_source_indices':[0,1],'field_object_ids':ids,'source_map_sha256':[src['payloads']['s0_count_map']['canonical_sha256'],src['payloads']['s1_count_map']['canonical_sha256']]})
  del w,b,f1,f0; gc.collect()
 else:
  if ws['payloads'].get('same_field_object_handoff') is not False or ws['payloads'].get('ordered_source_indices')!=[0,1]: raise RuntimeError('fail-closed restored field-order semantics mismatch')
  if not wp.exists() or file_sha(wp)!=ws['payloads']['workspace_fits']['sha256']: raise RuntimeError('fail-closed workspace restore SHA mismatch')
  wsha=ws['payloads']['workspace_fits']['sha256']
 manifest(root,'mcm_fits_verified',replica,args.source_head,args.contract_fingerprint,{'workspace_fits':{'sha256':wsha},'ordered_source_indices':[0,1],'same_field_object_handoff':False})
 ee_st=load_manifest(root,'selected_ee_complete',replica,args.source_head,args.contract_fingerprint); full_st=load_manifest(root,'full_window_complete',replica,args.source_head,args.contract_fingerprint); full=root/'exact_route'/'full_window.bin'; ee=root/'exact_route'/'selected_ee.bin'
 if ee_st is not None:
  if not ee.exists() or file_sha(ee)!=ee_st['payloads']['selected_ee']['sha256']: raise RuntimeError('fail-closed selected EE restore mismatch')
  if full_st is None or not full.exists() or file_sha(full)!=full_st['payloads']['full_window']['sha256']: raise RuntimeError('fail-closed full-window restore mismatch')
  adapter={'route':'RESTORED_VERIFIED_PUBLIC_BPW_CHECKPOINT','mcm_filebacked':True,'historical_manual_reconstruction':False,'no_tolerance_rescue':True}
 else:
  full,ee,adapter=public_bpw_from_serialized_workspace(wp,root/'exact_route')
  manifest(root,'full_window_complete',replica,args.source_head,args.contract_fingerprint,{'full_window':{'sha256':file_sha(full),'shape':list(FULL_SHAPE),'route':adapter['route'],'mcm_filebacked':True}}); manifest(root,'selected_ee_complete',replica,args.source_head,args.contract_fingerprint,{'selected_ee':{'sha256':file_sha(ee),'shape':list(EE_SHAPE),'dtype':'<f8','semantics':'wins[0,:,0,:] = EE<-EE','route':adapter['route']}})
 rec={'schema':SCHEMA+'.replica','replica':replica,'selected_ee_sha256':file_sha(ee),'selected_ee_path':str(ee),'workspace_fits_sha256':wsha,'adapter_receipt':adapter,'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','ordered_source_indices':[0,1],'same_field_object_handoff':False,'source_pair':'S0->S1','source_map_sha256':ws['payloads']['source_map_sha256'],'source_head':args.source_head,'contract_fingerprint':args.contract_fingerprint,'checkpoint_namespace':NAMESPACES[replica],'historical_ww_numerical_import':False,'other_replica_output_read':False,'science_gate_scored':False}
 atomic_json(root/'replica_receipt.json',rec); manifest(root,'replica_receipt_complete',replica,args.source_head,args.contract_fingerprint,{'replica_receipt':{'sha256':file_sha(root/'replica_receipt.json')},'selected_ee':{'sha256':rec['selected_ee_sha256']}}); return rec

def compare(a,b,out):
 for r in (a,b):
  if r.get('source_pair')!='S0->S1' or r.get('ordered_source_indices')!=[0,1] or r.get('same_field_object_handoff') is not False or r.get('bpw_route')!='public_get_bandpower_windows_after_filebacked_fits_read': raise RuntimeError('fail-closed A/B semantics')
 aa=np.memmap(a['selected_ee_path'],dtype='<f8',mode='r',shape=EE_SHAPE); bb=np.memmap(b['selected_ee_path'],dtype='<f8',mode='r',shape=EE_SHAPE); se=a['selected_ee_sha256']==b['selected_ee_sha256']; ae=bool(np.array_equal(aa,bb)); finite=bool(np.isfinite(aa).all() and np.isfinite(bb).all()); del aa,bb
 status='PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1' if se and ae and finite else 'FAIL_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'; r={'schema':SCHEMA+'.ab_compare','status':status,'sha256_equal':se,'numpy_array_equal':ae,'all_finite':finite,'a_sha256':a['selected_ee_sha256'],'b_sha256':b['selected_ee_sha256'],'source_pair':'S0->S1','ordered_source_indices':[0,1],'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','same_field_object_handoff':False,'no_tolerance_rescue':True,'science_gate_scored':True,'ww_s0_s1_authority_created':False}; atomic_json(out,r); return r

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--replica',choices=['A','B','AB'],default='AB'); ap.add_argument('--r1-root',required=True); ap.add_argument('--r1-artifact-digest',required=True); ap.add_argument('--checkpoint-root',required=True); ap.add_argument('--source-head',required=True); ap.add_argument('--contract-fingerprint',required=True); ap.add_argument('--ab-out',required=True); a=ap.parse_args()
 if a.replica=='A':run_replica('A',a);return
 if a.replica=='B':run_replica('B',a);return
 ra=run_replica('A',a); rb=run_replica('B',a); print(compare(ra,rb,Path(a.ab_out))['status'])
if __name__=='__main__':main()
