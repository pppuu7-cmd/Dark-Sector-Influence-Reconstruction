#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, statistics, struct
from pathlib import Path
import numpy as np


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot import {path}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def f64(h):
    return struct.unpack('>d', bytes.fromhex(h))[0]


def rel(a, b):
    return abs(a-b) / max(abs(a), abs(b), np.finfo(np.float64).tiny)


def krow(r):
    return (r['kind'], r['d'], r['z'], r['k'])


def transfer_grid(jj, c, nodes, targets, z):
    tk = c.get_transfer(z=float(z), output_format='class')
    dm = [q for q in tk if q.strip() == 'd_m']
    if len(dm) != 1:
        raise RuntimeError('exact d_m key missing')
    kkey = None
    scale = None
    for q in tk:
        s = q.lower().replace(' ', '')
        if s in {'k(h/mpc)', 'k[h/mpc]', 'k_h/mpc'} or ('k' in s and 'h/mpc' in s):
            kkey = q
            scale = float(c.h())
            break
        if s in {'k(1/mpc)', 'k[1/mpc]'} or ('k' in s and '1/mpc' in s):
            kkey = q
            scale = 1.0
            break
    if kkey is None:
        raise RuntimeError('unrecognized CLASS k key')
    k = np.asarray(tk[kkey], dtype=np.float64) * scale
    y = np.asarray(tk[dm[0]], dtype=np.float64)
    if k.ndim != 1 or y.shape != k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k <= 0) or np.any(np.diff(k) <= 0):
        raise RuntimeError('invalid transfer table')
    yn, mx = jj.requested_values(k, y, nodes)
    vals, valid = jj.cubic_centered(nodes, yn, np.asarray(targets, dtype=np.float64))
    return vals, valid, float(mx), str(kkey)


