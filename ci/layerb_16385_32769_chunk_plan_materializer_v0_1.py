#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json
from pathlib import Path

EXPECTED_COARSE_PLAN_SHA='505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0'
EXPECTED_FINE_PLAN_SHA='0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e'
EXPECTED_COUNTS=(377,64,441,128)
EXPECTED_SLOTS=(10.0,10.0,20.0,20.0)
EXPECTED_COARSE_SCALARS=83666
EXPECTED_FINE_SCALARS=121682

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    ap=argparse.ArgumentParser()
    for x in ('frozen-engine','ir-script','request-plan-script','request-plan-authority','parent-root','parent-authority','manifest','angular-root','expim-root','boss-root','source','lens','camb-root','expz2-script','exp073iq-script','baseline','precision','scratch','out'):
        ap.add_argument('--'+x,required=True)
    a=ap.parse_args()
    eng=load('frozen_jl_plan_engine',a.frozen_engine)
    ir=load('frozen_ir_plan_engine',a.ir_script)
    planmod=load('frozen_plan_audit',a.request_plan_script)
    codec=load('chunk_call_codec',Path(__file__).with_name('layerb_chunk_call_codec_v0_1.py'))
    auth=json.loads(Path(a.request_plan_authority).read_text())
    if auth.get('classification')!='RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0': raise RuntimeError('invalid request-plan authority')
    if auth.get('coarse_common_plan_sha256')!=EXPECTED_COARSE_PLAN_SHA or auth.get('fine_plan_with_gl128_sha256')!=EXPECTED_FINE_PLAN_SHA: raise RuntimeError('request-plan authority hash mismatch')
    scratch=Path(a.scratch); scratch.mkdir(parents=True,exist_ok=True)
    audit=eng.run_request_plan_audit(planmod,a,scratch/'request_plan_audit.json')
    if audit.get('classification')!='RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0': raise RuntimeError('live plan audit classification mismatch')
    if audit.get('coarse_common_plan_sha256')!=EXPECTED_COARSE_PLAN_SHA or audit.get('fine_plan_with_gl128_sha256')!=EXPECTED_FINE_PLAN_SHA: raise RuntimeError('live plan digest mismatch')
    if audit.get('scientific_response_read') is not False or audit.get('class_solver_invoked') is not False: raise RuntimeError('plan audit touched science')
    eng.PlannerSuite.reset()
    planner_dir=scratch/'planner_ir'; planner_dir.mkdir(parents=True,exist_ok=True)
    planner_result=eng.run_ir_with_suite(ir,eng.PlannerSuite,a,planner_dir,planner_dir/'planner_result.json')
    if len(eng.PlannerSuite.instances)!=4: raise RuntimeError('planner instance count mismatch')
    slots=tuple(x.slot for x in eng.PlannerSuite.instances); counts=tuple(len(x.calls) for x in eng.PlannerSuite.instances)
    if slots!=EXPECTED_SLOTS or counts!=EXPECTED_COUNTS: raise RuntimeError(f'planner topology mismatch {slots} {counts}')
    coarse=eng.PlannerSuite.instances[0].calls+eng.PlannerSuite.instances[1].calls
    fine=eng.PlannerSuite.instances[2].calls+eng.PlannerSuite.instances[3].calls
    if eng.calls_scalar_count(coarse)!=EXPECTED_COARSE_SCALARS or eng.calls_scalar_count(fine)!=EXPECTED_FINE_SCALARS: raise RuntimeError('planner scalar count mismatch')
    out={
      'schema':'LAYERB_16385_32769_CHUNK_PRODUCTION_PLAN_V0_1','effect':'+0/+0',
      'scientific_response_read':False,'class_solver_invoked':False,'scientific_execution_authorized':False,
      'covariance_read':False,'Wm_S3_opened':False,
      'legacy_coarse_plan_sha256':EXPECTED_COARSE_PLAN_SHA,'legacy_fine_plan_sha256':EXPECTED_FINE_PLAN_SHA,
      'coarse_calls_digest':codec.calls_digest(coarse),'fine_calls_digest':codec.calls_digest(fine),
      'coarse_call_count':len(coarse),'fine_call_count':len(fine),
      'coarse_scalar_count':eng.calls_scalar_count(coarse),'fine_scalar_count':eng.calls_scalar_count(fine),
      'coarse_calls':codec.encode_calls(coarse),'fine_calls':codec.encode_calls(fine),
      'planner_inner_status_ignored':planner_result.get('status'),
      'token':'LAYERB_16385_32769_CHUNK_PRODUCTION_PLAN_MATERIALIZED_PLUS_0_PLUS_0'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
    print(out['token']); print('COARSE_DIGEST',out['coarse_calls_digest']); print('FINE_DIGEST',out['fine_calls_digest'])
    return 0
if __name__=='__main__': raise SystemExit(main())
