#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

import numpy as np

EXPECTED_SCHEMA = 'LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_CONTRACT_V0_26_R1'
EXPECTED_NUMPY = '1.26.4'
KMIN = 1e-4
KMAX = 0.06664762008318016
TARGET_MIN = 0.00033800000000000003
TARGET_MAX = 0.06664596609379447


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git_blob_sha1(b: bytes) -> str:
    h = hashlib.sha1()
    h.update(f'blob {len(b)}\0'.encode('ascii'))
    h.update(b)
    return h.hexdigest()


def canonical_sha(x) -> str:
    return sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode('utf-8'))


def uhex(x: float) -> str:
    return struct.pack('>d', float(x)).hex()


def f64(h: str) -> float:
    return struct.unpack('>d', bytes.fromhex(h))[0]


def read_bytes(path: str) -> bytes:
    return Path(path).read_bytes()


def read_json(path: str):
    return json.loads(Path(path).read_text())


def assert_blob(path: str, expected: str) -> None:
    got = git_blob_sha1(read_bytes(path))
    if got != expected:
        raise AssertionError(f'git blob mismatch {path}: {got} != {expected}')


def parse_kv(path: str):
    out = {}
    for raw in Path(path).read_text().splitlines():
        s = raw.strip()
        if not s or s.startswith('#') or '=' not in s:
            continue
        k, v = s.split('=', 1)
        k = k.strip()
        v = v.split('#', 1)[0].strip()
        if k and v:
            out[k] = v
    return out


def unique_targets(call):
    return tuple(sorted(set(call['targets_u64hex'])))


def build_grid896():
    base = np.geomspace(KMIN, KMAX, 896, dtype=np.float64)
    ratio = np.float64(base[1] / base[0])
    nlo = nhi = 0

    def make(lo, hi):
        lower = np.asarray([np.float64(base[0] / (ratio ** m)) for m in range(lo, 0, -1)], dtype=np.float64)
        upper = np.asarray([np.float64(base[-1] * (ratio ** m)) for m in range(1, hi + 1)], dtype=np.float64)
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
    return np.asarray(nodes, dtype=np.float64), ratio, nlo, nhi


def build_mixed(des_sets, boss_set):
    ordered = sorted((len(s), i) for i, s in enumerate(des_sets))
    lo, hi = 0, len(ordered) - 1
    raw = []
    while lo <= hi:
        if lo == hi:
            raw.append((ordered[hi][1],))
            break
        small_count, small_i = ordered[lo]
        large_count, large_i = ordered[hi]
        if small_count + large_count <= 255:
            raw.append(tuple(sorted((small_i, large_i))))
            lo += 1
            hi -= 1
        else:
            raw.append((large_i,))
            hi -= 1
    des_batches = sorted(raw, key=lambda xs: (min(xs), xs))
    result = []
    for bid, calls in enumerate(des_batches):
        target = sorted(set().union(*(set(des_sets[i]) for i in calls)))
        result.append({'batch_id': f'M{bid:03d}', 'domain': 'DES', 'call_indices': list(calls), 'target_u64hex': target})
    result.append({'batch_id': 'M300', 'domain': 'BOSS', 'call_indices': list(range(377, 441)), 'target_u64hex': list(boss_set)})
    return result


def build_direct(des_sets, boss_set):
    bins = []
    for i in sorted(range(377), key=lambda q: (-len(des_sets[q]), q)):
        cur = set(des_sets[i])
        for b in bins:
            union = b['targets'] | cur
            if len(union) <= 1152:
                b['calls'].append(i)
                b['targets'] = union
                break
        else:
            bins.append({'calls': [i], 'targets': cur})
    result = []
    for bid, b in enumerate(bins):
        result.append({'batch_id': f'D{bid:02d}', 'domain': 'DES', 'call_indices': sorted(b['calls']), 'target_u64hex': sorted(b['targets'])})
    result.append({'batch_id': f'D{len(result):02d}', 'domain': 'BOSS', 'call_indices': list(range(377, 441)), 'target_u64hex': list(boss_set)})
    return result


