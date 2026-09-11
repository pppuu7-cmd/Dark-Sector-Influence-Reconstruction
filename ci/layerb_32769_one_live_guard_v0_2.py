#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
PASS="LAYERB_32769_ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS_PLUS_0_PLUS_0"; FAIL="LAYERB_32769_ONE_LIVE_ANTI_DUPLICATION_GUARD_FAIL_PLUS_0_PLUS_0"
WORKFLOW=".github/workflows/layerb-16385-to-32769-canonical-scientific-v0-2.yml"; PARENT="7958e1f44c0224e1828f89b1472aa33226c61886"; NODE="82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"; BUILD="b5cd7304c110962dc3baef8d04ef67d5a8042e5f"; CONTRACT="9e20a5f3a6cb36c185edf48ad74857f20e8f62d8"
def blob(b): return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--runs-json',required=True); ap.add_argument('--contract',required=True); ap.add_argument('--current-run-id',required=True,type=int); ap.add_argument('--out',required=True); a=ap.parse_args(); e=[]
 cb=Path(a.contract).read_bytes(); c=json.loads(cb)
 if blob(cb)!=CONTRACT:e.append('contract_blob')
 if c.get('production_workflow_path')!=WORKFLOW:e.append('workflow')
 r=c.get('initial_run_rule',{}); ident=c.get('bound_scientific_identity',{})
 if r.get('exclude_current_run_id') is not True or r.get('allowed_other_matching_workflow_runs')!=0 or r.get('any_prior_matching_production_run_blocks_initial_authorization') is not True:e.append('initial_rule')
 if ident.get('parent_authority_git_blob')!=PARENT or ident.get('canonical_32769_node_sha256')!=NODE or ident.get('class_build_authority_git_blob')!=BUILD or ident.get('parser_capacity')!=1048576:e.append('identity')
 runs=json.loads(Path(a.runs_json).read_text()).get('workflow_runs');
 if not isinstance(runs,list): e.append('workflow_runs_missing'); runs=[]
 matches=[]; current=False
 for x in runs:
  if not isinstance(x,dict) or x.get('path')!=WORKFLOW: continue
  if x.get('id')==a.current_run_id: current=True; continue
  matches.append({'id':x.get('id'),'status':x.get('status'),'conclusion':x.get('conclusion'),'head_sha':x.get('head_sha'),'run_attempt':x.get('run_attempt')})
 if not current:e.append('current_run_not_seen')
 live=[x for x in matches if x.get('status') in {'queued','in_progress'}]; prior=[x for x in matches if x.get('status')=='completed']; unknown=[x for x in matches if x.get('status') not in {'queued','in_progress','completed'}]
 if live:e.append('other_live_matching_run')
 if prior:e.append('prior_matching_production_run')
 if unknown:e.append('unknown_matching_run_status')
 ok=not e and not matches; cls=PASS if ok else FAIL
 out={'schema':'LAYERB_32769_ONE_LIVE_GUARD_RESULT_V0_2','classification':cls,'effect':'+0/+0','guard_pass':ok,'errors':e,'guard_contract_git_blob':CONTRACT,'current_run_id':a.current_run_id,'production_workflow_path':WORKFLOW,'matching_other_live_authoritative_runs':len(live),'matching_other_all_status_runs':len(matches),'matching_other_completed_runs':len(prior),'parent_authority_git_blob':PARENT,'canonical_32769_node_sha256':NODE,'class_build_authority_git_blob':BUILD,'parser_capacity':1048576,'queried_run_ids':[x.get('id') for x in matches],'scientific_response_read':False,'scientific_execution_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':cls}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(cls)
 if e: print('ERRORS',','.join(e))
 return 0 if ok else 31
if __name__=='__main__': raise SystemExit(main())
