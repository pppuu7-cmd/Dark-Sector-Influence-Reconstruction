#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import math
import random
from typing import Any

Z_MIN = 0.295
Z_MAX = 2.33
K_MAX_MPC_INV = 0.06664762008318016
MAX_INVALID = 0.05
MIN_RETAINED = 15
PASS = "PASS_PHYSICAL_SUPPORT_ARTICLE3"
FAIL = "FAIL_PHYSICAL_SUPPORT_ARTICLE3"
INVALID = "INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT"

# Selection-stage payloads that must not exist anywhere in the support input.
FORBIDDEN_KEY_TOKENS = (
    "covariance",
    "inverse_covariance",
    "whitening",
    "nuisance",
    "svd",
    "relation",
    "pvalue",
    "chi2",
    "g7",
    "g8",
)

EXPECTED_PARENT = {
    "run_id": 33175886694,
    "terminal_conclusion": "success",
    "final_assertion_conclusion": "success",
    "upstream_pass_token": "SYNTHETIC_PARENT_PASS_TOKEN",
    "artifact_id": 9999999999,
    "artifact_sha256": "0" * 64,
}

EXPECTED_ANTI_LEAKAGE = {
    "normalization_scope": "FULL_PRE_SUPPORT_COORDINATE_SET",
    "crop_before_normalization": False,
    "fiducial_P_weighting": False,
    "effective_ell_override": False,
    "signed_Wm": True,
    "selection_reads": [],
}


