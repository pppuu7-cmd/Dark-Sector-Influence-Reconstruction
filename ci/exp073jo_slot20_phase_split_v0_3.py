#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

CONTRACT_ID = "EXP073JO_ARTICLE3_JL_DURABLE_RESPONSE_CHECKPOINT_RECOVERY_V0_1"
PHASE_SPLIT_VERSION = "EXP073JO_SLOT20_HISTORY_PHASE_SPLIT_V0_3"
WRAPPER_BLOB_SHA = "aa4c544c1e3e81137010fcdbd34f20567e1eb894"
CAPACITY = 4608
PARSER_CAPACITY = 131072
H = 1e-4
REL_TOL = 1e-3
NATIVE_KPD = 20.0
EXPECTED_NODE_COUNT = 4097
EXPECTED_RESPONSE_SHAPE = (4, 2)
EXPECTED_NBYTES = 64


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def f8_bytes(x) -> bytes:
    return np.ascontiguousarray(np.asarray(x, dtype="<f8")).tobytes()


def bool_mask_bits(x: np.ndarray) -> dict:
    finite = np.ascontiguousarray(np.isfinite(x), dtype=np.uint8)
    positive = np.ascontiguousarray(x > 0.0, dtype=np.uint8)
    return {
        "finite_mask_u8_sha256": sha_bytes(finite.tobytes()),
        "positive_mask_u8_sha256": sha_bytes(positive.tobytes()),
        "all_finite": bool(np.all(finite)),
        "all_positive": bool(np.all(positive)),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["slot20_after_history", "slot20_fresh_tail"], required=True)
    ap.add_argument("--wrapper-script", required=True)
    ap.add_argument("--jj-script", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--precision", required=True)
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-bin", required=True)
    a = ap.parse_args()

    jo = load_module("exp073jo_v03_parent", a.wrapper_script)
    jj = load_module("exp073jj_v03_parent", a.jj_script)
    if jo.CONTRACT_ID != CONTRACT_ID or jo.CAPACITY != CAPACITY or jo.PARSER_CAPACITY != PARSER_CAPACITY:
        raise SystemExit("JO recovery contract/capacity mismatch")
    if jo.H != H or jo.REL_TOL != REL_TOL or jo.NATIVE_KPD != NATIVE_KPD:
        raise SystemExit("JO frozen numerical constants mismatch")
    if jj.H != H or jj.REL_TOL != REL_TOL or jj.NATIVE_KPD != NATIVE_KPD:
        raise SystemExit("JJ response-engine constants mismatch")

    jj.CAPACITY = CAPACITY
    fine, ratio, lower_guard, upper_guard = jj.guarded_lattice(4096)
    if (lower_guard, upper_guard, len(fine)) != (0, 1, EXPECTED_NODE_COUNT):
        raise SystemExit("slot20 frozen JL lattice mismatch")
    jj.ResolutionSuite.coarse_nodes = fine
    jj.ResolutionSuite.fine_nodes = fine

    pre_z = float.fromhex("0x1.3851eb851eb85p-1")
    tail_z = float.fromhex("0x1.1c28f5c28f5c3p+0")
    pre_targets = np.asarray([0.0013, 0.0047, 0.013, 0.041], dtype=np.float64)
    tail_targets = np.asarray([0.0019, 0.0073, 0.021, 0.057], dtype=np.float64)

    jj.ResolutionSuite.audit = {}
    suite = jj.ResolutionSuite(Path(a.baseline), Path(a.precision), 20.0)
    try:
        if a.phase == "slot20_after_history":
            _ = suite.response(pre_z, pre_targets)
        response = np.ascontiguousarray(suite.response(tail_z, tail_targets), dtype="<f8")
        audit = json.loads(json.dumps(jj.ResolutionSuite.audit, sort_keys=True))
    finally:
        suite.close()

    if response.shape != EXPECTED_RESPONSE_SHAPE or response.dtype != np.dtype("<f8"):
        raise SystemExit(f"unexpected response identity shape={response.shape} dtype={response.dtype}")
    raw = response.tobytes(order="C")
    if len(raw) != EXPECTED_NBYTES:
        raise SystemExit(f"unexpected response byte count {len(raw)}")

    out_bin = Path(a.out_bin)
    out_bin.parent.mkdir(parents=True, exist_ok=True)
    out_bin.write_bytes(raw)
    masks = bool_mask_bits(response)
    result = {
        "schema": "EXP073JO_SLOT20_HISTORY_PHASE_RECEIPT_V0_3",
        "phase_split_version": PHASE_SPLIT_VERSION,
        "contract_id": CONTRACT_ID,
        "phase": a.phase,
        "classification": "SLOT20_HISTORY_PHASE_RECEIPT_PLUS_0_PLUS_0",
        "effect": "+0/+0",
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "wrapper_blob_sha": WRAPPER_BLOB_SHA,
        "slot": 20,
        "native_kpd": NATIVE_KPD,
        "h": H,
        "rel_tol": REL_TOL,
        "capacity": CAPACITY,
        "parser_capacity": PARSER_CAPACITY,
        "base_n": 4096,
        "requested_node_count": int(len(fine)),
        "lower_guard_count": int(lower_guard),
        "upper_guard_count": int(upper_guard),
        "grid_ratio_binary64": float(ratio),
        "node_sha256": sha_bytes(f8_bytes(fine)),
        "pre_z_hex": pre_z.hex(),
        "tail_z_hex": tail_z.hex(),
        "pre_targets_hex": [float(x).hex() for x in pre_targets],
        "tail_targets_hex": [float(x).hex() for x in tail_targets],
        "pre_query_executed": a.phase == "slot20_after_history",
        "response_shape": list(response.shape),
        "response_dtype": "<f8",
        "response_nbytes": len(raw),
        "response_sha256": sha_bytes(raw),
        **masks,
        "audit": audit,
        "token": (
            "PASS_EXP073JO_SLOT20_AFTER_HISTORY_RECEIPT_V0_3"
            if a.phase == "slot20_after_history"
            else "PASS_EXP073JO_SLOT20_FRESH_TAIL_RECEIPT_V0_3"
        ),
    }
    out_json = Path(a.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
