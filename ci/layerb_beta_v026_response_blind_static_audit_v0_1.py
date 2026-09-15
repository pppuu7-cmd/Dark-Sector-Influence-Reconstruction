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
MIXED_DIGEST = '59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85'
DIRECT_DIGEST = '1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864'
KMIN = 1e-4
KMAX = 0.06664762008318016
TARGET_MIN = 0.00033800000000000003
TARGET_MAX = 0.06664596609379447
CAPACITY = 1152
PARSER_CAPACITY = 32768
COMMON_N = 896
EXPECTED_SENTINEL = {
    'M076': {'calls': [76, 78], 'targets': 255, 'direct': 'D50', 'direct_targets': 1146},
    'M298': {'calls': [375], 'targets': 244, 'direct': 'D00', 'direct_targets': 1152},
    'M300': {'calls': list(range(377, 441)), 'targets': 99, 'direct': 'D58', 'direct_targets': 99},
}


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canonical_bytes(x) -> bytes:
    return json.dumps(x, sort_keys=True, separators=(',', ':')).encode('utf-8')


def u64hex_to_f64(h: str) -> float:
    return struct.unpack('>d', bytes.fromhex(h))[0]


def f64_to_u64hex(x: float) -> str:
    return struct.pack('>d', float(x)).hex()


def guarded_lattice(n: int):
    base = np.geomspace(KMIN, KMAX, n, dtype=np.float64)
    r = np.float64(base[1] / base[0])
    nlo = nhi = 0

    def make(lo, hi):
        lower = np.asarray([np.float64(base[0] / (r ** m)) for m in range(lo, 0, -1)], dtype=np.float64)
        upper = np.asarray([np.float64(base[-1] * (r ** m)) for m in range(1, hi + 1)], dtype=np.float64)
        return np.concatenate((lower, base, upper))

    def valid(nodes, k):
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
    return nodes, nlo, nhi


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


