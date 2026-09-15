#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

EXPECTED = {
    'r1_contract': ('docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json','b510d8e97baf1c0b7b216c0605d83cdd029254e9'),
    'r1_promotion': ('docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json','cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'),
    'implementation_contract': ('docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json','e14804463d9eab288162b4c98e8dd5c1fd6a10eb'),
    'implementation_qualification': ('docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_PR171_QUALIFICATION_AUDIT_V0_2.json','5d042377fa48d896865db0ada11508015c74e350'),
    'executor': ('ci/layerb_beta_v026_r1_sentinel_v0_1.py','9affe7c7d4e02bbc728ba15e3cde893ec9876b38'),
    'decision': ('ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py','97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9'),
    'W': ('docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml','19907175f0f3417ddee2aba6916d961c6be02e26'),
    'A': ('docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json','4ba40e59e6a9d48636d95d07efab575e56ae0966'),
    'L': ('docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json','9c217e41764d979bea12644fae372354241bc976'),
    'package_contract': ('docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_CONTRACT_V0_1.json','26806597e651fb22956de59f102c0ad24d11c576'),
}

ACTIVE_W = '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
ACTIVE_A = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
ACTIVE_L = 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
ACTIVE_Q = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'


def blob(path: str) -> str:
    return subprocess.check_output(['git','hash-object',path], text=True).strip()


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); args=ap.parse_args()
    for name,(p,h) in EXPECTED.items():
        if not Path(p).is_file(): raise RuntimeError(f'missing {name}: {p}')
        got=blob(p)
        if got!=h: raise RuntimeError(f'{name} blob mismatch {got} != {h}')
    for p in (ACTIVE_W,ACTIVE_A,ACTIVE_L,ACTIVE_Q):
        if Path(p).exists(): raise RuntimeError(f'active/final path must be absent during package audit: {p}')

    W=Path(EXPECTED['W'][0]).read_text()
    A=json.load(open(EXPECTED['A'][0])); L=json.load(open(EXPECTED['L'][0])); C=json.load(open(EXPECTED['package_contract'][0]))

    if A['schema']!='LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1' or A['status']!='TERMINAL_LAUNCH_AUTHORITY': raise RuntimeError('A schema/status')
    if A['active_workflow_git_blob_sha1']!=EXPECTED['W'][1]: raise RuntimeError('A does not bind W')
    if A['launch_descriptor_git_blob_bound_by_authority'] is not False: raise RuntimeError('A claims to bind L')
    if 'launch_descriptor_git_blob_sha1' in A: raise RuntimeError('A contains forbidden final L hash')
    if A['requires_separate_launch_package_qualification'] is not True: raise RuntimeError('A does not require Q')
    if A['authorized_launch_count']!=1 or A['sentinel_science_execution_authorized'] is not True or A['full_107_row_execution_authorized'] is not False: raise RuntimeError('A launch boundary')
    if A['r1_contract_git_blob_sha1']!=EXPECTED['r1_contract'][1] or A['r1_promotion_authority_git_blob_sha1']!=EXPECTED['r1_promotion'][1]: raise RuntimeError('A R1 upstream')
    if A['sentinel_implementation_contract_git_blob_sha1']!=EXPECTED['implementation_contract'][1] or A['sentinel_implementation_qualification_git_blob_sha1']!=EXPECTED['implementation_qualification'][1]: raise RuntimeError('A implementation upstream')
    if A['executor_git_blob_sha1']!=EXPECTED['executor'][1] or A['decision_git_blob_sha1']!=EXPECTED['decision'][1]: raise RuntimeError('A implementation code')

    if L['schema']!='LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1' or L['status']!='FROZEN_ONE_RUN_LAUNCH_DESCRIPTOR': raise RuntimeError('L schema/status')
    if L['active_workflow_git_blob_sha1']!=EXPECTED['W'][1] or L['launch_authority_git_blob_sha1']!=EXPECTED['A'][1]: raise RuntimeError('L does not bind exact W/A')
    if L['authorized_launch_count']!=1 or L['sentinel_science_execution_authorized'] is not True or L['full_107_row_execution_authorized'] is not False: raise RuntimeError('L launch boundary')
    if L['trigger_semantics']['final_operation_must_create_new_file_not_modify_existing_file'] is not True or L['trigger_semantics']['workflow_run_attempt_must_equal']!=1 or L['trigger_semantics']['rerun_forbidden'] is not True: raise RuntimeError('L one-run semantics')
    if L['package_qualification']['must_bind_exact_active_workflow_blob'] is not True or L['package_qualification']['must_bind_exact_launch_authority_blob'] is not True or L['package_qualification']['must_bind_exact_launch_descriptor_blob'] is not True: raise RuntimeError('L Q binding requirements')

    if C['status']!='PROSPECTIVELY_FROZEN_INACTIVE_LAUNCH_PACKAGE_CANDIDATE_NOT_EXECUTABLE': raise RuntimeError('package contract status')
    P=C['acyclic_package']
    if P['topology']!='W_TO_A_TO_L_THEN_STATIC_AUDIT_THEN_Q': raise RuntimeError('DAG topology')
    if P['W']['git_blob_sha1']!=EXPECTED['W'][1] or P['A']['git_blob_sha1']!=EXPECTED['A'][1] or P['L']['git_blob_sha1']!=EXPECTED['L'][1]: raise RuntimeError('package contract W/A/L binding')
    if P['A']['binds_W'] is not True or P['A']['binds_L'] is not False or P['L']['binds_A'] is not True or P['L']['binds_W'] is not True: raise RuntimeError('package edge directions')
    if C['forbidden']['mutual_A_L_final_blob_hash_cycle'] is not True: raise RuntimeError('cycle firewall missing')

    needles=[
      "paths:\n      - 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'",
      "test \"$CURRENT_RUN_ATTEMPT\" = 1",
      "assert added.count(launch)==1",
      "assert launch not in modified and launch not in removed",
      "actions/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml/runs?head_sha=${CURRENT_HEAD_SHA}&event=push",
      "assert Q['active_workflow_git_blob_sha1']==blob(W)",
      "assert Q['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])",
      "assert Q['launch_descriptor_git_blob_sha1']==blob(os.environ['LAUNCH'])",
      "max-parallel: 32",
      "python-version: '3.12.3'",
      "'numpy==1.26.4' 'scipy==1.17.1'",
      "assert d['full_replay_launch_authorized'] is False",
      "assert d['full_107_row_execution_authorized'] is False",
    ]
    for n in needles:
        if n not in W: raise RuntimeError(f'W missing required guard: {n}')
    if 'workflow_dispatch' in W: raise RuntimeError('science W must not allow workflow_dispatch')
    if 'cancel-in-progress: false' not in W: raise RuntimeError('concurrency rerun guard missing')
    if W.count('R01')<1 or W.count('R32')<1: raise RuntimeError('32-lane matrix endpoints missing')

    # Prove the candidate bytes are path-independent git blobs for future exact copy.
    tmp=Path(args.out).with_name('future_W_exact_copy.yml'); tmp.parent.mkdir(parents=True,exist_ok=True); tmp.write_bytes(Path(EXPECTED['W'][0]).read_bytes())
    if blob(str(tmp))!=EXPECTED['W'][1]: raise RuntimeError('future W copy blob mismatch')
    tmpa=Path(args.out).with_name('future_A_exact_copy.json'); tmpa.write_bytes(Path(EXPECTED['A'][0]).read_bytes())
    if blob(str(tmpa))!=EXPECTED['A'][1]: raise RuntimeError('future A copy blob mismatch')
    tmpl=Path(args.out).with_name('future_L_exact_copy.json'); tmpl.write_bytes(Path(EXPECTED['L'][0]).read_bytes())
    if blob(str(tmpl))!=EXPECTED['L'][1]: raise RuntimeError('future L copy blob mismatch')

    out={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_STATIC_AUDIT_V0_1',
      'classification':'SENTINEL_LAUNCH_PACKAGE_ACYCLIC_RESPONSE_BLIND_STATIC_AUDIT_PASS',
      'effect':'+0/+0',
      'W_git_blob_sha1':EXPECTED['W'][1], 'A_git_blob_sha1':EXPECTED['A'][1], 'L_git_blob_sha1':EXPECTED['L'][1],
      'package_contract_git_blob_sha1':EXPECTED['package_contract'][1],
      'provenance_topology':'W_TO_A_TO_L_THEN_Q',
      'A_binds_W':True,'A_binds_L':False,'L_binds_A':True,'L_binds_W':True,
      'future_active_W_present':False,'future_authority_A_present':False,'future_trigger_L_present':False,'future_package_Q_present':False,
      'one_run_new_file_trigger_guard_present':True,'first_attempt_guard_present':True,'unique_exact_head_workflow_run_guard_present':True,
      'Q_runtime_gate_present':True,'class_solver_invoked':False,'scientific_response_read':False,'covariance_read':False,
      'sentinel_science_execution_authorized_by_this_receipt':False,'full_107_row_execution_authorized':False,
      'next_admissible_action':'INDEPENDENT_LAUNCH_PACKAGE_FUNNEL_AUDIT_THEN_CREATE_Q_AND_STAGE_W_A_WITHOUT_L_IF_QUALIFIED',
      'token':'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_STATIC_AUDIT_PLUS_0_PLUS_0'
    }
    Path(args.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'])
    return 0

if __name__=='__main__': raise SystemExit(main())
