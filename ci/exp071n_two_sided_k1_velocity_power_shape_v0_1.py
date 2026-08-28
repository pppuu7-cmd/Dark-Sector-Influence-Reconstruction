#!/usr/bin/env python3
"""Exp071N: two-sided primordial-tilt line in linear velocity-power-shape response space."""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import k2_gdm_total_velocity_direction_control_v0_1 as e71i

TH = 45.0
H = 0.67
KPIV = 0.05  # 1/Mpc
NS_REF = 0.965
NS_PLUS = 0.970
NS_MINUS = 0.960
K1_STEP = 0.005
PREREG = 'cfaf9d14fa734e155cab5dca028bc1a14d0afd46'
PASS = 'K1_TWO_SIDED_VELOCITY_POWER_SHAPE_SEPARATED_FROM_BOTH_GDM_AXES_EXP071N'
FAIL = 'K1_TWO_SIDED_VELOCITY_POWER_SHAPE_OVERLAPS_GDM_EXP071N'
INVALID = 'INVALID_FOR_SCIENCE_EXP071N'


def transfer_log_ratio(root: Path, model_prefix: str, ref_prefix: str, field: str = 't_tot') -> tuple[np.ndarray, dict]:
    model = e71i.collect_by_z(root, model_prefix, 'tk.dat')
    ref = e71i.collect_by_z(root, ref_prefix, 'tk.dat')
    rows = []
    min_abs_ref = math.inf
    sign_preserved = True
    for z in e71i.Z:
        zz = float(z)
        mv = e71i.load_transfer_core(model[zz], (field,))[field]
        rv = e71i.load_transfer_core(ref[zz], (field,))[field]
        min_abs_ref = min(min_abs_ref, float(np.min(np.abs(rv))))
        if np.any(np.abs(rv) <= 1e-30):
            raise ValueError(f'reference {field} denominator <=1e-30 at z={zz}')
        if np.any(mv * rv <= 0):
            sign_preserved = False
            raise ValueError(f'{field} sign violation at z={zz}: {model_prefix}/{ref_prefix}')
        r = np.log(np.abs(mv / rv))
        if not np.all(np.isfinite(r)):
            raise ValueError(f'nonfinite transfer log response at z={zz}')
        rows.append(r)
    mat = np.asarray(rows, dtype=float)
    return mat, {'min_abs_reference': min_abs_ref, 'sign_preserved': sign_preserved,
                 'n_nodes': int(mat.size), 'max_abs_log_response': float(np.max(np.abs(mat)))}


def ref_ttot_reproduction(fresh_root: Path, parent_root: Path) -> dict:
    ff = e71i.collect_by_z(fresh_root, 'ref_', 'tk.dat')
    pp = e71i.collect_by_z(parent_root, 'ref_', 'tk.dat')
    mx = 0.0
    per = []
    for z in e71i.Z:
        zz = float(z)
        fv = e71i.load_transfer_core(ff[zz], ('t_tot',))['t_tot']
        pv = e71i.load_transfer_core(pp[zz], ('t_tot',))['t_tot']
        if np.any(np.abs(pv) <= 1e-30):
            raise ValueError(f'parent ref t_tot too small z={zz}')
        rel = np.abs(fv - pv) / np.maximum(np.abs(pv), 1e-300)
        r = float(np.max(rel)); mx = max(mx, r)
        per.append({'z': zz, 'max_abs_relative_ttot_difference': r})
    return {'threshold': 1e-10, 'max_abs_relative_ttot_difference': mx,
            'pass': bool(mx <= 1e-10), 'per_z': per}


def shape(x: np.ndarray) -> np.ndarray:
    a = np.asarray(x, dtype=float).reshape(len(e71i.Z), len(e71i.K))
    return (a - a.mean(axis=1, keepdims=True)).reshape(-1)


