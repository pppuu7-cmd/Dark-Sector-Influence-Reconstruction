#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib.util
import json
import resource
from pathlib import Path

import numpy as np

H = 1e-4
REL_TOL_LINEAGE_ONLY = 1e-3
LOOKUP_REL_TOL = 1e-12
NATIVE_KPD = 20.0
CAPACITY = 32769
PARSER_CAPACITY = 1048576
NODE_COUNT = 32769
TEXT_SHA = "7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2"
NODE_SHA = "82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"
CANONICAL_AUTH_PASS = "CANONICAL_32769_STATIC_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"
BUILD_AUTH_PASS = "LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_V0_2_PASS_PLUS_0_PLUS_0"
PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
FAIL = "LAYERB_32769_RESOURCE_OR_INFRA_NOT_FEASIBLE_PLUS_0_PLUS_0"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_nodes(path: str | Path) -> np.ndarray:
    raw = Path(path).read_bytes()
    if sha(raw) != TEXT_SHA:
        raise RuntimeError("canonical 32769 text SHA mismatch")
    lines = raw.decode().splitlines()
    if len(lines) != NODE_COUNT:
        raise RuntimeError("canonical 32769 line-count mismatch")
    words = np.asarray([int(x, 16) for x in lines], dtype="<u8")
    nodes = np.ascontiguousarray(words.view("<f8"), dtype=np.float64)
    if sha(nodes.tobytes()) != NODE_SHA:
        raise RuntimeError("canonical 32769 decoded-node SHA mismatch")
    if not (np.all(np.isfinite(nodes)) and np.all(nodes > 0.0) and np.all(np.diff(nodes) > 0.0)):
        raise RuntimeError("invalid canonical 32769 nodes")
    return nodes


def validate_canonical_authority(path: str | Path) -> dict:
    d = json.loads(Path(path).read_text())
    if (
        d.get("classification") != CANONICAL_AUTH_PASS
        or d.get("artifact_verified_independently") is not True
        or d.get("scientific_response_read") is not False
        or d.get("class_solver_invoked") is not False
        or d.get("successor_execution_authorized") is not False
        or d.get("requested_node_count") != NODE_COUNT
        or d.get("node_payload_sha256") != NODE_SHA
        or d.get("u64hex_sha256") != TEXT_SHA
    ):
        raise RuntimeError("canonical 32769 authority invalid")
    return d


def validate_build_authority(path: str | Path) -> dict:
    d = json.loads(Path(path).read_text())
    if (
        d.get("classification") != BUILD_AUTH_PASS
        or d.get("artifact_verified_independently") is not True
        or d.get("class_commit") != "ac627d54e9ce196a08878d1ba33999819925d19c"
        or d.get("new_capacity") != CAPACITY
        or d.get("parser_new_argument_capacity") != PARSER_CAPACITY
        or d.get("canonical_32769_payload_bytes_including_nul") != 719273
        or d.get("parser_margin_bytes") != 329303
        or d.get("only_delta_from_v0_1_32769_tree_is_parser_capacity_constant") is not True
        or d.get("functional_payload_sufficiency_static") is not True
        or d.get("scientific_response_read") is not False
        or d.get("scientific_execution_authorized") is not False
    ):
        raise RuntimeError("32769 CLASS build authority V0.2 invalid")
    return d


