#!/usr/bin/env python3
from __future__ import annotations

import argparse
import glob
import json
import math
import re
from pathlib import Path

import numpy as np

K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], float)
Z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], float)
LOGK = np.log(K)
OMEGA_M = 0.1424
REF_OMEGA_B = 0.0224
THRESHOLD_DEG = 45.0
STATUS = 'COMPLETE_K2_MATTER_WEYL_SLIP_DIRECTION_CONTROL_V0_1'
CLASS_SEPARATED = 'K2_3CHANNEL_DIRECTION_SEPARATED_FROM_BOTH_GDM_AXES_EXP071F'
CLASS_OVERLAP = 'K2_3CHANNEL_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071F'


def unique(root: str, name: str) -> Path:
    hits = list(Path(root).rglob(name))
    if len(hits) != 1:
        raise ValueError(f'expected one {name} under {root}, got {hits}')
    return hits[0]


def header_z(path: str | Path) -> float:
    with open(path, encoding='utf-8', errors='replace') as f:
        for _ in range(20):
            line = f.readline()
            m = re.search(r'redshift\s+z\s*=\s*([+\-0-9.eE]+)', line, re.I)
            if m:
                return float(m.group(1))
    raise ValueError(f'missing redshift header: {path}')


def by_z(root: str, prefix: str) -> dict[float, Path]:
    hits = sorted(Path(root).rglob(prefix + '*pk.dat'))
    if len(hits) != 7:
        raise ValueError(f'expected 7 pk files for {prefix}, got {len(hits)}')
    out = {header_z(p): p for p in hits}
    zs = np.asarray(sorted(out), float)
    if len(out) != 7 or not np.allclose(zs, Z, rtol=0, atol=1e-10):
        raise ValueError(f'wrong z grid for {prefix}: {zs}')
    return out


def nearest(d: dict[float, Path], z: float) -> float:
    q = min(d, key=lambda x: abs(x-z))
    if abs(q-z) > 1e-10:
        raise ValueError(z)
    return q


def nodes_pk(path: Path) -> np.ndarray:
    a = np.loadtxt(path, comments='#')
    if a.ndim != 2 or a.shape[1] < 2:
        raise ValueError(f'bad P(k): {path}')
    k, p = np.asarray(a[:, 0], float), np.asarray(a[:, 1], float)
    good = np.isfinite(k) & np.isfinite(p) & (k > 0) & (p > 0)
    k, p = k[good], p[good]
    order = np.argsort(k)
    k, p = k[order], p[order]
    if len(k) < 20 or np.any(np.diff(k) <= 0) or k.min() > K.min() or k.max() < K.max():
        raise ValueError(f'bad k coverage: {path}')
    return np.interp(LOGK, np.log(k), np.log(p))


def pk_response(ref: dict[float, Path], mod: dict[float, Path]) -> np.ndarray:
    return np.asarray([
        nodes_pk(mod[nearest(mod, float(z))]) - nodes_pk(ref[nearest(ref, float(z))])
        for z in Z
    ], float)


def flat_response(rec: dict, key: str) -> np.ndarray:
    rows = sorted(rec['files'], key=lambda x: float(x['z']))
    zs = np.asarray([float(x['z']) for x in rows], float)
    if len(rows) != 7 or not np.allclose(zs, Z, rtol=0, atol=1e-10):
        raise ValueError(f'wrong response z grid for {key}: {zs}')
    out = np.concatenate([np.asarray(x[key], float) for x in rows])
    if out.shape != (35,) or not np.all(np.isfinite(out)):
        raise ValueError(f'bad flattened {key}: {out.shape}')
    return out


def angle(a: np.ndarray, b: np.ndarray) -> float:
    na, nb = float(np.linalg.norm(a)), float(np.linalg.norm(b))
    if not (math.isfinite(na) and math.isfinite(nb)) or na <= 0 or nb <= 0:
        raise ValueError(f'bad vector norms {na}, {nb}')
    c = float(np.dot(a, b)/(na*nb))
    return float(np.degrees(np.arccos(np.clip(c, -1.0, 1.0))))


