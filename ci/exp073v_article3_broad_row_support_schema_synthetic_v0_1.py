#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import random
from pathlib import Path
from typing import Any

Z_MIN = 0.295
Z_MAX = 2.33
K_MAX = 0.06664762008318016
MAX_INVALID = 0.05
MIN_RETAINED = 15
EXP073U_ORDER_SHA256 = "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"

PASS_A = "PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1"
FAIL_A = "FAIL_ARTICLE3_OPERATOR_SUPPORT_V0_1"
INVALID_A = "INVALID_FOR_SCIENCE_ARTICLE3_OPERATOR_SUPPORT_V0_1"
PASS_B = "PASS_PHYSICAL_SUPPORT_ARTICLE3"
FAIL_B = "FAIL_PHYSICAL_SUPPORT_ARTICLE3"
INVALID_B = "INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT"
INVALID_SCHEMA = "INVALID_FOR_SCIENCE_EXP073V_BROAD_ROW_SCHEMA_V0_1"

FORBIDDEN_DOWNSTREAM_TOKENS = (
    "covariance",
    "inverse_covariance",
    "whitening",
    "cholesky",
    "nuisance",
    "svd",
    "quotient",
    "relation",
    "null_residual",
    "pvalue",
    "chi2",
    "g7",
    "g8",
    "g9",
)

ROW_SCALAR_PROXY_KEYS = {
    "z",
    "k_Mpc^-1",
    "k_mpc^-1",
    "ell",
    "effective_z",
    "effective_k",
    "effective_k_Mpc^-1",
    "effective_ell",
    "z_eff",
    "k_eff",
    "ell_eff",
    "weighted_mean_k",
    "centroid_k",
    "midpoint_k",
}

EXPECTED_ANTI_LEAKAGE = {
    "normalization_scope": "FULL_PRE_SUPPORT_COORDINATE_SET",
    "crop_before_normalization": False,
    "fiducial_P_weighting": False,
    "effective_ell_override": False,
    "effective_z_override": False,
    "effective_k_override": False,
    "signed_Wm": True,
    "selection_reads": [],
}


def ordered_id_digest(ids: list[str]) -> str:
    return hashlib.sha256(("\n".join(ids) + "\n").encode("utf-8")).hexdigest()


def forbidden_key_path(obj: Any, path: str = "") -> str | None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            key_l = str(key).lower()
            if any(token in key_l for token in FORBIDDEN_DOWNSTREAM_TOKENS):
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


