#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

import numpy as np

PLAN_SHA256 = 'c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064'
PLAN_BYTES = 3953984
COARSE_CALLS_DIGEST = '9e829d5127457085f18d79901d4aa621a050ce8406ff30c4d7e157dd069b80b4'
FINE_CALLS_DIGEST = '9f5f85e92570b68576bae91f52163cb0c005a1e003bfc09b8ccc80b332f79b36'
MIXED_CANONICAL_SHA256 = '59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85'
DIRECT_CANONICAL_SHA256 = '1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864'
KMIN = 1e-4
KMAX = 0.06664762008318016
TARGET_MIN = 0.00033800000000000003
TARGET_MAX = 0.06664596609379447
GRID_N = 896
CAPACITY = 1152
PARSER_CAPACITY = 32768
EXPECTED_NUMPY = '1.26.4'


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canonical_hash(x) -> str:
    return sha256_bytes(json.dumps(x, sort_keys=True, separators=(',', ':')).encode('utf-8'))


def f64_to_u64hex(x: float) -> str:
    return struct.pack('>d', float(x)).hex()


def u64hex_to_f64(h: str) -> float:
    return struct.unpack('>d', bytes.fromhex(h))[0]


def guarded_lattice(n: int):
    base = np.geomspace(KMIN, KMAX, n, dtype=np.float64)
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
    if n + nlo + nhi > CAPACITY:
        raise RuntimeError('guarded lattice capacity exceeded')
    return np.asarray(nodes, dtype=np.float64), ratio, nlo, nhi


def uniq_targets(call):
    return tuple(sorted(set(call['targets_u64hex'])))


def mixed_plan(des_sets, boss_set):
    arr = sorted((len(s), i) for i, s in enumerate(des_sets))
    lo, hi = 0, len(arr) - 1
    raw = []
    while lo <= hi:
        if lo == hi:
            raw.append((arr[hi][1],))
            break
        cs, ismall = arr[lo]
        cb, ibig = arr[hi]
        if cs + cb <= 255:
            raw.append(tuple(sorted((ismall, ibig))))
            lo += 1
            hi -= 1
        else:
            raw.append((ibig,))
            hi -= 1
    des_batches = sorted(raw, key=lambda xs: (min(xs), xs))
    out = []
    for n, calls in enumerate(des_batches):
        targets = sorted(set().union(*(set(des_sets[i]) for i in calls)))
        out.append({'batch_id': f'M{n:03d}', 'domain': 'DES', 'call_indices': list(calls), 'target_u64hex': targets})
    out.append({'batch_id': 'M300', 'domain': 'BOSS', 'call_indices': list(range(377, 441)), 'target_u64hex': list(boss_set)})
    return out


def direct_plan(des_sets, boss_set):
    bins = []
    for i in sorted(range(len(des_sets)), key=lambda i: (-len(des_sets[i]), i)):
        s = set(des_sets[i])
        for b in bins:
            u = b['targets'] | s
            if len(u) <= CAPACITY:
                b['calls'].append(i)
                b['targets'] = u
                break
        else:
            bins.append({'calls': [i], 'targets': set(s)})
    out = []
    for n, b in enumerate(bins):
        out.append({'batch_id': f'D{n:02d}', 'domain': 'DES', 'call_indices': sorted(b['calls']), 'target_u64hex': sorted(b['targets'])})
    out.append({'batch_id': f'D{len(out):02d}', 'domain': 'BOSS', 'call_indices': list(range(377, 441)), 'target_u64hex': list(boss_set)})
    return out


