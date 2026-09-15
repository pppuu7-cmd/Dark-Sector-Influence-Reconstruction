#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

BASE = '78f96f2c60db385f88a391b7fd046dd312176019'
A_C = 'docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json'
L_C = 'docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json'
Q_C = 'docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json'
FINAL_A = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
FINAL_Q = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'
FINAL_L = 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
W = '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
E = 'ci/layerb_beta_v026_r1_sentinel_v0_1.py'
D = 'ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py'
I = 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json'
IQ = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_PR171_QUALIFICATION_AUDIT_V0_2.json'
R1 = 'docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json'
P = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json'
BLOCKER = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_SCHEMA_BLOCKER_V0_2.json'
CONTRACT = 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_CONTRACT_V0_2.json'

OLD_A = '4ba40e59e6a9d48636d95d07efab575e56ae0966'
OLD_L = '9c217e41764d979bea12644fae372354241bc976'
OLD_Q = 'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd'
NEW_A = '1c9945dd00b137f3e202efa14bf4112fffebf8af'
NEW_L = 'fa7014435f0a5688def2124898ddd01d0c0183aa'
NEW_Q = 'f7b97f47d9e771e3d3ea78875da5a45962160cd0'
W_BLOB = '19907175f0f3417ddee2aba6916d961c6be02e26'
E_BLOB = '9affe7c7d4e02bbc728ba15e3cde893ec9876b38'
D_BLOB = '97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9'
I_BLOB = 'e14804463d9eab288162b4c98e8dd5c1fd6a10eb'
IQ_BLOB = '5d042377fa48d896865db0ada11508015c74e350'
R1_BLOB = 'b510d8e97baf1c0b7b216c0605d83cdd029254e9'
P_BLOB = 'cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'
BLOCKER_BLOB = '09190c92c1311b66e953d19ef3811d63a0bf871a'
CONTRACT_BLOB = '01af3648bd3dc640acf35c7b0b7c116334b61cfe'

EXPECTED_LIVE = {
    A_C: NEW_A,
    L_C: NEW_L,
    Q_C: NEW_Q,
    FINAL_A: OLD_A,
    FINAL_Q: OLD_Q,
    W: W_BLOB,
    E: E_BLOB,
    D: D_BLOB,
    I: I_BLOB,
    IQ: IQ_BLOB,
    R1: R1_BLOB,
    P: P_BLOB,
    BLOCKER: BLOCKER_BLOB,
    CONTRACT: CONTRACT_BLOB,
}
Q_TOP = {
    'active_workflow_git_blob_sha1': W_BLOB,
    'launch_authority_git_blob_sha1': NEW_A,
    'launch_descriptor_git_blob_sha1': NEW_L,
    'executor_git_blob_sha1': E_BLOB,
    'decision_git_blob_sha1': D_BLOB,
    'implementation_contract_git_blob_sha1': I_BLOB,
}


def run(*args: str) -> str:
    return subprocess.check_output(list(args), text=True).strip()


def blob(path: str) -> str:
    return run('git', 'hash-object', path)


def load(path: str):
    return json.load(open(path))


