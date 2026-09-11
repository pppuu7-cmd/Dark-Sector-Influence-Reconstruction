#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

REL_TOL = 1e-3
H = 1e-4
LOOKUP_REL_TOL = 1e-12
CONVERGED = "COMMON_GRID_FOURTH_REFINEMENT_CONVERGED_PLUS_0_PLUS_0"
NOT_CONVERGED = "COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0"
INVALID_INFRA = "INVALID_INFRA_PLUS_0_PLUS_0"
COARSE_TEXT_SHA = "290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7"
COARSE_NODE_SHA = "f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb"
FINE_TEXT_SHA = "90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6"
FINE_NODE_SHA = "6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515"
COARSE_PLAN_SHA = "505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0"
FINE_PLAN_SHA = "0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e"
PARENT_RETAINED_SHA = "44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7"
FULL_ORDER_SHA = "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"
PASS = "EXP073JM_TERMINAL_RESULT_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise RuntimeError(msg)


def validate(d: dict) -> dict:
    require(d.get("schema") == "EXP073JM_ARTICLE3_RECOVERED_CANONICAL_ONE_LIVE_FOURTH_REFINEMENT_RESULT_V0_2", "schema")
    require(d.get("experiment") == "Exp073JM", "experiment")
    cls = d.get("classification")
    require(cls in {CONVERGED, NOT_CONVERGED}, "terminal classification is not scientific-support valid")
    require(d.get("effect") == "+0/+0", "effect")
    require(d.get("scientific_authority_created") is False, "premature scientific authority")
    require(d.get("covariance_restriction_authorized") is False, "premature covariance authorization")
    require(d.get("Wm_S3_opened") is False, "premature Wm_S3 opening")
    require(d.get("h") == H and d.get("rel_tol") == REL_TOL, "frozen h/tolerance")
    require(d.get("native_k_per_decade_for_pk_frozen") == 20.0, "native kpd")

    latt = d.get("canonical_lattices", {})
    c = latt.get("coarse", {})
    f = latt.get("fine", {})
    require(c == {"requested_node_count":4097, "text_sha256":COARSE_TEXT_SHA, "node_sha256":COARSE_NODE_SHA}, "coarse canonical lattice")
    require(f == {"requested_node_count":8193, "text_sha256":FINE_TEXT_SHA, "node_sha256":FINE_NODE_SHA}, "fine canonical lattice")

    plan = d.get("request_plan_authority", {})
    require(plan.get("coarse_common_plan_sha256") == COARSE_PLAN_SHA, "coarse plan sha")
    require(plan.get("fine_plan_with_gl128_sha256") == FINE_PLAN_SHA, "fine plan sha")
    require(plan.get("coarse_calls_per_role") == 441, "coarse calls")
    require(plan.get("fine_calls_per_role") == 569, "fine calls")
    require(plan.get("total_get_transfer_calls") == 4040, "total calls")

    life = d.get("execution_lifecycle", {})
    require(life.get("total_solver_constructions") == 8, "solver construction count")
    require(life.get("max_live_instances") == 1, "max live")
    require(life.get("final_live_instances") == 0, "final live")
    require(life.get("cross_process_raw_operand_combination") is False, "cross-process raw operands")

    require(d.get("parent_identity_preserved") is True, "parent identity")
    require(d.get("unsupported_target_evaluations") == 0, "unsupported targets")
    lookup = d.get("max_requested_node_coordinate_rel_mismatch")
    require(isinstance(lookup, (int,float)) and math.isfinite(float(lookup)) and float(lookup) <= LOOKUP_REL_TOL, "lookup ceiling")

    conv = d.get("convergence", {})
    layer = d.get("layer_b", {})
    mx = conv.get("max_relative_component_difference")
    require(isinstance(mx, (int,float)) and math.isfinite(float(mx)), "finite convergence maximum")
    require(isinstance(layer.get("invalid_row_fraction"), (int,float)), "invalid row fraction")
    require(isinstance(layer.get("retained_after_layer_b"), int), "retained dimension")

    expected_converged = bool(
        conv.get("finite_nonzero_status_changed") is False
        and conv.get("row_label_changed") is False
        and conv.get("boss_dense_z_disagreement") is False
        and float(mx) < REL_TOL
        and float(layer["invalid_row_fraction"]) <= 0.05
        and layer["retained_after_layer_b"] >= 15
    )
    expected_cls = CONVERGED if expected_converged else NOT_CONVERGED
    require(cls == expected_cls, f"classifier mismatch expected {expected_cls}")

    expected_token = (
        "PASS_EXP073JM_RECOVERED_CANONICAL_ONE_LIVE_FOURTH_REFINEMENT_CONVERGED_V0_2"
        if expected_converged else
        "PASS_EXP073JM_RECOVERED_CANONICAL_ONE_LIVE_FOURTH_REFINEMENT_NOT_CONVERGED_V0_2"
    )
    require(d.get("token") == expected_token, "terminal token mismatch")

    return {
        "classification": PASS,
        "effect": "+0/+0",
        "validated_jm_classification": cls,
        "max_relative_component_difference": float(mx),
        "retained_after_layer_b": layer["retained_after_layer_b"],
        "invalid_row_fraction": float(layer["invalid_row_fraction"]),
        "total_solver_constructions": life["total_solver_constructions"],
        "max_live_instances": life["max_live_instances"],
        "total_get_transfer_calls": plan["total_get_transfer_calls"],
        "unsupported_target_evaluations": d["unsupported_target_evaluations"],
        "max_requested_node_coordinate_rel_mismatch": float(lookup),
        "branch_selected": "CONVERGED_FRESH_CLOSURE" if expected_converged else "NOT_CONVERGED_8193_TO_16385",
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": PASS,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--result", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rp = Path(a.result)
    d = json.loads(rp.read_text())
    out = validate(d)
    out["source_result_json_sha256"] = sha256(rp)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(PASS)
    print(json.dumps(out, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