def parser_payload_record(batch_id: str, values):
    vals = [float(x) for x in values]
    payload_ascii = ','.join(format(x, '.17g') for x in vals).encode('ascii')
    words = [f64_to_u64hex(x) for x in vals]
    word_bytes = ('\n'.join(words) + '\n').encode('ascii')
    return {
        'batch_id': batch_id,
        'node_count': len(vals),
        'c_string_payload_bytes': len(payload_ascii) + 1,
        'ascii_without_nul_sha256': sha256_bytes(payload_ascii),
        'node_u64hex_lines_sha256': sha256_bytes(word_bytes),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--plan', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    if np.__version__ != EXPECTED_NUMPY:
        raise RuntimeError(f'numpy identity mismatch: {np.__version__} != {EXPECTED_NUMPY}')

    raw = Path(args.plan).read_bytes()
    if len(raw) != PLAN_BYTES or sha256_bytes(raw) != PLAN_SHA256:
        raise RuntimeError('source plan byte identity mismatch')
    plan = json.loads(raw)
    if plan.get('coarse_calls_digest') != COARSE_CALLS_DIGEST or plan.get('fine_calls_digest') != FINE_CALLS_DIGEST:
        raise RuntimeError('source plan digest mismatch')
    coarse, fine = plan['coarse_calls'], plan['fine_calls']
    if len(coarse) != 441 or len(fine) != 569 or coarse != fine[:441]:
        raise RuntimeError('source plan shape/prefix mismatch')

    des_sets = [uniq_targets(c) for c in coarse[:377]]
    boss_sets = [uniq_targets(c) for c in coarse[377:441]]
    if len({x for s in boss_sets for x in [tuple(s)]}) != 1:
        raise RuntimeError('BOSS target-set identity mismatch')
    boss_set = boss_sets[0]

    mixed = mixed_plan(des_sets, boss_set)
    direct = direct_plan(des_sets, boss_set)
    if canonical_hash(mixed) != MIXED_CANONICAL_SHA256:
        raise RuntimeError('mixed target-plan canonical hash mismatch')
    if canonical_hash(direct) != DIRECT_CANONICAL_SHA256:
        raise RuntimeError('direct target-plan canonical hash mismatch')

    common, ratio, nlo, nhi = guarded_lattice(GRID_N)
    if (nlo, nhi, len(common)) != (0, 1, 897):
        raise RuntimeError('GRID896 guarded geometry mismatch')

    common_le = np.ascontiguousarray(common, dtype='<f8').tobytes()
    common_words = [f64_to_u64hex(x) for x in common]
    common_hex_lines = ('\n'.join(common_words) + '\n').encode('ascii')
    common_ascii = ','.join(format(float(x), '.17g') for x in common).encode('ascii')

    mixed_records = []
    for b in mixed:
        targets = [u64hex_to_f64(h) for h in b['target_u64hex']]
        vals = sorted(set(float(x) for x in common).union(targets))
        rec = parser_payload_record(b['batch_id'], vals)
        if rec['node_count'] > CAPACITY or rec['c_string_payload_bytes'] > PARSER_CAPACITY:
            raise RuntimeError(f'mixed capacity exceeded {b["batch_id"]}')
        mixed_records.append(rec)

    direct_records = []
    for b in direct:
        vals = [u64hex_to_f64(h) for h in b['target_u64hex']]
        rec = parser_payload_record(b['batch_id'], vals)
        if rec['node_count'] > CAPACITY or rec['c_string_payload_bytes'] > PARSER_CAPACITY:
            raise RuntimeError(f'direct capacity exceeded {b["batch_id"]}')
        direct_records.append(rec)

    max_mixed = max(mixed_records, key=lambda r: (r['c_string_payload_bytes'], r['batch_id']))
    max_direct = max(direct_records, key=lambda r: (r['c_string_payload_bytes'], r['batch_id']))

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_STATIC_IDENTITY_V0_1',
        'numpy_version': np.__version__,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'source_plan': {'byte_length': len(raw), 'sha256': sha256_bytes(raw)},
        'payload_byte_counting_convention': 'len(ASCII comma-separated Python format(x,.17g) k_output_values bytes) + 1 terminal NUL byte',
        'grid896': {
            'base_n': GRID_N,
            'lower_guard_count': nlo,
            'upper_guard_count': nhi,
            'common_node_count': len(common),
            'ratio_u64hex': f64_to_u64hex(ratio),
            'node_payload_format': 'contiguous little-endian IEEE-754 binary64 in ascending node order',
            'node_payload_byte_length': len(common_le),
            'node_payload_sha256': sha256_bytes(common_le),
            'node_u64hex_lines_sha256': sha256_bytes(common_hex_lines),
            'dot17g_ascii_without_nul_byte_length': len(common_ascii),
            'dot17g_ascii_without_nul_sha256': sha256_bytes(common_ascii),
        },
        'mixed': {
            'batch_count': len(mixed_records),
            'target_plan_canonical_sha256': canonical_hash(mixed),
            'payload_manifest_canonical_sha256': canonical_hash(mixed_records),
            'max_payload_batch_id': max_mixed['batch_id'],
            'max_payload_bytes': max_mixed['c_string_payload_bytes'],
            'records': mixed_records,
        },
        'direct': {
            'batch_count': len(direct_records),
            'target_plan_canonical_sha256': canonical_hash(direct),
            'payload_manifest_canonical_sha256': canonical_hash(direct_records),
            'max_payload_batch_id': max_direct['batch_id'],
            'max_payload_bytes': max_direct['c_string_payload_bytes'],
            'records': direct_records,
        },
        'token': 'PASS_LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_STATIC_IDENTITY',
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(out, indent=2, sort_keys=True) + '\n').encode('utf-8')
    Path(args.out).write_bytes(data)
    print(out['token'])
    print('GRID896', out['grid896']['node_payload_sha256'])
    print('MIXED', max_mixed['batch_id'], max_mixed['c_string_payload_bytes'], out['mixed']['payload_manifest_canonical_sha256'])
    print('DIRECT', max_direct['batch_id'], max_direct['c_string_payload_bytes'], out['direct']['payload_manifest_canonical_sha256'])


if __name__ == '__main__':
    main()
