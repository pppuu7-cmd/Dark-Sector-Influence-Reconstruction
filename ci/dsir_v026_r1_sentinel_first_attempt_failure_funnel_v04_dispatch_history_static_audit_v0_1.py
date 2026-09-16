#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

HOSTED='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-4.yml'
POST='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-post-run-history-v0-4.yml'
HOSTED_BLOB='6bf2027a121348823914e9076338055a4820162e'
POST_BLOB='6c2617e756877fb3cbb8b27dcf16b2bfc164cab5'
V03_QUAL='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_3_DISPATCH_HISTORY_QUALIFICATION_V0_1.json'
V03_QUAL_BLOB='f55eaec50895debdbb9d2363b64a79e55db1f218'

def sh(*a): return subprocess.check_output(a,text=True).strip()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live-runs-json',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    assert sh('git','hash-object',HOSTED)==HOSTED_BLOB
    assert sh('git','hash-object',POST)==POST_BLOB
    assert sh('git','hash-object',V03_QUAL)==V03_QUAL_BLOB
    q=json.loads(Path(V03_QUAL).read_text())
    assert q['verdict']=='QUALIFIED'
    assert q['frozen_v0_3_dispatch_authorized'] is False
    h=Path(HOSTED).read_text(); p=Path(POST).read_text()
    required_h=[
      'test "$GITHUB_RUN_NUMBER" = "1"',
      'test "$GITHUB_RUN_ATTEMPT" = "1"',
      "assert int(only['run_number'])==1",
      "assert int(os.environ['GITHUB_RUN_NUMBER'])==1",
      "assert int(only['run_attempt'])==1",
      "assert int(os.environ['GITHUB_RUN_ATTEMPT'])==1",
      "assert only['head_branch']=='main'",
      'Recheck live dispatch history at end of main work',
      'safe/end_of_run_dispatch_history.json',
      'POST_RUN_HISTORY_WORKFLOW_PATH',
    ]
    miss_h=[x for x in required_h if x not in h]; assert not miss_h, miss_h
    required_p=[
      'workflow_run:',
      'types:',
      '- completed',
      "assert int(e['run_number'])==1",
      "assert int(e['run_attempt'])==1",
      "assert e['head_branch']=='main'",
      "assert e['status']=='completed'",
      "assert e['conclusion']=='success'",
      "assert len(exact)==1",
      "assert int(only['run_number'])==1",
      "assert int(only['run_attempt'])==1",
      "assert only['status']=='completed'",
      "assert only['conclusion']=='success'",
      "'late_duplicate_dispatch_detected':False",
      "'failure_funnel_result_promotion_authorized_by_this_receipt':False",
    ]
    miss_p=[x for x in required_p if x not in p]; assert not miss_p, miss_p
    live=json.loads(Path(a.live_runs_json).read_text()); runs=live.get('workflow_runs',[])
    exact=[x for x in runs if x.get('path')==HOSTED and x.get('event')=='workflow_dispatch']
    assert exact==[], [(x.get('id'),x.get('run_number'),x.get('run_attempt')) for x in exact]
    out={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_DISPATCH_HISTORY_STATIC_AUDIT_V0_1',
      'effect':'+0/+0','verdict':'QUALIFIED',
      'classification':'V0_4_MONOTONIC_FIRST_DISPATCH_AND_POST_RUN_TERMINAL_HISTORY_CLOSURE_STATICALLY_CONFIRMED',
      'hosted_workflow_git_blob_sha1':HOSTED_BLOB,
      'post_run_history_workflow_git_blob_sha1':POST_BLOB,
      'v0_3_dispatch_history_qualification_git_blob_sha1':V03_QUAL_BLOB,
      'candidate_dispatch_run_count':0,
      'github_run_number_1_guard_verified':True,
      'api_run_number_1_guard_verified':True,
      'run_attempt_1_guard_verified':True,
      'end_of_run_live_history_recheck_verified':True,
      'post_run_completed_trigger_verified':True,
      'post_run_single_terminal_history_verified':True,
      'late_duplicate_fail_closed_verified':True,
      'failure_funnel_executed_during_audit':False,
      'promotion_authorized_by_this_receipt':False,
      'failure_funnel_dispatch_authorized_by_this_receipt':False,
      'science_run_35033268924_rerun_authorized':False,
      'same_nonce_second_attempt_authorized':False,
      'successor_sentinel_science_authorized':False,
      'full_107_row_execution_authorized':False,
      'next_gate':'PERSIST_SEPARATE_TERMINAL_V0_4_STATIC_AUDIT_AUTHORITY_BEFORE_AUTHORING_EXACT_EXECUTION_AUTHORITY_SET',
      'token':'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_DISPATCH_HISTORY_STATIC_PLUS_0_PLUS_0'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'])
    return 0

if __name__=='__main__': raise SystemExit(main())
