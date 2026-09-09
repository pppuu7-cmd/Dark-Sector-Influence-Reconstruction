#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np

EXPECTED_A_SHA = '963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd'
EXPECTED_K_SHA = 'c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795'
EXPECTED_W_SHA = '96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087'
EXPECTED_SHAPE = (39, 12288)
FIXED_CORE = 'Nehalem'
PASS = 'PASS_EXP073IO_C2_WM_S2_EXACT_BYTE_MATERIALIZATION_V0_1'
EDGES = np.array([
    0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,
    750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,
    3914,4444,5047,5731,6508,7390,8392,9529,10821,12288
], dtype=np.int64)


def canon(x: np.ndarray) -> np.ndarray:
    return np.ascontiguousarray(np.asarray(x, dtype='<f8'))


def ahash(x: np.ndarray) -> str:
    return hashlib.sha256(canon(x).tobytes()).hexdigest()


def k_from_a(A: np.ndarray) -> np.ndarray:
    nb = len(EDGES) - 1
    K = np.empty((nb, nb), dtype=np.float64)
    for ib, (lo, hi) in enumerate(zip(EDGES[:-1], EDGES[1:])):
        acc = np.zeros(nb, dtype=np.float64)
        for ell in range(int(lo), int(hi)):
            acc += A[:, ell]
        K[:, ib] = acc
    return canon(K)


def find_compact(root: Path) -> Path:
    hits = list(root.rglob('*compact_a_v0_1.npz'))
    if len(hits) != 1:
        hits = list(root.rglob('*.npz'))
    if len(hits) != 1:
        raise AssertionError(('compact_npz_hits', [str(x) for x in hits]))
    return hits[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--compact-root', required=True)
    ap.add_argument('--out-npy', required=True)
    ap.add_argument('--out-json', required=True)
    args = ap.parse_args()

    if os.environ.get('OPENBLAS_CORETYPE') != FIXED_CORE:
        raise AssertionError(('OPENBLAS_CORETYPE', os.environ.get('OPENBLAS_CORETYPE')))
    if np.__version__ != '2.1.3':
        raise AssertionError(('numpy_version', np.__version__))

    p = find_compact(Path(args.compact_root))
    with np.load(p, allow_pickle=False) as z:
        if 'A' not in z.files:
            raise AssertionError(('missing_A', z.files))
        A = canon(z['A'])
    if A.shape != EXPECTED_SHAPE or not np.isfinite(A).all():
        raise AssertionError(('A_shape_or_finite', A.shape))
    a_sha = ahash(A)
    if a_sha != EXPECTED_A_SHA:
        raise AssertionError(('A_sha', a_sha, EXPECTED_A_SHA))

    K = k_from_a(A)
    k_sha = ahash(K)
    if k_sha != EXPECTED_K_SHA:
        raise AssertionError(('K_sha', k_sha, EXPECTED_K_SHA))

    W = canon(np.linalg.solve(K, A))
    if W.shape != EXPECTED_SHAPE or not np.isfinite(W).all():
        raise AssertionError(('W_shape_or_finite', W.shape))
    w_sha = ahash(W)
    if w_sha != EXPECTED_W_SHA:
        raise AssertionError(('W_sha', w_sha, EXPECTED_W_SHA))

    out_npy = Path(args.out_npy)
    out_npy.parent.mkdir(parents=True, exist_ok=True)
    np.save(out_npy, W, allow_pickle=False)

    rec = {
        'experiment': 'Exp073IO',
        'status': PASS,
        'classification': 'EXACT_MATERIALIZATION_OF_PREEXISTING_EXP073CI_AUTHORITY',
        'source_lane_rule': 'LEXICAL_A_BEFORE_B',
        'source_artifact_id': 9841348367,
        'source_artifact_digest': 'sha256:d6703819745b22eadc9c6557c4d89d926ed9675c09bd41cb19e79d4050ef399b',
        'numpy_version': np.__version__,
        'openblas_coretype': os.environ.get('OPENBLAS_CORETYPE'),
        'openblas_num_threads': os.environ.get('OPENBLAS_NUM_THREADS'),
        'A': {'dtype': A.dtype.str, 'shape': list(A.shape), 'sha256': a_sha},
        'K': {'dtype': K.dtype.str, 'shape': list(K.shape), 'sha256': k_sha},
        'W': {'dtype': W.dtype.str, 'shape': list(W.shape), 'sha256': w_sha},
        'no_tolerance_used': True,
        'new_scientific_authority_created': False,
        'radial_support_scored': False,
        'downstream_reads': [],
    }
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': PASS, 'A': a_sha, 'K': k_sha, 'W': w_sha}, sort_keys=True))


if __name__ == '__main__':
    main()
