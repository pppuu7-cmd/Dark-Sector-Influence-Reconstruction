#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, itertools, json, math
from pathlib import Path
import numpy as np


def load(name, path):
    s = importlib.util.spec_from_file_location(name, Path(path))
    if s is None or s.loader is None:
        raise RuntimeError(f'cannot import {path}')
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def f64hex(h):
    import struct
    return struct.unpack('>d', bytes.fromhex(h))[0]


def rel(a, b):
    return abs(a-b) / max(abs(a), abs(b), np.finfo(np.float64).tiny)


def run_lane(a, C):
    if a.grid not in C['grids'] or a.profile not in C['profiles']:
        raise RuntimeError('unfrozen lane')
    v12 = load('v12', a.v12_executor)
    jj = load('jj', a.jj_script)
    exp = C['grids'][a.grid]
    common, ratio, nlo, nhi = jj.guarded_lattice(int(exp['base_n']))
    if [nlo, nhi, len(common)] != [exp['lower_guard_count'], exp['upper_guard_count'], exp['requested_node_count']]:
        raise RuntimeError('grid identity mismatch')
    target_ks = np.asarray(sorted({f64hex(x['k']) for x in C['targets']}), dtype=np.float64)
    mixed = np.asarray(sorted(set(float(x) for x in common).union(float(x) for x in target_ks)), dtype=np.float64)
    lane_cells = [x for x in C['diagnostic_cells'] if x['grid'] == a.grid]
    hs = sorted({float(x['h']) for x in lane_cells}, reverse=True)
    repeat_count = int(C['repeat_count'])
    from classy import Class
    repeats = []
    max_lookup = 0.0
    solver_count = 0
    for rep in range(1, repeat_count + 1):
        rep_cells = []
        for h in hs:
            pure = {}
            companions = {}
            try:
                for label, beta in [('plus', h), ('minus', -h)]:
                    p = jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, common)
                    p['tol_perturb_integration'] = C['tol300_override']
                    c = Class(); c.set(p); c.compute(['transfer']); pure[label] = c; solver_count += 1
                    if a.profile == 'INTERLEAVED':
                        q = jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, mixed)
                        q['tol_perturb_integration'] = C['tol300_override']
                        m = Class(); m.set(q); m.compute(['transfer']); companions[label] = m; solver_count += 1
                for cell in [x for x in lane_cells if float(x['h']) == h]:
                    z = f64hex(cell['z']); k = f64hex(cell['k']); vals = {}
                    for label in ['plus', 'minus']:
                        yn, mx, _ = v12.extract(jj, pure[label], common, z)
                        max_lookup = max(max_lookup, mx)
                        vv, ok = jj.cubic_centered(common, yn, np.asarray([k], dtype=np.float64))
                        if not bool(ok[0]):
                            raise RuntimeError('unsupported frozen target')
                        vals[label] = float(vv[0])
                    response = (vals['plus'] - vals['minus']) / (2*h)
                    if not math.isfinite(response):
                        raise RuntimeError('non-finite response')
                    rep_cells.append({
                        'role': cell['role'], 'grid': a.grid, 'profile': a.profile,
                        'repeat': rep, 'h': h, 'h_key': format(h,'.17g'),
                        'kind': cell['kind'], 'd': cell['d'], 'z': cell['z'], 'k': cell['k'],
                        'response': response
                    })
            finally:
                for c in list(pure.values()) + list(companions.values()):
                    try: c.struct_cleanup()
                    except Exception: pass
        repeats.append({'repeat': rep, 'cells': rep_cells})
    out = {
        'schema': 'LAYERB_BETA_SAME_RUN_SOLVER_DETERMINISM_LANE_V0_14',
        'grid': a.grid, 'profile': a.profile, 'repeat_count': repeat_count,
        'effect': '+0/+0', 'tol_perturb_integration': C['tol300'],
        'solver_construction_count': solver_count,
        'max_requested_node_coordinate_rel_mismatch': max_lookup,
        'repeats': repeats,
        'production_h_mutated': False, 'sampling_stepsize_changed': False,
        'global_65537_launched': False, 'covariance_read': False,
        'whitening_read': False, 'nuisance_read': False, 'relation_null_read': False,
        'Wm_S3_opened': False, 'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_SAME_RUN_SOLVER_DETERMINISM_LANE_V0_14'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(out['token'], a.grid, a.profile, repeat_count, solver_count, max_lookup)


def decision(a, C):
    docs = [json.load(open(p)) for p in a.inputs]
    expected = {(g,p) for g in C['grids'] for p in C['profiles']}
    got = {(d['grid'],d['profile']) for d in docs}
    if got != expected:
        raise RuntimeError('lane identity mismatch')
    if any(int(d['repeat_count']) != int(C['repeat_count']) for d in docs):
        raise RuntimeError('repeat count mismatch')
    vals = {}
    max_lookup = 0.0
    flags_ok = True
    for d in docs:
        max_lookup = max(max_lookup, float(d['max_requested_node_coordinate_rel_mismatch']))
        flags_ok &= not any(bool(d[k]) for k in ['production_h_mutated','sampling_stepsize_changed','global_65537_launched','covariance_read','whitening_read','nuisance_read','relation_null_read','Wm_S3_opened','science_gate_opened'])
        for r in d['repeats']:
            for c in r['cells']:
                vals[(d['grid'],d['profile'],int(r['repeat']),format(float(c['h']),'.17g'),c['kind'],c['d'],c['z'],c['k'])] = float(c['response'])
    tol = float(C['determinism_relative_tolerance'])
    summaries = []
    any_failure_nondet = False
    anchors_ok = True
    for cell in C['diagnostic_cells']:
        hkey = format(float(cell['h']), '.17g')
        s = {'role':cell['role'],'grid':cell['grid'],'h':cell['h'],'z':cell['z'],'k':cell['k'],'profiles':{}}
        for prof in C['profiles']:
            rr = [vals[(cell['grid'],prof,rep,hkey,cell['kind'],cell['d'],cell['z'],cell['k'])] for rep in range(1,int(C['repeat_count'])+1)]
            spread = max(rel(x,y) for x,y in itertools.combinations(rr,2))
            stable = spread < tol
            s['profiles'][prof] = {'responses':rr,'max_pairwise_repeat_rel':spread,'repeat_stable':stable}
            if cell['role'] == 'REPLAY_FAILURE' and not stable:
                any_failure_nondet = True
            if cell['role'] == 'ANCHOR' and not stable:
                anchors_ok = False
        summaries.append(s)
    finite_ok = all(math.isfinite(v) for v in vals.values())
    invariant_ok = flags_ok and finite_ok and max_lookup <= float(C['exact_target_binding_tolerance']) and anchors_ok
    if not invariant_ok:
        cls = 'SAME_RUN_SOLVER_DETERMINISM_AUDIT_INCONCLUSIVE'
        nxt = 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_14_INVARIANT_FAILURE'
    elif any_failure_nondet:
        cls = 'SAME_RUN_REPEATED_SOLVER_NONDETERMINISM_SUPPORTED'
        nxt = 'PROSPECTIVELY_FROZEN_SOLVER_STATE_INITIALIZATION_MEMORY_OR_PARALLEL_REDUCTION_LOCALIZATION_AUDIT'
    else:
        cls = 'SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED'
        nxt = 'PROSPECTIVELY_FROZEN_CROSS_HOST_ENVIRONMENT_FINGERPRINT_REPRODUCIBILITY_AUDIT'
    out = {
        'schema':'LAYERB_BETA_SAME_RUN_SOLVER_DETERMINISM_DECISION_V0_14',
        'classification':cls, 'effect':'+0/+0',
        'diagnostic_cells':summaries,
        'any_failure_cell_same_run_nondeterminism':any_failure_nondet,
        'anchor_invariant_ok':anchors_ok, 'finite_ok':finite_ok,
        'max_requested_node_coordinate_rel_mismatch':max_lookup,
        'determinism_relative_tolerance':tol, 'invariant_ok':invariant_ok,
        'negative_control_cross_profile_differences_ignored':True,
        'production_h_mutated':False, 'sampling_stepsize_changed':False,
        'global_65537_launched':False, 'covariance_read':False,
        'whitening_read':False, 'nuisance_read':False, 'relation_null_read':False,
        'Wm_S3_opened':False, 'science_gate_opened':False,
        'next_stage':nxt,
        'token':'PASS_LAYERB_BETA_SAME_RUN_SOLVER_DETERMINISM_DECISION_V0_14'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(out['token'], json.dumps({'classification':cls,'next_stage':nxt,'same_run_nondeterminism':any_failure_nondet},sort_keys=True))


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode', choices=['lane','decision'], required=True)
    p.add_argument('--contract', required=True)
    p.add_argument('--grid'); p.add_argument('--profile')
    p.add_argument('--v12-executor'); p.add_argument('--jj-script'); p.add_argument('--baseline'); p.add_argument('--precision')
    p.add_argument('--inputs', nargs='*', default=[]); p.add_argument('--out', required=True)
    a=p.parse_args(); C=json.load(open(a.contract))
    run_lane(a,C) if a.mode=='lane' else decision(a,C)

if __name__=='__main__':
    main()
