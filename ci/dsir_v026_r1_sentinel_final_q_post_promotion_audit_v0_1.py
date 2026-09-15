#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

PROMO = 'bcd1cfaaee2961fe4997d5789971547e3ea42955'
P1 = '370e8bb6fd77bcc3cbf3d5826a6e3a908beacda4'
P2 = '24082fa57d420de2f6e837c578fbbf0d21e25fb7'
W = '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
A = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
Q = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'
QC = 'docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json'
L = 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
E = 'ci/layerb_beta_v026_r1_sentinel_v0_1.py'
D = 'ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py'
I = 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json'

EXPECTED = {
    W: '19907175f0f3417ddee2aba6916d961c6be02e26',
    A: '4ba40e59e6a9d48636d95d07efab575e56ae0966',
    Q: 'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd',
    QC: 'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd',
    E: '9affe7c7d4e02bbc728ba15e3cde893ec9876b38',
    D: '97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9',
    I: 'e14804463d9eab288162b4c98e8dd5c1fd6a10eb',
}
REQUIRED_TOP_LEVEL = [
    'active_workflow_git_blob_sha1',
    'launch_authority_git_blob_sha1',
    'launch_descriptor_git_blob_sha1',
    'executor_git_blob_sha1',
    'decision_git_blob_sha1',
    'implementation_contract_git_blob_sha1',
]
L_BLOB = '9c217e41764d979bea12644fae372354241bc976'


def git(*args: str, check: bool = True) -> str:
    p = subprocess.run(['git', *args], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed: {p.stderr.strip()}")
    return p.stdout.strip()


def blob_at(commit: str, path: str) -> str:
    return git('rev-parse', f'{commit}:{path}')


def json_at(commit: str, path: str):
    return json.loads(git('show', f'{commit}:{path}'))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--runs-json', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    parents = git('show', '-s', '--format=%P', PROMO).split()
    if parents != [P1, P2]:
        raise RuntimeError(f'promotion parents mismatch: {parents}')

    changes = [x for x in git('diff', '--name-status', P1, PROMO).splitlines() if x]
    if changes != [f'A\t{Q}']:
        raise RuntimeError(f'unexpected promotion diff: {changes}')

    for path, expected in EXPECTED.items():
        got = blob_at(PROMO, path)
        if got != expected:
            raise RuntimeError(f'{path} blob mismatch: {got} != {expected}')

    if subprocess.run(['git', 'cat-file', '-e', f'{PROMO}:{L}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
        raise RuntimeError('final L unexpectedly present at Q promotion head')

    runs = json.load(open(args.runs_json))
    rows = runs.get('workflow_runs', [])
    if len(rows) != 0:
        raise RuntimeError(f'Q promotion head has push Actions runs: {len(rows)}')

    q = json_at(PROMO, Q)
    w = git('show', f'{PROMO}:{W}')

    if q['schema'] != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1':
        raise RuntimeError('Q schema mismatch')
    if q['status'] != 'TERMINAL_AUDIT_AUTHORITY' or q['verdict'] != 'QUALIFIED':
        raise RuntimeError('Q status/verdict mismatch')
    if q['sentinel_science_execution_authorized'] is not True:
        raise RuntimeError('Q sentinel authorization field mismatch')
    if q['full_107_row_execution_authorized'] is not False or q['full_replay_launch_authorized'] is not False:
        raise RuntimeError('Q full replay firewall mismatch')

    required_assertions = [
        "Q['active_workflow_git_blob_sha1']",
        "Q['launch_authority_git_blob_sha1']",
        "Q['launch_descriptor_git_blob_sha1']",
        "Q['executor_git_blob_sha1']",
        "Q['decision_git_blob_sha1']",
        "Q['implementation_contract_git_blob_sha1']",
    ]
    missing_w_assertions = [s for s in required_assertions if s not in w]
    if missing_w_assertions:
        raise RuntimeError(f'active W no longer requires expected Q top-level keys: {missing_w_assertions}')

    missing = [k for k in REQUIRED_TOP_LEVEL if k not in q]
    if missing != REQUIRED_TOP_LEVEL:
        raise RuntimeError(f'unexpected Q top-level compatibility state: {missing}')

    nested = {
        'active_workflow_git_blob_sha1': q['acyclic_package']['active_workflow_git_blob_sha1'],
        'launch_authority_git_blob_sha1': q['acyclic_package']['launch_authority_git_blob_sha1'],
        'launch_descriptor_git_blob_sha1': q['acyclic_package']['launch_descriptor_git_blob_sha1'],
        'executor_git_blob_sha1': q['implementation_bindings']['executor_git_blob_sha1'],
        'decision_git_blob_sha1': q['implementation_bindings']['decision_git_blob_sha1'],
        'implementation_contract_git_blob_sha1': q['implementation_bindings']['implementation_contract_git_blob_sha1'],
    }
    expected_nested = {
        'active_workflow_git_blob_sha1': EXPECTED[W],
        'launch_authority_git_blob_sha1': EXPECTED[A],
        'launch_descriptor_git_blob_sha1': L_BLOB,
        'executor_git_blob_sha1': EXPECTED[E],
        'decision_git_blob_sha1': EXPECTED[D],
        'implementation_contract_git_blob_sha1': EXPECTED[I],
    }
    if nested != expected_nested:
        raise RuntimeError(f'nested Q bindings mismatch: {nested}')

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_FINAL_Q_POST_PROMOTION_AUDIT_RECEIPT_V0_1',
        'verdict': 'BLOCKED',
        'classification': 'SENTINEL_FINAL_Q_POST_PROMOTION_RUNTIME_SCHEMA_BLOCKED',
        'effect': '+0/+0',
        'promotion_merge_sha': PROMO,
        'promotion_parents': parents,
        'promotion_changed_files': [Q],
        'final_Q_git_blob_sha1': EXPECTED[Q],
        'final_Q_exactly_equals_candidate_blob': True,
        'final_L_present': False,
        'promotion_head_push_run_count': 0,
        'active_W_git_blob_sha1': EXPECTED[W],
        'launch_A_git_blob_sha1': EXPECTED[A],
        'runtime_required_Q_top_level_keys': REQUIRED_TOP_LEVEL,
        'runtime_missing_Q_top_level_keys': missing,
        'equivalent_nested_bindings_present_and_exact': True,
        'runtime_failure_mode_if_L_created_now': 'AUTHORIZE_JOB_KEYERROR_BEFORE_SENTINEL_SOLVE',
        'sentinel_workflow_executed': False,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'sentinel_science_execution_authorized_by_this_receipt': False,
        'full_107_row_execution_authorized': False,
        'authorized_next_stage': 'PROSPECTIVE_Q_RUNTIME_SCHEMA_CORRECTION_AND_REQUALIFICATION_ONLY',
        'final_L_creation_authorized': False,
        'token': 'BLOCKED_LAYERB_BETA_V0_26_R1_SENTINEL_FINAL_Q_RUNTIME_SCHEMA_PLUS_0_PLUS_0',
    }
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])


if __name__ == '__main__':
    main()
