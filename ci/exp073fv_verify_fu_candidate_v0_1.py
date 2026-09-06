#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,math,struct
from pathlib import Path
STAGES=['fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
PASS='PASS_EXP073FU_WW_S1_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'
SOURCE_HEAD='de83e20a68f79ccf25b89b0d33eb4206e294c757'
CONTRACT='b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'

def sha(p:Path):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''): h.update(b)
 return h.hexdigest()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--log',required=True); a=ap.parse_args(); root=Path(a.root)
 log=Path(a.log).read_bytes().decode('utf-8','replace')
 for t in ('PASS_EXP073FU_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1','PASS_EXP073FU_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1',PASS,'PASS_EXP073FU_LIVE_EXCLUSIVITY'): assert t in log,t
 term=json.loads((root/'terminal_receipt.json').read_text())
 expected={'classification':'SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION','token':PASS,'science_gate_scored':True,'ww_s1_s3_authority_created':False,'source_pair':'S1->S3','ordered_source_indices':[1,3],'same_field_object_handoff':False,'selected_semantics':'EE<-EE','selected_shape':[39,12288],'selected_dtype':'<f8','sha256_equal':True,'numpy_array_equal':True,'all_finite':True,'source_head':SOURCE_HEAD,'contract_fingerprint':CONTRACT,'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','no_tolerance_rescue':True,'terminal_compare_restored_replica':False,'full_chain_verified_before_prune':True}
 for k,v in expected.items(): assert term.get(k)==v,(k,term.get(k),v)
 eps=[]
 for rep in ('A','B'):
  rr=root/'checkpoints'/rep; rp=rr/'replica_receipt.json'; cp=rr/'replica_receipt_complete.json'; pp=rr/'post_receipt_prune.json'; ep=rr/'exact_route'/'selected_ee.bin'
  rec=json.loads(rp.read_text()); comp=json.loads(cp.read_text()); prune=json.loads(pp.read_text()); src=json.loads((rr/'fresh_sources_complete.json').read_text())['payloads']; ws=json.loads((rr/'fresh_workspace_mcm_complete.json').read_text())['payloads']; ad=rec['adapter_receipt']
  assert rec['source_pair']=='S1->S3' and rec['ordered_source_indices']==[1,3] and rec['same_field_object_handoff'] is False and rec['historical_ww_numerical_import'] is False and rec['other_replica_output_read'] is False
  assert src['ordered_source_indices']==[1,3] and src['reconstruction_counts']=={'s1':1,'s3':1} and src['same_source_map_both_sides'] is False
  ids=ws['field_object_ids']; assert ws['field_construction_count']==2 and ws['same_field_object_handoff'] is False and len(ids)==2 and ids[0]!=ids[1]
  assert ad['mcm_backing_bytes']==19327352832 and ad['mcm_filebacked'] is True and ad['mcm_proc_maps'] is True and ad['read_unbinned_MCM'] is True and ad['route']=='public_get_bandpower_windows_after_filebacked_fits_read' and ad['public_full_shape']==[4,39,4,12288] and ad['selected_semantics']=='wins[0,:,0,:] = EE<-EE' and ad['no_tolerance_rescue'] is True
  assert prune['complete_chain_verified_before_prune'] is True and prune['pruned_only_after_receipt'] is True and prune['same_field_object_handoff'] is False and prune['field_construction_count']==2 and set(prune['stage_manifest_sha256'])==set(STAGES)
  for st in STAGES:
   sp=rr/(st+'.json'); assert sha(sp)==prune['stage_manifest_sha256'][st]
  he=sha(ep); assert he==rec['selected_ee_sha256']==prune['selected_ee_sha256']==comp['payloads']['selected_ee']['sha256'] and ep.stat().st_size==39*12288*8
  eps.append((ep,he))
 assert eps[0][1]==eps[1][1]==term['a_sha256']==term['b_sha256']
 ba=eps[0][0].read_bytes(); bb=eps[1][0].read_bytes(); assert ba==bb and all(math.isfinite(x[0]) for x in struct.iter_unpack('<d',ba))
 print('PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1')
 print('classification=SCIENTIFIC_AUTHORITY_ADMITTED')
 print('ww_s1_s3_authority_created=true')
if __name__=='__main__': main()
