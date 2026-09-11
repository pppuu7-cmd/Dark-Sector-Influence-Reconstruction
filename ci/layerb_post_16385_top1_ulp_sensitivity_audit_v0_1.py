#!/usr/bin/env python3
import argparse
import json
import math
from pathlib import Path

EXPECTED_CLASS = "POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0"
OUT_CLASS = "POST_16385_TOP1_ULP_SENSITIVITY_AUDIT_PASS_PLUS_0_PLUS_0"


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b))


def neighbors(x):
    return [math.nextafter(x, -math.inf), x, math.nextafter(x, math.inf)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--authority", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    src = json.loads(Path(a.authority).read_text())
    assert src["classification"] == EXPECTED_CLASS
    atom = src["selected_atom"]
    coarse = float(atom["coarse_value"])
    fine = float(atom["fine_value"])
    recorded = float(atom["relative_difference"])
    assert rel(coarse, fine) == recorded

    values = []
    for c in neighbors(coarse):
        for f in neighbors(fine):
            values.append(rel(c, f))
    lo, hi = min(values), max(values)
    max_abs_shift = max(abs(v - recorded) for v in values)
    strict_tol = 1e-3

    # A ±1 ULP perturbation of both already-rounded endpoint values must not
    # remotely account for the observed ~1.25e-2 plateau.
    assert lo > strict_tol
    assert max_abs_shift < 1e-12

    out = {
        "schema": "LAYERB_POST_16385_TOP1_ULP_SENSITIVITY_AUDIT_V0_1",
        "classification": OUT_CLASS,
        "effect": "+0/+0",
        "recorded_relative_difference": recorded,
        "nine_neighbor_min_relative_difference": lo,
        "nine_neighbor_max_relative_difference": hi,
        "max_absolute_metric_shift_under_endpoint_plusminus_one_ulp": max_abs_shift,
        "coarse_ulp": math.ulp(coarse),
        "fine_ulp": math.ulp(fine),
        "strict_science_tolerance": strict_tol,
        "all_nine_neighbor_metrics_remain_above_tolerance": lo > strict_tol,
        "class_solver_invoked": False,
        "alternative_h_evaluated": False,
        "scientific_107_row_replay_executed": False,
        "scientific_classification_created": False,
        "scientific_authority_created": False,
        "next_rung_authorized": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
