#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
PASS='LAYERB_32769_CHUNK_ONE_LIVE_GUARD_PASS_PLUS_0_PLUS_0'
FAIL='LAYERB_32769_CHUNK_ONE_LIVE_GUARD_FAIL_PLUS_0_PLUS_0'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--runs-json',required=True); ap.add_argument('--current-run-id',required=True,type=int); ap.add_argument('--workflow-path',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    d=json.loads(Path(a.runs_json).read_text()); runs=d.get('workflow_runs',[])
    current=[r for r in runs if int(r.get('id',-1))==a.current_run_id]
    others=[r for r in runs if int(r.get('id',-1))!=a.current_run_id]
    live=[r for r in others if r.get('status') in ('queued','in_progress','waiting','pending','requested')]
    errors=[]
    if len(current)!=1: errors.append(f'current run multiplicity {len(current)}')
    if current and current[0].get('path')!=a.workflow_path: errors.append('current workflow path mismatch')
    if live: errors.append(f'other live production runs {[r.get("id") for r in live]}')
    if others: errors.append(f'prior/other production workflow runs exist {[r.get("id") for r in others]}')
    out={
      'schema':'LAYERB_32769_CHUNK_ONE_LIVE_GUARD_RESULT_V0_1','effect':'+0/+0',
      'classification':PASS if not errors else FAIL,'guard_pass':not errors,'errors':errors,
      'current_run_id':a.current_run_id,'production_workflow_path':a.workflow_path,
      'matching_current_runs':len(current),'matching_other_live_authoritative_runs':len(live),'matching_other_all_status_runs':len(others),
      'scientific_response_read':False,'scientific_execution_authorized':False,'scientific_authority_created':False,
      'covariance_restriction_authorized':False,'Wm_S3_opened':False,
      'token':PASS if not errors else FAIL
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token']);
    return 0 if not errors else 31
if __name__=='__main__': raise SystemExit(main())
