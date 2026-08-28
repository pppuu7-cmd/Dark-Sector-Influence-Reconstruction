#!/usr/bin/env python3
from __future__ import annotations

import argparse
import glob
import json
import math
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
THRESHOLD_DEG = 45.0
STATUS = 'COMPLETE_K2_JOINT_METRIC_DIRECTION_CONTROL_V0_1'
CLASS_SEPARATED = 'K2_DIRECTION_SEPARATED_FROM_BOTH_GDM_AXES_EXP071E'
CLASS_OVERLAP = 'K2_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071E'


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
    if len(k) < 2 or K[0] < k[0] or K[-1] > k[-1]:
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
    if len(zs) != 7:
        raise AssertionError(f'expected 7 common redshifts for {prefix}, got {zs}')
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
    na, nb = float(np.linalg.norm(a)), float(np.linalg.norm(b))
    if not (math.isfinite(na) and math.isfinite(nb)) or na <= 0 or nb <= 0:
        raise AssertionError(f'non-finite/zero vector norm: {na}, {nb}')
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


def gdm_tangent(gdm: dict, model_key: str, step: float) -> tuple[np.ndarray, np.ndarray]:
    rec = gdm['models'][model_key]['response']
    rw = flat(rec, 'r_W') / step
    ds = flat(rec, 'delta_slip') / step
    if not np.all(np.isfinite(rw)) or not np.all(np.isfinite(ds)):
        raise AssertionError(f'non-finite GDM tangent {model_key}')
    if np.linalg.norm(rw) <= 0 or np.linalg.norm(ds) <= 0:
        raise AssertionError(f'zero GDM tangent channel {model_key}')
    return rw, ds


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--directory', required=True)
    ap.add_argument('--known-control', required=True)
    ap.add_argument('--gdm-discriminant', required=True)
    ap.add_argument('--gdm-hard-gate', required=True)
    ap.add_argument('--exp071d', required=True)
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

    parent_d = json.load(open(args.exp071d, encoding='utf-8'))
    assert parent_d['status'] == 'COMPLETE_K2_KNOWN_SECTOR_METRIC_SLIP_CONTROL_V0_1'
    assert parent_d['classification'] == 'K2_SLIP_TO_WEYL_RATIO_OVERLAPS_GDM_AXES_EXP071D'

    cs_w, cs_s = gdm_tangent(gdm, 'cs2_1e-7', 1e-7)
    cv_w, cv_s = gdm_tangent(gdm, 'cv2_1e-7', 1e-7)
    s_w = max(float(np.linalg.norm(cs_w)), float(np.linalg.norm(cv_w)), 1e-300)
    s_s = max(float(np.linalg.norm(cs_s)), float(np.linalg.norm(cv_s)), 1e-300)
    u_cs = np.r_[cs_w / s_w, cs_s / s_s]
    u_cv = np.r_[cv_w / s_w, cv_s / s_s]

    directory = Path(args.directory)
    models = []
    joint_vectors: list[np.ndarray] = []
    rw_tangents: list[np.ndarray] = []
    slip_tangents: list[np.ndarray] = []

    for i, ((ob, oc), prefix) in enumerate(zip(K2, [f'bar{j}_' for j in range(1, 6)]), 1):
        if abs((ob + oc) - OMEGA_M) > 2e-15:
            raise AssertionError((ob, oc))
        rec = response(directory, prefix)
        delta_fb = (ob - REFERENCE_OMEGA_B) / OMEGA_M
        if delta_fb <= 0:
            raise AssertionError(delta_fb)
        rw = flat(rec, 'r_W') / delta_fb
        ds = flat(rec, 'delta_slip') / delta_fb
        if not np.all(np.isfinite(rw)) or not np.all(np.isfinite(ds)):
            raise AssertionError(f'non-finite K2 tangent at bar{i}')
        if np.linalg.norm(rw) <= 0 or np.linalg.norm(ds) <= 0:
            raise AssertionError(f'zero K2 tangent channel at bar{i}')
        u = np.r_[rw / s_w, ds / s_s]
        joint_vectors.append(u)
        rw_tangents.append(rw)
        slip_tangents.append(ds)
        models.append({
            'index': i,
            'omega_b': ob,
            'omega_cdm': oc,
            'omega_m': ob + oc,
            'delta_f_b': delta_fb,
            'response': rec,
            'tangent_norm_r_W_per_delta_f_b': float(np.linalg.norm(rw)),
            'tangent_norm_delta_slip_per_delta_f_b': float(np.linalg.norm(ds)),
            'joint_equalized_norm': float(np.linalg.norm(u)),
            'joint_angle_to_primary_bar1_deg': None,
            'joint_angle_to_gdm_cs2_deg': angle(u, u_cs),
            'joint_angle_to_gdm_cv2_deg': angle(u, u_cv),
            'r_W_angle_to_primary_bar1_deg': None,
            'delta_slip_angle_to_primary_bar1_deg': None,
        })

    primary = joint_vectors[0]
    for i, m in enumerate(models):
        m['joint_angle_to_primary_bar1_deg'] = angle(primary, joint_vectors[i])
        m['r_W_angle_to_primary_bar1_deg'] = angle(rw_tangents[0], rw_tangents[i])
        m['delta_slip_angle_to_primary_bar1_deg'] = angle(slip_tangents[0], slip_tangents[i])

    theta_cs = models[0]['joint_angle_to_gdm_cs2_deg']
    theta_cv = models[0]['joint_angle_to_gdm_cv2_deg']
    primary_pass = bool(theta_cs >= THRESHOLD_DEG and theta_cv >= THRESHOLD_DEG)
    classification = CLASS_SEPARATED if primary_pass else CLASS_OVERLAP

    out = {
        'schema': 'dsir.k2_joint_metric_direction_control.v0.1',
        'experiment': 'Exp071E',
        'status': STATUS,
        'classification': classification,
        'primary_pass': primary_pass,
        'preregistered_threshold_deg': THRESHOLD_DEG,
        'primary_k2_point': 'bar1',
        'frozen_k_h_mpc': K.tolist(),
        'definition': {
            'W': 'phi+psi',
            'r_W': 'ln |W_model/W_ref|',
            'slip': '(phi-psi)/(phi+psi)',
            'delta_slip': 'slip_model-slip_ref',
            'K2_step': 'delta_f_b=(omega_b-omega_b_ref)/omega_m',
            'joint_equalization': 'sW=max(norm(GDM cs2 rW tangent), norm(GDM cv2 rW tangent)); sS analogous for slip; K2 does not set scales',
        },
        'parent_binding': {
            'Exp071C': {
                'run_id': 33020201997,
                'status': known['status'],
                'classification': known['primary_specificity_classification'],
            },
            'GDM_metric': {
                'run_id': 32774198185,
                'hard_gate_status': hard['status'],
                'hard_gate_pass': hard['pass'],
            },
            'Exp071D': {
                'run_id': 33176559280,
                'status': parent_d['status'],
                'classification': parent_d['classification'],
            },
        },
        'gdm_equalization_scales': {'s_W': s_w, 's_S': s_s},
        'primary_angles_deg': {
            'K2_bar1_vs_GDM_cs2': theta_cs,
            'K2_bar1_vs_GDM_cv2': theta_cv,
        },
        'K2_models': models,
        'robustness_nonclassifying': {
            'joint_family_centered_svd': svd_summary(joint_vectors),
            'max_joint_angle_to_bar1_deg': max(m['joint_angle_to_primary_bar1_deg'] for m in models),
            'max_r_W_angle_to_bar1_deg': max(m['r_W_angle_to_primary_bar1_deg'] for m in models),
            'max_delta_slip_angle_to_bar1_deg': max(m['delta_slip_angle_to_primary_bar1_deg'] for m in models),
        },
        'interpretation_boundary': [
            'PASS would separate this K2 local direction from the two tested GDM axes only; it would not prove dark-sector uniqueness',
            'FAIL would show the current joint r_W+slip direction is insufficient for generic specificity against K2',
            'robustness diagnostics cannot change the primary bar1 classification',
            'no observational covariance, nuisance quotient, G7, G8 or G9 is evaluated',
        ],
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }
    Path(args.json).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('EXP071E_CLASSIFICATION', classification)
    print('PRIMARY_ANGLES_DEG', out['primary_angles_deg'])
    print('ROBUSTNESS', out['robustness_nonclassifying'])


if __name__ == '__main__':
    main()
