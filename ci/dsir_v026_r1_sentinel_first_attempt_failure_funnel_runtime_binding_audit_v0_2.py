#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import subprocess
from pathlib import Path

WORKFLOW_PATH = '.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-2.yml'
WORKFLOW_BLOB = '670a771e1d2e2854c33d71cc1c37ea6beea85566'
AUTHORITY_PATH = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_2.json'
AUTHORITY_BLOB = '47788695c3ab7050099ed44cacbb6f507cbbf03d'
REVIEW_PATH = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_V0_2.json'
REVIEW_BLOB = 'f8824d107a7fbfb260e5c5946a9d05f71131c94b'
EXPECTED_REF = 'refs/heads/main'
EXPECTED_NONCE = 'DSIR-V026R1-FFHOSTED-V0-2-8493F247-670A771E-20260916-A1'

def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--candidate-live-runs-json', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    assert sh('git','hash-object',WORKFLOW_PATH) == WORKFLOW_BLOB
    assert sh('git','hash-object',AUTHORITY_PATH) == AUTHORITY_BLOB
    assert sh('git','hash-object',REVIEW_PATH) == REVIEW_BLOB

    authority=json.loads(Path(AUTHORITY_PATH).read_text())
    review=json.loads(Path(REVIEW_PATH).read_text())
    src=Path(WORKFLOW_PATH).read_text()

    assert authority['workflow_git_blob_sha1']==WORKFLOW_BLOB
    assert authority['authorized_ref']==EXPECTED_REF
    assert authority['execution_nonce']==EXPECTED_NONCE
    assert authority['authorized_dispatch_count']==1
    assert authority['authorized_run_attempt']==1
    assert authority['authority_active_before_independent_hosted_audit_and_exact_promotion'] is False

    assert review['reviewed_execution_authority_git_blob_sha1']==AUTHORITY_BLOB
    assert review['reviewed_workflow_git_blob_sha1']==WORKFLOW_BLOB
    assert review['authorized_ref']==EXPECTED_REF
    assert review['execution_nonce']==EXPECTED_NONCE
    assert review['authorized_dispatch_count']==1
    assert review['authorized_run_attempt']==1
    assert review['qualification_active_before_independent_hosted_audit'] is False

    required = [
        'test "$GITHUB_REF" = "refs/heads/main"',
        "assert authority['authorized_ref']==os.environ['GITHUB_REF']",
        "assert review['reviewed_execution_authority_git_blob_sha1']==authority_blob",
        "assert review['reviewed_workflow_git_blob_sha1']==workflow_blob",
        "assert review['execution_nonce']==os.environ['INPUT_EXECUTION_NONCE']",
        "assert review['authorized_ref']==os.environ['GITHUB_REF']",
        "assert review_blob==os.environ['INPUT_EXECUTION_AUTHORITY_REVIEW_BLOB_SHA1']",
        "assert authority_blob==os.environ['INPUT_EXECUTION_AUTHORITY_BLOB_SHA1']",
        "assert len(exact)==1",
        "assert int(os.environ['GITHUB_RUN_ATTEMPT'])==1",
        "assert only['head_branch']=='main'",
    ]
    missing=[x for x in required if x not in src]
    assert not missing, missing

    live=json.loads(Path(a.candidate_live_runs_json).read_text())
    runs=live.get('workflow_runs', [])
    assert int(live.get('total_count',len(runs)))==0
    assert runs==[]

    receipt={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_RUNTIME_BINDING_AUDIT_V0_2',
      'effect':'+0/+0',
      'verdict':'QUALIFIED',
      'classification':'HOSTED_FAILURE_FUNNEL_V0_2_RUNTIME_BINDING_CORRECTIONS_INDEPENDENTLY_CONFIRMED',
      'workflow_git_blob_sha1':WORKFLOW_BLOB,
      'execution_authority_git_blob_sha1':AUTHORITY_BLOB,
      'review_confirmation_git_blob_sha1':REVIEW_BLOB,
      'execution_nonce':EXPECTED_NONCE,
      'authorized_ref':EXPECTED_REF,
      'candidate_dispatch_run_count':0,
      'authorized_ref_runtime_enforced':True,
      'independent_review_runtime_bound':True,
      'authority_blob_runtime_bound':True,
      'review_blob_runtime_bound':True,
      'workflow_blob_runtime_bound':True,
      'nonce_runtime_bound':True,
      'first_attempt_only_runtime_guard_present':True,
      'failure_funnel_executed_during_audit':False,
      'science_run_35033268924_rerun_authorized':False,
      'same_nonce_second_attempt_authorized':False,
      'successor_sentinel_science_authorized':False,
      'full_107_row_execution_authorized':False,
      'promotion_authorized_by_this_receipt':False,
      'failure_funnel_dispatch_authorized_by_this_receipt':False,
      'next_gate':'PERSIST_SEPARATE_RUNTIME_BINDING_AUDIT_AUTHORITY_ON_MAIN_THEN_PROMOTE_EXACT_WORKFLOW_AUTHORITY_AND_REVIEW_SET_BEFORE_ONE_DISPATCH',
      'token':'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_RUNTIME_BINDING_V0_2_PLUS_0_PLUS_0'
    }
    out=Path(a.out)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(receipt['token'])
    return 0

if __name__=='__main__':
    raise SystemExit(main())
