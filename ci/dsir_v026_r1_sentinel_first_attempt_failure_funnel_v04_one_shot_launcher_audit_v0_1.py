#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

LAUNCHER='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-v04-one-shot-launcher.yml'
LAUNCHER_BLOB='df5f94df25dfc98dc5ff387a5b685092c6d2a5c5'
TARGET='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-4.yml'; TARGET_BLOB='6bf2027a121348823914e9076338055a4820162e'
POST='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-post-run-history-v0-4.yml'; POST_BLOB='6c2617e756877fb3cbb8b27dcf16b2bfc164cab5'
EXEC='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_4.json'; EXEC_BLOB='d68aa9ffa3fb5a7768e6802146aed74a3b57cf1b'
REVIEW='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_V0_4.json'; REVIEW_BLOB='01e5e9e0145e8c2ad1f0da639f3de073d9b26da2'
STATIC='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_STATIC_AUDIT_AUTHORITY_V0_4.json'; STATIC_BLOB='6bbacdc70dbfbee1dc4753e4a05266f9dbe45399'
GATE='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_TERMINAL_EXECUTION_AUTHORITY_GATE_V0_1.json'; GATE_BLOB='35578c8eab01b11474c00b5306abe0c0fae7ac70'
NONCE='DSIR-V026R1-FFHOSTED-V0-4-10E7F9BD-7072FA7F-20260916-A1'
AUTH_TRIGGER='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_TERMINAL_ONE_SHOT_LAUNCH_AUTHORITY_V0_1.json'

