#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

H = 1e-4
REL_TOL = 1e-3
LOOKUP_REL_TOL = 1e-12
NATIVE_KPD = 20.0
CAPACITY = 18432
PARSER_CAPACITY = 524288
NEXT_REFINEMENT_CONVERGED = "COMMON_GRID_NEXT_REFINEMENT_CONVERGED_PLUS_0_PLUS_0"
SCI_PASS = "PASS_PHYSICAL_SUPPORT_ARTICLE3_SHARED_GRID_POST_16385_V0_1"
SCI_FAIL = "FAIL_PHYSICAL_SUPPORT_ARTICLE3_SHARED_GRID_POST_16385_V0_1"
NUM_UNRES = "NUMERICALLY_UNRESOLVED_POST_16385_LAYERB_CLOSURE_V0_1"
INVALID_INFRA = "INVALID_INFRA_PLUS_0_PLUS_0"
COARSE_TEXT_SHA = "90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6"
COARSE_NODE_SHA = "6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515"
FINE_TEXT_SHA = "7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69"
FINE_NODE_SHA = "3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975"
COARSE_PLAN_SHA = "505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0"
FINE_PLAN_SHA = "0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e"
PARENT_RETAINED_SHA = "44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7"
FULL_ORDER_SHA = "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"
CANONICAL_16385_AUTH_CLASS = "CANONICAL_16385_ANCHOR_SELECTED_QUORUM_PASS_PLUS_0_PLUS_0"
PLAN_CLASS = "RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0"


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def is_sha256(x) -> bool:
    return isinstance(x, str) and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def validate_activation(path: str | Path) -> dict:
    jm = json.loads(Path(path).read_text())
    if jm.get("classification") != NEXT_REFINEMENT_CONVERGED:
        raise RuntimeError("post-16385 scientific closure activation condition not met")
    if jm.get("artifact_verified_independently") is not True:
        raise RuntimeError("activating next-refinement artifact is not independently verified")
    if not is_sha256(jm.get("artifact_zip_sha256")) or not is_sha256(jm.get("result_json_sha256")):
        raise RuntimeError("activating next-refinement provenance digest missing")
    return jm


def validate_canonical_16385(path: str | Path) -> dict:
    d = json.loads(Path(path).read_text())
    if (
        d.get("classification") != CANONICAL_16385_AUTH_CLASS
        or d.get("artifact_verified_independently") is not True
        or d.get("successor_branch_activated") is not False
        or d.get("successor_execution_authorized") is not False
        or d.get("scientific_response_read") is not False
        or d.get("class_solver_invoked") is not False
        or d.get("requested_node_count") != 16385
        or d.get("guard_counts") != [0, 1]
        or d.get("node_payload_sha256") != FINE_NODE_SHA
        or d.get("u64hex_sha256") != FINE_TEXT_SHA
        or d.get("anchor_8193_node_sha256") != COARSE_NODE_SHA
        or d.get("anchor_8193_u64hex_sha256") != COARSE_TEXT_SHA
        or d.get("anchor_match_count", 0) < d.get("minimum_anchor_quorum", 999)
    ):
        raise RuntimeError("invalid canonical 16385 authority")
    return d


def validate_plan_authority(path: str | Path) -> dict:
    d = json.loads(Path(path).read_text())
    shape = d.get("execution_shape_if_recovered_one_live", {})
    if (
        d.get("classification") != PLAN_CLASS
        or d.get("artifact_verified_independently") is not True
        or d.get("scientific_response_read") is not False
        or d.get("class_solver_invoked") is not False
        or d.get("parent_retained_count") != 107
        or d.get("parent_retained_id_sha256") != PARENT_RETAINED_SHA
        or d.get("parent_full_order_sha256") != FULL_ORDER_SHA
        or d.get("coarse_common_plan_sha256") != COARSE_PLAN_SHA
        or d.get("fine_plan_with_gl128_sha256") != FINE_PLAN_SHA
        or shape.get("coarse_get_transfer_calls_per_role") != 441
        or shape.get("fine_get_transfer_calls_per_role") != 569
        or shape.get("total_get_transfer_calls_all_roles") != 4040
        or shape.get("total_solver_constructions") != 8
        or shape.get("max_live_instances") != 1
    ):
        raise RuntimeError("invalid response-blind request-plan authority")
    return d


