#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import os
import platform
import struct
import subprocess
import sys
from pathlib import Path

import numpy as np

V023_PATH = 'ci/layerb_beta_forced_baseline_production_h_replay_revalidation_v0_23.py'
NUMPY_DISABLE = 'AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX'
SERIES = ('pure_interp_response', 'mixed_interp_response', 'mixed_exact_response', 'direct_response')


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot import {path}')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def load_v023():
    return load_module('v023_for_v024', V023_PATH)


def canonical_hash(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def f64(h):
    return struct.unpack('>d', bytes.fromhex(h))[0]


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), np.finfo(np.float64).tiny)


def clean_env():
    e = os.environ.copy()
    e.pop('NPY_DISABLE_CPU_FEATURES', None)
    e.pop('GLIBC_TUNABLES', None)
    return e


def forced_env():
    e = clean_env()
    e['NPY_DISABLE_CPU_FEATURES'] = NUMPY_DISABLE
    return e


def response_free_fingerprint(M23):
    M22 = M23.load_v022()
    return M23.response_free_fingerprint(M22)


def run_self(a, mode, outpath, env, extra=None):
    cmd = [
        sys.executable, str(Path(__file__).resolve()),
        '--mode', mode,
        '--contract', a.contract,
        '--out', str(outpath),
    ]
    if extra:
        cmd.extend(extra)
    subprocess.run(cmd, check=True, env=env)
    return json.load(open(outpath))


