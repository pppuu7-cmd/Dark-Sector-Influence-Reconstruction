#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

HOSTED='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-4.yml'
HOSTED_BLOB='6bf2027a121348823914e9076338055a4820162e'
POST='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-post-run-history-v0-4.yml'
POST_BLOB='6c2617e756877fb3cbb8b27dcf16b2bfc164cab5'
CONTRACT='docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_CANDIDATE_V0_4.json'
CONTRACT_BLOB='23e2404d835b4615308fbbb345f8a00e45c449a1'
STATIC_QUAL='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_FINAL_STATIC_QUALIFICATION_V0_1.json'
STATIC_QUAL_BLOB='eba53204d3a46b11c54c37adefe729722b00783f'
AUTH='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_4.json'
AUTH_BLOB='d68aa9ffa3fb5a7768e6802146aed74a3b57cf1b'
REVIEW='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_V0_4.json'
REVIEW_BLOB='01e5e9e0145e8c2ad1f0da639f3de073d9b26da2'
RUNTIME_STATIC='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_STATIC_AUDIT_AUTHORITY_V0_4.json'
RUNTIME_STATIC_BLOB='6bbacdc70dbfbee1dc4753e4a05266f9dbe45399'
NONCE='DSIR-V026R1-FFHOSTED-V0-4-10E7F9BD-7072FA7F-20260916-A1'

def h(path: str) -> str:
    return subprocess.check_output(['git','hash-object',path], text=True).strip()

