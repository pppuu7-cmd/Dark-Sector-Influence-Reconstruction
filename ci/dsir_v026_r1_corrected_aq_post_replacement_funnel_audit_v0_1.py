#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
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

OLD_A_BLOB = '4ba40e59e6a9d48636d95d07efab575e56ae0966'
OLD_Q_BLOB = 'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd'
A_BLOB = '1c9945dd00b137f3e202efa14bf4112fffebf8af'
Q_BLOB = 'f7b97f47d9e771e3d3ea78875da5a45962160cd0'
L_BLOB = 'fa7014435f0a5688def2124898ddd01d0c0183aa'
W_BLOB = '19907175f0f3417ddee2aba6916d961c6be02e26'
E_BLOB = '9affe7c7d4e02bbc728ba15e3cde893ec9876b38'
D_BLOB = '97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9'
I_BLOB = 'e14804463d9eab288162b4c98e8dd5c1fd6a10eb'
P_BLOB = 'cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'
C_BLOB = '019efc37f9a1110e70574c381482b1bef3310700'
PRODUCER_RECEIPT_SHA256 = 'e0b31076a7dea383a2749c63089373de3b1be1fa4426f6f23c39d7b3c37d43d2'
PRODUCER_RECEIPT_BYTES = 1970
PRODUCER_RUN_ID = 35032839418
PRODUCER_JOB_ID = 104595075657
PRODUCER_ARTIFACT_ID = 10421774259
PRODUCER_ZIP_SHA256 = '5b3c9e894d1f09d3aab707a1894adaf20df7ed16f3caa1b60a8b8fc00d246c5c'


def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def blob(path: str) -> str:
    return sh('git', 'hash-object', path)


def rev_blob(rev: str, path: str) -> str | None:
    try:
        return sh('git', 'rev-parse', f'{rev}:{path}')
    except subprocess.CalledProcessError:
        return None


