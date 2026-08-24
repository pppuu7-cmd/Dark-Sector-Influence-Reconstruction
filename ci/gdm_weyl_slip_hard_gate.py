#!/usr/bin/env python3
import argparse, json, math

THRESHOLDS = {
    "r_W_angle_deg_max": 1.0,
    "delta_slip_angle_deg_min": 120.0,
    "combined_equalized_angle_deg_min": 45.0,
    "tangent_convergence_angle_deg_max": 1.0,
    "relative_l2_change_max": 0.02,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()
    d = json.load(open(args.input))
    g = d["geometry"]
    rw = g["r_W"]
    sl = g["delta_slip"]

    checks = {
        "r_W_angle_1e-7": rw["cs2_cv2_angle_deg_at_1e-7"] <= THRESHOLDS["r_W_angle_deg_max"],
        "r_W_angle_1e-6": rw["cs2_cv2_angle_deg_at_1e-6"] <= THRESHOLDS["r_W_angle_deg_max"],
        "slip_angle_1e-7": sl["cs2_cv2_angle_deg_at_1e-7"] >= THRESHOLDS["delta_slip_angle_deg_min"],
        "slip_angle_1e-6": sl["cs2_cv2_angle_deg_at_1e-6"] >= THRESHOLDS["delta_slip_angle_deg_min"],
        "combined_angle": g["combined_equalized_metric_angle_deg_at_1e-7"] >= THRESHOLDS["combined_equalized_angle_deg_min"],
        "rw_cs_convergence": rw["cs2_tangent_convergence_angle_deg"] <= THRESHOLDS["tangent_convergence_angle_deg_max"],
        "rw_cv_convergence": rw["cv2_tangent_convergence_angle_deg"] <= THRESHOLDS["tangent_convergence_angle_deg_max"],
        "slip_cs_convergence": sl["cs2_tangent_convergence_angle_deg"] <= THRESHOLDS["tangent_convergence_angle_deg_max"],
        "slip_cv_convergence": sl["cv2_tangent_convergence_angle_deg"] <= THRESHOLDS["tangent_convergence_angle_deg_max"],
        "rw_cs_l2": rw["cs2_relative_l2_change_1e-7_to_1e-6"] <= THRESHOLDS["relative_l2_change_max"],
        "rw_cv_l2": rw["cv2_relative_l2_change_1e-7_to_1e-6"] <= THRESHOLDS["relative_l2_change_max"],
        "slip_cs_l2": sl["cs2_relative_l2_change_1e-7_to_1e-6"] <= THRESHOLDS["relative_l2_change_max"],
        "slip_cv_l2": sl["cv2_relative_l2_change_1e-7_to_1e-6"] <= THRESHOLDS["relative_l2_change_max"],
    }
    failures = [k for k, ok in checks.items() if not ok]
    out = {
        "schema": "dsir.gdm_weyl_slip_hard_gate.v0.1",
        "thresholds_frozen_before_rerun": THRESHOLDS,
        "observed": {
            "r_W_angle_deg_at_1e-7": rw["cs2_cv2_angle_deg_at_1e-7"],
            "r_W_angle_deg_at_1e-6": rw["cs2_cv2_angle_deg_at_1e-6"],
            "delta_slip_angle_deg_at_1e-7": sl["cs2_cv2_angle_deg_at_1e-7"],
            "delta_slip_angle_deg_at_1e-6": sl["cs2_cv2_angle_deg_at_1e-6"],
            "combined_equalized_metric_angle_deg_at_1e-7": g["combined_equalized_metric_angle_deg_at_1e-7"],
        },
        "checks": checks,
        "failures": failures,
        "pass": not failures,
        "status": "PASS_GDM_SLIP_BREAKS_LOW_K_DEGENERACY" if not failures else "FAIL_GDM_SLIP_SEPARATOR_GATE",
        "interpretation_rule": "PASS proves a reproducible channel-level separator for the calibrated GDM cs2/cv2 local rays. It is not a discovery of new physics and is not an observational evidence ratio."
    }
    with open(args.json, "w") as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(json.dumps(out, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
