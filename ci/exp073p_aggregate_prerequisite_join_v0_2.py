#!/usr/bin/env python3
"""Superseding fail-closed Exp073P prerequisite join for replacement R1.

Version 0.2 reuses the byte-frozen v0.1 semantic validators and changes only
the exact R1 Actions authority.  The v0.1 module is loaded under a private
module name so importing this adapter cannot mutate the historical evaluator.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def _load_v01():
    path = Path(__file__).with_name("exp073p_aggregate_prerequisite_join_v0_1.py")
    spec = importlib.util.spec_from_file_location("_dsir_exp073p_join_v01_for_v02", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load byte-frozen aggregate join v0.1")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


_base = _load_v01()

PASS = "PASS_EXP073P_PREREQUISITE_BINDING_V0_2"
REJECTED = "REJECTED_EXP073P_PREREQUISITE_BINDING_V0_2"
INCOMPLETE = "INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_2"
SYNTHETIC_PASS = "PASS_EXP073P_AGGREGATE_JOIN_SYNTHETIC_SELFTEST_V0_2"

REPOSITORY = _base.REPOSITORY
EXPECTED_GATE_STATE = _base.EXPECTED_GATE_STATE
FROZEN_SUPPORT = copy.deepcopy(_base.FROZEN_SUPPORT)
R1_ARTIFACT_NAME = (
    "exp073r1-v06-selfhosted-longrun-"
    "98c4b8783a95932949947d9e214706c4ec7eaf8c"
)

EXPECTED_RUNS = copy.deepcopy(_base.EXPECTED_RUNS)
EXPECTED_RUNS["r1"] = {
    "id": 33222848695,
    "head": "98c4b8783a95932949947d9e214706c4ec7eaf8c",
    "path": ".github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml",
    "name": "Exp073R1 DESY1 self-hosted long-run Stage-B v0.6",
    "jobs": {99020389131: "metacal-map-longrun"},
    "artifacts": [_base.artifact(None, R1_ARTIFACT_NAME, None)],
}

_base.PASS = PASS
_base.REJECTED = REJECTED
_base.INCOMPLETE = INCOMPLETE
_base.SYNTHETIC_PASS = SYNTHETIC_PASS
_base.R1_ARTIFACT_NAME = R1_ARTIFACT_NAME
_base.EXPECTED_RUNS = EXPECTED_RUNS
_base.LOCAL_CONTRACT_SHA256 = copy.deepcopy(_base.LOCAL_CONTRACT_SHA256)
_base.LOCAL_CONTRACT_SHA256.update(
    {
        "ci/exp073p_aggregate_prerequisite_join_v0_1.py":
            "9dc0b5a0ea82b8fb69d82e06b566b08d61c1982bd5e13ecd8db6752253bc0e46",
        "experiments/073p_aggregate_prerequisite_join_superseding_r1_authority_prereg_v0_2.md":
            "601f904200d72ebf5d483c973a92261eebd38b065a909220ccd8c6b86c46ad76",
    }
)

JoinError = _base.JoinError
JoinIncomplete = _base.JoinIncomplete
load_record = _base.load_record
write_json = _base.write_json


def _v02_receipt(out: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(out)
    out["experiment"] = "Exp073P-aggregate-prerequisite-join-v0.2"
    out["supersedes"] = {
        "evaluator": "Exp073P-aggregate-prerequisite-join-v0.1",
        "reason": "v0.1 is permanently bound to infrastructure-incomplete R1 run 33212521957",
    }
    out["r1_authority"] = {
        "run_id": 33222848695,
        "job_id": 99020389131,
        "head_sha": "98c4b8783a95932949947d9e214706c4ec7eaf8c",
        "artifact_name": R1_ARTIFACT_NAME,
    }
    return out


def validate_metadata(meta: dict[str, Any]) -> dict[str, Any]:
    return _base.validate_metadata(meta)


def validate_join(
    metadata: dict[str, Any],
    records: dict[str, tuple[dict[str, Any], str]],
    *,
    synthetic: bool,
) -> dict[str, Any]:
    return _v02_receipt(_base.validate_join(metadata, records, synthetic=synthetic))


def valid_metadata_fixture() -> dict[str, Any]:
    return _base.valid_metadata_fixture()


def valid_record_fixture() -> dict[str, tuple[dict[str, Any], str]]:
    return _base.valid_record_fixture()


def _must_reject_legacy_r1(mutator) -> None:
    metadata = valid_metadata_fixture()
    records = valid_record_fixture()
    mutator(metadata, records)
    try:
        validate_join(metadata, records, synthetic=True)
    except JoinError:
        return
    raise AssertionError("superseded v0.1 R1 authority unexpectedly crossed v0.2")


def selftest() -> dict[str, Any]:
    out = _v02_receipt(_base.selftest())
    assert out["status"] == SYNTHETIC_PASS
    assert out["support_executor_authorized"] is False

    _must_reject_legacy_r1(
        lambda m, r: m["parents"]["r1"]["run"].__setitem__("id", 33212521957)
    )
    _must_reject_legacy_r1(
        lambda m, r: m["parents"]["r1"]["jobs"][0].__setitem__("id", 98988824629)
    )
    _must_reject_legacy_r1(
        lambda m, r: m["parents"]["r1"]["artifacts"][0].__setitem__(
            "name",
            "exp073r1-v06-selfhosted-longrun-79abf2a9694e57e7a2ba1fbb563a0f6413e891f9",
        )
    )
    out["superseded_r1_mutations_rejected"] = 3
    return out


def _error_receipt(status: str, error: str) -> dict[str, Any]:
    return _v02_receipt(_base.base_receipt(status, synthetic=False, error=error))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--classifying", action="store_true")
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--preflight", type=Path)
    parser.add_argument("--large-source", type=Path)
    parser.add_argument("--large-metacal", type=Path)
    parser.add_argument("--p2", type=Path)
    parser.add_argument("--s0", type=Path)
    parser.add_argument("--r1", type=Path)
    parser.add_argument("--boss", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    if args.selftest:
        if args.classifying:
            parser.error("--selftest and --classifying are mutually exclusive")
        write_json(args.out, selftest())
        print(SYNTHETIC_PASS)
        return

    if not args.classifying:
        parser.error("real evidence evaluation requires explicit --classifying")
    required = (
        "metadata", "preflight", "large_source", "large_metacal",
        "p2", "s0", "r1", "boss",
    )
    for name in required:
        if getattr(args, name) is None:
            parser.error(f"--{name.replace('_', '-')} is required with --classifying")

    try:
        metadata, _ = load_record(args.metadata)
        records = {
            "preflight": load_record(args.preflight),
            "large_source": load_record(args.large_source),
            "large_metacal": load_record(args.large_metacal),
            "p2": load_record(args.p2),
            "s0": load_record(args.s0),
            "r1": load_record(args.r1),
            "boss": load_record(args.boss),
        }
        receipt = validate_join(metadata, records, synthetic=False)
    except JoinIncomplete as exc:
        receipt = _error_receipt(INCOMPLETE, str(exc))
        write_json(args.out, receipt)
        print(INCOMPLETE)
        raise SystemExit(3) from exc
    except JoinError as exc:
        receipt = _error_receipt(REJECTED, str(exc))
        write_json(args.out, receipt)
        print(REJECTED)
        raise SystemExit(2) from exc

    write_json(args.out, receipt)
    print(PASS)


if __name__ == "__main__":
    main()
