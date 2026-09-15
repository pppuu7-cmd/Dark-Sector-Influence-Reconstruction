#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import struct
import subprocess
import sys
from pathlib import Path

R1_CONTRACT = 'docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json'
R1_CONTRACT_BLOB = 'b510d8e97baf1c0b7b216c0605d83cdd029254e9'
PROMOTION_AUTHORITY = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json'
PROMOTION_AUTHORITY_BLOB = 'cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'
STATIC_PROBE = 'ci/layerb_beta_v026_r1_static_identity_probe_v0_1.py'
V025 = 'ci/layerb_beta_forced_baseline_production_h_common_grid_interpolation_remedy_benchmark_v0_25.py'
V12 = 'ci/layerb_beta_production_h_common_grid_interpolation_v0_12.py'
JJ = 'ci/exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1.py'
CODEC = 'ci/layerb_chunk_call_codec_v0_1.py'
BASELINE = 'configs/dsir4/c2/ide0_reference_v0_1.ini'
PRECISION = 'configs/dsir4/c2/dsir_ide_p8_v0_1.pre'
NUMPY_DISABLE = 'AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX'
SENTINEL_BATCH_IDS = ('M076', 'M298', 'M300')
DIRECT_BY_MIXED = {'M076': 'D50', 'M298': 'D00', 'M300': 'D58'}
EXPECTED_SOLVERS = 14
EXPECTED_NUMPY = '1.26.4'
EXPECTED_SCIPY = '1.17.1'


