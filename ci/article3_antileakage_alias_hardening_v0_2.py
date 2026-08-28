#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from typing import Any

PASS = "PASS_ARTICLE3_ANTILEAKAGE_ALIAS_HARDENING_V0_2"
INVALID = "INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT"

# This is execution hardening of the already-frozen no-downstream-selection rule.
# It does not add, relax, or reinterpret any scientific acceptance criterion.
FORBIDDEN_CANONICAL_TOKENS = (
    "covariance",
    "inversecovariance",
    "whitening",
    "nuisance",
    "svd",
    "relation",
    "pvalue",
    "chisquared",
    "chi2",
    "g7",
    "g8",
)


def canonical_key(key: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(key).lower())


def forbidden_key_path(obj: Any, path: str = "") -> str | None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            canon = canonical_key(key)
            if any(token in canon for token in FORBIDDEN_CANONICAL_TOKENS):
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


def classify(payload: Any) -> str:
    return INVALID if forbidden_key_path(payload) is not None else "CLEAN"


def main() -> None:
    forbidden_cases = {
        "p_value": {"rows": [{"diagnostics": {"p_value": 0.1}}]},
        "p-value": {"rows": [{"diagnostics": {"p-value": 0.1}}]},
        "P VALUE": {"rows": [{"diagnostics": {"P VALUE": 0.1}}]},
        "chi_squared": {"rows": [{"fit": {"chi_squared": 1.2}}]},
        "chi-squared": {"rows": [{"fit": {"chi-squared": 1.2}}]},
        "inverse_covariance": {"nested": [{"inverse_covariance": [[1.0]]}]},
        "inverse-covariance": {"nested": [{"inverse-covariance": [[1.0]]}]},
        "nuisance_tangent": {"nested": {"nuisance_tangent": [0.2]}},
        "whitening_matrix": {"nested": {"whitening_matrix": [[1.0]]}},
        "relation_score": {"nested": {"relation_score": 0.2}},
        "G7_score": {"nested": {"G7_score": 1}},
        "g8-statistic": {"nested": {"g8-statistic": 1}},
    }
    clean_cases = {
        "physical_support": {"rows": [{"coordinate_id": "c001", "z": 0.5, "k_Mpc^-1": 0.01}]},
        "response_only": {"rows": [{"final_response_abs_values": [1.0, 2.0]}]},
        "geometry": {"mapper": {"nside": 4096, "ordering": "RING"}},
    }

    tests = []
    for name, payload in forbidden_cases.items():
        path = forbidden_key_path(payload)
        ok = path is not None and classify(payload) == INVALID
        tests.append({"name": f"reject_{name}", "pass": ok, "detected_path": path})
    for name, payload in clean_cases.items():
        path = forbidden_key_path(payload)
        ok = path is None and classify(payload) == "CLEAN"
        tests.append({"name": f"allow_{name}", "pass": ok, "detected_path": path})

    if not all(t["pass"] for t in tests):
        raise AssertionError(tests)

    result = {
        "experiment": "Article3AntiLeakageAliasHardening_v0_2",
        "status": PASS,
        "scope": "SYNTHETIC_ONLY_EXECUTION_HARDENING",
        "scientific_acceptance_criteria_changed": False,
        "real_science_gate_scored": False,
        "covariance_restriction_authorized": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "canonicalization": "lowercase then remove all non [a-z0-9] characters before forbidden-token matching",
        "tests": tests,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
