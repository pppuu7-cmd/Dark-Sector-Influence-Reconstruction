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


def key(r):
    return (r['kind'], r['d'], r['z'], r['k'])


def profile_metrics(rows, unstable_keys, tol):
    rmap = {key(r): r for r in rows}
    if not unstable_keys.issubset(rmap):
        raise RuntimeError('missing frozen parent-unstable coordinate')
    u = [rmap[k] for k in unstable_keys]
    c = [r for r in rows if r['kind'] == 'C']
    rec = sum(float(r['raw_magnitude_h_spread']) < tol for r in u)
    median = statistics.median(float(r['raw_magnitude_h_spread']) for r in u)
    control_max = max(float(r['raw_magnitude_h_spread']) for r in c)
    return {
        'parent_unstable_count': len(u),
        'recovered_count': rec,
        'recovery_fraction': rec / len(u),
        'median_parent_unstable_h_spread': median,
        'control_max_h_spread': control_max,
        'controls_stable': control_max < tol,
    }


def decision_mode(a, C):
    tol = float(C['relative_tolerance'])
    # Production/raw parent from V0.6 defines the immutable 20-coordinate subset.
    raw_rows = []
    for p in a.parent_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_FD_REPAIR_DOMAIN_V0_6':
            raise RuntimeError('parent V0.6 token mismatch')
        raw_rows.extend(d['rows'])
    if len({key(r) for r in raw_rows}) != C['probe_counts']['unique_all_zk_coordinates']:
        raise RuntimeError('parent coordinate count mismatch')
    fail = [r for r in raw_rows if r['kind'] == 'F']
    controls = [r for r in raw_rows if r['kind'] == 'C']
    unstable = [r for r in fail if float(r['raw_magnitude_h_spread']) >= tol]
    if len(unstable) != C['expected_parent_h_unstable_failure_coordinates']:
        raise RuntimeError('frozen unstable subset mismatch')
    unstable_keys = {key(r) for r in unstable}
    metrics = {
        'PROD': profile_metrics(raw_rows, unstable_keys, tol)
    }

    # Reuse terminal V0.7 tolerance-only artifacts, never recompute them.
    reused = {}
    for p in a.reused_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_SOLVER_CONDITIONING_DOMAIN_V0_7':
            raise RuntimeError('reused V0.7 token mismatch')
        prof = d['profile']
        if prof in C['reused_profiles']:
            reused.setdefault(prof, []).append(d)
    if set(reused) != set(C['reused_profiles']):
        raise RuntimeError('reused profile set mismatch')
    for prof in C['reused_profiles']:
        docs = reused[prof]
        if sorted(d['domain'] for d in docs) != ['B', 'D']:
            raise RuntimeError(f'reused {prof} domain set mismatch')
        rows = [r for d in docs for r in d['rows']]
        metrics[prof] = profile_metrics(rows, unstable_keys, tol)

    # New V0.8 profiles.
    new = {}
    max_lookup = 0.0
    for p in a.new_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_SOLVER_CONDITIONING_DOMAIN_V0_7':
            raise RuntimeError('new domain token mismatch')
        prof = d['profile']
        if prof in C['profiles']:
            new.setdefault(prof, []).append(d)
            max_lookup = max(max_lookup, float(d['max_exact_target_binding_relative_mismatch']))
    if set(new) != set(C['profiles']):
        raise RuntimeError('new profile set mismatch')
    for prof in C['profiles']:
        docs = new[prof]
        if sorted(d['domain'] for d in docs) != ['B', 'D']:
            raise RuntimeError(f'new {prof} domain set mismatch')
        rows = [r for d in docs for r in d['rows']]
        metrics[prof] = profile_metrics(rows, unstable_keys, tol)

    order = C['tolerance_order']
    if set(order) != set(metrics):
        raise RuntimeError('tolerance-order/profile mismatch')
    # Bind known tolerance values exactly and compute deterministic candidate rules.
    for prof in order:
        metrics[prof]['tol_perturb_integration'] = float(C['all_tolerances'][prof])
        metrics[prof]['median_reduction_factor_vs_production'] = (
            metrics['PROD']['median_parent_unstable_h_spread'] /
            max(metrics[prof]['median_parent_unstable_h_spread'], np.finfo(np.float64).tiny)
        )
        metrics[prof]['adequate'] = (
            prof != 'PROD' and
            metrics[prof]['controls_stable'] and
            metrics[prof]['recovery_fraction'] >= C['adequate_recovery_fraction'] and
            metrics[prof]['median_parent_unstable_h_spread'] < C['adequate_median_h_spread']
        )

    # Tighter tolerance must not materially worsen median or lose >1 recovered coordinate.
    adjacent = []
    monotonic_sane = True
    for loose, tight in zip(order, order[1:]):
        med_ok = metrics[tight]['median_parent_unstable_h_spread'] <= C['adjacent_median_worsening_factor'] * metrics[loose]['median_parent_unstable_h_spread']
        rec_ok = metrics[tight]['recovered_count'] >= metrics[loose]['recovered_count'] - C['adjacent_recovered_count_loss_allowance']
        adjacent.append({'looser': loose, 'tighter': tight, 'median_sane': med_ok, 'recovery_sane': rec_ok})
        monotonic_sane = monotonic_sane and med_ok and rec_ok

    candidate = None
    # Least strict adequate profile whose entire tighter suffix remains adequate and locally sane.
    for i, prof in enumerate(order[1:], start=1):
        suffix = order[i:]
        suffix_adj = adjacent[i:]  # comparisons prof->next and tighter
        if all(metrics[p]['adequate'] for p in suffix) and all(x['median_sane'] and x['recovery_sane'] for x in suffix_adj):
            candidate = prof
            break

    finite = all(
        math.isfinite(float(v))
        for p in metrics.values()
        for k2, v in p.items()
        if isinstance(v, (int, float)) and not isinstance(v, bool)
    )
    all_controls = all(p['controls_stable'] for p in metrics.values())
    invariant_ok = (
        finite and all_controls and
        len(fail) == C['probe_counts']['unique_failing_zk_coordinates'] and
        len(controls) == C['probe_counts']['unique_control_zk_coordinates'] and
        max_lookup <= C['exact_target_binding_tolerance']
    )
    strictest = order[-1]
    if not invariant_ok:
        cls = 'TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE'
    elif candidate is not None:
        cls = 'TOLERANCE_ONLY_STABLE_PROFILE_IDENTIFIED'
    elif metrics[strictest]['adequate']:
        cls = 'TOLERANCE_ONLY_NONMONOTONIC_OR_UNSTABLE_THRESHOLD'
    elif monotonic_sane:
        cls = 'TOLERANCE_ONLY_NO_ADEQUATE_PROFILE_WITHIN_SWEEP'
    else:
        cls = 'TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE'

    next_stage = {
        'TOLERANCE_ONLY_STABLE_PROFILE_IDENTIFIED': 'PROSPECTIVELY_FROZEN_STABILIZED_TOLERANCE_LOCAL_COMMON_GRID_VALIDATION',
        'TOLERANCE_ONLY_NO_ADEQUATE_PROFILE_WITHIN_SWEEP': 'PROSPECTIVELY_FROZEN_COORDINATE_LOCAL_RESPONSE_REGULARITY_AUDIT',
        'TOLERANCE_ONLY_NONMONOTONIC_OR_UNSTABLE_THRESHOLD': 'PROSPECTIVELY_FROZEN_TOLERANCE_INTERACTION_REPRODUCIBILITY_AUDIT',
        'TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE': 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_INVARIANT_OR_TOLERANCE_SWEEP',
    }[cls]
    out = {
        'schema': 'LAYERB_BETA_TOLERANCE_KNOB_ISOLATION_DECISION_V0_8',
        'classification': cls,
        'effect': '+0/+0',
        'candidate_profile': candidate,
        'candidate_tolerance': None if candidate is None else float(C['all_tolerances'][candidate]),
        'tolerance_order': order,
        'profiles': metrics,
        'adjacent_checks': adjacent,
        'monotonic_sane': monotonic_sane,
        'all_controls_stable': all_controls,
        'max_exact_target_binding_relative_mismatch_new_profiles': max_lookup,
        'invariant_ok': invariant_ok,
        'production_h': C['production_h'],
        'production_h_mutated': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'next_stage': next_stage,
        'token': 'PASS_LAYERB_BETA_TOLERANCE_KNOB_ISOLATION_DECISION_V0_8'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(out['token'], json.dumps(out, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', choices=['domain', 'decision'], required=True)
    ap.add_argument('--domain', choices=['D', 'B'])
    ap.add_argument('--profile')
    ap.add_argument('--probes')
    ap.add_argument('--contract', required=True)
    ap.add_argument('--v07-executor', required=True)
    ap.add_argument('--jj-script')
    ap.add_argument('--baseline')
    ap.add_argument('--precision')
    ap.add_argument('--parent-inputs', nargs='*')
    ap.add_argument('--reused-inputs', nargs='*')
    ap.add_argument('--new-inputs', nargs='*')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    C = json.load(open(a.contract))
    if a.mode == 'domain':
        if not all([a.domain, a.profile, a.probes, a.jj_script, a.baseline, a.precision]):
            raise RuntimeError('domain mode missing required arguments')
        v07 = load('v07_domain_engine', a.v07_executor)
        P = json.load(open(a.probes))
        jj = load('jj_tol_v08', a.jj_script)
        v07.domain_mode(a, C, P, jj)
    else:
        if not a.parent_inputs or not a.reused_inputs or not a.new_inputs:
            raise RuntimeError('decision mode missing required inputs')
        decision_mode(a, C)


if __name__ == '__main__':
    main()