def load(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot import {path}')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def git_blob(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canonical_hash(x) -> str:
    return sha256_bytes(json.dumps(x, sort_keys=True, separators=(',', ':')).encode())


def rel(a: float, b: float, np) -> float:
    return abs(a-b) / max(abs(a), abs(b), np.finfo(np.float64).tiny)


def clean_env():
    e = os.environ.copy()
    e.pop('NPY_DISABLE_CPU_FEATURES', None)
    e.pop('GLIBC_TUNABLES', None)
    return e


def forced_env():
    e = clean_env()
    e['NPY_DISABLE_CPU_FEATURES'] = NUMPY_DISABLE
    return e


def load_contract(path: str):
    c = json.loads(Path(path).read_text())
    if c.get('schema') != 'LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_CONTRACT_V0_26_R1':
        raise RuntimeError('R1 contract schema mismatch')
    if git_blob(path) != R1_CONTRACT_BLOB:
        raise RuntimeError('R1 contract blob mismatch')
    if git_blob(PROMOTION_AUTHORITY) != PROMOTION_AUTHORITY_BLOB:
        raise RuntimeError('R1 promotion authority blob mismatch')
    q = json.loads(Path(PROMOTION_AUTHORITY).read_text())
    if q.get('verdict') != 'QUALIFIED' or q.get('classification') != 'V0_26_R1_PROSPECTIVE_NUMERICAL_SPECIFICATION_QUALIFIED_FOR_PROMOTION':
        raise RuntimeError('R1 promotion authority invalid')
    if q.get('post_promotion_authorization', {}).get('sentinel_executor_construction_authorized_after_exact_r1_is_on_main') is not True:
        raise RuntimeError('sentinel construction not authorized')
    if q.get('sentinel_science_execution_authorized') is not False:
        raise RuntimeError('promotion authority unexpectedly authorizes science')
    return c


def require_launch_authority(path: str | None, contract_path: str):
    if not path:
        raise RuntimeError('sentinel science launch authority is required and absent')
    p = Path(path)
    if not p.is_file():
        raise RuntimeError('sentinel science launch authority file does not exist')
    a = json.loads(p.read_text())
    if a.get('schema') != 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1':
        raise RuntimeError('sentinel launch authority schema mismatch')
    if a.get('status') != 'TERMINAL_LAUNCH_AUTHORITY':
        raise RuntimeError('sentinel launch authority status mismatch')
    if a.get('sentinel_science_execution_authorized') is not True:
        raise RuntimeError('sentinel science execution is not authorized')
    if a.get('full_107_row_execution_authorized') is not False:
        raise RuntimeError('sentinel launch authority illegally opens full replay')
    if a.get('r1_contract_git_blob_sha1') != R1_CONTRACT_BLOB:
        raise RuntimeError('sentinel launch authority contract binding mismatch')
    if a.get('promotion_authority_git_blob_sha1') != PROMOTION_AUTHORITY_BLOB:
        raise RuntimeError('sentinel launch authority promotion-authority binding mismatch')
    if git_blob(contract_path) != R1_CONTRACT_BLOB:
        raise RuntimeError('live contract changed after launch authority')
    return a


def plan_bytes(path: str, c):
    raw = Path(path).read_bytes()
    p = c['response_blind_plan']
    if len(raw) != int(p['inner_byte_length']) or sha256_bytes(raw) != p['inner_sha256']:
        raise RuntimeError('source-plan byte identity mismatch')
    d = json.loads(raw)
    if d.get('coarse_calls_digest') != p['coarse_calls_digest'] or d.get('fine_calls_digest') != p['fine_calls_digest']:
        raise RuntimeError('source-plan call digest mismatch')
    if len(d['coarse_calls']) != 441 or len(d['fine_calls']) != 569 or d['coarse_calls'] != d['fine_calls'][:441]:
        raise RuntimeError('source-plan shape/prefix mismatch')
    return d


def reconstruct(c, plan):
    import numpy as np
    if np.__version__ != EXPECTED_NUMPY:
        raise RuntimeError(f'NumPy mismatch {np.__version__} != {EXPECTED_NUMPY}')
    probe = load('v026_r1_static_probe_for_sentinel', STATIC_PROBE)
    codec = load('chunk_codec_for_sentinel', CODEC)
    des_sets = [probe.uniq_targets(x) for x in plan['coarse_calls'][:377]]
    boss_sets = [probe.uniq_targets(x) for x in plan['coarse_calls'][377:441]]
    if len({tuple(x) for x in boss_sets}) != 1:
        raise RuntimeError('BOSS target identity mismatch')
    mixed = probe.mixed_plan(des_sets, boss_sets[0])
    direct = probe.direct_plan(des_sets, boss_sets[0])
    if probe.canonical_hash(mixed) != c['parser_payload_identity']['mixed_target_plan_canonical_sha256']:
        raise RuntimeError('mixed plan hash mismatch')
    if probe.canonical_hash(direct) != c['parser_payload_identity']['direct_target_plan_canonical_sha256']:
        raise RuntimeError('direct plan hash mismatch')
    common, ratio, nlo, nhi = probe.guarded_lattice(896)
    raw = np.ascontiguousarray(common, dtype='<f8').tobytes()
    if sha256_bytes(raw) != c['grid896']['node_payload_sha256']:
        raise RuntimeError('GRID896 binary identity mismatch')
    if (nlo, nhi, len(common)) != (0, 1, 897):
        raise RuntimeError('GRID896 geometry mismatch')
    by_m = {x['batch_id']: x for x in mixed}
    by_d = {x['batch_id']: x for x in direct}
    specs = c['sentinel']['batches']
    expected = {x['mixed_batch_id']: x for x in specs}
    if set(expected) != set(SENTINEL_BATCH_IDS):
        raise RuntimeError('sentinel batch IDs mismatch')
    for mid in SENTINEL_BATCH_IDS:
        m = by_m[mid]; d = by_d[DIRECT_BY_MIXED[mid]]; e = expected[mid]
        calls = m['call_indices']
        if 'mixed_call_indices' in e and calls != e['mixed_call_indices']:
            raise RuntimeError(f'{mid} call identity mismatch')
        if 'mixed_call_index_range' in e and calls != list(range(e['mixed_call_index_range'][0], e['mixed_call_index_range'][1] + 1)):
            raise RuntimeError(f'{mid} call range mismatch')
        if len(m['target_u64hex']) != e['mixed_target_count']:
            raise RuntimeError(f'{mid} target count mismatch')
        if 897 + len(m['target_u64hex']) != e['mixed_requested_node_count']:
            raise RuntimeError(f'{mid} requested node count mismatch')
        if d['batch_id'] != e['direct_batch_id'] or len(d['target_u64hex']) != e['direct_target_count']:
            raise RuntimeError(f'{mid} direct comparator mismatch')
        if not set(m['target_u64hex']).issubset(set(d['target_u64hex'])):
            raise RuntimeError(f'{mid} targets not contained in direct comparator')
    return np, probe, codec, common, by_m, by_d


def static_preflight(a):
    c = load_contract(a.contract)
    plan = plan_bytes(a.plan, c)
    np, probe, codec, common, by_m, by_d = reconstruct(c, plan)
    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_STATIC_PREFLIGHT_V0_1',
        'effect': '+0/+0',
        'r1_contract_git_blob_sha1': git_blob(a.contract),
        'promotion_authority_git_blob_sha1': git_blob(PROMOTION_AUTHORITY),
        'source_plan_sha256': c['response_blind_plan']['inner_sha256'],
        'grid896_sha256': sha256_bytes(np.ascontiguousarray(common, dtype='<f8').tobytes()),
        'sentinel_mixed_batches': list(SENTINEL_BATCH_IDS),
        'sentinel_direct_batches': [DIRECT_BY_MIXED[x] for x in SENTINEL_BATCH_IDS],
        'class_constructions_per_lane': c['sentinel']['class_constructions_per_lane'],
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'launch_authority_present': bool(a.launch_authority and Path(a.launch_authority).is_file()),
        'science_execution_authorized': False,
        'token': 'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_STATIC_PREFLIGHT_PLUS_0_PLUS_0',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])


