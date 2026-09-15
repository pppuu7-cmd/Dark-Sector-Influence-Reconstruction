#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess, zipfile
from pathlib import Path

MAIN='438ab2e6732512cf50c163719ade01575257b209'
HEAD='973eea003e6e246b7e1853b5469cb0a7d90c8177'
PR=171
FILES={
 '.github/workflows/layerb-beta-v026-r1-sentinel-static-audit-v0-1.yml':'a7eb32f900431b73daf9d5c2c7b98d0137755475',
 'ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py':'97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9',
 'ci/layerb_beta_v026_r1_sentinel_static_audit_v0_2.py':'ebb1db6b365560e9e4c8ab7e575d163bdab58cc4',
 'ci/layerb_beta_v026_r1_sentinel_v0_1.py':'9affe7c7d4e02bbc728ba15e3cde893ec9876b38',
 'docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_STATIC_AUDIT_CANDIDATE_V0_1.md':'d2a89f0f143a1af4c844248f4385d6b1a55d16e5',
 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json':'e14804463d9eab288162b4c98e8dd5c1fd6a10eb',
 'docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_SCIENCE_WORKFLOW_CANDIDATE_V0_1.yml':'1ed36c850d80537646556a858204cac14eca852e',
}
STATIC_RUN=34958187529
STATIC_HEAD='510a7145bd5ea49e45db3ab53e56093567da746f'
STATIC_ART=10392400462
STATIC_ZIP='2384436ee78a9a1ee4d55e5297e3b36f2dff9ffe53a243e20af0b2f7dfe729f0'
PLAN_ART=10298655751
PLAN_ZIP='9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7'
PLAN_SHA='c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064'


def sh(*x): return subprocess.check_output(x,text=True).strip()
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def readj(p): return json.loads(Path(p).read_text())
def member(z,n):
 with zipfile.ZipFile(z) as q: return q.read(n)
def blob(ref,p): return sh('git','rev-parse',f'{ref}:{p}')

