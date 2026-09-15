#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

EXPECTED = {
  'r1_contract': ('docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json','b510d8e97baf1c0b7b216c0605d83cdd029254e9'),
  'promotion_authority': ('docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json','cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'),
  'executor': ('ci/layerb_beta_v026_r1_sentinel_v0_1.py','9affe7c7d4e02bbc728ba15e3cde893ec9876b38'),
  'decision': ('ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py','97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9'),
  'blueprint': ('docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_SCIENCE_WORKFLOW_CANDIDATE_V0_1.yml','1ed36c850d80537646556a858204cac14eca852e'),
  'implementation_contract': ('docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json','e14804463d9eab288162b4c98e8dd5c1fd6a10eb'),
}
SOURCE_PLAN_SHA='c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064'
SOURCE_PLAN_BYTES=3953984
ACTIVE_SCIENCE='.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
LAUNCH_AUTH='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
LAUNCH_SENTINEL='docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'


def blob(path): return subprocess.check_output(['git','hash-object',path],text=True).strip()
def sha(b): return hashlib.sha256(b).hexdigest()

def main():
  ap=argparse.ArgumentParser(); ap.add_argument('--plan',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
  for name,(p,h) in EXPECTED.items():
    if not Path(p).is_file() or blob(p)!=h: raise RuntimeError(f'{name} blob mismatch')
  if Path(ACTIVE_SCIENCE).exists(): raise RuntimeError('active sentinel science workflow exists before authority')
  if Path(LAUNCH_AUTH).exists(): raise RuntimeError('sentinel launch authority exists before static audit authority')
  if Path(LAUNCH_SENTINEL).exists(): raise RuntimeError('sentinel launch file exists before static audit authority')

  raw=Path(a.plan).read_bytes()
  if len(raw)!=SOURCE_PLAN_BYTES or sha(raw)!=SOURCE_PLAN_SHA: raise RuntimeError('source plan identity mismatch')
  plan=json.loads(raw)
  if len(plan['coarse_calls'])!=441 or len(plan['fine_calls'])!=569 or plan['coarse_calls']!=plan['fine_calls'][:441]: raise RuntimeError('source plan shape mismatch')

  C=json.load(open(EXPECTED['implementation_contract'][0])); R=json.load(open(EXPECTED['r1_contract'][0])); A=json.load(open(EXPECTED['promotion_authority'][0]))
  if C['schema']!='LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1': raise RuntimeError('implementation schema')
  if C['status']!='PROSPECTIVELY_FROZEN_IMPLEMENTATION_CANDIDATE_NOT_EXECUTABLE': raise RuntimeError('implementation status')
  if C['effect']!='+0/+0': raise RuntimeError('effect')
  if A['verdict']!='QUALIFIED' or A['post_promotion_authorization']['sentinel_response_blind_static_audit_required'] is not True: raise RuntimeError('construction authority')
  if A['sentinel_science_execution_authorized'] is not False or A['full_107_row_execution_authorized'] is not False: raise RuntimeError('authority boundary')
  if R['sentinel']['lane_count']!=32 or R['sentinel']['class_constructions_per_lane']!=14: raise RuntimeError('R1 sentinel geometry')
  if C['sentinel_geometry']['lane_count']!=32 or C['sentinel_geometry']['class_constructions_per_lane']!=14: raise RuntimeError('implementation geometry')
  if C['sentinel_geometry']['mixed_batches']!=['M076','M298','M300']: raise RuntimeError('mixed selections')
  if C['sentinel_geometry']['direct_comparators']!={'M076':'D50','M298':'D00','M300':'D58'}: raise RuntimeError('direct comparators')
  if C['sentinel_geometry']['total_possible_class_constructions_if_all_32_eligible']!=448: raise RuntimeError('total sentinel construction accounting')
  if C['power']!={
    'minimum_eligible_lanes':6,'minimum_native_avx512_active':3,'minimum_native_avx512_inactive':3,
    'both_native_classes_required':True,'science_retry_to_change_native_class_mix_forbidden':True}: raise RuntimeError('power identity')

  exe=Path(EXPECTED['executor'][0]).read_text(); dec=Path(EXPECTED['decision'][0]).read_text(); wf=Path(EXPECTED['blueprint'][0]).read_text()
  for needle in ["raise RuntimeError('sentinel science launch authority is required and absent')","require_launch_authority(a.launch_authority, a.contract)","from classy import Class"]:
    if needle not in exe: raise RuntimeError(f'executor missing {needle}')
  child=exe[exe.index('def child(a):'):exe.index('def lane(a):')]
  if child.index('require_launch_authority(a.launch_authority, a.contract)') > child.index('from classy import Class'): raise RuntimeError('child can import CLASS before launch authority')
  lane=exe[exe.index('def lane(a):'):exe.index('def main():')]
  if lane.index('require_launch_authority(a.launch_authority, a.contract)') > lane.index("v025 = load('v025_for_v026_sentinel_lane'"): raise RuntimeError('lane imports numerical chain before launch authority')
  for forbidden in ["'full_layerb_107_row_traversal_launched': True","'full_replay_launch_authorized':True","'full_107_row_execution_authorized':True"]:
    if forbidden in exe or forbidden in dec: raise RuntimeError('implementation contains forbidden authorization true')

  if '# INERT CANDIDATE BLUEPRINT' not in wf: raise RuntimeError('workflow blueprint not marked inert')
  if 'max-parallel: 32' not in wf: raise RuntimeError('workflow max parallel mismatch')
  if wf.count('R01')<1 or wf.count('R32')<1: raise RuntimeError('workflow matrix endpoints missing')
  if "pattern: layerb-beta-v026-r1-sentinel-R*" not in wf: raise RuntimeError('decision lane download missing')
  if "assert d['full_replay_launch_authorized'] is False" not in wf: raise RuntimeError('workflow decision firewall missing')
  if LAUNCH_AUTH not in wf or LAUNCH_SENTINEL not in wf: raise RuntimeError('future launch bindings absent')

  if "'SENTINEL_INVALID'" not in dec or "'SENTINEL_PASS'" not in dec: raise RuntimeError('decision hierarchy endpoints missing')
  if "'full_replay_launch_authorized':False" not in dec or "'full_107_row_execution_authorized':False" not in dec: raise RuntimeError('decision does not remain fail-closed')
  if "primitive_response_metrics" not in dec: raise RuntimeError('complete primitive metrics field missing')

  pre=Path(a.out).with_name('executor_static_preflight.json')
  subprocess.run(['python3',EXPECTED['executor'][0],'--mode','static-preflight','--contract',EXPECTED['r1_contract'][0],'--plan',a.plan,'--out',str(pre)],check=True)
  P=json.loads(pre.read_text())
  if P['token']!='PASS_LAYERB_BETA_V0_26_R1_SENTINEL_STATIC_PREFLIGHT_PLUS_0_PLUS_0': raise RuntimeError('static preflight token')
  if P['class_solver_invoked'] is not False or P['scientific_response_read'] is not False or P['science_execution_authorized'] is not False: raise RuntimeError('static preflight touched science')
  if P['launch_authority_present'] is not False: raise RuntimeError('launch authority unexpectedly present')
  if P['class_constructions_per_lane']!=14: raise RuntimeError('static preflight construction count')

  fail=Path(a.out).with_name('lane_without_authority.txt')
  forbidden_lane=Path(a.out).with_name('must_not_exist_lane.json')
  cp=subprocess.run(['python3',EXPECTED['executor'][0],'--mode','lane','--replicate','R01','--contract',EXPECTED['r1_contract'][0],'--plan',a.plan,'--out',str(forbidden_lane)],text=True,capture_output=True)
  fail.write_text(cp.stdout+'\n---STDERR---\n'+cp.stderr)
  if cp.returncode==0: raise RuntimeError('lane unexpectedly ran without launch authority')
  if 'sentinel science launch authority is required and absent' not in cp.stderr: raise RuntimeError('lane failed for unexpected reason')
  if forbidden_lane.exists(): raise RuntimeError('unauthorized lane produced output')

  subprocess.run(['python3','-m','py_compile',EXPECTED['executor'][0],EXPECTED['decision'][0],str(Path(__file__))],check=True)
  out={
    'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_STATIC_AUDIT_V0_2','classification':'SENTINEL_IMPLEMENTATION_RESPONSE_BLIND_STATIC_AUDIT_PASS',
    'effect':'+0/+0','r1_contract_blob':EXPECTED['r1_contract'][1],'promotion_authority_blob':EXPECTED['promotion_authority'][1],
    'implementation_contract_blob':EXPECTED['implementation_contract'][1],'executor_blob':EXPECTED['executor'][1],'decision_blob':EXPECTED['decision'][1],
    'workflow_blueprint_blob':EXPECTED['blueprint'][1],'source_plan_sha256':SOURCE_PLAN_SHA,
    'historical_v0_1_auditor_status':'SUPERSEDED_PRE_EXECUTION_SYNTAX_DEFECT_NO_HOSTED_RUN',
    'active_science_workflow_present':False,'launch_authority_present':False,'launch_sentinel_present':False,
    'lane_without_launch_authority_failed_closed':True,'class_solver_invoked':False,'scientific_response_read':False,'covariance_read':False,
    'sentinel_science_execution_authorized':False,'full_107_row_execution_authorized':False,
    'next_admissible_action':'INDEPENDENT_FUNNEL_REVIEW_THEN_SEPARATE_EXPLICIT_SENTINEL_LAUNCH_AUTHORITY_IF_QUALIFIED',
    'token':'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_STATIC_AUDIT_PLUS_0_PLUS_0'
  }
  Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
  print(out['token'])
  return 0
if __name__=='__main__': raise SystemExit(main())
