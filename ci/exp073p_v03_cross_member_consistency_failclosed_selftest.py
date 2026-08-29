#!/usr/bin/env python3
"""Supplemental fail-closed cross-member consistency validation for Exp073P v0.3.

Implementation/reproducibility validation only. It does not authorize or evaluate
physical support, f_invalid, covariance, whitening, nuisance SVD, relation/null,
or G8 quantities, and it changes no frozen scientific acceptance criterion.
"""
from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from typing import Any

METACAL_BYTES = 84075649920
METACAL_SHA256 = "39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8"
SOURCE_SHA256 = "491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5"
SOURCE_INDEX_SHA256 = "dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628"
R1_STATUS = "PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1"
ROWS = 136930995


@dataclass(frozen=True)
class Decision:
    admitted: bool
    reason: str
    support_executor_authorized: bool = False
    support_fraction_evaluated: bool = False
    f_invalid_computed: bool = False
    covariance_read: bool = False
    whitening_read: bool = False
    nuisance_svd_read: bool = False
    relation_null_read: bool = False
    G8_read: bool = False


def baseline() -> dict[str, Any]:
    return {
        "summary": {
            "status": R1_STATUS,
            "observed_bytes_metacal": METACAL_BYTES,
            "expected_bytes_metacal": METACAL_BYTES,
            "metacal_sha256": METACAL_SHA256,
            "expected_metacal_sha256": METACAL_SHA256,
            "rows_read_source_index": ROWS,
            "rows_read_metacal": ROWS,
            "source_identity_binding": {
                "source_whole_sha256": SOURCE_SHA256,
                "source_index_sha256": SOURCE_INDEX_SHA256,
            },
            "science_gate_scored": False,
            "f_invalid_computed": False,
            "covariance_read": False,
            "G8_read": False,
        },
        "acquisition": {
            "authorized_for_replay": True,
            "http_range_requests": 0,
            "whole_object_attempts_from_zero": True,
            "final_bytes": METACAL_BYTES,
            "final_sha256": METACAL_SHA256,
        },
        "runtime": {
            "python_abi": "cp314",
            "numpy": "2.5.2",
            "healpy": "1.20.0",
            "captured": True,
        },
    }


def inspect(x: dict[str, Any]) -> Decision:
    s = x.get("summary")
    a = x.get("acquisition")
    r = x.get("runtime")
    if not isinstance(s, dict) or not isinstance(a, dict) or not isinstance(r, dict):
        return Decision(False, "missing_member_payload")

    if s.get("status") != R1_STATUS:
        return Decision(False, "summary_not_genuine_r1_pass")
    if a.get("authorized_for_replay") is not True:
        return Decision(False, "acquisition_not_authorized")
    if a.get("http_range_requests") != 0 or a.get("whole_object_attempts_from_zero") is not True:
        return Decision(False, "acquisition_transport_contract_mismatch")

    # Cross-member byte identity: the mapper summary and acquisition receipt must
    # identify exactly the same complete frozen metacal object.
    byte_values = (s.get("observed_bytes_metacal"), s.get("expected_bytes_metacal"), a.get("final_bytes"))
    if byte_values != (METACAL_BYTES, METACAL_BYTES, METACAL_BYTES):
        return Decision(False, "metacal_byte_count_cross_member_mismatch")
    sha_values = (s.get("metacal_sha256"), s.get("expected_metacal_sha256"), a.get("final_sha256"))
    if sha_values != (METACAL_SHA256, METACAL_SHA256, METACAL_SHA256):
        return Decision(False, "metacal_sha256_cross_member_mismatch")

    # Frozen parent identity and exact one-pass row accounting remain summary facts.
    sib = s.get("source_identity_binding")
    if not isinstance(sib, dict):
        return Decision(False, "source_identity_binding_missing")
    if sib.get("source_whole_sha256") != SOURCE_SHA256 or sib.get("source_index_sha256") != SOURCE_INDEX_SHA256:
        return Decision(False, "source_identity_binding_mismatch")
    if s.get("rows_read_source_index") != ROWS or s.get("rows_read_metacal") != ROWS:
        return Decision(False, "row_accounting_mismatch")

    # Runtime provenance must be present and nonempty, but this supplemental guard
    # does not post-hoc redefine the frozen v0.7 runtime contract.
    if r.get("captured") is not True:
        return Decision(False, "runtime_provenance_not_captured")
    for key in ("python_abi", "numpy", "healpy"):
        if not isinstance(r.get(key), str) or not r[key].strip():
            return Decision(False, f"runtime_field_missing:{key}")

    # Explicit downstream firewall: admission here is only evidence consistency.
    if s.get("science_gate_scored") is not False or s.get("f_invalid_computed") is not False:
        return Decision(False, "premature_science_quantity")
    if s.get("covariance_read") is not False or s.get("G8_read") is not False:
        return Decision(False, "premature_downstream_read")
    return Decision(True, "cross_member_identity_consistent")


