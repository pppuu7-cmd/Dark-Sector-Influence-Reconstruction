#!/usr/bin/env python3
from __future__ import annotations

import argparse
import glob
import json
import re
from pathlib import Path

import numpy as np

K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)
OMEGA_M = 0.1424
REFERENCE_OMEGA_B = 0.0224
K2 = [
    (0.0228, 0.1196),
    (0.0232, 0.1192),
    (0.0236, 0.1188),
    (0.0240, 0.1184),
    (0.0244, 0.1180),
]
STATUS = 'COMPLETE_K2_KNOWN_SECTOR_METRIC_SLIP_CONTROL_V0_1'
CLASS_BELOW = 'K2_SLIP_TO_WEYL_RATIO_BELOW_BOTH_GDM_AXES_EXP071D'
CLASS_OVERLAP = 'K2_SLIP_TO_WEYL_RATIO_OVERLAPS_GDM_AXES_EXP071D'


def z_header(path: str) -> float:
    with open(path, encoding='utf-8', errors='replace') as f:
        for _ in range(16):
            line = f.readline()
            m = re.search(r'redshift\s+z\s*=\s*([+\-0-9.eE]+)', line)
            if m:
                return float(m.group(1))
    raise ValueError('missing redshift: ' + path)


def columns(path: str) -> dict[str, int]:
    text = ''
    with open(path, encoding='utf-8', errors='replace') as f:
        for _ in range(16):
            line = f.readline()
            if not line.startswith('#'):
                break
            text += line
    out = {'k': 0}
    for name in ('phi', 'psi'):
        m = re.search(r'(\d+):' + name + r'(?:\s|$)', text)
        if not m:
            raise ValueError(f'missing {name} column in {path}')
        out[name] = int(m.group(1)) - 1
    return out


def load_core(path: str) -> tuple[np.ndarray, np.ndarray]:
    c = columns(path)
    a = np.loadtxt(path, comments='#')
    k = np.asarray(a[:, c['k']], float)
    phi = np.asarray(a[:, c['phi']], float)
    psi = np.asarray(a[:, c['psi']], float)
    good = np.isfinite(k) & np.isfinite(phi) & np.isfinite(psi) & (k > 0)
    k, phi, psi = k[good], phi[good], psi[good]
    order = np.argsort(k)
    k, phi, psi = k[order], phi[order], psi[order]
    if K[0] < k[0] or K[-1] > k[-1]:
        raise ValueError(f'core outside transfer grid in {path}: [{k[0]}, {k[-1]}]')
    x, xx = np.log(k), np.log(K)
    return np.interp(xx, x, phi), np.interp(xx, x, psi)


def files(directory: Path, prefix: str) -> dict[float, str]:
    hits = sorted(glob.glob(str(directory / (prefix + '*tk.dat'))))
    if not hits:
        raise ValueError('no tk files for ' + prefix)
    out: dict[float, str] = {}
    for p in hits:
        z = z_header(p)
        if z in out:
            raise ValueError('duplicate z in ' + prefix)
        out[z] = p
    return out


def response(directory: Path, prefix: str, refprefix: str = 'ref_') -> dict:
    fs, rs = files(directory, prefix), files(directory, refprefix)
    zs = sorted(set(fs) & set(rs))
    rows = []
    sign_ok = True
    min_abs_w = np.inf
    for z in zs:
        pm, qm = load_core(fs[z])
        pr, qr = load_core(rs[z])
        wm, wr = pm + qm, pr + qr
        sign_ok = sign_ok and bool(np.all(wm * wr > 0))
        min_abs_w = min(min_abs_w, float(np.min(np.abs(wr))))
        if np.any(np.abs(wr) < 1e-30) or np.any(np.abs(wm) < 1e-30):
            raise ValueError('Weyl denominator too small')
        rw = np.log(np.abs(wm / wr))
        sm = (pm - qm) / wm
        sr = (pr - qr) / wr
        ds = sm - sr
        rows.append({'z': z, 'r_W': rw.tolist(), 'delta_slip': ds.tolist()})
    return {
        'files': rows,
        'weyl_sign_preserved': sign_ok,
        'min_abs_reference_phi_plus_psi': min_abs_w,
    }


def flat(rec: dict, key: str) -> np.ndarray:
    return np.concatenate([
        np.asarray(x[key], float)
        for x in sorted(rec['files'], key=lambda y: y['z'])
    ])


def angle(a: np.ndarray, b: np.ndarray) -> float:
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return float('nan')
    c = float(np.dot(a, b) / (na * nb))
    return float(np.degrees(np.arccos(np.clip(c, -1.0, 1.0))))


def svd_summary(vectors: list[np.ndarray]) -> dict:
    a = np.stack(vectors)
    centered = a - a.mean(axis=0, keepdims=True)
    s = np.linalg.svd(centered, compute_uv=False)
    ss = s * s
    total = float(ss.sum())
    vf = (ss / total).tolist() if total > 0 else [0.0 for _ in s]
    return {
        'singular_values': s.tolist(),
        'variance_fraction': vf,
        'cumulative_variance_fraction': np.cumsum(vf).tolist(),
    }