def domain_mode(a, C, P, jj):
    if a.grid not in C['grids']:
        raise RuntimeError(f'unknown frozen grid {a.grid}')
    if jj.H != C['production_h'] or jj.REL_TOL != C['relative_tolerance'] or jj.NATIVE_KPD != C['native_k_per_decade_for_pk']:
        raise RuntimeError('frozen response constants mismatch')
    base_n = int(C['grids'][a.grid]['base_n'])
    nodes, ratio, nlo, nhi = jj.guarded_lattice(base_n)
    exp = C['grids'][a.grid]
    if [nlo, nhi, len(nodes)] != [exp['lower_guard_count'], exp['upper_guard_count'], exp['requested_node_count']]:
        raise RuntimeError('guarded lattice geometry mismatch')
    source = [x for x in P['items'] if x['d'] == a.domain]
    uniq = {}
    for x in source:
        key = (x['kind'], x['z'], x['k'])
        if key in uniq:
            if uniq[key]['c'] != x['c'] or uniq[key]['f'] != x['f']:
                raise RuntimeError('duplicate probe mismatch')
        else:
            uniq[key] = x
    rows = list(uniq.values())
    hs = [float(x) for x in C['h_values']]
    zs = sorted(set(f64(x['z']) for x in rows))
    targets_by_z = {
        z: np.asarray(sorted(set(f64(x['k']) for x in rows if f64(x['z']) == z)), dtype=np.float64)
        for z in zs
    }
    responses = {(f64(x['z']), f64(x['k'])): {} for x in rows}
    from classy import Class
    solver_count = 0
    max_lookup = 0.0
    kkeys = set()
    unsupported = 0
    for h in hs:
        models = {}
        try:
            for label, beta in [('plus', h), ('minus', -h)]:
                params = jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, nodes)
                params['tol_perturb_integration'] = C['tol300_override']
                c = Class()
                c.set(params)
                c.compute(['transfer'])
                models[label] = c
                solver_count += 1
            for z in zs:
                targets = targets_by_z[z]
                bp, vp, m1, k1 = transfer_grid(jj, models['plus'], nodes, targets, z)
                bm, vm, m2, k2 = transfer_grid(jj, models['minus'], nodes, targets, z)
                valid = vp & vm
                unsupported += int(np.count_nonzero(~valid))
                max_lookup = max(max_lookup, m1, m2)
                kkeys.update((k1, k2))
                if not np.all(valid):
                    continue
                for i, k in enumerate(targets):
                    responses[(z, float(k))][format(h, '.17g')] = float(bp[i] - bm[i]) / (2*h)
        finally:
            for c in models.values():
                try:
                    c.struct_cleanup()
                except Exception:
                    pass
    outrows = []
    hkeys = [format(h, '.17g') for h in hs]
    for x in rows:
        z = f64(x['z']); k = f64(x['k'])
        signed = responses[(z, k)]
        if set(signed) != set(hkeys):
            raise RuntimeError('missing common-grid response at frozen coordinate')
        vals = [signed[q] for q in hkeys]
        if not all(math.isfinite(v) for v in vals):
            raise RuntimeError('nonfinite response')
        mags = [abs(v) for v in vals]
        spread = max(rel(mags[i], mags[j]) for i in range(len(mags)) for j in range(i+1, len(mags)))
        outrows.append({
            'kind': x['kind'], 'd': x['d'], 'z': x['z'], 'k': x['k'],
            'z_value': z, 'k_value': k,
            'signed_centered_d2_by_h': signed,
            'raw_magnitude_h_spread': spread,
        })
    out = {
        'schema': 'LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_DOMAIN_RESULT_V0_10',
        'grid': a.grid,
        'base_n': base_n,
        'domain': a.domain,
        'effect': '+0/+0',
        'tol_perturb_integration': float(C['tol300']),
        'production_h': C['production_h'],
        'h_values': hs,
        'relative_tolerance': C['relative_tolerance'],
        'common_grid_used': True,
        'direct_target_k_insertion_for_science_response': False,
        'guarded_lattice': {
            'base_n': base_n,
            'ratio_binary64': float(ratio),
            'lower_guard_count': nlo,
            'upper_guard_count': nhi,
            'requested_node_count': len(nodes),
            'extended_k_min': float(nodes[0]),
            'extended_k_max': float(nodes[-1])
        },
        'cubic_log_k_interpolation_used': True,
        'unsupported_target_evaluations': unsupported,
        'max_requested_node_coordinate_rel_mismatch': max_lookup,
        'solver_construction_count': solver_count,
        'native_transfer_k_keys': sorted(kkeys),
        'row_count': len(outrows),
        'rows': outrows,
        'production_h_mutated': False,
        'sampling_stepsize_changed': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_DOMAIN_V0_10'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(out['token'], a.grid, a.domain, len(outrows), unsupported, max_lookup)


def metrics(rows, unstable_keys, tol):
    rmap = {krow(r): r for r in rows}
    if not unstable_keys.issubset(rmap):
        raise RuntimeError('missing parent unstable coordinate')
    u = [rmap[k] for k in unstable_keys]
    c = [r for r in rows if r['kind'] == 'C']
    recovered = [r for r in u if float(r['raw_magnitude_h_spread']) < tol]
    return {
        'unique_all_coordinates': len(rmap),
        'recovered_count': len(recovered),
        'recovery_fraction': len(recovered)/len(u),
        'median_parent_unstable_h_spread': statistics.median(float(r['raw_magnitude_h_spread']) for r in u),
        'control_max_h_spread': max(float(r['raw_magnitude_h_spread']) for r in c),
        'controls_stable': max(float(r['raw_magnitude_h_spread']) for r in c) < tol,
    }, rmap


def response_max_rel(a_map, b_map, hkeys):
    if set(a_map) != set(b_map):
        raise RuntimeError('coordinate keyset mismatch')
    worst = 0.0
    worst_key = None
    worst_h = None
    for k in sorted(a_map):
        aa = a_map[k]['signed_centered_d2_by_h']
        bb = b_map[k]['signed_centered_d2_by_h']
        if set(aa) != set(hkeys) or set(bb) != set(hkeys):
            raise RuntimeError('h keyset mismatch')
        for h in hkeys:
            rr = rel(float(aa[h]), float(bb[h]))
            if rr > worst:
                worst, worst_key, worst_h = rr, k, h
    return worst, None if worst_key is None else list(worst_key), worst_h


def decision_mode(a, C):
    tol = float(C['relative_tolerance'])
    raw = []
    for p in a.parent_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_FD_REPAIR_DOMAIN_V0_6':
            raise RuntimeError('raw parent token mismatch')
        raw.extend(d['rows'])
    raw_map = {krow(r): r for r in raw}
    if len(raw_map) != C['probe_counts']['unique_all_zk_coordinates']:
        raise RuntimeError('raw parent coordinate count mismatch')
    unstable = {
        k for k,r in raw_map.items()
        if r['kind'] == 'F' and float(r['raw_magnitude_h_spread']) >= tol
    }
    if len(unstable) != C['expected_parent_h_unstable_failure_coordinates']:
        raise RuntimeError('parent unstable subset mismatch')

    direct_docs = []
    for p in a.direct_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_TOL30_RESONANCE_DOMAIN_V0_9' or d['profile'] != 'TOL300R':
            raise RuntimeError('direct TOL300R provenance mismatch')
        direct_docs.append(d)
    if sorted(d['domain'] for d in direct_docs) != ['B','D']:
        raise RuntimeError('direct TOL300R domains mismatch')
    direct_rows = [r for d in direct_docs for r in d['rows']]
    direct_m, direct_map = metrics(direct_rows, unstable, tol)

    grouped = {}
    max_lookup = 0.0
    unsupported = 0
    for p in a.grid_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_DOMAIN_V0_10':
            raise RuntimeError('grid result token mismatch')
        grouped.setdefault(d['grid'], []).append(d)
        max_lookup = max(max_lookup, float(d['max_requested_node_coordinate_rel_mismatch']))
        unsupported += int(d['unsupported_target_evaluations'])
    if set(grouped) != set(C['grids']):
        raise RuntimeError('grid set mismatch')

    gm = {}; maps = {}; keysets_exact = True
    for grid in C['grids']:
        docs = grouped[grid]
        if sorted(d['domain'] for d in docs) != ['B','D']:
            raise RuntimeError(f'{grid} domain set mismatch')
        rows = [r for d in docs for r in d['rows']]
        m, rmap = metrics(rows, unstable, tol)
        exact = set(rmap) == set(raw_map)
        keysets_exact = keysets_exact and exact
        m['coordinate_keyset_exact'] = exact
        m['adequate'] = (
            m['controls_stable'] and
            m['recovery_fraction'] >= C['adequate_recovery_fraction'] and
            m['median_parent_unstable_h_spread'] < C['adequate_median_h_spread']
        )
        gm[grid] = m; maps[grid] = rmap

    hkeys = [format(float(h), '.17g') for h in C['h_values']]
    coarse = C['coarse_grid']; fine = C['fine_grid']
    grid_max_rel, grid_worst_key, grid_worst_h = response_max_rel(maps[coarse], maps[fine], hkeys)
    prod_h_key = format(float(C['production_h']), '.17g')
    fine_direct_max_rel, fine_direct_worst_key, _ = response_max_rel(
        {k:{'signed_centered_d2_by_h':{prod_h_key:v['signed_centered_d2_by_h'][prod_h_key]}} for k,v in maps[fine].items()},
        {k:{'signed_centered_d2_by_h':{prod_h_key:v['signed_centered_d2_by_h'][prod_h_key]}} for k,v in direct_map.items()},
        [prod_h_key]
    )
    count_agree = abs(gm[fine]['recovered_count'] - direct_m['recovered_count']) <= C['direct_recovered_count_difference_max']
    med_ratio = max(gm[fine]['median_parent_unstable_h_spread'], direct_m['median_parent_unstable_h_spread']) / max(min(gm[fine]['median_parent_unstable_h_spread'], direct_m['median_parent_unstable_h_spread']), np.finfo(np.float64).tiny)
    median_agree = med_ratio <= C['direct_median_ratio_max']

    finite = all(math.isfinite(float(x)) for x in [max_lookup, grid_max_rel, fine_direct_max_rel, med_ratio])
    invariant_ok = (
        finite and keysets_exact and unsupported == 0 and
        max_lookup <= C['exact_target_binding_tolerance'] and
        direct_m['unique_all_coordinates'] == C['probe_counts']['unique_all_zk_coordinates']
    )
    validated = (
        invariant_ok and gm[coarse]['adequate'] and gm[fine]['adequate'] and
        grid_max_rel < C['common_grid_response_relative_tolerance'] and
        fine_direct_max_rel < C['fine_vs_direct_response_relative_tolerance'] and
        count_agree and median_agree
    )
    if not invariant_ok:
        cls = 'STABILIZED_TOL300_LOCAL_COMMON_GRID_VALIDATION_INCONCLUSIVE'
    elif validated:
        cls = 'STABILIZED_TOL300_LOCAL_COMMON_GRID_VALIDATED'
    else:
        cls = 'STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED'
    next_stage = {
        'STABILIZED_TOL300_LOCAL_COMMON_GRID_VALIDATED': 'PROSPECTIVELY_FROZEN_STABILIZED_TOL300_FULL_LAYERB_COMMON_GRID_REEVALUATION',
        'STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED': 'PROSPECTIVELY_FROZEN_COMMON_GRID_DISCREPANCY_LOCALIZATION_AUDIT',
        'STABILIZED_TOL300_LOCAL_COMMON_GRID_VALIDATION_INCONCLUSIVE': 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_COMMON_GRID_INVARIANT_FAILURE'
    }[cls]
    out = {
        'schema': 'LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_DECISION_V0_10',
        'classification': cls,
        'effect': '+0/+0',
        'tol_perturb_integration': C['tol300'],
        'production_h': C['production_h'],
        'direct_tol300_metrics': direct_m,
        'grid_metrics': gm,
        'common_grid_max_relative_response_difference_all_h': grid_max_rel,
        'common_grid_worst_coordinate': grid_worst_key,
        'common_grid_worst_h': grid_worst_h,
        'fine_vs_direct_production_h_max_relative_response_difference': fine_direct_max_rel,
        'fine_vs_direct_worst_coordinate': fine_direct_worst_key,
        'fine_vs_direct_recovered_count_agree': count_agree,
        'fine_vs_direct_median_ratio': med_ratio,
        'fine_vs_direct_median_agree': median_agree,
        'unsupported_target_evaluations': unsupported,
        'max_requested_node_coordinate_rel_mismatch': max_lookup,
        'all_coordinate_keysets_exact': keysets_exact,
        'invariant_ok': invariant_ok,
        'production_h_mutated': False,
        'sampling_stepsize_changed': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'next_stage': next_stage,
        'token': 'PASS_LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_DECISION_V0_10'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(out['token'], json.dumps(out, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', choices=['domain','decision'], required=True)
    ap.add_argument('--grid')
    ap.add_argument('--domain', choices=['D','B'])
    ap.add_argument('--contract', required=True)
    ap.add_argument('--probes')
    ap.add_argument('--jj-script')
    ap.add_argument('--baseline')
    ap.add_argument('--precision')
    ap.add_argument('--parent-inputs', nargs='*')
    ap.add_argument('--direct-inputs', nargs='*')
    ap.add_argument('--grid-inputs', nargs='*')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    C = json.load(open(a.contract))
    if a.mode == 'domain':
        if not all([a.grid, a.domain, a.probes, a.jj_script, a.baseline, a.precision]):
            raise RuntimeError('domain mode missing arguments')
        P = json.load(open(a.probes)); jj = load('jj_v010', a.jj_script)
        domain_mode(a, C, P, jj)
    else:
        if not a.parent_inputs or not a.direct_inputs or not a.grid_inputs:
            raise RuntimeError('decision mode missing inputs')
        decision_mode(a, C)


if __name__ == '__main__':
    main()
