#!/usr/bin/env python3
import argparse
import json
import math
from pathlib import Path

EXPECTED_CLASS = "POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0"
OUT_CLASS = "POST_16385_TOP1_CANCELLATION_AMPLIFICATION_AUDIT_PASS_PLUS_0_PLUS_0"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--authority", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    src = json.loads(Path(a.authority).read_text())
    assert src["classification"] == EXPECTED_CLASS
    assert src["primary_component_reproduced"] is True
    assert src["relative_reproduction_error"] == 0.0
    assert src["execution_lifecycle"] == {"constructions": 8, "max_live": 1, "live": 0}
    assert src["unsupported_target_evaluations"] == 0
    assert src["max_requested_node_coordinate_rel_mismatch"] <= 1e-12
    assert src["scientific_authority_created"] is False
    assert src["next_rung_authorized"] is False
    assert src["covariance_restriction_authorized"] is False
    assert src["Wm_S3_opened"] is False

    raw = src["cross_grid_raw_role_relative_differences"]
    assert set(raw) == {"alpha_minus", "beta_minus", "beta_plus", "reference"}
    raw_max = max(float(v) for v in raw.values())
    raw_min = min(float(v) for v in raw.values())
    beta_response = float(src["beta_response_cross_grid_relative_difference"])
    beta_numerator = float(src["beta_numerator_cross_grid_relative_difference"])
    c0 = float(src["beta_cancellation_scale_8193"])
    c1 = float(src["beta_cancellation_scale_16385"])
    assert all(math.isfinite(x) and x >= 0.0 for x in [raw_max, raw_min, beta_response, beta_numerator, c0, c1])
    assert raw_max > 0.0 and c0 > 0.0 and c1 > 0.0

    cancellation_scale_relative_difference = abs(c1 - c0) / max(abs(c0), abs(c1))
    amplification_vs_max_raw_role = beta_response / raw_max
    amplification_vs_min_raw_role = beta_response / raw_min

    out = {
        "schema": "LAYERB_POST_16385_TOP1_CANCELLATION_AMPLIFICATION_AUDIT_V0_1",
        "classification": OUT_CLASS,
        "effect": "+0/+0",
        "source_classification": src["classification"],
        "selected_atom": src["selected_atom"],
        "raw_role_relative_differences": raw,
        "max_raw_role_relative_difference": raw_max,
        "min_raw_role_relative_difference": raw_min,
        "beta_response_cross_grid_relative_difference": beta_response,
        "beta_numerator_cross_grid_relative_difference": beta_numerator,
        "beta_cancellation_scale_8193": c0,
        "beta_cancellation_scale_16385": c1,
        "cancellation_scale_relative_difference": cancellation_scale_relative_difference,
        "response_to_max_raw_role_amplification_factor": amplification_vs_max_raw_role,
        "response_to_min_raw_role_amplification_factor": amplification_vs_min_raw_role,
        "alternative_h_evaluated": False,
        "scientific_107_row_replay_executed": False,
        "class_solver_invoked": False,
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
