#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

WRAPPER_BLOB_SHA = "aa4c544c1e3e81137010fcdbd34f20567e1eb894"
CONTRACT_ID = "EXP073JO_ARTICLE3_JL_DURABLE_RESPONSE_CHECKPOINT_RECOVERY_V0_1"
SPLIT_VERSION = "EXP073JO_SPLIT_EXACT_BUILD_PREFLIGHT_V0_2"


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def f8_bytes(x) -> bytes:
    return np.ascontiguousarray(np.asarray(x, dtype="<f8")).tobytes()


def run_history_part(jo, jj, baseline: str, precision: str, slot: int) -> dict:
    if slot not in (10, 20):
        raise RuntimeError("history slot must be 10 or 20")
    jj.CAPACITY = jo.CAPACITY
    coarse, *_ = jj.guarded_lattice(2048)
    fine, *_ = jj.guarded_lattice(4096)
    if len(coarse) != 2049 or len(fine) != 4097:
        raise RuntimeError("JL grid identity mismatch in split JO history control")
    jj.ResolutionSuite.coarse_nodes = coarse
    jj.ResolutionSuite.fine_nodes = fine

    pre_z = float.fromhex("0x1.3851eb851eb85p-1")
    tail_z = float.fromhex("0x1.1c28f5c28f5c3p+0")
    pre_targets = np.asarray([0.0013, 0.0047, 0.013, 0.041], dtype=np.float64)
    tail_targets = np.asarray([0.0019, 0.0073, 0.021, 0.057], dtype=np.float64)

    jj.ResolutionSuite.audit = {}
    a = jj.ResolutionSuite(Path(baseline), Path(precision), float(slot))
    try:
        _ = a.response(pre_z, pre_targets)
        tail_after_history = np.ascontiguousarray(a.response(tail_z, tail_targets), dtype="<f8")
    finally:
        a.close()

    jj.ResolutionSuite.audit = {}
    b = jj.ResolutionSuite(Path(baseline), Path(precision), float(slot))
    try:
        tail_fresh = np.ascontiguousarray(b.response(tail_z, tail_targets), dtype="<f8")
    finally:
        b.close()

    exact_array = bool(np.array_equal(tail_after_history, tail_fresh))
    exact_finite = bool(np.array_equal(np.isfinite(tail_after_history), np.isfinite(tail_fresh)))
    exact_positive = bool(np.array_equal(tail_after_history > 0.0, tail_fresh > 0.0))
    if not (exact_array and exact_finite and exact_positive):
        raise RuntimeError(f"history-independence exact equality failed for slot {slot}")

    nodes = coarse if slot == 10 else fine
    return {
        "schema": "EXP073JO_HISTORY_INDEPENDENCE_PART_RESULT_V0_2",
        "split_version": SPLIT_VERSION,
        "contract_id": CONTRACT_ID,
        "part": f"history_slot{slot}",
        "classification": "HISTORY_INDEPENDENCE_PART_PASS_PLUS_0_PLUS_0",
        "effect": "+0/+0",
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "slot": slot,
        "exact_array_equal": True,
        "exact_finite_pattern_equal": True,
        "exact_positive_pattern_equal": True,
        "tail_response_sha256": sha_bytes(tail_after_history.tobytes()),
        "node_sha256": sha_bytes(f8_bytes(nodes)),
        "node_count": len(nodes),
        "pre_z_hex": pre_z.hex(),
        "tail_z_hex": tail_z.hex(),
        "pre_targets_hex": [float(x).hex() for x in pre_targets],
        "tail_targets_hex": [float(x).hex() for x in tail_targets],
        "token": f"PASS_EXP073JO_HISTORY_SLOT{slot}_EXACT_V0_2",
    }


def run_roundtrip_part(jo, jj, baseline: str, precision: str) -> dict:
    d = jo.run_roundtrip_control(jj, baseline, precision)
    if d.get("exact_response_bytes_equal") is not True or d.get("exact_audit_restoration") is not True:
        raise RuntimeError("wrapper roundtrip did not pass exact controls")
    return {
        "schema": "EXP073JO_CACHE_ROUNDTRIP_PART_RESULT_V0_2",
        "split_version": SPLIT_VERSION,
        "contract_id": CONTRACT_ID,
        "part": "cache_roundtrip_slot10",
        "classification": "CACHE_ROUNDTRIP_PART_PASS_PLUS_0_PLUS_0",
        "effect": "+0/+0",
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "slot": 10,
        "exact_response_bytes_equal": True,
        "exact_audit_restoration": True,
        "response_sha256": d["response_sha256"],
        "audit_after": d["audit_after"],
        "z_hex": d["z_hex"],
        "targets_hex": d["targets_hex"],
        "token": "PASS_EXP073JO_CACHE_ROUNDTRIP_SLOT10_EXACT_V0_2",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", choices=["history_slot10", "history_slot20", "cache_roundtrip_slot10"], required=True)
    ap.add_argument("--wrapper-script", required=True)
    ap.add_argument("--jj-script", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--precision", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    jo = load_module("exp073jo_split_parent", a.wrapper_script)
    jj = load_module("exp073jj_split_parent", a.jj_script)
    if jo.CONTRACT_ID != CONTRACT_ID or jo.FLUSH_EVERY != 16 or jo.CAPACITY != 4608 or jo.PARSER_CAPACITY != 131072:
        raise SystemExit("JO wrapper contract constants mismatch")
    if jo.H != 1e-4 or jo.REL_TOL != 1e-3 or jo.NATIVE_KPD != 20.0:
        raise SystemExit("JO wrapper frozen numerical constants mismatch")
    if jj.H != jo.H or jj.REL_TOL != jo.REL_TOL or jj.NATIVE_KPD != jo.NATIVE_KPD:
        raise SystemExit("canonical JJ constants mismatch")

    if a.part == "history_slot10":
        result = run_history_part(jo, jj, a.baseline, a.precision, 10)
    elif a.part == "history_slot20":
        result = run_history_part(jo, jj, a.baseline, a.precision, 20)
    else:
        result = run_roundtrip_part(jo, jj, a.baseline, a.precision)

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
