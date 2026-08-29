#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PASS = 'PASS_EXP073U_ARTICLE3_PRESUPPORT_COORDINATE_SKELETON_V0_1'
GATES = {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}
EXPECTED = {
    'receipt': '52c9dc6f51078da430788a90551cba5069706481fe2d6cf68f2f879b8537fc45',
    'inventory': '55f55d21eedd3779a729af387205ec7db360617c5e026406d21b3b542f355309',
    'namaster': 'f6000b5e0b87a93ff31f9a22d7aa66ada64149885b126a73f38b6f0f82a59519',
    's0': '7ed9ee2730482f1fb225ec7d07a9221789a15ad03e866968176d01a2bf46bfce',
    's1': 'e38438052af992372ee2006a56fce3a417cc9dd5ee87c9487097c3c986575406',
    's2': 'b0dd293663325de82bf39cc970ac7b84c9c904163234ede451f2925778ff0edc',
    's3': '5f1472e0f7e05426c16aaf416161059c67b056b3f155ab85701bf5c397e2d16d',
}


def sha256_file(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def order_sha256(ids: list[str]) -> str:
    return hashlib.sha256(('\n'.join(ids) + '\n').encode('utf-8')).hexdigest()


def load(path: str, key: str) -> dict:
    observed = sha256_file(path)
    if observed != EXPECTED[key]:
        raise AssertionError(f'{key} JSON SHA mismatch: {observed}')
    return json.loads(Path(path).read_text(encoding='utf-8'))


def main() -> None:
    ap = argparse.ArgumentParser()
    for name in ('receipt', 'inventory', 'namaster', 's0', 's1', 's2', 's3', 'out'):
        ap.add_argument(f'--{name}', required=True)
    a = ap.parse_args()

    receipt = load(a.receipt, 'receipt')
    inv = load(a.inventory, 'inventory')
    namaster = load(a.namaster, 'namaster')
    source = [load(getattr(a, f's{i}'), f's{i}') for i in range(4)]

    assert receipt['status'] == 'PASS_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED'
    assert receipt['support_executor_authorized'] is True
    assert receipt['artifact']['id'] == 9720335366
    assert receipt['artifact']['digest'] == 'sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd'

    assert inv['status'] == 'PASS_EXP073T_PINNED_COSMOTHEKA_INVENTORY_V0_1'
    assert inv['Wm_scalar_coordinate_count'] == 780
    assert inv['WW_scalar_coordinate_count'] == 390
    assert inv['DES_scalar_coordinate_count'] == 1170
    assert inv['BOSS_frozen_pre_support_coordinate_count'] == 240
    assert inv['DES_plus_BOSS_pre_support_inventory_count'] == 1410

    wm = inv['Wm_coordinate_ids']
    ww = inv['WW_coordinate_ids']
    assert order_sha256(wm) == inv['Wm_coordinate_order_sha256'] == 'dc20ff104c707d006992c1579ce9175295fae426b1c32ff47e56c53d9300603a'
    assert order_sha256(ww) == inv['WW_coordinate_order_sha256'] == 'e0cc92706598a8ac6360d0fd669451e4816091f83c01e8744940e94a2b8593b5'
    assert order_sha256(wm + ww) == inv['DES_coordinate_order_sha256'] == '736f80a6dd407b1a3891cb34f35262e415a4f0c9bbb200a9f376102b05988ee4'

    assert namaster['status'] == 'PASS_EXP073T_NAMASTER_2P7_COMPONENT_ORDER_V0_1'
    assert namaster['verified_component_order']['spin0_x_spin2'] == ['TE', 'TB']
    assert namaster['verified_component_order']['spin2_x_spin2'] == ['EE', 'EB', 'BE', 'BB']

    for i, item in enumerate(source):
        assert item['status'] == 'PASS_EXP073S_DESY1_SOURCE_COUNTMASK_RECONSTRUCTION_V0_1'
        assert item['source_bin'] == i
        assert item['binary_occupancy_reproduction']['matches_r1_summary'] is True
        assert item['physical_support_evaluated'] is False
        assert item['science_gate_scored'] is False
        assert item['f_invalid_computed'] is False
        assert item['authority']['r1_run_id'] == 33270843577
        assert item['authority']['r1_job_id'] == 99148916507
        assert item['authority']['r1_head_sha'] == 'ef783ca941fb9b9b5f5eae537986c56ff06e6536'

    boss: list[str] = []
    for cap in ('NGC', 'SGC'):
        for ell, lo, hi in (('P0', 0, 40), ('P2', 80, 120), ('P4', 160, 200)):
            boss.extend(f'BOSS|{cap}|{ell}|matrix_row={row:03d}' for row in range(lo, hi))
    assert len(boss) == 240 and len(set(boss)) == 240

    # Prospective block concatenation: preserve the already-frozen DES Wm->WW
    # order exactly, then append the previously frozen BOSS finite-matrix order.
    ids = wm + ww + boss
    assert len(ids) == 1410 and len(set(ids)) == 1410

    result = {
        'experiment': 'Exp073U',
        'status': PASS,
        'record_type': 'ARTICLE3_PRESUPPORT_COORDINATE_SKELETON_NONCLASSIFYING',
        'coordinate_order': ['Wm', 'WW', 'BOSS'],
        'candidate_count': 1410,
        'blocks': {
            'Wm': {'offset': [0, 780], 'count': 780, 'component': 'TE', 'component_index': 0, 'ordered_id_sha256': order_sha256(wm)},
            'WW': {'offset': [780, 1170], 'count': 390, 'component': 'EE', 'component_index': 0, 'ordered_id_sha256': order_sha256(ww)},
            'BOSS': {
                'offset': [1170, 1410],
                'count': 240,
                'order': 'NGC P0 rows 0:39; NGC P2 rows 80:119; NGC P4 rows 160:199; SGC same',
                'ordered_id_sha256': order_sha256(boss),
            },
        },
        'ordered_coordinate_ids': ids,
        'ordered_coordinate_id_sha256': order_sha256(ids),
        'source_bin_countmask_fingerprints': {
            str(i): source[i]['sparse_count_map_fingerprint']['sha256'] for i in range(4)
        },
        'authority': {
            'hosted_receipt': {
                'run_id': 33271876425,
                'job_id': 99151650192,
                'artifact_id': 9720339539,
                'artifact_digest': 'sha256:dc63797a8bfe12a91c264eb5204182164e15d9f6441886ef79ab25f55b3040fc',
            },
            'r1': {
                'run_id': 33270843577,
                'job_id': 99148916507,
                'head_sha': 'ef783ca941fb9b9b5f5eae537986c56ff06e6536',
                'artifact_id': 9720335366,
                'artifact_digest': 'sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd',
            },
            'exp073s_run_id': 33272641756,
            'exp073t_run_id': 33272691162,
            'exp073s_internal_r1_artifact_id_digest_are_legacy_non_authoritative': True,
        },
        'science_boundary': {
            'full_finite_operator_built': False,
            'z_k_bound': False,
            'final_response_abs_values_bound': False,
            'physical_support_evaluated': False,
            'science_gate_scored': False,
            'f_invalid_computed': False,
            'covariance_read': False,
            'nuisance_geometry_read': False,
            'relation_null_read': False,
            'G8_read': False,
            'gate_state': GATES,
            'readiness_credit_authorized': False,
        },
        'next_required_block': 'bind full real finite-operator support representation for Layer A; this skeleton alone does not close the 55-57% manifest milestone',
    }

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(PASS, result['ordered_coordinate_id_sha256'], result['blocks']['BOSS']['ordered_id_sha256'])


if __name__ == '__main__':
    main()