def line_angle(theta_deg: float) -> float:
    return float(min(theta_deg, 180.0 - theta_deg))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--exp071m-root', required=True)
    ap.add_argument('--exp071i-root', required=True)
    ap.add_argument('--json', required=True)
    a = ap.parse_args()
    mroot = Path(a.exp071m_root)
    iroot = Path(a.exp071i_root)
    fresh = mroot / 'fresh/k1m'
    outp = Path(a.json)
    out = {'experiment': 'Exp071N', 'preregistration_commit': PREREG,
           'threshold_deg': TH, 'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}}
    try:
        # Exp071M must remain invalid for the frozen transfer-only null reason.
        mterm = json.loads((mroot / 'exp071m_two_sided_k1_velocity_shape_nuisance_v0_1.json').read_text())
        assert mterm['status'] == 'INVALID_FOR_SCIENCE_EXP071M'
        assert 'zero/nonfinite response vector plus1_ t_tot' in mterm['invalid_reason']
        iterm = json.loads((iroot / 'exp071i_k2_gdm_total_velocity_direction_control_v0_1.json').read_text())
        assert iterm['classification'] == 'K2_TOTAL_VELOCITY_SEPARATED_FROM_BOTH_GDM_AXES_EXP071I'

        pkrep = e71i.reproduce_family(fresh, iroot / 'fresh/k2', ['ref_'])
        ttrep = ref_ttot_reproduction(fresh, iroot / 'fresh/k2')
        if not pkrep['pass'] or not ttrep['pass']:
            raise ValueError(f'fresh reference reproduction failed pk={pkrep} tt={ttrep}')

        k1p_tr, k1p_meta = transfer_log_ratio(fresh, 'plus1_', 'ref_')
        k1m_tr, k1m_meta = transfer_log_ratio(fresh, 'minus1_', 'ref_')
        cs_tr, cs_meta = transfer_log_ratio(iroot / 'fresh/gdm', 'cs1em7_', 'gdm0_')
        cv_tr, cv_meta = transfer_log_ratio(iroot / 'fresh/gdm', 'cv1em7_', 'gdm0_')

        kphys = H * np.asarray(e71i.K, dtype=float)
        primordial_basis = np.log(kphys / KPIV)[None, :]
        primordial_basis = np.repeat(primordial_basis, len(e71i.Z), axis=0)

        # Full log linear-power responses, then tangent normalization with positive step magnitudes.
        k1p_raw = ((NS_PLUS - NS_REF) * primordial_basis + 2.0 * k1p_tr) / K1_STEP
        k1m_raw = ((NS_MINUS - NS_REF) * primordial_basis + 2.0 * k1m_tr) / K1_STEP
        cs_raw = (2.0 * cs_tr) / e71i.GDM_STEP
        cv_raw = (2.0 * cv_tr) / e71i.GDM_STEP

        raw = {'K1_plus': k1p_raw.reshape(-1), 'K1_minus': k1m_raw.reshape(-1),
               'GDM_cs2': cs_raw.reshape(-1), 'GDM_cv2': cv_raw.reshape(-1)}
        proj = {k: shape(v) for k, v in raw.items()}
        retained = {k: float(np.linalg.norm(proj[k]) / np.linalg.norm(raw[k])) for k in raw}
        if not all(math.isfinite(v) and v > 1e-12 for v in retained.values()):
            raise ValueError(f'unresolved full velocity-power shape projection {retained}')

        primary = {
            'K1_plus_vs_GDM_cs2_deg': e71i.angle_deg(proj['K1_plus'], proj['GDM_cs2']),
            'K1_plus_vs_GDM_cv2_deg': e71i.angle_deg(proj['K1_plus'], proj['GDM_cv2']),
            'K1_minus_vs_GDM_cs2_deg': e71i.angle_deg(proj['K1_minus'], proj['GDM_cs2']),
            'K1_minus_vs_GDM_cv2_deg': e71i.angle_deg(proj['K1_minus'], proj['GDM_cv2']),
        }
        passed = all(v >= TH for v in primary.values())
        plus_line = {
            'K1_line_vs_GDM_cs2_deg': line_angle(primary['K1_plus_vs_GDM_cs2_deg']),
            'K1_line_vs_GDM_cv2_deg': line_angle(primary['K1_plus_vs_GDM_cv2_deg']),
        }
        line_valid = {
            'cs2_abs_prediction_minus_fresh_deg': abs(plus_line['K1_line_vs_GDM_cs2_deg'] - primary['K1_minus_vs_GDM_cs2_deg']),
            'cv2_abs_prediction_minus_fresh_deg': abs(plus_line['K1_line_vs_GDM_cv2_deg'] - primary['K1_minus_vs_GDM_cv2_deg']),
        }
        anti = float(np.linalg.norm(proj['K1_plus'] + proj['K1_minus']) /
                     ((np.linalg.norm(proj['K1_plus']) + np.linalg.norm(proj['K1_minus'])) / 2.0))

        out.update({
            'status': 'COMPLETE_EXP071N',
            'representation': 'linear_velocity_power_shape',
            'response_formula': 'Delta ln P_R(k) + 2 Delta ln |t_tot|',
            'constants': {'h': H, 'k_pivot_Mpc_inv': KPIV, 'K1_step_abs_n_s': K1_STEP},
            'fresh_reference_integrity': {'matter_power': pkrep, 't_tot': ttrep},
            'transfer_only_null_diagnostic': {
                'K1_plus_max_abs_log_ttot_response': k1p_meta['max_abs_log_response'],
                'K1_minus_max_abs_log_ttot_response': k1m_meta['max_abs_log_response'],
            },
            'response_integrity': {'K1_plus_transfer': k1p_meta, 'K1_minus_transfer': k1m_meta,
                                   'GDM_cs2_transfer': cs_meta, 'GDM_cv2_transfer': cv_meta},
            'retained_shape_norm_fraction': retained,
            'primary_angles_deg': primary,
            'primary_min_angle_deg': float(min(primary.values())),
            'primary_pass': bool(passed),
            'classification': PASS if passed else FAIL,
            'K1_minus_vs_plus_mutual_angle_deg': e71i.angle_deg(proj['K1_minus'], proj['K1_plus']),
            'K1_nonlinear_antisymmetry_error': anti,
            'line_angle_prediction_from_plus_deg': plus_line,
            'line_angle_prediction_validation': line_valid,
            'GDM_cs2_vs_cv2_projected_angle_deg': e71i.angle_deg(proj['GDM_cs2'], proj['GDM_cv2']),
            'not_a_claim': ['not tracer RSD', 'not f sigma_8', 'not survey distinguishability',
                            'not covariance whitening', 'not observational nuisance marginalization',
                            'not unique microscopic identification', 'not dark-sector detection'],
        })
        outp.write_text(json.dumps(out, indent=2) + '\n')
        print('EXP071N', out['classification'])
        print('PRIMARY', primary)
        print('MIN', out['primary_min_angle_deg'])
        print('K1_MINUS_PLUS', out['K1_minus_vs_plus_mutual_angle_deg'])
        print('ANTI', anti)
        print('TRANSFER_NULL', out['transfer_only_null_diagnostic'])
        print('LINE_VALIDATION', line_valid)
    except Exception as exc:
        out.update({'status': INVALID, 'invalid_reason': f'{type(exc).__name__}: {exc}'})
        outp.write_text(json.dumps(out, indent=2) + '\n')
        print(json.dumps(out, indent=2))
        raise SystemExit(2)


if __name__ == '__main__':
    main()
