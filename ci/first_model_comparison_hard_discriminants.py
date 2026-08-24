#!/usr/bin/env python3
import argparse, json

THRESHOLDS = {
    "gdm_internal_full_angle_deg_max": 1.0,
    "gdm_fr_scale_angle_deg_max": 1.0,
    "gdm_fr_time_unoriented_angle_deg_min": 15.0,
    "gdm_fr_full_oriented_angle_deg_min": 120.0,
}


def pair(rows, a, b):
    for r in rows:
        if {r["a"], r["b"]} == {a, b}:
            return r
    raise KeyError((a,b))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()
    d = json.load(open(args.input))
    full = d["full_response_pairwise_geometry"]
    rank1 = d["rank1_mode_pairwise_geometry"]

    gdm_internal = pair(full, "C3_GDM_cs2", "C3_GDM_cv2")
    cs_fr_full = pair(full, "C3_GDM_cs2", "C5_designer_fR_B0")
    cv_fr_full = pair(full, "C3_GDM_cv2", "C5_designer_fR_B0")
    cs_fr = pair(rank1, "C3_GDM_cs2", "C5_designer_fR_B0")
    cv_fr = pair(rank1, "C3_GDM_cv2", "C5_designer_fR_B0")

    checks = {
        "gdm_internal_low_k_degenerate": gdm_internal["cone_angle_deg"] <= THRESHOLDS["gdm_internal_full_angle_deg_max"],
        "gdm_cs_fr_scale_degenerate": cs_fr["scale_mode_angle_deg"] <= THRESHOLDS["gdm_fr_scale_angle_deg_max"],
        "gdm_cv_fr_scale_degenerate": cv_fr["scale_mode_angle_deg"] <= THRESHOLDS["gdm_fr_scale_angle_deg_max"],
        "gdm_cs_fr_time_separates": cs_fr["time_mode_unoriented_angle_deg"] >= THRESHOLDS["gdm_fr_time_unoriented_angle_deg_min"],
        "gdm_cv_fr_time_separates": cv_fr["time_mode_unoriented_angle_deg"] >= THRESHOLDS["gdm_fr_time_unoriented_angle_deg_min"],
        "gdm_cs_fr_full_sign_time_separates": cs_fr_full["cone_angle_deg"] >= THRESHOLDS["gdm_fr_full_oriented_angle_deg_min"],
        "gdm_cv_fr_full_sign_time_separates": cv_fr_full["cone_angle_deg"] >= THRESHOLDS["gdm_fr_full_oriented_angle_deg_min"],
    }
    failures=[k for k,v in checks.items() if not v]
    out={
        "schema":"dsir.first_model_comparison_hard_discriminants.v0.1",
        "thresholds_frozen_before_rerun":THRESHOLDS,
        "observed":{
            "gdm_cs_cv_full_angle_deg":gdm_internal["cone_angle_deg"],
            "gdm_cs_fr_scale_angle_deg":cs_fr["scale_mode_angle_deg"],
            "gdm_cv_fr_scale_angle_deg":cv_fr["scale_mode_angle_deg"],
            "gdm_cs_fr_time_unoriented_angle_deg":cs_fr["time_mode_unoriented_angle_deg"],
            "gdm_cv_fr_time_unoriented_angle_deg":cv_fr["time_mode_unoriented_angle_deg"],
            "gdm_cs_fr_full_oriented_angle_deg":cs_fr_full["cone_angle_deg"],
            "gdm_cv_fr_full_oriented_angle_deg":cv_fr_full["cone_angle_deg"],
        },
        "checks":checks,
        "failures":failures,
        "pass":not failures,
        "status":"PASS_CONDITIONAL_DEGENERACY_BREAKS" if not failures else "FAIL_CONDITIONAL_DEGENERACY_BREAKS",
        "interpretation_rule":"PASS establishes response-space conditional degeneracies and their theory-channel separators for the frozen controls. It is not observational distinguishability or a discovery claim."
    }
    json.dump(out, open(args.json,"w"), indent=2, sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    if failures: raise SystemExit(1)

if __name__ == "__main__":
    main()
