#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

H = 1e-4
LOOKUP_REL_TOL = 1e-12
NATIVE_KPD = 20.0
CAPACITY = 18432
PARSER_CAPACITY = 524288
NODE_COUNT = 16385
TEXT_SHA = "7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69"
NODE_SHA = "3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975"
CANONICAL_AUTH_PASS = "CANONICAL_16385_ANCHOR_SELECTED_QUORUM_PASS_PLUS_0_PLUS_0"
PASS = "CANONICAL_16385_SINGLE_ROLE_RESOURCE_PROBE_PASS_PLUS_0_PLUS_0"
FAIL = "CANONICAL_16385_SINGLE_ROLE_RESOURCE_PROBE_NOT_FEASIBLE_PLUS_0_PLUS_0"
MODELS = {
    "reference": (0.0, 0.0),
    "alpha_minus": (-H, 0.0),
    "beta_plus": (0.0, H),
    "beta_minus": (0.0, -H),
}
REQUESTS = (
    ("A", float.fromhex("0x1.3851eb851eb85p-1"), np.asarray([0.0013, 0.0047, 0.013, 0.041], dtype=np.float64)),
    ("B", float.fromhex("0x1.1c28f5c28f5c3p+0"), np.asarray([0.0019, 0.0073, 0.021, 0.057], dtype=np.float64)),
)


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
    if sha(nodes.tobytes()) != NODE_SHA:
        raise RuntimeError("canonical 16385 decoded-node SHA mismatch")
    if not (np.all(np.isfinite(nodes)) and np.all(nodes > 0) and np.all(np.diff(nodes) > 0)):
        raise RuntimeError("invalid canonical nodes")
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
    ):
        raise RuntimeError("canonical authority invalid")
    return d


def validate_patch(path: str | Path) -> None:
    d = json.loads(Path(path).read_text())
    if (
        d.get("old_capacity") != 30 or d.get("new_capacity") != CAPACITY or d.get("replacement_count") != 1
        or d.get("parser_old_argument_capacity") != 1024 or d.get("parser_new_argument_capacity") != PARSER_CAPACITY
        or d.get("parser_replacement_count") != 1
    ):
        raise RuntimeError("capacity patch invalid")


def execute(a) -> dict:
    validate_authority(a.canonical_authority)
    validate_patch(a.capacity_patch_record)
    nodes = load_nodes(a.fine)
    jj = load_module("jj_single_role_16385", a.jj_script)
    jo = load_module("jo_single_role_16385", a.jo_script)
    if jj.H != H or jj.LOOKUP_REL_TOL != LOOKUP_REL_TOL or jj.NATIVE_KPD != NATIVE_KPD:
        raise RuntimeError("JJ constants mismatch")
    jj.CAPACITY = CAPACITY
    if a.role not in MODELS:
        raise RuntimeError("unknown role")
    alpha, beta = MODELS[a.role]

    from classy import Class

    c = None
    tracker = {"constructions": 1, "live": 1, "max_live": 1}
    unsupported = 0
    max_lookup = 0.0
    receipts = {}
    try:
        c = Class()
        c.set(jj.class_params(Path(a.baseline), Path(a.precision), alpha, beta, nodes))
        c.compute(["transfer"])
        for q, z, targets in REQUESTS:
            v, valid, mx, key = jo.evaluate(jj, c, nodes, z, targets)
            u = int(np.count_nonzero(~valid))
            unsupported += u
            max_lookup = max(max_lookup, float(mx))
            receipts[q] = {
                "z_binary64_hex": float(z).hex(),
                "target_count": int(targets.size),
                "operand_payload_sha256": sha(v.tobytes()),
                "operand_shape": list(v.shape),
                "finite": bool(np.all(np.isfinite(v))),
                "unsupported": u,
                "max_lookup": float(mx),
                "k_key": str(key),
            }
    finally:
        if c is not None:
            try:
                c.struct_cleanup()
            except Exception:
                pass
        tracker["live"] = 0

    passed = bool(
        tracker == {"constructions": 1, "live": 0, "max_live": 1}
        and unsupported == 0 and max_lookup <= LOOKUP_REL_TOL
        and len(receipts) == 2 and all(r["finite"] and r["operand_shape"] == [4] for r in receipts.values())
    )
    classification = PASS if passed else FAIL
    return {
        "schema": "LAYERB_POST_JM_CANONICAL_16385_SINGLE_ROLE_RESOURCE_PROBE_RESULT_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "role": a.role,
        "canonical_16385_node_sha256": NODE_SHA,
        "canonical_16385_text_sha256": TEXT_SHA,
        "capacity": CAPACITY,
        "parser_capacity": PARSER_CAPACITY,
        "execution_lifecycle": tracker,
        "unsupported_target_evaluations": unsupported,
        "max_requested_node_coordinate_rel_mismatch": max_lookup,
        "request_receipts": receipts,
        "cross_role_operands_combined": False,
        "jm_result_read": False,
        "branch_activated": False,
        "next_rung_execution_authorized": False,
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": classification,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--role", required=True, choices=sorted(MODELS))
    for x in ("canonical-authority", "fine", "jo-script", "jj-script", "baseline", "precision", "capacity-patch-record", "out"):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    out = Path(a.out)
    try:
        d = execute(a)
    except Exception as e:
        d = {
            "schema": "LAYERB_POST_JM_CANONICAL_16385_SINGLE_ROLE_RESOURCE_PROBE_RESULT_V0_1",
            "classification": FAIL,
            "effect": "+0/+0",
            "role": a.role,
            "error": f"{type(e).__name__}: {e}",
            "cross_role_operands_combined": False,
            "jm_result_read": False,
            "branch_activated": False,
            "next_rung_execution_authorized": False,
            "scientific_authority_created": False,
            "covariance_restriction_authorized": False,
            "Wm_S3_opened": False,
            "token": FAIL,
        }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
    print(d["token"], d.get("role"))
    if "error" in d:
        print("ERROR", d["error"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
