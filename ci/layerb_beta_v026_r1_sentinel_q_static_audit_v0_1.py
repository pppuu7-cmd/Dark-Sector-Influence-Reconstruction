#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

Q_CANDIDATE = 'docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json'
FUTURE_W = '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
FUTURE_A = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
FUTURE_L = 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
FUTURE_Q = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'

EXPECTED = {
    'Q_candidate': (Q_CANDIDATE, 'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd'),
    'r1_contract': ('docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json', 'b510d8e97baf1c0b7b216c0605d83cdd029254e9'),
    'r1_promotion': ('docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json', 'cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'),
    'implementation_contract': ('docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json', 'e14804463d9eab288162b4c98e8dd5c1fd6a10eb'),
    'implementation_qualification': ('docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_PR171_QUALIFICATION_AUDIT_V0_2.json', '5d042377fa48d896865db0ada11508015c74e350'),
    'pr173_funnel_authority': ('docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PR173_FUNNEL_QUALIFICATION_V0_1.json', 'ed3cec954d2077e6b5a6daab5da53e8fe72cc2e0'),
    'pr173_promotion_confirmation': ('docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PR173_PROMOTION_CONFIRMATION_V0_1.json', '499fec9c1738f410bb1d4c714da96f60ac1de7ab'),
    'package_contract': ('docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_CONTRACT_V0_1.json', '26806597e651fb22956de59f102c0ad24d11c576'),
    'W': ('docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml', '19907175f0f3417ddee2aba6916d961c6be02e26'),
    'A': ('docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json', '4ba40e59e6a9d48636d95d07efab575e56ae0966'),
    'L': ('docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json', '9c217e41764d979bea12644fae372354241bc976'),
    'executor': ('ci/layerb_beta_v026_r1_sentinel_v0_1.py', '9affe7c7d4e02bbc728ba15e3cde893ec9876b38'),
    'decision': ('ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py', '97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9'),
}

STATIC_RECEIPT_LEN = 1348
STATIC_RECEIPT_SHA256 = '133df1d2753c9228198a15be792fdcbbf99da243efeccdb785d610aad7dc5ee5'
FUNNEL_RECEIPT_LEN = 1728
FUNNEL_RECEIPT_SHA256 = 'f525feaf938e99a9282ea97619842ded9883ac54219e60c9bbdd3f34f934a1aa'


