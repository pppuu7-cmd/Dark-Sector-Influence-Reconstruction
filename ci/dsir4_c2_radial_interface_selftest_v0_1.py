#!/usr/bin/env python3
"""Synthetic fail-closed QA for DSIR4 C2 radial executor interface v0.1.

No DES data, covariance, nuisance information, relation/null statistic or model
score is read here. Passing this script is implementation readiness only.
"""
from __future__ import annotations

import hashlib
import json
import math

SLOTS = [
    "Wm_S0", "Wm_S1", "Wm_S2", "Wm_S3",
    "WW_S0_S0", "WW_S0_S1", "WW_S0_S2", "WW_S0_S3",
    "WW_S1_S1", "WW_S1_S2", "WW_S1_S3",
    "WW_S2_S2", "WW_S2_S3", "WW_S3_S3",
]
SOURCE_BRIDGE = {0: "BIN1", 1: "BIN2", 2: "BIN3", 3: "BIN4"}
SOURCE_SHA = "b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b"
LENS_SHA = "114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca"
FORBIDDEN_KEYS = {
    "covariance", "inverse_covariance", "whitening", "nuisance", "nuisance_svd",
    "nuisance_rank", "relation", "null", "g7", "g8", "article_selection",
    "fiducial_p_weighting", "effective_ell", "effective_z", "effective_k",
    "interpolation", "extrapolation", "smoothing", "rounding",
}
INVALID = "INVALID_FOR_SCIENCE_RADIAL_INTERFACE"


def require(cond: bool, why: str) -> None:
    if not cond:
        raise ValueError(f"{INVALID}: {why}")


def validate_contract_input(d: dict) -> None:
    require(d.get("ordered_slots") == SLOTS, "ordered slot mismatch")
    require(d.get("source_bridge") == SOURCE_BRIDGE, "source bridge mismatch")
    require(d.get("source_sha256") == SOURCE_SHA, "source payload SHA mismatch")
    require(d.get("lens_sha256") == LENS_SHA, "lens payload SHA mismatch")
    require(d.get("photoz_shift_dz") == 0, "nonzero photo-z shift")
    require(d.get("k_unit") == "Mpc^-1", "physical-k unit mismatch")
    require(d.get("signed_Wm") is True, "Wm must remain signed")
    require(d.get("fiducial_P_weighting") is False, "fiducial P weighting forbidden")
    lower = {str(k).lower() for k in d}
    leaked = sorted(lower & FORBIDDEN_KEYS)
    # Explicit allowed false-valued bookkeeping keys are handled above.
    leaked = [k for k in leaked if not (k == "fiducial_p_weighting" and d.get("fiducial_P_weighting") is False)]
    require(not leaked, f"forbidden metadata keys {leaked}")


def validate_rows(rows: list[dict]) -> list[dict]:
    ids = set()
    ords = set()
    for row in rows:
        cid = row.get("coordinate_id")
        ordinal = row.get("ordinal")
        require(isinstance(cid, str) and cid != "", "empty coordinate_id")
        require(isinstance(ordinal, int) and ordinal >= 0, "bad ordinal")
        require(cid not in ids, "duplicate coordinate_id")
        require(ordinal not in ords, "duplicate ordinal")
        ids.add(cid); ords.add(ordinal)
        require(row.get("slot") in SLOTS, "unknown slot")
        require(isinstance(row.get("band_index"), int) and 0 <= row["band_index"] <= 38, "band out of range")
        z = row.get("z"); k = row.get("k_Mpc^-1")
        require(isinstance(z, float) and math.isfinite(z), "nonfinite/noncanonical z")
        require(isinstance(k, float) and math.isfinite(k) and k > 0.0, "nonfinite/nonpositive k")
        vals = row.get("final_response_abs_values")
        require(isinstance(vals, list) and len(vals) > 0, "empty response vector")
        require(all(isinstance(v, float) and math.isfinite(v) for v in vals), "nonfinite response")
        norm = row.get("radial_normalization")
        require(isinstance(norm, float) and math.isfinite(norm) and norm > 0.0, "bad radial normalization")
    return sorted(rows, key=lambda r: r["ordinal"])


def digest_rows(rows: list[dict]) -> str:
    ordered = validate_rows(rows)
    payload = json.dumps(ordered, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(payload).hexdigest()


def expect_fail(fn, *args) -> None:
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError("expected fail-closed ValueError")


def base_input() -> dict:
    return {
        "ordered_slots": list(SLOTS),
        "source_bridge": dict(SOURCE_BRIDGE),
        "source_sha256": SOURCE_SHA,
        "lens_sha256": LENS_SHA,
        "photoz_shift_dz": 0,
        "k_unit": "Mpc^-1",
        "signed_Wm": True,
        "fiducial_P_weighting": False,
    }


def sample_rows() -> list[dict]:
    return [
        {"coordinate_id":"Wm_S0:b0:z0","ordinal":0,"slot":"Wm_S0","band_index":0,
         "z":0.30,"k_Mpc^-1":0.01,"final_response_abs_values":[1.0,2.0],"radial_normalization":1.0},
        {"coordinate_id":"WW_S0_S0:b0:z0","ordinal":1,"slot":"WW_S0_S0","band_index":0,
         "z":0.31,"k_Mpc^-1":0.02,"final_response_abs_values":[0.5,3.0],"radial_normalization":2.0},
    ]


def selftest() -> None:
    d = base_input(); validate_contract_input(d)

    # 14-slot order/permutation fail closed.
    bad = base_input(); bad["ordered_slots"][0], bad["ordered_slots"][1] = bad["ordered_slots"][1], bad["ordered_slots"][0]
    expect_fail(validate_contract_input, bad)

    # Source bridge and payload identities are exact.
    bad = base_input(); bad["source_bridge"] = {0:"BIN2",1:"BIN1",2:"BIN3",3:"BIN4"}; expect_fail(validate_contract_input, bad)
    bad = base_input(); bad["source_sha256"] = "0"*64; expect_fail(validate_contract_input, bad)
    bad = base_input(); bad["lens_sha256"] = "0"*64; expect_fail(validate_contract_input, bad)

    # dz and units.
    bad = base_input(); bad["photoz_shift_dz"] = 0.01; expect_fail(validate_contract_input, bad)
    bad = base_input(); bad["k_unit"] = "h/Mpc"; expect_fail(validate_contract_input, bad)

    # No effective/interpolated/downstream metadata.
    for key in sorted(FORBIDDEN_KEYS - {"fiducial_p_weighting"}):
        bad = base_input(); bad[key] = True; expect_fail(validate_contract_input, bad)

    rows = sample_rows()
    h1 = digest_rows(rows)
    h2 = digest_rows(list(reversed(rows)))
    assert h1 == h2, "input permutation changed canonical digest"

    bad = sample_rows(); bad[1]["coordinate_id"] = bad[0]["coordinate_id"]; expect_fail(digest_rows, bad)
    bad = sample_rows(); bad[1]["ordinal"] = bad[0]["ordinal"]; expect_fail(digest_rows, bad)
    bad = sample_rows(); bad[0]["k_Mpc^-1"] = math.nan; expect_fail(digest_rows, bad)
    bad = sample_rows(); bad[0]["radial_normalization"] = 0.0; expect_fail(digest_rows, bad)
    bad = sample_rows(); bad[0]["final_response_abs_values"] = [1.0, math.inf]; expect_fail(digest_rows, bad)

    print("PASS_DSIR4_C2_RADIAL_INTERFACE_SYNTHETIC_QA_V0_1")


if __name__ == "__main__":
    selftest()
