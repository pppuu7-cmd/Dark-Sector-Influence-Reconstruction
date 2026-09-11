#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

H = 1e-4
REL_TOL_LINEAGE_ONLY = 1e-3
LOOKUP_REL_TOL = 1e-12
NATIVE_KPD = 20.0
CAPACITY = 18432
PARSER_CAPACITY = 524288
NODE_COUNT = 16385
TEXT_SHA = "7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69"
NODE_SHA = "3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975"
CANONICAL_AUTH_PASS = "CANONICAL_16385_ANCHOR_SELECTED_QUORUM_PASS_PLUS_0_PLUS_0"
PASS = "CANONICAL_16385_ONE_LIVE_FOUR_BUILD_RESOURCE_PILOT_PASS_PLUS_0_PLUS_0"
FAIL = "CANONICAL_16385_RESOURCE_OR_INFRA_NOT_FEASIBLE_PLUS_0_PLUS_0"


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
        raise RuntimeError("canonical 16385 text SHA mismatch")
    lines = raw.decode().splitlines()
    if len(lines) != NODE_COUNT:
        raise RuntimeError("canonical 16385 line-count mismatch")
    words = np.asarray([int(x, 16) for x in lines], dtype="<u8")
    nodes = np.ascontiguousarray(words.view("<f8"), dtype=np.float64)
    if sha(np.ascontiguousarray(nodes, dtype="<f8").tobytes()) != NODE_SHA:
        raise RuntimeError("canonical 16385 decoded-node SHA mismatch")
    if not (np.all(np.isfinite(nodes)) and np.all(nodes > 0.0) and np.all(np.diff(nodes) > 0.0)):
        raise RuntimeError("invalid canonical 16385 nodes")
    return nodes


def validate_authority(path: str | Path) -> dict:
    d = json.loads(Path(path).read_text())
    if (
        d.get("classification") != CANONICAL_AUTH_PASS
        or d.get("artifact_verified_independently") is not True
        or d.get("scientific_response_read") is not False
        or d.get("class_solver_invoked") is not False
        or d.get("successor_branch_activated") is not False
        or d.get("successor_execution_authorized") is not False
        or d.get("requested_node_count") != NODE_COUNT
        or d.get("node_payload_sha256") != NODE_SHA
        or d.get("u64hex_sha256") != TEXT_SHA
        or d.get("anchor_match_count", 0) < d.get("minimum_anchor_quorum", 999)
    ):
        raise RuntimeError("canonical 16385 dormant authority invalid")
    return d


def validate_patch(path: str | Path) -> dict:
    d = json.loads(Path(path).read_text())
    if (
        d.get("old_capacity") != 30
        or d.get("new_capacity") != CAPACITY
        or d.get("replacement_count") != 1
        or d.get("parser_old_argument_capacity") != 1024
        or d.get("parser_new_argument_capacity") != PARSER_CAPACITY
        or d.get("parser_replacement_count") != 1
    ):
        raise RuntimeError("16385 capacity patch receipt invalid")
    return d


