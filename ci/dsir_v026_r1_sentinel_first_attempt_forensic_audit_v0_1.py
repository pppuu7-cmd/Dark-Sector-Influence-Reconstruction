#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

RUN_ID = 35033268924
AUTHORIZE_JOB_ID = 104596462857
DECISION_JOB_ID = 104596495504
HEAD = '9a333294f3acb80201c5f6ed5b74918c1c767232'
FIRST_PARENT = '2ca2d4c35f9dcfe2be00e573598e6189f987508d'
STAGING_PARENT = '657e5d6b2fe3ad7f7c11bcd2af873cffe800cc96'
W = '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
A = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
Q = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'
L = 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
C = 'docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json'
P = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json'
I = 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json'
IQ = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_PR171_QUALIFICATION_AUDIT_V0_2.json'
E = 'ci/layerb_beta_v026_r1_sentinel_v0_1.py'
D = 'ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py'
L_GATE = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_EXACT_L_GATE_AUTHORITY_V0_1.json'

BLOBS = {
    W: '19907175f0f3417ddee2aba6916d961c6be02e26',
    A: '1c9945dd00b137f3e202efa14bf4112fffebf8af',
    Q: 'f7b97f47d9e771e3d3ea78875da5a45962160cd0',
    L: 'fa7014435f0a5688def2124898ddd01d0c0183aa',
    C: 'b510d8e97baf1c0b7b216c0605d83cdd029254e9',
    P: 'cdbcea2622564d40aa9d1edc045a5808f8cdd1c4',
    I: 'e14804463d9eab288162b4c98e8dd5c1fd6a10eb',
    IQ: '5d042377fa48d896865db0ada11508015c74e350',
    E: '9affe7c7d4e02bbc728ba15e3cde893ec9876b38',
    D: '97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9',
    L_GATE: '1c1819ee6aa7a48597770d9bc9116185d061a49c',
}


