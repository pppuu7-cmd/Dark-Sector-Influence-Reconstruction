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
CAPACITY = 9216
PARSER_CAPACITY = 262144
NODE_COUNT = 8193
TEXT_SHA = "90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6"
NODE_SHA = "6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515"
CLASS_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
JL_NOT_CONVERGED = "COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0"
JM_STATIC_PASS = "EXP073JM_RECOVERED_STATIC_IMPLEMENTATION_AUDIT_PASS_PLUS_0_PLUS_0"
CANONICAL_AUTH_PASS = "CANONICAL_8193_ANCHOR_SELECTED_QUORUM_PASS_PLUS_0_PLUS_0"
PASS = "CANONICAL_8193_ONE_LIVE_FOUR_BUILD_RESOURCE_PILOT_PASS_PLUS_0_PLUS_0"
FAIL = "CANONICAL_8193_RESOURCE_OR_INFRA_NOT_FEASIBLE_PLUS_0_PLUS_0"
MODELS = (
    ("reference", 0.0, 0.0),
    ("alpha_minus", -H, 0.0),
    ("beta_plus", 0.0, H),
    ("beta_minus", 0.0, -H),
)
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
        raise RuntimeError("canonical 8193 text SHA mismatch")
    lines = raw.decode().splitlines()
    if len(lines) != NODE_COUNT:
        raise RuntimeError("canonical 8193 line-count mismatch")
    words = np.asarray([int(x, 16) for x in lines], dtype="<u8")
    nodes = np.ascontiguousarray(words.view("<f8"), dtype=np.float64)
    if sha(np.ascontiguousarray(nodes, dtype="<f8").tobytes()) != NODE_SHA:
        raise RuntimeError("canonical 8193 decoded-node SHA mismatch")
    if not (np.all(np.isfinite(nodes)) and np.all(nodes > 0.0) and np.all(np.diff(nodes) > 0.0)):
        raise RuntimeError("canonical 8193 node validity mismatch")
    return nodes


def validate_authorities(a):
    jl = json.loads(Path(a.jl_authority).read_text())
    jm = json.loads(Path(a.jm_static_authority).read_text())
    ca = json.loads(Path(a.canonical_authority).read_text())
    patch = json.loads(Path(a.capacity_patch_record).read_text())

    if (
        jl.get("classification") != JL_NOT_CONVERGED
        or jl.get("artifact_verified_independently") is not True
        or jl.get("jm_branch_activated") is not True
        or jl.get("jn_branch_activated") is not False
    ):
        raise RuntimeError("JL NOT_CONVERGED activation authority invalid")
    if (
        jm.get("classification") != JM_STATIC_PASS
        or jm.get("artifact_verified_independently") is not True
        or jm.get("checks_all_pass") is not True
        or jm.get("resource_pilot_still_required") is not True
    ):
        raise RuntimeError("JM recovered static authority invalid")
    if (
        ca.get("classification") != CANONICAL_AUTH_PASS
        or ca.get("artifact_verified_independently") is not True
        or ca.get("branch_activated") is not False
        or ca.get("scientific_response_read") is not False
        or ca.get("class_solver_invoked") is not False
        or ca.get("requested_node_count") != NODE_COUNT
        or ca.get("node_payload_sha256") != NODE_SHA
        or ca.get("u64hex_sha256") != TEXT_SHA
        or ca.get("anchor_match_count", 0) < ca.get("minimum_anchor_quorum", 999)
    ):
        raise RuntimeError("canonical 8193 authority invalid")
    if (
        patch.get("old_capacity") != 30
        or patch.get("new_capacity") != CAPACITY
        or patch.get("replacement_count") != 1
        or patch.get("parser_old_argument_capacity") != 1024
        or patch.get("parser_new_argument_capacity") != PARSER_CAPACITY
        or patch.get("parser_replacement_count") != 1
    ):
        raise RuntimeError("JM pilot capacity patch receipt invalid")
    return jl, jm, ca