def execute(a) -> dict:
    authority = validate_authority(a.canonical_authority)
    validate_patch(a.capacity_patch_record)
    nodes = load_nodes(a.fine)
    jo = load_module("exp073jo_parent_for_16385", a.jo_script)
    jj = load_module("exp073jj_parent_for_16385", a.jj_script)
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

    raw = {q: {} for q, _, _ in jo.REQUESTS}
    receipts = []
    tracker = {"constructions": 0, "live": 0, "max_live": 0}
    unsupported = 0
    max_lookup = 0.0
    operands_finite = True

    for role, alpha, beta in jo.MODELS:
        c = None
        tracker["constructions"] += 1
        tracker["live"] += 1
        tracker["max_live"] = max(tracker["max_live"], tracker["live"])
        try:
            c = Class()
            c.set(jj.class_params(Path(a.baseline), Path(a.precision), alpha, beta, nodes))
            c.compute(["transfer"])
            rr = {"role": role, "requests": {}, "k_keys": set()}
            for q, z, targets in jo.REQUESTS:
                v, valid, mx, key = jo.evaluate(jj, c, nodes, z, targets)
                raw[q][role] = v
                u = int(np.count_nonzero(~valid))
                unsupported += u
                max_lookup = max(max_lookup, mx)
                operands_finite &= bool(np.all(np.isfinite(v)))
                rr["k_keys"].add(key)
                rr["requests"][q] = {
                    "z_binary64_hex": float(z).hex(),
                    "target_count": int(targets.size),
                    "operand_payload_sha256": sha(v.tobytes()),
                    "unsupported": u,
                    "max_lookup": mx,
                }
            rr["k_keys"] = sorted(rr["k_keys"])
            receipts.append(rr)
        finally:
            if c is not None:
                try:
                    c.struct_cleanup()
                except Exception:
                    pass
            tracker["live"] -= 1
            if tracker["live"] < 0:
                raise RuntimeError("live-instance tracker underflow")

    responses = {}
    responses_finite = True
    for q, _, _ in jo.REQUESTS:
        ref = raw[q]["reference"]
        al = raw[q]["alpha_minus"]
        bp = raw[q]["beta_plus"]
        bm = raw[q]["beta_minus"]
        response = np.ascontiguousarray(
            np.column_stack((np.abs((al - ref) / (-H)), np.abs((bp - bm) / (2 * H)))),
            dtype="<f8",
        )
        finite = bool(np.all(np.isfinite(response)))
        responses_finite &= finite
        responses[q] = {"payload_sha256": sha(response.tobytes()), "shape": list(response.shape), "finite": finite}

    passed = bool(
        tracker == {"constructions": 4, "live": 0, "max_live": 1}
        and unsupported == 0
        and max_lookup <= LOOKUP_REL_TOL
        and operands_finite
        and responses_finite
        and all(v["shape"] == [4, 2] for v in responses.values())
    )
    classification = PASS if passed else FAIL
    return {
        "schema": "LAYERB_POST_JM_CANONICAL_16385_ONE_LIVE_RESOURCE_PILOT_RESULT_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "branch_activated": False,
        "jm_result_read": False,
        "scientific_response_read_for_branch_decision": False,
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "canonical_authority_run_id": authority.get("run_id"),
        "canonical_16385_text_sha256": TEXT_SHA,
        "canonical_16385_node_sha256": NODE_SHA,
        "canonical_16385_requested_node_count": NODE_COUNT,
        "capacity": CAPACITY,
        "parser_capacity": PARSER_CAPACITY,
        "role_order": [r for r, _, _ in jo.MODELS],
        "model_receipts": receipts,
        "execution_lifecycle": {
            "total_solver_constructions": tracker["constructions"],
            "max_live_instances": tracker["max_live"],
            "final_live_instances": tracker["live"],
            "cross_process_raw_operand_combination": False,
        },
        "unsupported_target_evaluations": unsupported,
        "max_requested_node_coordinate_rel_mismatch": max_lookup,
        "transfer_operands_finite": operands_finite,
        "pilot_responses": responses,
        "pilot_responses_finite": responses_finite,
        "full_next_rung_107_row_traversal_executed": False,
        "next_rung_convergence_classification_created": False,
        "next_rung_execution_authorized": False,
        "article3_repository_readiness_percent": 68,
        "funnel_freeze_readiness_percent": 67,
        "token": classification,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    for x in ("canonical-authority", "fine", "jo-script", "jj-script", "baseline", "precision", "capacity-patch-record", "out"):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    out = Path(a.out)
    try:
        result = execute(a)
    except Exception as e:
        result = {
            "schema": "LAYERB_POST_JM_CANONICAL_16385_ONE_LIVE_RESOURCE_PILOT_RESULT_V0_1",
            "classification": FAIL,
            "effect": "+0/+0",
            "branch_activated": False,
            "jm_result_read": False,
            "scientific_authority_created": False,
            "covariance_restriction_authorized": False,
            "Wm_S3_opened": False,
            "next_rung_execution_authorized": False,
            "error": f"{type(e).__name__}: {e}",
            "token": FAIL,
        }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    if "error" in result:
        print("ERROR", result["error"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
