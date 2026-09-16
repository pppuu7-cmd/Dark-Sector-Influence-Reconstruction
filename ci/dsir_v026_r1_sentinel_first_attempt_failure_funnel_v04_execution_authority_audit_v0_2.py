#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

HOSTED='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-4.yml'; HOSTED_BLOB='6bf2027a121348823914e9076338055a4820162e'
POST='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-post-run-history-v0-4.yml'; POST_BLOB='6c2617e756877fb3cbb8b27dcf16b2bfc164cab5'
CONTRACT='docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_CANDIDATE_V0_4.json'; CONTRACT_BLOB='23e2404d835b4615308fbbb345f8a00e45c449a1'
QUAL='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_FINAL_STATIC_QUALIFICATION_V0_1.json'; QUAL_BLOB='eba53204d3a46b11c54c37adefe729722b00783f'
AUTH='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_4.json'; AUTH_BLOB='d68aa9ffa3fb5a7768e6802146aed74a3b57cf1b'
REVIEW='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_V0_4.json'; REVIEW_BLOB='01e5e9e0145e8c2ad1f0da639f3de073d9b26da2'
STATIC='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_STATIC_AUDIT_AUTHORITY_V0_4.json'; STATIC_BLOB='6bbacdc70dbfbee1dc4753e4a05266f9dbe45399'
NONCE='DSIR-V026R1-FFHOSTED-V0-4-10E7F9BD-7072FA7F-20260916-A1'

