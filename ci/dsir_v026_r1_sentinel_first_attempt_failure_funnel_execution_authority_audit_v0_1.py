#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

MAIN = '8493f247b3095a139626cf11cfaa80e85daad293'
STATIC_AUTH = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_STATIC_AUDIT_AUTHORITY_V0_1.json'
STATIC_AUTH_BLOB = 'aa35756e8dd14cca9f9c14cc52cd0ab9465073df'
WORKFLOW_HEAD = '1a1f33df835218b7c6232e2a9078d6681081b16f'
WORKFLOW_PATH = '.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-1.yml'
WORKFLOW_BLOB = '71d054036e251dce50d0bcfc8429b6d875ceb9c4'
AUTH_HEAD = '30461cd9f9d8b43072b47ef78718fe49bfd3a2dd'
AUTH_PATH = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_1.json'
AUTH_BLOB = 'b5a99a35df29289f10c779eb6e6d0627d4901e5f'
EXPECTED_NONCE = 'DSIR-V026R1-FFHOSTED-V0-1-8493F247-71D05403-20260916-A1'
EXPECTED_REF = 'refs/heads/main'


def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def rev_blob(rev: str, path: str) -> str:
    return sh('git', 'rev-parse', f'{rev}:{path}')


def show(rev: str, path: str) -> str:
    return subprocess.check_output(['git', 'show', f'{rev}:{path}'], text=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--candidate-live-runs-json', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    assert sh('git', 'hash-object', STATIC_AUTH) == STATIC_AUTH_BLOB
    sa = json.loads(Path(STATIC_AUTH).read_text())
    assert sa['verdict'] == 'QUALIFIED'
    assert sa['authorized_next_stage'] == 'PROSPECTIVELY_AUTHOR_AND_INDEPENDENTLY_REVIEW_SEPARATE_ONE_RUN_HOSTED_FAILURE_FUNNEL_EXECUTION_AUTHORITY'
    assert sa['failure_funnel_execution_authorized_now'] is False

    assert rev_blob(WORKFLOW_HEAD, WORKFLOW_PATH) == WORKFLOW_BLOB
    assert rev_blob(AUTH_HEAD, AUTH_PATH) == AUTH_BLOB
    auth = json.loads(show(AUTH_HEAD, AUTH_PATH))
    assert auth['schema'] == 'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_1'
    assert auth['status'] == 'AUTHORIZED_SCOPED'
    assert auth['workflow_path'] == WORKFLOW_PATH
    assert auth['workflow_git_blob_sha1'] == WORKFLOW_BLOB
    assert auth['authorized_event'] == 'workflow_dispatch'
    assert auth['authorized_ref'] == EXPECTED_REF
    assert auth['execution_nonce'] == EXPECTED_NONCE
    assert auth['authorized_dispatch_count'] == 1
    assert auth['authorized_run_attempt'] == 1
    assert auth['failure_funnel_execution_authorized'] is True
    assert auth['activation_conditions']['independent_execution_authority_review_required_before_promotion'] is True
    assert auth['activation_conditions']['dispatch_ref_must_equal_authorized_ref'] is True
    assert auth['science_run_35033268924_rerun_authorized'] is False
    assert auth['same_nonce_second_attempt_authorized'] is False
    assert auth['successor_sentinel_science_authorized'] is False
    assert auth['full_107_row_execution_authorized'] is False
    assert auth['authority_active_before_independent_review_and_exact_promotion'] is False

    src = show(WORKFLOW_HEAD, WORKFLOW_PATH)
    # Existing guards that are correctly enforced.
    assert "assert a['workflow_git_blob_sha1']==workflow_blob" in src
    assert "assert a['execution_nonce']==os.environ['INPUT_EXECUTION_NONCE']" in src
    assert "assert a['failure_funnel_execution_authorized'] is True" in src
    assert "assert a['authorized_run_attempt']==1" in src
    assert "assert a['science_run_35033268924_rerun_authorized'] is False" in src
    assert "assert a['same_nonce_second_attempt_authorized'] is False" in src
    assert "assert int(os.environ['GITHUB_RUN_ATTEMPT'])==1" in src
    assert "assert len(exact)==1" in src

    # Material authority constraints that must be runtime-enforced before promotion.
    ref_enforcement_fragments = [
        "a['authorized_ref']",
        "GITHUB_REF",
    ]
    ref_runtime_enforced = all(x in src for x in ref_enforcement_fragments)

    review_confirmation_markers = [
        'EXECUTION_AUTHORITY_REVIEW',
        'review_confirmation',
        'reviewed_execution_authority_git_blob_sha1',
    ]
    independent_review_runtime_bound = any(x in src for x in review_confirmation_markers)

    live = json.loads(Path(a.candidate_live_runs_json).read_text())
    runs = live.get('workflow_runs', [])
    assert int(live.get('total_count', len(runs))) == 0
    assert runs == []

    blockers = []
    if not ref_runtime_enforced:
        blockers.append('AUTHORIZED_REF_DECLARED_BUT_NOT_RUNTIME_ENFORCED')
    if not independent_review_runtime_bound:
        blockers.append('INDEPENDENT_EXECUTION_AUTHORITY_REVIEW_NOT_RUNTIME_BOUND')
    assert blockers == [
        'AUTHORIZED_REF_DECLARED_BUT_NOT_RUNTIME_ENFORCED',
        'INDEPENDENT_EXECUTION_AUTHORITY_REVIEW_NOT_RUNTIME_BOUND',
    ], blockers

    receipt = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_AUDIT_V0_1',
        'effect': '+0/+0',
        'verdict': 'BLOCKED',
        'classification': 'HOSTED_FAILURE_FUNNEL_EXECUTION_AUTHORITY_RUNTIME_BINDING_INCOMPLETE',
        'workflow_head_sha': WORKFLOW_HEAD,
        'workflow_git_blob_sha1': WORKFLOW_BLOB,
        'execution_authority_head_sha': AUTH_HEAD,
        'execution_authority_git_blob_sha1': AUTH_BLOB,
        'execution_nonce': EXPECTED_NONCE,
        'candidate_dispatch_run_count': 0,
        'existing_nonce_and_attempt_guards_present': True,
        'authorized_ref_declared': True,
        'authorized_ref_runtime_enforced': ref_runtime_enforced,
        'independent_review_required_by_authority': True,
        'independent_review_runtime_bound': independent_review_runtime_bound,
        'blockers': blockers,
        'failure_funnel_execution_authorized_after_review': False,
        'authority_promotion_authorized': False,
        'workflow_candidate_promotion_authorized': False,
        'rerun_authorized': False,
        'same_nonce_second_attempt_authorized': False,
        'successor_sentinel_science_authorized': False,
        'full_107_row_execution_authorized': False,
        'required_corrections': [
            'ENFORCE_AUTHORIZED_REF_EQUALS_GITHUB_REF_BEFORE_ANY_EVIDENCE_ACCESS',
            'REQUIRE_AND_VALIDATE_SEPARATE_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_BINDING_EXACT_AUTHORITY_BLOB_WORKFLOW_BLOB_NONCE_AND_AUTHORIZED_REF',
            'REPEAT_INDEPENDENT_STATIC_WORKFLOW_AND_AUTHORITY_COMPATIBILITY_AUDIT_AFTER_CORRECTION',
        ],
        'next_gate': 'PROSPECTIVELY_HARDEN_NONEXECUTED_HOSTED_WORKFLOW_AND_REVIEW_BINDING;_DO_NOT_PROMOTE_EXECUTION_AUTHORITY_OR_DISPATCH',
        'token': 'BLOCKED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_RUNTIME_BINDING_PLUS_0_PLUS_0',
    }
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(receipt['token'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