def gdm_ratio(gdm: dict, model_key: str) -> float:
    rec = gdm['models'][model_key]['response']
    rw = flat(rec, 'r_W')
    ds = flat(rec, 'delta_slip')
    nrw = float(np.linalg.norm(rw))
    nds = float(np.linalg.norm(ds))
    if nrw <= 0:
        raise AssertionError(f'zero GDM r_W norm for {model_key}')
    return nds / nrw


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--directory', required=True)
    ap.add_argument('--known-control', required=True)
    ap.add_argument('--gdm-discriminant', required=True)
    ap.add_argument('--gdm-hard-gate', required=True)
    ap.add_argument('--json', required=True)
    args = ap.parse_args()

    known = json.load(open(args.known_control, encoding='utf-8'))
    assert known['status'] == 'COMPLETE_KNOWN_SECTOR_F30_SPECIFICITY_CONTROL_V0_1'
    assert known['primary_specificity_classification'] == 'F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL'
    assert known['K2_baryon_fraction_fixed_omega_m']['pass_full_and_all_leave_one_z'] is True

    gdm = json.load(open(args.gdm_discriminant, encoding='utf-8'))
    hard = json.load(open(args.gdm_hard_gate, encoding='utf-8'))
    assert hard['status'] == 'PASS_GDM_SLIP_BREAKS_LOW_K_DEGENERACY'
    assert hard['pass'] is True

    d = Path(args.directory)
    prefixes = [f'bar{i}_' for i in range(1, 6)]
    models = []
    rw_tangents: list[np.ndarray] = []
    slip_tangents: list[np.ndarray] = []
    k2_ratios = []

    for i, ((ob, oc), prefix) in enumerate(zip(K2, prefixes), 1):
        if abs((ob + oc) - OMEGA_M) > 2e-15:
            raise AssertionError((ob, oc))
        rec = response(d, prefix)
        rw = flat(rec, 'r_W')
        ds = flat(rec, 'delta_slip')
        nrw = float(np.linalg.norm(rw))
        nds = float(np.linalg.norm(ds))
        if nrw <= 0:
            raise AssertionError(f'zero K2 r_W norm at point {i}')
        q = nds / nrw
        k2_ratios.append(q)
        delta_fb = (ob - REFERENCE_OMEGA_B) / OMEGA_M
        if delta_fb <= 0:
            raise AssertionError(delta_fb)
        trw = rw / delta_fb
        tds = ds / delta_fb
        rw_tangents.append(trw)
        slip_tangents.append(tds)
        models.append({
            'index': i,
            'omega_b': ob,
            'omega_cdm': oc,
            'omega_m': ob + oc,
            'delta_f_b': delta_fb,
            'response': rec,
            'norm_r_W': nrw,
            'norm_delta_slip': nds,
            'q_slip_over_W': q,
            'tangent_norm_r_W_per_delta_f_b': float(np.linalg.norm(trw)),
            'tangent_norm_delta_slip_per_delta_f_b': float(np.linalg.norm(tds)),
        })

    gdm_cs = gdm_ratio(gdm, 'cs2_1e-7')
    gdm_cv = gdm_ratio(gdm, 'cv2_1e-7')
    k2_max = max(k2_ratios)
    classification = CLASS_BELOW if k2_max < min(gdm_cs, gdm_cv) else CLASS_OVERLAP

    geometry = {
        'r_W_angles_to_first_tangent_deg': [angle(rw_tangents[0], x) for x in rw_tangents],
        'delta_slip_angles_to_first_tangent_deg': [angle(slip_tangents[0], x) for x in slip_tangents],
        'r_W_family_svd': svd_summary(rw_tangents),
        'delta_slip_family_svd': svd_summary(slip_tangents),
    }

    out = {
        'schema': 'dsir.k2_known_sector_metric_slip_control.v0.1',
        'experiment': 'Exp071D',
        'status': STATUS,
        'classification': classification,
        'definition': {
            'W': 'phi+psi',
            'r_W': 'ln |W_model/W_ref|',
            'slip': '(phi-psi)/(phi+psi)',
            'delta_slip': 'slip_model-slip_ref',
            'q_slip_over_W': 'L2(delta_slip)/L2(r_W) on identical flattened z,k grid',
        },
        'frozen_k_h_mpc': K.tolist(),
        'known_sector_parent_binding': {
            'experiment': known['experiment'],
            'status': known['status'],
            'primary_specificity_classification': known['primary_specificity_classification'],
            'K2_pass_full_and_all_leave_one_z': known['K2_baryon_fraction_fixed_omega_m']['pass_full_and_all_leave_one_z'],
        },
        'gdm_parent_binding': {
            'hard_gate_status': hard['status'],
            'hard_gate_pass': hard['pass'],
            'gdm_1e-7_q_slip_over_W': {'cs2': gdm_cs, 'cv2': gdm_cv},
            'prior_observed_angles_deg': hard['observed'],
        },
        'K2_models': models,
        'K2_q_slip_over_W': k2_ratios,
        'K2_max_q_slip_over_W': k2_max,
        'strict_reference_min_gdm_q_slip_over_W': min(gdm_cs, gdm_cv),
        'geometry': geometry,
        'interpretation_boundary': [
            'ordering is a mechanism-control diagnostic, not a discovery claim',
            'K2 below both GDM axes would show that this matter-space mimic has weaker relative slip, not prove uniqueness',
            'overlap would further weaken metric-slip specificity for this control set',
            'no observational covariance, nuisance quotient, G7, G8 or G9 is evaluated',
        ],
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }
    Path(args.json).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('EXP071D_CLASSIFICATION', classification)
    print('K2_Q', k2_ratios)
    print('GDM_Q', {'cs2': gdm_cs, 'cv2': gdm_cv})


if __name__ == '__main__':
    main()
