#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

PROMO = '41ef654d7552b670c20d3202249d7687bae5f870'
FIRST_PARENT = '08cdbe102f0b9035f815b7321afc45a187fa76b8'
STAGING_PARENT = 'd7c8931ebee1536ae6491395bfc2eb8db2ccd379'
A = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
Q = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'
L = 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
W = '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
E = 'ci/layerb_beta_v026_r1_sentinel_v0_1.py'
D = 'ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py'
I = 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json'
P = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json'
C = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_FUNNEL_CONFIRMATION_V0_1.json'

A_BLOB = '1c9945dd00b137f3e202efa14bf4112fffebf8af'
Q_BLOB = 'f7b97f47d9e771e3d3ea78875da5a45962160cd0'
L_BLOB = 'fa7014435f0a5688def2124898ddd01d0c0183aa'
W_BLOB = '19907175f0f3417ddee2aba6916d961c6be02e26'
E_BLOB = '9affe7c7d4e02bbc728ba15e3cde893ec9876b38'
D_BLOB = '97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9'
I_BLOB = 'e14804463d9eab288162b4c98e8dd5c1fd6a10eb'
P_BLOB = 'cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'
C_BLOB = '019efc37f9a1110e70574c381482b1bef3310700'


def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def blob(path: str) -> str:
    return sh('git', 'hash-object', path)