def svd_summary(vectors: list[np.ndarray]) -> dict:
    a = np.stack(vectors)
    c = a - a.mean(axis=0, keepdims=True)
    s = np.linalg.svd(c, compute_uv=False)
    ss = s*s
    total = float(ss.sum())
    vf = ss/total if total > 0 else np.zeros_like(ss)
    return {
        'singular_values': s.tolist(),
        'variance_fraction': vf.tolist(),
        'cumulative_variance_fraction': np.cumsum(vf).tolist(),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--known-root', required=True)
    ap.add_argument('--gdm-root', required=True)
    ap.add_argument('--exp071e', required=True)
    ap.add_argument('--json', required=True)
    args = ap.parse_args()

    known = json.loads(unique(args.known_root, 'exp071c_known_sector_f30_specificity_control_v0_1.json').read_text())
    assert known['status'] == 'COMPLETE_KNOWN_SECTOR_F30_SPECIFICITY_CONTROL_V0_1'
    assert known['primary_specificity_classification'] == 'F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL'
    assert known['K2_baryon_fraction_fixed_omega_m']['pass_full_and_all_leave_one_z'] is True

    gdm = json.loads(unique(args.gdm_root, 'gdm_weyl_slip_discriminant.json').read_text())
    hard = json.loads(unique(args.gdm_root, 'gdm_weyl_slip_hard_gate.json').read_text())
    assert hard['status'] == 'PASS_GDM_SLIP_BREAKS_LOW_K_DEGENERACY' and hard['pass'] is True

    exp071e = json.load(open(args.exp071e, encoding='utf-8'))
    assert exp071e['status'] == 'COMPLETE_K2_JOINT_METRIC_DIRECTION_CONTROL_V0_1'
    assert exp071e['classification'] == 'K2_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071E'
    assert exp071e['primary_k2_point'] == 'bar1'
    assert exp071e['preregistered_threshold_deg'] == 45.0

    # Matter responses from immutable parent spectra.
    k_ref = by_z(args.known_root, 'ref_')
    k2_p = [pk_response(k_ref, by_z(args.known_root, f'bar{i}_')) for i in range(1, 6)]
    g_ref = by_z(args.gdm_root, 'gdm0_')
    cs_p = pk_response(g_ref, by_z(args.gdm_root, 'cs1em7_')).reshape(-1)/1e-7
    cv_p = pk_response(g_ref, by_z(args.gdm_root, 'cv1em7_')).reshape(-1)/1e-7

    # Weyl/slip GDM tangents from immutable parent response JSON.
    cs_rec = gdm['models']['cs2_1e-7']['response']
    cv_rec = gdm['models']['cv2_1e-7']['response']
    cs_w = flat_response(cs_rec, 'r_W')/1e-7
    cs_s = flat_response(cs_rec, 'delta_slip')/1e-7
    cv_w = flat_response(cv_rec, 'r_W')/1e-7
    cv_s = flat_response(cv_rec, 'delta_slip')/1e-7

    s_p = max(float(np.linalg.norm(cs_p)), float(np.linalg.norm(cv_p)), 1e-300)
    s_w = max(float(np.linalg.norm(cs_w)), float(np.linalg.norm(cv_w)), 1e-300)
    s_s = max(float(np.linalg.norm(cs_s)), float(np.linalg.norm(cv_s)), 1e-300)
    for x in (s_p, s_w, s_s):
        if not math.isfinite(x) or x <= 0:
            raise ValueError('bad equalization scale')

    u_cs_2 = np.r_[cs_w/s_w, cs_s/s_s]
    u_cv_2 = np.r_[cv_w/s_w, cv_s/s_s]
    u_cs_3 = np.r_[cs_p/s_p, cs_w/s_w, cs_s/s_s]
    u_cv_3 = np.r_[cv_p/s_p, cv_w/s_w, cv_s/s_s]

    models = []
    u_k2_3 = []
    for i, (parent_model, rp) in enumerate(zip(exp071e['K2_models'], k2_p), 1):
        ob = float(parent_model['omega_b'])
        oc = float(parent_model['omega_cdm'])
        if abs((ob+oc)-OMEGA_M) > 2e-15:
            raise ValueError('K2 fixed omega_m violated')
        df = (ob-REF_OMEGA_B)/OMEGA_M
        if df <= 0:
            raise ValueError('nonpositive K2 step')
        tp = rp.reshape(-1)/df
        tw = flat_response(parent_model['response'], 'r_W')/df
        ts = flat_response(parent_model['response'], 'delta_slip')/df
        u2 = np.r_[tw/s_w, ts/s_s]
        u3 = np.r_[tp/s_p, tw/s_w, ts/s_s]
        u_k2_3.append(u3)
        models.append({
            'index': i,
            'omega_b': ob,
            'omega_cdm': oc,
            'delta_f_b': df,
            'matter_tangent_norm': float(np.linalg.norm(tp)),
            'three_channel_angle_to_gdm_cs2_deg': angle(u3, u_cs_3),
            'three_channel_angle_to_gdm_cv2_deg': angle(u3, u_cv_3),
            'three_channel_angle_to_primary_bar1_deg': None,
            'two_channel_angle_to_gdm_cs2_deg': angle(u2, u_cs_2),
            'two_channel_angle_to_gdm_cv2_deg': angle(u2, u_cv_2),
        })

    primary = u_k2_3[0]
    for i, m in enumerate(models):
        m['three_channel_angle_to_primary_bar1_deg'] = angle(primary, u_k2_3[i])

    # Exact Exp071E integrity cross-check before using the new statistic.
    e_cs = float(exp071e['primary_angles_deg']['K2_bar1_vs_GDM_cs2'])
    e_cv = float(exp071e['primary_angles_deg']['K2_bar1_vs_GDM_cv2'])
    if abs(models[0]['two_channel_angle_to_gdm_cs2_deg']-e_cs) > 1e-8:
        raise AssertionError('Exp071E cs2 angle cross-check failed')
    if abs(models[0]['two_channel_angle_to_gdm_cv2_deg']-e_cv) > 1e-8:
        raise AssertionError('Exp071E cv2 angle cross-check failed')

    # Matter-only diagnostics for the same primary K2 tangent.
    df0 = float(models[0]['delta_f_b'])
    k2p0 = k2_p[0].reshape(-1)/df0
    matter_angles = {
        'K2_bar1_vs_GDM_cs2': angle(k2p0, cs_p),
        'K2_bar1_vs_GDM_cv2': angle(k2p0, cv_p),
    }
    theta_cs = float(models[0]['three_channel_angle_to_gdm_cs2_deg'])
    theta_cv = float(models[0]['three_channel_angle_to_gdm_cv2_deg'])
    primary_pass = bool(theta_cs >= THRESHOLD_DEG and theta_cv >= THRESHOLD_DEG)
    classification = CLASS_SEPARATED if primary_pass else CLASS_OVERLAP

    out = {
        'schema': 'dsir.k2_matter_weyl_slip_direction_control.v0.1',
        'experiment': 'Exp071F',
        'status': STATUS,
        'classification': classification,
        'primary_pass': primary_pass,
        'preregistered_threshold_deg': THRESHOLD_DEG,
        'primary_k2_point': 'bar1',
        'frozen_z': Z.tolist(),
        'frozen_k_h_mpc': K.tolist(),
        'definition': {
            'r_P': 'ln(P_model/P_ref)',
            'r_W': 'ln |(phi+psi)_model/(phi+psi)_ref|',
            'delta_slip': '[(phi-psi)/(phi+psi)]_model-reference',
            'equalization': 'each channel scale is the max tangent norm of immutable GDM cs2/cv2 1e-7 axes; K2 never sets scales',
        },
        'parent_binding': {
            'Exp071C_run': 33020201997,
            'GDM_metric_run': 32774198185,
            'Exp071E_run': 33177588360,
            'Exp071E_classification': exp071e['classification'],
        },
        'gdm_equalization_scales': {'s_P': s_p, 's_W': s_w, 's_S': s_s},
        'matter_only_primary_angles_deg': matter_angles,
        'two_channel_integrity_angles_deg': {
            'K2_bar1_vs_GDM_cs2': models[0]['two_channel_angle_to_gdm_cs2_deg'],
            'K2_bar1_vs_GDM_cv2': models[0]['two_channel_angle_to_gdm_cv2_deg'],
        },
        'three_channel_primary_angles_deg': {
            'K2_bar1_vs_GDM_cs2': theta_cs,
            'K2_bar1_vs_GDM_cv2': theta_cv,
        },
        'K2_models': models,
        'robustness_nonclassifying': {
            'max_three_channel_angle_to_bar1_deg': max(float(m['three_channel_angle_to_primary_bar1_deg']) for m in models),
            'three_channel_family_centered_svd': svd_summary(u_k2_3),
        },
        'interpretation_boundary': [
            'PASS would separate only this K2 control from the two tested GDM local axes under this three-channel metric',
            'FAIL would retain a known-sector/local-GDM degeneracy even after adding matter response',
            'no microscopic uniqueness or observational preference is tested',
            'G7 G8 G9 remain open',
        ],
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }
    Path(args.json).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print('EXP071F_CLASSIFICATION', classification)
    print('MATTER_ONLY_ANGLES_DEG', matter_angles)
    print('THREE_CHANNEL_ANGLES_DEG', out['three_channel_primary_angles_deg'])
    print('ROBUSTNESS', out['robustness_nonclassifying'])


if __name__ == '__main__':
    main()