def ordered_id_digest(ids: list[str]) -> str:
    payload = json.dumps(ids, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def forbidden_key_path(obj: Any, path: str = "") -> str | None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            key_l = str(key).lower()
            if any(token in key_l for token in FORBIDDEN_KEY_TOKENS):
                return f"{path}.{key}" if path else str(key)
            child = forbidden_key_path(value, f"{path}.{key}" if path else str(key))
            if child is not None:
                return child
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            child = forbidden_key_path(value, f"{path}[{i}]")
            if child is not None:
                return child
    return None


def classify(manifest: dict[str, Any], expected_parent: dict[str, Any]) -> dict[str, Any]:
    """Pure fail-closed reference classifier used only by synthetic QA."""
    try:
        if not isinstance(manifest, dict):
            raise ValueError("manifest must be an object")

        parent = manifest["parent"]
        if not isinstance(parent, dict):
            raise ValueError("parent must be an object")
        for key, expected in expected_parent.items():
            if parent.get(key) != expected:
                raise ValueError(f"parent mismatch: {key}")

        anti = manifest["anti_leakage"]
        if anti != EXPECTED_ANTI_LEAKAGE:
            raise ValueError("anti-leakage metadata mismatch")

        # anti_leakage is validated by exact equality above. Scan every other payload recursively.
        scan_payload = {k: v for k, v in manifest.items() if k != "anti_leakage"}
        forbidden = forbidden_key_path(scan_payload)
        if forbidden is not None:
            raise ValueError(f"forbidden downstream selection payload at {forbidden}")

        rows = manifest["rows"]
        if not isinstance(rows, list):
            raise ValueError("rows must be a list")

        seen_ids: set[str] = set()
        seen_ordinals: set[int] = set()
        parsed: list[tuple[int, str, float, float, list[float]]] = []

        for row in rows:
            if not isinstance(row, dict):
                raise ValueError("row must be an object")
            cid = row.get("coordinate_id")
            ordinal = row.get("ordinal")
            z = row.get("z")
            k = row.get("k_Mpc^-1")
            response = row.get("final_response_abs_values")

            if not isinstance(cid, str) or not cid:
                raise ValueError("malformed coordinate_id")
            if cid in seen_ids:
                raise ValueError("duplicate coordinate_id")
            seen_ids.add(cid)

            if isinstance(ordinal, bool) or not isinstance(ordinal, int) or ordinal < 0:
                raise ValueError("malformed ordinal")
            if ordinal in seen_ordinals:
                raise ValueError("duplicate ordinal")
            seen_ordinals.add(ordinal)

            if isinstance(z, bool) or not isinstance(z, (int, float)) or not math.isfinite(float(z)):
                raise ValueError("malformed z")
            if isinstance(k, bool) or not isinstance(k, (int, float)) or not math.isfinite(float(k)):
                raise ValueError("malformed k")
            if not isinstance(response, list) or len(response) == 0:
                raise ValueError("missing/empty final-response vector")

            response_f: list[float] = []
            for value in response:
                if isinstance(value, bool) or not isinstance(value, (int, float)):
                    raise ValueError("non-numeric final-response component")
                response_f.append(float(value))

            parsed.append((ordinal, cid, float(z), float(k), response_f))

        # Canonical output order is inherited upstream ordinal, not input row order.
        parsed.sort(key=lambda x: x[0])

        geometric: list[tuple[int, str, bool]] = []
        for ordinal, cid, z, k, response in parsed:
            in_domain = Z_MIN <= z <= Z_MAX and 0.0 < k <= K_MAX_MPC_INV
            if not in_domain:
                continue
            envelope_valid = all(math.isfinite(x) and x > 0.0 for x in response)
            geometric.append((ordinal, cid, envelope_valid))

        n_geometric = len(geometric)
        n_invalid = sum(not valid for _, _, valid in geometric)
        retained_ids = [cid for _, cid, valid in geometric if valid]
        f_invalid = (n_invalid / n_geometric) if n_geometric else None

        passes = bool(
            n_geometric > 0
            and f_invalid is not None
            and f_invalid <= MAX_INVALID
            and len(retained_ids) >= MIN_RETAINED
        )
        return {
            "classification": PASS if passes else FAIL,
            "counts": {
                "input": len(parsed),
                "geometric_eligible": n_geometric,
                "invalid_envelope": n_invalid,
                "retained": len(retained_ids),
            },
            "f_invalid": f_invalid,
            "retained_ids": retained_ids,
            "retained_ids_sha256": ordered_id_digest(retained_ids),
            "covariance_restriction_authorized": passes,
        }
    except Exception as exc:
        return {
            "classification": INVALID,
            "error": f"{type(exc).__name__}: {exc}",
            "covariance_restriction_authorized": False,
        }


def row(i: int, *, z: float = 0.5, k: float = 0.01, response: list[float] | None = None) -> dict[str, Any]:
    return {
        "coordinate_id": f"c{i:03d}",
        "ordinal": i,
        "z": z,
        "k_Mpc^-1": k,
        "final_response_abs_values": [1.0, 2.0] if response is None else response,
    }


def base_manifest(n: int = 20) -> dict[str, Any]:
    return {
        "parent": copy.deepcopy(EXPECTED_PARENT),
        "anti_leakage": copy.deepcopy(EXPECTED_ANTI_LEAKAGE),
        "rows": [row(i) for i in range(n)],
    }


def demand(name: str, condition: bool, details: Any, records: list[dict[str, Any]]) -> None:
    records.append({"name": name, "pass": bool(condition), "details": details})
    if not condition:
        raise AssertionError(f"{name}: {details}")


def main() -> None:
    records: list[dict[str, Any]] = []

    baseline = classify(base_manifest(), EXPECTED_PARENT)
    demand("baseline_pass", baseline["classification"] == PASS, baseline, records)

    permuted = base_manifest()
    random.Random(73001).shuffle(permuted["rows"])
    rp = classify(permuted, EXPECTED_PARENT)
    demand(
        "input_permutation_invariance",
        rp["classification"] == PASS and rp["retained_ids_sha256"] == baseline["retained_ids_sha256"],
        rp,
        records,
    )

    boundary = base_manifest()
    boundary["rows"][0]["z"] = Z_MIN
    boundary["rows"][1]["z"] = Z_MAX
    boundary["rows"][2]["k_Mpc^-1"] = K_MAX_MPC_INV
    rb = classify(boundary, EXPECTED_PARENT)
    demand("inclusive_exact_boundaries", rb["classification"] == PASS and rb["counts"]["retained"] == 20, rb, records)

    outside = base_manifest()
    outside["rows"][0]["z"] = math.nextafter(Z_MIN, -math.inf)
    outside["rows"][1]["z"] = math.nextafter(Z_MAX, math.inf)
    outside["rows"][2]["k_Mpc^-1"] = math.nextafter(K_MAX_MPC_INV, math.inf)
    ro = classify(outside, EXPECTED_PARENT)
    demand(
        "nextafter_outside_boundaries_rejected",
        ro["classification"] == PASS and ro["counts"]["geometric_eligible"] == 17 and ro["counts"]["retained"] == 17,
        ro,
        records,
    )

    exact_fraction = base_manifest(20)
    exact_fraction["rows"][0]["final_response_abs_values"] = [0.0, 1.0]
    rf = classify(exact_fraction, EXPECTED_PARENT)
    demand(
        "invalid_fraction_exact_0p05_passes",
        rf["classification"] == PASS and rf["f_invalid"] == 0.05 and rf["counts"]["retained"] == 19,
        rf,
        records,
    )

    over_fraction = base_manifest(19)
    over_fraction["rows"][0]["final_response_abs_values"] = [float("nan"), 1.0]
    rof = classify(over_fraction, EXPECTED_PARENT)
    demand(
        "invalid_fraction_above_0p05_scientific_fail",
        rof["classification"] == FAIL and rof["f_invalid"] > 0.05 and not rof["covariance_restriction_authorized"],
        rof,
        records,
    )

    r15 = classify(base_manifest(15), EXPECTED_PARENT)
    demand("minimum_15_retained_passes", r15["classification"] == PASS, r15, records)

    r14 = classify(base_manifest(14), EXPECTED_PARENT)
    demand("fourteen_retained_scientific_fail", r14["classification"] == FAIL, r14, records)

    zero_and_inf = base_manifest(20)
    zero_and_inf["rows"][0]["final_response_abs_values"] = [0.0, 2.0]
    zero_and_inf["rows"][1]["final_response_abs_values"] = [1.0, float("inf")]
    rzi = classify(zero_and_inf, EXPECTED_PARENT)
    demand(
        "zero_or_nonfinite_component_invalidates_common_envelope",
        rzi["classification"] == FAIL and rzi["counts"]["invalid_envelope"] == 2,
        rzi,
        records,
    )

    scaled = base_manifest()
    for rr in scaled["rows"]:
        rr["final_response_abs_values"] = [x * 1.0e20 for x in rr["final_response_abs_values"]]
    rs = classify(scaled, EXPECTED_PARENT)
    demand(
        "positive_amplitude_scale_invariance",
        rs["classification"] == PASS and rs["retained_ids_sha256"] == baseline["retained_ids_sha256"],
        rs,
        records,
    )

    dup_id = base_manifest()
    dup_id["rows"][1]["coordinate_id"] = dup_id["rows"][0]["coordinate_id"]
    rdi = classify(dup_id, EXPECTED_PARENT)
    demand("duplicate_id_is_invalid_for_science", rdi["classification"] == INVALID, rdi, records)

    dup_ord = base_manifest()
    dup_ord["rows"][1]["ordinal"] = dup_ord["rows"][0]["ordinal"]
    rdo = classify(dup_ord, EXPECTED_PARENT)
    demand("duplicate_ordinal_is_invalid_for_science", rdo["classification"] == INVALID, rdo, records)

    malformed = base_manifest()
    malformed["rows"][0]["final_response_abs_values"] = []
    rm = classify(malformed, EXPECTED_PARENT)
    demand("missing_response_vector_is_invalid_for_science", rm["classification"] == INVALID, rm, records)

    parent_bad = base_manifest()
    parent_bad["parent"]["artifact_sha256"] = "1" * 64
    rpb = classify(parent_bad, EXPECTED_PARENT)
    demand("parent_digest_mismatch_is_invalid_for_science", rpb["classification"] == INVALID, rpb, records)

    assertion_bad = base_manifest()
    assertion_bad["parent"]["final_assertion_conclusion"] = "failure"
    rab = classify(assertion_bad, EXPECTED_PARENT)
    demand("upstream_final_assertion_not_success_is_invalid", rab["classification"] == INVALID, rab, records)

    leak = base_manifest()
    leak["covariance"] = [[1.0]]
    rl = classify(leak, EXPECTED_PARENT)
    demand("covariance_payload_leak_is_invalid_for_science", rl["classification"] == INVALID, rl, records)

    nuisance_leak = base_manifest()
    nuisance_leak["rows"][0]["nuisance_alignment"] = 0.2
    rnl = classify(nuisance_leak, EXPECTED_PARENT)
    demand("nuisance_payload_leak_is_invalid_for_science", rnl["classification"] == INVALID, rnl, records)

    anti_bad = base_manifest()
    anti_bad["anti_leakage"]["crop_before_normalization"] = True
    rac = classify(anti_bad, EXPECTED_PARENT)
    demand("crop_before_normalization_is_invalid_for_science", rac["classification"] == INVALID, rac, records)

    selection_bad = base_manifest()
    selection_bad["anti_leakage"]["selection_reads"] = ["whitening"]
    rsel = classify(selection_bad, EXPECTED_PARENT)
    demand("downstream_selection_read_is_invalid_for_science", rsel["classification"] == INVALID, rsel, records)

    result = {
        "experiment": "Article3PhysicalSupportSyntheticQA_v0_1",
        "scope": "SYNTHETIC_ONLY_NO_DES_ARTIFACT_ACCESS",
        "upstream_real_run_id_frozen": 33175886694,
        "real_science_gate_scored": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "constants": {
            "z_min": Z_MIN,
            "z_max": Z_MAX,
            "k_max_Mpc^-1": K_MAX_MPC_INV,
            "max_invalid_fraction": MAX_INVALID,
            "min_retained": MIN_RETAINED,
        },
        "tests": records,
        "status": "PASS_ARTICLE3_PHYSICAL_SUPPORT_SYNTHETIC_QA_V0_1",
        "covariance_restriction_authorized_by_this_QA": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