def rev_blob(rev: str, path: str) -> str | None:
    try:
        return sh('git', 'rev-parse', f'{rev}:{path}')
    except subprocess.CalledProcessError:
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--runs-json', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    assert sh('git', 'rev-parse', f'{PROMO}^1') == FIRST_PARENT
    assert sh('git', 'rev-parse', f'{PROMO}^2') == STAGING_PARENT
    subprocess.run(['git', 'merge-base', '--is-ancestor', PROMO, 'HEAD'], check=True)

    changed = sh('git', 'diff-tree', '--no-commit-id', '--name-status', '-r', FIRST_PARENT, PROMO).splitlines()
    assert changed == [f'M\t{A}', f'M\t{Q}'], changed
    assert rev_blob(PROMO, A) == A_BLOB
    assert rev_blob(PROMO, Q) == Q_BLOB
    assert rev_blob(PROMO, L) is None

    expected_live = {
        A: A_BLOB,
        Q: Q_BLOB,
        W: W_BLOB,
        E: E_BLOB,
        D: D_BLOB,
        I: I_BLOB,
        P: P_BLOB,
        C: C_BLOB,
    }
    live = {p: blob(p) for p in expected_live}
    assert live == expected_live, (live, expected_live)
    assert not Path(L).exists()

    aa = json.loads(Path(A).read_text())
    qq = json.loads(Path(Q).read_text())
    pp = json.loads(Path(P).read_text())
    cc = json.loads(Path(C).read_text())

    assert cc['verdict'] == 'CONFIRMED_SCOPED'
    assert cc['authorized_next_stage'] == 'EXACT_CORRECTED_A_AND_Q_REPLACEMENT_WITHOUT_FINAL_L_THEN_SEPARATE_POST_REPLACEMENT_FAIL_CLOSED_AUDIT'
    assert cc['exact_bindings']['corrected_A_git_blob_sha1'] == A_BLOB
    assert cc['exact_bindings']['corrected_L_git_blob_sha1'] == L_BLOB
    assert cc['exact_bindings']['corrected_Q_git_blob_sha1'] == Q_BLOB

    assert aa['schema'] == 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1'
    assert aa['status'] == 'TERMINAL_LAUNCH_AUTHORITY'
    assert aa['r1_promotion_authority_git_blob_sha1'] == P_BLOB
    assert aa['promotion_authority_git_blob_sha1'] == P_BLOB
    assert aa['executor_git_blob_sha1'] == E_BLOB
    assert aa['decision_git_blob_sha1'] == D_BLOB
    assert aa['active_workflow_git_blob_sha1'] == W_BLOB
    assert aa['sentinel_implementation_contract_git_blob_sha1'] == I_BLOB
    assert aa['sentinel_science_execution_authorized'] is True
    assert aa['full_107_row_execution_authorized'] is False
    assert aa['launch_descriptor_git_blob_bound_by_authority'] is False

    assert qq['schema'] == 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1'
    assert qq['status'] == 'TERMINAL_AUDIT_AUTHORITY'
    assert qq['verdict'] in ('QUALIFIED', 'CONFIRMED')
    required_q = {
        'active_workflow_git_blob_sha1': W_BLOB,
        'launch_authority_git_blob_sha1': A_BLOB,
        'launch_descriptor_git_blob_sha1': L_BLOB,
        'executor_git_blob_sha1': E_BLOB,
        'decision_git_blob_sha1': D_BLOB,
        'implementation_contract_git_blob_sha1': I_BLOB,
    }
    for k, v in required_q.items():
        assert qq[k] == v, (k, qq.get(k), v)
    assert qq['acyclic_package']['active_workflow_git_blob_sha1'] == W_BLOB
    assert qq['acyclic_package']['launch_authority_git_blob_sha1'] == A_BLOB
    assert qq['acyclic_package']['launch_descriptor_git_blob_sha1'] == L_BLOB
    assert qq['implementation_bindings']['executor_git_blob_sha1'] == E_BLOB
    assert qq['implementation_bindings']['decision_git_blob_sha1'] == D_BLOB
    assert qq['implementation_bindings']['implementation_contract_git_blob_sha1'] == I_BLOB
    assert qq['sentinel_science_execution_authorized'] is True
    assert qq['full_107_row_execution_authorized'] is False

    assert pp['verdict'] == 'QUALIFIED'
    assert pp['post_promotion_authorization']['sentinel_executor_construction_authorized_after_exact_r1_is_on_main'] is True
    assert pp['sentinel_science_execution_authorized'] is False

    wtxt = Path(W).read_text()
    for key in required_q:
        assert f"Q['{key}']" in wtxt, key
    assert "A['active_workflow_git_blob_sha1']" in wtxt
    assert "L['launch_authority_git_blob_sha1']" in wtxt
    assert "L['active_workflow_git_blob_sha1']" in wtxt

    etxt = Path(E).read_text()
    assert "a.get('promotion_authority_git_blob_sha1')" in etxt
    assert "a.get('r1_contract_git_blob_sha1')" in etxt
    assert "a.get('full_107_row_execution_authorized') is not False" in etxt

    dtxt = Path(D).read_text()
    assert "'full_replay_launch_authorized':False" in dtxt
    assert "'full_107_row_execution_authorized':False" in dtxt

    runs = json.loads(Path(a.runs_json).read_text())
    rows = runs.get('workflow_runs', [])
    assert int(runs.get('total_count', len(rows))) == len(rows)
    assert len(rows) == 0, rows

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_CORRECTED_AQ_POST_REPLACEMENT_AUDIT_V0_1',
        'effect': '+0/+0',
        'verdict': 'CONFIRMED_SCOPED',
        'classification': 'SENTINEL_CORRECTED_AQ_MAIN_REPLACEMENT_CONFIRMED_FAIL_CLOSED_L_GATE_REVIEW_ADMISSIBLE',
        'reviewed_promotion_merge_sha': PROMO,
        'first_parent_sha': FIRST_PARENT,
        'staging_parent_sha': STAGING_PARENT,
        'exact_changed_files': [A, Q],
        'final_A_git_blob_sha1': A_BLOB,
        'final_Q_git_blob_sha1': Q_BLOB,
        'bound_future_L_git_blob_sha1': L_BLOB,
        'active_W_git_blob_sha1': W_BLOB,
        'executor_git_blob_sha1': E_BLOB,
        'decision_git_blob_sha1': D_BLOB,
        'qualification_authority_git_blob_sha1': C_BLOB,
        'final_L_present': False,
        'promotion_head_push_run_count': 0,
        'frozen_W_Q_consumer_contract_compatible': True,
        'frozen_executor_A_consumer_contract_compatible': True,
        'PR169_executor_precondition_valid': True,
        'decision_full_replay_firewall_intact': True,
        'sentinel_workflow_executed': False,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'final_L_creation_authorized_by_this_receipt': False,
        'sentinel_science_execution_authorized_by_this_receipt': False,
        'full_107_row_execution_authorized': False,
        'next_gate': 'INDEPENDENT_POST_REPLACEMENT_FUNNEL_REVIEW_THEN_EXPLICIT_L_GATE_AUTHORITY_IF_CONFIRMED',
        'token': 'CONFIRMED_LAYERB_BETA_V0_26_R1_CORRECTED_AQ_POST_REPLACEMENT_FAIL_CLOSED_PLUS_0_PLUS_0',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
