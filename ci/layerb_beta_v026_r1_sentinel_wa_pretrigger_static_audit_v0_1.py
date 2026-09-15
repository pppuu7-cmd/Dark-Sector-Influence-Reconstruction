#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

W='.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
A='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
L='docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
Q='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'
Q_CAND='docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json'
Q_FUNNEL='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_Q_FUNNEL_QUALIFICATION_V0_1.json'
W_SOURCE='docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml'
A_SOURCE='docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json'
EXPECTED={
 W:'19907175f0f3417ddee2aba6916d961c6be02e26',
 A:'4ba40e59e6a9d48636d95d07efab575e56ae0966',
 W_SOURCE:'19907175f0f3417ddee2aba6916d961c6be02e26',
 A_SOURCE:'4ba40e59e6a9d48636d95d07efab575e56ae0966',
 Q_CAND:'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd',
 Q_FUNNEL:'43696ebc566c23871c0bcd94feca40bb9c03d82c',
 'docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json':'b510d8e97baf1c0b7b216c0605d83cdd029254e9',
 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json':'e14804463d9eab288162b4c98e8dd5c1fd6a10eb',
 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_PR171_QUALIFICATION_AUDIT_V0_2.json':'5d042377fa48d896865db0ada11508015c74e350',
 'ci/layerb_beta_v026_r1_sentinel_v0_1.py':'9affe7c7d4e02bbc728ba15e3cde893ec9876b38',
 'ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py':'97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9',
}

def blob(p:str)->str:
    return subprocess.check_output(['git','hash-object',p],text=True).strip()

def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument('--runs-json',required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    for p,h in EXPECTED.items():
        if not Path(p).is_file(): raise RuntimeError(f'missing {p}')
        got=blob(p)
        if got!=h: raise RuntimeError(f'blob mismatch {p}: {got} != {h}')
    if Path(L).exists(): raise RuntimeError('final L must be absent during W/A pretrigger staging')
    if Path(Q).exists(): raise RuntimeError('final Q must be absent during W/A pretrigger staging')

    a=json.load(open(A)); qc=json.load(open(Q_CAND)); qf=json.load(open(Q_FUNNEL))
    if a['schema']!='LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1' or a['status']!='TERMINAL_LAUNCH_AUTHORITY': raise RuntimeError('A schema/status')
    if a['active_workflow_git_blob_sha1']!=EXPECTED[W]: raise RuntimeError('A W binding')
    if a['requires_separate_launch_package_qualification'] is not True: raise RuntimeError('A Q requirement')
    if a['launch_descriptor_git_blob_bound_by_authority'] is not False: raise RuntimeError('A must not bind L')
    if a['sentinel_science_execution_authorized'] is not True or a['full_107_row_execution_authorized'] is not False: raise RuntimeError('A boundary')
    if qc['candidate_storage']['candidate_storage_is_inert'] is not True: raise RuntimeError('Q candidate storage')
    if qc['sentinel_science_execution_authorized'] is not True or qc['full_107_row_execution_authorized'] is not False: raise RuntimeError('future Q content')
    if qf['verdict']!='QUALIFIED' or qf['classification']!='SENTINEL_PACKAGE_Q_QUALIFIED_FOR_INACTIVE_PROMOTION_TO_MAIN': raise RuntimeError('Q funnel authority')
    if qf['sentinel_science_execution_authorized'] is not False or qf['full_107_row_execution_authorized'] is not False: raise RuntimeError('Q funnel execution boundary')

    w=Path(W).read_text()
    needles=[
      'branches: [main]',
      "- 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'",
      "PACKAGE_QUALIFICATION: 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'",
      "test \"$CURRENT_RUN_ATTEMPT\" = 1",
      "assert Q['active_workflow_git_blob_sha1']==blob(W)",
      "assert Q['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])",
      "assert Q['launch_descriptor_git_blob_sha1']==blob(os.environ['LAUNCH'])",
      "assert Q['full_107_row_execution_authorized'] is False",
      'max-parallel: 32',
      "python-version: '3.12.3'",
      "'numpy==1.26.4' 'scipy==1.17.1'",
    ]
    for n in needles:
        if n not in w: raise RuntimeError(f'W missing frozen guard: {n}')
    if 'workflow_dispatch:' in w: raise RuntimeError('science W must not have workflow_dispatch')

    runs=json.load(open(args.runs_json)).get('workflow_runs',[])
    sentinel_runs=[r for r in runs if r.get('path')==W or r.get('name')=='layerb-beta-v026-r1-sentinel-science-v0-1']
    if sentinel_runs: raise RuntimeError(f'sentinel workflow executed at pretrigger head: {[(r.get("id"),r.get("status"),r.get("conclusion")) for r in sentinel_runs]}')

    result={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_WA_PRETRIGGER_STATIC_AUDIT_V0_1',
      'token':'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_WA_PRETRIGGER_STATIC_AUDIT_PLUS_0_PLUS_0',
      'classification':'SENTINEL_WA_STAGING_FAIL_CLOSED_PRETRIGGER_STATIC_AUDIT_PASS',
      'effect':'+0/+0',
      'head_sha':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
      'W_git_blob_sha1':EXPECTED[W],
      'A_git_blob_sha1':EXPECTED[A],
      'Q_candidate_git_blob_sha1':EXPECTED[Q_CAND],
      'Q_funnel_authority_git_blob_sha1':EXPECTED[Q_FUNNEL],
      'L_present':False,
      'final_Q_present':False,
      'sentinel_workflow_run_count_at_exact_head':0,
      'W_trigger_branch_main_only':True,
      'W_trigger_path_final_L_only':True,
      'W_workflow_dispatch_absent':True,
      'A_requires_Q':True,
      'A_does_not_bind_L':True,
      'candidate_Q_is_inert':True,
      'class_solver_invoked':False,
      'scientific_response_read':False,
      'covariance_read':False,
      'sentinel_science_execution_authorized_by_this_receipt':False,
      'full_107_row_execution_authorized':False,
      'next_admissible_action':'INDEPENDENT_WA_PRETRIGGER_FUNNEL_REVIEW_BEFORE_ANY_MAIN_STAGING; FINAL_L_REMAINS_FORBIDDEN',
    }
    Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token'])
if __name__=='__main__': main()
