#!/usr/bin/env python3
"""Prospective fail-closed schema-closure guard for Exp073P v0.3 evidence.

Validation/reproducibility control only.  This guard does NOT alter any frozen
Exp073P evaluator, preregistration, acceptance criterion, or authorize execution
of the physical-support mask.  It demonstrates that authority-bearing JSON can
be required to use an exact, closed vocabulary instead of permissive extra-key
semantics.
"""
from __future__ import annotations

import copy
import json
from typing import Any

PASS = "PASS_EXP073P_V03_EVIDENCE_SCHEMA_CLOSURE_GUARD_V0_1"


class SchemaReject(ValueError):
    pass


def exact_object(value: Any, required: set[str], where: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SchemaReject(f"{where}: expected object")
    got = set(value)
    if got != required:
        extra = sorted(got - required)
        missing = sorted(required - got)
        raise SchemaReject(f"{where}: schema not closed; extra={extra}, missing={missing}")
    for key in value:
        if key != key.strip() or not key.isascii():
            raise SchemaReject(f"{where}: non-canonical key {key!r}")
    return value


def validate(bundle: Any) -> None:
    root = exact_object(bundle, {"summary", "acquisition", "runtime"}, "$")

    summary = exact_object(
        root["summary"],
        {"authority", "status", "parent", "catalog"},
        "$.summary",
    )
    authority = exact_object(
        summary["authority"],
        {"run_id", "run_attempt", "job_id", "workflow", "head_sha"},
        "$.summary.authority",
    )
    exact_object(summary["catalog"], {"rows", "bytes", "sha256"}, "$.summary.catalog")

    acquisition = exact_object(
        root["acquisition"],
        {"source", "bytes", "sha256", "http_status", "range_used", "from_zero"},
        "$.acquisition",
    )
    runtime = exact_object(
        root["runtime"],
        {"python", "numpy", "healpy", "platform"},
        "$.runtime",
    )

    if type(authority["run_id"]) is not int or type(authority["run_attempt"]) is not int or type(authority["job_id"]) is not int:
        raise SchemaReject("authority integer fields must be exact JSON integers")
    if summary["status"] != "PASS_SYNTHETIC_ONLY":
        raise SchemaReject("synthetic guard refuses non-synthetic status")
    if type(summary["catalog"]["rows"]) is not int or type(summary["catalog"]["bytes"]) is not int:
        raise SchemaReject("catalog counts must be exact JSON integers")
    if type(acquisition["bytes"]) is not int or type(acquisition["http_status"]) is not int:
        raise SchemaReject("acquisition counts/status must be exact JSON integers")
    if type(acquisition["range_used"]) is not bool or type(acquisition["from_zero"]) is not bool:
        raise SchemaReject("acquisition flags must be exact JSON booleans")


def baseline() -> dict[str, Any]:
    return {
        "summary": {
            "authority": {
                "run_id": 33240490287,
                "run_attempt": 2,
                "job_id": 99080934021,
                "workflow": ".github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml",
                "head_sha": "SYNTHETIC_NOT_AUTHORITY",
            },
            "status": "PASS_SYNTHETIC_ONLY",
            "parent": "exp073_r1_v0_5_frozen",
            "catalog": {
                "rows": 136930995,
                "bytes": 84075649920,
                "sha256": "39a7fe03c120a7d2ea3146fb9ffb574f304e509e5665e084c935a3569501ebc8",
            },
        },
        "acquisition": {
            "source": "SYNTHETIC_OFFICIAL_SOURCE_IDENTITY",
            "bytes": 84075649920,
            "sha256": "39a7fe03c120a7d2ea3146fb9ffb574f304e509e5665e084c935a3569501ebc8",
            "http_status": 200,
            "range_used": False,
            "from_zero": True,
        },
        "runtime": {
            "python": "SYNTHETIC",
            "numpy": "SYNTHETIC",
            "healpy": "SYNTHETIC",
            "platform": "SYNTHETIC",
        },
    }


def must_reject(name: str, mutator) -> None:
    x = copy.deepcopy(baseline())
    mutator(x)
    try:
        validate(x)
    except SchemaReject:
        return
    raise AssertionError(f"schema mutation unexpectedly accepted: {name}")


def selftest() -> None:
    validate(baseline())
    cases = [
        ("unknown-root", lambda x: x.__setitem__("evidence", {})),
        ("unknown-summary", lambda x: x["summary"].__setitem__("note", "x")),
        ("unknown-authority", lambda x: x["summary"]["authority"].__setitem__("artifact_id", 1)),
        ("unknown-catalog", lambda x: x["summary"]["catalog"].__setitem__("selected", True)),
        ("unknown-acquisition", lambda x: x["acquisition"].__setitem__("resume", False)),
        ("unknown-runtime", lambda x: x["runtime"].__setitem__("abi", "x")),
        ("alias-runAttempt", lambda x: (x["summary"]["authority"].__setitem__("runAttempt", x["summary"]["authority"].pop("run_attempt")))),
        ("case-Status", lambda x: (x["summary"].__setitem__("Status", x["summary"].pop("status")))),
        ("padded-status", lambda x: (x["summary"].__setitem__("status ", x["summary"].pop("status")))),
        ("unicode-confusable", lambda x: x["summary"].__setitem__("stаtus", x["summary"].pop("status"))),  # Cyrillic a
        ("wrong-nesting-job", lambda x: x["summary"].__setitem__("job_id", x["summary"]["authority"].pop("job_id"))),
        ("root-list", lambda x: None),
        ("authority-list", lambda x: x["summary"].__setitem__("authority", [])),
        ("catalog-scalar", lambda x: x["summary"].__setitem__("catalog", "x")),
        ("bool-as-run-id", lambda x: x["summary"]["authority"].__setitem__("run_id", True)),
        ("float-as-bytes", lambda x: x["summary"]["catalog"].__setitem__("bytes", 84075649920.0)),
        ("int-as-range-flag", lambda x: x["acquisition"].__setitem__("range_used", 0)),
    ]

    for name, fn in cases:
        if name == "root-list":
            try:
                validate([baseline()])
            except SchemaReject:
                continue
            raise AssertionError("schema mutation unexpectedly accepted: root-list")
        must_reject(name, fn)

    print(PASS, f"synthetic_negative_cases={len(cases)}")
    print("guard_scope=prospective_schema_closure_only")
    print("frozen_acceptance_criteria_changed=false")
    print("scientific_classification=None")
    print("support_executor_authorized=false")
    print("gate_state=G7:OPEN,G8:OPEN,G9:OPEN")


if __name__ == "__main__":
    selftest()