def validate_capacity_patch(path: str | Path) -> dict:
    d = json.loads(Path(path).read_text())
    if (
        d.get("old_capacity") != 30
        or d.get("new_capacity") != CAPACITY
        or d.get("replacement_count") != 1
        or d.get("parser_old_argument_capacity") != 1024
        or d.get("parser_new_argument_capacity") != PARSER_CAPACITY
        or d.get("parser_replacement_count") != 1
    ):
        raise RuntimeError("invalid post-16385 closure capacity patch")
    return d


def execute(a) -> dict:
    jm = validate_activation(a.jm_authority)
    canon16385 = validate_canonical_16385(a.canonical_16385_authority)
    validate_plan_authority(a.request_plan_authority)
    validate_capacity_patch(a.capacity_patch_record)

    engine = load_module("recovered_jl_engine_for_post_jm_closure", a.recovered_jl_script)
    ir = load_module("exp073ir_post_jm_closure", a.ir_script)
    jj = load_module("exp073jj_post_jm_closure", a.jj_script)
    planmod = load_module("post_jm_request_plan_guard", a.request_plan_script)

    if (
        engine.H != H
        or engine.REL_TOL != REL_TOL
        or engine.LOOKUP_REL_TOL != LOOKUP_REL_TOL
        or engine.NATIVE_KPD != NATIVE_KPD
        or engine.COARSE_PLAN_SHA != COARSE_PLAN_SHA
        or engine.FINE_PLAN_SHA != FINE_PLAN_SHA
        or jj.H != H
        or jj.REL_TOL != REL_TOL
        or jj.LOOKUP_REL_TOL != LOOKUP_REL_TOL
        or jj.NATIVE_KPD != NATIVE_KPD
        or ir.H != H
        or ir.REL_TOL != REL_TOL
        or ir.PARENT_RETAINED_SHA != PARENT_RETAINED_SHA
        or ir.FULL_ORDER_SHA != FULL_ORDER_SHA
    ):
        raise RuntimeError("frozen parent/engine constants mismatch")
    jj.CAPACITY = CAPACITY

    scratch = Path(a.scratch)
    scratch.mkdir(parents=True, exist_ok=True)
    plan_out = scratch / "request_plan_guard.json"
    plan_guard = engine.run_request_plan_audit(planmod, a, plan_out)
    if (
        plan_guard.get("classification") != PLAN_CLASS
        or plan_guard.get("scientific_response_read") is not False
        or plan_guard.get("class_solver_invoked") is not False
        or plan_guard.get("coarse_common_plan_sha256") != COARSE_PLAN_SHA
        or plan_guard.get("fine_plan_with_gl128_sha256") != FINE_PLAN_SHA
        or plan_guard.get("execution_shape_if_recovered_one_live", {}).get("total_get_transfer_calls_all_roles") != 4040
    ):
        raise RuntimeError("live request-plan guard mismatch")

    coarse = engine.load_nodes(a.coarse, 8193, COARSE_TEXT_SHA, COARSE_NODE_SHA)
    fine = engine.load_nodes(a.fine, 16385, FINE_TEXT_SHA, FINE_NODE_SHA)

    engine.PlannerSuite.reset()
    planner_dir = scratch / "planner_ir"
    planner_dir.mkdir(parents=True, exist_ok=True)
    planner_result = engine.run_ir_with_suite(ir, engine.PlannerSuite, a, planner_dir, planner_dir / "planner_result.json")
    if len(engine.PlannerSuite.instances) != 4:
        raise RuntimeError("unexpected inherited suite count")
    slots = [x.slot for x in engine.PlannerSuite.instances]
    counts = [len(x.calls) for x in engine.PlannerSuite.instances]
    if slots != [10.0, 10.0, 20.0, 20.0] or counts != [377, 64, 441, 128]:
        raise RuntimeError(f"inherited request traversal mismatch slots={slots} counts={counts}")

    coarse_calls = engine.PlannerSuite.instances[0].calls + engine.PlannerSuite.instances[1].calls
    fine_calls = engine.PlannerSuite.instances[2].calls + engine.PlannerSuite.instances[3].calls
    if len(coarse_calls) != 441 or len(fine_calls) != 569:
        raise RuntimeError("merged request count mismatch")
    if engine.calls_scalar_count(coarse_calls) != 83666 or engine.calls_scalar_count(fine_calls) != 121682:
        raise RuntimeError("merged request scalar-count mismatch")

    tracker = {"constructions": 0, "live": 0, "max_live": 0}
    coarse_responses, coarse_audit, coarse_kkeys = engine.evaluate_lattice(
        jj, coarse, coarse_calls, a.baseline, a.precision, "coarse", tracker
    )
    if tracker != {"constructions": 4, "live": 0, "max_live": 1}:
        raise RuntimeError(f"coarse lifecycle mismatch {tracker}")
    fine_responses, fine_audit, fine_kkeys = engine.evaluate_lattice(
        jj, fine, fine_calls, a.baseline, a.precision, "fine", tracker
    )
    if tracker != {"constructions": 8, "live": 0, "max_live": 1}:
        raise RuntimeError(f"full lifecycle mismatch {tracker}")

    unsupported = int(coarse_audit["unsupported_target_evaluations"]) + int(fine_audit["unsupported_target_evaluations"])
    lookup = max(
        float(coarse_audit["max_requested_node_coordinate_rel_mismatch"]),
        float(fine_audit["max_requested_node_coordinate_rel_mismatch"]),
    )
    if unsupported != 0 or lookup > LOOKUP_REL_TOL:
        raise RuntimeError("unsupported target or lookup mismatch")

    replay_plans = [
        engine.PlannerSuite.instances[0].calls,
        engine.PlannerSuite.instances[1].calls,
        engine.PlannerSuite.instances[2].calls,
        engine.PlannerSuite.instances[3].calls,
    ]
    replay_responses = [
        coarse_responses[:377], coarse_responses[377:],
        fine_responses[:441], fine_responses[441:],
    ]
    engine.ReplaySuite.configure(replay_plans, replay_responses, {10.0: coarse_kkeys, 20.0: fine_kkeys})
    replay_dir = scratch / "fresh_scientific_replay_ir"
    replay_dir.mkdir(parents=True, exist_ok=True)
    d = engine.run_ir_with_suite(ir, engine.ReplaySuite, a, replay_dir, replay_dir / "inner_ir.json")
    if len(engine.ReplaySuite.instances) != 4 or any(x.pos != len(x.plan) or not x.closed for x in engine.ReplaySuite.instances):
        raise RuntimeError("IR replay did not consume exact request sequence")
    if any(d.get(k) is not False for k in ("covariance_read", "whitening_read", "nuisance_read", "relation_null_read")):
        raise RuntimeError("forbidden downstream quantity read")
    if d.get("status") == ir.INVALID or "error" in d:
        raise RuntimeError(f"inner IR invalid: {d.get('error', d.get('status'))}")

    parent = d.get("parent", {})
    layer = d.get("layer_b", {})
    conv = d.get("convergence", {})
    exact_parent = bool(
        parent.get("retained_count") == 107
        and parent.get("retained_id_sha256") == PARENT_RETAINED_SHA
        and parent.get("full_order_sha256") == FULL_ORDER_SHA
    )
    mx = conv.get("max_relative_component_difference")
    structural_ok = bool(
        exact_parent
        and unsupported == 0
        and lookup <= LOOKUP_REL_TOL
        and conv.get("finite_nonzero_status_changed") is False
        and conv.get("row_label_changed") is False
        and conv.get("boss_dense_z_disagreement") is False
        and isinstance(mx, (int, float))
        and math.isfinite(float(mx))
    )
    if not structural_ok:
        raise RuntimeError("fresh closure structural/provenance condition failed")

    numerical_ok = bool(float(mx) < REL_TOL)
    physical_ok = bool(
        numerical_ok
        and isinstance(layer.get("invalid_row_fraction"), (int, float))
        and float(layer["invalid_row_fraction"]) <= ir.FB_MAX
        and isinstance(layer.get("retained_after_layer_b"), int)
        and layer["retained_after_layer_b"] >= ir.MIN_RETAINED
    )

    if not numerical_ok:
        classification = NUM_UNRES
    elif not physical_ok:
        classification = SCI_FAIL
    else:
        classification = SCI_PASS

    candidate_pass = classification == SCI_PASS
    return {
        "schema": "POST_16385_CONVERGED_FRESH_LAYERB_SCIENTIFIC_CLOSURE_RESULT_V0_1",
        "classification": classification,
        "candidate_scientific_pass": candidate_pass,
        "effect": "+0/+0 until independent artifact verification",
        "scientific_authority_created": False,
        "downstream_covariance_stage_may_be_preregistered_after_independent_verification": candidate_pass,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "h": H,
        "rel_tol": REL_TOL,
        "native_k_per_decade_for_pk_frozen": NATIVE_KPD,
        "activation_authority": {
            "next_refinement_classification": jm.get("classification"),
            "next_refinement_run_id": jm.get("run_id"),
            "next_refinement_job_id": jm.get("job_id"),
            "next_refinement_workflow_head_sha": jm.get("workflow_head_sha"),
            "next_refinement_artifact_id": jm.get("artifact_id"),
            "next_refinement_artifact_zip_sha256": jm.get("artifact_zip_sha256"),
            "next_refinement_result_json_sha256": jm.get("result_json_sha256"),
            "response_values_reused": False,
        },
        "canonical_lattices": {
            "coarse": {"requested_node_count": 8193, "text_sha256": COARSE_TEXT_SHA, "node_sha256": COARSE_NODE_SHA},
            "fine": {"requested_node_count": 16385, "text_sha256": FINE_TEXT_SHA, "node_sha256": FINE_NODE_SHA},
        },
        "canonical_16385_authority": {
            "classification": canon16385.get("classification"),
            "run_id": canon16385.get("run_id"),
            "artifact_id": canon16385.get("artifact_id"),
        },
        "request_plan_authority": {
            "coarse_common_plan_sha256": COARSE_PLAN_SHA,
            "fine_plan_with_gl128_sha256": FINE_PLAN_SHA,
            "total_get_transfer_calls": 4040,
        },
        "execution_lifecycle": {
            "total_solver_constructions": tracker["constructions"],
            "max_live_instances": tracker["max_live"],
            "final_live_instances": tracker["live"],
            "cross_process_raw_operand_combination": False,
        },
        "parent_identity_preserved": exact_parent,
        "response_engine_audit": {"coarse": coarse_audit, "fine": fine_audit},
        "unsupported_target_evaluations": unsupported,
        "max_requested_node_coordinate_rel_mismatch": lookup,
        "convergence": conv,
        "layer_b": layer,
        "planner_inner_status_ignored": planner_result.get("status"),
        "inner_status_for_accounting_only": d.get("status"),
        "token": (
            "CANDIDATE_POST_16385_LAYERB_SCIENTIFIC_PASS_REQUIRES_INDEPENDENT_VERIFICATION"
            if candidate_pass else classification
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jm-authority", required=True)
    ap.add_argument("--canonical-16385-authority", required=True)
    ap.add_argument("--recovered-jl-script", required=True)
    for x in (
        "ir-script", "jj-script", "request-plan-script", "request-plan-authority",
        "parent-root", "parent-authority", "manifest", "angular-root", "expim-root",
        "boss-root", "source", "lens", "camb-root", "expz2-script", "exp073iq-script",
        "baseline", "precision", "coarse", "fine", "capacity-patch-record", "scratch", "out",
    ):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    out = Path(a.out)
    try:
        result = execute(a)
    except Exception as e:
        result = {
            "schema": "POST_16385_CONVERGED_FRESH_LAYERB_SCIENTIFIC_CLOSURE_RESULT_V0_1",
            "classification": INVALID_INFRA,
            "candidate_scientific_pass": False,
            "effect": "+0/+0",
            "scientific_authority_created": False,
            "covariance_restriction_authorized": False,
            "Wm_S3_opened": False,
            "error": f"{type(e).__name__}: {e}",
            "token": INVALID_INFRA,
        }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    print("CLASSIFICATION", result["classification"])
    if "error" in result:
        print("ERROR", result["error"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