def reject(mutator, reason_prefix: str) -> None:
    x = baseline()
    mutator(x)
    d = inspect(x)
    assert not d.admitted, d
    assert d.reason.startswith(reason_prefix), (d.reason, reason_prefix)
    assert not any((d.support_executor_authorized, d.support_fraction_evaluated, d.f_invalid_computed,
                    d.covariance_read, d.whitening_read, d.nuisance_svd_read,
                    d.relation_null_read, d.G8_read)), d


def main() -> None:
    good = inspect(baseline())
    assert good.admitted and good.reason == "cross_member_identity_consistent"
    assert good.support_executor_authorized is False

    mutations = [
        (lambda x: x["summary"].__setitem__("observed_bytes_metacal", METACAL_BYTES - 1), "metacal_byte_count"),
        (lambda x: x["summary"].__setitem__("expected_bytes_metacal", METACAL_BYTES - 1), "metacal_byte_count"),
        (lambda x: x["acquisition"].__setitem__("final_bytes", METACAL_BYTES - 1), "metacal_byte_count"),
        (lambda x: x["summary"].__setitem__("metacal_sha256", "0" * 64), "metacal_sha256"),
        (lambda x: x["summary"].__setitem__("expected_metacal_sha256", "0" * 64), "metacal_sha256"),
        (lambda x: x["acquisition"].__setitem__("final_sha256", "0" * 64), "metacal_sha256"),
        (lambda x: x["summary"]["source_identity_binding"].__setitem__("source_whole_sha256", "0" * 64), "source_identity"),
        (lambda x: x["summary"]["source_identity_binding"].__setitem__("source_index_sha256", "0" * 64), "source_identity"),
        (lambda x: x["summary"].__setitem__("rows_read_metacal", ROWS - 1), "row_accounting"),
        (lambda x: x["summary"].__setitem__("rows_read_source_index", ROWS - 1), "row_accounting"),
        (lambda x: x["acquisition"].__setitem__("authorized_for_replay", False), "acquisition_not_authorized"),
        (lambda x: x["acquisition"].__setitem__("http_range_requests", 1), "acquisition_transport_contract"),
        (lambda x: x["acquisition"].__setitem__("whole_object_attempts_from_zero", False), "acquisition_transport_contract"),
        (lambda x: x["runtime"].__setitem__("captured", False), "runtime_provenance"),
        (lambda x: x["runtime"].__setitem__("numpy", ""), "runtime_field_missing"),
        (lambda x: x["summary"].__setitem__("status", "FAIL"), "summary_not_genuine_r1_pass"),
        (lambda x: x["summary"].__setitem__("f_invalid_computed", True), "premature_science_quantity"),
        (lambda x: x["summary"].__setitem__("covariance_read", True), "premature_downstream_read"),
        (lambda x: x["summary"].__setitem__("G8_read", True), "premature_downstream_read"),
    ]
    for mutator, reason in mutations:
        reject(mutator, reason)

    print(json.dumps({
        "status": "PASS_EXP073P_V03_CROSS_MEMBER_CONSISTENCY_FAILCLOSED_SELFTEST",
        "mutations_rejected": len(mutations),
        "scope": "supplemental implementation/reproducibility validation only",
        "support_executor_authorized": False,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "covariance_read": False,
        "whitening_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "G8_read": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }, sort_keys=True))


if __name__ == "__main__":
    main()