def payload_record(batch_id, values):
    vals = [float(x) for x in values]
    ascii_payload = ','.join(format(x, '.17g') for x in vals).encode('ascii')
    words = [uhex(x) for x in vals]
    return {
        'batch_id': batch_id,
        'node_count': len(vals),
        'c_string_payload_bytes': len(ascii_payload) + 1,
        'ascii_without_nul_sha256': sha256(ascii_payload),
        'node_u64hex_lines_sha256': sha256(('\n'.join(words) + '\n').encode('ascii')),
    }


def main():
    ap = argparse.ArgumentParser()
    for name in ('contract','prereg','plan','parent','qualification','exp073ir','jj','baseline','precision','localization','alpha-resource','alpha-partition','request-authority','out'):
        ap.add_argument('--' + name, required=True)
    a = ap.parse_args()

    if np.__version__ != EXPECTED_NUMPY:
        raise AssertionError(f'NumPy mismatch {np.__version__} != {EXPECTED_NUMPY}')

    C = read_json(a.contract)
    if C['schema'] != EXPECTED_SCHEMA:
        raise AssertionError('contract schema mismatch')
    if C['status'] != 'PROSPECTIVELY_FROZEN_R1_CANDIDATE_NOT_EXECUTABLE_PENDING_INDEPENDENT_AUDIT':
        raise AssertionError('contract status mismatch')
    if C['scope'] != 'DSIR_F1_NUMERICAL_REPRODUCIBILITY_ONLY' or C['effect'] != '+0/+0':
        raise AssertionError('scope/effect drift')

    # Immutable repository bindings.
    assert_blob(a.prereg, C['preregistration']['git_blob_sha1'])
    assert_blob(a.parent, C['terminal_parent']['git_blob_sha1'])
    assert_blob(a.qualification, C['split_candidate_qualification']['git_blob_sha1'])
    assert_blob(a.exp073ir, C['source_bindings']['exp073ir_semantic_parent']['git_blob_sha1'])
    assert_blob(a.jj, C['source_bindings']['jj_common_grid_source']['git_blob_sha1'])
    assert_blob(a.baseline, C['source_bindings']['baseline']['git_blob_sha1'])
    assert_blob(a.precision, C['source_bindings']['precision']['git_blob_sha1'])
    assert_blob(a.localization, C['alpha_route']['localization_authority_git_blob_sha1'])
    assert_blob(a.alpha_resource, C['alpha_route']['resource_authority_git_blob_sha1'])
    assert_blob(a.alpha_partition, C['alpha_route']['partition_invariance_authority_git_blob_sha1'])
    assert_blob(a.request_authority, C['response_blind_plan']['authority_git_blob_sha1'])

    P = read_json(a.parent)
    Q = read_json(a.qualification)
    L = read_json(a.localization)
    AR = read_json(a.alpha_resource)
    AP = read_json(a.alpha_partition)
    RA = read_json(a.request_authority)

    if P.get('corrected_authorized_next_stage') != C['terminal_parent']['authorized_next_stage']:
        raise AssertionError('parent authorization mismatch')
    if P.get('successor_execution_status') != 'NOT_OPEN_UNTIL_SEPARATE_PROSPECTIVE_PREREGISTRATION_AND_FROZEN_CONTRACT':
        raise AssertionError('unexpected parent execution state')
    if Q.get('verdict') != 'QUALIFIED' or not Q.get('required_correction_before_promotion', {}).get('independent_r1_contract_audit_required_before_sentinel_executor_or_workflow'):
        raise AssertionError('qualification authority mismatch')
    if C['authorization_state']['execution_open'] or C['authorization_state']['sentinel_executor_authorized'] or C['authorization_state']['sentinel_workflow_authorized'] or C['authorization_state']['sentinel_science_execution_authorized'] or C['authorization_state']['full_107_row_execution_authorized']:
        raise AssertionError('execution opened prematurely')

    # Denominator / authority identities.
    D = C['row_denominator']
    if (D['retained_count'], D['des_count'], D['boss_count']) != (107, 53, 54):
        raise AssertionError('denominator counts mismatch')
    if D['retained_id_sha256'] != '44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7' or D['full_order_sha256'] != 'bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75':
        raise AssertionError('denominator hash mismatch')
    if RA.get('classification') != 'RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0':
        raise AssertionError('request-plan authority mismatch')

    # Route-specific tolerance identities.
    precision = parse_kv(a.precision)
    if precision.get('tol_perturb_integration') != '3e-10':
        raise AssertionError('precision alpha tolerance source mismatch')
    if float(precision.get('perturb_sampling_stepsize')) != 0.00035:
        raise AssertionError('sampling mismatch')
    FS = C['frozen_science']
    if FS['alpha_tol_perturb_integration'] != '3e-10' or FS['beta_tol_perturb_integration'] != '1e-12':
        raise AssertionError('route-specific tolerance mismatch')
    if C['alpha_route']['tol_perturb_integration'] != '3e-10' or C['beta_route']['tol_perturb_integration'] != '1e-12':
        raise AssertionError('route-level tolerance mismatch')

    # Alpha route authorities and exact method identity.
    if abs(L['max_by_component']['abs_dDelta_m_dalpha_left']['relative_difference'] - 0.0006776803529834111) > 0.0:
        raise AssertionError('alpha localization mismatch')
    if abs(L['max_by_component']['abs_dDelta_m_dbeta_symmetric']['relative_difference'] - 0.007384797439715474) > 0.0:
        raise AssertionError('beta localization mismatch')
    if AR['classification'] != 'LAYERB_32769_EIGHT_CHUNK_RESPONSE_BLIND_RESOURCE_ALL_PASS_PLUS_0_PLUS_0':
        raise AssertionError('alpha resource authority classification mismatch')
    if AP['classification'] != 'LAYERB_32769_BLINDED_PARTITION_INVARIANCE_ALL_ROLES_PASS_PLUS_0_PLUS_0':
        raise AssertionError('alpha partition authority classification mismatch')
    if AP['acceptance_evidence']['max_normalized_response_difference'] != 0.0 or AP['acceptance_evidence']['minimum_exact_binary64_fraction'] != 1.0:
        raise AssertionError('partition invariance evidence mismatch')
    A = C['alpha_route']
    if A['canonical_node_payload_sha256'] != '82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599' or A['canonical_text_sha256'] != '7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2':
        raise AssertionError('alpha canonical identity mismatch')
    expected_slices = [[0,4097],[4097,8193],[8193,12289],[12289,16385],[16385,20481],[20481,24577],[24577,28673],[28673,32769]]
    if A['partition_a_slices'] != expected_slices or A['model_constructions'] != 16 or not A['all_569_calls_required']:
        raise AssertionError('alpha route geometry/accounting mismatch')

    # Exact plan bytes and response-blind call geometry.
    raw_plan = read_bytes(a.plan)
    RP = C['response_blind_plan']
    if len(raw_plan) != RP['inner_byte_length'] or sha256(raw_plan) != RP['inner_sha256']:
        raise AssertionError('plan byte identity mismatch')
    plan = json.loads(raw_plan)
    if plan.get('coarse_calls_digest') != RP['coarse_calls_digest'] or plan.get('fine_calls_digest') != RP['fine_calls_digest']:
        raise AssertionError('plan digest mismatch')
    coarse = plan['coarse_calls']; fine = plan['fine_calls']
    if len(coarse) != 441 or len(fine) != 569 or coarse != fine[:441]:
        raise AssertionError('plan count/prefix mismatch')
    if sum(len(q['targets_u64hex']) for q in coarse) != 83666 or sum(len(q['targets_u64hex']) for q in fine) != 121682:
        raise AssertionError('plan scalar count mismatch')

    des_sets = [unique_targets(q) for q in coarse[:377]]
    boss_sets = [unique_targets(q) for q in coarse[377:441]]
    all_des = set()
    overlap = 0
    for s in des_sets:
        ss = set(s); overlap += len(all_des & ss); all_des |= ss
    if len(all_des) != 64658 or overlap != 0 or min(map(len, des_sets)) != 90 or max(map(len, des_sets)) != 244:
        raise AssertionError('DES target geometry mismatch')
    if len({tuple(s) for s in boss_sets}) != 1 or len(boss_sets[0]) != 99:
        raise AssertionError('BOSS target geometry mismatch')
    boss_set = boss_sets[0]
    if set(boss_set) & all_des:
        raise AssertionError('DES/BOSS target overlap')
    fine_boss = [unique_targets(q) for q in fine[441:]]
    if len(fine_boss) != 128 or any(tuple(s) != tuple(boss_set) for s in fine_boss):
        raise AssertionError('BOSS GL128 target identity mismatch')

    # Independently regenerate exact hosted NumPy-1.26.4 GRID896 identity.
    common, ratio, nlo, nhi = build_grid896()
    G = C['grid896']
    if (nlo, nhi, len(common)) != (0, 1, 897) or uhex(ratio) != G['ratio_u64hex']:
        raise AssertionError('GRID896 geometry/ratio mismatch')
    raw_common = np.ascontiguousarray(common, dtype='<f8').tobytes()
    common_words = [uhex(x) for x in common]
    common_lines = ('\n'.join(common_words) + '\n').encode('ascii')
    common_ascii = ','.join(format(float(x), '.17g') for x in common).encode('ascii')
    if len(raw_common) != G['node_payload_byte_length'] or sha256(raw_common) != G['node_payload_sha256']:
        raise AssertionError('GRID896 binary64 payload mismatch')
    if sha256(common_lines) != G['node_u64hex_lines_sha256']:
        raise AssertionError('GRID896 u64hex-lines mismatch')
    if len(common_ascii) != G['dot17g_ascii_without_nul_byte_length'] or sha256(common_ascii) != G['dot17g_ascii_without_nul_sha256']:
        raise AssertionError('GRID896 .17g ASCII mismatch')

    # Independently regenerate target packing and complete parser-payload manifests.
    mixed = build_mixed(des_sets, boss_set)
    direct = build_direct(des_sets, boss_set)
    PI = C['parser_payload_identity']
    if canonical_sha(mixed) != PI['mixed_target_plan_canonical_sha256']:
        raise AssertionError('mixed target-plan hash mismatch')
    if canonical_sha(direct) != PI['direct_target_plan_canonical_sha256']:
        raise AssertionError('direct target-plan hash mismatch')
    if len(mixed) != 301 or len(direct) != 59:
        raise AssertionError('batch count mismatch')
    pair_count = sum(1 for b in mixed[:-1] if len(b['call_indices']) == 2)
    singleton_count = sum(1 for b in mixed[:-1] if len(b['call_indices']) == 1)
    if (pair_count, singleton_count) != (77, 223):
        raise AssertionError('mixed pair/singleton count mismatch')

    mixed_records = []
    for b in mixed:
        targets = [f64(h) for h in b['target_u64hex']]
        vals = sorted(set(float(x) for x in common).union(targets))
        r = payload_record(b['batch_id'], vals)
        if r['node_count'] > 1152 or r['c_string_payload_bytes'] > 32768:
            raise AssertionError(f'mixed capacity failure {b["batch_id"]}')
        mixed_records.append(r)
    direct_records = []
    for b in direct:
        vals = [f64(h) for h in b['target_u64hex']]
        r = payload_record(b['batch_id'], vals)
        if r['node_count'] > 1152 or r['c_string_payload_bytes'] > 32768:
            raise AssertionError(f'direct capacity failure {b["batch_id"]}')
        direct_records.append(r)
    mm = max(mixed_records, key=lambda r: (r['c_string_payload_bytes'], r['batch_id']))
    dm = max(direct_records, key=lambda r: (r['c_string_payload_bytes'], r['batch_id']))
    if canonical_sha(mixed_records) != PI['mixed_payload_manifest_canonical_sha256'] or (mm['batch_id'], mm['c_string_payload_bytes']) != (PI['mixed_max_payload_batch_id'], PI['mixed_max_payload_bytes']):
        raise AssertionError('mixed payload manifest/max mismatch')
    if canonical_sha(direct_records) != PI['direct_payload_manifest_canonical_sha256'] or (dm['batch_id'], dm['c_string_payload_bytes']) != (PI['direct_max_payload_batch_id'], PI['direct_max_payload_bytes']):
        raise AssertionError('direct payload manifest/max mismatch')
    if PI['mixed_max_payload_bytes'] != 25063 or not PI['superseded_split_candidate_mixed_max_25062_is_r1_invalid']:
        raise AssertionError('superseded 25062 not eliminated')

    # Sentinel identities/comparator containment, but no authorization to execute.
    by_m = {b['batch_id']: b for b in mixed}; by_d = {b['batch_id']: b for b in direct}
    expected = [('M076','D50',[76,78]),('M298','D00',[375]),('M300','D58',list(range(377,441)))]
    for mid, did, calls in expected:
        if by_m[mid]['call_indices'] != calls:
            raise AssertionError(f'sentinel call identity mismatch {mid}')
        if not set(by_m[mid]['target_u64hex']).issubset(set(by_d[did]['target_u64hex'])):
            raise AssertionError(f'sentinel direct comparator not superset {mid}/{did}')
    if C['sentinel']['status'] != 'PREREGISTERED_NOT_AUTHORIZED_FOR_CONSTRUCTION_OR_EXECUTION':
        raise AssertionError('sentinel status drift')

    # Solver accounting / sharding / full-firewall checks.
    S = C['solver_accounting']
    if (S['alpha_canonical_32769'], S['beta_pure_grid896'], S['beta_mixed'], S['beta_direct'], S['total_class_constructions']) != (16,2,602,118,738):
        raise AssertionError('solver accounting mismatch')
    SH = C['full_run_sharding']
    mixed_counts = [sum(1 for b in mixed if int(b['batch_id'][1:]) % 16 == i) for i in range(16)]
    direct_counts = [sum(1 for b in direct if int(b['batch_id'][1:]) % 4 == i) for i in range(4)]
    if mixed_counts != SH['beta_mixed_expected_batch_counts'] or direct_counts != SH['beta_direct_expected_batch_counts']:
        raise AssertionError('shard geometry mismatch')
    F = C['forbidden']
    required_forbidden = ['response_informed_row_selection','response_informed_target_selection','post_response_batch_repacking','silent_science_retry','sentinel_executor_or_workflow_before_independent_r1_audit_authority','full_replay_before_sentinel_pass_and_separate_launch_authorization','read_covariance','read_whitening','read_nuisance','read_relation_null','open_Wm_S3','launch_global_65537','open_downstream_physical_science_gate']
    if not all(F.get(k) is True for k in required_forbidden):
        raise AssertionError('firewall missing')

    receipt = {
        'schema': 'LAYERB_BETA_V0_26_R1_CONTRACT_CODE_INPUT_PROVENANCE_AUDIT_RESULT_V0_1',
        'token': 'PASS_LAYERB_BETA_V0_26_R1_CONTRACT_AUDIT_PLUS_0_PLUS_0',
        'effect': '+0/+0',
        'numpy_version': np.__version__,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'contract_git_blob_sha1': git_blob_sha1(read_bytes(a.contract)),
        'prereg_git_blob_sha1': git_blob_sha1(read_bytes(a.prereg)),
        'source_plan_sha256': sha256(raw_plan),
        'grid896_node_payload_sha256': sha256(raw_common),
        'grid896_u64hex_lines_sha256': sha256(common_lines),
        'mixed_target_plan_sha256': canonical_sha(mixed),
        'mixed_payload_manifest_sha256': canonical_sha(mixed_records),
        'mixed_max_payload': {'batch_id': mm['batch_id'], 'bytes': mm['c_string_payload_bytes']},
        'direct_target_plan_sha256': canonical_sha(direct),
        'direct_payload_manifest_sha256': canonical_sha(direct_records),
        'direct_max_payload': {'batch_id': dm['batch_id'], 'bytes': dm['c_string_payload_bytes']},
        'des_unique_targets': len(all_des),
        'mixed_batches': len(mixed),
        'direct_batches': len(direct),
        'alpha_tol_perturb_integration': FS['alpha_tol_perturb_integration'],
        'beta_tol_perturb_integration': FS['beta_tol_perturb_integration'],
        'solver_constructions_full_replay': S['total_class_constructions'],
        'sentinel_execution_authorized': False,
        'full_107_row_execution_authorized': False,
        'next_action': 'INDEPENDENT_FUNNEL_REVIEW_OF_R1_AUDIT_BEFORE_SENTINEL_CONSTRUCTION',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(receipt['token'])


if __name__ == '__main__':
    main()
