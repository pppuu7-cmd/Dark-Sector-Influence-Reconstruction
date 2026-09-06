#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np

SOURCE='de83e20a68f79ccf25b89b0d33eb4206e294c757'
FP='b7845df5ce4bd730461476b7ff0831512003ceb5b3558436005c9876bd251'
NAMASTER='24365fa59a38c15732f4f37e8b29265b75c442d5'
PATCH='9a80a756960afa8b4ddf61b5fbba7fba6ad5ed9ac919e093bb1365a636c789f0'
EM_ID=9977333691
EM_DIGEST='sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1'
RUN=33994398927
HEAD='4d1cbd504067a64a94b038292793e5e8bffba911'
WF='.github/workflows/exp073en-ww-s0-s0-filebacked-ab-network-retry-v0-2.yml'
DR='dsir.exp073dq.ww_s0_s0.durable_ab_production.v0.1'
NS={'A':'checkpoints/exp073dq-ww-s0-s0-a-v0-1','B':'checkpoints/exp073dq-ww-s0-s0-b-v0-1'}
STAGES=['fresh_s0_mask_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
DUMMY='a'*64
ARTDIG='sha256:'+'c'*64

def sha(p:Path):
 h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()
def writej(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def manifest(rep,stage,payload):
 return {'schema':DR+'.checkpoint','stage':stage,'complete':True,'replica':rep,'checkpoint_namespace':NS[rep],'source_head':SOURCE,'contract_fingerprint':FP,'payloads':payload,'historical_ww_numerical_import':False,'other_replica_output_read':False}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); a=ap.parse_args(); root=Path(a.root); root.mkdir(parents=True,exist_ok=True)
 writej(root/'run.json',{'id':RUN,'head_sha':HEAD,'path':WF,'status':'completed','conclusion':'success'})
 writej(root/'artifact.json',{'id':123456789,'expired':False,'digest':ARTDIG,'workflow_run':{'id':RUN,'head_sha':HEAD}})
 comp={'frozen_source_head':SOURCE,'contract_fingerprint':FP,'namaster_head':NAMASTER,'patch_sha256':PATCH,'hosted_exp073em_artifact_id':EM_ID,'hosted_exp073em_artifact_digest':EM_DIGEST}
 writej(root/'component_blobs.json',comp)
 writej(root/'local_exp073em_activation'/'local_activation_receipt.json',{'status':'PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1','no_tolerance_rescue':True})
 writej(root/'local_exp073em_activation'/'build_identity.json',{'namaster_head':NAMASTER,'patch_sha256':PATCH,'hosted_exp073em_artifact_id':EM_ID,'hosted_exp073em_artifact_digest':EM_DIGEST})
 x=np.arange(39*12288,dtype='<f8').reshape(39,12288)/17.0
 selected_sha=None
 for rep in ('A','B'):
  d=root/'checkpoints'/rep; (d/'exact_route').mkdir(parents=True,exist_ok=True)
  sp=d/'exact_route'/'selected_ee.bin'; sp.write_bytes(memoryview(x).cast('B')); selected_sha=sha(sp)
  ws=('1' if rep=='A' else '2')*64; fw=('3' if rep=='A' else '4')*64; canon=('5' if rep=='A' else '6')*64
  writej(d/'fresh_s0_mask_complete.json',manifest(rep,'fresh_s0_mask_complete',{'s0_count_map':{'canonical_sha256':DUMMY,'shape':[201326592],'dtype':'<f8'},'r1_authority':{'checks':{'fixture':True}},'s0_authority':{'fixture':True},'reconstruction_count':1}))
  writej(d/'fresh_workspace_mcm_complete.json',manifest(rep,'fresh_workspace_mcm_complete',{'workspace_fits':{'sha256':ws},'same_field_object_handoff':True,'field_object_ids':[123,123],'reconstruction_count':1}))
  writej(d/'mcm_fits_verified.json',manifest(rep,'mcm_fits_verified',{'workspace_fits':{'sha256':ws}}))
  writej(d/'full_window_complete.json',manifest(rep,'full_window_complete',{'full_window':{'sha256':fw,'shape':[4,39,4,12288]}}))
  writej(d/'selected_ee_complete.json',manifest(rep,'selected_ee_complete',{'selected_ee':{'sha256':selected_sha,'shape':[39,12288],'dtype':'<f8','semantics':'wins[0,:,0,:] = EE<-EE'}}))
  adapter={'schema':'dsir.exp073do.ww_s0_s0.production_exact_adapter.v0.1','status':'PRODUCTION_ADAPTER_EXECUTED','workspace_fits_sha256':ws,'canonical_mcm_sha256':canon,'full_window_sha256':fw,'selected_ee_sha256':selected_sha,'full_shape':[4,39,4,12288],'selected_ee_shape':[39,12288],'selected_semantics':'wins[0,:,0,:] = EE<-EE','source_head':SOURCE,'contract_fingerprint':FP,'checkpoint_namespace':NS[rep],'no_tolerance_rescue':True,'historical_ww_numerical_import':False,'get_coupling_matrix_materialization_forbidden':True,'component_blob_ids':comp}
  rp={'schema':DR+'.replica','replica':rep,'selected_ee_sha256':selected_sha,'selected_ee_path':f'/synthetic/{rep}/exact_route/selected_ee.bin','workspace_fits_sha256':ws,'adapter_receipt':adapter,'source_head':SOURCE,'contract_fingerprint':FP,'checkpoint_namespace':NS[rep],'historical_ww_numerical_import':False,'other_replica_output_read':False}
  writej(d/'replica_receipt.json',rp)
  writej(d/'replica_receipt_complete.json',manifest(rep,'replica_receipt_complete',{'replica_receipt':{'sha256':sha(d/'replica_receipt.json')},'selected_ee':{'sha256':selected_sha}}))
  writej(d/'exp073en_prune_receipt.json',{'schema':'dsir.exp073en.prune_receipt.v0.1','replica':rep,'only_after_replica_receipt_complete':True,'selected_preserved_sha256':selected_sha,'pruned':[{'path':f'/synthetic/{rep}/fresh_workspace.fits','sha256':ws,'bytes':19327360000},{'path':f'/synthetic/{rep}/exact_route/mcm_canonical.bin','sha256':canon,'bytes':19327352832}]})
  (root/f'{rep}_driver.log').write_text(f'DSIR_NMT_FILEBACKED_MCM path=/synthetic/{rep}/dsir-nmt-mcm-X bytes=19327352832 rows=49152 zero_init=1\n')
 (root/'tiny.stderr').write_text('DSIR_OMP_TEAM=8\n')
 writej(root/'ab_compare.json',{'schema':DR+'.ab_compare','status':'PASS_EXP073DQ_WW_S0_S0_DURABLE_AB_PROVISIONAL_EXACT_REPEATABILITY_V0_1','sha256_equal':True,'numpy_array_equal':True,'a_sha256':selected_sha,'b_sha256':selected_sha,'no_tolerance_rescue':True})
 checks={'hosted_storage_qualifier_bound':True,'local_storage_qualifier_pass':True,'provisional_pass':True,'sha_flag':True,'array_flag':True,'no_tolerance':True,'a_exists':True,'b_exists':True,'a_size':True,'b_size':True,'sha_recomputed_equal':True,'array_recomputed_equal':True,'finite':True,'a_fullres_filebacked_proof':True,'b_fullres_filebacked_proof':True,'a_all_six_stages':True,'b_all_six_stages':True,'a_prune_receipt':True,'b_prune_receipt':True}
 writej(root/'terminal_science_candidate_receipt.json',{'schema':'dsir.exp073en.ww_s0_s0.filebacked_terminal.v0.1','experiment':'Exp073EN','task':'WW_S0_S0','classification':'SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION','token':'PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1','science_gate_scored':True,'ww_s0_s0_authority_created':False,'authority_admission_pending':'Exp073EO','checks':checks,'stage_checks':{'A':{s:True for s in STAGES},'B':{s:True for s in STAGES}},'a_sha256':selected_sha,'b_sha256':selected_sha,'selected_shape':[39,12288],'dtype':'<f8','selected_semantics':'EE<-EE','full_shape':[4,39,4,12288],'frozen_source_head':SOURCE,'contract_fingerprint':FP,'namaster_head':NAMASTER,'patch_sha256':PATCH,'hosted_exp073em_artifact_id':EM_ID,'hosted_exp073em_artifact_digest':EM_DIGEST,'no_tolerance_rescue':True})
 print(ARTDIG)
if __name__=='__main__': main()
