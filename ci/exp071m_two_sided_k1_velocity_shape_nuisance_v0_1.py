#!/usr/bin/env python3
"""Exp071M: two-sided primordial-tilt nuisance vs immutable GDM velocity-shape rays."""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import k2_gdm_total_velocity_direction_control_v0_1 as e71i

TH = 45.0
STEP = 0.005
PREREG = 'e3c0c7315ccb78d0a292db765eda172113f664bd'
PASS = 'K1_TWO_SIDED_VELOCITY_SHAPE_SEPARATED_FROM_BOTH_GDM_AXES_EXP071M'
FAIL = 'K1_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071M'
INVALID = 'INVALID_FOR_SCIENCE_EXP071M'


def shape(v: np.ndarray) -> np.ndarray:
    x = np.asarray(v, float).reshape(len(e71i.Z), len(e71i.K))
    return (x - x.mean(axis=1, keepdims=True)).reshape(-1)


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
        r = float(np.max(rel))
        mx = max(mx, r)
        per.append({'z': zz, 'max_abs_relative_ttot_difference': r})
    return {'threshold': 1e-10, 'max_abs_relative_ttot_difference': mx,
            'pass': bool(mx <= 1e-10), 'per_z': per}


def line_angle(theta_deg: float) -> float:
    return float(min(theta_deg, 180.0 - theta_deg))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--fresh-k1', required=True)
    ap.add_argument('--parent-root', required=True)
    ap.add_argument('--json', required=True)
    a = ap.parse_args()
    fresh = Path(a.fresh_k1)
    parent = Path(a.parent_root)
    outp = Path(a.json)
    out = {
        'experiment': 'Exp071M',
        'preregistration_commit': PREREG,
        'threshold_deg': TH,
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }
    try:
        term = json.loads((parent / 'exp071i_k2_gdm_total_velocity_direction_control_v0_1.json').read_text())
        assert term['classification'] == 'K2_TOTAL_VELOCITY_SEPARATED_FROM_BOTH_GDM_AXES_EXP071I'

        pkrep = e71i.reproduce_family(fresh, parent / 'fresh/k2', ['ref_'])
        ttrep = ref_ttot_reproduction(fresh, parent / 'fresh/k2')
        if not pkrep['pass'] or not ttrep['pass']:
            raise ValueError(f'fresh reference reproduction failed pk={pkrep} tt={ttrep}')

        plus_raw, plus_meta = e71i.response_vector(fresh, 'plus1_', 'ref_', 't_tot')
        minus_raw, minus_meta = e71i.response_vector(fresh, 'minus1_', 'ref_', 't_tot')
        cs_raw, cs_meta = e71i.response_vector(parent / 'fresh/gdm', 'cs1em7_', 'gdm0_', 't_tot')
        cv_raw, cv_meta = e71i.response_vector(parent / 'fresh/gdm', 'cv1em7_', 'gdm0_', 't_tot')

        # Preserve actual displacement orientation: divide both +/- K1 responses by positive |Delta n_s|.
        plus = shape(plus_raw / STEP)
        minus = shape(minus_raw / STEP)
        cs = shape(cs_raw / e71i.GDM_STEP)
        cv = shape(cv_raw / e71i.GDM_STEP)
        raws = {
            'K1_plus': plus_raw / STEP,
            'K1_minus': minus_raw / STEP,
            'GDM_cs2': cs_raw / e71i.GDM_STEP,
            'GDM_cv2': cv_raw / e71i.GDM_STEP,
        }
        projs = {'K1_plus': plus, 'K1_minus': minus, 'GDM_cs2': cs, 'GDM_cv2': cv}
        retained = {k: float(np.linalg.norm(projs[k]) / np.linalg.norm(raws[k])) for k in projs}
        if not all(math.isfinite(v) and v > 1e-12 for v in retained.values()):
            raise ValueError(f'unresolved shape projection {retained}')

        primary = {
            'K1_plus_vs_GDM_cs2_deg': e71i.angle_deg(plus, cs),
            'K1_plus_vs_GDM_cv2_deg': e71i.angle_deg(plus, cv),
            'K1_minus_vs_GDM_cs2_deg': e71i.angle_deg(minus, cs),
            'K1_minus_vs_GDM_cv2_deg': e71i.angle_deg(minus, cv),
        }
        passed = all(v >= TH for v in primary.values())
        plus_line = {
            'K1_line_vs_GDM_cs2_deg': line_angle(primary['K1_plus_vs_GDM_cs2_deg']),
            'K1_line_vs_GDM_cv2_deg': line_angle(primary['K1_plus_vs_GDM_cv2_deg']),
        }
        line_validation = {
            'cs2_abs_prediction_minus_fresh_deg': abs(plus_line['K1_line_vs_GDM_cs2_deg'] - primary['K1_minus_vs_GDM_cs2_deg']),
            'cv2_abs_prediction_minus_fresh_deg': abs(plus_line['K1_line_vs_GDM_cv2_deg'] - primary['K1_minus_vs_GDM_cv2_deg']),
        }
        anti = float(np.linalg.norm(plus + minus) / ((np.linalg.norm(plus) + np.linalg.norm(minus)) / 2.0))

        out.update({
            'status': 'COMPLETE_EXP071M',
            'fresh_reference_integrity': {'matter_power': pkrep, 't_tot': ttrep},
            'response_integrity': {'K1_plus': plus_meta, 'K1_minus': minus_meta,
                                   'GDM_cs2': cs_meta, 'GDM_cv2': cv_meta},
            'retained_shape_norm_fraction': retained,
            'primary_angles_deg': primary,
            'primary_min_angle_deg': float(min(primary.values())),
            'primary_pass': bool(passed),
            'classification': PASS if passed else FAIL,
            'K1_minus_vs_plus_mutual_angle_deg': e71i.angle_deg(minus, plus),
            'K1_nonlinear_antisymmetry_error': anti,
            'line_angle_prediction_from_plus_deg': plus_line,
            'line_angle_prediction_validation': line_validation,
            'GDM_cs2_vs_cv2_projected_angle_deg': e71i.angle_deg(cs, cv),
            'frozen_parameter_points': {'reference_n_s': 0.965, 'plus_n_s': 0.970,
                                        'minus_n_s': 0.960, 'step_abs_n_s': STEP},
            'interpretation_boundary': 'K1 is treated as a physically two-sided nuisance line. Actual +/- displacement orientations are preserved. PASS/FAIL is theory-space velocity-shape geometry only.',
            'not_a_claim': ['not tracer RSD', 'not survey distinguishability',
                            'not covariance whitening', 'not observational nuisance marginalization',
                            'not unique microscopic identification', 'not dark-sector detection'],
        })
        outp.write_text(json.dumps(out, indent=2) + '\n')
        print('EXP071M', out['classification'])
        print('PRIMARY', primary)
        print('MIN', out['primary_min_angle_deg'])
        print('K1_MINUS_PLUS', out['K1_minus_vs_plus_mutual_angle_deg'])
        print('ANTI', anti)
        print('LINE_PRED', plus_line)
        print('LINE_VALIDATION', line_validation)
    except Exception as exc:
        out.update({'status': INVALID, 'invalid_reason': f'{type(exc).__name__}: {exc}'})
        outp.write_text(json.dumps(out, indent=2) + '\n')
        print(json.dumps(out, indent=2))
        raise SystemExit(2)


if __name__ == '__main__':
    main()
