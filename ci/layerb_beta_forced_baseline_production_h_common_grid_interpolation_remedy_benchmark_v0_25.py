#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import os
import struct
import subprocess
import sys
from pathlib import Path

import numpy as np

V024_PATH = 'ci/layerb_beta_forced_baseline_production_h_common_grid_interpolation_reassessment_v0_24.py'
NUMPY_DISABLE = 'AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX'
PRIMITIVE_SERIES = ('control_response', 'exact_target_union_response', 'one_step_refinement_response', 'direct_response')
CLASSES = ('NATIVE_AVX512_ACTIVE', 'NATIVE_AVX512_INACTIVE')


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot import {path}')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def load_v024():
    return load_module('v024_for_v025', V024_PATH)


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


def run_self(a, mode, outpath, env, extra=None):
    cmd = [sys.executable, str(Path(__file__).resolve()), '--mode', mode, '--contract', a.contract, '--out', str(outpath)]
    if extra:
        cmd.extend(extra)
    subprocess.run(cmd, check=True, env=env)
    return json.load(open(outpath))


def response_free_fingerprint(M24):
    M23 = M24.load_v023()
    return M24.response_free_fingerprint(M23)


def fingerprint_mode(a, M24):
    out = {
        'schema': 'LAYERB_BETA_FORCED_BASELINE_INTERPOLATION_REMEDY_FINGERPRINT_V0_25',
        'fingerprint': response_free_fingerprint(M24),
        'token': 'PASS_LAYERB_BETA_FORCED_BASELINE_INTERPOLATION_REMEDY_FINGERPRINT_V0_25',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')


def exact_union(common, target_ks):
    return np.asarray(sorted(set(float(x) for x in common).union(float(x) for x in target_ks)), dtype=np.float64)


def child_mode(a, C, M24):
    M23 = M24.load_v023()
    M22 = M23.load_v022()
    pre = response_free_fingerprint(M24)
    if not M22.forced_profile_ok(pre):
        raise RuntimeError('forced NumPy dispatch profile invalid before substantive solve')

    v12 = load_module('v12_for_v025', a.v12_executor)
    jj = load_module('jj_for_v025', a.jj_script)
    if jj.H != C['production_h']:
        raise RuntimeError('production h identity mismatch')
    if jj.REL_TOL != C['scientific_response_relative_tolerance']:
        raise RuntimeError('scientific threshold identity mismatch')
    if jj.NATIVE_KPD != C['native_k_per_decade_for_pk']:
        raise RuntimeError('native k-per-decade identity mismatch')

    target_by_id = {t['target_id']: t for t in C['targets']}
    if set(target_by_id) != {'T1', 'T2', 'T3'}:
        raise RuntimeError('target identity mismatch')
    target_ks = np.asarray(sorted(f64(t['k']) for t in C['targets']), dtype=np.float64)

    common = {}
    for grid in ('GRID768', 'GRID896', 'GRID1024'):
        spec = C['grids'][grid]
        nodes, ratio, nlo, nhi = jj.guarded_lattice(int(spec['base_n']))
        if [nlo, nhi, len(nodes)] != [spec['lower_guard_count'], spec['upper_guard_count'], spec['requested_node_count']]:
            raise RuntimeError(f'guarded lattice mismatch {grid}')
        common[grid] = nodes

    mixed = {'GRID768': exact_union(common['GRID768'], target_ks), 'GRID896': exact_union(common['GRID896'], target_ks)}
    mixed_added = {}
    for grid in ('GRID768', 'GRID896'):
        mixed_added[grid] = sum(1 for k in target_ks if not np.any(np.isclose(common[grid], k, rtol=0.0, atol=0.0)))
        if len(mixed[grid]) != len(common[grid]) + mixed_added[grid]:
            raise RuntimeError(f'exact-target union mismatch {grid}')

    direct_rows, direct_nodes = M24.direct_nodes_from_manifest(a.probe_manifest, C['direct_domain'])
    direct_node_set = set(float(x) for x in direct_nodes)
    if not all(f64(t['k']) in direct_node_set for t in C['targets']):
        raise RuntimeError('benchmark target absent from frozen direct node set')

    h = float(C['production_h'])
    from classy import Class

    node_sets = {
        'COMMON768': common['GRID768'],
        'COMMON896': common['GRID896'],
        'COMMON1024': common['GRID1024'],
        'MIXED768': mixed['GRID768'],
        'MIXED896': mixed['GRID896'],
        'DIRECT': direct_nodes,
    }
    models = {}
    solver_count = 0
    max_lookup = 0.0
    kkeys = set()
    try:
        for set_id, nodes in node_sets.items():
            models[set_id] = {}
            for label, beta in [('plus', h), ('minus', -h)]:
                p = jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, nodes)
                p['tol_perturb_integration'] = C['tol300_override']
                c = Class()
                c.set(p)
                c.compute(['transfer'])
                models[set_id][label] = c
                solver_count += 1

        cells = []
        for original_grid in C['benchmark_grids']:
            control_set = 'COMMON768' if original_grid == 'GRID768' else 'COMMON896'
            mixed_set = 'MIXED768' if original_grid == 'GRID768' else 'MIXED896'
            refine_grid = C['refinement_map'][original_grid]
            refine_set = 'COMMON896' if refine_grid == 'GRID896' else 'COMMON1024'
            for target_id in C['target_ids']:
                t = target_by_id[target_id]
                z = f64(t['z'])
                k = f64(t['k'])
                sign = {}
                for label in ('plus', 'minus'):
                    yc, m1, q1 = v12.extract(jj, models[control_set][label], common[original_grid], z)
                    ym, m2, q2 = v12.extract(jj, models[mixed_set][label], common[original_grid], z)
                    ye, m3, q3 = v12.extract(jj, models[mixed_set][label], [k], z)
                    yr, m4, q4 = v12.extract(jj, models[refine_set][label], common[refine_grid], z)
                    yd, m5, q5 = v12.extract(jj, models['DIRECT'][label], [k], z)
                    max_lookup = max(max_lookup, m1, m2, m3, m4, m5)
                    kkeys.update((q1, q2, q3, q4, q5))
                    ic, vc = jj.cubic_centered(common[original_grid], yc, np.asarray([k], dtype=np.float64))
                    im, vm = jj.cubic_centered(common[original_grid], ym, np.asarray([k], dtype=np.float64))
                    ir, vr = jj.cubic_centered(common[refine_grid], yr, np.asarray([k], dtype=np.float64))
                    if not (bool(vc[0]) and bool(vm[0]) and bool(vr[0])):
                        raise RuntimeError('unsupported frozen interpolation target')
                    sign[label] = {
                        'control_transfer': float(ic[0]),
                        'mixed_common_interp_transfer': float(im[0]),
                        'exact_target_union_transfer': float(ye[0]),
                        'one_step_refinement_transfer': float(ir[0]),
                        'direct_transfer': float(yd[0]),
                    }

                def centered(key):
                    return (sign['plus'][key] - sign['minus'][key]) / (2 * h)

                control_response = centered('control_transfer')
                mixed_common_interp_response = centered('mixed_common_interp_transfer')
                exact_target_union_response = centered('exact_target_union_transfer')
                one_step_refinement_response = centered('one_step_refinement_transfer')
                direct_response = centered('direct_transfer')
                cells.append({
                    'original_grid': original_grid,
                    'refinement_grid': refine_grid,
                    'target_id': target_id,
                    'kind': t['kind'],
                    'd': t['d'],
                    'z': t['z'],
                    'k': t['k'],
                    'z_value': z,
                    'k_value': k,
                    'control_response': control_response,
                    'mixed_common_interp_response': mixed_common_interp_response,
                    'exact_target_union_response': exact_target_union_response,
                    'one_step_refinement_response': one_step_refinement_response,
                    'direct_response': direct_response,
                    'control_vs_direct_rel': rel(control_response, direct_response),
                    'mixed_common_vs_control_rel': rel(mixed_common_interp_response, control_response),
                    'exact_target_union_vs_direct_rel': rel(exact_target_union_response, direct_response),
                    'one_step_refinement_vs_direct_rel': rel(one_step_refinement_response, direct_response),
                    'is_parent_gating_cell': (original_grid, target_id) in {('GRID768', 'T2'), ('GRID896', 'T3')},
                })
    finally:
        for by_sign in models.values():
            for c in by_sign.values():
                try:
                    c.struct_cleanup()
                except Exception:
                    pass

    if solver_count != C['expected_solver_construction_count']:
        raise RuntimeError(f'unexpected solver count {solver_count}')
    if len(cells) != C['panel_cell_count']:
        raise RuntimeError('panel cell count mismatch')
    if any(not math.isfinite(float(c[s])) for c in cells for s in PRIMITIVE_SERIES + ('mixed_common_interp_response',)):
        raise RuntimeError('nonfinite primitive response')

    M21 = M22.load_v021()
    B = M21.load_base()
    fp = B.fingerprint()
    software_key = canonical_hash({
        'python': fp['software']['python'], 'system': fp['software']['system'], 'machine': fp['software']['machine'],
        'numpy': fp['numpy']['numpy'], 'scipy': fp['numpy']['scipy'],
    })

    out = {
        'schema': 'LAYERB_BETA_FORCED_BASELINE_INTERPOLATION_REMEDY_CHILD_V0_25',
        'forced_profile_valid': M22.forced_profile_ok(fp),
        'validated_numpy_mask': NUMPY_DISABLE,
        'fingerprint': fp,
        'software_control_key': software_key,
        'solver_construction_count': solver_count,
        'direct_domain': C['direct_domain'],
        'direct_deduplicated_probe_row_count': len(direct_rows),
        'direct_unique_node_count': len(direct_nodes),
        'requested_node_counts': {k: int(len(v)) for k, v in node_sets.items()},
        'mixed_exact_targets_added': mixed_added,
        'max_requested_node_coordinate_rel_mismatch': max_lookup,
        'native_transfer_k_keys': sorted(kkeys),
        'cells': cells,
        'production_h_mutated': False,
        'sampling_stepsize_changed': False,
        'global_65537_launched': False,
        'full_layerb_107_row_traversal_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_FORCED_BASELINE_INTERPOLATION_REMEDY_CHILD_V0_25',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], solver_count, len(cells), max_lookup)


