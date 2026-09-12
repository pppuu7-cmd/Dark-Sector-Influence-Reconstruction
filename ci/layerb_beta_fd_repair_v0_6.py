#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, statistics, struct
from pathlib import Path
import numpy as np

LOOKUP = 1e-12

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def f64(h):
    return struct.unpack('>d', bytes.fromhex(h))[0]

def rel(a, b):
    return abs(a-b) / max(abs(a), abs(b), np.finfo(np.float64).tiny)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def transfer_exact(jj, c, nodes, z):
    tk = c.get_transfer(z=float(z), output_format='class')
    dm = [q for q in tk if q.strip() == 'd_m']
    if len(dm) != 1:
        raise RuntimeError('exact d_m key missing')
    kkey = None
    scale = None
    for q in tk:
        s = q.lower().replace(' ', '')
        if s in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in s and 'h/mpc' in s):
            kkey = q
            scale = float(c.h())
            break
        if s in {'k(1/mpc)','k[1/mpc]'} or ('k' in s and '1/mpc' in s):
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
    if sha(a.probes) != C['probe_manifest_sha256']:
        raise RuntimeError('probe manifest sha mismatch')
    if sha(a.executor) != C['executor_sha256']:
        raise RuntimeError('executor sha mismatch')
    if jj.REL_TOL != C['relative_tolerance'] or jj.NATIVE_KPD != C['native_k_per_decade_for_pk']:
        raise RuntimeError('frozen constants mismatch')
    if C['production_h'] != jj.H:
        raise RuntimeError('production h identity mismatch')
    hs = [float(x) for x in C['h_values']]
    if hs != [4e-4, 2e-4, 1e-4, 5e-5, 2.5e-5]:
        raise RuntimeError('unexpected h grid')
    h0 = float(C['production_h'])
    if [h0*4, h0*2, h0, h0/2, h0/4] != hs:
        raise RuntimeError('h grid is not nested around production h')
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
    from classy import Class
    responses = {(f64(x['z']), f64(x['k'])): {} for x in rows}
    max_lookup = 0.0
    kkeys = set()
    solver_count = 0
    for h in hs:
        models = {}
        try:
            for label, beta in [('plus', h), ('minus', -h)]:
                c = Class()
                c.set(jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, nodes))
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
        raw_spread = max(rel(mags[i], mags[j]) for i in range(len(mags)) for j in range(i+1, len(mags)))
        rich = {}
        for i in range(len(hs)-1):
            hc, hf = hs[i], hs[i+1]
            if not math.isclose(hc, 2.0*hf, rel_tol=0.0, abs_tol=1e-20):
                raise RuntimeError('non-nested Richardson pair')
            dc = signed[format(hc, '.17g')]
            df = signed[format(hf, '.17g')]
            rich[f'{format(hc,".17g")}->{format(hf,".17g")}'] = (4.0*df-dc)/3.0
        rprod = rich[f'{format(h0,".17g")}->{format(h0/2,".17g")}']
        rfine = rich[f'{format(h0/2,".17g")}->{format(h0/4,".17g")}']
        repair_local = rel(abs(rprod), abs(rfine))
        rich_mags = [abs(v) for v in rich.values()]
        rich_spread = max(rel(rich_mags[i], rich_mags[j]) for i in range(len(rich_mags)) for j in range(i+1, len(rich_mags)))
        coarse_ref = float(x['c'])
        fine_ref = float(x['f'])
        candidate = abs(rprod)
        outrows.append({
            'kind': x['kind'], 'd': x['d'], 'z': x['z'], 'k': x['k'],
            'z_value': z, 'k_value': k,
            'signed_centered_d2_by_h': signed,
            'raw_magnitude_h_spread': raw_spread,
            'signed_richardson_d4_by_nested_pair': rich,
            'production_neighborhood_repaired_magnitude': candidate,
            'finer_neighborhood_repaired_magnitude': abs(rfine),
            'repair_local_spread': repair_local,
            'richardson_full_spread': rich_spread,
            'repair_improvement_ratio': repair_local/max(raw_spread, np.finfo(np.float64).tiny),
            'repaired_closer_to_fine_than_coarse': rel(candidate, fine_ref) < rel(candidate, coarse_ref),
            'coarse_reference': coarse_ref, 'fine_reference': fine_ref
        })
    result = {
        'schema': 'LAYERB_BETA_FD_REPAIR_DOMAIN_RESULT_V0_6',
        'domain': a.domain, 'effect': '+0/+0',
        'h_values': hs, 'production_h': h0, 'relative_tolerance': C['relative_tolerance'],
        'repair': 'Richardson extrapolation of centered D2: D4(h)=(4*D2(h/2)-D2(h))/3',
        'candidate_uses_production_h_and_half_h': True,
        'validation_uses_half_h_and_quarter_h': True,
        'class_solver_invoked': True, 'solver_construction_count': solver_count,
        'support_cubic_interpolation_used': False,
        'exact_target_k_inserted_via_k_output_values': True,
        'unique_node_count': len(nodes), 'unique_z_count': len(zs), 'row_count': len(outrows),
        'max_exact_target_binding_relative_mismatch': max_lookup,
        'native_transfer_k_keys': sorted(kkeys),
        'production_h_mutated': False, 'global_65537_launched': False,
        'covariance_read': False, 'whitening_read': False, 'nuisance_read': False,
        'relation_null_read': False, 'Wm_S3_opened': False, 'science_gate_opened': False,
        'rows': outrows, 'token': 'PASS_LAYERB_BETA_FD_REPAIR_DOMAIN_V0_6'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(result['token'], a.domain, len(outrows), solver_count, max_lookup)

def decision_mode(a, C):
    rows = []
    exact = []
    for p in a.inputs:
        d = json.load(open(p))
        if d['token'] != 'PASS_LAYERB_BETA_FD_REPAIR_DOMAIN_V0_6':
            raise RuntimeError('domain token mismatch')
        rows.extend(d['rows'])
        exact.append(float(d['max_exact_target_binding_relative_mismatch']))
    F = [r for r in rows if r['kind'] == 'F']
    K = [r for r in rows if r['kind'] == 'C']
    if len(F) != C['probe_counts']['unique_failing_zk_coordinates'] or len(K) != C['probe_counts']['unique_control_zk_coordinates']:
        raise RuntimeError('probe counts mismatch')
    if len({(r['z'], r['k']) for r in F}) != len(F) or len({(r['z'], r['k']) for r in K}) != len(K):
        raise RuntimeError('duplicate decision rows')
    tol = float(C['relative_tolerance'])
    raw_sig = [r for r in F if r['raw_magnitude_h_spread'] >= tol]
    recovered = [r for r in raw_sig if r['repair_local_spread'] < tol]
    recovery_fraction = len(recovered)/len(raw_sig) if raw_sig else 0.0
    control_raw_max = max(r['raw_magnitude_h_spread'] for r in K)
    control_repair_max = max(r['repair_local_spread'] for r in K)
    bind = max(exact)
    parent_reproduced = len(raw_sig) == int(C['expected_parent_h_unstable_failure_coordinates'])
    finite = all(
        math.isfinite(v)
        for r in rows
        for v in (
            r['raw_magnitude_h_spread'], r['repair_local_spread'], r['richardson_full_spread'],
            r['production_neighborhood_repaired_magnitude'], r['finer_neighborhood_repaired_magnitude']
        )
    )
    invariant_ok = bind <= C['exact_target_binding_tolerance'] and finite and parent_reproduced and control_raw_max < tol and control_repair_max < tol
    if not invariant_ok:
        cls = 'FD_REPAIR_VALIDATION_INCONCLUSIVE'
    elif recovery_fraction >= C['strong_support_fraction']:
        cls = 'FOURTH_ORDER_FD_REPAIR_STRONGLY_SUPPORTED'
    elif recovery_fraction >= C['mixed_support_fraction']:
        cls = 'FOURTH_ORDER_FD_REPAIR_PARTIALLY_SUPPORTED'
    else:
        cls = 'FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED'
    next_stage = {
        'FOURTH_ORDER_FD_REPAIR_STRONGLY_SUPPORTED': 'PROSPECTIVELY_FROZEN_REPAIRED_DIRECT_K_TO_COMMON_GRID_LOCAL_VALIDATION',
        'FOURTH_ORDER_FD_REPAIR_PARTIALLY_SUPPORTED': 'PROSPECTIVELY_FROZEN_LOCALIZED_RESPONSE_SOLVER_CONDITIONING_AUDIT',
        'FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED': 'PROSPECTIVELY_FROZEN_UPSTREAM_RESPONSE_SOLVER_CONDITIONING_AUDIT',
        'FD_REPAIR_VALIDATION_INCONCLUSIVE': 'NO_SCIENTIFIC_PROMOTION'
    }[cls]
    out = {
        'schema': 'LAYERB_BETA_FD_REPAIR_DECISION_V0_6',
        'classification': cls, 'effect': '+0/+0',
        'unique_failure_coordinates': len(F), 'unique_control_coordinates': len(K),
        'expected_parent_h_unstable_failure_coordinates': C['expected_parent_h_unstable_failure_coordinates'],
        'reproduced_parent_h_unstable_failure_coordinates': len(raw_sig),
        'recovered_h_unstable_failure_coordinates': len(recovered),
        'recovery_fraction': recovery_fraction,
        'strong_support_fraction': C['strong_support_fraction'],
        'mixed_support_fraction': C['mixed_support_fraction'],
        'failure_median_raw_h_spread': statistics.median(r['raw_magnitude_h_spread'] for r in F),
        'failure_median_repair_local_spread': statistics.median(r['repair_local_spread'] for r in F),
        'failure_max_repair_local_spread': max(r['repair_local_spread'] for r in F),
        'control_max_raw_h_spread': control_raw_max,
        'control_max_repair_local_spread': control_repair_max,
        'repaired_closer_to_fine_fraction_all_failures': sum(r['repaired_closer_to_fine_than_coarse'] for r in F)/len(F),
        'max_exact_target_binding_relative_mismatch': bind,
        'parent_h_dependence_reproduced': parent_reproduced,
        'invariant_ok': invariant_ok,
        'production_h': C['production_h'], 'relative_tolerance': tol,
        'production_h_mutated': False, 'global_65537_launched': False,
        'covariance_read': False, 'Wm_S3_opened': False, 'science_gate_opened': False,
        'next_stage': next_stage,
        'token': 'PASS_LAYERB_BETA_FD_REPAIR_DECISION_V0_6'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(out['token'], json.dumps(out, sort_keys=True))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', choices=['domain','decision'], required=True)
    ap.add_argument('--domain', choices=['D','B'])
    ap.add_argument('--probes')
    ap.add_argument('--contract', required=True)
    ap.add_argument('--jj-script')
    ap.add_argument('--baseline')
    ap.add_argument('--precision')
    ap.add_argument('--executor', default=__file__)
    ap.add_argument('--inputs', nargs='*')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    C = json.load(open(a.contract))
    if a.mode == 'domain':
        required = [a.domain, a.probes, a.jj_script, a.baseline, a.precision]
        if not all(required):
            raise RuntimeError('domain mode missing required arguments')
        P = json.load(open(a.probes))
        jj = load('jj_fd_v06', a.jj_script)
        domain_mode(a, C, P, jj)
    else:
        if not a.inputs:
            raise RuntimeError('decision mode requires --inputs')
        decision_mode(a, C)

if __name__ == '__main__':
    main()
