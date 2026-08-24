#!/usr/bin/env python3
"""Audit the pressureless-matter comoving density across Newtonian/synchronous gauges.

For the pinned CLASS-family convention, transfer outputs use d_i=delta rho_i/rho_i
and t_i=theta_i. For pressureless clustering matter define

    Delta_m = delta_m + 3 Hconf theta_m / k^2,

where Hconf=a H and k is in Mpc^-1. In synchronous CDM-comoving gauge the
`t_cdm` column is absent and is therefore zero by construction.

This script is calibration-first: it emits the full-core and frozen-node gauge
residual and only enforces a threshold when --max-rel is explicitly supplied.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np

K_NODES = np.array([1e-3, 3e-3, 1e-2, 3e-2, 1e-1], dtype=float)
CORE_MIN = 1e-3
CORE_MAX = 1e-1


def parse_numeric(path: Path) -> np.ndarray:
    return np.loadtxt(path)


def parse_header_columns(path: Path) -> dict[str, int]:
    header_line = None
    for line in path.read_text().splitlines():
        if line.startswith('#') and '1:k' in line:
            header_line = line
    if header_line is None:
        raise ValueError(f'No transfer-column header in {path}')
    pairs = re.findall(r'(\d+):([^\s]+)', header_line)
    return {name: int(idx) - 1 for idx, name in pairs}


def background_at_z(path: Path, z: float) -> dict[str, float]:
    arr = parse_numeric(path)
    order = np.argsort(arr[:, 0])
    zz = arr[order, 0]
    aa = arr[order]
    def interp(col: int) -> float:
        return float(np.interp(z, zz, aa[:, col]))
    return {
        'H_1_per_Mpc': interp(3),
        'rho_b': interp(9),
        'rho_cdm': interp(10),
    }


def matter_transfer(path: Path, background: Path, z: float, h: float):
    cols = parse_header_columns(path)
    data = parse_numeric(path)
    k_h = data[:, cols['k']]
    bg = background_at_z(background, z)
    rb, rc = bg['rho_b'], bg['rho_cdm']
    denom = rb + rc
    delta = (rb * data[:, cols['d_b']] + rc * data[:, cols['d_cdm']]) / denom
    theta_b = data[:, cols['t_b']]
    theta_cdm = data[:, cols['t_cdm']] if 't_cdm' in cols else np.zeros_like(theta_b)
    theta = (rb * theta_b + rc * theta_cdm) / denom
    k_mpc = k_h * h
    Hconf = bg['H_1_per_Mpc'] / (1.0 + z)
    Delta = delta + 3.0 * Hconf * theta / (k_mpc * k_mpc)
    return k_h, delta, theta, Delta


def log_interp_abs(k: np.ndarray, y: np.ndarray, nodes: np.ndarray) -> np.ndarray:
    # Delta_m has a common sign in the tested adiabatic sector. Interpolate its
    # magnitude in log-k while preserving the nearest local sign.
    mag = np.exp(np.interp(np.log(nodes), np.log(k), np.log(np.abs(y))))
    signs = np.sign(np.interp(np.log(nodes), np.log(k), np.sign(y)))
    signs[signs == 0] = 1.0
    return signs * mag


def compare_one(newt: Path, sync: Path, bg_newt: Path, bg_sync: Path, z: float, h: float):
    kn, dn, tn, Dn = matter_transfer(newt, bg_newt, z, h)
    ks, ds, ts, Ds = matter_transfer(sync, bg_sync, z, h)
    if not np.allclose(kn, ks, rtol=0, atol=1e-14):
        Ds = np.interp(kn, ks, Ds)
        ds = np.interp(kn, ks, ds)
        ts = np.interp(kn, ks, ts)
        ks = kn
    core = (kn >= CORE_MIN) & (kn <= CORE_MAX)
    rel = np.abs(Ds[core] / Dn[core] - 1.0)
    raw = np.abs(ds[core] / dn[core] - 1.0)
    imax = int(np.argmax(rel))

    nodes = K_NODES[(K_NODES >= max(kn.min(), ks.min())) & (K_NODES <= min(kn.max(), ks.max()))]
    Dnn = log_interp_abs(kn, Dn, nodes)
    Dsn = log_interp_abs(ks, Ds, nodes)
    dnn = log_interp_abs(kn, dn, nodes)
    dsn = log_interp_abs(ks, ds, nodes)
    node_out = {}
    for kval, va, vb, ra, rb in zip(nodes, Dnn, Dsn, dnn, dsn):
        node_out[f'k_{kval:g}'] = {
            'k_h_mpc': float(kval),
            'comoving_abs_relative': float(abs(vb / va - 1.0)),
            'raw_density_abs_relative': float(abs(rb / ra - 1.0)),
        }

    # Empirical gauge-transformation coefficient. For the pinned convention it
    # should approach +3 wherever the velocity difference is numerically active.
    bg = background_at_z(bg_newt, z)
    Hconf = bg['H_1_per_Mpc'] / (1.0 + z)
    k_mpc = kn * h
    denom_theta = tn - ts
    coeff = (ds - dn) * k_mpc * k_mpc / (Hconf * denom_theta)
    active = core & np.isfinite(coeff) & (np.abs(denom_theta) > 1e-20)
    coeff_summary = {
        'median': float(np.median(coeff[active])) if np.any(active) else float('nan'),
        'p16': float(np.quantile(coeff[active], 0.16)) if np.any(active) else float('nan'),
        'p84': float(np.quantile(coeff[active], 0.84)) if np.any(active) else float('nan'),
    }

    return {
        'z': z,
        'linear_core': {
            'max_comoving_abs_relative': float(rel[imax]),
            'k_at_max_h_mpc': float(kn[core][imax]),
            'median_comoving_abs_relative': float(np.median(rel)),
            'max_raw_density_abs_relative': float(np.max(raw)),
        },
        'frozen_nodes': node_out,
        'empirical_gauge_coefficient_expected_3': coeff_summary,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--directory', required=True)
    ap.add_argument('--h', type=float, required=True)
    ap.add_argument('--json', required=True)
    ap.add_argument('--max-rel', type=float, default=None)
    args = ap.parse_args()

    d = Path(args.directory)
    cases = []
    # CLASS z1 corresponds to first z_pk entry, here z=0; z2 to z=1.
    for idx, z in [(1, 0.0), (2, 1.0)]:
        cases.append(compare_one(
            d / f'newt_z{idx}_tk.dat', d / f'sync_z{idx}_tk.dat',
            d / 'newt_background.dat', d / 'sync_background.dat', z, args.h))
    global_max = max(c['linear_core']['max_comoving_abs_relative'] for c in cases)
    out = {
        'definition': 'Delta_m = delta_m + 3 a H theta_m / k^2',
        'k_units': 'transfer k converted from h/Mpc to 1/Mpc using supplied h',
        'linear_core_h_mpc': [CORE_MIN, CORE_MAX],
        'frozen_nodes_h_mpc': K_NODES.tolist(),
        'cases': cases,
        'global_max_comoving_abs_relative': global_max,
    }
    Path(args.json).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    if args.max_rel is not None and global_max > args.max_rel:
        raise SystemExit(f'comoving gauge residual {global_max:.6e} exceeds {args.max_rel:.6e}')


if __name__ == '__main__':
    main()