def finite_number(value: Any, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be numeric")
    x = float(value)
    if not math.isfinite(x):
        raise ValueError(f"{name} must be finite")
    return x


def parse_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    if not isinstance(manifest, dict):
        raise ValueError("manifest must be an object")
    if manifest.get("exp073u_order_sha256") != EXP073U_ORDER_SHA256:
        raise ValueError("Exp073U ordered-ID authority mismatch")
    if manifest.get("anti_leakage") != EXPECTED_ANTI_LEAKAGE:
        raise ValueError("anti-leakage metadata mismatch")

    scan_payload = {k: v for k, v in manifest.items() if k != "anti_leakage"}
    forbidden = forbidden_key_path(scan_payload)
    if forbidden is not None:
        raise ValueError(f"forbidden downstream payload at {forbidden}")

    rows = manifest.get("rows")
    if not isinstance(rows, list):
        raise ValueError("rows must be a list")

    seen_ids: set[str] = set()
    seen_ordinals: set[int] = set()
    parsed: list[dict[str, Any]] = []

    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("row must be an object")
        bad_proxy = sorted(set(row).intersection(ROW_SCALAR_PROXY_KEYS))
        if bad_proxy:
            raise ValueError(f"row-level scalar physical proxy forbidden: {bad_proxy}")

        cid = row.get("coordinate_id")
        ordinal = row.get("ordinal")
        block = row.get("observable_block")
        atoms = row.get("support_atoms")

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

        if block not in {"Wm", "WW", "BOSS"}:
            raise ValueError("unknown observable_block")
        if not isinstance(atoms, list) or not atoms:
            raise ValueError("support_atoms must be a non-empty list")

        parsed_atoms: list[dict[str, Any]] = []
        for atom in atoms:
            if not isinstance(atom, dict):
                raise ValueError("support atom must be an object")
            z = finite_number(atom.get("z"), "atom z")
            k = finite_number(atom.get("k_Mpc^-1"), "atom k")
            w = finite_number(atom.get("operator_abs_weight"), "operator_abs_weight")
            if k <= 0.0:
                raise ValueError("physical support atom k must be strictly positive")
            if w < 0.0:
                raise ValueError("operator_abs_weight must be non-negative")

            response = atom.get("final_response_abs_values")
            if not isinstance(response, list) or not response:
                raise ValueError("missing/empty final response vector")
            response_f: list[float] = []
            for rv in response:
                if isinstance(rv, bool) or not isinstance(rv, (int, float)):
                    raise ValueError("final response component must be numeric")
                response_f.append(float(rv))

            parsed_atoms.append(
                {
                    "z": z,
                    "k": k,
                    "weight": w,
                    "response": response_f,
                }
            )

        den = sum(a["weight"] for a in parsed_atoms)
        if not math.isfinite(den) or den <= 0.0:
            raise ValueError("non-positive broad operator normalization")

        parsed.append(
            {
                "coordinate_id": cid,
                "ordinal": ordinal,
                "observable_block": block,
                "atoms": parsed_atoms,
            }
        )

    parsed.sort(key=lambda r: r["ordinal"])
    return parsed


def in_domain(atom: dict[str, Any]) -> bool:
    return Z_MIN <= atom["z"] <= Z_MAX and 0.0 < atom["k"] <= K_MAX


def layer_a_row(row: dict[str, Any]) -> dict[str, Any]:
    den = sum(a["weight"] for a in row["atoms"])
    num = sum(a["weight"] for a in row["atoms"] if not in_domain(a))
    f_invalid = num / den
    return {
        "coordinate_id": row["coordinate_id"],
        "ordinal": row["ordinal"],
        "operator_f_invalid": f_invalid,
        "retained": bool(f_invalid <= MAX_INVALID),
    }


def layer_b_row_valid(row: dict[str, Any]) -> bool:
    active = [a for a in row["atoms"] if a["weight"] > 0.0 and in_domain(a)]
    if not active:
        return False
    for atom in active:
        if not atom["response"]:
            return False
        if not all(math.isfinite(x) and x > 0.0 for x in atom["response"]):
            return False
    return True


def classify(manifest: dict[str, Any]) -> dict[str, Any]:
    try:
        rows = parse_manifest(manifest)
    except Exception as exc:
        return {
            "schema_classification": INVALID_SCHEMA,
            "layer_a_classification": INVALID_A,
            "layer_b_classification": INVALID_B,
            "error": f"{type(exc).__name__}: {exc}",
            "simulated_dual_support_pass": False,
            "real_covariance_authorized": False,
        }

    a_rows = [layer_a_row(r) for r in rows]
    keep_ordinals = {r["ordinal"] for r in a_rows if r["retained"]}
    s_op = [r for r in rows if r["ordinal"] in keep_ordinals]
    a_pass = len(s_op) >= MIN_RETAINED

    result: dict[str, Any] = {
        "schema_classification": "PASS_EXP073V_BROAD_ROW_SCHEMA_PARSE_V0_1",
        "layer_a_classification": PASS_A if a_pass else FAIL_A,
        "layer_a": {
            "input_rows": len(rows),
            "retained_rows": len(s_op),
            "retained_ids": [r["coordinate_id"] for r in s_op],
            "retained_ids_sha256": ordered_id_digest([r["coordinate_id"] for r in s_op]),
            "rows": a_rows,
        },
        "real_covariance_authorized": False,
    }

    if not a_pass:
        result["layer_b_classification"] = "NOT_AUTHORIZED_BY_LAYER_A"
        result["simulated_dual_support_pass"] = False
        return result

    b_valid = [(r, layer_b_row_valid(r)) for r in s_op]
    n_invalid = sum(not valid for _, valid in b_valid)
    f_b = n_invalid / len(s_op)
    final_rows = [r for r, valid in b_valid if valid]
    b_pass = f_b <= MAX_INVALID and len(final_rows) >= MIN_RETAINED

    result["layer_b_classification"] = PASS_B if b_pass else FAIL_B
    result["layer_b"] = {
        "input_S_op_rows": len(s_op),
        "invalid_common_response_rows": n_invalid,
        "article3_coordinate_f_invalid": f_b,
        "retained_rows": len(final_rows),
        "retained_ids": [r["coordinate_id"] for r in final_rows],
        "retained_ids_sha256": ordered_id_digest([r["coordinate_id"] for r in final_rows]),
    }
    result["simulated_dual_support_pass"] = bool(a_pass and b_pass)
    return result


def atom(
    z: float = 0.6,
    k: float = 0.04,
    weight: float = 1.0,
    response: list[float] | None = None,
) -> dict[str, Any]:
    return {
        "z": z,
        "k_Mpc^-1": k,
        "operator_abs_weight": weight,
        "final_response_abs_values": [1.0, 2.0] if response is None else response,
    }


def row(i: int) -> dict[str, Any]:
    block = ("Wm", "WW", "BOSS")[i % 3]
    return {
        "coordinate_id": f"synthetic|{block}|{i:03d}",
        "ordinal": i,
        "observable_block": block,
        "support_atoms": [atom(k=0.03, weight=0.4), atom(k=0.05, weight=0.6)],
    }


def base_manifest(n: int = 20) -> dict[str, Any]:
    return {
        "exp073u_order_sha256": EXP073U_ORDER_SHA256,
        "anti_leakage": copy.deepcopy(EXPECTED_ANTI_LEAKAGE),
        "rows": [row(i) for i in range(n)],
    }


def demand(name: str, condition: bool, details: Any, records: list[dict[str, Any]]) -> None:
    records.append({"name": name, "pass": bool(condition), "details": details})
    if not condition:
        raise AssertionError(f"{name}: {details}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    tests: list[dict[str, Any]] = []

    baseline = classify(base_manifest())
    demand(
        "baseline_dual_pass",
        baseline["layer_a_classification"] == PASS_A
        and baseline["layer_b_classification"] == PASS_B
        and baseline["simulated_dual_support_pass"],
        baseline,
        tests,
    )

    permuted = base_manifest()
    random.Random(73073).shuffle(permuted["rows"])
    rp = classify(permuted)
    demand(
        "row_permutation_invariance_by_inherited_ordinal",
        rp["simulated_dual_support_pass"]
        and rp["layer_a"]["retained_ids_sha256"] == baseline["layer_a"]["retained_ids_sha256"]
        and rp["layer_b"]["retained_ids_sha256"] == baseline["layer_b"]["retained_ids_sha256"],
        rp,
        tests,
    )

    scalar_proxy = base_manifest()
    scalar_proxy["rows"][0]["k_Mpc^-1"] = 0.04
    rsp = classify(scalar_proxy)
    demand(
        "row_level_scalar_k_proxy_is_invalid_for_science",
        rsp["schema_classification"] == INVALID_SCHEMA,
        rsp,
        tests,
    )

    scalar_z = base_manifest()
    scalar_z["rows"][0]["effective_z"] = 0.6
    rsz = classify(scalar_z)
    demand(
        "row_level_effective_z_proxy_is_invalid_for_science",
        rsz["schema_classification"] == INVALID_SCHEMA,
        rsz,
        tests,
    )

    counterexample = base_manifest()
    counterexample["rows"][0]["support_atoms"] = [
        atom(k=0.04, weight=0.90),
        atom(k=0.10, weight=0.10),
    ]
    rc = classify(counterexample)
    weighted_mean_k = 0.04 * 0.90 + 0.10 * 0.10
    c0 = rc["layer_a"]["rows"][0]
    demand(
        "effective_k_can_pass_while_broad_operator_row_fails",
        weighted_mean_k <= K_MAX
        and c0["operator_f_invalid"] > MAX_INVALID
        and c0["retained"] is False
        and rc["layer_a"]["retained_rows"] == 19,
        {"weighted_mean_k": weighted_mean_k, "layer_a_row": c0},
        tests,
    )

    exact_a = base_manifest()
    exact_a["rows"][0]["support_atoms"] = [
        atom(k=0.04, weight=19.0),
        atom(k=0.10, weight=1.0),
    ]
    rea = classify(exact_a)
    ea0 = rea["layer_a"]["rows"][0]
    demand(
        "layer_a_exact_0p05_boundary_passes",
        math.isclose(ea0["operator_f_invalid"], 0.05, rel_tol=0.0, abs_tol=0.0)
        and ea0["retained"] is True,
        ea0,
        tests,
    )

    over_a = base_manifest()
    over_a["rows"][0]["support_atoms"] = [
        atom(k=0.04, weight=949.0),
        atom(k=0.10, weight=51.0),
    ]
    roa = classify(over_a)
    oa0 = roa["layer_a"]["rows"][0]
    demand(
        "layer_a_above_0p05_rejects_row",
        oa0["operator_f_invalid"] > MAX_INVALID and oa0["retained"] is False,
        oa0,
        tests,
    )

    boundary = base_manifest()
    boundary["rows"][0]["support_atoms"] = [
        atom(z=Z_MIN, k=K_MAX, weight=0.5),
        atom(z=Z_MAX, k=0.02, weight=0.5),
    ]
    rb = classify(boundary)
    demand(
        "exact_atom_domain_boundaries_are_inclusive",
        rb["layer_a"]["rows"][0]["operator_f_invalid"] == 0.0
        and rb["layer_a"]["rows"][0]["retained"],
        rb["layer_a"]["rows"][0],
        tests,
    )

    layer_b_independent = base_manifest()
    layer_b_independent["rows"][0]["support_atoms"][0]["final_response_abs_values"] = [1.0, 0.0]
    rbi = classify(layer_b_independent)
    demand(
        "layer_a_pass_does_not_imply_layer_b_common_response_pass",
        rbi["layer_a_classification"] == PASS_A
        and rbi["layer_a"]["retained_rows"] == 20
        and rbi["layer_b"]["invalid_common_response_rows"] == 1,
        rbi,
        tests,
    )

    exact_b = base_manifest(20)
    exact_b["rows"][0]["support_atoms"][0]["final_response_abs_values"] = [0.0, 1.0]
    reb = classify(exact_b)
    demand(
        "layer_b_exact_0p05_row_fraction_passes",
        reb["layer_b_classification"] == PASS_B
        and reb["layer_b"]["article3_coordinate_f_invalid"] == 0.05
        and reb["layer_b"]["retained_rows"] == 19,
        reb,
        tests,
    )

    over_b = base_manifest(19)
    over_b["rows"][0]["support_atoms"][0]["final_response_abs_values"] = [0.0, 1.0]
    rob = classify(over_b)
    demand(
        "layer_b_above_0p05_row_fraction_scientific_fail",
        rob["layer_a_classification"] == PASS_A
        and rob["layer_b_classification"] == FAIL_B
        and rob["layer_b"]["article3_coordinate_f_invalid"] > MAX_INVALID,
        rob,
        tests,
    )

    r15 = classify(base_manifest(15))
    demand(
        "minimum_15_observation_rows_passes",
        r15["simulated_dual_support_pass"],
        r15,
        tests,
    )

    r14 = classify(base_manifest(14))
    demand(
        "fourteen_layer_a_rows_is_scientific_fail_and_blocks_layer_b",
        r14["layer_a_classification"] == FAIL_A
        and r14["layer_b_classification"] == "NOT_AUTHORIZED_BY_LAYER_A",
        r14,
        tests,
    )

    scaled = base_manifest()
    for rr in scaled["rows"]:
        for aa in rr["support_atoms"]:
            aa["final_response_abs_values"] = [x * 1.0e20 for x in aa["final_response_abs_values"]]
    rs = classify(scaled)
    demand(
        "positive_response_amplitude_scale_invariance",
        rs["simulated_dual_support_pass"]
        and rs["layer_b"]["retained_ids_sha256"] == baseline["layer_b"]["retained_ids_sha256"],
        rs,
        tests,
    )

    zero_weight = base_manifest()
    zero_weight["rows"][0]["support_atoms"] = [atom(weight=0.0), atom(weight=0.0)]
    rzw = classify(zero_weight)
    demand(
        "nonpositive_operator_normalization_is_invalid_for_science",
        rzw["schema_classification"] == INVALID_SCHEMA,
        rzw,
        tests,
    )

    dup_id = base_manifest()
    dup_id["rows"][1]["coordinate_id"] = dup_id["rows"][0]["coordinate_id"]
    rdi = classify(dup_id)
    demand("duplicate_observation_id_is_invalid", rdi["schema_classification"] == INVALID_SCHEMA, rdi, tests)

    dup_ord = base_manifest()
    dup_ord["rows"][1]["ordinal"] = dup_ord["rows"][0]["ordinal"]
    rdo = classify(dup_ord)
    demand("duplicate_observation_ordinal_is_invalid", rdo["schema_classification"] == INVALID_SCHEMA, rdo, tests)

    leak = base_manifest()
    leak["covariance"] = [[1.0]]
    rl = classify(leak)
    demand("downstream_covariance_payload_is_invalid", rl["schema_classification"] == INVALID_SCHEMA, rl, tests)

    wrong_parent = base_manifest()
    wrong_parent["exp073u_order_sha256"] = "0" * 64
    rwp = classify(wrong_parent)
    demand("exp073u_order_authority_mismatch_is_invalid", rwp["schema_classification"] == INVALID_SCHEMA, rwp, tests)

    result = {
        "experiment": "Exp073V",
        "status": "PASS_EXP073V_ARTICLE3_BROAD_ROW_SUPPORT_SCHEMA_SYNTHETIC_V0_1",
        "scope": "SYNTHETIC_ARCHITECTURE_QA_ONLY_NO_REAL_SURVEY_SUPPORT_SCORE",
        "frozen_exp073u_order_sha256": EXP073U_ORDER_SHA256,
        "constants": {
            "z_min": Z_MIN,
            "z_max": Z_MAX,
            "k_max_Mpc^-1": K_MAX,
            "max_invalid_fraction_layer_a": MAX_INVALID,
            "max_invalid_fraction_layer_b": MAX_INVALID,
            "min_retained_observation_rows": MIN_RETAINED,
        },
        "representation": {
            "observation_row_has_scalar_z": False,
            "observation_row_has_scalar_k": False,
            "physical_domain_is_evaluated_on_support_atoms": True,
            "layer_a_is_weighted_broad_operator_leakage": True,
            "layer_b_is_row_level_common_response_validity_over_active_in_domain_atoms": True,
        },
        "tests": tests,
        "science_gate_scored": False,
        "scientific_readiness_credit": False,
        "real_covariance_authorized": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_required_block": "real content-hashed Wm/WW NaMaster-window x redshift-kernel atoms plus BOSS C=W@M true-k x survey-redshift support",
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    print(result["status"])


if __name__ == "__main__":
    main()
