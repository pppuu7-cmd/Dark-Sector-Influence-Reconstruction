#!/usr/bin/env python3
"""Independent fail-closed JSON ambiguity guard for prospective Exp073P v0.3 evidence.

This is a validation/reproducibility control only. It does not alter the frozen
Exp073P v0.3 prerequisite-join evaluator, its acceptance criteria, or authorize
physical-support execution. It exists so future real JSON receipts can be checked
for parser-level ambiguity before any downstream scientific use.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

PASS = "PASS_EXP073P_V03_STRICT_JSON_EVIDENCE_AMBIGUITY_GUARD_V0_1"
REJECTED = "REJECTED_EXP073P_V03_STRICT_JSON_EVIDENCE_AMBIGUITY_GUARD_V0_1"


class AmbiguousJSON(ValueError):
    pass


def _pairs_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise AmbiguousJSON(f"duplicate object key: {key!r}")
        out[key] = value
    return out


def _reject_constant(token: str) -> Any:
    raise AmbiguousJSON(f"non-standard/non-finite JSON constant: {token}")


def _walk_finite(value: Any, where: str = "$") -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise AmbiguousJSON(f"non-finite float at {where}")
    if isinstance(value, dict):
        for key, child in value.items():
            if not isinstance(key, str):
                raise AmbiguousJSON(f"non-string key at {where}")
            _walk_finite(child, f"{where}.{key}")
    elif isinstance(value, list):
        for i, child in enumerate(value):
            _walk_finite(child, f"{where}[{i}]")


def strict_load_bytes(raw: bytes, *, require_object: bool = True) -> Any:
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise AmbiguousJSON(f"non-UTF-8 evidence: {exc}") from exc
    try:
        data = json.loads(
            text,
            object_pairs_hook=_pairs_no_duplicates,
            parse_constant=_reject_constant,
        )
    except (json.JSONDecodeError, AmbiguousJSON) as exc:
        raise AmbiguousJSON(str(exc)) from exc
    if require_object and not isinstance(data, dict):
        raise AmbiguousJSON("top-level evidence must be a JSON object")
    _walk_finite(data)
    return data


def verify_file(path: Path) -> None:
    strict_load_bytes(path.read_bytes(), require_object=True)
    print(PASS, str(path))
    print("support_executor_authorized=false")
    print("gate_state=G7:OPEN,G8:OPEN,G9:OPEN")


def selftest() -> None:
    canonical = b'{"status":"PASS_SYNTHETIC_ONLY","nested":{"x":1},"values":[0,1.25,null,false]}'
    parsed = strict_load_bytes(canonical)
    assert parsed["nested"]["x"] == 1

    rejected = {
        "duplicate-top": b'{"status":"A","status":"B"}',
        "duplicate-nested": b'{"x":{"a":1,"a":2}}',
        "nan": b'{"x":NaN}',
        "positive-infinity": b'{"x":Infinity}',
        "negative-infinity": b'{"x":-Infinity}',
        "invalid-utf8": b'{"x":"\xff"}',
        "trailing-json": b'{"x":1}{"y":2}',
        "top-level-array": b'[{"x":1}]',
    }
    for name, raw in rejected.items():
        try:
            strict_load_bytes(raw)
        except AmbiguousJSON:
            continue
        raise AssertionError(f"ambiguity mutation unexpectedly accepted: {name}")

    # Demonstrate why the duplicate/non-finite controls are material: CPython's
    # default decoder accepts these inputs with semantics unsuitable for authority
    # evidence. This assertion documents behavior; it does not modify frozen code.
    assert json.loads('{"a":1,"a":2}')["a"] == 2
    assert math.isnan(json.loads('{"x":NaN}')["x"])

    print(PASS, f"synthetic_cases={len(rejected)}")
    print("frozen_acceptance_criteria_changed=false")
    print("scientific_classification=None")
    print("support_executor_authorized=false")
    print("gate_state=G7:OPEN,G8:OPEN,G9:OPEN")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if not args.selftest and not args.files:
        ap.error("provide --selftest and/or one or more JSON evidence files")
    if args.selftest:
        selftest()
    for path in args.files:
        verify_file(path)


if __name__ == "__main__":
    main()
