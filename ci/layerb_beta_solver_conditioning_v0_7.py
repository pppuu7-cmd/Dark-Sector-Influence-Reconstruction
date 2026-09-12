#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, statistics
from pathlib import Path
import numpy as np

LOOKUP = 1e-12


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot import {path}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def f64(h):
    import struct
    return struct.unpack('>d', bytes.fromhex(h))[0]


def rel(a, b):
    return abs(a-b) / max(abs(a), abs(b), np.finfo(np.float64).tiny)


def transfer_exact(jj, c, nodes, z):
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
    yn, mx = jj.requested_values(k, y, nodes)
    if mx > LOOKUP:
        raise RuntimeError(f'exact target binding failed {mx}')
    return yn, float(mx), str(kkey)


def domain_mode(a, C, P, jj):
    if a.profile not in C['profiles']:
        raise RuntimeError(f'unknown frozen profile {a.profile}')
    if jj.REL_TOL != C['relative_tolerance'] or jj.NATIVE_KPD != C['native_k_per_decade_for_pk']:
        raise RuntimeError('frozen constants mismatch')
    if jj.H != C['production_h']:
        raise RuntimeError('production h identity mismatch')
    profile = C['profiles'][a.profile]
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
    nodes = np.asarray(sorted(set(f64(x['k']) for x in rows)), dtype=np.float64)
    zs = sorted(set(f64(x['z']) for x in rows))
    hs = [float(x) for x in C['h_values']]
    from classy import Class
    responses = {(f64(x['z']), f64(x['k'])): {} for x in rows}
    max_lookup = 0.0
    kkeys = set()
    solver_count = 0
    for h in hs:
        models = {}
        try:
            for label, beta in [('plus', h), ('minus', -h)]:
                params = jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, nodes)
                for key, value in profile['overrides'].items():
                    params[str(key)] = str(value)
                c = Class()
                c.set(params)
                c.compute(['transfer'])
                models[label] = c
                solver_count += 1
            byz = {}
            for z in zs:
                bp, m1, k1 = transfer_exact(jj, models['plus'], nodes, z)
                bm, m2, k2 = transfer_exact(jj, models['minus'], nodes, z)
                max_lookup = max(max_lookup, m1, m2)
                kkeys.update((k1, k2))
                byz[z] = (bp, bm)
            idx = {float(k): i for i, k in enumerate(nodes)}
            for z, k in responses:
                bp, bm = byz[z]
                responses[(z, k)][format(h, '.17g')] = float(bp[idx[k]] - bm[idx[k]]) / (2*h)
        finally:
            for c in models.values():
                try:
                    c.struct_cleanup()
                except Exception:
                    pass
    outrows = []
    keys = [format(h, '.17g') for h in hs]
    for x in rows:
        z = f64(x['z'])
        k = f64(x['k'])
        signed = responses[(z, k)]
        vals = [signed[q] for q in keys]
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
    result = {
        'schema': 'LAYERB_BETA_SOLVER_CONDITIONING_DOMAIN_RESULT_V0_7',
        'profile': a.profile,
        'profile_overrides': profile['overrides'],
        'profile_axis': profile['axis'],
        'domain': a.domain,
        'effect': '+0/+0',
        'h_values': hs,
        'production_h': C['production_h'],
        'relative_tolerance': C['relative_tolerance'],
        'class_solver_invoked': True,
        'solver_construction_count': solver_count,
        'exact_target_k_inserted_via_k_output_values': True,
        'unique_node_count': len(nodes),
        'unique_z_count': len(zs),
        'row_count': len(outrows),
        'max_exact_target_binding_relative_mismatch': max_lookup,
        'native_transfer_k_keys': sorted(kkeys),
        'production_h_mutated': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'rows': outrows,
        'token': 'PASS_LAYERB_BETA_SOLVER_CONDITIONING_DOMAIN_V0_7'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(result['token'], a.profile, a.domain, len(outrows), solver_count, max_lookup)


def decision_mode(a, C):
    parent_rows = []
    for p in a.parent_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_FD_REPAIR_DOMAIN_V0_6':
            raise RuntimeError('parent domain token mismatch')
        parent_rows.extend(d['rows'])
    pmap = {(r['kind'], r['d'], r['z'], r['k']): r for r in parent_rows}
    if len(pmap) != C['probe_counts']['unique_all_zk_coordinates']:
        raise RuntimeError('parent probe count mismatch')
    tol = float(C['relative_tolerance'])
    parent_fail = [r for r in parent_rows if r['kind'] == 'F']
    parent_ctrl = [r for r in parent_rows if r['kind'] == 'C']
    unstable = [r for r in parent_fail if float(r['raw_magnitude_h_spread']) >= tol]
    if len(unstable) != C['expected_parent_h_unstable_failure_coordinates']:
        raise RuntimeError('parent h-unstable set mismatch')
    unstable_keys = {(r['kind'], r['d'], r['z'], r['k']) for r in unstable}
    parent_u_median = statistics.median(float(r['raw_magnitude_h_spread']) for r in unstable)

    profile_docs = {}
    max_lookup = 0.0
    for p in a.profile_inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_SOLVER_CONDITIONING_DOMAIN_V0_7':
            raise RuntimeError('profile domain token mismatch')
        prof = d['profile']
        profile_docs.setdefault(prof, []).append(d)
        max_lookup = max(max_lookup, float(d['max_exact_target_binding_relative_mismatch']))
    if set(profile_docs) != set(C['profiles']):
        raise RuntimeError('profile set mismatch')

    metrics = {}
    all_controls_stable = True
    all_keysets_exact = True
    for prof in C['profiles']:
        docs = profile_docs[prof]
        if sorted(x['domain'] for x in docs) != ['B', 'D']:
            raise RuntimeError(f'profile {prof} domain set mismatch')
        rows = [r for d in docs for r in d['rows']]
        rmap = {(r['kind'], r['d'], r['z'], r['k']): r for r in rows}
        keyset_exact = set(rmap) == set(pmap)
        all_keysets_exact = all_keysets_exact and keyset_exact
        if not keyset_exact:
            raise RuntimeError(f'profile {prof} coordinate keyset mismatch')
        new_u = [rmap[k] for k in unstable_keys]
        controls = [r for r in rows if r['kind'] == 'C']
        recovered = [r for r in new_u if float(r['raw_magnitude_h_spread']) < tol]
        median_u = statistics.median(float(r['raw_magnitude_h_spread']) for r in new_u)
        control_max = max(float(r['raw_magnitude_h_spread']) for r in controls)
        control_stable = control_max < tol
        all_controls_stable = all_controls_stable and control_stable
        metrics[prof] = {
            'parent_unstable_count': len(new_u),
            'recovered_count': len(recovered),
            'recovery_fraction': len(recovered)/len(new_u),
            'median_parent_unstable_h_spread': median_u,
            'median_reduction_factor_vs_parent': parent_u_median/max(median_u, np.finfo(np.float64).tiny),
            'control_max_h_spread': control_max,
            'controls_stable': control_stable,
            'coordinate_keyset_exact': keyset_exact,
        }

    m = metrics
    tol_axis_monotonic = m['TOL100']['median_parent_unstable_h_spread'] <= m['TOL10']['median_parent_unstable_h_spread'] <= parent_u_median
    sampling_axis_monotonic = m['SAMP4']['median_parent_unstable_h_spread'] <= m['SAMP2']['median_parent_unstable_h_spread'] <= parent_u_median
    joint = m['JOINT100_S4']
    joint_not_pathological = joint['median_parent_unstable_h_spread'] <= C['joint_pathology_factor'] * min(m['TOL100']['median_parent_unstable_h_spread'], m['SAMP4']['median_parent_unstable_h_spread'])
    finite = all(
        math.isfinite(float(v))
        for prof in m.values()
        for k, v in prof.items()
        if isinstance(v, (int, float)) and not isinstance(v, bool)
    )
    invariant_ok = (
        finite and all_controls_stable and all_keysets_exact and
        max_lookup <= C['exact_target_binding_tolerance'] and
        len(parent_ctrl) == C['probe_counts']['unique_control_zk_coordinates'] and
        len(parent_fail) == C['probe_counts']['unique_failing_zk_coordinates']
    )
    strong = (
        invariant_ok and
        joint['recovery_fraction'] >= C['strong_recovery_fraction'] and
        joint['median_reduction_factor_vs_parent'] >= C['strong_median_reduction_factor'] and
        (tol_axis_monotonic or sampling_axis_monotonic) and
        joint_not_pathological
    )
    partial = (
        invariant_ok and not strong and
        (joint['recovery_fraction'] >= C['partial_recovery_fraction'] or
         joint['median_reduction_factor_vs_parent'] >= C['partial_median_reduction_factor'])
    )
    if not invariant_ok or (max(x['recovery_fraction'] for x in m.values()) >= C['strong_recovery_fraction'] and not joint_not_pathological):
        cls = 'SOLVER_CONDITIONING_AUDIT_INCONCLUSIVE'
    elif strong:
        cls = 'UPSTREAM_RESPONSE_SOLVER_CONDITIONING_STRONGLY_SUPPORTED'
    elif partial:
        cls = 'UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED'
    else:
        cls = 'UPSTREAM_RESPONSE_SOLVER_CONDITIONING_NOT_SUPPORTED'

    tol_sensitive = tol_axis_monotonic and m['TOL100']['median_reduction_factor_vs_parent'] >= C['axis_material_reduction_factor']
    sampling_sensitive = sampling_axis_monotonic and m['SAMP4']['median_reduction_factor_vs_parent'] >= C['axis_material_reduction_factor']
    if tol_sensitive and sampling_sensitive:
        attribution = 'BOTH_TOLERANCE_AND_SAMPLING_SENSITIVE'
    elif tol_sensitive:
        attribution = 'PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE'
    elif sampling_sensitive:
        attribution = 'PERTURBATION_SAMPLING_SENSITIVE'
    else:
        attribution = 'NO_MATERIAL_AXIS_SENSITIVITY_AT_PREREGISTERED_SCALE'

    next_stage = {
        'UPSTREAM_RESPONSE_SOLVER_CONDITIONING_STRONGLY_SUPPORTED': 'PROSPECTIVELY_FROZEN_STABILIZED_SOLVER_PROFILE_LOCAL_COMMON_GRID_VALIDATION',
        'UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED': 'PROSPECTIVELY_FROZEN_LOCALIZED_SOLVER_KNOB_ISOLATION_AUDIT',
        'UPSTREAM_RESPONSE_SOLVER_CONDITIONING_NOT_SUPPORTED': 'PROSPECTIVELY_FROZEN_RESPONSE_PARAMETERIZATION_OR_MODEL_REGULARITY_AUDIT',
        'SOLVER_CONDITIONING_AUDIT_INCONCLUSIVE': 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_PROFILE_INTERACTION_OR_INVARIANT_FAILURE',
    }[cls]
    out = {
        'schema': 'LAYERB_BETA_SOLVER_CONDITIONING_DECISION_V0_7',
        'classification': cls,
        'attribution': attribution,
        'effect': '+0/+0',
        'relative_tolerance': tol,
        'production_h': C['production_h'],
        'parent_unstable_failure_coordinates': len(unstable),
        'parent_unstable_median_h_spread': parent_u_median,
        'profiles': metrics,
        'tol_axis_monotonic': tol_axis_monotonic,
        'sampling_axis_monotonic': sampling_axis_monotonic,
        'joint_not_pathological': joint_not_pathological,
        'all_controls_stable': all_controls_stable,
        'all_coordinate_keysets_exact': all_keysets_exact,
        'max_exact_target_binding_relative_mismatch': max_lookup,
        'invariant_ok': invariant_ok,
        'production_h_mutated': False,
        'global_65537_launched': False,
        'covariance_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'next_stage': next_stage,
        'token': 'PASS_LAYERB_BETA_SOLVER_CONDITIONING_DECISION_V0_7'
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
    ap.add_argument('--jj-script')
    ap.add_argument('--baseline')
    ap.add_argument('--precision')
    ap.add_argument('--parent-inputs', nargs='*')
    ap.add_argument('--profile-inputs', nargs='*')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    C = json.load(open(a.contract))
    if a.mode == 'domain':
        if not all([a.domain, a.profile, a.probes, a.jj_script, a.baseline, a.precision]):
            raise RuntimeError('domain mode missing required arguments')
        P = json.load(open(a.probes))
        jj = load('jj_solver_v07', a.jj_script)
        domain_mode(a, C, P, jj)
    else:
        if not a.parent_inputs or not a.profile_inputs:
            raise RuntimeError('decision mode missing inputs')
        decision_mode(a, C)


if __name__ == '__main__':
    main()
