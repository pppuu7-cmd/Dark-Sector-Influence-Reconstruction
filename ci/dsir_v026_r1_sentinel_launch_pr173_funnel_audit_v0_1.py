#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

MAIN='6ccd564184456052a993593c43951604ccd3aaef'
HEAD='1403581d4d608d98597eaff2c77c80a98d6c3c6e'
PR=173
FILES={
 '.github/workflows/layerb-beta-v026-r1-sentinel-launch-package-static-audit-v0-1.yml':'09e3a4b14bacd33e451b5f35aa4dc78004ac7945',
 'ci/layerb_beta_v026_r1_sentinel_launch_package_static_audit_v0_1.py':'8efdccffcf0e740a799fd462c3988cdc20a29b1a',
 'docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_STATIC_AUDIT_CANDIDATE_V0_1.md':'4bbed7fc77e57aab82a72bf886c697cf6f07c1a6',
 'docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json':'4ba40e59e6a9d48636d95d07efab575e56ae0966',
 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_CONTRACT_V0_1.json':'26806597e651fb22956de59f102c0ad24d11c576',
 'docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json':'9c217e41764d979bea12644fae372354241bc976',
 'docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml':'19907175f0f3417ddee2aba6916d961c6be02e26',
}
W=FILES['docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml']
A=FILES['docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json']
L=FILES['docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json']
PACKAGE=FILES['docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_CONTRACT_V0_1.json']
STATIC_RUN=34959657394
STATIC_HEAD='5d42cd84ce54c9781d7bbefd41b01d3cf775fbd7'
STATIC_ART=10393170033
STATIC_ZIP='e95c4675db77a2ecd864d21e39dfdccffe289ed61a84ece95182f22c46e16184'
RECEIPT_SHA='133df1d2753c9228198a15be792fdcbbf99da243efeccdb785d610aad7dc5ee5'

ACTIVE_W='.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
ACTIVE_A='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
ACTIVE_L='docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
ACTIVE_Q='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'

UPSTREAM={
 'docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json':'b510d8e97baf1c0b7b216c0605d83cdd029254e9',
 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json':'cdbcea2622564d40aa9d1edc045a5808f8cdd1c4',
 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json':'e14804463d9eab288162b4c98e8dd5c1fd6a10eb',
 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_PR171_QUALIFICATION_AUDIT_V0_2.json':'5d042377fa48d896865db0ada11508015c74e350',
 'ci/layerb_beta_v026_r1_sentinel_v0_1.py':'9affe7c7d4e02bbc728ba15e3cde893ec9876b38',
 'ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py':'97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9',
}

