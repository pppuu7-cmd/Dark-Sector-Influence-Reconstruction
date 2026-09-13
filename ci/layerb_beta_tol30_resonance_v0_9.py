#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, statistics
from pathlib import Path
import numpy as np


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot import {path}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def krow(r):
    return (r['kind'], r['d'], r['z'], r['k'])


def domain_mode(a, C):
    if a.profile not in C['profiles']:
        raise RuntimeError(f'unknown profile {a.profile}')
    scope = C['profiles'][a.profile]['scope']
    v07 = load('v07_engine_v09', a.v07_executor)
    jj = load('jj_v09', a.jj_script)
    P = json.load(open(a.probes))
    if scope == 'controls':
        P = dict(P)
        P['items'] = [x for x in P['items'] if x['kind'] == 'C']
    elif scope != 'all':
        raise RuntimeError(f'unknown scope {scope}')
    v07.domain_mode(a, C, P, jj)
    d = json.load(open(a.out))
    d['schema'] = 'LAYERB_BETA_TOL30_RESONANCE_DOMAIN_RESULT_V0_9'
    d['scope'] = scope
    d['token'] = 'PASS_LAYERB_BETA_TOL30_RESONANCE_DOMAIN_V0_9'
    Path(a.out).write_text(json.dumps(d, indent=2, sort_keys=True)+'\n')
    print(d['token'], a.profile, a.domain, scope, d['row_count'], d['max_exact_target_binding_relative_mismatch'])


def assemble_profile(docs, expected_domains=('B','D')):
    if sorted(d['domain'] for d in docs) != sorted(expected_domains):
        raise RuntimeError('profile domain set mismatch')
    rows = [r for d in docs for r in d['rows']]
    return rows, max(float(d['max_exact_target_binding_relative_mismatch']) for d in docs)


def control_metrics(rows, tol):
    if any(r['kind'] != 'C' for r in rows):
        raise RuntimeError('control profile contains non-control row')
    rmap = {krow(r): r for r in rows}
    unstable = {k for k,r in rmap.items() if float(r['raw_magnitude_h_spread']) >= tol}
    return {
        'unique_control_coordinates': len(rmap),
        'unstable_control_count': len(unstable),
        'unstable_control_keys': [list(k) for k in sorted(unstable)],
        'control_max_h_spread': max(float(r['raw_magnitude_h_spread']) for r in rmap.values()),
        'controls_stable': len(unstable) == 0,
    }, unstable


def full_metrics(rows, parent_unstable_keys, tol):
    rmap = {krow(r): r for r in rows}
    if not parent_unstable_keys.issubset(rmap):
        raise RuntimeError('full replicate missing parent unstable key')
    u = [rmap[k] for k in parent_unstable_keys]
    c = [r for r in rows if r['kind'] == 'C']
    rec = [r for r in u if float(r['raw_magnitude_h_spread']) < tol]
    return {
        'unique_all_coordinates': len(rmap),
        'recovered_count': len(rec),
        'recovery_fraction': len(rec)/len(u),
        'median_parent_unstable_h_spread': statistics.median(float(r['raw_magnitude_h_spread']) for r in u),
        'control_max_h_spread': max(float(r['raw_magnitude_h_spread']) for r in c),
        'controls_stable': max(float(r['raw_magnitude_h_spread']) for r in c) < tol,
    }


