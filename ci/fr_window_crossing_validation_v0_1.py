#!/usr/bin/env python3
"""Experiment 049C: withheld designer-f(R) window-crossing validation.

Prediction and thresholds are frozen in experiments/049c_fr_window_crossing_validation_v0_1.md
before any intermediate-B0 solver outputs are generated.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

LD = np.longdouble
FROZEN_B0 = np.array([1.5e-4, 2e-4, 3e-4, 5e-4, 7e-4], dtype=float)
FROZEN_Z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], dtype=float)
FROZEN_K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)
KMAX = 0.1
MONOTONIC_TOL = 1e-6  # h/Mpc, frozen before withheld outputs
CONTROL_TOL = LD('1e-12')
B0_REL_TOL = 1e-6
C_KM_S = 299792.458
H100_OVER_C_PER_MPC = 100.0 / C_KM_S


def norm(x):
    x = np.asarray(x, dtype=LD)
    return np.sqrt(np.sum(x * x, dtype=LD), dtype=LD)


def decompose(R):
    R = np.asarray(R, dtype=LD)
    nz, nk = R.shape
    mu = np.sum(R, dtype=LD) / LD(R.size)
    T = np.sum(R, axis=0, dtype=LD) / LD(nz) - mu
    tau = np.sum(R, axis=1, dtype=LD) / LD(nk) - mu
    core = np.full(R.shape, mu, dtype=LD) + np.tile(T, (nz, 1)) + np.tile(tau[:, None], (1, nk))
    I = R - core
    nr, nc, ni = norm(R), norm(core), norm(I)
    if nr == 0 or ni == 0:
        raise ValueError('nonzero response and interaction norms required')
    recon = norm(R - core - I) / nr
    orth = abs(np.sum(core * I, dtype=LD)) / (nc * ni) if nc > 0 else LD(0)
    zero = max(abs(np.mean(T, dtype=LD)), abs(np.mean(tau, dtype=LD))) / max(LD(1), nr)
    qk = np.sum(I * I, axis=0, dtype=LD) / (ni * ni)
    qz = np.sum(I * I, axis=1, dtype=LD) / (ni * ni)
    qres = max(abs(np.sum(qk, dtype=LD) - 1), abs(np.sum(qz, dtype=LD) - 1))
    kgeo = np.exp(np.sum(qk * np.log(np.asarray(FROZEN_K, dtype=LD)), dtype=LD), dtype=LD)
    zmean = np.sum(qz * np.asarray(FROZEN_Z, dtype=LD), dtype=LD)
    return {
        'chi_I': float((ni * ni) / (nr * nr)),
        'k_I_geo_h_mpc': float(kgeo),
        'z_I': float(zmean),
        'q_k': [float(x) for x in qk],
        'q_z': [float(x) for x in qz],
        'controls': {
            'reconstruction': float(recon),
            'orthogonality': float(orth),
            'zero_mean': float(zero),
            'profile_normalization': float(qres),
        },
    }


def load_response(path: Path):
    d = json.loads(path.read_text())
    if not np.allclose(np.asarray(d['z_nodes'], float), FROZEN_Z, rtol=0, atol=1e-14):
        raise ValueError(f'unexpected z grid in {path}')
    if not np.allclose(np.asarray(d['k_h_mpc'], float), FROZEN_K, rtol=0, atol=1e-14):
        raise ValueError(f'unexpected k grid in {path}')
    R = np.asarray(d['r_Delta'], dtype=LD)
    if R.shape != (len(FROZEN_Z), len(FROZEN_K)):
        raise ValueError(f'unexpected response shape {R.shape} in {path}')
    return d, R


def load_diag(path: Path):
    tab = np.loadtxt(path, comments='#')
    if tab.ndim != 2 or tab.shape[1] < 8:
        raise ValueError(f'bad diagnostic {path}: {tab.shape}')
    x, a, B, Rbar, fR, E, Ep, Epp = [np.asarray(tab[:, i], float) for i in range(8)]
    m = np.all(np.isfinite(tab[:, :8]), axis=1) & (a > 0) & (a <= 1.00000001) & (E > 0)
    vals = [v[m] for v in (x, a, B, Rbar, fR, E, Ep, Epp)]
    if vals[1].size < 1000 or vals[1].max() < 0.999:
        raise ValueError(f'insufficient diagnostic coverage in {path}')
    order = np.argsort(vals[1])
    keys = ('x', 'a', 'B', 'Rbar', 'fR', 'E', 'Ep', 'Epp')
    return {k: v[order] for k, v in zip(keys, vals)}


def interp_a(diag, key, zq):
    aq = 1.0 / (1.0 + np.asarray(zq, float))
    return np.interp(aq, diag['a'], diag[key])


def compton_scale(diag, zq):
    zq = np.atleast_1d(np.asarray(zq, float))
    a = 1.0 / (1.0 + zq)
    B = interp_a(diag, 'B', zq)
    E = interp_a(diag, 'E', zq)
    Ep = interp_a(diag, 'Ep', zq)
    Epp = interp_a(diag, 'Epp', zq)
    Rprime_bar = 3.0 * (4.0 * Ep + Epp)
    Hp_over_H = Ep / (2.0 * E)
    inv3frr = Rprime_bar / (3.0 * B * Hp_over_H)
    if np.any(~np.isfinite(inv3frr)) or np.any(inv3frr <= 0):
        raise ValueError('non-positive inverse Compton ratio')
    return a * H100_OVER_C_PER_MPC * np.sqrt(inv3frr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--zero', required=True, help='B0=0 response JSON')
    ap.add_argument('--models', nargs='+', required=True, help='B0:response_json:diagnostic_file')
    ap.add_argument('--json', required=True)
    args = ap.parse_args()

    _, zero = load_response(Path(args.zero))
    parsed = []
    for spec in args.models:
        b_s, response_s, diag_s = spec.split(':', 2)
        parsed.append((float(b_s), Path(response_s), Path(diag_s)))
    parsed.sort(key=lambda x: x[0])
    amps = np.array([x[0] for x in parsed], float)
    if not np.allclose(amps, FROZEN_B0, rtol=0, atol=1e-16):
        raise ValueError(f'unexpected withheld B0 grid {amps}')

    rows = []
    max_controls = {k: 0.0 for k in ('reconstruction', 'orthogonality', 'zero_mean', 'profile_normalization')}
    for B0, response_path, diag_path in parsed:
        response_meta, raw = load_response(response_path)
        if abs(float(response_meta['B0']) - B0) > max(1e-16, B0 * 1e-12):
            raise ValueError(f'B0 metadata mismatch for {response_path}')
        d = decompose(raw - zero)
        for key, value in d['controls'].items():
            max_controls[key] = max(max_controls[key], value)

        diag = load_diag(diag_path)
        terminal_rel = abs(float(diag['B'][-1]) - B0) / B0
        kc = compton_scale(diag, FROZEN_Z)
        rows.append({
            'B0': B0,
            'response_json': str(response_path),
            'diagnostic_file': str(diag_path),
            'terminal_B0_relative_error': float(terminal_rel),
            'k_compton_frozen_z_h_mpc': [float(x) for x in kc],
            'k_compton_frozen_z_min_h_mpc': float(np.min(kc)),
            'k_compton_frozen_z_max_h_mpc': float(np.max(kc)),
            'transition_inside_kmax_at_any_frozen_z': bool(np.min(kc) <= KMAX),
            'chi_I': d['chi_I'],
            'k_I_geo_h_mpc': d['k_I_geo_h_mpc'],
            'z_I': d['z_I'],
            'q_k': d['q_k'],
            'q_z': d['q_z'],
        })

    op_pass = bool(max(max_controls.values()) <= float(CONTROL_TOL))
    b0_pass = bool(max(r['terminal_B0_relative_error'] for r in rows) <= B0_REL_TOL)
    kc_min = np.array([r['k_compton_frozen_z_min_h_mpc'] for r in rows], float)
    source_inside = bool(all(r['transition_inside_kmax_at_any_frozen_z'] for r in rows))
    source_decreasing = bool(np.all(np.diff(kc_min) < 0))
    source_pass = bool(b0_pass and source_inside and source_decreasing)

    kgeo = np.array([r['k_I_geo_h_mpc'] for r in rows], float)
    kgeo_steps = np.diff(kgeo)
    prediction_pass = bool(np.all(kgeo_steps <= MONOTONIC_TOL))

    if not op_pass:
        status = 'FAIL_FR_WINDOW_CROSSING_OPERATOR_CONTROLS_V0_1'
    elif not source_pass:
        status = 'FAIL_FR_WINDOW_CROSSING_SOURCE_SCALE_CONTRACT_V0_1'
    elif not prediction_pass:
        status = 'FAIL_FR_WINDOW_CROSSING_PREDICTION_V0_1'
    else:
        status = 'PASS_FR_WINDOW_CROSSING_VALIDATION_V0_1'

    out = {
        'schema': 'dsir.fr_window_crossing_validation.v0.1',
        'status': status,
        'frozen_before_withheld_outputs': {
            'B0_grid': FROZEN_B0.tolist(),
            'k_window_h_mpc': [float(FROZEN_K.min()), KMAX],
            'scientific_prediction': 'k_I_geo is non-increasing with B0 across the withheld grid',
            'max_allowed_positive_k_I_step_h_mpc': MONOTONIC_TOL,
            'no_prediction_for': ['z_I', 'chi_I', 'exact k_I values', 'shift magnitude', 'survey significance'],
        },
        'operator_controls': {
            'threshold': float(CONTROL_TOL),
            'maxima': max_controls,
            'pass': op_pass,
        },
        'source_scale_contract': {
            'terminal_B0_relative_threshold': B0_REL_TOL,
            'max_terminal_B0_relative_error': max(r['terminal_B0_relative_error'] for r in rows),
            'all_transitions_inside_kmax_at_any_frozen_z': source_inside,
            'k_compton_min_strictly_decreases_with_B0': source_decreasing,
            'pass': source_pass,
        },
        'scientific_prediction_test': {
            'k_I_geo_h_mpc': kgeo.tolist(),
            'consecutive_steps_h_mpc': kgeo_steps.tolist(),
            'pass': prediction_pass,
        },
        'models': rows,
        'interpretation_boundary': [
            'This is a withheld directional interpolation test, not a fit to the known 1e-4 and 1e-3 anchors.',
            'A PASS supports the finite-window transition/localization principle in designer f(R) but does not establish universality.',
            'A source-eligible prediction failure is a scientific negative result for this frozen hypothesis/domain.',
            'No G7 law, G8 discovery, field-count, no-hair, or observation-space detectability claim follows.'
        ],
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))
    raise SystemExit(0 if status.startswith('PASS_') else 2)


if __name__ == '__main__':
    main()