def fingerprint_mode(a, M23):
    out = {
        'schema': 'LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_FINGERPRINT_V0_24',
        'fingerprint': response_free_fingerprint(M23),
        'token': 'PASS_LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_FINGERPRINT_V0_24',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')


def direct_nodes_from_manifest(manifest_path, domain):
    P = json.load(open(manifest_path))
    uniq = {}
    for x in P['items']:
        if x['d'] != domain:
            continue
        key = (x['kind'], x['z'], x['k'])
        if key in uniq:
            if uniq[key]['c'] != x['c'] or uniq[key]['f'] != x['f']:
                raise RuntimeError('historical direct probe duplicate mismatch')
        else:
            uniq[key] = x
    rows = list(uniq.values())
    nodes = np.asarray(sorted(set(f64(x['k']) for x in rows)), dtype=np.float64)
    return rows, nodes


def expected_cell_key(c):
    return (c['grid'], c['target_id'], c['kind'], c['d'], c['z'], c['k'])


def child_mode(a, C, M23):
    M22 = M23.load_v022()
    pre = response_free_fingerprint(M23)
    if not M22.forced_profile_ok(pre):
        raise RuntimeError('forced NumPy dispatch profile invalid before substantive solve')

    v12 = load_module('v12_for_v024', a.v12_executor)
    jj = load_module('jj_for_v024', a.jj_script)
    if jj.H != C['production_h']:
        raise RuntimeError('production h identity mismatch')
    if jj.REL_TOL != C['scientific_response_relative_tolerance']:
        raise RuntimeError('scientific threshold identity mismatch')
    if jj.NATIVE_KPD != C['native_k_per_decade_for_pk']:
        raise RuntimeError('native k-per-decade identity mismatch')

    h = float(C['production_h'])
    all_target_ks = np.asarray(sorted(set(f64(t['k']) for t in C['all_v012_targets'])), dtype=np.float64)
    target_by_id = {t['target_id']: t for t in C['all_v012_targets']}
    direct_rows, direct_nodes = direct_nodes_from_manifest(a.probe_manifest, C['direct_domain'])
    direct_node_set = set(float(x) for x in direct_nodes)

    for cell in C['parent_cells']:
        k = f64(cell['k'])
        if k not in direct_node_set:
            raise RuntimeError(f'parent target absent from frozen direct node set: {cell["target_id"]}')

    from classy import Class

    cells = []
    solver_count = 0
    max_lookup = 0.0
    kkeys = set()

    # Pure/mixed common-grid object, preserving the V0.12 all-three-target mixed union.
    for cell in C['parent_cells']:
        grid = cell['grid']
        target_id = cell['target_id']
        t = target_by_id[target_id]
        if (t['kind'], t['d'], t['z'], t['k']) != (cell['kind'], cell['d'], cell['z'], cell['k']):
            raise RuntimeError('parent/target identity mismatch')
        gcfg = C['grids'][grid]
        common, ratio, nlo, nhi = jj.guarded_lattice(int(gcfg['base_n']))
        if [nlo, nhi, len(common)] != [gcfg['lower_guard_count'], gcfg['upper_guard_count'], gcfg['requested_node_count']]:
            raise RuntimeError(f'guarded lattice mismatch {grid}')
        mixed = np.asarray(sorted(set(float(x) for x in common).union(float(x) for x in all_target_ks)), dtype=np.float64)
        expected_added = sum(1 for k0 in all_target_ks if not np.any(np.isclose(common, k0, rtol=0.0, atol=0.0)))
        if len(mixed) != len(common) + expected_added:
            raise RuntimeError(f'mixed node identity mismatch {grid}')

        pure = {}
        mixed_models = {}
        try:
            for label, beta in [('plus', h), ('minus', -h)]:
                for nodes, store in [(common, pure), (mixed, mixed_models)]:
                    p = jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, nodes)
                    p['tol_perturb_integration'] = C['tol300_override']
                    c = Class()
                    c.set(p)
                    c.compute(['transfer'])
                    store[label] = c
                    solver_count += 1

            z = f64(t['z'])
            k = f64(t['k'])
            sign = {}
            for label in ('plus', 'minus'):
                yp, m1, k1 = v12.extract(jj, pure[label], common, z)
                ym, m2, k2 = v12.extract(jj, mixed_models[label], common, z)
                ye, m3, k3 = v12.extract(jj, mixed_models[label], [k], z)
                max_lookup = max(max_lookup, float(m1), float(m2), float(m3))
                kkeys.update((k1, k2, k3))
                ip, vp = jj.cubic_centered(common, yp, np.asarray([k], dtype=np.float64))
                im, vm = jj.cubic_centered(common, ym, np.asarray([k], dtype=np.float64))
                if not bool(vp[0]) or not bool(vm[0]):
                    raise RuntimeError('unsupported frozen interpolation target')
                sign[label] = {
                    'pure_interp_transfer': float(ip[0]),
                    'mixed_interp_transfer': float(im[0]),
                    'mixed_exact_transfer': float(ye[0]),
                }

            cells.append({
                'grid': grid,
                'target_id': target_id,
                'kind': t['kind'],
                'd': t['d'],
                'z': t['z'],
                'k': t['k'],
                'z_value': z,
                'k_value': k,
                'common_requested_node_count': len(common),
                'mixed_requested_node_count': len(mixed),
                'exact_targets_added': expected_added,
                'pure_interp_response': (sign['plus']['pure_interp_transfer'] - sign['minus']['pure_interp_transfer']) / (2 * h),
                'mixed_interp_response': (sign['plus']['mixed_interp_transfer'] - sign['minus']['mixed_interp_transfer']) / (2 * h),
                'mixed_exact_response': (sign['plus']['mixed_exact_transfer'] - sign['minus']['mixed_exact_transfer']) / (2 * h),
            })
        finally:
            for c in list(pure.values()) + list(mixed_models.values()):
                try:
                    c.struct_cleanup()
                except Exception:
                    pass

    # Fresh direct-TOL300 object with the exact historical V0.7/V0.9 D-domain node semantics.
    direct = {}
    try:
        for label, beta in [('plus', h), ('minus', -h)]:
            p = jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, direct_nodes)
            p['tol_perturb_integration'] = C['tol300_override']
            c = Class()
            c.set(p)
            c.compute(['transfer'])
            direct[label] = c
            solver_count += 1

        for cell in cells:
            z = f64(cell['z'])
            k = f64(cell['k'])
            vals = {}
            for label in ('plus', 'minus'):
                yy, mx, kk = v12.extract(jj, direct[label], [k], z)
                max_lookup = max(max_lookup, float(mx))
                kkeys.add(kk)
                vals[label] = float(yy[0])
            cell['direct_response'] = (vals['plus'] - vals['minus']) / (2 * h)
            cell['pure_vs_direct_response_rel'] = rel(cell['pure_interp_response'], cell['direct_response'])
            cell['mixed_interp_vs_exact_response_rel'] = rel(cell['mixed_interp_response'], cell['mixed_exact_response'])
            cell['mixed_exact_vs_direct_response_rel'] = rel(cell['mixed_exact_response'], cell['direct_response'])
            cell['pure_vs_mixed_interp_response_rel'] = rel(cell['pure_interp_response'], cell['mixed_interp_response'])
            cell['parent_violation_reproduced'] = cell['pure_vs_direct_response_rel'] >= C['scientific_response_relative_tolerance']
            cell['interpolation_mechanism_supported'] = (
                cell['mixed_interp_vs_exact_response_rel'] >= C['scientific_response_relative_tolerance'] and
                cell['mixed_exact_vs_direct_response_rel'] < C['scientific_response_relative_tolerance'] and
                cell['pure_vs_mixed_interp_response_rel'] < C['scientific_response_relative_tolerance']
            )
            cell['node_set_dependence_supported'] = (
                cell['mixed_exact_vs_direct_response_rel'] >= C['scientific_response_relative_tolerance'] or
                cell['pure_vs_mixed_interp_response_rel'] >= C['scientific_response_relative_tolerance']
            )
    finally:
        for c in direct.values():
            try:
                c.struct_cleanup()
            except Exception:
                pass

    if solver_count != C['expected_solver_construction_count']:
        raise RuntimeError(f'unexpected solver count {solver_count}')
    if any(not math.isfinite(float(c[s])) for c in cells for s in SERIES):
        raise RuntimeError('nonfinite primitive response')

    M21 = M22.load_v021()
    B = M21.load_base()
    fp = B.fingerprint()
    software_key = canonical_hash({
        'python': fp['software']['python'],
        'system': fp['software']['system'],
        'machine': fp['software']['machine'],
        'numpy': fp['numpy']['numpy'],
        'scipy': fp['numpy']['scipy'],
    })

    out = {
        'schema': 'LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_CHILD_V0_24',
        'forced_profile_valid': M22.forced_profile_ok(fp),
        'validated_numpy_mask': NUMPY_DISABLE,
        'fingerprint': fp,
        'software_control_key': software_key,
        'direct_domain': C['direct_domain'],
        'direct_deduplicated_probe_row_count': len(direct_rows),
        'direct_unique_node_count': len(direct_nodes),
        'solver_construction_count': solver_count,
        'max_requested_node_coordinate_rel_mismatch': max_lookup,
        'native_transfer_k_keys': sorted(kkeys),
        'cells': cells,
        'production_h_mutated': False,
        'sampling_stepsize_changed': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_CHILD_V0_24',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], solver_count, len(direct_nodes), max_lookup)


def lane_mode(a, C, M23):
    if a.replicate not in C['replicates']:
        raise RuntimeError('unfrozen replicate')
    M22 = M23.load_v022()
    tmp = Path(a.out).parent / f'.v024_{a.replicate}'
    tmp.mkdir(parents=True, exist_ok=True)

    native = run_self(a, 'fingerprint', tmp / 'native.json', clean_env())
    nfp = native['fingerprint']
    candidate = M22.native_candidate_ok(nfp)
    forced = None
    preflight_valid = None
    result = None
    if candidate:
        forced = run_self(a, 'fingerprint', tmp / 'forced.json', forced_env())
        preflight_valid = M22.forced_profile_ok(forced['fingerprint'])
        if preflight_valid:
            extra = [
                '--v12-executor', a.v12_executor,
                '--jj-script', a.jj_script,
                '--probe-manifest', a.probe_manifest,
                '--baseline', a.baseline,
                '--precision', a.precision,
            ]
            result = run_self(a, 'child', tmp / 'result.json', forced_env(), extra)

    eligible = bool(candidate and preflight_valid)
    out = {
        'schema': 'LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_LANE_V0_24',
        'replicate': a.replicate,
        'candidate': candidate,
        'eligible': eligible,
        'native_class': M22.native_class(nfp) if candidate else None,
        'native_fingerprint': nfp,
        'forced_preflight': forced,
        'preflight_valid': preflight_valid,
        'substantive_response_computed': bool(result is not None),
        'result': result,
        'effect': '+0/+0',
        'production_h_mutated': False,
        'sampling_stepsize_changed': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_LANE_V0_24',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], a.replicate, 'ELIGIBLE' if eligible else ('INVALID_PREFLIGHT' if candidate else 'SKIP'))


def decision_mode(a, C):
    docs = [json.load(open(p)) for p in a.inputs]
    expected_reps = set(C['replicates'])
    got = {d.get('replicate') for d in docs}
    if got != expected_reps or len(docs) != len(expected_reps):
        raise RuntimeError('lane identity mismatch')

    candidates = [d for d in docs if d.get('candidate')]
    eligible = [d for d in docs if d.get('eligible')]
    invalid = any(d.get('preflight_valid') is not True for d in candidates)
    invalid |= any(d.get('substantive_response_computed') and d.get('preflight_valid') is not True for d in docs)

    expected_cells = {expected_cell_key(c) for c in C['parent_cells']}
    binary_keys = []
    software_keys = []
    direct_counts = []
    max_lookup = 0.0
    invariant_ok = True

    for d in eligible:
        r = d.get('result')
        if r is None or r.get('forced_profile_valid') is not True:
            invalid = True
            continue
        if r.get('solver_construction_count') != C['expected_solver_construction_count']:
            invalid = True
        cells = r.get('cells', [])
        keys = {expected_cell_key(c) for c in cells}
        if len(cells) != len(expected_cells) or keys != expected_cells:
            invalid = True
        if r.get('direct_domain') != C['direct_domain']:
            invalid = True
        if 'fingerprint' not in r or 'binary' not in r['fingerprint'] or 'software_control_key' not in r:
            invalid = True
            continue
        binary_keys.append(r['fingerprint']['binary']['key'])
        software_keys.append(r['software_control_key'])
        direct_counts.append((r.get('direct_deduplicated_probe_row_count'), r.get('direct_unique_node_count')))
        max_lookup = max(max_lookup, float(r.get('max_requested_node_coordinate_rel_mismatch', float('inf'))))
        for c in cells:
            invariant_ok &= all(math.isfinite(float(c.get(s, float('nan')))) for s in SERIES)
            invariant_ok &= all(math.isfinite(float(c.get(q, float('nan')))) for q in [
                'pure_vs_direct_response_rel', 'mixed_interp_vs_exact_response_rel',
                'mixed_exact_vs_direct_response_rel', 'pure_vs_mixed_interp_response_rel'])
        invariant_ok &= not any(bool(r.get(k, True)) for k in [
            'production_h_mutated', 'sampling_stepsize_changed', 'global_65537_launched',
            'covariance_read', 'whitening_read', 'nuisance_read', 'relation_null_read',
            'Wm_S3_opened', 'science_gate_opened'])

    if eligible and (len(set(binary_keys)) != 1 or len(set(software_keys)) != 1 or len(set(direct_counts)) != 1):
        invalid = True
    invariant_ok &= max_lookup <= float(C['exact_target_binding_tolerance'])

    classes = ('NATIVE_AVX512_ACTIVE', 'NATIVE_AVX512_INACTIVE')
    counts = {x: sum(d.get('native_class') == x for d in eligible) for x in classes}
    powered = (
        len(eligible) >= int(C['minimum_eligible_lane_n']) and
        counts['NATIVE_AVX512_ACTIVE'] >= int(C['minimum_per_native_class_n']) and
        counts['NATIVE_AVX512_INACTIVE'] >= int(C['minimum_per_native_class_n'])
    )

    primitive_metrics = []
    primitive_reproducible = False
    cell_unanimity = []
    if not invalid and invariant_ok and powered:
        primitive_reproducible = True
        maps = {
            d['replicate']: {expected_cell_key(c): c for c in d['result']['cells']}
            for d in eligible
        }
        for cell_spec in C['parent_cells']:
            ck = expected_cell_key(cell_spec)
            for series in SERIES:
                vals = [float(maps[d['replicate']][ck][series]) for d in eligible]
                spread = max([rel(x, y) for x, y in itertools.combinations(vals, 2)] or [0.0])
                means = {}
                for cls in classes:
                    vv = [float(maps[d['replicate']][ck][series]) for d in eligible if d['native_class'] == cls]
                    means[cls] = sum(vv) / len(vv)
                sep = rel(means['NATIVE_AVX512_ACTIVE'], means['NATIVE_AVX512_INACTIVE'])
                ok = spread < C['replay_relative_tolerance'] and sep < C['replay_relative_tolerance']
                primitive_reproducible &= ok
                primitive_metrics.append({
                    'grid': cell_spec['grid'], 'target_id': cell_spec['target_id'], 'series': series,
                    'cross_host_max_pairwise_rel_spread': spread,
                    'native_class_mean_rel_separation': sep,
                    'reproducible': ok,
                })

        for cell_spec in C['parent_cells']:
            ck = expected_cell_key(cell_spec)
            lane_cells = [maps[d['replicate']][ck] for d in eligible]
            rep = all(bool(c['parent_violation_reproduced']) for c in lane_cells)
            interp = all(bool(c['interpolation_mechanism_supported']) for c in lane_cells)
            nodeset = all(bool(c['node_set_dependence_supported']) for c in lane_cells)
            cell_unanimity.append({
                'grid': cell_spec['grid'], 'target_id': cell_spec['target_id'],
                'parent_violation_reproduced_unanimous': rep,
                'interpolation_mechanism_supported_unanimous': interp,
                'node_set_dependence_supported_unanimous': nodeset,
                'lane_pure_vs_direct_response_rel_min': min(float(c['pure_vs_direct_response_rel']) for c in lane_cells),
                'lane_pure_vs_direct_response_rel_max': max(float(c['pure_vs_direct_response_rel']) for c in lane_cells),
                'lane_mixed_interp_vs_exact_response_rel_min': min(float(c['mixed_interp_vs_exact_response_rel']) for c in lane_cells),
                'lane_mixed_interp_vs_exact_response_rel_max': max(float(c['mixed_interp_vs_exact_response_rel']) for c in lane_cells),
                'lane_mixed_exact_vs_direct_response_rel_max': max(float(c['mixed_exact_vs_direct_response_rel']) for c in lane_cells),
                'lane_pure_vs_mixed_interp_response_rel_max': max(float(c['pure_vs_mixed_interp_response_rel']) for c in lane_cells),
            })

    if invalid:
        cls = 'FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_REASSESSMENT_INVALID'
        nxt = 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_24_FORCED_BASELINE_VALIDATION'
    elif not invariant_ok:
        cls = 'FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_REASSESSMENT_INCONCLUSIVE'
        nxt = 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_24_INVARIANT_FAILURE'
    elif not powered:
        cls = 'FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_REASSESSMENT_UNDERPOWERED'
        nxt = 'PROSPECTIVELY_FROZEN_EXPANDED_FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_REPLICATION_AUDIT'
    elif not primitive_reproducible:
        cls = 'FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_REASSESSMENT_REPRODUCIBILITY_BLOCKED'
        nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_INTERPOLATION_OBJECT_REPRODUCIBILITY_DIAGNOSTIC'
    else:
        all_rep = all(x['parent_violation_reproduced_unanimous'] for x in cell_unanimity)
        interps = [x['interpolation_mechanism_supported_unanimous'] for x in cell_unanimity]
        nodes = [x['node_set_dependence_supported_unanimous'] for x in cell_unanimity]
        accounted = [i or n for i, n in zip(interps, nodes)]
        if not all_rep:
            cls = 'FORCED_BASELINE_PRODUCTION_H_PARENT_VIOLATIONS_NOT_REPRODUCED'
            nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_DISCREPANCY_REBASELINE_AUDIT'
        elif all(interps) and not any(nodes):
            cls = 'FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_CUBIC_INTERPOLATION_SUPPORTED'
            nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK'
        elif all(nodes) and not any(interps):
            cls = 'FORCED_BASELINE_PRODUCTION_H_K_OUTPUT_NODE_SET_SOLVER_DEPENDENCE_SUPPORTED'
            nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_K_OUTPUT_NODE_SET_SENSITIVITY_AUDIT'
        elif all(accounted) and any(interps) and any(nodes):
            cls = 'FORCED_BASELINE_PRODUCTION_H_MIXED_INTERPOLATION_AND_NODE_SET_DEPENDENCE_SUPPORTED'
            nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_MIXED_NUMERICAL_MECHANISM_AUDIT'
        else:
            cls = 'FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_PATTERN_UNRESOLVED'
            nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_TARGET_STENCIL_GEOMETRY_AUDIT'

    out = {
        'schema': 'LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_DECISION_V0_24',
        'classification': cls,
        'effect': '+0/+0',
        'candidate_lane_count': len(candidates),
        'eligible_lane_count': len(eligible),
        'eligible_replicates': [d['replicate'] for d in eligible],
        'native_class_counts': counts,
        'minimum_eligible_lane_n': int(C['minimum_eligible_lane_n']),
        'minimum_per_native_class_n': int(C['minimum_per_native_class_n']),
        'invalid': invalid,
        'invariant_ok': invariant_ok,
        'powered': powered,
        'primitive_response_reproducibility_ok': primitive_reproducible,
        'primitive_response_metrics': primitive_metrics,
        'cell_unanimity': cell_unanimity,
        'max_requested_node_coordinate_rel_mismatch': max_lookup,
        'binary_key_count': len(set(binary_keys)),
        'software_control_key_count': len(set(software_keys)),
        'direct_node_identity_count': len(set(direct_counts)),
        'next_stage': nxt,
        'production_h_mutated': False,
        'sampling_stepsize_changed': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_INTERPOLATION_DECISION_V0_24',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], json.dumps({
        'classification': cls,
        'eligible_lane_count': len(eligible),
        'native_class_counts': counts,
        'primitive_response_reproducibility_ok': primitive_reproducible,
        'next_stage': nxt,
    }, sort_keys=True))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--mode', choices=['fingerprint', 'child', 'lane', 'decision'], required=True)
    p.add_argument('--replicate')
    p.add_argument('--contract', required=True)
    p.add_argument('--v12-executor')
    p.add_argument('--jj-script')
    p.add_argument('--probe-manifest')
    p.add_argument('--baseline')
    p.add_argument('--precision')
    p.add_argument('--inputs', nargs='*')
    p.add_argument('--out', required=True)
    a = p.parse_args()
    C = json.load(open(a.contract))
    M23 = load_v023()
    if a.mode == 'fingerprint':
        fingerprint_mode(a, M23)
    elif a.mode == 'child':
        required = [a.v12_executor, a.jj_script, a.probe_manifest, a.baseline, a.precision]
        if not all(required):
            raise RuntimeError('child mode missing required args')
        child_mode(a, C, M23)
    elif a.mode == 'lane':
        required = [a.replicate, a.v12_executor, a.jj_script, a.probe_manifest, a.baseline, a.precision]
        if not all(required):
            raise RuntimeError('lane mode missing required args')
        lane_mode(a, C, M23)
    else:
        if not a.inputs:
            raise RuntimeError('decision mode missing inputs')
        decision_mode(a, C)


if __name__ == '__main__':
    main()
