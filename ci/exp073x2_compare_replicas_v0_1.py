#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

PASS = 'PASS_EXP073X2_DES_N4096_WM0_MASK_ONLY_REPEATABILITY_V0_1'
EXPECTED_GATES = {'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
EXPECTED_EDGES = [
    0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,
    852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,
    5047,5731,6508,7390,8392,9529,10821,12288
]
FIREWALL_FALSE = [
    'direct_signal_catalog_read_for_workspace', 'physical_support_evaluated',
    'science_gate_scored', 'retained_coordinates_evaluated',
    'fiducial_P_weighting_used', 'covariance_read', 'nuisance_geometry_read',
    'relation_null_read', 'G8_read', 'scientific_pass_claimed',
]


def one(root: Path, name: str) -> Path:
    hits = list(root.rglob(name))
    if len(hits) != 1:
        raise AssertionError(f'expected exactly one {name}, found {len(hits)}')
    return hits[0]


def canonical_hash(a: np.ndarray) -> str:
    x = np.ascontiguousarray(np.asarray(a, dtype=np.dtype('<f8')))
    return hashlib.sha256(x.tobytes(order='C')).hexdigest()


def load_replica(root: Path, label: str) -> tuple[dict, np.ndarray, Path, Path]:
    j = one(root, f'exp073x2_replica_{label.lower()}_v0_1.json')
    n = one(root, f'exp073x2_replica_{label.lower()}_v0_1.npz')
    d = json.loads(j.read_text(encoding='utf-8'))
    with np.load(n, allow_pickle=False) as z:
        if set(z.files) != {'wm0_te_window'}:
            raise AssertionError(f'replica {label} NPZ schema mismatch {z.files}')
        a = np.ascontiguousarray(z['wm0_te_window'], dtype='<f8')
    if d.get('experiment') != 'Exp073X2' or d.get('replica') != label:
        raise AssertionError(f'replica {label} identity mismatch')
    if d.get('status') != f'PASS_EXP073X2_REPLICA_{label}_DES_N4096_WM0_MASK_ONLY_V0_1':
        raise AssertionError(f'replica {label} did not complete')
    if d.get('nside') != 4096 or d.get('npix') != 201326592:
        raise AssertionError(f'replica {label} geometry mismatch')
    if d.get('ell_axis') != {'first':0,'last':12287,'count':12288}:
        raise AssertionError(f'replica {label} ell-axis mismatch')
    if d.get('bandpower_count') != 39 or d.get('bandpower_edges') != EXPECTED_EDGES:
        raise AssertionError(f'replica {label} bandpower mismatch')
    if d.get('component_order') != {'spin0_x_spin2':['TE','TB'],'selected_output':'TE','selected_input':'TE'}:
        raise AssertionError(f'replica {label} component mismatch')
    if d.get('gate_state') != EXPECTED_GATES or d.get('article3_scientific_readiness_percent') != 52:
        raise AssertionError(f'replica {label} gate/readiness mismatch')
    for k in FIREWALL_FALSE:
        if d.get(k) is not False:
            raise AssertionError(f'replica {label} firewall violation {k}')
    if a.shape != (39, 12288) or not np.all(np.isfinite(a)):
        raise AssertionError(f'replica {label} TE array invalid')
    meta = d.get('workspace',{}).get('te_window_authority',{})
    if meta.get('dtype') != '<f8' or meta.get('shape') != [39,12288]:
        raise AssertionError(f'replica {label} canonical metadata mismatch')
    if canonical_hash(a) != meta.get('sha256'):
        raise AssertionError(f'replica {label} NPZ/hash mismatch')
    return d, a, j, n


def exact_equal_metadata(a: dict, b: dict) -> None:
    keys = [
        'pymaster_version','nside','npix','ell_axis','bandpower_edges','bandpower_count',
        'component_order','r1_authority','source_mask','lens_mask','gate_state',
        'article3_scientific_readiness_percent',
    ]
    mismatched = [k for k in keys if a.get(k) != b.get(k)]
    if mismatched:
        raise AssertionError(f'replica frozen-metadata mismatch {mismatched}')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--replica-a-root', required=True)
    ap.add_argument('--replica-b-root', required=True)
    ap.add_argument('--output-json', required=True)
    args = ap.parse_args()

    da, a, ja, na = load_replica(Path(args.replica_a_root), 'A')
    db, b, jb, nb = load_replica(Path(args.replica_b_root), 'B')
    exact_equal_metadata(da, db)

    ha = canonical_hash(a)
    hb = canonical_hash(b)
    hashes_equal = ha == hb
    arrays_equal = np.array_equal(a, b)
    if not hashes_equal or not arrays_equal:
        raise AssertionError(f'Exp073X2 repeatability mismatch hashes_equal={hashes_equal} arrays_equal={arrays_equal}')

    out = {
        'experiment': 'Exp073X2',
        'status': PASS,
        'record_type': 'REAL_DES_N4096_MASK_ONLY_WM0_ANGULAR_OPERATOR_REPEATABILITY_AUTHORITY_NONCLASSIFYING',
        'replica_a_status': da['status'],
        'replica_b_status': db['status'],
        'canonical_te_window_sha256': ha,
        'te_window_shape': [39,12288],
        'repeatability': {'canonical_sha256_identical': True, 'array_equal': True},
        'frozen_metadata_identical': True,
        'gate_state': EXPECTED_GATES,
        'article3_scientific_readiness_percent': 52,
        'readiness_increment_from_x2': 0,
        'science_gate_scored': False,
        'scientific_pass_claimed': False,
        'physical_support_evaluated': False,
        'covariance_read': False,
        'G8_read': False,
        'exp073x_prior_record': 'INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE',
        'next_authorized_step': 'Expand exact nside4096 mask-only NaMaster angular windows to Wm source bins 1..3 and all ten WW source-mask pairs, then bind exact DES redshift kernels and freeze the complete finite candidate-operator manifest before Layer A.',
    }
    p = Path(args.output_json); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True, allow_nan=False)+'\n', encoding='utf-8')
    print(PASS)
    print('TE_WINDOW_SHA256', ha)


if __name__ == '__main__':
    main()
