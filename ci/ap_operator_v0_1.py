#!/usr/bin/env python3
"""Experiment 035: hard method gate for the calibration-free AP operator."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import cumulative_trapezoid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dsir.ap_operator import (
    dh_over_dm_log_response,
    fap_log_response,
    fap_log_response_linear,
)


def direct_fap(z, e):
    chi = np.concatenate(([0.0], cumulative_trapezoid(1.0 / e, z)))
    return e * chi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default="ap_operator_v0_1.json")
    args = ap.parse_args()

    z = np.linspace(0.0, 2.33, 16001)
    om = 0.31
    e_ref = np.sqrt(om * (1 + z) ** 3 + (1 - om))
    w = -0.93
    e_model = np.sqrt(om * (1 + z) ** 3 + (1 - om) * (1 + z) ** (3 * (1 + w)))

    q = np.log(e_model / e_ref)
    zstar = 0.51
    q_anchor = q - np.interp(zstar, z, q)

    predicted = fap_log_response(z, e_ref, q_anchor)
    f_ref = direct_fap(z, e_ref)
    f_model = direct_fap(z, e_model)
    direct = np.zeros_like(z)
    direct[1:] = np.log(f_model[1:] / f_ref[1:])

    direct_error = float(np.max(np.abs(predicted[1:] - direct[1:])))
    calibration_error = float(np.max(np.abs(
        fap_log_response(z, e_ref, q_anchor + 0.731) - predicted
    )))
    sign_error = float(np.max(np.abs(
        dh_over_dm_log_response(z, e_ref, q_anchor) + predicted
    )))

    shape = z / (1 + z) - 0.2 * z
    linear_errors = []
    for eps in (1e-3, 5e-4):
        exact = fap_log_response(z, e_ref, eps * shape)
        linear = fap_log_response_linear(z, e_ref, eps * shape)
        linear_errors.append(float(np.max(np.abs(exact[1:] - linear[1:]))))
    linear_halving_ratio = linear_errors[1] / linear_errors[0]

    thresholds = {
        "direct_wcdm_logFAP_error_max": 1e-11,
        "calibration_mode_error_max": 1e-12,
        "DH_over_DM_sign_identity_error_max": 1e-14,
        "linear_remainder_halving_ratio_max": 0.27,
    }
    failures = []
    if direct_error > thresholds["direct_wcdm_logFAP_error_max"]:
        failures.append("direct_wcdm_bridge")
    if calibration_error > thresholds["calibration_mode_error_max"]:
        failures.append("calibration_invariance")
    if sign_error > thresholds["DH_over_DM_sign_identity_error_max"]:
        failures.append("DH_over_DM_sign")
    if linear_halving_ratio > thresholds["linear_remainder_halving_ratio_max"]:
        failures.append("linear_remainder_scaling")

    targets = np.array([0.51, 0.71, 0.92, 1.32, 1.49])
    synthetic_dh_log = np.interp(targets, z, -predicted)

    status = "PASS_CALIBRATION_FREE_AP_OPERATOR_V0_1" if not failures else "FAIL_AP_OPERATOR_V0_1"
    out = {
        "schema": "dsir.observation_operator.ap.v0.1",
        "status": status,
        "failures": failures,
        "thresholds_frozen_before_hard_run": thresholds,
        "control_cosmology": {"Omega_m": om, "w_model": w, "z_star": zstar},
        "direct_wcdm_logFAP_error": direct_error,
        "calibration_mode_error": calibration_error,
        "DH_over_DM_sign_identity_error": sign_error,
        "linear_remainder_errors": linear_errors,
        "linear_remainder_halving_ratio": linear_halving_ratio,
        "shapefit_target_z": targets.tolist(),
        "synthetic_DH_over_DM_log_response": synthetic_dh_log.tolist(),
        "interpretation": [
            "an additive constant in log E is exactly quotiented by F_AP",
            "anchored DSIR r_E retains the AP information needed for DH/DM",
            "a real family comparison still requires validated background response histories covering z=0 to the measurement redshift",
            "this method gate alone does not whiten a family atlas and does not advance G7",
        ],
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