def git_blob(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def read_json_bytes(path: str, expected_len: int, expected_sha: str) -> dict:
    b = Path(path).read_bytes()
    if len(b) != expected_len:
        raise RuntimeError(f'{path}: byte length {len(b)} != {expected_len}')
    got = sha256_bytes(b)
    if got != expected_sha:
        raise RuntimeError(f'{path}: sha256 {got} != {expected_sha}')
    return json.loads(b)


def require_bool(d: dict, key: str, value: bool) -> None:
    if d.get(key) is not value:
        raise RuntimeError(f'{key}: {d.get(key)!r} != {value!r}')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--static-receipt', required=True)
    ap.add_argument('--funnel-receipt', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    for name, (path, expected) in EXPECTED.items():
        p = Path(path)
        if not p.is_file():
            raise RuntimeError(f'missing frozen input {name}: {path}')
        got = git_blob(path)
        if got != expected:
            raise RuntimeError(f'{name} blob {got} != {expected}')

    active_state = {p: Path(p).exists() for p in (FUTURE_W, FUTURE_A, FUTURE_L, FUTURE_Q)}
    if any(active_state.values()):
        raise RuntimeError(f'active/final path present during Q candidate audit: {active_state}')

    q = json.loads(Path(Q_CANDIDATE).read_text())
    if q['schema'] != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1':
        raise RuntimeError('Q schema')
    if q['status'] != 'TERMINAL_AUDIT_AUTHORITY' or q['verdict'] != 'QUALIFIED':
        raise RuntimeError('Q future authority status/verdict')
    if q['classification'] != 'SENTINEL_ACYCLIC_LAUNCH_PACKAGE_QUALIFIED_FOR_EXACT_ONE_RUN_SENTINEL_ACTIVATION':
        raise RuntimeError('Q classification')
    cs = q['candidate_storage']
    require_bool(cs, 'candidate_storage_is_inert', True)
    require_bool(cs, 'qualification_effective_only_after_exact_copy_to_future_authority_path', True)
    if cs['future_authority_path'] != FUTURE_Q:
        raise RuntimeError('Q future path')
    if cs['base_main_sha_at_candidate_creation'] != 'f9de6daceb887bf86b47b02f71cae70b70f173a0':
        raise RuntimeError('Q base main binding')

    g = q['governing_authorities']
    expected_governing = {
        'r1_contract_git_blob_sha1': EXPECTED['r1_contract'][1],
        'r1_promotion_authority_git_blob_sha1': EXPECTED['r1_promotion'][1],
        'implementation_contract_git_blob_sha1': EXPECTED['implementation_contract'][1],
        'implementation_qualification_git_blob_sha1': EXPECTED['implementation_qualification'][1],
        'pr173_funnel_authority_git_blob_sha1': EXPECTED['pr173_funnel_authority'][1],
        'pr173_post_promotion_confirmation_git_blob_sha1': EXPECTED['pr173_promotion_confirmation'][1],
        'inactive_package_contract_git_blob_sha1': EXPECTED['package_contract'][1],
    }
    for k, v in expected_governing.items():
        if g[k] != v:
            raise RuntimeError(f'Q governing {k}')

    pkg = q['acyclic_package']
    if pkg['active_workflow_git_blob_sha1'] != EXPECTED['W'][1]:
        raise RuntimeError('Q W binding')
    if pkg['launch_authority_git_blob_sha1'] != EXPECTED['A'][1]:
        raise RuntimeError('Q A binding')
    if pkg['launch_descriptor_git_blob_sha1'] != EXPECTED['L'][1]:
        raise RuntimeError('Q L binding')
    for k in ('A_binds_W', 'L_binds_W', 'L_binds_A', 'mutual_A_L_exact_blob_cycle_absent'):
        require_bool(pkg, k, True)
    require_bool(pkg, 'A_binds_L', False)

    impl = q['implementation_bindings']
    if impl['executor_git_blob_sha1'] != EXPECTED['executor'][1] or impl['decision_git_blob_sha1'] != EXPECTED['decision'][1]:
        raise RuntimeError('Q implementation code binding')
    if impl['implementation_contract_git_blob_sha1'] != EXPECTED['implementation_contract'][1]:
        raise RuntimeError('Q implementation contract binding')

    static = read_json_bytes(args.static_receipt, STATIC_RECEIPT_LEN, STATIC_RECEIPT_SHA256)
    if static['token'] != 'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_STATIC_AUDIT_PLUS_0_PLUS_0':
        raise RuntimeError('static receipt token')
    if static['classification'] != 'SENTINEL_LAUNCH_PACKAGE_ACYCLIC_RESPONSE_BLIND_STATIC_AUDIT_PASS':
        raise RuntimeError('static receipt classification')
    if static['W_git_blob_sha1'] != EXPECTED['W'][1] or static['A_git_blob_sha1'] != EXPECTED['A'][1] or static['L_git_blob_sha1'] != EXPECTED['L'][1]:
        raise RuntimeError('static receipt W/A/L binding')
    require_bool(static, 'class_solver_invoked', False)
    require_bool(static, 'scientific_response_read', False)
    require_bool(static, 'sentinel_science_execution_authorized_by_this_receipt', False)
    require_bool(static, 'full_107_row_execution_authorized', False)

    se = q['static_package_evidence']
    if se['artifact_id'] != 10393170033 or se['artifact_zip_sha256'] != 'e95c4675db77a2ecd864d21e39dfdccffe289ed61a84ece95182f22c46e16184':
        raise RuntimeError('Q static artifact binding')
    if se['receipt_byte_length'] != STATIC_RECEIPT_LEN or se['receipt_sha256'] != STATIC_RECEIPT_SHA256:
        raise RuntimeError('Q static inner binding')

    funnel = read_json_bytes(args.funnel_receipt, FUNNEL_RECEIPT_LEN, FUNNEL_RECEIPT_SHA256)
    if funnel['token'] != 'QUALIFIED_DSIR_V0_26_R1_SENTINEL_LAUNCH_PR173_FUNNEL_AUDIT_PLUS_0_PLUS_0' or funnel['verdict'] != 'QUALIFIED':
        raise RuntimeError('external funnel token/verdict')
    if funnel['W_git_blob_sha1'] != EXPECTED['W'][1] or funnel['A_git_blob_sha1'] != EXPECTED['A'][1] or funnel['L_git_blob_sha1'] != EXPECTED['L'][1]:
        raise RuntimeError('external funnel W/A/L binding')
    require_bool(funnel, 'candidate_future_workflow_executed_by_funnel_audit', False)
    require_bool(funnel, 'class_solver_invoked_by_funnel_audit', False)
    require_bool(funnel, 'scientific_response_read_by_funnel_audit', False)
    require_bool(funnel, 'sentinel_science_execution_authorized_by_this_receipt', False)
    require_bool(funnel, 'full_107_row_execution_authorized_by_this_receipt', False)

    fe = q['external_funnel_evidence']
    if fe['artifact_id'] != 10392992058 or fe['artifact_zip_sha256'] != '73ea7849b60dd65b20e2f93144c7afbb0f7dc7bd09ae8e0e9cfe0e3d63801c59':
        raise RuntimeError('Q funnel artifact binding')
    if fe['receipt_byte_length'] != FUNNEL_RECEIPT_LEN or fe['receipt_sha256'] != FUNNEL_RECEIPT_SHA256:
        raise RuntimeError('Q funnel inner binding')

    pp = json.loads(Path(EXPECTED['pr173_promotion_confirmation'][0]).read_text())
    if pp['verdict'] != 'CONFIRMED_SCOPED':
        raise RuntimeError('post-promotion confirmation verdict')

    one = q['one_run_authorization']
    if one['authorized_launch_count'] != 1:
        raise RuntimeError('Q launch count')
    require_bool(one, 'sentinel_science_execution_authorized', True)
    for k in ('workflow_event_must_be_push', 'unique_exact_head_workflow_push_run_required', 'launch_descriptor_must_be_newly_added_exactly_once', 'launch_descriptor_modify_or_remove_forbidden', 'rerun_forbidden'):
        require_bool(one, k, True)
    if one['workflow_run_attempt_must_equal_one'] is not True:
        raise RuntimeError('Q first attempt gate')

    require_bool(q, 'sentinel_science_execution_authorized', True)
    require_bool(q, 'full_replay_launch_authorized', False)
    require_bool(q, 'full_107_row_execution_authorized', False)

    act = q['activation_order_after_Q_is_independently_qualified_and_promoted']
    require_bool(act, 'phase_1_exact_copy_W_to_active_path_and_A_to_authority_path_without_L', True)
    require_bool(act, 'phase_1_must_not_trigger_science', True)
    require_bool(act, 'phase_1_requires_separate_pretrigger_static_audit', True)
    require_bool(act, 'phase_2_exact_copy_this_Q_to_future_authority_path', True)
    require_bool(act, 'phase_2_must_not_trigger_science', True)
    require_bool(act, 'phase_3_create_exact_L_at_new_trigger_path', True)
    require_bool(act, 'phase_3_is_only_one_run_trigger', True)

    forbidden = q['forbidden']
    for k in (
        'treat_candidate_storage_as_current_authority',
        'stage_active_W_or_A_before_Q_static_audit_and_promotion',
        'create_final_L_before_pretrigger_audit',
        'launch_sentinel_science_from_candidate_storage',
        'launch_full_107_row_replay',
        'read_covariance', 'read_whitening', 'read_nuisance', 'read_relation_null',
        'open_Wm_S3', 'launch_global_65537', 'open_statistical_or_physical_science_gate',
    ):
        require_bool(forbidden, k, True)

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_Q_STATIC_AUDIT_V0_1',
        'token': 'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_Q_STATIC_AUDIT_PLUS_0_PLUS_0',
        'classification': 'SENTINEL_PACKAGE_Q_RESPONSE_BLIND_STATIC_AUDIT_PASS',
        'effect': '+0/+0',
        'candidate_head_sha': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        'Q_candidate_git_blob_sha1': EXPECTED['Q_candidate'][1],
        'W_git_blob_sha1': EXPECTED['W'][1],
        'A_git_blob_sha1': EXPECTED['A'][1],
        'L_git_blob_sha1': EXPECTED['L'][1],
        'static_receipt_sha256': STATIC_RECEIPT_SHA256,
        'external_funnel_receipt_sha256': FUNNEL_RECEIPT_SHA256,
        'active_path_state': active_state,
        'candidate_storage_inert': True,
        'future_Q_exact_copy_semantics_verified': True,
        'authorized_launch_count_if_future_Q_promoted': 1,
        'sentinel_science_execution_authorized_by_candidate_storage': False,
        'future_Q_content_authorizes_one_sentinel_run': True,
        'full_replay_launch_authorized': False,
        'full_107_row_execution_authorized': False,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'next_admissible_action': 'INDEPENDENT_Q_FUNNEL_REVIEW_THEN_EXACT_Q_PROMOTION_AND_W_A_PRETRIGGER_STAGING_ONLY_IF_QUALIFIED',
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])


if __name__ == '__main__':
    main()