def sh(*args): return subprocess.check_output(args,text=True).strip()
def blob(ref,path): return sh('git','rev-parse',f'{ref}:{path}')
def readj(p): return json.loads(Path(p).read_text())
def sha_file(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def member(z,n):
    with zipfile.ZipFile(z) as q: return q.read(n)

def assert_art(meta,aid,digest):
    assert meta['id']==aid and meta['expired'] is False and meta['digest']=='sha256:'+digest

def main():
    ap=argparse.ArgumentParser()
    for x in ['pr-json','pr-files-json','static-run-json','static-runs-json','static-art-json','static-zip','out']:
        ap.add_argument('--'+x,required=True)
    a=ap.parse_args()

    pr=readj(a.pr_json); fs=readj(a.pr_files_json)
    assert pr['number']==PR and pr['state']=='open' and pr['draft'] is True and pr['merged'] is False
    assert pr['base']['ref']=='main' and pr['base']['sha']==MAIN and pr['head']['sha']==HEAD
    assert sh('git','merge-base',MAIN,HEAD)==MAIN
    assert len(sh('git','rev-list',f'{MAIN}..{HEAD}').splitlines())==10
    assert {f['filename'] for f in fs}==set(FILES)
    assert all(f['status']=='added' and f.get('deletions',0)==0 for f in fs)
    for p,h in FILES.items(): assert blob(HEAD,p)==h,(p,blob(HEAD,p),h)
    for p,h in UPSTREAM.items(): assert blob(MAIN,p)==h,(p,blob(MAIN,p),h)
    assert not any(f['filename'] in (ACTIVE_W,ACTIVE_A,ACTIVE_L,ACTIVE_Q) for f in fs)

    # Read candidate objects as text/data only. Never execute W or any candidate science code.
    wpath='docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml'
    apath='docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json'
    lpath='docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json'
    cpath='docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_CONTRACT_V0_1.json'
    w=subprocess.check_output(['git','show',f'{HEAD}:{wpath}'],text=True)
    Aobj=json.loads(subprocess.check_output(['git','show',f'{HEAD}:{apath}']))
    Lobj=json.loads(subprocess.check_output(['git','show',f'{HEAD}:{lpath}']))
    C=json.loads(subprocess.check_output(['git','show',f'{HEAD}:{cpath}']))

    assert Aobj['schema']=='LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1'
    assert Aobj['status']=='TERMINAL_LAUNCH_AUTHORITY'
    assert Aobj['active_workflow_git_blob_sha1']==W
    assert Aobj['launch_descriptor_git_blob_bound_by_authority'] is False
    assert 'launch_descriptor_git_blob_sha1' not in Aobj
    assert Aobj['requires_separate_launch_package_qualification'] is True
    assert Aobj['authorized_launch_count']==1 and Aobj['sentinel_science_execution_authorized'] is True and Aobj['full_107_row_execution_authorized'] is False
    assert Aobj['r1_contract_git_blob_sha1']==UPSTREAM['docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json']
    assert Aobj['r1_promotion_authority_git_blob_sha1']==UPSTREAM['docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json']
    assert Aobj['sentinel_implementation_contract_git_blob_sha1']==UPSTREAM['docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json']
    assert Aobj['sentinel_implementation_qualification_git_blob_sha1']==UPSTREAM['docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_PR171_QUALIFICATION_AUDIT_V0_2.json']
    assert Aobj['executor_git_blob_sha1']==UPSTREAM['ci/layerb_beta_v026_r1_sentinel_v0_1.py']
    assert Aobj['decision_git_blob_sha1']==UPSTREAM['ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py']
    assert Aobj['forbidden']['mutual_authority_descriptor_blob_hash_cycle'] is True

    assert Lobj['schema']=='LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1'
    assert Lobj['status']=='FROZEN_ONE_RUN_LAUNCH_DESCRIPTOR'
    assert Lobj['active_workflow_git_blob_sha1']==W and Lobj['launch_authority_git_blob_sha1']==A
    assert Lobj['authorized_launch_count']==1 and Lobj['sentinel_science_execution_authorized'] is True and Lobj['full_107_row_execution_authorized'] is False
    assert Lobj['trigger_semantics']['final_operation_must_create_new_file_not_modify_existing_file'] is True
    assert Lobj['trigger_semantics']['workflow_run_attempt_must_equal']==1 and Lobj['trigger_semantics']['rerun_forbidden'] is True
    assert Lobj['package_qualification']['must_bind_exact_active_workflow_blob'] is True
    assert Lobj['package_qualification']['must_bind_exact_launch_authority_blob'] is True
    assert Lobj['package_qualification']['must_bind_exact_launch_descriptor_blob'] is True

    assert C['status']=='PROSPECTIVELY_FROZEN_INACTIVE_LAUNCH_PACKAGE_CANDIDATE_NOT_EXECUTABLE'
    P=C['acyclic_package']
    assert P['topology']=='W_TO_A_TO_L_THEN_STATIC_AUDIT_THEN_Q'
    assert P['W']['git_blob_sha1']==W and P['A']['git_blob_sha1']==A and P['L']['git_blob_sha1']==L
    assert P['A']['binds_W'] is True and P['A']['binds_L'] is False
    assert P['L']['binds_A'] is True and P['L']['binds_W'] is True
    assert C['forbidden']['mutual_A_L_final_blob_hash_cycle'] is True
    plan=C['activation_plan_after_future_package_qualification']
    assert plan['phase_1_promote_exact_W_to_active_path_and_exact_A_to_authority_path_without_L'] is True
    assert plan['phase_1_must_not_trigger_science'] is True
    assert plan['phase_2_promote_exact_Q_package_qualification'] is True and plan['phase_2_must_not_trigger_science'] is True
    assert plan['phase_3_create_exact_L_at_new_trigger_path'] is True and plan['phase_3_is_the_only_authorized_one_run_trigger'] is True
    assert plan['never_modify_L_after_trigger'] is True

    # Adversarial one-run and runtime guard inspection of W.
    required=[
      "branches: [main]",
      "- 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'",
      "permissions:\n  contents: read\n  actions: read",
      "cancel-in-progress: false",
      "test \"$EVENT_NAME\" = push",
      "test \"$CURRENT_RUN_ATTEMPT\" = 1",
      "assert added.count(launch)==1",
      "assert launch not in modified and launch not in removed",
      "assert ev.get('forced') is False",
      "assert len(rows)==1, len(rows)",
      "assert int(r.get('run_attempt',1))==1",
      "assert Q['active_workflow_git_blob_sha1']==blob(W)",
      "assert Q['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])",
      "assert Q['launch_descriptor_git_blob_sha1']==blob(os.environ['LAUNCH'])",
      "max-parallel: 32",
      "python-version: '3.12.3'",
      "'numpy==1.26.4' 'scipy==1.17.1'",
      "assert d['full_replay_launch_authorized'] is False",
      "assert d['full_107_row_execution_authorized'] is False",
    ]
    for n in required: assert n in w,n
    assert 'workflow_dispatch' not in w
    assert w.count('R01')>=1 and w.count('R32')>=1
    assert "pattern: layerb-beta-v026-r1-sentinel-R*" in w
    # Path-stale comments are non-executable and explicitly classified as cosmetic only.
    stale_comment=('Stored under docs/ and therefore inert.' in w)
    assert stale_comment is True

    sr=readj(a.static_run_json)
    assert sr['id']==STATIC_RUN and sr['head_sha']==STATIC_HEAD and sr['event']=='push' and sr['run_attempt']==1 and sr['conclusion']=='success'
    rows=readj(a.static_runs_json)['workflow_runs']; rr=[r for r in rows if r.get('path')=='.github/workflows/layerb-beta-v026-r1-sentinel-launch-package-static-audit-v0-1.yml']
    assert len(rr)==1 and rr[0]['id']==STATIC_RUN
    assert_art(readj(a.static_art_json),STATIC_ART,STATIC_ZIP)
    assert sha_file(a.static_zip)==STATIC_ZIP
    rb=member(a.static_zip,'launch_package_static_audit.json')
    assert len(rb)==1348 and hashlib.sha256(rb).hexdigest()==RECEIPT_SHA
    r=json.loads(rb)
    assert r['classification']=='SENTINEL_LAUNCH_PACKAGE_ACYCLIC_RESPONSE_BLIND_STATIC_AUDIT_PASS'
    assert r['W_git_blob_sha1']==W and r['A_git_blob_sha1']==A and r['L_git_blob_sha1']==L and r['package_contract_git_blob_sha1']==PACKAGE
    assert r['A_binds_W'] is True and r['A_binds_L'] is False and r['L_binds_A'] is True and r['L_binds_W'] is True
    for k in ['future_active_W_present','future_authority_A_present','future_trigger_L_present','future_package_Q_present','class_solver_invoked','scientific_response_read','sentinel_science_execution_authorized_by_this_receipt','full_107_row_execution_authorized']:
        assert r[k] is False,k
    assert r['one_run_new_file_trigger_guard_present'] is True and r['first_attempt_guard_present'] is True and r['unique_exact_head_workflow_run_guard_present'] is True and r['Q_runtime_gate_present'] is True
    assert hashlib.sha256(member(a.static_zip,'future_W_exact_copy.yml')).hexdigest()=='1d8de6326efb9de2cf0d0ed9c6107221820e8158b3a6b9ee99606227173457c4'
    assert hashlib.sha256(member(a.static_zip,'future_A_exact_copy.json')).hexdigest()=='b9b6b57f898b4abd089bb30a7def3542625a653e0737abd5d6c7a80bd0f6b549'
    assert hashlib.sha256(member(a.static_zip,'future_L_exact_copy.json')).hexdigest()=='bcc4ec835d504fa5bc64fbedd3d7ad98a5fd9744e19f41ce081ec9fe7ded8223'

    out={
      'schema':'DSIR_V0_26_R1_SENTINEL_LAUNCH_PR173_FUNNEL_AUDIT_V0_1',
      'verdict':'QUALIFIED','effect':'+0/+0','main_sha':MAIN,'pr_number':PR,'candidate_head':HEAD,
      'changed_file_count':7,'W_git_blob_sha1':W,'A_git_blob_sha1':A,'L_git_blob_sha1':L,'package_contract_git_blob_sha1':PACKAGE,
      'static_audit_run_id':STATIC_RUN,'static_audit_artifact_id':STATIC_ART,'static_audit_zip_sha256':STATIC_ZIP,'static_audit_receipt_sha256':RECEIPT_SHA,
      'provenance_topology':'W_TO_A_TO_L_THEN_STATIC_AUDIT_THEN_Q','A_binds_L':False,'L_binds_A':True,
      'candidate_future_workflow_executed_by_funnel_audit':False,'class_solver_invoked_by_funnel_audit':False,'scientific_response_read_by_funnel_audit':False,
      'stale_W_storage_comment_present':True,'stale_W_storage_comment_material_to_runtime':False,
      'sentinel_science_execution_authorized_by_this_receipt':False,'full_107_row_execution_authorized_by_this_receipt':False,
      'classification':'SENTINEL_ACYCLIC_LAUNCH_PACKAGE_QUALIFIED_FOR_INACTIVE_PROMOTION_AND_Q_CONSTRUCTION',
      'next_admissible_action':'PERSIST_EXTERNAL_PACKAGE_AUTHORITY; PROMOTE_EXACT_INACTIVE_PR173; CONSTRUCT_Q_BINDING_EXACT_W_A_L; THEN STAGE_EXACT_W_AND_A_WITHOUT_L_FOR_FINAL_PRETRIGGER_AUDIT',
      'token':'QUALIFIED_DSIR_V0_26_R1_SENTINEL_LAUNCH_PR173_FUNNEL_AUDIT_PLUS_0_PLUS_0'
    }
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'])
    return 0

if __name__=='__main__': raise SystemExit(main())
