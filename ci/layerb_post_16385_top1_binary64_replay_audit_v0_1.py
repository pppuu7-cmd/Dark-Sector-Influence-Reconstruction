#!/usr/bin/env python3
import argparse
import json
import math
from pathlib import Path

EXPECTED_CLASS = "POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0"
OUT_CLASS = "POST_16385_TOP1_BINARY64_REPLAY_AUDIT_PASS_PLUS_0_PLUS_0"


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b))


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
    replay = rel(coarse, fine)

    assert math.isfinite(coarse) and math.isfinite(fine) and math.isfinite(recorded)
    assert float.hex(float(atom["target_k"])) == atom["target_k_binary64_hex"]
    assert float.hex(float(atom["z"])) == atom["z_binary64_hex"]
    assert replay == recorded
    assert replay == float(src["beta_response_cross_grid_relative_difference"])
    assert replay == float(src["beta_numerator_cross_grid_relative_difference"])
    assert src["relative_reproduction_error"] == 0.0

    out = {
        "schema": "LAYERB_POST_16385_TOP1_BINARY64_REPLAY_AUDIT_V0_1",
        "classification": OUT_CLASS,
        "effect": "+0/+0",
        "coarse_value": coarse,
        "coarse_hex": float.hex(coarse),
        "fine_value": fine,
        "fine_hex": float.hex(fine),
        "absolute_difference": abs(fine - coarse),
        "relative_difference_replayed": replay,
        "relative_difference_recorded": recorded,
        "bitwise_binary64_metric_reproduced": replay == recorded,
        "target_k_hex_reproduced": True,
        "z_hex_reproduced": True,
        "strict_science_tolerance": 1e-3,
        "ratio_to_strict_science_tolerance": replay / 1e-3,
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
