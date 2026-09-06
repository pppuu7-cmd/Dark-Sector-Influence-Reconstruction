#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np

EE_SHAPE=(39,12288)
SOURCE_HEAD='de83e20a68f79ccf25b89b0d33eb4206e294c757'
CONTRACT='b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'
NAMESPACES={'A':'checkpoints/exp073fs-ww-s1-s2-a-v0-1','B':'checkpoints/exp073fs-ww-s1-s2-b-v0-1'}
STAGES=['fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
PASS='PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'
FAIL='FAIL_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'

def sha(p:Path)->str:
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''): h.update(b)
 return h.hexdigest()
def load(root:Path,rep:str):
 rr=root/'checkpoints'/rep; rp=rr/'replica_receipt.json'; ep=rr/'exact_route'/'selected_ee.bin'; cp=rr/'replica_receipt_complete.json'; pp=rr/'post_receipt_prune.json'
 if not all(p.is_file() for p in (rp,ep,cp,pp)): raise RuntimeError(f'fail-closed missing terminal/prune evidence {rep}')
 r=json.loads(rp.read_text()); c=json.loads(cp.read_text()); p=json.loads(pp.read_text())
 req={'replica':rep,'source_pair':'S1->S2','ordered_source_indices':[1,2],'same_field_object_handoff':False,'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','source_head':SOURCE_HEAD,'contract_fingerprint':CONTRACT,'checkpoint_namespace':NAMESPACES[rep],'historical_ww_numerical_import':False,'other_replica_output_read':False,'science_gate_scored':False}
 for k,v in req.items():
  if r.get(k)!=v: raise RuntimeError(f'fail-closed receipt identity {rep}:{k}')
 preq={'replica':rep,'checkpoint_namespace':NAMESPACES[rep],'source_head':SOURCE_HEAD,'contract_fingerprint':CONTRACT,'source_pair':'S1->S2','ordered_source_indices':[1,2],'same_field_object_handoff':False,'field_construction_count':2,'complete_chain_verified_before_prune':True,'preserved_complete_receipt':True,'pruned_only_after_receipt':True,'no_tolerance_rescue':True}
 for k,v in preq.items():
  if p.get(k)!=v: raise RuntimeError(f'fail-closed prune receipt {rep}:{k}')
 msh=p.get('stage_manifest_sha256',{})
 if set(msh)!=set(STAGES): raise RuntimeError(f'fail-closed stage inventory {rep}')
 for st in STAGES:
  sp=rr/(st+'.json')
  if not sp.is_file() or sha(sp)!=msh[st]: raise RuntimeError(f'fail-closed stage SHA {rep}:{st}')
  o=json.loads(sp.read_text())
  if o.get('stage')!=st or o.get('complete') is not True or o.get('replica')!=rep or o.get('checkpoint_namespace')!=NAMESPACES[rep] or o.get('source_head')!=SOURCE_HEAD or o.get('contract_fingerprint')!=CONTRACT: raise RuntimeError(f'fail-closed stage identity {rep}:{st}')
 src=json.loads((rr/'fresh_sources_complete.json').read_text())['payloads']; ws=json.loads((rr/'fresh_workspace_mcm_complete.json').read_text())['payloads']; ids=ws.get('field_object_ids',[])
 if src.get('ordered_source_indices')!=[1,2] or src.get('reconstruction_counts')!={'s1':1,'s2':1} or src.get('same_source_map_both_sides') is not False: raise RuntimeError(f'fail-closed source semantics {rep}')
 if ws.get('same_field_object_handoff') is not False or ws.get('field_construction_count')!=2 or len(ids)!=2 or ids[0]==ids[1]: raise RuntimeError(f'fail-closed distinct field semantics {rep}')
 d=sha(ep); hr=sha(rp); vp=p.get('verified_payload_sha256',{})
 if d!=r.get('selected_ee_sha256') or d!=c.get('payloads',{}).get('selected_ee',{}).get('sha256') or d!=p.get('selected_ee_sha256') or d!=vp.get('selected_ee'): raise RuntimeError(f'fail-closed selected SHA {rep}')
 if hr!=c.get('payloads',{}).get('replica_receipt',{}).get('sha256') or hr!=p.get('replica_receipt_sha256') or hr!=vp.get('replica_receipt'): raise RuntimeError(f'fail-closed receipt SHA {rep}')
 if ep.stat().st_size!=39*12288*8: raise RuntimeError(f'fail-closed selected bytes {rep}')
 return ep,d

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args(); root=Path(a.root)
 pa,ha=load(root,'A'); pb,hb=load(root,'B'); aa=np.memmap(pa,dtype='<f8',mode='r',shape=EE_SHAPE); bb=np.memmap(pb,dtype='<f8',mode='r',shape=EE_SHAPE)
 se=ha==hb; ae=bool(np.array_equal(aa,bb)); finite=bool(np.isfinite(aa).all() and np.isfinite(bb).all()); del aa,bb
 token=PASS if se and ae and finite else FAIL
 out={'schema':'dsir.exp073fs.ww_s1_s2_terminal_receipt_compare.v0.1','classification':'SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION' if token==PASS else 'SCIENTIFIC_FAIL','token':token,'science_gate_scored':True,'ww_s1_s2_authority_created':False,'source_pair':'S1->S2','ordered_source_indices':[1,2],'same_field_object_handoff':False,'selected_semantics':'EE<-EE','selected_shape':[39,12288],'selected_dtype':'<f8','a_sha256':ha,'b_sha256':hb,'sha256_equal':se,'numpy_array_equal':ae,'all_finite':finite,'source_head':SOURCE_HEAD,'contract_fingerprint':CONTRACT,'checkpoint_namespaces':[NAMESPACES['A'],NAMESPACES['B']],'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','historical_ww_numerical_import':False,'other_replica_output_read':False,'no_tolerance_rescue':True,'terminal_compare_restored_replica':False,'full_chain_verified_before_prune':True}
 Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(token)
if __name__=='__main__': main()