def evaluate(jj, c, nodes: np.ndarray, z: float, targets: np.ndarray):
    tk = c.get_transfer(z=float(z), output_format="class")
    dm = [q for q in tk if q.strip() == "d_m"]
    if len(dm) != 1:
        raise RuntimeError("expected exact public d_m transfer key")
    kkey = None
    scale = None
    for q in tk:
        s = q.lower().replace(" ", "")
        if s in {"k(h/mpc)", "k[h/mpc]", "k_h/mpc"} or ("k" in s and "h/mpc" in s):
            kkey = q
            scale = float(c.h())
            break
        if s in {"k(1/mpc)", "k[1/mpc]"} or ("k" in s and "1/mpc" in s):
            kkey = q
            scale = 1.0
            break
    if kkey is None:
        raise RuntimeError("unrecognized CLASS transfer k key")
    k = np.asarray(tk[kkey], dtype=np.float64) * scale
    y = np.asarray(tk[dm[0]], dtype=np.float64)
    if (
        k.ndim != 1
        or y.shape != k.shape
        or np.any(~np.isfinite(k))
        or np.any(~np.isfinite(y))
        or np.any(k <= 0.0)
        or np.any(np.diff(k) <= 0.0)
    ):
        raise RuntimeError("invalid transfer table")
    yn, mx = jj.requested_values(k, y, nodes)
    v, valid = jj.cubic_centered(nodes, yn, targets)
    return np.ascontiguousarray(v, dtype="<f8"), np.asarray(valid, dtype=bool), float(mx), str(kkey)


