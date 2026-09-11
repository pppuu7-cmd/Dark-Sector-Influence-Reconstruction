#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
PASS="LAYERB_16385_TO_32769_ONE_RUN_AUTHORIZED_PLUS_0_PLUS_0"; FAIL="LAYERB_16385_TO_32769_ONE_RUN_NOT_AUTHORIZED_PLUS_0_PLUS_0"; RESOURCE_PASS="LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"; GUARD_PASS="LAYERB_32769_ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS_PLUS_0_PLUS_0"
WORKFLOW=".github/workflows/layerb-16385-to-32769-canonical-scientific-v0-2.yml"; PARENT="7958e1f44c0224e1828f89b1472aa33226c61886"; NODE="82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"; TEXT="7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2"; BUILD="b5cd7304c110962dc3baef8d04ef67d5a8042e5f"; TERMINAL="e441c54f8ad4a0590ad521710d4b9dbf37f111ba"; TERMINAL_CONSUMER="661e0a69b7110fb0c0fcbb27fd6413456bb01ae2"; CONTRACT="a4e8b58711f520946d1195f739f111225d840ef8"
def bound(p):
 b=Path(p).read_bytes(); return json.loads(b),hashlib.sha256(b).hexdigest(),hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--contract',required=True); ap.add_argument('--resource-authority',required=True); ap.add_argument('--one-live-guard',required=True); ap.add_argument('--current-run-id',required=True,type=int); ap.add_argument('--out',required=True); a=ap.parse_args(); e=[]
 c,csha,cblob=bound(a.contract); r,rsha,rblob=bound(a.resource_authority); g,gsha,gblob=bound(a.one_live_guard)
 if cblob!=CONTRACT:e.append('contract_blob')
 if c.get('production_workflow_path')!=WORKFLOW or c.get('authorization_pass_classification')!=PASS or c.get('authorization_fail_classification')!=FAIL or c.get('authorized_canonical_run_count_if_pass')!=1 or c.get('retry_inference_forbidden') is not True or c.get('execution_authorized_by_contract_file_itself') is not False:e.append('contract_semantics')
 ident=c.get('bound_scientific_identity',{})
 if ident.get('parent_authority_git_blob')!=PARENT or ident.get('canonical_32769_node_sha256')!=NODE or ident.get('canonical_32769_text_sha256')!=TEXT or ident.get('class_build_authority_git_blob')!=BUILD or ident.get('terminal_contract_git_blob')!=TERMINAL or ident.get('terminal_consumer_git_blob')!=TERMINAL_CONSUMER:e.append('contract_identity')
 req=c.get('required_resource_authority',{})
 if r.get('classification')!=RESOURCE_PASS or r.get('artifact_verified_independently') is not True or r.get('high_memory_resource_lifecycle_preflight_pass') is not True:e.append('resource_classification')
 mem=r.get('candidate_memtotal_kb'); life=r.get('execution_lifecycle',{})
 if not isinstance(mem,int) or mem<=req.get('candidate_memtotal_kb_must_be_strictly_greater_than') or r.get('parser_capacity')!=1048576:e.append('resource_capacity_memory')
 if life.get('total_solver_constructions')!=4 or life.get('max_live_instances')!=1 or life.get('final_live_instances')!=0:e.append('resource_lifecycle')
 if r.get('scientific_response_read') is not False or r.get('scientific_authority_created') is not False or r.get('canonical_32769_node_sha256')!=NODE or r.get('class_build_authority_git_blob')!=BUILD:e.append('resource_identity')
 if g.get('classification')!=GUARD_PASS or g.get('guard_pass') is not True or g.get('errors')!=[] or g.get('current_run_id')!=a.current_run_id or g.get('production_workflow_path')!=WORKFLOW or g.get('matching_other_live_authoritative_runs')!=0 or g.get('matching_other_all_status_runs')!=0:e.append('guard_state')
 if g.get('parent_authority_git_blob')!=PARENT or g.get('canonical_32769_node_sha256')!=NODE or g.get('class_build_authority_git_blob')!=BUILD or g.get('parser_capacity')!=1048576 or g.get('scientific_response_read') is not False or g.get('scientific_execution_authorized') is not False:e.append('guard_identity')
 ok=not e; cls=PASS if ok else FAIL
 out={'schema':'LAYERB_16385_TO_32769_ONE_RUN_AUTHORIZATION_V0_2','classification':cls,'effect':'+0/+0','execution_authorized':ok,'authorized_canonical_run_count':1 if ok else 0,'current_run_id':a.current_run_id,'production_workflow_path':WORKFLOW,'errors':e,'authorization_contract_json_sha256':csha,'authorization_contract_git_blob':cblob,'resource_authority_json_sha256':rsha,'resource_authority_git_blob':rblob,'one_live_guard_json_sha256':gsha,'one_live_guard_git_blob':gblob,'parent_authority_git_blob':PARENT,'canonical_32769_node_sha256':NODE,'canonical_32769_text_sha256':TEXT,'class_build_authority_git_blob':BUILD,'parser_capacity':1048576,'terminal_contract_git_blob':TERMINAL,'terminal_consumer_git_blob':TERMINAL_CONSUMER,'scientific_response_read':False,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':cls}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(cls)
 if e: print('ERRORS',','.join(e))
 return 0 if ok else 31
if __name__=='__main__': raise SystemExit(main())