def lane_mode(a, C, M24):
    if a.replicate not in C['replicates']:
        raise RuntimeError('unfrozen replicate')
    M23 = M24.load_v023()
    M22 = M23.load_v022()
    tmp = Path(a.out).parent / f'.v025_{a.replicate}'
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
            extra = ['--v12-executor', a.v12_executor, '--jj-script', a.jj_script, '--probe-manifest', a.probe_manifest, '--baseline', a.baseline, '--precision', a.precision]
            result = run_self(a, 'child', tmp / 'result.json', forced_env(), extra)
    eligible = bool(candidate and preflight_valid)
    out = {
        'schema': 'LAYERB_BETA_FORCED_BASELINE_INTERPOLATION_REMEDY_LANE_V0_25',
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
        'full_layerb_107_row_traversal_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_FORCED_BASELINE_INTERPOLATION_REMEDY_LANE_V0_25',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], a.replicate, 'ELIGIBLE' if eligible else ('INVALID_PREFLIGHT' if candidate else 'SKIP'))


def cell_key(c):
    return (c['original_grid'], c['target_id'], c['kind'], c['d'], c['z'], c['k'])


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

    expected_cells = {(grid, t['target_id'], t['kind'], t['d'], t['z'], t['k']) for grid in C['benchmark_grids'] for t in C['targets']}
    binary_keys = []
    software_keys = []
    direct_counts = []
    node_count_records = []
    max_lookup = 0.0
    invariant_ok = True
    forbidden_keys = ['production_h_mutated', 'sampling_stepsize_changed', 'global_65537_launched', 'full_layerb_107_row_traversal_launched', 'covariance_read', 'whitening_read', 'nuisance_read', 'relation_null_read', 'Wm_S3_opened', 'science_gate_opened']

    for d in eligible:
        r = d.get('result')
        if r is None or r.get('forced_profile_valid') is not True:
            invalid = True
            continue
        if r.get('solver_construction_count') != C['expected_solver_construction_count']:
            invalid = True
        cells = r.get('cells', [])
        if len(cells) != C['panel_cell_count'] or {cell_key(c) for c in cells} != expected_cells:
            invalid = True
        if r.get('direct_domain') != C['direct_domain']:
            invalid = True
        if r.get('requested_node_counts') != C['expected_requested_node_counts']:
            invalid = True
        if r.get('mixed_exact_targets_added') != C['expected_mixed_exact_targets_added']:
            invalid = True
        if 'fingerprint' not in r or 'binary' not in r['fingerprint'] or 'software_control_key' not in r:
            invalid = True
            continue
        binary_keys.append(r['fingerprint']['binary']['key'])
        software_keys.append(r['software_control_key'])
        direct_counts.append((r.get('direct_deduplicated_probe_row_count'), r.get('direct_unique_node_count')))
        node_count_records.append(canonical_hash(r.get('requested_node_counts')))
        max_lookup = max(max_lookup, float(r.get('max_requested_node_coordinate_rel_mismatch', float('inf'))))
        for c in cells:
            invariant_ok &= all(math.isfinite(float(c.get(s, float('nan')))) for s in PRIMITIVE_SERIES + ('mixed_common_interp_response',))
            invariant_ok &= all(math.isfinite(float(c.get(q, float('nan')))) for q in ['control_vs_direct_rel', 'mixed_common_vs_control_rel', 'exact_target_union_vs_direct_rel', 'one_step_refinement_vs_direct_rel'])
        invariant_ok &= not any(bool(r.get(k, True)) for k in forbidden_keys)

    if eligible and (len(set(binary_keys)) != 1 or len(set(software_keys)) != 1 or len(set(direct_counts)) != 1 or len(set(node_count_records)) != 1):
        invalid = True
    invariant_ok &= max_lookup <= float(C['exact_target_binding_tolerance'])
    counts = {x: sum(d.get('native_class') == x for d in eligible) for x in CLASSES}
    powered = len(eligible) >= int(C['minimum_eligible_lane_n']) and counts['NATIVE_AVX512_ACTIVE'] >= int(C['minimum_per_native_class_n']) and counts['NATIVE_AVX512_INACTIVE'] >= int(C['minimum_per_native_class_n'])

    primitive_metrics = []
    primitive_reproducible = False
    panel_summary = []
    parent_reproduced = False
    exact_supported = False
    refinement_supported = False
    node_set_safety = False

    if not invalid and invariant_ok and powered:
        maps = {d['replicate']: {cell_key(c): c for c in d['result']['cells']} for d in eligible}
        primitive_reproducible = True
        for grid in C['benchmark_grids']:
            for t in C['targets']:
                ck = (grid, t['target_id'], t['kind'], t['d'], t['z'], t['k'])
                for series in PRIMITIVE_SERIES:
                    vals = [float(maps[d['replicate']][ck][series]) for d in eligible]
                    spread = max([rel(x, y) for x, y in itertools.combinations(vals, 2)] or [0.0])
                    means = {}
                    for cls in CLASSES:
                        vv = [float(maps[d['replicate']][ck][series]) for d in eligible if d['native_class'] == cls]
                        means[cls] = sum(vv) / len(vv)
                    sep = rel(means['NATIVE_AVX512_ACTIVE'], means['NATIVE_AVX512_INACTIVE'])
                    ok = spread < C['replay_relative_tolerance'] and sep < C['replay_relative_tolerance']
                    primitive_reproducible &= ok
                    primitive_metrics.append({'original_grid': grid, 'target_id': t['target_id'], 'series': series, 'cross_host_max_pairwise_rel_spread': spread, 'native_class_mean_rel_separation': sep, 'reproducible': ok})

        if primitive_reproducible:
            parent_flags = []
            exact_flags = []
            refine_flags = []
            node_safety_flags = []
            for grid in C['benchmark_grids']:
                for t in C['targets']:
                    ck = (grid, t['target_id'], t['kind'], t['d'], t['z'], t['k'])
                    lane_cells = [maps[d['replicate']][ck] for d in eligible]
                    is_parent = (grid, t['target_id']) in {('GRID768', 'T2'), ('GRID896', 'T3')}
                    parent_ok = all(float(c['control_vs_direct_rel']) >= C['scientific_response_relative_tolerance'] for c in lane_cells) if is_parent else None
                    exact_ok = all(float(c['exact_target_union_vs_direct_rel']) < C['scientific_response_relative_tolerance'] for c in lane_cells)
                    refine_ok = all(float(c['one_step_refinement_vs_direct_rel']) < C['scientific_response_relative_tolerance'] for c in lane_cells)
                    node_ok = all(float(c['mixed_common_vs_control_rel']) < C['scientific_response_relative_tolerance'] for c in lane_cells)
                    if is_parent:
                        parent_flags.append(parent_ok)
                    exact_flags.append(exact_ok)
                    refine_flags.append(refine_ok)
                    node_safety_flags.append(node_ok)
                    panel_summary.append({
                        'original_grid': grid, 'target_id': t['target_id'], 'parent_gating_cell': is_parent,
                        'parent_control_reproduced_unanimous': parent_ok,
                        'exact_target_union_pass_unanimous': exact_ok,
                        'one_step_refinement_pass_unanimous': refine_ok,
                        'mixed_node_set_safety_pass_unanimous': node_ok,
                        'control_vs_direct_rel_min': min(float(c['control_vs_direct_rel']) for c in lane_cells),
                        'control_vs_direct_rel_max': max(float(c['control_vs_direct_rel']) for c in lane_cells),
                        'exact_target_union_vs_direct_rel_max': max(float(c['exact_target_union_vs_direct_rel']) for c in lane_cells),
                        'one_step_refinement_vs_direct_rel_max': max(float(c['one_step_refinement_vs_direct_rel']) for c in lane_cells),
                        'mixed_common_vs_control_rel_max': max(float(c['mixed_common_vs_control_rel']) for c in lane_cells),
                    })
            parent_reproduced = all(parent_flags)
            node_set_safety = all(node_safety_flags)
            exact_supported = all(exact_flags) and node_set_safety
            refinement_supported = all(refine_flags)

    if invalid:
        cls = 'FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_INVALID'
        nxt = 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_25_FORCED_BASELINE_VALIDATION'
    elif not invariant_ok:
        cls = 'FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_INCONCLUSIVE'
        nxt = 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_25_INVARIANT_FAILURE'
    elif not powered:
        cls = 'FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_UNDERPOWERED'
        nxt = 'PROSPECTIVELY_FROZEN_EXPANDED_FORCED_BASELINE_INTERPOLATION_REMEDY_REPLICATION_AUDIT'
    elif not primitive_reproducible:
        cls = 'FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_REPRODUCIBILITY_BLOCKED'
        nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_INTERPOLATION_REMEDY_OBJECT_REPRODUCIBILITY_DIAGNOSTIC'
    elif not parent_reproduced:
        cls = 'FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_PARENT_NOT_REPRODUCED'
        nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_DISCREPANCY_REBASELINE_AUDIT'
    elif exact_supported and refinement_supported:
        cls = 'FORCED_BASELINE_EXACT_TARGET_UNION_AND_ONE_STEP_REFINEMENT_REMEDIES_SUPPORTED_EXACT_TARGET_UNION_PREFERRED'
        nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT'
    elif exact_supported:
        cls = 'FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED'
        nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT'
    elif refinement_supported:
        cls = 'FORCED_BASELINE_ONE_STEP_GRID_REFINEMENT_REMEDY_SUPPORTED'
        nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_REFINED_COMMON_GRID_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT'
    else:
        cls = 'FORCED_BASELINE_INTERPOLATION_REMEDY_BENCHMARK_NO_CANDIDATE_SUPPORTED'
        nxt = 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_INTERPOLATION_REMEDY_EXPANSION_AUDIT'

    out = {
        'schema': 'LAYERB_BETA_FORCED_BASELINE_INTERPOLATION_REMEDY_DECISION_V0_25',
        'classification': cls, 'effect': '+0/+0',
        'candidate_lane_count': len(candidates), 'eligible_lane_count': len(eligible),
        'eligible_replicates': [d['replicate'] for d in eligible], 'native_class_counts': counts,
        'minimum_eligible_lane_n': int(C['minimum_eligible_lane_n']), 'minimum_per_native_class_n': int(C['minimum_per_native_class_n']),
        'invalid': invalid, 'invariant_ok': invariant_ok, 'powered': powered,
        'primitive_response_reproducibility_ok': primitive_reproducible, 'primitive_response_metrics': primitive_metrics,
        'parent_problem_reproduced': parent_reproduced,
        'exact_target_union_node_set_safety_ok': node_set_safety,
        'exact_target_union_remedy_supported': exact_supported,
        'one_step_grid_refinement_remedy_supported': refinement_supported,
        'panel_summary': panel_summary,
        'max_requested_node_coordinate_rel_mismatch': max_lookup,
        'binary_key_count': len(set(binary_keys)), 'software_control_key_count': len(set(software_keys)),
        'direct_node_identity_count': len(set(direct_counts)), 'node_count_identity_count': len(set(node_count_records)),
        'next_stage': nxt,
        'production_h_mutated': False, 'sampling_stepsize_changed': False, 'global_65537_launched': False,
        'full_layerb_107_row_traversal_launched': False, 'covariance_read': False, 'whitening_read': False,
        'nuisance_read': False, 'relation_null_read': False, 'Wm_S3_opened': False, 'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_FORCED_BASELINE_INTERPOLATION_REMEDY_DECISION_V0_25',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], json.dumps({'classification': cls, 'eligible_lane_count': len(eligible), 'native_class_counts': counts, 'primitive_response_reproducibility_ok': primitive_reproducible, 'parent_problem_reproduced': parent_reproduced, 'exact_target_union_remedy_supported': exact_supported, 'one_step_grid_refinement_remedy_supported': refinement_supported, 'next_stage': nxt}, sort_keys=True))


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
    if a.mode == 'decision':
        decision_mode(a, C)
        return
    M24 = load_v024()
    if a.mode == 'fingerprint':
        fingerprint_mode(a, M24)
    elif a.mode == 'child':
        child_mode(a, C, M24)
    elif a.mode == 'lane':
        lane_mode(a, C, M24)


if __name__ == '__main__':
    main()
