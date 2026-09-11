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
JL_CONVERGED = "COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0"
ENGINE_CONVERGED = JL_CONVERGED
ENGINE_NOT_CONVERGED = "COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0"
SCI_PASS = "PASS_PHYSICAL_SUPPORT_ARTICLE3_SHARED_GRID_V0_1"
SCI_FAIL = "FAIL_PHYSICAL_SUPPORT_ARTICLE3_SHARED_GRID_V0_1"
NUM_UNRES = "NUMERICALLY_UNRESOLVED_EXP073JN"
INVALID_INFRA = "INVALID_INFRA_PLUS_0_PLUS_0"
COARSE_NODE_SHA = "6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46"
FINE_NODE_SHA = "f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb"
COARSE_TEXT_SHA = "72c732a02b9f6f4adeab70c7792f16e4490f038544c221aed9b72a14e5b1ec47"
FINE_TEXT_SHA = "290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7"
COARSE_PLAN_SHA = "505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0"
FINE_PLAN_SHA = "0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e"


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _is_sha256(x) -> bool:
    return isinstance(x, str) and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def validate_activation(path: str | Path) -> dict:
    jl = json.loads(Path(path).read_text())
    # Frozen activation is intentionally no stricter than branch token + independent verification.
    if jl.get("classification") != JL_CONVERGED:
        raise RuntimeError("Exp073JN activation condition not met")
    if jl.get("artifact_verified_independently") is not True:
        raise RuntimeError("activating JL artifact is not independently verified")
    # Digest presence is provenance integrity, not an additional scientific activation predicate.
    if not _is_sha256(jl.get("artifact_zip_sha256")) or not _is_sha256(jl.get("result_json_sha256")):
        raise RuntimeError("activating JL authority provenance digest missing")
    return jl