def rev_json(rev: str, path: str):
    return json.loads(subprocess.check_output(['git', 'show', f'{rev}:{path}']))


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--producer-receipt', required=True)
    ap.add_argument('--science-runs', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    assert sh('git', 'rev-parse', f'{PROMO}^1') == FIRST_PARENT
    assert sh('git', 'rev-parse', f'{PROMO}^2') == STAGING_PARENT
    subprocess.run(['git', 'merge-base', '--is-ancestor', PROMO, 'HEAD'], check=True)
    changed = sh('git', 'diff-tree', '--no-commit-id', '--name-status', '-r', FIRST_PARENT, PROMO).splitlines()
    assert changed == [f'M\t{A}', f'M\t{Q}'], changed
    assert rev_blob(FIRST_PARENT, A) == OLD_A_BLOB
    assert rev_blob(FIRST_PARENT, Q) == OLD_Q_BLOB
    assert rev_blob(PROMO, A) == A_BLOB
    assert rev_blob(PROMO, Q) == Q_BLOB
    assert rev_blob(PROMO, L) is None

    expected_live = {A:A_BLOB,Q:Q_BLOB,W:W_BLOB,E:E_BLOB,D:D_BLOB,I:I_BLOB,P:P_BLOB,C:C_BLOB}
    live = {p:blob(p) for p in expected_live}
    assert live == expected_live, (live, expected_live)
    assert not Path(L).exists()

    old_a = rev_json(FIRST_PARENT, A)
    new_a = json.loads(Path(A).read_text())
    expected_a = copy.deepcopy(old_a)
    expected_a['promotion_authority_git_blob_sha1'] = P_BLOB
    assert new_a == expected_a

    old_q = rev_json(FIRST_PARENT, Q)
    new_q = json.loads(Path(Q).read_text())
    expected_q = copy.deepcopy(old_q)
    top = {
        'active_workflow_git_blob_sha1': W_BLOB,
        'launch_authority_git_blob_sha1': A_BLOB,
        'launch_descriptor_git_blob_sha1': L_BLOB,
        'executor_git_blob_sha1': E_BLOB,
        'decision_git_blob_sha1': D_BLOB,
        'implementation_contract_git_blob_sha1': I_BLOB,
    }
    for k,v in top.items():
        expected_q[k] = v
    expected_q['acyclic_package']['launch_authority_git_blob_sha1'] = A_BLOB
    expected_q['acyclic_package']['launch_descriptor_git_blob_sha1'] = L_BLOB
    assert new_q == expected_q

    conf = json.loads(Path(C).read_text())
    assert conf['verdict'] == 'CONFIRMED_SCOPED'
    assert conf['exact_bindings']['corrected_A_git_blob_sha1'] == A_BLOB
    assert conf['exact_bindings']['corrected_L_git_blob_sha1'] == L_BLOB
    assert conf['exact_bindings']['corrected_Q_git_blob_sha1'] == Q_BLOB
    assert conf['promotion_order']['final_L_creation_authorized_now'] is False

    wtxt = Path(W).read_text()
    for k in top:
        assert f"Q['{k}']" in wtxt, k
    etxt = Path(E).read_text()
    assert "a.get('promotion_authority_git_blob_sha1')" in etxt
    assert "a.get('full_107_row_execution_authorized') is not False" in etxt
    dtxt = Path(D).read_text()
    assert "'full_replay_launch_authorized':False" in dtxt
    assert "'full_107_row_execution_authorized':False" in dtxt

    raw = Path(a.producer_receipt).read_bytes()
    assert len(raw) == PRODUCER_RECEIPT_BYTES
    assert sha256_bytes(raw) == PRODUCER_RECEIPT_SHA256
    producer = json.loads(raw)
    assert producer['verdict'] == 'CONFIRMED_SCOPED'
    assert producer['classification'] == 'SENTINEL_CORRECTED_AQ_MAIN_REPLACEMENT_CONFIRMED_FAIL_CLOSED_L_GATE_REVIEW_ADMISSIBLE'
    assert producer['reviewed_promotion_merge_sha'] == PROMO
    assert producer['final_A_git_blob_sha1'] == A_BLOB
    assert producer['final_Q_git_blob_sha1'] == Q_BLOB
    assert producer['bound_future_L_git_blob_sha1'] == L_BLOB
    assert producer['final_L_present'] is False
    assert producer['promotion_head_push_run_count'] == 0
    assert producer['frozen_W_Q_consumer_contract_compatible'] is True
    assert producer['frozen_executor_A_consumer_contract_compatible'] is True
    assert producer['decision_full_replay_firewall_intact'] is True
    assert producer['sentinel_workflow_executed'] is False
    assert producer['class_solver_invoked'] is False
    assert producer['scientific_response_read'] is False
    assert producer['covariance_read'] is False
    assert producer['final_L_creation_authorized_by_this_receipt'] is False
    assert producer['full_107_row_execution_authorized'] is False

    runs = json.loads(Path(a.science_runs).read_text())
    rows = runs.get('workflow_runs', [])
    assert int(runs.get('total_count', len(rows))) == len(rows)
    assert len(rows) == 0, rows

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_CORRECTED_AQ_POST_REPLACEMENT_FUNNEL_AUDIT_V0_1',
        'effect': '+0/+0',
        'verdict': 'QUALIFIED',
        'classification': 'SENTINEL_CORRECTED_AQ_POST_REPLACEMENT_FAIL_CLOSED_QUALIFIED_FOR_EXPLICIT_L_GATE_AUTHORITY',
        'reviewed_promotion_merge_sha': PROMO,
        'producer_run_id': PRODUCER_RUN_ID,
        'producer_job_id': PRODUCER_JOB_ID,
        'producer_artifact_id': PRODUCER_ARTIFACT_ID,
        'producer_artifact_zip_sha256': PRODUCER_ZIP_SHA256,
        'producer_receipt_sha256': PRODUCER_RECEIPT_SHA256,
        'producer_receipt_byte_length': PRODUCER_RECEIPT_BYTES,
        'final_A_git_blob_sha1': A_BLOB,
        'final_Q_git_blob_sha1': Q_BLOB,
        'future_exact_L_git_blob_sha1': L_BLOB,
        'active_W_git_blob_sha1': W_BLOB,
        'executor_git_blob_sha1': E_BLOB,
        'decision_git_blob_sha1': D_BLOB,
        'minimal_A_delta_reproduced': True,
        'minimal_Q_delta_reproduced': True,
        'frozen_W_Q_consumer_contract_compatible': True,
        'frozen_executor_A_consumer_contract_compatible': True,
        'decision_full_replay_firewall_intact': True,
        'final_L_present': False,
        'science_workflow_run_count_at_replacement_head': 0,
        'sentinel_science_executed': False,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'L_gate_authority_creation_admissible': True,
        'final_L_creation_authorized_by_this_receipt': False,
        'sentinel_science_execution_authorized_by_this_receipt': False,
        'full_107_row_execution_authorized': False,
        'next_gate': 'PERSIST_SEPARATE_TERMINAL_L_GATE_AUTHORITY_ON_MAIN_THEN_EXACT_CORRECTED_L_NEW_FILE_TRIGGER_ONLY_IF_AUTHORITY_EXPLICITLY_AUTHORIZES',
        'token': 'QUALIFIED_LAYERB_BETA_V0_26_R1_CORRECTED_AQ_POST_REPLACEMENT_FUNNEL_PLUS_0_PLUS_0',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
