#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
PASS='LAYERB_16385_TO_32769_CHUNK_ONE_RUN_AUTHORIZED_PLUS_0_PLUS_0'
FAIL='LAYERB_16385_TO_32769_CHUNK_ONE_RUN_NOT_AUTHORIZED_PLUS_0_PLUS_0'
GUARD_PASS='LAYERB_32769_CHUNK_ONE_LIVE_GUARD_PASS_PLUS_0_PLUS_0'

def git_blob(path):
    b=Path(path).read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),hashlib.sha256(b).hexdigest()

def independently_verified(key,d):
    if key=='v141_method':
        wf=d.get('workflow',{}); jobs=wf.get('jobs',{}); agg=d.get('aggregate',{})
        return wf.get('conclusion')=='success' and isinstance(jobs.get('independent_finalizer'),int) and agg.get('missing_roles')==[]
    return d.get('artifact_verified_independently') is True

def main():
    ap=argparse.ArgumentParser()
    for x in ('contract','guard','v141-authority','v142-authority','v143-authority','parent-refinement-authority','request-plan-authority','out'): ap.add_argument('--'+x,required=True)
    ap.add_argument('--current-run-id',required=True,type=int); a=ap.parse_args()
    c=json.loads(Path(a.contract).read_text()); g=json.loads(Path(a.guard).read_text()); errors=[]
    if c.get('schema')!='LAYERB_16385_TO_32769_CHUNK_PRODUCTION_CONTRACT_V0_1': errors.append('contract schema mismatch')
    if c.get('scientific_semantics',{}).get('relative_tolerance')!=0.001 or c.get('scientific_semantics',{}).get('strict_less_than') is not True: errors.append('frozen science tolerance mismatch')
    if c.get('scientific_semantics',{}).get('h')!=0.0001 or c.get('scientific_semantics',{}).get('native_k_per_decade_for_pk')!=20.0: errors.append('frozen science constants mismatch')
    if c.get('scientific_semantics',{}).get('covariance_restriction_authorized') is not False or c.get('scientific_semantics',{}).get('Wm_S3_opened') is not False: errors.append('downstream gate leak')
    if g.get('classification')!=GUARD_PASS or g.get('guard_pass') is not True or g.get('current_run_id')!=a.current_run_id or g.get('matching_other_live_authoritative_runs')!=0 or g.get('matching_other_all_status_runs')!=0: errors.append('one-live guard mismatch')
    bindings=[
      ('v141_method',a.v141_authority),('v142_resource',a.v142_authority),('v143_method',a.v143_authority),
      ('parent_refinement',a.parent_refinement_authority),('request_plan',a.request_plan_authority)
    ]
    observed={}
    for key,path in bindings:
        spec=c.get('authority_bindings',{}).get(key,{})
        try:
            blob,sha=git_blob(path); d=json.loads(Path(path).read_text()); observed[key]={'path':path,'git_blob':blob,'sha256':sha,'classification':d.get('classification'),'independently_verified':independently_verified(key,d)}
            if blob!=spec.get('git_blob'): errors.append(f'{key} blob mismatch')
            if spec.get('classification') is not None and d.get('classification')!=spec.get('classification'): errors.append(f'{key} classification mismatch')
            if not independently_verified(key,d): errors.append(f'{key} not independently verified')
        except Exception as e: errors.append(f'{key} validation error {type(e).__name__}: {e}')
    out={
      'schema':'LAYERB_16385_TO_32769_CHUNK_ONE_RUN_AUTHORIZATION_V0_1','effect':'+0/+0',
      'classification':PASS if not errors else FAIL,'execution_authorized':not errors,'authorized_canonical_run_count':1 if not errors else 0,
      'current_run_id':a.current_run_id,'production_workflow_path':c.get('production_workflow_path'),
      'scientific_response_persistence_authorized':not errors,
      'scientific_result_classification_authorized':not errors,
      'relative_tolerance':0.001,'strict_less_than':True,'h':0.0001,'native_k_per_decade_for_pk':20.0,
      'authority_bindings_observed':observed,'guard_json_sha256':hashlib.sha256(Path(a.guard).read_bytes()).hexdigest(),
      'errors':errors,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,
      'token':PASS if not errors else FAIL
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token']);
    if errors: print('ERRORS',json.dumps(errors))
    return 0 if not errors else 37
if __name__=='__main__': raise SystemExit(main())