def load(path: str):
    return json.loads(Path(path).read_text())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--live-runs-json', required=True)
    ap.add_argument('--out', required=True)
    a=ap.parse_args()

    for path, blob in [
        (HOSTED,HOSTED_BLOB),(POST,POST_BLOB),(CONTRACT,CONTRACT_BLOB),
        (STATIC_QUAL,STATIC_QUAL_BLOB),(AUTH,AUTH_BLOB),(REVIEW,REVIEW_BLOB),
        (RUNTIME_STATIC,RUNTIME_STATIC_BLOB),
    ]:
        assert h(path)==blob, (path,h(path),blob)

    contract=load(CONTRACT); qual=load(STATIC_QUAL); auth=load(AUTH); review=load(REVIEW); static=load(RUNTIME_STATIC)
    assert contract['status']=='PROSPECTIVE_NONEXECUTED_CANDIDATE'
    assert contract['failure_funnel_dispatch_authorized_now'] is False
    assert contract['promotion_authorized_now'] is False
    assert contract['science_run_35033268924_rerun_authorized'] is False
    assert contract['same_nonce_second_attempt_authorized'] is False
    assert contract['successor_sentinel_science_authorized'] is False
    assert contract['full_107_row_execution_authorized'] is False
    assert contract['downstream_science_authorized'] is False

    assert qual['status']=='TERMINAL_STATIC_QUALIFICATION' and qual['verdict']=='QUALIFIED'
    assert qual['reviewed_candidate']['head_sha']=='10e7f9bd8aaa5623e9f34adf17c2f53f50db5873'
    assert qual['reviewed_candidate']['hosted_workflow_git_blob_sha1']==HOSTED_BLOB
    assert qual['reviewed_candidate']['post_run_history_workflow_git_blob_sha1']==POST_BLOB
    assert qual['authoritative_static_audit']['run_id']==35139440106
    assert qual['authoritative_static_audit']['artifact_id']==10464695970
    assert qual['authoritative_static_audit']['artifact_zip_sha256']=='bff94d6a0c0eb956efd19357a8099075ea035fcc78fe8a638b6e2c7b75333b60'
    assert qual['authoritative_static_audit']['receipt_sha256']=='7072fa7f39f8c903f0b75fddc14f108981c9ec6beafc052f5593ba949b4e88ae'
    assert qual['failure_funnel_dispatch_authorized_by_this_authority'] is False

    assert auth['schema']=='LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_4'
    assert auth['status']=='AUTHORIZED_SCOPED'
    assert auth['workflow_git_blob_sha1']==HOSTED_BLOB
    assert auth['post_run_history_workflow_git_blob_sha1']==POST_BLOB
    assert auth['final_static_qualification_git_blob_sha1']==STATIC_QUAL_BLOB
    assert auth['authorized_event']=='workflow_dispatch'
    assert auth['authorized_ref']=='refs/heads/main'
    assert auth['execution_nonce']==NONCE
    assert auth['authorized_dispatch_count']==1
    assert auth['required_prior_dispatch_count']==0
    assert auth['required_parallel_or_in_progress_sibling_count']==0
    assert auth['authorized_run_number']==1 and auth['authorized_run_attempt']==1
    assert auth['rerun_authorized'] is False
    assert auth['second_dispatch_authorized'] is False
    assert auth['same_nonce_second_attempt_authorized'] is False
    assert auth['end_of_run_live_history_recheck_required'] is True
    assert auth['post_run_terminal_history_audit_required'] is True
    assert auth['fail_closed_on_any_history_or_identity_ambiguity'] is True
    assert auth['failure_funnel_execution_authorized_after_activation'] is True
    assert auth['authority_active_before_terminal_execution_gate_and_exact_promotion'] is False
    assert auth['successor_sentinel_science_authorized'] is False
    assert auth['full_107_row_execution_authorized'] is False

    assert review['schema']=='LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_V0_4'
    assert review['status']=='QUALIFIED' and review['verdict']=='QUALIFIED'
    assert review['reviewed_execution_authority_git_blob_sha1']==AUTH_BLOB
    assert review['reviewed_workflow_git_blob_sha1']==HOSTED_BLOB
    assert review['reviewed_post_run_history_workflow_git_blob_sha1']==POST_BLOB
    assert review['reviewed_final_static_qualification_git_blob_sha1']==STATIC_QUAL_BLOB
    assert review['execution_nonce']==NONCE
    assert review['authorized_event']=='workflow_dispatch' and review['authorized_ref']=='refs/heads/main'
    assert review['authorized_dispatch_count']==1
    assert review['required_prior_dispatch_count']==0
    assert review['required_parallel_or_in_progress_sibling_count']==0
    assert review['authorized_run_number']==1 and review['authorized_run_attempt']==1
    for k in ['exact_final_static_qualification_bound','exact_execution_authority_blob_bound','exact_workflow_blob_bound','exact_post_run_history_workflow_blob_bound','fresh_nonce_bound','authorized_ref_is_main','github_run_number_1_runtime_guard_present','api_run_number_1_runtime_guard_present','run_attempt_1_runtime_guard_present','zero_prior_dispatch_required_before_activation','zero_parallel_sibling_required_before_activation','end_of_run_live_history_recheck_present','post_run_terminal_history_workflow_bound','late_duplicate_fails_closed','rerun_forbidden','second_dispatch_forbidden']:
        assert review['findings'][k] is True, k
    assert review['rerun_authorized'] is False and review['same_nonce_second_attempt_authorized'] is False
    assert review['successor_sentinel_science_authorized'] is False and review['full_107_row_execution_authorized'] is False

    assert static['schema']=='LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_STATIC_AUDIT_AUTHORITY_V0_4'
    assert static['status']=='TERMINAL_STATIC_AUDIT_AUTHORITY' and static['verdict']=='QUALIFIED'
    assert static['reviewed_workflow_git_blob_sha1']==HOSTED_BLOB
    assert static['reviewed_post_run_history_workflow_git_blob_sha1']==POST_BLOB
    assert static['reviewed_execution_authority_git_blob_sha1']==AUTH_BLOB
    assert static['reviewed_execution_authority_review_git_blob_sha1']==REVIEW_BLOB
    assert static['reviewed_final_static_qualification_git_blob_sha1']==STATIC_QUAL_BLOB
    assert static['execution_nonce']==NONCE and static['authorized_ref']=='refs/heads/main'
    assert static['authorized_run_number']==1 and static['authorized_run_attempt']==1
    assert static['consumer_schema_exact_match_verified'] is True
    assert static['first_dispatch_run_number_guard_verified'] is True
    assert static['end_of_run_live_history_recheck_verified'] is True
    assert static['post_run_terminal_live_history_audit_verified'] is True
    assert static['late_duplicate_fail_closed_verified'] is True
    assert static['rerun_forbidden_verified'] is True and static['second_dispatch_forbidden_verified'] is True
    assert static['terminal_execution_gate_required_before_activation'] is True
    assert static['authority_active_before_terminal_execution_gate_and_exact_promotion'] is False
    assert static['failure_funnel_dispatch_authorized_after_exact_promotion'] is True
    assert static['successor_sentinel_science_authorized'] is False and static['full_107_row_execution_authorized'] is False

    hosted=Path(HOSTED).read_text(); post=Path(POST).read_text()
    required_hosted=[
        'test "$GITHUB_REF" = "refs/heads/main"',
        'test "$GITHUB_RUN_NUMBER" = "1"',
        'test "$GITHUB_RUN_ATTEMPT" = "1"',
        "assert int(only['run_number'])==1",
        "assert int(only['run_attempt'])==1",
        "assert len(exact)==1",
        'Recheck live dispatch history at end of main work',
        "assert d['successor_science_authorized_by_this_receipt'] is False",
    ]
    for marker in required_hosted: assert marker in hosted, marker
    required_post=[
        'workflow_run:', 'types:', '- completed',
        "assert int(trig['run_number'])==1", "assert int(trig['run_attempt'])==1",
        "assert trig['head_branch']=='main'", "assert trig['status']=='completed'", "assert trig['conclusion']=='success'",
        "assert len(exact)==1",
    ]
    for marker in required_post: assert marker in post, marker

    live=load(a.live_runs_json)
    runs=live.get('workflow_runs',[])
    assert int(live.get('total_count',len(runs)))==0, [(x.get('id'),x.get('status'),x.get('run_number'),x.get('run_attempt')) for x in runs]
    assert runs==[]

    out={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_EXECUTION_AUTHORITY_GATE_AUDIT_V0_1',
      'status':'TERMINAL_EXECUTION_AUTHORITY_GATE',
      'verdict':'QUALIFIED',
      'classification':'V0_4_EXACT_ONE_FIRST_LIVE_FAILURE_FUNNEL_DISPATCH_AUTHORITY_QUALIFIED',
      'effect':'+0/+0',
      'candidate_dispatch_run_count':0,
      'parallel_or_in_progress_target_sibling_count':0,
      'execution_nonce':NONCE,
      'authorized_ref':'refs/heads/main',
      'authorized_event':'workflow_dispatch',
      'authorized_run_number':1,
      'authorized_run_attempt':1,
      'exact_hosted_workflow_blob':HOSTED_BLOB,
      'exact_post_run_history_workflow_blob':POST_BLOB,
      'exact_execution_authority_blob':AUTH_BLOB,
      'exact_execution_authority_review_blob':REVIEW_BLOB,
      'exact_runtime_static_authority_blob':RUNTIME_STATIC_BLOB,
      'final_static_qualification_bound':True,
      'consumer_schema_exact_match_verified':True,
      'end_of_run_live_history_recheck_verified':True,
      'post_run_terminal_history_closure_verified':True,
      'late_duplicate_fail_closed_verified':True,
      'atomic_pre_dispatch_recheck_required':True,
      'single_target_dispatch_authorized_after_exact_promotion':True,
      'dispatch_performed_by_this_receipt':False,
      'rerun_authorized':False,
      'second_dispatch_authorized':False,
      'same_nonce_second_attempt_authorized':False,
      'science_run_35033268924_rerun_authorized':False,
      'successor_sentinel_science_authorized':False,
      'full_107_row_execution_authorized':False,
      'downstream_science_authorized':False,
      'token':'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_EXECUTION_GATE_PLUS_0_PLUS_0'
    }
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'])

if __name__=='__main__': main()
