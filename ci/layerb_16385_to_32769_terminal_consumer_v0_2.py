#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,importlib.util,json
from pathlib import Path
BUILD="b5cd7304c110962dc3baef8d04ef67d5a8042e5f"; BUILD_CLASS="LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_V0_2_PASS_PLUS_0_PLUS_0"; PARSER=1048576; MEM=16373452; WORKFLOW=".github/workflows/layerb-16385-to-32769-canonical-scientific-v0-2.yml"; PASS="LAYERB_16385_TO_32769_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0"; FAIL="LAYERB_16385_TO_32769_TERMINAL_VALIDATION_FAIL_PLUS_0_PLUS_0"
def load_old():
 p=Path(__file__).with_name('layerb_16385_to_32769_terminal_consumer_v0_1.py'); spec=importlib.util.spec_from_file_location('terminal_v01_frozen',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--resource-authority',required=True); ap.add_argument('--one-live-guard',required=True); ap.add_argument('--one-run-authorization',required=True); ap.add_argument('--out',required=True); a=ap.parse_args(); old=load_old(); pre=[]
 result=json.loads(Path(a.input).read_text()); resource,rsha,rblob=old.load_bound(a.resource_authority); guard,gsha,gblob=old.load_bound(a.one_live_guard); auth,asha,ablob=old.load_bound(a.one_run_authorization)
 ba=result.get('class_build_authority',{})
 if ba.get('authority_git_blob')!=BUILD or ba.get('classification')!=BUILD_CLASS or ba.get('class_commit')!='ac627d54e9ce196a08878d1ba33999819925d19c' or ba.get('capacity')!=32769 or ba.get('parser_capacity')!=PARSER: pre.append('parser_corrected_class_build_authority')
 if resource.get('class_build_authority_git_blob')!=BUILD or resource.get('parser_capacity')!=PARSER or not isinstance(resource.get('candidate_memtotal_kb'),int) or resource['candidate_memtotal_kb']<=MEM: pre.append('parser_corrected_resource_authority')
 if guard.get('class_build_authority_git_blob')!=BUILD or guard.get('parser_capacity')!=PARSER or guard.get('production_workflow_path')!=WORKFLOW: pre.append('parser_corrected_guard')
 if auth.get('class_build_authority_git_blob')!=BUILD or auth.get('parser_capacity')!=PARSER or auth.get('production_workflow_path')!=WORKFLOW: pre.append('parser_corrected_authorization')
 validation={'valid':False,'errors':pre,'classification':result.get('classification'),'max_relative_component_difference':result.get('convergence',{}).get('max_relative_component_difference'),'strict_relative_tolerance':old.REL_TOL}
 if not pre:
  old.BUILD_AUTH_BLOB=BUILD; old.HOSTED_MEMTOTAL_KB=MEM
  normalized=copy.deepcopy(result); normalized['class_build_authority']['classification']='LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_PASS_PLUS_0_PLUS_0'; normalized['class_build_authority']['parser_capacity']=524288
  validation=old.validate(normalized,resource,rsha,rblob,guard,gsha,gblob,auth,asha,ablob)
 cls=PASS if validation['valid'] else FAIL
 out={'schema':'LAYERB_16385_TO_32769_TERMINAL_VALIDATION_V0_2','classification':cls,'effect':'+0/+0','validation':validation,'parser_corrected_infrastructure_precheck_pass':not pre,'frozen_v0_1_strict_classifier_reused':True,'resource_authority_json_sha256':rsha,'resource_authority_git_blob':rblob,'one_live_guard_json_sha256':gsha,'one_live_guard_git_blob':gblob,'one_run_authorization_json_sha256':asha,'one_run_authorization_git_blob':ablob,'class_build_authority_git_blob':BUILD,'parser_capacity':PARSER,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':cls}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(cls)
 if validation['errors']: print('ERRORS',','.join(validation['errors']))
 return 0 if validation['valid'] else 31
if __name__=='__main__': raise SystemExit(main())