def execute(a):
    jl, jm, ca = validate_authorities(a)
    nodes = load_nodes(a.fine)
    jj = load_module("exp073jj_jo_pilot", a.jj_script)
    if (
        jj.H != H
        or jj.REL_TOL != REL_TOL_LINEAGE_ONLY
        or jj.LOOKUP_REL_TOL != LOOKUP_REL_TOL
        or jj.NATIVE_KPD != NATIVE_KPD
    ):
        raise RuntimeError("JJ frozen response-engine constants mismatch")
    jj.CAPACITY = CAPACITY

    from classy import Class

    raw = {q: {} for q, _, _ in REQUESTS}
    receipts = []
    tracker = {"constructions": 0, "live": 0, "max_live": 0}
    unsupported = 0
    max_lookup = 0.0
    transfer_operands_finite = True

    for role, alpha, beta in MODELS:
        c = None
        tracker["constructions"] += 1
        tracker["live"] += 1
        tracker["max_live"] = max(tracker["max_live"], tracker["live"])
        try:
            c = Class()
            c.set(jj.class_params(Path(a.baseline), Path(a.precision), alpha, beta, nodes))
            c.compute(["transfer"])
            rr = {"role": role, "requests": {}, "k_keys": set()}
            for q, z, targets in REQUESTS:
                v, valid, mx, key = evaluate(jj, c, nodes, z, targets)
                raw[q][role] = v
                u = int(np.count_nonzero(~valid))
                unsupported += u
                max_lookup = max(max_lookup, mx)
                transfer_operands_finite &= bool(np.all(np.isfinite(v)))
                rr["k_keys"].add(key)
                rr["requests"][q] = {
                    "z_binary64_hex": float(z).hex(),
                    "target_count": int(targets.size),
                    "target_payload_sha256": sha(np.ascontiguousarray(targets, dtype="<f8").tobytes()),
                    "operand_payload_sha256": sha(v.tobytes()),
                    "operand_shape": list(v.shape),
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
    for q, _, _ in REQUESTS:
        ref = raw[q]["reference"]
        al = raw[q]["alpha_minus"]
        bp = raw[q]["beta_plus"]
        bm = raw[q]["beta_minus"]
        response = np.ascontiguousarray(
            np.column_stack((np.abs((al - ref) / (-H)), np.abs((bp - bm) / (2 * H)))),
            dtype="<f8",
        )
        responses_finite &= bool(np.all(np.isfinite(response)))
        responses[q] = {
            "payload_sha256": sha(response.tobytes()),
            "shape": list(response.shape),
            "finite": bool(np.all(np.isfinite(response))),
        }

    passed = bool(
        tracker == {"constructions": 4, "live": 0, "max_live": 1}
        and unsupported == 0
        and max_lookup <= LOOKUP_REL_TOL
        and transfer_operands_finite
        and responses_finite
        and all(v["shape"] == [4, 2] for v in responses.values())
    )
    classification = PASS if passed else FAIL

    return {
        "schema": "EXP073JO_ARTICLE3_JM_CANONICAL_8193_ONE_LIVE_RESOURCE_PILOT_RESULT_V0_1",
        "experiment": "Exp073JO",
        "classification": classification,
        "effect": "+0/+0",
        "class_commit": CLASS_COMMIT,
        "h_lineage_only": H,
        "rel_tol_lineage_only": REL_TOL_LINEAGE_ONLY,
        "native_k_per_decade_for_pk": NATIVE_KPD,
        "capacity": CAPACITY,
        "parser_capacity": PARSER_CAPACITY,
        "canonical_8193_text_sha256": TEXT_SHA,
        "canonical_8193_node_sha256": NODE_SHA,
        "canonical_8193_requested_node_count": NODE_COUNT,
        "activation": {
            "jl_classification": jl.get("classification"),
            "jl_run_id": jl.get("run_id"),
            "jl_artifact_id": jl.get("artifact_id"),
            "jm_static_classification": jm.get("classification"),
            "canonical_authority_classification": ca.get("classification"),
        },
        "fixed_requests": {
            q: {
                "z_binary64_hex": float(z).hex(),
                "targets": [float(x) for x in targets],
                "target_payload_sha256": sha(np.ascontiguousarray(targets, dtype="<f8").tobytes()),
            }
            for q, z, targets in REQUESTS
        },
        "role_order": [r for r, _, _ in MODELS],
        "model_receipts": receipts,
        "execution_lifecycle": {
            "total_solver_constructions": tracker["constructions"],
            "max_live_instances": tracker["max_live"],
            "final_live_instances": tracker["live"],
            "cross_process_raw_operand_combination": False,
        },
        "unsupported_target_evaluations": unsupported,
        "max_requested_node_coordinate_rel_mismatch": max_lookup,
        "transfer_operands_finite": transfer_operands_finite,
        "pilot_responses": responses,
        "pilot_responses_finite": responses_finite,
        "full_jm_107_row_traversal_executed": False,
        "jm_convergence_classification_created": False,
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "full_jm_production_permitted": passed,
        "article3_repository_readiness_percent": 68,
        "funnel_freeze_readiness_percent": 67,
        "token": classification,
    }


def main():
    ap = argparse.ArgumentParser()
    for x in (
        "jl-authority", "jm-static-authority", "canonical-authority", "fine",
        "jj-script", "baseline", "precision", "capacity-patch-record", "out",
    ):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    out = Path(a.out)
    try:
        result = execute(a)
    except Exception as e:
        result = {
            "schema": "EXP073JO_ARTICLE3_JM_CANONICAL_8193_ONE_LIVE_RESOURCE_PILOT_RESULT_V0_1",
            "experiment": "Exp073JO",
            "classification": FAIL,
            "effect": "+0/+0",
            "error": f"{type(e).__name__}: {e}",
            "full_jm_107_row_traversal_executed": False,
            "jm_convergence_classification_created": False,
            "scientific_authority_created": False,
            "covariance_restriction_authorized": False,
            "Wm_S3_opened": False,
            "full_jm_production_permitted": False,
            "article3_repository_readiness_percent": 68,
            "funnel_freeze_readiness_percent": 67,
            "token": FAIL,
        }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    if "execution_lifecycle" in result:
        print("LIFECYCLE", json.dumps(result["execution_lifecycle"], sort_keys=True))
        print("UNSUPPORTED", result["unsupported_target_evaluations"])
        print("MAX_LOOKUP", result["max_requested_node_coordinate_rel_mismatch"])
    if "error" in result:
        print("ERROR", result["error"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