def h(p): return subprocess.check_output(['git','hash-object',p],text=True).strip()
def j(p): return json.loads(Path(p).read_text())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live-runs-json',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    for p,b in [(LAUNCHER,LAUNCHER_BLOB),(TARGET,TARGET_BLOB),(POST,POST_BLOB),(EXEC,EXEC_BLOB),(REVIEW,REVIEW_BLOB),(STATIC,STATIC_BLOB),(GATE,GATE_BLOB)]:
        assert h(p)==b,(p,h(p),b)
    gate=j(GATE)
    assert gate['status']=='TERMINAL_EXECUTION_AUTHORITY_GATE' and gate['verdict']=='QUALIFIED'
    assert gate['classification']=='V0_4_EXACT_ONE_FIRST_LIVE_FAILURE_FUNNEL_DISPATCH_AUTHORITY_QUALIFIED'
    assert gate['hosted_workflow_git_blob_sha1']==TARGET_BLOB
    assert gate['post_run_history_workflow_git_blob_sha1']==POST_BLOB
    assert gate['execution_authority_git_blob_sha1']==EXEC_BLOB
    assert gate['execution_authority_review_git_blob_sha1']==REVIEW_BLOB
    assert gate['runtime_static_authority_git_blob_sha1']==STATIC_BLOB
    assert gate['execution_nonce']==NONCE
    assert gate['authorized_ref']=='refs/heads/main' and gate['authorized_event']=='workflow_dispatch'
    assert gate['authorized_run_number']==1 and gate['authorized_run_attempt']==1
    assert gate['live_history_at_terminal_gate']['prior_target_dispatch_count']==0
    assert gate['live_history_at_terminal_gate']['parallel_or_in_progress_target_sibling_count']==0
    assert gate['exact_promotion_to_main_authorized'] is True
    assert gate['atomic_pre_dispatch_recheck_required'] is True
    assert gate['single_target_dispatch_authorized_after_exact_promotion_and_atomic_preflight'] is True
    assert gate['failure_funnel_dispatch_authorized_now'] is False
    for k in ['rerun_authorized','second_dispatch_authorized','same_nonce_second_attempt_authorized','science_run_35033268924_rerun_authorized','successor_sentinel_science_authorized','full_107_row_execution_authorized','downstream_science_authorized']:
        assert gate[k] is False,k

    src=Path(LAUNCHER).read_text()
    required=[
      'branches:\n      - main',
      AUTH_TRIGGER,
      'actions: write',
      'contents: read',
      'test "$GITHUB_REF" = "refs/heads/main"',
      'test "$GITHUB_RUN_NUMBER" = "1"',
      'test "$GITHUB_RUN_ATTEMPT" = "1"',
      'assert len(exact)==0, preflight',
      'assert len(active)==0, preflight',
      "'execution_nonce':os.environ['EXECUTION_NONCE']",
      "'execution_authority_blob_sha1':os.environ['EXECUTION_AUTHORITY_BLOB']",
      "'execution_authority_review_blob_sha1':os.environ['EXECUTION_AUTHORITY_REVIEW_BLOB']",
      "'terminal_static_audit_authority_blob_sha1':os.environ['RUNTIME_STATIC_AUTHORITY_BLOB']",
      '/actions/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-4.yml/dispatches',
      "'ref':'main'",
      "method='POST'",
      "'dispatch_call_count':1",
      "assert status in (200,204), record",
      "assert launch['exactly_one_dispatch_authorized'] is True",
      "assert launch['rerun_authorized'] is False",
      "assert launch['second_dispatch_authorized'] is False",
      "assert launch['successor_sentinel_science_authorized'] is False",
      "assert launch['full_107_row_execution_authorized'] is False",
    ]
    for marker in required: assert marker in src,marker
    assert src.count("method='POST'")==1,src.count("method='POST'")
    assert src.count('/dispatches')==1,src.count('/dispatches')
    preflight_pos=src.index("assert len(exact)==0, preflight")
    dispatch_pos=src.index('/dispatches')
    assert preflight_pos < dispatch_pos
    assert 'rerun_workflow' not in src
    assert 'rerun-failed-jobs' not in src
    assert 'workflow_dispatch:' not in src.split('permissions:',1)[0]

    live=j(a.live_runs_json); runs=live.get('workflow_runs',[])
    assert int(live.get('total_count',len(runs)))==0,runs
    assert runs==[]

    out={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_ONE_SHOT_LAUNCHER_STATIC_AUDIT_V0_1',
      'status':'TERMINAL_LAUNCHER_STATIC_AUDIT','verdict':'QUALIFIED',
      'classification':'V0_4_ONE_SHOT_LAUNCHER_FAIL_CLOSED_AND_SINGLE_DISPATCH_STATICALLY_QUALIFIED',
      'effect':'+0/+0',
      'reviewed_launcher_workflow_git_blob_sha1':LAUNCHER_BLOB,
      'terminal_execution_gate_git_blob_sha1':GATE_BLOB,
      'target_workflow_git_blob_sha1':TARGET_BLOB,
      'post_run_workflow_git_blob_sha1':POST_BLOB,
      'execution_authority_git_blob_sha1':EXEC_BLOB,
      'execution_authority_review_git_blob_sha1':REVIEW_BLOB,
      'runtime_static_authority_git_blob_sha1':STATIC_BLOB,
      'execution_nonce':NONCE,
      'target_dispatch_count_at_static_audit':0,
      'target_active_sibling_count_at_static_audit':0,
      'launcher_main_only_trigger_verified':True,
      'launcher_run_number_1_attempt_1_guards_verified':True,
      'atomic_preflight_precedes_dispatch_verified':True,
      'single_dispatch_post_call_verified':True,
      'exact_target_inputs_verified':True,
      'target_runtime_and_post_run_closure_bound':True,
      'dispatch_performed_by_this_audit':False,
      'launcher_promotion_authorized_by_this_receipt':False,
      'successor_sentinel_science_authorized':False,
      'full_107_row_execution_authorized':False,
      'downstream_science_authorized':False,
      'token':'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_ONE_SHOT_LAUNCHER_STATIC_PLUS_0_PLUS_0'
    }
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'])

if __name__=='__main__': main()
