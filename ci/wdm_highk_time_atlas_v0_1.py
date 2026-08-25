#!/usr/bin/env python3
"""Experiment 050A: C4 thermal-WDM high-k time atlas.

This is a calibration/domain-completion analysis. Only grid/provenance/algebra
controls are hard; no scientific threshold is applied to time dependence,
interaction power, or agreement with the legacy transfer fit.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import re
from pathlib import Path

import numpy as np

LD = np.longdouble
K_NODES = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 20.0], float)
Z_NODES = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], float)
MASSES = np.array([2.0, 3.0, 5.0], float)
ALG_TOL = LD('1e-12')
UPSTREAM = 'lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540'


def header_redshift(path: str) -> float:
    with open(path) as f:
        for _ in range(20):
            line = f.readline()
            if not line:
                break
            m = re.search(r'redshift\s+z\s*=\s*([+\-0-9.eE]+)', line, flags=re.I)
            if m:
                return float(m.group(1))
    # CLASS versions can also encode z only through ordered output names; do
    # not silently guess here because explicit z provenance is a hard control.
    raise ValueError(f'could not recover explicit redshift header: {path}')


def load_pk(path: str):
    a = np.loadtxt(path, comments='#')
    if a.ndim != 2 or a.shape[1] < 2:
        raise ValueError(f'bad P(k) file {path}: {a.shape}')
    k, p = np.asarray(a[:, 0], float), np.asarray(a[:, 1], float)
    mask = np.isfinite(k) & np.isfinite(p) & (k > 0) & (p > 0)
    k, p = k[mask], p[mask]
    order = np.argsort(k)
    k, p = k[order], p[order]
    if len(k) < 20 or np.any(np.diff(k) <= 0):
        raise ValueError(f'invalid/non-monotonic k grid in {path}')
    if K_NODES[0] < k[0] or K_NODES[-1] > k[-1]:
        raise ValueError(f'frozen high-k nodes outside {path} range {k[0]}..{k[-1]}')
    core = np.exp(np.interp(np.log(K_NODES), np.log(k), np.log(p)))
    return k, p, core


def files_for(directory: Path, prefix: str):
    hits = sorted(glob.glob(str(directory / (prefix + '*pk.dat'))))
    if not hits:
        raise ValueError(f'no CLASS pk files for prefix {prefix!r}')
    rows = []
    for path in hits:
        z = header_redshift(path)
        rows.append((z, path))
    rows.sort(key=lambda x: x[0])
    return rows


def matrix(directory: Path, prefix: str):
    rows = files_for(directory, prefix)
    z = np.array([x[0] for x in rows], float)
    if len(z) != len(Z_NODES) or not np.allclose(z, Z_NODES, rtol=0, atol=1e-10):
        raise ValueError(f'unexpected explicit z nodes for {prefix}: {z}')
    vals = []
    ranges = []
    files = []
    for zi, path in rows:
        k, p, core = load_pk(path)
        vals.append(core)
        ranges.append([float(k[0]), float(k[-1])])
        files.append(Path(path).name)
    return np.asarray(vals, float), files, ranges


def norm(x):
    x = np.asarray(x, dtype=LD)
    return np.sqrt(np.sum(x * x, dtype=LD), dtype=LD)


def decompose(R):
    R = np.asarray(R, dtype=LD)
    nz, nk = R.shape
    mu = np.sum(R, dtype=LD) / LD(R.size)
    T = np.sum(R, axis=0, dtype=LD) / LD(nz) - mu
    tau = np.sum(R, axis=1, dtype=LD) / LD(nk) - mu
    C = np.full(R.shape, mu, dtype=LD) + np.tile(T, (nz, 1)) + np.tile(tau[:, None], (1, nk))
    I = R - C
    nr, nc, ni = norm(R), norm(C), norm(I)
    if nr == 0:
        raise ValueError('zero WDM response matrix')
    recon = norm(R - C - I) / nr
    orth = abs(np.sum(C * I, dtype=LD)) / (nc * ni) if nc > 0 and ni > 0 else LD(0)
    zero = max(abs(np.mean(T, dtype=LD)), abs(np.mean(tau, dtype=LD))) / max(LD(1), nr)
    if ni > 0:
        qk = np.sum(I * I, axis=0, dtype=LD) / (ni * ni)
        qz = np.sum(I * I, axis=1, dtype=LD) / (ni * ni)
        qres = max(abs(np.sum(qk, dtype=LD) - 1), abs(np.sum(qz, dtype=LD) - 1))
        kgeo = np.exp(np.sum(qk * np.log(np.asarray(K_NODES, dtype=LD)), dtype=LD), dtype=LD)
        zmean = np.sum(qz * np.asarray(Z_NODES, dtype=LD), dtype=LD)
    else:
        qk = np.zeros(nk, dtype=LD)
        qz = np.zeros(nz, dtype=LD)
        qres = LD(0)
        kgeo = LD('nan')
        zmean = LD('nan')
    return {
        'mu': float(mu),
        'T_k': [float(x) for x in T],
        'tau_z': [float(x) for x in tau],
        'I': [[float(x) for x in row] for row in I],
        'chi_I': float((ni * ni) / (nr * nr)),
        'q_k': [float(x) for x in qk],
        'q_z': [float(x) for x in qz],
        'k_I_geo_h_mpc': float(kgeo) if np.isfinite(kgeo) else None,
        'z_I': float(zmean) if np.isfinite(zmean) else None,
        'controls': {
            'reconstruction': float(recon),
            'orthogonality': float(orth),
            'zero_mean': float(zero),
            'profile_normalization': float(qres),
        },
    }


def alpha_viel(m_keV: float, omega_wdm: float = 0.25, h: float = 0.7):
    return 0.049 * m_keV ** -1.11 * (omega_wdm / 0.25) ** 0.11 * (h / 0.7) ** 1.22


def legacy_response(m_keV: float, omega_wdm: float = 0.25, h: float = 0.7, nu: float = 1.12):
    alpha = alpha_viel(m_keV, omega_wdm=omega_wdm, h=h)
    T = (1 + (alpha * K_NODES) ** (2 * nu)) ** (-5 / nu)
    return 2 * np.log(T)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--directory', required=True)
    ap.add_argument('--reference-prefix', required=True)
    ap.add_argument('--models', nargs='+', required=True, help='m_keV:prefix')
    ap.add_argument('--h', type=float, default=0.67)
    ap.add_argument('--omega-wdm', type=float, default=0.1200)
    ap.add_argument('--json', required=True)
    args = ap.parse_args()

    root = Path(args.directory)
    pref_specs = []
    for spec in args.models:
        m_s, prefix = spec.split(':', 1)
        pref_specs.append((float(m_s), prefix))
    pref_specs.sort()
    if not np.allclose([x[0] for x in pref_specs], MASSES, rtol=0, atol=1e-14):
        raise ValueError(f'unexpected mass grid {pref_specs}')

    ref, ref_files, ref_ranges = matrix(root, args.reference_prefix)
    rows = []
    max_controls = {k: 0.0 for k in ('reconstruction', 'orthogonality', 'zero_mean', 'profile_normalization')}
    matched_omega = args.omega_wdm / args.h**2

    for mass, prefix in pref_specs:
        mod, files, ranges = matrix(root, prefix)
        R = np.log(mod / ref)
        d = decompose(R)
        for k, v in d['controls'].items():
            max_controls[k] = max(max_controls[k], v)

        legacy_default = legacy_response(mass)
        legacy_matched = legacy_response(mass, omega_wdm=matched_omega, h=args.h)
        z_drift = R - R[0][None, :]
        rows.append({
            'm_keV': mass,
            'prefix': prefix,
            'files': files,
            'k_ranges_h_mpc': ranges,
            'r_wdm': R.tolist(),
            'r_at_lowest_z': R[0].tolist(),
            'r_at_highest_z': R[-1].tolist(),
            'max_abs_redshift_drift_from_z0p295_by_k': np.max(np.abs(z_drift), axis=0).tolist(),
            'max_abs_redshift_drift': float(np.max(np.abs(z_drift))),
            'legacy_viel_default_r_T': legacy_default.tolist(),
            'legacy_viel_matched_cosmology_r_T': legacy_matched.tolist(),
            'lowest_z_minus_legacy_default': (R[0] - legacy_default).tolist(),
            'lowest_z_minus_legacy_matched': (R[0] - legacy_matched).tolist(),
            'interaction': d,
        })

    controls_pass = bool(max(max_controls.values()) <= float(ALG_TOL))
    out = {
        'schema': 'dsir.wdm_highk_time_atlas.v0.1',
        'status': 'PASS_WDM_HIGHK_TIME_ATLAS_OPERATOR_CONTROLS_V0_1' if controls_pass else 'FAIL_WDM_HIGHK_TIME_ATLAS_OPERATOR_CONTROLS_V0_1',
        'scope': 'Boltzmann thermal-WDM total-matter P(k,z) response on the separate frozen C4 high-k domain',
        'pinned_upstream': UPSTREAM,
        'z_nodes': Z_NODES.tolist(),
        'k_h_mpc': K_NODES.tolist(),
        'reference_prefix': args.reference_prefix,
        'reference_files': ref_files,
        'reference_k_ranges_h_mpc': ref_ranges,
        'cosmology_for_matched_fit_only': {'h': args.h, 'omega_wdm': args.omega_wdm, 'Omega_wdm': matched_omega},
        'operator_controls': {'threshold': float(ALG_TOL), 'maxima': max_controls, 'pass': controls_pass},
        'models': rows,
        'not_a_claim': [
            'No scientific threshold is imposed on chi_I, redshift drift, mass ordering, or agreement with the Viel fitting form.',
            'This is a linear Boltzmann calibration block, not nonlinear WDM power and not a Ly-alpha likelihood.',
            'C4 is not zero-padded into the low-k common-family matrix.',
            'No universal rank, G7 law, G8 discovery, or universal-model claim follows.'
        ]
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))
    raise SystemExit(0 if controls_pass else 2)


if __name__ == '__main__':
    main()