def execute(a) -> dict:
    jl = validate_activation(a.jl_authority)
    engine = load_module("exp073jl_recovered_engine_for_jn", a.recovered_jl_script)

    # Pin the fresh engine science/execution contract before invoking it.
    if (
        engine.H != H
        or engine.REL_TOL != REL_TOL
        or engine.LOOKUP_REL_TOL != LOOKUP_REL_TOL
        or engine.NATIVE_KPD != NATIVE_KPD
        or engine.COARSE_NODE_SHA != COARSE_NODE_SHA
        or engine.FINE_NODE_SHA != FINE_NODE_SHA
        or engine.COARSE_TEXT_SHA != COARSE_TEXT_SHA
        or engine.FINE_TEXT_SHA != FINE_TEXT_SHA
        or engine.COARSE_PLAN_SHA != COARSE_PLAN_SHA
        or engine.FINE_PLAN_SHA != FINE_PLAN_SHA
    ):
        raise RuntimeError("recovered JL engine contract mismatch")

    # Fresh scientific traversal. No response operand/value is imported from the activating JL artifact.
    fresh = engine.execute(a)
    if fresh.get("classification") not in {ENGINE_CONVERGED, ENGINE_NOT_CONVERGED}:
        raise RuntimeError(f"fresh recovered engine invalid classification: {fresh.get('classification')}")

    conv = fresh.get("convergence", {})
    layer = fresh.get("layer_b", {})
    lifecycle = fresh.get("execution_lifecycle", {})
    plan = fresh.get("request_plan_authority", {})
    mx = conv.get("max_relative_component_difference")

    structural_ok = bool(
        fresh.get("parent_identity_preserved") is True
        and fresh.get("unsupported_target_evaluations") == 0
        and isinstance(fresh.get("max_requested_node_coordinate_rel_mismatch"), (int, float))
        and math.isfinite(float(fresh["max_requested_node_coordinate_rel_mismatch"]))
        and float(fresh["max_requested_node_coordinate_rel_mismatch"]) <= LOOKUP_REL_TOL
        and conv.get("finite_nonzero_status_changed") is False
        and conv.get("row_label_changed") is False
        and conv.get("boss_dense_z_disagreement") is False
        and lifecycle.get("total_solver_constructions") == 8
        and lifecycle.get("max_live_instances") == 1
        and lifecycle.get("final_live_instances") == 0
        and lifecycle.get("cross_process_raw_operand_combination") is False
        and plan.get("total_get_transfer_calls") == 4040
        and plan.get("coarse_common_plan_sha256") == COARSE_PLAN_SHA
        and plan.get("fine_plan_with_gl128_sha256") == FINE_PLAN_SHA
    )
    numerical_ok = bool(
        structural_ok
        and isinstance(mx, (int, float))
        and math.isfinite(float(mx))
        and float(mx) < REL_TOL
    )
    physical_ok = bool(
        numerical_ok
        and isinstance(layer.get("invalid_row_fraction"), (int, float))
        and float(layer["invalid_row_fraction"]) <= 0.05
        and isinstance(layer.get("retained_after_layer_b"), int)
        and layer["retained_after_layer_b"] >= 15
    )

    if not structural_ok:
        status = INVALID_INFRA
    elif not numerical_ok:
        status = NUM_UNRES
    elif not physical_ok:
        status = SCI_FAIL
    else:
        status = SCI_PASS

    passed = status == SCI_PASS
    return {
        "schema": "EXP073JN_ARTICLE3_RECOVERED_CANONICAL_ONE_LIVE_SCIENTIFIC_CLOSURE_RESULT_V0_2",
        "experiment": "Exp073JN",
        "status": status,
        "effect": "+0/+0",
        "scientific_authority_created": passed,
        "layer_b_physical_support_closed": passed,
        "downstream_covariance_whitening_stage_may_be_preregistered": passed,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "h": H,
        "rel_tol": REL_TOL,
        "native_k_per_decade_for_pk_frozen": NATIVE_KPD,
        "activation_authority": {
            "jl_classification": jl.get("classification"),
            "jl_run_id": jl.get("run_id"),
            "jl_job_id": jl.get("job_id"),
            "jl_workflow_head_sha": jl.get("workflow_head_sha"),
            "jl_artifact_id": jl.get("artifact_id"),
            "jl_artifact_zip_sha256": jl.get("artifact_zip_sha256"),
            "jl_result_json_sha256": jl.get("result_json_sha256"),
            "response_values_reused": False,
        },
        "canonical_lattices": {
            "coarse": {
                "requested_node_count": 2049,
                "text_sha256": COARSE_TEXT_SHA,
                "node_sha256": COARSE_NODE_SHA,
            },
            "fine": {
                "requested_node_count": 4097,
                "text_sha256": FINE_TEXT_SHA,
                "node_sha256": FINE_NODE_SHA,
            },
        },
        "fresh_engine_classification": fresh.get("classification"),
        "fresh_parent_identity_preserved": fresh.get("parent_identity_preserved"),
        "fresh_response_engine_audit": fresh.get("response_engine_audit"),
        "fresh_unsupported_target_evaluations": fresh.get("unsupported_target_evaluations"),
        "fresh_max_requested_node_coordinate_rel_mismatch": fresh.get("max_requested_node_coordinate_rel_mismatch"),
        "fresh_convergence": conv,
        "fresh_layer_b": layer,
        "fresh_execution_lifecycle": lifecycle,
        "fresh_request_plan_authority": plan,
        "structural_provenance_ok": structural_ok,
        "numerical_convergence_ok": numerical_ok,
        "physical_support_ok": physical_ok,
        "forbidden_downstream_reads": {
            "covariance": False,
            "whitening": False,
            "nuisance": False,
            "relation_null": False,
        },
        "token": (
            "PASS_EXP073JN_RECOVERED_CANONICAL_ONE_LIVE_SCIENTIFIC_CLOSURE_V0_2"
            if passed
            else (
                "EXP073JN_RECOVERED_INVALID_INFRA_V0_2"
                if status == INVALID_INFRA
                else "PASS_EXP073JN_RECOVERED_VALID_NONPASS_RESULT_V0_2"
            )
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    # Activation + engine implementation.
    ap.add_argument("--jl-authority", required=True)
    ap.add_argument("--recovered-jl-script", required=True)

    # Arguments consumed by the frozen recovered-JL engine.
    for x in (
        "ir-script", "jj-script", "request-plan-script", "jk-authority", "ji-authority",
        "jv-authority", "jt-authority", "jw-authority", "request-plan-authority",
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
            "schema": "EXP073JN_ARTICLE3_RECOVERED_CANONICAL_ONE_LIVE_SCIENTIFIC_CLOSURE_RESULT_V0_2",
            "experiment": "Exp073JN",
            "status": INVALID_INFRA,
            "effect": "+0/+0",
            "scientific_authority_created": False,
            "layer_b_physical_support_closed": False,
            "downstream_covariance_whitening_stage_may_be_preregistered": False,
            "covariance_restriction_authorized": False,
            "Wm_S3_opened": False,
            "error": f"{type(e).__name__}: {e}",
            "token": "EXP073JN_RECOVERED_INVALID_INFRA_V0_2",
        }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    print("STATUS", result["status"])
    if "fresh_convergence" in result:
        print("CONVERGENCE", json.dumps(result["fresh_convergence"], sort_keys=True))
        print("LAYER_B", json.dumps(result["fresh_layer_b"], sort_keys=True))
        print("LIFECYCLE", json.dumps(result["fresh_execution_lifecycle"], sort_keys=True))
    if "error" in result:
        print("ERROR", result["error"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