def payload_bytes(values) -> int:
    return len(','.join(format(float(x), '.17g') for x in values).encode('utf-8')) + 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--plan', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    raw = Path(a.plan).read_bytes()
    if len(raw) != PLAN_BYTES or sha256_bytes(raw) != PLAN_SHA256:
        raise RuntimeError('source plan byte identity mismatch')
    plan = json.loads(raw)
    if plan['coarse_calls_digest'] != COARSE_CALLS_DIGEST or plan['fine_calls_digest'] != FINE_CALLS_DIGEST:
        raise RuntimeError('source plan embedded digest mismatch')
    coarse, fine = plan['coarse_calls'], plan['fine_calls']
    if len(coarse) != 441 or len(fine) != 569 or coarse != fine[:441]:
        raise RuntimeError('call-count or 441-prefix identity mismatch')

    des = coarse[:377]
    boss = coarse[377:]
    des_sets = [uniq_targets(c) for c in des]
    boss_sets = [uniq_targets(c) for c in boss]
    if sum(len(s) for s in des_sets) != 64658:
        raise RuntimeError('DES unique-target scalar count mismatch')
    if len(set().union(*(set(s) for s in des_sets))) != 64658:
        raise RuntimeError('DES cross-call target overlap detected')
    if (min(map(len, des_sets)), max(map(len, des_sets))) != (90, 244):
        raise RuntimeError('DES per-call target range mismatch')
    if len(boss_sets) != 64 or len(boss_sets[0]) != 99 or not all(s == boss_sets[0] for s in boss_sets):
        raise RuntimeError('BOSS GL64 target-set identity mismatch')
    if not all(uniq_targets(c) == boss_sets[0] for c in fine[441:]):
        raise RuntimeError('BOSS GL128 target-set identity mismatch')
    if set().union(*(set(s) for s in des_sets)) & set(boss_sets[0]):
        raise RuntimeError('unexpected DES/BOSS target overlap')

    common, nlo, nhi = guarded_lattice(COMMON_N)
    if (nlo, nhi, len(common)) != (0, 1, 897):
        raise RuntimeError('GRID896 guard identity mismatch')
    grid_hex = {f64_to_u64hex(x) for x in common}
    all_target_hex = set().union(*(set(s) for s in des_sets), set(boss_sets[0]))
    if grid_hex & all_target_hex:
        raise RuntimeError('exact target already equals GRID896 node')

    mixed = mixed_plan(des_sets, boss_sets[0])
    direct = direct_plan(des_sets, boss_sets[0])
    if len(mixed) != 301 or len(direct) != 59:
        raise RuntimeError('batch-count mismatch')
    if sha256_bytes(canonical_bytes(mixed)) != MIXED_DIGEST:
        raise RuntimeError('mixed canonical digest mismatch')
    if sha256_bytes(canonical_bytes(direct)) != DIRECT_DIGEST:
        raise RuntimeError('direct canonical digest mismatch')

    pairs = sum(len(x['call_indices']) == 2 for x in mixed[:300])
    singles = sum(len(x['call_indices']) == 1 for x in mixed[:300])
    if (pairs, singles) != (77, 223):
        raise RuntimeError('mixed pair/singleton arithmetic mismatch')

    max_mixed_payload = (0, None)
    for b in mixed:
        ts = [u64hex_to_f64(h) for h in b['target_u64hex']]
        vals = sorted(set(map(float, common)).union(ts))
        if len(vals) > CAPACITY:
            raise RuntimeError(f'mixed capacity exceeded {b["batch_id"]}')
        q = payload_bytes(vals)
        max_mixed_payload = max(max_mixed_payload, (q, b['batch_id']))
        if q >= PARSER_CAPACITY:
            raise RuntimeError(f'mixed parser capacity exceeded {b["batch_id"]}')

    max_direct_payload = (0, None)
    for b in direct:
        vals = [u64hex_to_f64(h) for h in b['target_u64hex']]
        if len(vals) > CAPACITY:
            raise RuntimeError(f'direct capacity exceeded {b["batch_id"]}')
        q = payload_bytes(vals)
        max_direct_payload = max(max_direct_payload, (q, b['batch_id']))
        if q >= PARSER_CAPACITY:
            raise RuntimeError(f'direct parser capacity exceeded {b["batch_id"]}')

    by_m = {b['batch_id']: b for b in mixed}
    by_d = {b['batch_id']: b for b in direct}
    for mid, e in EXPECTED_SENTINEL.items():
        m = by_m[mid]
        d = by_d[e['direct']]
        if m['call_indices'] != e['calls'] or len(m['target_u64hex']) != e['targets'] or len(d['target_u64hex']) != e['direct_targets']:
            raise RuntimeError(f'sentinel identity mismatch {mid}')

    mixed_shards = [0] * 16
    for b in mixed:
        mixed_shards[int(b['batch_id'][1:]) % 16] += 1
    direct_shards = [0] * 4
    for b in direct:
        direct_shards[int(b['batch_id'][1:]) % 4] += 1

    out = {
        'schema': 'LAYERB_BETA_V0_26_RESPONSE_BLIND_STATIC_AUDIT_V0_1',
        'source_plan_sha256': PLAN_SHA256,
        'source_plan_bytes': PLAN_BYTES,
        'coarse_calls_digest': COARSE_CALLS_DIGEST,
        'fine_calls_digest': FINE_CALLS_DIGEST,
        'fine_prefix_441_bitwise_identical': True,
        'des': {'calls': 377, 'unique_targets': 64658, 'cross_call_overlap': 0, 'per_call_min': 90, 'per_call_max': 244},
        'boss': {'gl64_calls': 64, 'gl128_fine_only_calls': 128, 'shared_unique_targets': 99},
        'grid896': {'lower_guard_count': nlo, 'upper_guard_count': nhi, 'common_nodes': len(common), 'exact_target_overlap': 0},
        'mixed': {
            'batch_count': len(mixed), 'des_pairs': pairs, 'des_singletons': singles,
            'canonical_sha256': MIXED_DIGEST,
            'max_payload_bytes': max_mixed_payload[0], 'max_payload_batch_id': max_mixed_payload[1],
            'shard_batch_counts': mixed_shards,
        },
        'direct': {
            'batch_count': len(direct), 'canonical_sha256': DIRECT_DIGEST,
            'max_payload_bytes': max_direct_payload[0], 'max_payload_batch_id': max_direct_payload[1],
            'shard_batch_counts': direct_shards,
        },
        'sentinel': EXPECTED_SENTINEL,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'token': 'PASS_LAYERB_BETA_V0_26_RESPONSE_BLIND_STATIC_AUDIT',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
