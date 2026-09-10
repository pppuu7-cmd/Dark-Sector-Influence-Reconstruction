#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path

H = 1e-4
REL_TOL = 1e-3
LOOKUP_REL_TOL = 1e-12
CAPACITY = 4608
PARSER_CAPACITY = 131072
NATIVE_KPD = 20.0
JI_GEOM_SHA = "79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a"
JL_CONVERGED = "COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0"
SCI_PASS = "PASS_PHYSICAL_SUPPORT_ARTICLE3_SHARED_GRID_V0_1"
SCI_FAIL = "FAIL_PHYSICAL_SUPPORT_ARTICLE3_SHARED_GRID_V0_1"
NUM_UNRES = "NUMERICALLY_UNRESOLVED_EXP073JN"
INVALID_INFRA = "INVALID_INFRA_PLUS_0_PLUS_0"


def load_module(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    common = [
        "parent-root", "parent-authority", "manifest", "angular-root", "expim-root",
        "boss-root", "source", "lens", "camb-root", "expz2-script", "exp073iq-script",
        "baseline", "precision", "scratch"
    ]
    for x in common:
        ap.add_argument("--" + x, required=True)
    ap.add_argument("--ir-script", required=True)
    ap.add_argument("--jj-script", required=True)
    ap.add_argument("--jl-authority", required=True)
    ap.add_argument("--ji-authority", required=True)
    ap.add_argument("--capacity-patch-record", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    jl = json.loads(Path(a.jl_authority).read_text())
    ji = json.loads(Path(a.ji_authority).read_text())
    patch = json.loads(Path(a.capacity_patch_record).read_text())

    # Activation is intentionally no stricter than the pre-frozen JN contract:
    # a valid independently verified JL CONVERGED authority is sufficient.
    if jl.get("classification") != JL_CONVERGED:
        raise SystemExit("Exp073JN activation condition not met")
    if jl.get("artifact_verified_independently") is not True:
        raise SystemExit("JL artifact is not independently verified")
    jo = jl.get("observations", {})
    jl_max = jo.get("max_atomic_coarse_vs_fine_relative_component_difference")
    if not (isinstance(jl_max, (int, float)) and math.isfinite(jl_max) and jl_max < REL_TOL):
        raise SystemExit("JL convergence authority mismatch")
    if not isinstance(jl.get("artifact_zip_sha256"), str) or len(jl["artifact_zip_sha256"]) != 64:
        raise SystemExit("JL artifact digest missing")

    if ji.get("classification") != "GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0":
        raise SystemExit("invalid JI authority")
    if ji.get("geometry", {}).get("stream_sha256") != JI_GEOM_SHA:
        raise SystemExit("JI geometry mismatch")

    if patch.get("old_capacity") != 30 or patch.get("new_capacity") != CAPACITY or patch.get("replacement_count") != 1:
        raise SystemExit("invalid k-output capacity patch")
    if patch.get("parser_old_argument_capacity") != 1024 or patch.get("parser_new_argument_capacity") != PARSER_CAPACITY or patch.get("parser_replacement_count") != 1:
        raise SystemExit("invalid parser capacity patch")

    jj = load_module("exp073jj_jn_parent", a.jj_script)
    ir = load_module("exp073ir_jn_parent", a.ir_script)
    if jj.H != H or jj.REL_TOL != REL_TOL or jj.NATIVE_KPD != NATIVE_KPD or jj.JI_GEOM_SHA != JI_GEOM_SHA:
        raise SystemExit("JJ response-engine constants mismatch")
    if ir.H != H or ir.REL_TOL != REL_TOL or ir.KMAX != jj.KMAX or ir.ZMIN != 0.295 or ir.ZMAX != 2.33:
        raise SystemExit("IR frozen constants mismatch")

    jj.CAPACITY = CAPACITY
    coarse, r2048, l2048, u2048 = jj.guarded_lattice(2048)
    fine, r4096, l4096, u4096 = jj.guarded_lattice(4096)
    if (l2048, u2048, len(coarse)) != (0, 1, 2049) or (l4096, u4096, len(fine)) != (0, 1, 4097):
        raise SystemExit("frozen JL architecture mismatch")

    jj.ResolutionSuite.coarse_nodes = coarse
    jj.ResolutionSuite.fine_nodes = fine
    jj.ResolutionSuite.audit = {}

    scratch = Path(a.scratch) / "scientific_closure"
    out_inner = scratch / "exp073jn_inner_ir.json"
    scratch.mkdir(parents=True, exist_ok=True)

    old_argv = sys.argv
    argv = ["exp073ir"]
    for x in common:
        val = scratch if x == "scratch" else getattr(a, x.replace("-", "_"))
        argv += ["--" + x, str(val)]
    argv += ["--out", str(out_inner)]
    ir.ResponseSuite = jj.ResolutionSuite
    sys.argv = argv
    try:
        rc = ir.main()
    finally:
        sys.argv = old_argv
    if rc != 0 or not out_inner.exists():
        raise RuntimeError("fresh scientific Layer-B traversal failed")

    d = json.loads(out_inner.read_text())
    forbidden = ("covariance_read", "whitening_read", "nuisance_read", "relation_null_read")
    forbidden_ok = all(d.get(k) is False for k in forbidden)

    parent = d.get("parent", {})
    layer = d.get("layer_b", {})
    conv = d.get("convergence", {})
    audit = jj.ResolutionSuite.audit
    exact_parent = (
        parent.get("retained_count") == 107
        and parent.get("retained_id_sha256") == ir.PARENT_RETAINED_SHA
        and parent.get("full_order_sha256") == ir.FULL_ORDER_SHA
    )
    try:
        unsupported = sum(int(v["unsupported_target_evaluations"]) for v in audit.values())
        lookup = max(float(v["max_requested_node_coordinate_rel_mismatch"]) for v in audit.values())
    except Exception:
        unsupported = -1
        lookup = math.inf
    mx = conv.get("max_relative_component_difference")

    structural_ok = bool(
        forbidden_ok
        and exact_parent
        and unsupported == 0
        and math.isfinite(lookup)
        and lookup <= LOOKUP_REL_TOL
        and conv.get("finite_nonzero_status_changed") is False
        and conv.get("row_label_changed") is False
        and conv.get("boss_dense_z_disagreement") is False
    )
    numerical_ok = bool(
        structural_ok
        and isinstance(mx, (int, float))
        and math.isfinite(mx)
        and mx < REL_TOL
    )
    physical_ok = bool(
        numerical_ok
        and layer.get("invalid_row_fraction", 1.0) <= ir.FB_MAX
        and layer.get("retained_after_layer_b", 0) >= ir.MIN_RETAINED
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
    result = {
        "schema": "EXP073JN_ARTICLE3_LAYERB_SHARED_GRID_SCIENTIFIC_CLOSURE_RESULT_V0_1",
        "experiment": "Exp073JN",
        "status": status,
        "scientific_authority_created": passed,
        "layer_b_physical_support_closed": passed,
        "downstream_covariance_whitening_stage_may_be_preregistered": passed,
        "covariance_restriction_authorized": False,
        "wm_s3_authorized": False,
        "h": H,
        "rel_tol": REL_TOL,
        "native_k_per_decade_for_pk_frozen": NATIVE_KPD,
        "activation_authority": {
            "jl_classification": jl.get("classification"),
            "jl_run_id": jl.get("run_id"),
            "jl_job_id": jl.get("job_id"),
            "jl_head_sha": jl.get("head_sha"),
            "jl_artifact_zip_sha256": jl.get("artifact_zip_sha256"),
            "jl_max_relative_component_difference": jl_max,
        },
        "inherited_slot_remapping": {
            "10": "production_guarded_C2048_2049_nodes",
            "20": "dense_guarded_F4096_4097_nodes",
        },
        "lattices": {
            "production": {
                "base_n": 2048,
                "ratio_binary64": float(r2048),
                "lower_guard_count": l2048,
                "upper_guard_count": u2048,
                "requested_node_count": len(coarse),
                "extended_k_min": float(coarse[0]),
                "extended_k_max": float(coarse[-1]),
            },
            "dense": {
                "base_n": 4096,
                "ratio_binary64": float(r4096),
                "lower_guard_count": l4096,
                "upper_guard_count": u4096,
                "requested_node_count": len(fine),
                "extended_k_min": float(fine[0]),
                "extended_k_max": float(fine[-1]),
            },
        },
        "ji_geometry_stream_sha256": JI_GEOM_SHA,
        "parent_identity_preserved": exact_parent,
        "response_engine_audit": audit,
        "unsupported_target_evaluations": unsupported,
        "max_requested_node_coordinate_rel_mismatch": lookup,
        "convergence": conv,
        "layer_b": layer,
        "structural_provenance_ok": structural_ok,
        "forbidden_downstream_reads": {k: d.get(k) for k in forbidden},
        "inner_status_for_crosscheck": d.get("status"),
        "token": (
            "PASS_EXP073JN_LAYERB_SHARED_GRID_SCIENTIFIC_CLOSURE_V0_1"
            if passed
            else ("EXP073JN_INVALID_INFRA_V0_1" if status == INVALID_INFRA else "PASS_EXP073JN_VALID_NONPASS_RESULT_V0_1")
        ),
    }

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    print("STATUS", status)
    print("CONVERGENCE", json.dumps(conv, sort_keys=True))
    print("LAYER_B", json.dumps(layer, sort_keys=True))
    print("AUDIT", json.dumps(audit, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