def main():
 ap=argparse.ArgumentParser()
 for k in ['pr-json','pr-files-json','static-run-json','static-runs-json','static-art-json','static-zip','plan-art-json','plan-zip','out']:
  ap.add_argument('--'+k,required=True)
 a=ap.parse_args()
 pr=readj(a.pr_json); fs=readj(a.pr_files_json)
 assert pr['number']==PR and pr['state']=='open' and pr['draft'] is True and pr['merged'] is False
 assert pr['base']['ref']=='main' and pr['base']['sha']==MAIN and pr['head']['sha']==HEAD
 assert sh('git','merge-base',MAIN,HEAD)==MAIN
 assert len(sh('git','rev-list',f'{MAIN}..{HEAD}').splitlines())==9
 assert {x['filename'] for x in fs}==set(FILES)
 assert all(x['status']=='added' and x.get('deletions',0)==0 for x in fs)
 for p,h in FILES.items(): assert blob(HEAD,p)==h,(p,blob(HEAD,p),h)
 assert not any(x['filename']=='.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml' for x in fs)
 assert not any('SENTINEL_LAUNCH_AUTHORITY' in x['filename'] or 'SENTINEL_LAUNCH_V0_1' in x['filename'] for x in fs)

 C=json.loads(subprocess.check_output(['git','show',f"{HEAD}:docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json"]))
 assert C['status']=='PROSPECTIVELY_FROZEN_IMPLEMENTATION_CANDIDATE_NOT_EXECUTABLE'
 assert C['effect']=='+0/+0'
 assert C['base_main_sha']==MAIN
 assert C['r1_contract']['git_blob_sha1']=='b510d8e97baf1c0b7b216c0605d83cdd029254e9'
 assert C['construction_authority']['git_blob_sha1']=='cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'
 assert C['construction_authority']['sentinel_science_execution_authorized'] is False
 assert C['construction_authority']['full_107_row_execution_authorized'] is False
 I=C['implementation']; assert I['executor_git_blob_sha1']==FILES[I['executor_path']]
 assert I['decision_git_blob_sha1']==FILES[I['decision_path']]
 assert I['workflow_blueprint_git_blob_sha1']==FILES[I['workflow_blueprint_path']]
 assert I['active_science_workflow_must_be_absent_before_launch_authority'] is True
 assert I['launch_authority_must_be_absent_during_static_audit'] is True
 assert I['launch_sentinel_must_be_absent_during_static_audit'] is True
 G=C['sentinel_geometry']; assert G['lane_count']==32 and G['class_constructions_per_lane']==14 and G['total_possible_class_constructions_if_all_32_eligible']==448
 assert G['mixed_batches']==['M076','M298','M300'] and G['direct_comparators']=={'M076':'D50','M298':'D00','M300':'D58'}
 assert C['power']['minimum_eligible_lanes']==6 and C['power']['minimum_native_avx512_active']==3 and C['power']['minimum_native_avx512_inactive']==3
 assert C['fail_closed_authorization']['executor_lane_requires_launch_authority_argument'] is True
 assert C['fail_closed_authorization']['executor_child_requires_launch_authority_argument'] is True
 assert C['decision_semantics']['SENTINEL_PASS_does_not_authorize_full_replay'] is True

 # Candidate science code is inspected as text only; never executed here.
 exe=subprocess.check_output(['git','show',f"{HEAD}:ci/layerb_beta_v026_r1_sentinel_v0_1.py"],text=True)
 dec=subprocess.check_output(['git','show',f"{HEAD}:ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py"],text=True)
 bp=subprocess.check_output(['git','show',f"{HEAD}:docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_SCIENCE_WORKFLOW_CANDIDATE_V0_1.yml"],text=True)
 assert "require_launch_authority(a.launch_authority, a.contract)" in exe
 child=exe[exe.index('def child(a):'):exe.index('def lane(a):')]
 assert child.index('require_launch_authority(a.launch_authority, a.contract)') < child.index('from classy import Class')
 lane=exe[exe.index('def lane(a):'):exe.index('def main():')]
 assert lane.index('require_launch_authority(a.launch_authority, a.contract)') < lane.index("v025 = load('v025_for_v026_sentinel_lane'")
 assert "'full_replay_launch_authorized':False" in dec and "'full_107_row_execution_authorized':False" in dec
 assert '# INERT CANDIDATE BLUEPRINT' in bp and 'max-parallel: 32' in bp
 # Qualification: active-workflow self-binding is not yet present in the inert blueprint and must be added at activation.
 workflow_self_binding_present=('workflow_git_blob_sha1' in bp and '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml' in bp)
 launch_file_self_binding_present=('launch_sentinel_git_blob_sha1' in bp)
 assert workflow_self_binding_present is False
 assert launch_file_self_binding_present is False

 sr=readj(a.static_run_json); assert sr['id']==STATIC_RUN and sr['head_sha']==STATIC_HEAD and sr['conclusion']=='success' and sr['run_attempt']==1
 runs=readj(a.static_runs_json)['workflow_runs']; rr=[x for x in runs if x.get('path')=='.github/workflows/layerb-beta-v026-r1-sentinel-static-audit-v0-1.yml']
 assert len(rr)==1 and rr[0]['id']==STATIC_RUN
 sam=readj(a.static_art_json); assert sam['id']==STATIC_ART and sam['digest']=='sha256:'+STATIC_ZIP and sam['expired'] is False
 assert sha(a.static_zip)==STATIC_ZIP
 rb=member(a.static_zip,'sentinel_static_audit.json'); assert len(rb)==1344 and hashlib.sha256(rb).hexdigest()=='33972dc25eabb7a19097164234b5e336d4bc4bd3cfef37ff8a442443810b75a8'
 r=json.loads(rb); assert r['classification']=='SENTINEL_IMPLEMENTATION_RESPONSE_BLIND_STATIC_AUDIT_PASS'
 assert r['executor_blob']==FILES['ci/layerb_beta_v026_r1_sentinel_v0_1.py'] and r['decision_blob']==FILES['ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py']
 for k in ['active_science_workflow_present','launch_authority_present','launch_sentinel_present','class_solver_invoked','scientific_response_read','sentinel_science_execution_authorized','full_107_row_execution_authorized']:
  assert r[k] is False,k
 assert r['lane_without_launch_authority_failed_closed'] is True
 pb=member(a.static_zip,'executor_static_preflight.json'); assert hashlib.sha256(pb).hexdigest()=='63429e12875545d0a3d0be01882c6bf9b71dd5e26a840fe739b969fa3f5be3bb'
 p=json.loads(pb); assert p['class_constructions_per_lane']==14 and p['grid896_sha256']=='8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d'
 lb=member(a.static_zip,'lane_without_authority.txt'); assert hashlib.sha256(lb).hexdigest()=='8ebb37d6a3d51d46e259f2eb66d5622162a5494cc94f085c52534d501208991d'
 assert b'sentinel science launch authority is required and absent' in lb

 pam=readj(a.plan_art_json); assert pam['id']==PLAN_ART and pam['digest']=='sha256:'+PLAN_ZIP and pam['expired'] is False
 assert sha(a.plan_zip)==PLAN_ZIP
 pb=member(a.plan_zip,'plan.json'); assert len(pb)==3953984 and hashlib.sha256(pb).hexdigest()==PLAN_SHA

 out={
  'schema':'DSIR_V0_26_R1_SENTINEL_PR171_FUNNEL_AUDIT_V0_1','verdict':'QUALIFIED','effect':'+0/+0',
  'main_sha':MAIN,'pr_number':PR,'candidate_head':HEAD,'changed_file_count':7,
  'executor_blob':FILES['ci/layerb_beta_v026_r1_sentinel_v0_1.py'],'decision_blob':FILES['ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py'],
  'implementation_contract_blob':FILES['docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json'],
  'workflow_blueprint_blob':FILES['docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_SCIENCE_WORKFLOW_CANDIDATE_V0_1.yml'],
  'static_audit_run_id':STATIC_RUN,'static_audit_artifact_id':STATIC_ART,'static_audit_zip_sha256':STATIC_ZIP,
  'static_audit_receipt_sha256':'33972dc25eabb7a19097164234b5e336d4bc4bd3cfef37ff8a442443810b75a8',
  'source_plan_sha256':PLAN_SHA,'candidate_science_code_executed_by_funnel_audit':False,
  'sentinel_science_execution_authorized_by_receipt':False,'full_107_row_execution_authorized_by_receipt':False,
  'qualification_required_before_activation':{
    'active_workflow_must_bind_its_own_git_blob_in_launch_authority':True,
    'launch_sentinel_git_blob_must_be_bound_in_launch_authority':True,
    'active_workflow_and_launch_objects_require_separate_static_launch_audit':True,
    'explicit_one_run_launch_authority_required':True
  },
  'classification':'SENTINEL_IMPLEMENTATION_QUALIFIED_FOR_PROMOTION_WITH_LAUNCH_BINDING_HARDENING_REQUIRED',
  'next_admissible_action':'PERSIST_FUNNEL_AUTHORITY_THEN_PROMOTE_EXACT_PR171_IMPLEMENTATION; AFTER_PROMOTION_CONSTRUCT_ACTIVE_WORKFLOW_AND_LAUNCH_OBJECTS_WITH_SELF_BINDINGS_FOR_SEPARATE_STATIC_LAUNCH_AUDIT',
  'token':'QUALIFIED_DSIR_V0_26_R1_SENTINEL_PR171_FUNNEL_AUDIT_PLUS_0_PLUS_0'
 }
 Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(out['token'])
 return 0
if __name__=='__main__': raise SystemExit(main())