def load_at(commit: str, path: str):
    return json.loads(run('git', 'show', f'{commit}:{path}'))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    for path, expected in EXPECTED_LIVE.items():
        if not Path(path).is_file():
            raise RuntimeError(f'missing required path: {path}')
        got = blob(path)
        if got != expected:
            raise RuntimeError(f'{path} blob mismatch: {got} != {expected}')
    if Path(FINAL_L).exists():
        raise RuntimeError('final L must remain absent during correction audit')

    old_a = load_at(BASE, A_C)
    old_l = load_at(BASE, L_C)
    old_q = load_at(BASE, Q_C)
    if run('git', 'rev-parse', f'{BASE}:{A_C}') != OLD_A: raise RuntimeError('base A identity')
    if run('git', 'rev-parse', f'{BASE}:{L_C}') != OLD_L: raise RuntimeError('base L identity')
    if run('git', 'rev-parse', f'{BASE}:{Q_C}') != OLD_Q: raise RuntimeError('base Q identity')

    a = load(A_C); l = load(L_C); q = load(Q_C)
    contract = load(CONTRACT); blocker = load(BLOCKER)
    w = Path(W).read_text(); e = Path(E).read_text(); decision = Path(D).read_text()
    p = load(P)

    # Exact minimal semantic delta: A = old A + one alias.
    if 'promotion_authority_git_blob_sha1' in old_a:
        raise RuntimeError('base A unexpectedly already had executor alias')
    stripped_a = dict(a)
    if stripped_a.pop('promotion_authority_git_blob_sha1', None) != P_BLOB:
        raise RuntimeError('corrected A alias mismatch')
    if stripped_a != old_a:
        raise RuntimeError('corrected A changes semantics beyond one alias')

    # Exact minimal semantic delta: L changes only exact A binding.
    restored_l = dict(l)
    if restored_l.get('launch_authority_git_blob_sha1') != NEW_A:
        raise RuntimeError('corrected L does not bind corrected A')
    restored_l['launch_authority_git_blob_sha1'] = OLD_A
    if restored_l != old_l:
        raise RuntimeError('corrected L changes semantics beyond A binding')

    # Exact minimal semantic delta: Q adds six top-level bindings and updates nested A/L bindings.
    work_q = json.loads(json.dumps(q))
    for key, expected in Q_TOP.items():
        if key in old_q:
            raise RuntimeError(f'base Q unexpectedly has top-level {key}')
        if work_q.pop(key, None) != expected:
            raise RuntimeError(f'corrected Q top-level mismatch: {key}')
    if work_q['acyclic_package']['launch_authority_git_blob_sha1'] != NEW_A:
        raise RuntimeError('corrected Q nested A mismatch')
    if work_q['acyclic_package']['launch_descriptor_git_blob_sha1'] != NEW_L:
        raise RuntimeError('corrected Q nested L mismatch')
    work_q['acyclic_package']['launch_authority_git_blob_sha1'] = OLD_A
    work_q['acyclic_package']['launch_descriptor_git_blob_sha1'] = OLD_L
    if work_q != old_q:
        raise RuntimeError('corrected Q changes semantics beyond allowed runtime bindings')

    if blocker['verdict'] != 'BLOCKED' or blocker['final_L_creation_authorized'] is not False:
        raise RuntimeError('v0.2 blocker not fail-closed')
    if contract['status'] != 'PROSPECTIVELY_FROZEN_GOVERNANCE_ONLY_CORRECTION_CANDIDATE_NOT_EXECUTABLE':
        raise RuntimeError('correction contract status')
    if contract['corrected_package']['A_git_blob_sha1'] != NEW_A or contract['corrected_package']['L_git_blob_sha1'] != NEW_L or contract['corrected_package']['Q_git_blob_sha1'] != NEW_Q:
        raise RuntimeError('correction contract package identities')

    # Simulate frozen W authorize data contract against corrected A/L/Q.
    if a['schema'] != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1' or a['status'] != 'TERMINAL_LAUNCH_AUTHORITY':
        raise RuntimeError('A schema/status')
    if a['authorized_launch_count'] != 1 or a['sentinel_science_execution_authorized'] is not True or a['full_107_row_execution_authorized'] is not False:
        raise RuntimeError('A authorization boundary')
    if a['r1_contract_git_blob_sha1'] != R1_BLOB or a['r1_promotion_authority_git_blob_sha1'] != P_BLOB:
        raise RuntimeError('A R1 bindings')
    if a['sentinel_implementation_contract_git_blob_sha1'] != I_BLOB or a['sentinel_implementation_qualification_git_blob_sha1'] != IQ_BLOB:
        raise RuntimeError('A implementation bindings')
    if a['executor_git_blob_sha1'] != E_BLOB or a['decision_git_blob_sha1'] != D_BLOB or a['active_workflow_git_blob_sha1'] != W_BLOB:
        raise RuntimeError('A code/W bindings')
    if a['launch_descriptor_git_blob_bound_by_authority'] is not False or a['requires_separate_launch_package_qualification'] is not True:
        raise RuntimeError('A DAG boundary')

    if l['schema'] != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1' or l['status'] != 'FROZEN_ONE_RUN_LAUNCH_DESCRIPTOR':
        raise RuntimeError('L schema/status')
    if l['active_workflow_git_blob_sha1'] != W_BLOB or l['launch_authority_git_blob_sha1'] != NEW_A:
        raise RuntimeError('L W/A bindings')
    if l['authorized_launch_count'] != 1 or l['sentinel_science_execution_authorized'] is not True or l['full_107_row_execution_authorized'] is not False:
        raise RuntimeError('L authorization boundary')
    if l['trigger_semantics']['final_operation_must_create_new_file_not_modify_existing_file'] is not True or l['trigger_semantics']['workflow_run_attempt_must_equal'] != 1 or l['trigger_semantics']['rerun_forbidden'] is not True:
        raise RuntimeError('L one-run trigger semantics')

    if q['schema'] != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1' or q['status'] != 'TERMINAL_AUDIT_AUTHORITY' or q['verdict'] not in ('QUALIFIED','CONFIRMED'):
        raise RuntimeError('Q schema/status/verdict')
    if q['sentinel_science_execution_authorized'] is not True or q['full_107_row_execution_authorized'] is not False:
        raise RuntimeError('Q authorization boundary')
    for key, expected in Q_TOP.items():
        if q[key] != expected:
            raise RuntimeError(f'Q runtime binding {key}')
    if q['acyclic_package']['active_workflow_git_blob_sha1'] != W_BLOB or q['acyclic_package']['launch_authority_git_blob_sha1'] != NEW_A or q['acyclic_package']['launch_descriptor_git_blob_sha1'] != NEW_L:
        raise RuntimeError('Q nested package bindings')
    if q['implementation_bindings']['executor_git_blob_sha1'] != E_BLOB or q['implementation_bindings']['decision_git_blob_sha1'] != D_BLOB or q['implementation_bindings']['implementation_contract_git_blob_sha1'] != I_BLOB:
        raise RuntimeError('Q nested implementation bindings')

    # Frozen W source must still consume exactly the corrected package contract shape.
    w_needles = [
        "assert A['r1_promotion_authority_git_blob_sha1']==blob(P)",
        "assert A['active_workflow_git_blob_sha1']==blob(W)",
        "assert L['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])",
        "assert L['active_workflow_git_blob_sha1']==blob(W)",
        "assert Q['active_workflow_git_blob_sha1']==blob(W)",
        "assert Q['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])",
        "assert Q['launch_descriptor_git_blob_sha1']==blob(os.environ['LAUNCH'])",
        "assert Q['executor_git_blob_sha1']==blob(E)",
        "assert Q['decision_git_blob_sha1']==blob(D)",
        "assert Q['implementation_contract_git_blob_sha1']==blob(I)",
        "test \"$CURRENT_RUN_ATTEMPT\" = 1",
        "assert added.count(launch)==1",
        "assert launch not in modified and launch not in removed",
    ]
    missing_w = [x for x in w_needles if x not in w]
    if missing_w:
        raise RuntimeError(f'frozen W consumer contract changed: {missing_w}')
    if 'workflow_dispatch:' in w:
        raise RuntimeError('active W unexpectedly exposes workflow_dispatch')

    # Frozen executor launch-authority consumer must pass corrected A.
    e_needles = [
        "a.get('schema') != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1'",
        "a.get('status') != 'TERMINAL_LAUNCH_AUTHORITY'",
        "a.get('sentinel_science_execution_authorized') is not True",
        "a.get('full_107_row_execution_authorized') is not False",
        "a.get('r1_contract_git_blob_sha1') != R1_CONTRACT_BLOB",
        "a.get('promotion_authority_git_blob_sha1') != PROMOTION_AUTHORITY_BLOB",
    ]
    missing_e = [x for x in e_needles if x not in e]
    if missing_e:
        raise RuntimeError(f'frozen executor consumer contract changed: {missing_e}')
    if a['promotion_authority_git_blob_sha1'] != P_BLOB:
        raise RuntimeError('corrected A still fails executor promotion-authority alias')

    # Executor PR169 precondition and decision bindings remain satisfied.
    if p['verdict'] != 'QUALIFIED' or p['classification'] != 'V0_26_R1_PROSPECTIVE_NUMERICAL_SPECIFICATION_QUALIFIED_FOR_PROMOTION':
        raise RuntimeError('PR169 authority identity semantics')
    if p['post_promotion_authorization']['sentinel_executor_construction_authorized_after_exact_r1_is_on_main'] is not True:
        raise RuntimeError('PR169 executor construction precondition')
    if p['sentinel_science_execution_authorized'] is not False:
        raise RuntimeError('PR169 unexpectedly authorizes science')
    if "'full_replay_launch_authorized':False" not in decision or "'full_107_row_execution_authorized':False" not in decision:
        raise RuntimeError('decision full-replay firewall source changed')

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_STATIC_AUDIT_RECEIPT_V0_2',
        'verdict': 'PASS_STATIC_CANDIDATE',
        'classification': 'SENTINEL_GOVERNANCE_ONLY_A_L_Q_RUNTIME_CHAIN_CORRECTION_STATIC_COMPATIBLE_CANDIDATE',
        'effect': '+0/+0',
        'base_main_sha': BASE,
        'old_A_git_blob_sha1': OLD_A,
        'old_L_git_blob_sha1': OLD_L,
        'old_Q_git_blob_sha1': OLD_Q,
        'corrected_A_git_blob_sha1': NEW_A,
        'corrected_L_git_blob_sha1': NEW_L,
        'corrected_Q_git_blob_sha1': NEW_Q,
        'A_delta_exactly_one_alias': True,
        'L_delta_exactly_A_binding': True,
        'Q_delta_exactly_six_top_level_plus_corrected_A_L_bindings': True,
        'W_authorize_contract_static_pass': True,
        'executor_launch_authority_contract_static_pass': True,
        'PR169_executor_precondition_static_pass': True,
        'decision_full_replay_firewall_static_pass': True,
        'final_A_replaced_by_this_receipt': False,
        'final_Q_replaced_by_this_receipt': False,
        'final_L_present': False,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'sentinel_science_execution_authorized_by_this_receipt': False,
        'full_107_row_execution_authorized': False,
        'requires_independent_funnel_qualification': True,
        'token': 'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_STATIC_V0_2_PLUS_0_PLUS_0',
    }
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])


if __name__ == '__main__':
    main()
