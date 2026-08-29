#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.metadata
import json
from pathlib import Path

import healpy as hp
import numpy as np
import pymaster as nmt

PASS = 'PASS_EXP073T_NAMASTER_2P7_COMPONENT_ORDER_V0_1'
GATES = {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}


def dominant_index(cls: np.ndarray) -> tuple[int, list[float]]:
    if cls.ndim != 2:
        raise AssertionError(f'expected [ncls,nell], got {cls.shape}')
    power = np.sum(np.abs(cls[:, 2:]), axis=1)
    if not np.all(np.isfinite(power)) or float(power.max()) <= 0:
        raise AssertionError('nonfinite/zero synthetic spectrum')
    return int(np.argmax(power)), [float(x) for x in power]


def assert_target(label: str, cls: np.ndarray, target: int) -> dict:
    idx, power = dominant_index(cls)
    if idx != target:
        raise AssertionError(f'{label}: dominant component {idx}, expected {target}; power={power}')
    rest = [x for i, x in enumerate(power) if i != target]
    leakage = max(rest) if rest else 0.0
    ratio = float(power[target] / max(leakage, 1e-300))
    if ratio < 100.0:
        raise AssertionError(f'{label}: target/leakage ratio {ratio} < 100; power={power}')
    return {'dominant_component': idx, 'component_l1_power': power, 'target_to_max_other_ratio': ratio}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    version = importlib.metadata.version('pymaster')
    if not (version == '2.7' or version.startswith('2.7.')):
        raise AssertionError(f'expected pymaster 2.7 lineage, got {version}')

    nside = 32
    lmax = 3 * nside - 1
    ell0 = 8
    alm = np.zeros(hp.Alm.getsize(lmax), dtype=np.complex128)
    alm[hp.Alm.getidx(lmax, ell0, 0)] = 1.0 + 0.0j
    zero = np.zeros_like(alm)

    scalar_map = hp.alm2map(alm, nside, lmax=lmax)
    qE, uE = hp.alm2map_spin([alm, zero], nside, 2, lmax)
    qB, uB = hp.alm2map_spin([zero, alm], nside, 2, lmax)
    mask = np.ones(hp.nside2npix(nside), dtype=float)

    f0 = nmt.NmtField(mask, [scalar_map])
    fE = nmt.NmtField(mask, [qE, uE])
    fB = nmt.NmtField(mask, [qB, uB])

    c0E = nmt.compute_coupled_cell(f0, fE)
    c0B = nmt.compute_coupled_cell(f0, fB)
    cEE = nmt.compute_coupled_cell(fE, fE)
    cEB = nmt.compute_coupled_cell(fE, fB)
    cBE = nmt.compute_coupled_cell(fB, fE)
    cBB = nmt.compute_coupled_cell(fB, fB)

    if c0E.shape[0] != 2 or cEE.shape[0] != 4:
        raise AssertionError(f'unexpected ncls shapes: 0x2={c0E.shape}, 2x2={cEE.shape}')

    tests = {
        'spin0_x_E_is_component0_TE': assert_target('0xE', c0E, 0),
        'spin0_x_B_is_component1_TB': assert_target('0xB', c0B, 1),
        'E_x_E_is_component0_EE': assert_target('ExE', cEE, 0),
        'E_x_B_is_component1_EB': assert_target('ExB', cEB, 1),
        'B_x_E_is_component2_BE': assert_target('BxE', cBE, 2),
        'B_x_B_is_component3_BB': assert_target('BxB', cBB, 3),
    }

    result = {
        'experiment': 'Exp073T',
        'status': PASS,
        'pymaster_version': version,
        'synthetic': {
            'nside': nside,
            'lmax': lmax,
            'single_input_ell': ell0,
            'mask': 'full-sky unity',
        },
        'verified_component_order': {
            'spin0_x_spin2': ['TE', 'TB'],
            'spin2_x_spin2': ['EE', 'EB', 'BE', 'BB'],
        },
        'tests': tests,
        'physical_support_evaluated': False,
        'science_gate_scored': False,
        'covariance_read': False,
        'nuisance_geometry_read': False,
        'G8_read': False,
        'gate_state': GATES,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': PASS, 'pymaster_version': version, 'order': result['verified_component_order']}, sort_keys=True))


if __name__ == '__main__':
    main()