def fingerprint(a):
    c = load_contract(a.contract)
    v025 = load('v025_for_v026_sentinel_fp', V025)
    m24 = v025.load_v024()
    fp = v025.response_free_fingerprint(m24)
    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_FINGERPRINT_V0_1',
        'fingerprint': fp,
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'token': 'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_FINGERPRINT_PLUS_0_PLUS_0',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])


def run_self(a, mode: str, out: Path, env, extra=None):
    cmd = [sys.executable, str(Path(__file__).resolve()), '--mode', mode, '--contract', a.contract, '--plan', a.plan, '--out', str(out)]
    if a.launch_authority:
        cmd += ['--launch-authority', a.launch_authority]
    if extra:
        cmd += list(extra)
    subprocess.run(cmd, check=True, env=env)
    return json.loads(out.read_text())


def child(a):
    c = load_contract(a.contract)
    require_launch_authority(a.launch_authority, a.contract)
    if os.environ.get('NPY_DISABLE_CPU_FEATURES') != NUMPY_DISABLE:
        raise RuntimeError('forced NumPy mask not active before child imports')
    plan = plan_bytes(a.plan, c)
    np, probe, codec, common, by_m, by_d = reconstruct(c, plan)
    import scipy
    if scipy.__version__ != EXPECTED_SCIPY:
        raise RuntimeError(f'SciPy mismatch {scipy.__version__} != {EXPECTED_SCIPY}')
    v025 = load('v025_for_v026_sentinel_child', V025)
    m24 = v025.load_v024(); m23 = m24.load_v023(); m22 = m23.load_v022()
    forced_fp = v025.response_free_fingerprint(m24)
    if not m22.forced_profile_ok(forced_fp):
        raise RuntimeError('forced NumPy dispatch profile invalid before CLASS solve')
    v12 = load('v12_for_v026_sentinel', V12)
    jj = load('jj_for_v026_sentinel', JJ)
    h = float(c['frozen_science']['h'])
    if h != 1e-4 or jj.NATIVE_KPD != c['frozen_science']['native_k_per_decade_for_pk']:
        raise RuntimeError('frozen science constants mismatch')

    def fhex(x: str) -> float:
        return struct.unpack('>d', bytes.fromhex(x))[0]

    selected_m = [by_m[x] for x in SENTINEL_BATCH_IDS]
    selected_d = [by_d[DIRECT_BY_MIXED[x]] for x in SENTINEL_BATCH_IDS]
    node_sets = {'PURE': np.asarray(common, dtype=np.float64)}
    for b in selected_m:
        targets = [fhex(x) for x in b['target_u64hex']]
        node_sets[b['batch_id']] = np.asarray(sorted(set(float(x) for x in common).union(targets)), dtype=np.float64)
    for b in selected_d:
        node_sets[b['batch_id']] = np.asarray([fhex(x) for x in b['target_u64hex']], dtype=np.float64)

    expected_counts = {'PURE': 897, 'M076': 1152, 'M298': 1141, 'M300': 996, 'D50': 1146, 'D00': 1152, 'D58': 99}
    if {k: len(v) for k,v in node_sets.items()} != expected_counts:
        raise RuntimeError('sentinel requested-node count mismatch')

    from classy import Class
    models = {}
    solver_count = 0
    try:
        for sid, nodes in node_sets.items():
            models[sid] = {}
            for sign, beta in [('plus', h), ('minus', -h)]:
                p = jj.class_params(Path(BASELINE), Path(PRECISION), 0.0, beta, nodes)
                p['tol_perturb_integration'] = c['frozen_science']['beta_tol_perturb_integration']
                cl = Class(); cl.set(p); cl.compute(['transfer'])
                models[sid][sign] = cl
                solver_count += 1
        if solver_count != EXPECTED_SOLVERS:
            raise RuntimeError(f'sentinel solver count {solver_count} != {EXPECTED_SOLVERS}')

        records = []
        max_lookup = 0.0
        kkeys = set()
        coarse = plan['coarse_calls']
        for mid in SENTINEL_BATCH_IDS:
            m = by_m[mid]; did = DIRECT_BY_MIXED[mid]
            for call_index in m['call_indices']:
                row = coarse[call_index]
                z = codec.u64hex_f64(row['z_u64hex'])
                target_hex = sorted(set(row['targets_u64hex']))
                ks = codec.u64hex_arr(target_hex)
                signed = {}
                for sign in ('plus', 'minus'):
                    yp, q1, k1 = v12.extract(jj, models['PURE'][sign], common, z)
                    ym, q2, k2 = v12.extract(jj, models[mid][sign], common, z)
                    ye, q3, k3 = v12.extract(jj, models[mid][sign], ks, z)
                    yd, q4, k4 = v12.extract(jj, models[did][sign], ks, z)
                    max_lookup = max(max_lookup, q1, q2, q3, q4); kkeys.update((k1,k2,k3,k4))
                    ip, vp = jj.cubic_centered(common, yp, ks)
                    im, vm = jj.cubic_centered(common, ym, ks)
                    if not bool(np.all(vp)) or not bool(np.all(vm)):
                        raise RuntimeError(f'unsupported sentinel interpolation {mid} call {call_index}')
                    signed[sign] = {'pure': np.asarray(ip), 'mixed_common': np.asarray(im), 'exact': np.asarray(ye), 'direct': np.asarray(yd)}
                for j, kh in enumerate(target_hex):
                    pure = float((signed['plus']['pure'][j]-signed['minus']['pure'][j])/(2*h))
                    mixed_common = float((signed['plus']['mixed_common'][j]-signed['minus']['mixed_common'][j])/(2*h))
                    exact = float((signed['plus']['exact'][j]-signed['minus']['exact'][j])/(2*h))
                    direct = float((signed['plus']['direct'][j]-signed['minus']['direct'][j])/(2*h))
                    vals = (pure, mixed_common, exact, direct)
                    if not all(math.isfinite(x) for x in vals):
                        raise RuntimeError('nonfinite sentinel primitive')
                    records.append({
                        'mixed_batch_id': mid, 'direct_batch_id': did, 'call_index': call_index,
                        'z_u64hex': row['z_u64hex'], 'k_u64hex': kh,
                        'pure_common_response': pure,
                        'mixed_common_response': mixed_common,
                        'exact_target_response': exact,
                        'direct_response': direct,
                        'mixed_common_vs_pure_common_rel': rel(mixed_common, pure, np),
                        'exact_vs_direct_rel': rel(exact, direct, np),
                    })
    finally:
        for d in models.values():
            for cl in d.values():
                try: cl.struct_cleanup()
                except Exception: pass

    if max_lookup > c['sentinel']['requested_node_binding_le']:
        raise RuntimeError('sentinel exact-node binding failure')
    fp = forced_fp
    software_key = canonical_hash({
        'python': fp['software']['python'], 'system': fp['software']['system'], 'machine': fp['software']['machine'],
        'numpy': fp['numpy']['numpy'], 'scipy': fp['numpy']['scipy'],
    })
    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_CHILD_V0_1',
        'effect': '+0/+0',
        'forced_profile_valid': True,
        'fingerprint': fp,
        'software_control_key': software_key,
        'solver_construction_count': solver_count,
        'requested_node_counts': expected_counts,
        'primitive_record_count': len(records),
        'primitive_records': records,
        'max_requested_node_coordinate_rel_mismatch': max_lookup,
        'native_transfer_k_keys': sorted(kkeys),
        'production_h_mutated': False,
        'sampling_stepsize_changed': False,
        'full_layerb_107_row_traversal_launched': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_CHILD_PLUS_0_PLUS_0',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], solver_count, len(records), max_lookup)


