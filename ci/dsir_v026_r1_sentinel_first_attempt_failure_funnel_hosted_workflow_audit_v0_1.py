#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

BASE_MAIN = 'bb11150bebd8476b42c7e3c352cb4385c64251f7'
TARGET_HEAD = '1a1f33df835218b7c6232e2a9078d6681081b16f'
WORKFLOW = '.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-1.yml'
WORKFLOW_BLOB = '71d054036e251dce50d0bcfc8429b6d875ceb9c4'
CONTRACT = 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_CANDIDATE_V0_1.json'
CONTRACT_BLOB = '2152e952e37fd1f22f5f38b976379540103de2ef'
CONFIRMATION = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_REAUDIT_CONFIRMATION_V0_1.json'
CONFIRMATION_BLOB = 'd2fe264e2866b9f490a7523a32f341fb7cc08d0b'
EXECUTION_AUTHORITY = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_1.json'
TARGET_PR190_HEAD = '5731b605afdc35bd85d3a2014a9e135719a07697'
TARGET_AUDITOR_BLOB = 'f7eff337e511baa25d51e5b0c333a97534e1bbc3'
TARGET_CONTRACT_BLOB = '3369e5cdd2086ca22dca6bfa575054286fd1dcd7'
FORENSIC_ARTIFACT_ID = 10422924571
FORENSIC_ZIP_SHA256 = '226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b'
SCIENCE_RUN_ID = 35033268924
SCIENCE_WORKFLOW_ID = 359060727
SCIENCE_HEAD = '9a333294f3acb80201c5f6ed5b74918c1c767232'
EXPECTED_FILES = {WORKFLOW, CONTRACT}


def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def rev_blob(rev: str, path: str) -> str:
    return sh('git', 'rev-parse', f'{rev}:{path}')


def git_show(rev: str, path: str) -> str:
    return subprocess.check_output(['git', 'show', f'{rev}:{path}'], text=True)


