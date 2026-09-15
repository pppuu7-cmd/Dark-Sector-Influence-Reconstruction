#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

OLD_Q = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'
NEW_Q = 'docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json'
CONTRACT = 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_Q_RUNTIME_SCHEMA_CORRECTION_CONTRACT_V0_1.json'
BLOCKER = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FINAL_Q_RUNTIME_SCHEMA_BLOCKER_V0_1.json'
W = '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
A = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
L_CANDIDATE = 'docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json'
FINAL_L = 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
E = 'ci/layerb_beta_v026_r1_sentinel_v0_1.py'
D = 'ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py'
I = 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json'

EXPECTED_BLOBS = {
    OLD_Q: 'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd',
    NEW_Q: '928178e0e68660e7f892f8d3c064981d137fd736',
    CONTRACT: '6f72c0c39dfb67e5ad5b8a952093589388e9a80b',
    BLOCKER: '44cc53fb014e043d31f72519c3ac96493ddabb57',
    W: '19907175f0f3417ddee2aba6916d961c6be02e26',
    A: '4ba40e59e6a9d48636d95d07efab575e56ae0966',
    L_CANDIDATE: '9c217e41764d979bea12644fae372354241bc976',
    E: '9affe7c7d4e02bbc728ba15e3cde893ec9876b38',
    D: '97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9',
    I: 'e14804463d9eab288162b4c98e8dd5c1fd6a10eb',
}
REQUIRED = {
    'active_workflow_git_blob_sha1': EXPECTED_BLOBS[W],
    'launch_authority_git_blob_sha1': EXPECTED_BLOBS[A],
    'launch_descriptor_git_blob_sha1': EXPECTED_BLOBS[L_CANDIDATE],
    'executor_git_blob_sha1': EXPECTED_BLOBS[E],
    'decision_git_blob_sha1': EXPECTED_BLOBS[D],
    'implementation_contract_git_blob_sha1': EXPECTED_BLOBS[I],
}


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


