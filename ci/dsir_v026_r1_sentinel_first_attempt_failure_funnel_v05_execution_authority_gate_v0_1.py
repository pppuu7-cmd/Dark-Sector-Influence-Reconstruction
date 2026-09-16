#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path

TARGET='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-5.yml'
TERMINAL='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-terminal-history-v0-5.yml'
ORCH='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-orchestrator-v0-5.yml'
STATIC='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_STATIC_AUDIT_AUTHORITY_V0_5.json'
AUTH='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_5.json'
REVIEW='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_V0_5.json'
TARGET_BLOB='6844ff90d251f31097b359486df80774883800f1'
TERMINAL_BLOB='27ac9ed1131f0443968307c2181d9a2fd97ccbe8'
ORCH_BLOB='3373b44582c7cfdd040a50cc1ade3b060c9c132e'
STATIC_BLOB='961490275981c7312e4b1c4aed95bbe63fb10987'
AUTH_BLOB='fee0ea62b0fa465643b9bfe5cafae01666680631'
REVIEW_BLOB='ee644f633d011021f0d4437fc8e096a7b16e5c91'
NONCE='DSIR-V026R1-FFHOSTED-V0-5-728EC746-60286B97-20260916-A1'

def sh(*a):return subprocess.check_output(a,text=True).strip()
def main():
    p=argparse.ArgumentParser();p.add_argument('--live-runs-json',required=True);p.add_argument('--out',required=True);a=p.parse_args()
    for path,blob in [(TARGET,TARGET_BLOB),(TERMINAL,TERMINAL_BLOB),(ORCH,ORCH_BLOB),(STATIC,STATIC_BLOB),(AUTH,AUTH_BLOB),(REVIEW,REVIEW_BLOB)]:
        assert sh('git','hash-object',path)==blob,(path,sh('git','hash-object',path),blob)
    s=json.loads(Path(STATIC).read_text()); x=json.loads(Path(AUTH).read_text()); r=json.loads(Path(REVIEW).read_text())
    assert s['status']=='TERMINAL_STATIC_AUDIT_AUTHORITY' and s['verdict']=='QUALIFIED'
    assert s['failure_funnel_dispatch_authorized_by_this_authority'] is False
    assert s['separate_execution_authority_gate_required'] is True
    assert s['target_dispatch_run_count']==0 and s['terminal_history_dispatch_run_count']==0 and s['orchestrator_dispatch_run_count']==0
    assert x['status']=='AUTHORIZED_SCOPED'
    assert x['execution_nonce']==NONCE and x['authorized_event']=='workflow_dispatch' and x['authorized_ref']=='refs/heads/main'
    assert x['authorized_run_number']==1 and x['authorized_run_attempt']==1
    assert x['authorized_orchestrator_dispatch_count']==1 and x['authorized_target_dispatch_count']==1 and x['authorized_terminal_history_dispatch_count']==1
    assert x['required_pre_execution_target_dispatch_count']==0 and x['required_pre_execution_terminal_history_dispatch_count']==0 and x['required_pre_execution_orchestrator_dispatch_count']==0
    assert x['competing_or_in_progress_sibling_dispatch_allowed'] is False
    assert x['rerun_allowed'] is False and x['second_attempt_allowed'] is False
    assert x['science_run_35033268924_rerun_authorized'] is False and x['same_nonce_second_attempt_authorized'] is False
    assert x['successor_sentinel_science_authorized'] is False and x['full_107_row_execution_authorized'] is False and x['downstream_science_authorized'] is False
    assert r['status']=='QUALIFIED' and r['verdict']=='QUALIFIED'
    assert r['reviewed_execution_authority_git_blob_sha1']==AUTH_BLOB
    assert r['reviewed_workflow_git_blob_sha1']==TARGET_BLOB
    assert r['reviewed_terminal_history_workflow_git_blob_sha1']==TERMINAL_BLOB
    assert r['reviewed_orchestrator_workflow_git_blob_sha1']==ORCH_BLOB
    assert r['reviewed_static_authority_git_blob_sha1']==STATIC_BLOB
    assert r['execution_nonce']==NONCE and r['authorized_ref']=='refs/heads/main' and r['authorized_event']=='workflow_dispatch'
    assert r['authorized_run_number']==1 and r['authorized_run_attempt']==1
    assert r['findings']['static_qualification_is_not_execution_authority'] is True
    assert r['findings']['all_runtime_workflow_histories_required_zero_before_activation'] is True
    assert r['findings']['orchestrator_must_wait_for_target_terminal_success'] is True
    assert r['findings']['terminal_history_auditor_must_run_after_target_terminal_success'] is True
    assert r['findings']['rerun_and_second_attempt_forbidden'] is True
    live=json.loads(Path(a.live_runs_json).read_text())
    assert set(live)=={'target','terminal','orchestrator'}
    for k,v in live.items():
        assert v['total_count']==0 and v['workflow_runs']==[],(k,v)
    out={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_5_EXECUTION_AUTHORITY_GATE_V0_1',
      'status':'TERMINAL_EXECUTION_AUTHORITY_GATE','verdict':'QUALIFIED',
      'classification':'V0_5_EXACT_ONE_SHOT_ORCHESTRATOR_EXECUTION_AUTHORITY_QUALIFIED',
      'execution_nonce':NONCE,'authorized_ref':'refs/heads/main','authorized_event':'workflow_dispatch',
      'target_workflow_git_blob_sha1':TARGET_BLOB,'terminal_history_workflow_git_blob_sha1':TERMINAL_BLOB,'orchestrator_workflow_git_blob_sha1':ORCH_BLOB,
      'static_authority_git_blob_sha1':STATIC_BLOB,'execution_authority_git_blob_sha1':AUTH_BLOB,'review_confirmation_git_blob_sha1':REVIEW_BLOB,
      'pre_gate_target_dispatch_count':0,'pre_gate_terminal_history_dispatch_count':0,'pre_gate_orchestrator_dispatch_count':0,
      'exact_one_orchestrator_dispatch_authorized_after_exact_promotion':True,
      'direct_target_dispatch_authorized':False,'direct_terminal_history_dispatch_authorized':False,
      'orchestrator_run_number_required':1,'orchestrator_run_attempt_required':1,
      'rerun_authorized':False,'second_orchestrator_dispatch_authorized':False,'same_nonce_second_attempt_authorized':False,
      'science_run_35033268924_rerun_authorized':False,'successor_sentinel_science_authorized':False,
      'full_107_row_execution_authorized':False,'downstream_science_authorized':False,
      'token':'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_5_EXECUTION_AUTHORITY_PLUS_0_PLUS_0'
    }
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(out['token'])
if __name__=='__main__':main()