def path_exists(rev: str, path: str) -> bool:
    p = subprocess.run(['git', 'cat-file', '-e', f'{rev}:{path}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return p.returncode == 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--candidate-live-runs-json', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    assert sh('git', 'hash-object', CONFIRMATION) == CONFIRMATION_BLOB
    conf = json.loads(Path(CONFIRMATION).read_text())
    assert conf['verdict'] == 'CONFIRMED_SCOPED'
    assert conf['authorized_next_stage'] == 'PROSPECTIVELY_AUTHOR_SEPARATE_FROZEN_HOSTED_FAILURE_FUNNEL_WORKFLOW_CANDIDATE_AND_AUDIT_BEFORE_EXECUTION'
    assert conf['hosted_failure_funnel_execution_authorized'] is False
    assert conf['science_run_35033268924_rerun_authorized'] is False
    assert conf['successor_sentinel_science_authorized'] is False
    assert conf['full_107_row_execution_authorized'] is False

    sh('git', 'cat-file', '-e', f'{TARGET_HEAD}^{{commit}}')
    assert rev_blob(TARGET_HEAD, WORKFLOW) == WORKFLOW_BLOB
    assert rev_blob(TARGET_HEAD, CONTRACT) == CONTRACT_BLOB
    changed = {x for x in sh('git', 'diff', '--name-only', BASE_MAIN, TARGET_HEAD).splitlines() if x}
    assert changed == EXPECTED_FILES, changed
    assert not path_exists(TARGET_HEAD, EXECUTION_AUTHORITY)

    contract = json.loads(git_show(TARGET_HEAD, CONTRACT))
    assert contract['schema'] == 'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_CANDIDATE_V0_1'
    assert contract['status'] == 'FROZEN_NONEXECUTED_CANDIDATE_PENDING_INDEPENDENT_STATIC_AUDIT'
    assert contract['effect'] == '+0/+0'
    assert contract['governing_reaudit_confirmation']['git_blob_sha1'] == CONFIRMATION_BLOB
    assert contract['workflow']['path'] == WORKFLOW
    assert contract['workflow']['git_blob_sha1'] == WORKFLOW_BLOB
    assert contract['workflow']['trigger'] == 'workflow_dispatch_only'
    assert contract['workflow']['push_trigger_present'] is False
    assert contract['workflow']['schedule_trigger_present'] is False
    assert contract['workflow']['failure_funnel_execution_authorized_now'] is False
    assert contract['workflow']['requires_future_execution_authority_file'] == EXECUTION_AUTHORITY
    assert contract['workflow']['requires_execution_nonce'] is True
    assert contract['workflow']['requires_execution_authority_blob_input'] is True
    assert contract['workflow']['requires_first_run_attempt'] is True
    assert contract['workflow']['requires_unique_first_dispatch_of_workflow_path'] is True
    assert contract['workflow']['full_history_checkout'] is True
    assert contract['workflow']['live_science_history_pagination_required'] is True
    assert contract['hardened_pr190_target']['head_sha'] == TARGET_PR190_HEAD
    assert contract['hardened_pr190_target']['auditor_git_blob_sha1'] == TARGET_AUDITOR_BLOB
    assert contract['hardened_pr190_target']['contract_git_blob_sha1'] == TARGET_CONTRACT_BLOB
    assert contract['forensic_producer']['artifact_id'] == FORENSIC_ARTIFACT_ID
    assert contract['forensic_producer']['artifact_zip_sha256'] == FORENSIC_ZIP_SHA256
    assert contract['science_attempt']['workflow_id'] == SCIENCE_WORKFLOW_ID
    assert contract['science_attempt']['run_id'] == SCIENCE_RUN_ID
    assert contract['science_attempt']['head_sha'] == SCIENCE_HEAD
    assert contract['future_execution_authority_required'] is True
    assert contract['future_execution_authority_present_now'] is False
    assert contract['hosted_failure_funnel_execution_authorized_now'] is False
    assert contract['terminal_first_attempt_result_authority_authorized_now'] is False
    assert contract['rerun_authorized'] is False
    assert contract['same_nonce_second_attempt_authorized'] is False
    assert contract['successor_sentinel_science_authorized'] is False
    assert contract['full_107_row_execution_authorized'] is False

    src = git_show(TARGET_HEAD, WORKFLOW)
    on_block = src.split('on:\n', 1)[1].split('\npermissions:\n', 1)[0]
    assert '  workflow_dispatch:' in on_block
    for forbidden_event in ['\n  push:', '\n  schedule:', '\n  pull_request:', '\n  pull_request_target:', '\n  workflow_run:']:
        assert forbidden_event not in on_block, forbidden_event

    assert 'contents: read' in src
    assert 'actions: read' in src
    for forbidden_permission in ['contents: write', 'actions: write', 'pull-requests: write']:
        assert forbidden_permission not in src
    assert 'fetch-depth: 0' in src

    guard = src.index('      - name: Fail closed unless future exact execution authority exists')
    unique = src.index('      - name: Require unique first dispatch of this workflow path')
    bind = src.index('      - name: Bind exact hardened PR190 auditor and contract')
    capture = src.index('      - name: Capture exact producer metadata and fresh science run history')
    download = src.index('      - name: Download exact frozen forensic artifact')
    execute = src.index('      - name: Execute frozen independent failure funnel auditor')
    persist = src.index('      - name: Persist hosted failure funnel evidence')
    assert guard < unique < bind < capture < download < execute < persist

    required_fragments = [
        'test -f "$EXECUTION_AUTHORITY_PATH"',
        'git hash-object "$EXECUTION_AUTHORITY_PATH"',
        "assert a['status']=='AUTHORIZED_SCOPED'",
        "assert a['workflow_git_blob_sha1']==workflow_blob",
        "assert a['execution_nonce']==os.environ['INPUT_EXECUTION_NONCE']",
        "assert a['failure_funnel_execution_authorized'] is True",
        "assert a['authorized_run_attempt']==1",
        "assert a['science_run_35033268924_rerun_authorized'] is False",
        "assert a['same_nonce_second_attempt_authorized'] is False",
        'event=workflow_dispatch&per_page=100',
        "assert len(exact)==1",
        "assert int(only['id'])==int(os.environ['GITHUB_RUN_ID'])",
        "assert int(only['run_attempt'])==1",
        "assert int(os.environ['GITHUB_RUN_ATTEMPT'])==1",
        TARGET_PR190_HEAD,
        TARGET_AUDITOR_BLOB,
        TARGET_CONTRACT_BLOB,
        str(FORENSIC_ARTIFACT_ID),
        FORENSIC_ZIP_SHA256,
        "urllib.parse.urlencode({'head_sha':os.environ['SCIENCE_HEAD'],'event':'push','per_page':100})",
        "while url:",
        'actions/artifacts/$FORENSIC_ARTIFACT_ID/zip',
        '--science-live-runs-json safe/science_live_runs.json',
        "assert d['verdict']=='CONFIRMED_SCOPED'",
        "assert d['terminal_first_attempt_authority_admissible'] is True",
        "assert d['rerun_authorized'] is False",
        "assert d['successor_science_authorized'] is False",
        "assert d['full_107_row_execution_authorized'] is False",
    ]
    for frag in required_fragments:
        assert frag in src, frag

    for forbidden_action in [
        'git push',
        'git commit',
        'gh workflow run',
        '/rerun',
        'curl -X POST',
        'curl --request POST',
        "method='POST'",
        'method="POST"',
        'layerb-beta-v026-r1-sentinel-science-v0-1.yml',
        'layerb_beta_v026_r1_sentinel_v0_1.py',
    ]:
        assert forbidden_action not in src, forbidden_action

    live = json.loads(Path(a.candidate_live_runs_json).read_text())
    runs = live.get('workflow_runs', [])
    assert int(live.get('total_count', len(runs))) == 0
    assert runs == []

    receipt = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_STATIC_AUDIT_V0_1',
        'effect': '+0/+0',
        'verdict': 'QUALIFIED',
        'classification': 'HOSTED_FAILURE_FUNNEL_WORKFLOW_CANDIDATE_STATICALLY_QUALIFIED_FOR_SEPARATE_EXECUTION_AUTHORITY_REVIEW_ONLY',
        'target_head_sha': TARGET_HEAD,
        'workflow_git_blob_sha1': WORKFLOW_BLOB,
        'contract_git_blob_sha1': CONTRACT_BLOB,
        'target_diff_exactly_two_nonruntime_files': True,
        'workflow_dispatch_only': True,
        'future_execution_authority_absent_on_candidate': True,
        'execution_guard_precedes_all_evidence_access': True,
        'unique_first_dispatch_guard_present': True,
        'current_candidate_dispatch_run_count': 0,
        'exact_pr190_binding_present': True,
        'exact_forensic_artifact_binding_present': True,
        'fresh_science_history_pagination_present': True,
        'repository_or_science_mutation_action_detected': False,
        'failure_funnel_executed_during_static_audit': False,
        'failure_funnel_execution_authorized': False,
        'terminal_first_attempt_result_authority_authorized': False,
        'rerun_authorized': False,
        'same_nonce_second_attempt_authorized': False,
        'successor_sentinel_science_authorized': False,
        'full_107_row_execution_authorized': False,
        'next_gate': 'PERSIST_STATIC_AUDIT_AUTHORITY_THEN_REVIEW_A_SEPARATE_ONE_RUN_EXECUTION_AUTHORITY;_DO_NOT_DISPATCH_BEFORE_AUTHORITY',
        'token': 'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_STATIC_AUDIT_PLUS_0_PLUS_0',
    }
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(receipt['token'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