def lane(a):
    c = load_contract(a.contract)
    require_launch_authority(a.launch_authority, a.contract)
    if not a.replicate or a.replicate not in [f'R{i:02d}' for i in range(1,33)]:
        raise RuntimeError('unfrozen sentinel replicate')
    v025 = load('v025_for_v026_sentinel_lane', V025)
    m24 = v025.load_v024(); m23 = m24.load_v023(); m22 = m23.load_v022()
    tmp = Path(a.out).parent / f'.v026sent_{a.replicate}'; tmp.mkdir(parents=True, exist_ok=True)
    native = run_self(a, 'fingerprint', tmp/'native.json', clean_env())
    nfp = native['fingerprint']; candidate = m22.native_candidate_ok(nfp)
    forced = None; preflight_valid = None; result = None
    if candidate:
        forced = run_self(a, 'fingerprint', tmp/'forced.json', forced_env())
        preflight_valid = m22.forced_profile_ok(forced['fingerprint'])
        if preflight_valid:
            result = run_self(a, 'child', tmp/'result.json', forced_env())
    eligible = bool(candidate and preflight_valid and result is not None)
    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_LANE_V0_1',
        'replicate': a.replicate,
        'candidate': candidate,
        'eligible': eligible,
        'native_class': m22.native_class(nfp) if candidate else None,
        'native_fingerprint': nfp,
        'forced_preflight': forced,
        'preflight_valid': preflight_valid,
        'substantive_response_computed': bool(result is not None),
        'result': result,
        'effect': '+0/+0',
        'full_layerb_107_row_traversal_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_LANE_PLUS_0_PLUS_0',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], a.replicate, 'ELIGIBLE' if eligible else 'SKIP_OR_INVALID_PREFLIGHT')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--mode', required=True, choices=['static-preflight','fingerprint','lane','child'])
    p.add_argument('--contract', default=R1_CONTRACT)
    p.add_argument('--plan', required=True)
    p.add_argument('--launch-authority')
    p.add_argument('--replicate')
    p.add_argument('--out', required=True)
    a = p.parse_args()
    if a.mode == 'static-preflight': static_preflight(a)
    elif a.mode == 'fingerprint': fingerprint(a)
    elif a.mode == 'child': child(a)
    else: lane(a)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