def execute(a) -> dict:
    canonical = validate_canonical_authority(a.canonical_authority)
    build = validate_build_authority(a.build_authority)
    nodes = load_nodes(a.fine)
    jo = load_module("exp073jo_parent_for_32769_resource_v02", a.jo_script)
    jj = load_module("exp073jj_parent_for_32769_resource_v02", a.jj_script)
    if (
        jo.H != H
        or jo.REL_TOL_LINEAGE_ONLY != REL_TOL_LINEAGE_ONLY
        or jo.LOOKUP_REL_TOL != LOOKUP_REL_TOL
        or jo.NATIVE_KPD != NATIVE_KPD
        or jj.H != H
        or jj.REL_TOL != REL_TOL_LINEAGE_ONLY
        or jj.LOOKUP_REL_TOL != LOOKUP_REL_TOL
        or jj.NATIVE_KPD != NATIVE_KPD
    ):
        raise RuntimeError("frozen response-engine constants mismatch")
    jj.CAPACITY = CAPACITY

    from classy import Class

    tracker = {"constructions": 0, "live": 0, "max_live": 0}
    role_receipts = []
    for role, alpha, beta in jo.MODELS:
        c = None
        tracker["constructions"] += 1
        tracker["live"] += 1
        tracker["max_live"] = max(tracker["max_live"], tracker["live"])
        try:
            before = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            c = Class()
            params = jj.class_params(Path(a.baseline), Path(a.precision), alpha, beta, nodes)
            payload_bytes = len(params["k_output_values"].encode()) + 1
            if payload_bytes > PARSER_CAPACITY:
                raise RuntimeError(f"canonical payload exceeds parser capacity: {payload_bytes}>{PARSER_CAPACITY}")
            c.set(params)
            c.compute(["transfer"])
            after_compute = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            role_receipts.append({
                "role": role,
                "compute_completed": True,
                "k_output_values_bytes_including_nul": payload_bytes,
                "ru_maxrss_kb_before": before,
                "ru_maxrss_kb_after_compute": after_compute,
                "scientific_transfer_values_read": False,
                "scientific_response_computed": False,
                "scientific_response_serialized": False,
            })
        finally:
            if c is not None:
                try:
                    c.struct_cleanup()
                except Exception:
                    pass
            c = None
            tracker["live"] -= 1
            if tracker["live"] < 0:
                raise RuntimeError("live-instance tracker underflow")
            gc.collect()

    passed = bool(
        tracker == {"constructions": 4, "live": 0, "max_live": 1}
        and len(role_receipts) == 4
        and all(x["compute_completed"] for x in role_receipts)
        and all(x["scientific_transfer_values_read"] is False for x in role_receipts)
        and all(x["k_output_values_bytes_including_nul"] <= PARSER_CAPACITY for x in role_receipts)
    )
    classification = PASS if passed else FAIL
    return {
        "schema": "LAYERB_32769_RESPONSE_BLIND_RESOURCE_LIFECYCLE_PILOT_RESULT_V0_2",
        "classification": classification,
        "effect": "+0/+0",
        "canonical_authority_classification": canonical.get("classification"),
        "build_authority_classification": build.get("classification"),
        "canonical_32769_text_sha256": TEXT_SHA,
        "canonical_32769_node_sha256": NODE_SHA,
        "canonical_32769_requested_node_count": NODE_COUNT,
        "capacity": CAPACITY,
        "parser_capacity": PARSER_CAPACITY,
        "role_order": [r for r, _, _ in jo.MODELS],
        "role_receipts": role_receipts,
        "execution_lifecycle": {
            "total_solver_constructions": tracker["constructions"],
            "max_live_instances": tracker["max_live"],
            "final_live_instances": tracker["live"],
            "cross_process_scientific_operand_combination": False
        },
        "scientific_transfer_values_read": False,
        "scientific_response_read": False,
        "scientific_response_computed": False,
        "convergence_metric_computed": False,
        "convergence_classification_created": False,
        "scientific_authority_created": False,
        "successor_execution_authorized": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": classification
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    for x in ("canonical-authority", "build-authority", "fine", "jo-script", "jj-script", "baseline", "precision", "out"):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    out = Path(a.out)
    try:
        result = execute(a)
        rc = 0 if result["classification"] == PASS else 31
    except Exception as e:
        result = {
            "schema": "LAYERB_32769_RESPONSE_BLIND_RESOURCE_LIFECYCLE_PILOT_RESULT_V0_2",
            "classification": FAIL,
            "effect": "+0/+0",
            "scientific_transfer_values_read": False,
            "scientific_response_read": False,
            "scientific_response_computed": False,
            "convergence_metric_computed": False,
            "convergence_classification_created": False,
            "scientific_authority_created": False,
            "successor_execution_authorized": False,
            "covariance_restriction_authorized": False,
            "Wm_S3_opened": False,
            "error": f"{type(e).__name__}: {e}",
            "token": FAIL
        }
        rc = 31
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    if "error" in result:
        print("ERROR", result["error"])
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