def decision_mode(a, C):
    tol = float(C['relative_tolerance'])
    # Immutable parent raw set from V0.6 defines the 20 h-unstable failure coordinates.
    raw = []
    for p in a.parent_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_FD_REPAIR_DOMAIN_V0_6':
            raise RuntimeError('parent token mismatch')
        raw.extend(d['rows'])
    raw_map = {krow(r): r for r in raw}
    if len(raw_map) != C['probe_counts']['unique_all_zk_coordinates']:
        raise RuntimeError('parent coordinate count mismatch')
    parent_unstable = {
        k for k,r in raw_map.items()
        if r['kind'] == 'F' and float(r['raw_magnitude_h_spread']) >= tol
    }
    if len(parent_unstable) != C['expected_parent_h_unstable_failure_coordinates']:
        raise RuntimeError('parent unstable subset mismatch')

    grouped = {}
    max_lookup = 0.0
    for p in a.new_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_TOL30_RESONANCE_DOMAIN_V0_9':
            raise RuntimeError('V0.9 token mismatch')
        grouped.setdefault(d['profile'], []).append(d)
        max_lookup = max(max_lookup, float(d['max_exact_target_binding_relative_mismatch']))
    if set(grouped) != set(C['profiles']):
        raise RuntimeError('profile set mismatch')

    controls = {}
    unstable_sets = {}
    tol300r = None
    for prof, spec in C['profiles'].items():
        rows, lookup = assemble_profile(grouped[prof])
        max_lookup = max(max_lookup, lookup)
        if spec['scope'] == 'controls':
            m, u = control_metrics(rows, tol)
            if m['unique_control_coordinates'] != C['probe_counts']['unique_control_zk_coordinates']:
                raise RuntimeError(f'{prof} control coordinate count mismatch')
            controls[prof] = m
            unstable_sets[prof] = u
        else:
            if prof != 'TOL300R':
                raise RuntimeError('unexpected full-scope profile')
            tol300r = full_metrics(rows, parent_unstable, tol)
            if tol300r['unique_all_coordinates'] != C['probe_counts']['unique_all_zk_coordinates']:
                raise RuntimeError('TOL300R full coordinate count mismatch')

    r1, r2 = unstable_sets['T30R1'], unstable_sets['T30R2']
    exact_replicas_both_violate = bool(r1) and bool(r2)
    exact_replicas_same_unstable_set = r1 == r2
    exact_replicas_reproduce = exact_replicas_both_violate and exact_replicas_same_unstable_set

    neighbor_names = C['neighbor_profiles']
    violating_neighbors = [p for p in neighbor_names if not controls[p]['controls_stable']]
    all_neighbors_stable = len(violating_neighbors) == 0
    outer_anchors_stable = controls[C['outer_loose_neighbor']]['controls_stable'] and controls[C['outer_tight_neighbor']]['controls_stable']

    parent = C['parent_tol300_metrics']
    parent_adequate = (
        parent['controls_stable'] and
        parent['recovery_fraction'] >= C['adequate_recovery_fraction'] and
        parent['median_parent_unstable_h_spread'] < C['adequate_median_h_spread']
    )
    replicate_adequate = (
        tol300r['controls_stable'] and
        tol300r['recovery_fraction'] >= C['adequate_recovery_fraction'] and
        tol300r['median_parent_unstable_h_spread'] < C['adequate_median_h_spread']
    )
    count_agree = abs(tol300r['recovered_count'] - parent['recovered_count']) <= C['tol300_recovered_count_difference_max']
    ratio = max(tol300r['median_parent_unstable_h_spread'], parent['median_parent_unstable_h_spread']) / max(min(tol300r['median_parent_unstable_h_spread'], parent['median_parent_unstable_h_spread']), np.finfo(np.float64).tiny)
    median_agree = ratio <= C['tol300_median_ratio_max']
    tol300_replicated = parent_adequate and replicate_adequate and count_agree and median_agree

    finite = math.isfinite(max_lookup) and all(
        math.isfinite(float(m['control_max_h_spread'])) for m in controls.values()
    ) and all(math.isfinite(float(v)) for k,v in tol300r.items() if isinstance(v,(int,float)) and not isinstance(v,bool))
    invariant_ok = finite and max_lookup <= C['exact_target_binding_tolerance']

    if not invariant_ok:
        cls = 'TOL30_RESONANCE_AUDIT_INCONCLUSIVE'
    elif not exact_replicas_reproduce:
        cls = 'TOL30_CONTROL_SPIKE_NOT_REPRODUCIBLE'
    elif not tol300_replicated:
        cls = 'TOL300_ADEQUACY_NOT_REPLICATED'
    elif all_neighbors_stable and outer_anchors_stable:
        cls = 'REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300'
    else:
        cls = 'REPRODUCIBLE_BROAD_TOLERANCE_CONTROL_INSTABILITY'

    next_stage = {
        'REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300': 'PROSPECTIVELY_FROZEN_STABILIZED_TOL300_LOCAL_COMMON_GRID_VALIDATION',
        'REPRODUCIBLE_BROAD_TOLERANCE_CONTROL_INSTABILITY': 'PROSPECTIVELY_FROZEN_FINE_TOLERANCE_BOUNDARY_AND_CONTROL_COORDINATE_AUDIT',
        'TOL30_CONTROL_SPIKE_NOT_REPRODUCIBLE': 'PROSPECTIVELY_FROZEN_CROSS_RUN_NUMERICAL_REPRODUCIBILITY_AUDIT',
        'TOL300_ADEQUACY_NOT_REPLICATED': 'PROSPECTIVELY_FROZEN_TOL300_REPLICATION_DIAGNOSTIC',
        'TOL30_RESONANCE_AUDIT_INCONCLUSIVE': 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_INVARIANT_FAILURE',
    }[cls]

    out = {
        'schema': 'LAYERB_BETA_TOL30_RESONANCE_DECISION_V0_9',
        'classification': cls,
        'effect': '+0/+0',
        'control_profiles': controls,
        'exact_replicas_both_violate': exact_replicas_both_violate,
        'exact_replicas_same_unstable_set': exact_replicas_same_unstable_set,
        'exact_replicas_reproduce': exact_replicas_reproduce,
        'violating_neighbor_profiles': violating_neighbors,
        'all_neighbors_stable': all_neighbors_stable,
        'outer_anchors_stable': outer_anchors_stable,
        'tol300_parent_metrics': parent,
        'tol300_replicate_metrics': tol300r,
        'tol300_parent_adequate': parent_adequate,
        'tol300_replicate_adequate': replicate_adequate,
        'tol300_recovered_count_agree': count_agree,
        'tol300_median_ratio': ratio,
        'tol300_median_agree': median_agree,
        'tol300_replicated': tol300_replicated,
        'max_exact_target_binding_relative_mismatch': max_lookup,
        'invariant_ok': invariant_ok,
        'production_h': C['production_h'],
        'production_h_mutated': False,
        'sampling_stepsize_changed': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'next_stage': next_stage,
        'token': 'PASS_LAYERB_BETA_TOL30_RESONANCE_DECISION_V0_9'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(out['token'], json.dumps(out, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', choices=['domain','decision'], required=True)
    ap.add_argument('--profile')
    ap.add_argument('--domain', choices=['D','B'])
    ap.add_argument('--probes')
    ap.add_argument('--contract', required=True)
    ap.add_argument('--v07-executor')
    ap.add_argument('--jj-script')
    ap.add_argument('--baseline')
    ap.add_argument('--precision')
    ap.add_argument('--parent-inputs', nargs='*')
    ap.add_argument('--new-inputs', nargs='*')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    C = json.load(open(a.contract))
    if a.mode == 'domain':
        if not all([a.profile,a.domain,a.probes,a.v07_executor,a.jj_script,a.baseline,a.precision]):
            raise RuntimeError('domain mode missing required args')
        domain_mode(a, C)
    else:
        if not a.parent_inputs or not a.new_inputs:
            raise RuntimeError('decision mode missing inputs')
        decision_mode(a, C)

if __name__ == '__main__':
    main()