def h(p): return subprocess.check_output(['git','hash-object',p],text=True).strip()
def j(p): return json.loads(Path(p).read_text())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live-runs-json',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    for p,b in [(HOSTED,HOSTED_BLOB),(POST,POST_BLOB),(CONTRACT,CONTRACT_BLOB),(QUAL,QUAL_BLOB),(AUTH,AUTH_BLOB),(REVIEW,REVIEW_BLOB),(STATIC,STATIC_BLOB)]:
        assert h(p)==b,(p,h(p),b)

    c,q,au,r,s=map(j,[CONTRACT,QUAL,AUTH,REVIEW,STATIC])
    assert c['status']=='PROSPECTIVE_NONEXECUTED_CANDIDATE'
    for k in ['failure_funnel_dispatch_authorized_now','promotion_authorized_now','science_run_35033268924_rerun_authorized','same_nonce_second_attempt_authorized','successor_sentinel_science_authorized','full_107_row_execution_authorized','downstream_science_authorized']:
        assert c[k] is False,k
    assert q['status']=='TERMINAL_STATIC_QUALIFICATION' and q['verdict']=='QUALIFIED'
    assert q['reviewed_candidate']['head_sha']=='10e7f9bd8aaa5623e9f34adf17c2f53f50db5873'
    assert q['reviewed_candidate']['hosted_workflow_git_blob_sha1']==HOSTED_BLOB
    assert q['reviewed_candidate']['post_run_history_workflow_git_blob_sha1']==POST_BLOB
    assert q['authoritative_static_audit']['run_id']==35139440106
    assert q['authoritative_static_audit']['artifact_id']==10464695970
    assert q['authoritative_static_audit']['artifact_zip_sha256']=='bff94d6a0c0eb956efd19357a8099075ea035fcc78fe8a638b6e2c7b75333b60'
    assert q['authoritative_static_audit']['receipt_sha256']=='7072fa7f39f8c903f0b75fddc14f108981c9ec6beafc052f5593ba949b4e88ae'

    assert au['status']=='AUTHORIZED_SCOPED' and au['workflow_git_blob_sha1']==HOSTED_BLOB and au['post_run_history_workflow_git_blob_sha1']==POST_BLOB
    assert au['final_static_qualification_git_blob_sha1']==QUAL_BLOB and au['execution_nonce']==NONCE
    assert au['authorized_event']=='workflow_dispatch' and au['authorized_ref']=='refs/heads/main'
    assert au['required_prior_dispatch_count']==0 and au['required_parallel_or_in_progress_sibling_count']==0
    assert au['authorized_dispatch_count']==1 and au['authorized_run_number']==1 and au['authorized_run_attempt']==1
    assert au['failure_funnel_execution_authorized_after_activation'] is True
    assert au['authority_active_before_terminal_execution_gate_and_exact_promotion'] is False
    for k in ['rerun_authorized','second_dispatch_authorized','same_nonce_second_attempt_authorized','science_run_35033268924_rerun_authorized','successor_sentinel_science_authorized','full_107_row_execution_authorized','downstream_science_authorized']:
        assert au[k] is False,k

    assert r['status']=='QUALIFIED' and r['verdict']=='QUALIFIED'
    assert r['reviewed_execution_authority_git_blob_sha1']==AUTH_BLOB and r['reviewed_workflow_git_blob_sha1']==HOSTED_BLOB and r['reviewed_post_run_history_workflow_git_blob_sha1']==POST_BLOB
    assert r['reviewed_final_static_qualification_git_blob_sha1']==QUAL_BLOB and r['execution_nonce']==NONCE
    assert r['authorized_ref']=='refs/heads/main' and r['authorized_event']=='workflow_dispatch' and r['authorized_run_number']==1 and r['authorized_run_attempt']==1
    for k in ['github_run_number_1_runtime_guard_present','api_run_number_1_runtime_guard_present','run_attempt_1_runtime_guard_present','zero_prior_dispatch_required_before_activation','zero_parallel_sibling_required_before_activation','end_of_run_live_history_recheck_present','post_run_terminal_history_workflow_bound','late_duplicate_fails_closed','rerun_forbidden','second_dispatch_forbidden']:
        assert r['findings'][k] is True,k

    assert s['status']=='TERMINAL_STATIC_AUDIT_AUTHORITY' and s['verdict']=='QUALIFIED'
    assert s['reviewed_workflow_git_blob_sha1']==HOSTED_BLOB and s['reviewed_post_run_history_workflow_git_blob_sha1']==POST_BLOB
    assert s['reviewed_execution_authority_git_blob_sha1']==AUTH_BLOB and s['reviewed_execution_authority_review_git_blob_sha1']==REVIEW_BLOB
    assert s['reviewed_final_static_qualification_git_blob_sha1']==QUAL_BLOB and s['execution_nonce']==NONCE
    assert s['authorized_ref']=='refs/heads/main' and s['authorized_run_number']==1 and s['authorized_run_attempt']==1
    for k in ['consumer_schema_exact_match_verified','first_dispatch_run_number_guard_verified','end_of_run_live_history_recheck_verified','post_run_terminal_live_history_audit_verified','late_duplicate_fail_closed_verified','rerun_forbidden_verified','second_dispatch_forbidden_verified','terminal_execution_gate_required_before_activation']:
        assert s[k] is True,k
    assert s['authority_active_before_terminal_execution_gate_and_exact_promotion'] is False
    assert s['failure_funnel_dispatch_authorized_after_exact_promotion'] is True

    hosted=Path(HOSTED).read_text(); post=Path(POST).read_text()
    for marker in ['test "$GITHUB_REF" = "refs/heads/main"','test "$GITHUB_RUN_NUMBER" = "1"','test "$GITHUB_RUN_ATTEMPT" = "1"',"assert int(only['run_number'])==1","assert int(only['run_attempt'])==1",'Recheck live dispatch history at end of main work',"assert d['successor_science_authorized_by_this_receipt'] is False"]:
        assert marker in hosted,marker
    for marker in ['workflow_run:','- completed',"assert int(e['run_number'])==1","assert int(e['run_attempt'])==1","assert e['head_branch']=='main'","assert e['status']=='completed'","assert e['conclusion']=='success'","assert len(exact)==1","assert int(only['run_number'])==1","assert int(only['run_attempt'])==1"]:
        assert marker in post,marker

    live=j(a.live_runs_json); runs=live.get('workflow_runs',[])
    assert int(live.get('total_count',len(runs)))==0
    assert runs==[]

    out={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_EXECUTION_AUTHORITY_GATE_AUDIT_V0_2',
      'status':'TERMINAL_EXECUTION_AUTHORITY_GATE','verdict':'QUALIFIED',
      'classification':'V0_4_EXACT_ONE_FIRST_LIVE_FAILURE_FUNNEL_DISPATCH_AUTHORITY_QUALIFIED',
      'effect':'+0/+0','candidate_dispatch_run_count':0,'parallel_or_in_progress_target_sibling_count':0,
      'execution_nonce':NONCE,'authorized_ref':'refs/heads/main','authorized_event':'workflow_dispatch','authorized_run_number':1,'authorized_run_attempt':1,
      'exact_hosted_workflow_blob':HOSTED_BLOB,'exact_post_run_history_workflow_blob':POST_BLOB,'exact_execution_authority_blob':AUTH_BLOB,'exact_execution_authority_review_blob':REVIEW_BLOB,'exact_runtime_static_authority_blob':STATIC_BLOB,
      'final_static_qualification_bound':True,'consumer_schema_exact_match_verified':True,'end_of_run_live_history_recheck_verified':True,'post_run_terminal_history_closure_verified':True,'late_duplicate_fail_closed_verified':True,
      'atomic_pre_dispatch_recheck_required':True,'single_target_dispatch_authorized_after_exact_promotion':True,'dispatch_performed_by_this_receipt':False,
      'rerun_authorized':False,'second_dispatch_authorized':False,'same_nonce_second_attempt_authorized':False,'science_run_35033268924_rerun_authorized':False,'successor_sentinel_science_authorized':False,'full_107_row_execution_authorized':False,'downstream_science_authorized':False,
      'supersedes_failed_audit_run_id':35144971693,
      'superseded_failure_reason':'AUDITOR_MARKER_NAME_MISMATCH_TRIG_VS_E_ONLY;_FROZEN_V0_4_SOURCE_UNCHANGED',
      'token':'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_EXECUTION_GATE_V0_2_PLUS_0_PLUS_0'
    }
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'])

if __name__=='__main__': main()
