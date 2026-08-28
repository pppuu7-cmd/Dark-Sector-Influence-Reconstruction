#!/usr/bin/env python3
"""Exp073R1 -> Exp073P fail-closed admissibility interlock.

This module validates only the already-frozen R1 reproduction prerequisite.
It NEVER computes Exp073P support fractions, never reads covariance/G8, and
cannot classify Exp073P PASS/FAIL.  A successful result means only that a
trusted R1 summary is internally admissible as an input prerequisite to a
separate Exp073P execution under its frozen preregistration.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path

PASS_R1 = "PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1"
ADMISSIBLE = "ADMISSIBLE_EXP073P_EXECUTION_PREREQUISITE_R1"
REJECTED = "REJECTED_EXP073P_EXECUTION_PREREQUISITE_R1"
EXPECTED_SOURCE_SHA256 = "491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5"
EXPECTED_SOURCE_INDEX_SHA256 = "dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628"
EXPECTED_METACAL_SHA256 = "39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8"
EXPECTED_ROWS = 136_930_995
EXPECTED_METACAL_BYTES = 84_075_649_920
EXPECTED_SOURCE_INDEX_BYTES = 273_861_990
EXPECTED_SELECTION = "zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0"
EXPECTED_MAPPER = {"nside": 4096, "ordering": "RING", "coords": "C", "lonlat": True}
EXPECTED_GATE_STATE = {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}
EXPECTED_TRANSPORT = {"http_range_requests": 0, "whole_object_get": True, "accept_encoding": "identity"}


class InterlockError(ValueError):
    pass


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise InterlockError(f"{REJECTED}: {msg}")


def _is_sha256(x: object) -> bool:
    if not isinstance(x, str) or len(x) != 64:
        return False
    try:
        int(x, 16)
    except ValueError:
        return False
    return True


def validate_r1_summary(d: dict) -> dict:
    require(isinstance(d, dict), "summary is not an object")
    require(d.get("experiment") == "Exp073R1", "wrong experiment")
    require(d.get("status") == PASS_R1, "R1 internal PASS absent")
    require(d.get("transport") == EXPECTED_TRANSPORT, "transport drift")
    require(d.get("observed_bytes_metacal") == EXPECTED_METACAL_BYTES, "observed metacal bytes drift")
    require(d.get("expected_bytes_metacal") == EXPECTED_METACAL_BYTES, "expected metacal bytes drift")
    require(d.get("metacal_sha256") == EXPECTED_METACAL_SHA256, "metacal SHA256 drift")
    require(d.get("expected_metacal_sha256") == EXPECTED_METACAL_SHA256, "expected metacal SHA256 drift")

    sb = d.get("source_identity_binding")
    require(isinstance(sb, dict), "source identity binding missing")
    require(sb.get("source_whole_sha256") == EXPECTED_SOURCE_SHA256, "source SHA256 drift")
    require(sb.get("source_index_bytes") == EXPECTED_SOURCE_INDEX_BYTES, "source-index bytes drift")
    require(sb.get("source_index_sha256") == EXPECTED_SOURCE_INDEX_SHA256, "source-index SHA256 drift")

    require(d.get("rows_read_source_index") == EXPECTED_ROWS, "source row count drift")
    require(d.get("rows_read_metacal") == EXPECTED_ROWS, "metacal row count drift")
    require(d.get("selection") == EXPECTED_SELECTION, "selection drift")
    require(d.get("mapper") == EXPECTED_MAPPER, "HEALPix mapper drift")
    require(d.get("out_of_range_pixel_count") == 0, "out-of-range pixels present")

    selected = d.get("selected_rows_per_bin")
    require(isinstance(selected, dict), "selected_rows_per_bin missing")
    require(set(selected) == {"0", "1", "2", "3"}, "tomographic-bin key drift")
    require(all(isinstance(v, int) and not isinstance(v, bool) and v > 0 for v in selected.values()), "empty/invalid selected bin")

    repeat = d.get("repeatability_from_pixel_records")
    require(isinstance(repeat, dict) and set(repeat) == {"0", "1", "2", "3"}, "repeatability bins drift")
    for b, checks in repeat.items():
        require(isinstance(checks, dict) and checks, f"repeatability checks missing for bin {b}")
        require(all(v is True for v in checks.values()), f"repeatability failure for bin {b}")

    parent = d.get("parent_r0")
    require(isinstance(parent, dict), "R0 parent record missing")
    checks = parent.get("checks")
    require(isinstance(checks, dict) and checks, "R0 parent checks missing")
    require(all(v is True for v in checks.values()), "R0 parent hard control failed")

    masks = d.get("masks")
    require(isinstance(masks, dict) and set(masks) == {"0", "1", "2", "3"}, "mask records incomplete")
    mask_sha = {}
    for b, rec in masks.items():
        require(isinstance(rec, dict), f"mask record invalid for bin {b}")
        sha = rec.get("sha256")
        require(_is_sha256(sha), f"mask SHA256 invalid for bin {b}")
        mask_sha[b] = sha

    require(d.get("science_gate_scored") is False, "R1 scored science gate")
    require(d.get("f_invalid_computed") is False, "R1 computed Exp073P support fraction")
    require(d.get("covariance_read") is False, "R1 read covariance")
    require(d.get("G8_read") is False, "R1 read G8")
    require(d.get("gate_state") == EXPECTED_GATE_STATE, "gate state drift")

    return {
        "status": ADMISSIBLE,
        "r1_status": PASS_R1,
        "source_sha256": EXPECTED_SOURCE_SHA256,
        "metacal_sha256": EXPECTED_METACAL_SHA256,
        "rows": EXPECTED_ROWS,
        "selected_rows_per_bin": selected,
        "mask_sha256": mask_sha,
        "exp073p_scored": False,
        "f_invalid_computed_by_interlock": False,
        "covariance_read": False,
        "G8_read": False,
        "gate_state": EXPECTED_GATE_STATE,
    }


def _valid_fixture() -> dict:
    return {
        "experiment": "Exp073R1",
        "status": PASS_R1,
        "transport": copy.deepcopy(EXPECTED_TRANSPORT),
        "observed_bytes_metacal": EXPECTED_METACAL_BYTES,
        "expected_bytes_metacal": EXPECTED_METACAL_BYTES,
        "metacal_sha256": EXPECTED_METACAL_SHA256,
        "expected_metacal_sha256": EXPECTED_METACAL_SHA256,
        "source_identity_binding": {
            "source_whole_sha256": EXPECTED_SOURCE_SHA256,
            "source_index_bytes": EXPECTED_SOURCE_INDEX_BYTES,
            "source_index_sha256": EXPECTED_SOURCE_INDEX_SHA256,
        },
        "rows_read_source_index": EXPECTED_ROWS,
        "rows_read_metacal": EXPECTED_ROWS,
        "selection": EXPECTED_SELECTION,
        "mapper": copy.deepcopy(EXPECTED_MAPPER),
        "out_of_range_pixel_count": 0,
        "selected_rows_per_bin": {str(i): 1 for i in range(4)},
        "repeatability_from_pixel_records": {str(i): {"record_to_mask": True, "second_rebuild": True} for i in range(4)},
        "parent_r0": {"checks": {"identity": True, "pixels": True}},
        "masks": {str(i): {"sha256": hashlib.sha256(f"mask-{i}".encode()).hexdigest()} for i in range(4)},
        "science_gate_scored": False,
        "f_invalid_computed": False,
        "covariance_read": False,
        "G8_read": False,
        "gate_state": copy.deepcopy(EXPECTED_GATE_STATE),
    }


def _must_reject(mutator) -> None:
    d = _valid_fixture()
    mutator(d)
    try:
        validate_r1_summary(d)
    except InterlockError:
        return
    raise AssertionError("mutant unexpectedly crossed R1->P interlock")


def selftest() -> None:
    out = validate_r1_summary(_valid_fixture())
    assert out["status"] == ADMISSIBLE
    assert out["exp073p_scored"] is False
    assert out["covariance_read"] is False and out["G8_read"] is False

    mutants = [
        lambda d: d.__setitem__("status", "success"),
        lambda d: d["transport"].__setitem__("http_range_requests", 1),
        lambda d: d.__setitem__("observed_bytes_metacal", EXPECTED_METACAL_BYTES - 1),
        lambda d: d.__setitem__("metacal_sha256", "0" * 64),
        lambda d: d["source_identity_binding"].__setitem__("source_whole_sha256", "0" * 64),
        lambda d: d.__setitem__("rows_read_metacal", EXPECTED_ROWS - 1),
        lambda d: d.__setitem__("selection", EXPECTED_SELECTION + " and True"),
        lambda d: d["mapper"].__setitem__("nside", 2048),
        lambda d: d.__setitem__("out_of_range_pixel_count", 1),
        lambda d: d["selected_rows_per_bin"].__setitem__("2", 0),
        lambda d: d["repeatability_from_pixel_records"]["1"].__setitem__("second_rebuild", False),
        lambda d: d["parent_r0"]["checks"].__setitem__("pixels", False),
        lambda d: d["masks"]["3"].__setitem__("sha256", "bad"),
        lambda d: d.__setitem__("science_gate_scored", True),
        lambda d: d.__setitem__("f_invalid_computed", True),
        lambda d: d.__setitem__("covariance_read", True),
        lambda d: d.__setitem__("G8_read", True),
        lambda d: d["gate_state"].__setitem__("G7", "PASS"),
    ]
    for m in mutants:
        _must_reject(m)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--r1-summary", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        selftest()
        print("PASS_EXP073P_R1_ADMISSIBILITY_INTERLOCK_SELFTEST_V0_1")
        return

    if args.r1_summary is None or args.out is None:
        ap.error("--r1-summary and --out are required outside --selftest")

    raw = args.r1_summary.read_bytes()
    d = json.loads(raw)
    result = validate_r1_summary(d)
    result["r1_summary_sha256"] = hashlib.sha256(raw).hexdigest()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(ADMISSIBLE)


if __name__ == "__main__":
    main()