def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def blob(path: str) -> str:
    return sh('git', 'hash-object', path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--run-json', required=True)
    ap.add_argument('--jobs-json', required=True)
    ap.add_argument('--artifacts-json', required=True)
    ap.add_argument('--authorize-log', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    assert sh('git', 'rev-parse', 'HEAD') != ''
    assert sh('git', 'rev-parse', f'{HEAD}^1') == FIRST_PARENT
    assert sh('git', 'rev-parse', f'{HEAD}^2') == STAGING_PARENT
    subprocess.run(['git', 'merge-base', '--is-ancestor', HEAD, 'HEAD'], check=True)

    live = {p: blob(p) for p in BLOBS}
    assert live == BLOBS, (live, BLOBS)

    merge_changes = sh('git', 'diff-tree', '--no-commit-id', '--name-status', '-r', FIRST_PARENT, HEAD).splitlines()
    stage_changes = sh('git', 'diff-tree', '--no-commit-id', '--name-status', '-r', FIRST_PARENT, STAGING_PARENT).splitlines()
    expected_change = [f'A\t{L}']
    assert merge_changes == expected_change, merge_changes
    assert stage_changes == expected_change, stage_changes

    aa = json.loads(Path(A).read_text())
    qq = json.loads(Path(Q).read_text())
    ll = json.loads(Path(L).read_text())
    gate = json.loads(Path(L_GATE).read_text())

    # Reproduce every package/blob predicate that appears before the event-payload guard.
    assert aa['schema'] == 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1'
    assert aa['status'] == 'TERMINAL_LAUNCH_AUTHORITY'
    assert aa['authorized_launch_count'] == 1
    assert aa['sentinel_science_execution_authorized'] is True
    assert aa['full_107_row_execution_authorized'] is False
    assert aa['r1_contract_git_blob_sha1'] == BLOBS[C]
    assert aa['r1_promotion_authority_git_blob_sha1'] == BLOBS[P]
    assert aa['sentinel_implementation_contract_git_blob_sha1'] == BLOBS[I]
    assert aa['sentinel_implementation_qualification_git_blob_sha1'] == BLOBS[IQ]
    assert aa['executor_git_blob_sha1'] == BLOBS[E]
    assert aa['decision_git_blob_sha1'] == BLOBS[D]
    assert aa['active_workflow_git_blob_sha1'] == BLOBS[W]
    assert aa['launch_descriptor_git_blob_bound_by_authority'] is False
    assert aa['requires_separate_launch_package_qualification'] is True

    assert ll['schema'] == 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1'
    assert ll['authorized_launch_count'] == 1
    assert ll['sentinel_science_execution_authorized'] is True
    assert ll['full_107_row_execution_authorized'] is False
    assert ll['launch_authority_git_blob_sha1'] == BLOBS[A]
    assert ll['active_workflow_git_blob_sha1'] == BLOBS[W]

    assert qq['schema'] == 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1'
    assert qq['status'] == 'TERMINAL_AUDIT_AUTHORITY'
    assert qq['verdict'] in ('QUALIFIED', 'CONFIRMED')
    assert qq['sentinel_science_execution_authorized'] is True
    assert qq['full_107_row_execution_authorized'] is False
    assert qq['active_workflow_git_blob_sha1'] == BLOBS[W]
    assert qq['launch_authority_git_blob_sha1'] == BLOBS[A]
    assert qq['launch_descriptor_git_blob_sha1'] == BLOBS[L]
    assert qq['executor_git_blob_sha1'] == BLOBS[E]
    assert qq['decision_git_blob_sha1'] == BLOBS[D]
    assert qq['implementation_contract_git_blob_sha1'] == BLOBS[I]

    assert gate['verdict'] == 'AUTHORIZED_SCOPED'
    assert gate['one_run_trigger_authorization']['exact_final_L_git_blob_sha1'] == BLOBS[L]
    assert gate['one_run_trigger_authorization']['authorized_final_L_creation_count'] == 1
    assert gate['one_run_trigger_authorization']['rerun_forbidden'] is True
    assert gate['one_run_trigger_authorization']['full_107_row_execution_authorized'] is False

    run = json.loads(Path(args.run_json).read_text())
    assert int(run['id']) == RUN_ID
    assert run['head_sha'] == HEAD
    assert run['head_branch'] == 'main'
    assert run['event'] == 'push'
    assert int(run['run_number']) == 1
    assert int(run['run_attempt']) == 1
    assert run['status'] == 'completed'
    assert run['conclusion'] == 'failure'

    jobs_doc = json.loads(Path(args.jobs_json).read_text())
    jobs = jobs_doc['jobs']
    by_name = {j['name']: j for j in jobs}
    assert by_name['authorize']['id'] == AUTHORIZE_JOB_ID
    assert by_name['authorize']['conclusion'] == 'failure'
    assert by_name['materialize-plan']['conclusion'] == 'skipped'
    assert by_name['lane']['conclusion'] == 'skipped'
    assert by_name['decision']['id'] == DECISION_JOB_ID
    assert by_name['decision']['conclusion'] == 'failure'
    auth_steps = {s['name']: s for s in by_name['authorize'].get('steps', [])}
    assert auth_steps['Verify exact acyclic W-A-L-Q launch package and one-run trigger']['conclusion'] == 'failure'
    assert auth_steps['Enforce unique exact-head first-attempt workflow run']['conclusion'] == 'skipped'
    dec_steps = {s['name']: s for s in by_name['decision'].get('steps', [])}
    assert dec_steps['Require current-run authorization before finalization']['conclusion'] == 'failure'
    assert dec_steps['Finalize sentinel only; never launch full replay']['conclusion'] == 'skipped'

    artifacts = json.loads(Path(args.artifacts_json).read_text())
    assert int(artifacts.get('total_count', len(artifacts.get('artifacts', [])))) == 0
    assert artifacts.get('artifacts', []) == []

    log = Path(args.authorize_log).read_text(errors='replace')
    assert 'CURRENT_RUN_ATTEMPT: 1' in log
    assert f'CURRENT_HEAD_SHA: {HEAD}' in log
    assert 'EVENT_NAME: push' in log
    assert 'File "<stdin>", line 48, in <module>' in log
    assert 'AssertionError' in log
    assert 'Process completed with exit code 1.' in log

    wtxt = Path(W).read_text()
    marker = "python3 - <<'PY'\n"
    start = wtxt.index(marker) + len(marker)
    block = wtxt[start:]
    block = block[:block.index('\n          PY')]
    py_lines = [line[10:] if line.startswith('          ') else line for line in block.splitlines()]
    assert len(py_lines) >= 50
    assert py_lines[47].strip() == "assert added.count(launch)==1", py_lines[47]
    assert py_lines[48].strip() == "assert launch not in modified and launch not in removed", py_lines[48]
    assert py_lines[49].strip() == "assert ev.get('forced') is False", py_lines[49]

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FORENSIC_AUDIT_V0_1',
        'effect': '+0/+0',
        'verdict': 'TERMINAL_BLOCKED',
        'classification': 'SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE',
        'run_id': RUN_ID,
        'run_number': 1,
        'run_attempt': 1,
        'run_head_sha': HEAD,
        'run_conclusion': 'failure',
        'authorize_job_id': AUTHORIZE_JOB_ID,
        'authorize_job_conclusion': 'failure',
        'decision_job_id': DECISION_JOB_ID,
        'decision_job_conclusion': 'failure',
        'materialize_plan_conclusion': 'skipped',
        'lane_conclusion': 'skipped',
        'decision_finalizer_executed': False,
        'artifact_count': 0,
        'exact_L_present_on_run_head': True,
        'exact_L_git_blob_sha1': BLOBS[L],
        'repository_merge_diff_exactly_one_added_L': True,
        'repository_staging_diff_exactly_one_added_L': True,
        'all_package_assertions_before_event_guard_reproduced_pass': True,
        'traceback_stdin_line': 48,
        'traceback_line_source': "assert added.count(launch)==1",
        'event_payload_added_count_equals_one_predicate': False,
        'event_payload_actual_added_count_recoverable_from_persisted_run_evidence': False,
        'failure_scope': 'GITHUB_PUSH_EVENT_COMMITS_ADDED_AGGREGATION_GUARD_ONLY',
        'A_Q_L_runtime_binding_failure': False,
        'class_solver_invoked': False,
        'scientific_response_computed': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'sentinel_scientific_classification_available': False,
        'rerun_authorized': False,
        'same_nonce_second_attempt_authorized': False,
        'full_replay_launch_authorized': False,
        'full_107_row_execution_authorized': False,
        'next_admissible_action': 'INDEPENDENT_FIRST_ATTEMPT_FAILURE_FUNNEL_AUDIT_AND_TERMINAL_AUTHORITY; ANY_FUTURE_SENTINEL_REQUIRES_SEPARATE_PROSPECTIVE_SUCCESSOR_GOVERNANCE_NOT_RERUN',
        'token': 'TERMINAL_BLOCKED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_EVENT_GUARD_PLUS_0_PLUS_0',
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