def load(path: str):
    return json.load(open(path))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    for path, expected in EXPECTED_BLOBS.items():
        if not Path(path).is_file():
            raise RuntimeError(f'missing required file: {path}')
        got = blob(path)
        if got != expected:
            raise RuntimeError(f'{path} blob mismatch: {got} != {expected}')
    if Path(FINAL_L).exists():
        raise RuntimeError('final L must remain absent during Q correction audit')

    old = load(OLD_Q)
    new = load(NEW_Q)
    contract = load(CONTRACT)
    blocker = load(BLOCKER)
    a = load(A)
    l = load(L_CANDIDATE)
    w = Path(W).read_text()

    if blocker['verdict'] != 'BLOCKED' or blocker['final_L_creation_authorized'] is not False:
        raise RuntimeError('governing blocker not fail-closed')
    if contract['status'] != 'PROSPECTIVELY_FROZEN_CORRECTION_CANDIDATE_NOT_EXECUTABLE':
        raise RuntimeError('correction contract status')
    if contract['old_final_Q']['git_blob_sha1'] != EXPECTED_BLOBS[OLD_Q]:
        raise RuntimeError('contract old Q binding')
    if contract['corrected_Q_candidate']['git_blob_sha1'] != EXPECTED_BLOBS[NEW_Q]:
        raise RuntimeError('contract corrected Q binding')
    if contract['required_top_level_bindings'] != REQUIRED:
        raise RuntimeError('contract required bindings mismatch')

    stripped = dict(new)
    for key, expected in REQUIRED.items():
        if stripped.get(key) != expected:
            raise RuntimeError(f'corrected Q top-level binding mismatch: {key}')
        stripped.pop(key)
    if stripped != old:
        raise RuntimeError('corrected Q changes semantics beyond six top-level binding additions')

    nested = {
        'active_workflow_git_blob_sha1': new['acyclic_package']['active_workflow_git_blob_sha1'],
        'launch_authority_git_blob_sha1': new['acyclic_package']['launch_authority_git_blob_sha1'],
        'launch_descriptor_git_blob_sha1': new['acyclic_package']['launch_descriptor_git_blob_sha1'],
        'executor_git_blob_sha1': new['implementation_bindings']['executor_git_blob_sha1'],
        'decision_git_blob_sha1': new['implementation_bindings']['decision_git_blob_sha1'],
        'implementation_contract_git_blob_sha1': new['implementation_bindings']['implementation_contract_git_blob_sha1'],
    }
    if nested != REQUIRED:
        raise RuntimeError('corrected Q top-level/nested binding disagreement')

    if new['schema'] != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1':
        raise RuntimeError('corrected Q schema')
    if new['status'] != 'TERMINAL_AUDIT_AUTHORITY' or new['verdict'] not in ('QUALIFIED', 'CONFIRMED'):
        raise RuntimeError('corrected Q status/verdict')
    if new['sentinel_science_execution_authorized'] is not True:
        raise RuntimeError('corrected Q sentinel authorization field')
    if new['full_107_row_execution_authorized'] is not False or new['full_replay_launch_authorized'] is not False:
        raise RuntimeError('corrected Q full replay firewall')

    if a['schema'] != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1' or a['status'] != 'TERMINAL_LAUNCH_AUTHORITY':
        raise RuntimeError('A schema/status')
    if a['active_workflow_git_blob_sha1'] != EXPECTED_BLOBS[W]:
        raise RuntimeError('A/W binding')
    if a['executor_git_blob_sha1'] != EXPECTED_BLOBS[E] or a['decision_git_blob_sha1'] != EXPECTED_BLOBS[D]:
        raise RuntimeError('A code bindings')
    if a['sentinel_science_execution_authorized'] is not True or a['full_107_row_execution_authorized'] is not False:
        raise RuntimeError('A authorization boundary')
    if a['launch_descriptor_git_blob_bound_by_authority'] is not False:
        raise RuntimeError('A unexpectedly binds final L')

    if l['schema'] != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1' or l['status'] != 'FROZEN_ONE_RUN_LAUNCH_DESCRIPTOR':
        raise RuntimeError('L candidate schema/status')
    if l['active_workflow_git_blob_sha1'] != EXPECTED_BLOBS[W] or l['launch_authority_git_blob_sha1'] != EXPECTED_BLOBS[A]:
        raise RuntimeError('L candidate W/A binding')
    if l['sentinel_science_execution_authorized'] is not True or l['full_107_row_execution_authorized'] is not False:
        raise RuntimeError('L candidate authorization boundary')

    required_w_fragments = [
        "assert Q['active_workflow_git_blob_sha1']==blob(W)",
        "assert Q['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])",
        "assert Q['launch_descriptor_git_blob_sha1']==blob(os.environ['LAUNCH'])",
        "assert Q['executor_git_blob_sha1']==blob(E)",
        "assert Q['decision_git_blob_sha1']==blob(D)",
        "assert Q['implementation_contract_git_blob_sha1']==blob(I)",
        "paths:\n      - 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'",
        "test \"$CURRENT_RUN_ATTEMPT\" = 1",
    ]
    missing_fragments = [x for x in required_w_fragments if x not in w]
    if missing_fragments:
        raise RuntimeError(f'W runtime contract changed/missing fragments: {missing_fragments}')
    if 'workflow_dispatch:' in w:
        raise RuntimeError('active W unexpectedly has manual dispatch')

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_Q_RUNTIME_SCHEMA_CORRECTION_STATIC_AUDIT_RECEIPT_V0_1',
        'verdict': 'PASS_STATIC_CANDIDATE',
        'classification': 'SENTINEL_Q_RUNTIME_SCHEMA_CORRECTION_STATIC_COMPATIBLE_CANDIDATE',
        'effect': '+0/+0',
        'old_final_Q_git_blob_sha1': EXPECTED_BLOBS[OLD_Q],
        'corrected_Q_candidate_git_blob_sha1': EXPECTED_BLOBS[NEW_Q],
        'semantic_delta_exactly_six_top_level_bindings': True,
        'top_level_bindings_match_nested_bindings': True,
        'would_pass_W_Q_binding_assertions_with_frozen_L_candidate': True,
        'final_Q_replaced_by_this_receipt': False,
        'final_L_present': False,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'sentinel_science_execution_authorized_by_this_receipt': False,
        'full_107_row_execution_authorized': False,
        'requires_independent_funnel_qualification': True,
        'token': 'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_Q_RUNTIME_SCHEMA_CORRECTION_STATIC_PLUS_0_PLUS_0',
    }
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])


if __name__ == '__main__':
    main()
