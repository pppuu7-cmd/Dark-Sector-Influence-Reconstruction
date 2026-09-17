#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import struct
import subprocess
import sys

KMIN = 1e-4
KMAX = 0.06664762008318016
TARGET_MIN = 0.00033800000000000003
TARGET_MAX = 0.06664596609379447
GRID_N = 896
EXPECTED_NUMPY = '1.26.4'
EXPECTED_GRID_SHA256 = '8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d'
NUMPY_DISABLE = 'AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX'


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def f64hex(x: float) -> str:
    return struct.pack('>d', float(x)).hex()


def child() -> dict:
    import numpy as np
    if np.__version__ != EXPECTED_NUMPY:
        raise RuntimeError(f'NumPy mismatch {np.__version__} != {EXPECTED_NUMPY}')
    base = np.geomspace(KMIN, KMAX, GRID_N, dtype=np.float64)
    ratio = np.float64(base[1] / base[0])
    nlo = nhi = 0

    def make(lo: int, hi: int):
        lower = np.asarray([np.float64(base[0] / (ratio ** m)) for m in range(lo, 0, -1)], dtype=np.float64)
        upper = np.asarray([np.float64(base[-1] * (ratio ** m)) for m in range(1, hi + 1)], dtype=np.float64)
        return np.concatenate((lower, base, upper))

    def valid(nodes, k: float) -> bool:
        j = int(np.searchsorted(nodes, np.float64(k)))
        return bool(k > 0.0 and j >= 2 and j <= len(nodes) - 2)

    nodes = make(0, 0)
    while not valid(nodes, TARGET_MIN):
        nlo += 1
        nodes = make(nlo, nhi)
    while not valid(nodes, TARGET_MAX):
        nhi += 1
        nodes = make(nlo, nhi)
    nodes = np.asarray(nodes, dtype=np.float64)
    raw = np.ascontiguousarray(nodes, dtype='<f8').tobytes()
    features = getattr(np.core._multiarray_umath, '__cpu_features__', {})
    return {
        'numpy_version': np.__version__,
        'npy_disable_cpu_features': os.environ.get('NPY_DISABLE_CPU_FEATURES'),
        'grid_sha256': sha256_bytes(raw),
        'expected_grid_sha256': EXPECTED_GRID_SHA256,
        'matches_frozen_grid': sha256_bytes(raw) == EXPECTED_GRID_SHA256,
        'ratio_u64hex': f64hex(ratio),
        'lower_guard_count': nlo,
        'upper_guard_count': nhi,
        'node_count': len(nodes),
        'node_u64hex': [f64hex(x) for x in nodes],
        'active_cpu_features': sorted(k for k, v in features.items() if v),
    }


def run_child(env: dict[str, str]) -> dict:
    p = subprocess.run([sys.executable, __file__, '--child'], env=env, check=True, text=True, capture_output=True)
    return json.loads(p.stdout)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--child', action='store_true')
    ap.add_argument('--out')
    a = ap.parse_args()
    if a.child:
        print(json.dumps(child(), sort_keys=True))
        return 0
    if not a.out:
        raise SystemExit('--out required')

    native_env = os.environ.copy()
    native_env.pop('NPY_DISABLE_CPU_FEATURES', None)
    forced_env = native_env.copy()
    forced_env['NPY_DISABLE_CPU_FEATURES'] = NUMPY_DISABLE
    native = run_child(native_env)
    forced = run_child(forced_env)

    diffs = []
    for i, (x, y) in enumerate(zip(native['node_u64hex'], forced['node_u64hex'])):
        if x != y:
            diffs.append({'index': i, 'native_u64hex': x, 'forced_u64hex': y})
    same_geometry = (
        native['node_count'], native['lower_guard_count'], native['upper_guard_count']
    ) == (
        forced['node_count'], forced['lower_guard_count'], forced['upper_guard_count']
    ) == (897, 0, 1)

    if native['matches_frozen_grid'] and not forced['matches_frozen_grid']:
        classification = 'GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED'
    elif native['matches_frozen_grid'] and forced['matches_frozen_grid']:
        classification = 'GRID896_DISPATCH_HYPOTHESIS_REJECTED_BOTH_MATCH'
    elif (not native['matches_frozen_grid']) and (not forced['matches_frozen_grid']):
        classification = 'GRID896_HOST_RUNTIME_IDENTITY_DRIFT_OR_OTHER_CONSTRUCTION_CAUSE'
    else:
        classification = 'GRID896_FORCED_ONLY_MATCHES_FROZEN_UNEXPECTED'

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_GRID896_DISPATCH_DIAGNOSTIC_RESULT_V0_1',
        'classification': classification,
        'effect': '+0/+0',
        'science': False,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'same_geometry': same_geometry,
        'native_grid_sha256': native['grid_sha256'],
        'forced_grid_sha256': forced['grid_sha256'],
        'frozen_grid_sha256': EXPECTED_GRID_SHA256,
        'native_matches_frozen_grid': native['matches_frozen_grid'],
        'forced_matches_frozen_grid': forced['matches_frozen_grid'],
        'native_ratio_u64hex': native['ratio_u64hex'],
        'forced_ratio_u64hex': forced['ratio_u64hex'],
        'differing_node_count': len(diffs),
        'first_differences': diffs[:16],
        'native_active_cpu_features': native['active_cpu_features'],
        'forced_active_cpu_features': forced['active_cpu_features'],
        'npy_disable_cpu_features_forced': NUMPY_DISABLE,
        'successor_run_35174721773_must_not_be_rerun': True,
        'new_science_experiment_authorized': False,
        'full_107_row_execution_authorized': False,
        'token': 'TERMINAL_LAYERB_BETA_V0_26_R1_GRID896_DISPATCH_DIAGNOSTIC_PLUS_0_PLUS_0',
    }
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write('\n')
    print(out['classification'])
    print(out['token'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
