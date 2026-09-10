#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

REL_TOL = 1e-3
LOOKUP_REL_TOL = 1e-12
CONVERGED = "COMMON_GRID_FOURTH_REFINEMENT_CONVERGED_PLUS_0_PLUS_0"
NOT_CONVERGED = "COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0"
INVALID_INFRA = "INVALID_INFRA_PLUS_0_PLUS_0"


def finalize(d: dict) -> dict:
    if d.get("schema") != "EXP073JM_ARTICLE3_LAYERB_COMMON_GRID_FOURTH_REFINEMENT_CONVERGENCE_RESULT_V0_1":
        raise ValueError("unexpected JM raw schema")
    if d.get("classification") not in {CONVERGED, NOT_CONVERGED}:
        raise ValueError("unexpected JM raw classification")
    if d.get("scientific_authority_created") is not False or d.get("covariance_restriction_authorized") is not False:
        raise ValueError("JM must remain support-only")
    if d.get("rel_tol") != REL_TOL or d.get("h") != 1e-4 or d.get("native_k_per_decade_for_pk_frozen") != 20.0:
        raise ValueError("frozen numerical constants changed")

    latt = d.get("lattices", {})
    c = latt.get("coarse", {})
    f = latt.get("fine", {})
    grid_identity_ok = (
        c.get("base_n") == 4096
        and c.get("lower_guard_count") == 0
        and c.get("upper_guard_count") == 1
        and c.get("requested_node_count") == 4097
        and f.get("base_n") == 8192
        and f.get("lower_guard_count") == 0
        and f.get("upper_guard_count") == 1
        and f.get("requested_node_count") == 8193
    )

    audit = d.get("response_engine_audit", {})
    try:
        lookup = max(float(v["max_requested_node_coordinate_rel_mismatch"]) for v in audit.values())
    except Exception:
        lookup = math.inf
    unsupported = d.get("unsupported_target_evaluations")
    parent_ok = d.get("parent_identity_preserved") is True
    stencil_lookup_ok = unsupported == 0 and math.isfinite(lookup) and lookup <= LOOKUP_REL_TOL

    conv = d.get("convergence", {})
    mx = conv.get("max_relative_component_difference")
    diagnostic = d.get("diagnostic", {})
    argmax = diagnostic.get("relative_argmax") or {}
    dmx = argmax.get("relative_difference")
    diagnostic_ok = (
        diagnostic.get("decision_neutral") is True
        and isinstance(mx, (int, float)) and math.isfinite(mx)
        and isinstance(dmx, (int, float)) and math.isfinite(dmx)
        and float(mx) == float(dmx)
    )

    infra_ok = bool(parent_ok and grid_identity_ok and stencil_lookup_ok and diagnostic_ok)

    out = dict(d)
    out["raw_classification"] = d.get("classification")
    out["contract_finalizer"] = {
        "schema": "EXP073JM_CONTRACT_FINALIZER_V0_1",
        "infra_ok": infra_ok,
        "parent_identity_ok": parent_ok,
        "grid_identity_ok": grid_identity_ok,
        "stencil_lookup_ok": stencil_lookup_ok,
        "max_requested_node_coordinate_rel_mismatch": lookup,
        "diagnostic_identity_ok": diagnostic_ok,
        "decision_metric_unchanged": True,
        "relative_tolerance_unchanged": REL_TOL,
    }
    if not infra_ok:
        out["classification"] = INVALID_INFRA
        out["token"] = "EXP073JM_INVALID_INFRA_V0_1"
    else:
        out["classification"] = d["classification"]
        out["token"] = (
            "PASS_EXP073JM_COMMON_GRID_FOURTH_REFINEMENT_CONVERGED_V0_1"
            if d["classification"] == CONVERGED
            else "PASS_EXP073JM_COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_V0_1"
        )
    out["scientific_authority_created"] = False
    out["covariance_restriction_authorized"] = False
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    d = json.loads(Path(a.raw).read_text())
    out = finalize(d)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(out["token"])
    print("FINAL_CLASSIFICATION", out["classification"])
    print("CONTRACT_FINALIZER", json.dumps(out["contract_finalizer"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
