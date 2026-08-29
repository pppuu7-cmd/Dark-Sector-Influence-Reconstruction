#!/usr/bin/env python3
"""Fail-closed Exp073P prerequisite join for the frozen v0.7 R1 authority.

Version 0.3 privately reuses the byte-frozen v0.1 aggregate and R1 semantic
validators.  It adds only attempt-specific Actions identity, v0.7 acquisition
provenance and complete-payload byte interlocks.  It does not evaluate physical
support or read covariance, nuisance, relation/null or held-out information.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]


def _load_v01():
    path = Path(__file__).with_name("exp073p_aggregate_prerequisite_join_v0_1.py")
    spec = importlib.util.spec_from_file_location("_dsir_exp073p_join_v01_for_v03", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load byte-frozen aggregate join v0.1")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


_base = _load_v01()

PASS = "PASS_EXP073P_PREREQUISITE_BINDING_V0_3"
REJECTED = "REJECTED_EXP073P_PREREQUISITE_BINDING_V0_3"
INCOMPLETE = "INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_3"
SYNTHETIC_PASS = "PASS_EXP073P_AGGREGATE_JOIN_SYNTHETIC_SELFTEST_V0_3"

REPOSITORY = _base.REPOSITORY
EXPECTED_GATE_STATE = copy.deepcopy(_base.EXPECTED_GATE_STATE)
FROZEN_SUPPORT = copy.deepcopy(_base.FROZEN_SUPPORT)
EXPECTED_RUN_ATTEMPT = 2
EXPECTED_R1_RUN_ID = 33_240_490_287
EXPECTED_R1_JOB_ID = 99_080_934_021
EXPECTED_R1_HEAD = "9a4606fb37d5aaa071aa57322ebb7c05eca905d7"
EXPECTED_R1_HEAD_BRANCH = "main"
EXPECTED_R1_EVENT = "push"
EXPECTED_R1_WORKFLOW_ID = 345_172_058
EXPECTED_METACAL_URL = (
    "https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/"
    "shear_catalogs/mcal-y1a1-combined-riz-unblind-v4-matched.fits"
)
EXPECTED_METACAL_BYTES = 84_075_649_920
EXPECTED_METACAL_SHA256 = (
    "39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8"
)
R1_ARTIFACT_NAME = f"exp073r1-v07-transport-stabilized-{EXPECTED_R1_HEAD}"
PAYLOAD_SCHEMA = "dsir.exp073p.v07-r1-complete-payload.v0.3"
PAYLOAD_PASS = "PASS_EXP073P_V07_R1_COMPLETE_PAYLOAD_V0_3"

EXPECTED_RUNS = copy.deepcopy(_base.EXPECTED_RUNS)
EXPECTED_RUNS["r1"] = {
    "id": EXPECTED_R1_RUN_ID,
    "head": EXPECTED_R1_HEAD,
    "path": ".github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml",
    "name": "Exp073R1 DESY1 transport-stabilized exact-byte replay v0.7",
    "jobs": {EXPECTED_R1_JOB_ID: "transport-stabilized-replay"},
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
        "ci/exp073p_actions_metadata_bundle_v0_1.py":
            "cda5cb20c2d4f9be8a3068dacfead4db25e5dfbd867815005b754ab8cde955f3",
        "ci/exp073r1_v0_7_whole_object_acquire.py":
            "18ca2ed0dbf0ae9ab534ffff9f10bc9bb4b3e388e6ee6a03daa353fa1692c15b",
        ".github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml":
            "8ef3fb2305fe2789e6198547f5095969cfc107df1f0e17853b20a7aa5c601328",
        "experiments/073p_aggregate_prerequisite_join_v07_r1_authority_prereg_v0_3.md":
            "e27761b2db4a81283bb9fbac1decb95f62fadb785c40cb3e3f676f8651711f40",
    }
)

JoinError = _base.JoinError
JoinIncomplete = _base.JoinIncomplete
load_record = _base.load_record
write_json = _base.write_json
need = _base.need
available = _base.available
sha256_bytes = _base.sha256_bytes


def _is_sha256(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def validate_metadata(meta: dict[str, Any]) -> dict[str, Any]:
    bound = _base.validate_metadata(meta)
    run = meta.get("parents", {}).get("r1", {}).get("run", {})
    need(run.get("run_attempt") == EXPECTED_RUN_ATTEMPT, "r1: run attempt drift")
    need(run.get("head_branch") == EXPECTED_R1_HEAD_BRANCH, "r1: head branch drift")
    need(run.get("event") == EXPECTED_R1_EVENT, "r1: event drift")
    need(run.get("workflow_id") == EXPECTED_R1_WORKFLOW_ID, "r1: workflow id drift")
    jobs = meta.get("parents", {}).get("r1", {}).get("jobs", [])
    need(isinstance(jobs, list), "r1: jobs missing")
    need({job.get("id") for job in jobs if isinstance(job, dict)} == {EXPECTED_R1_JOB_ID}, "r1: exact job set drift")
    need(jobs[0].get("run_attempt") == EXPECTED_RUN_ATTEMPT, "r1: job run attempt drift")
    bound["r1"].update(
        {
            "run_attempt": EXPECTED_RUN_ATTEMPT,
            "head_branch": EXPECTED_R1_HEAD_BRANCH,
            "event": EXPECTED_R1_EVENT,
            "workflow_id": EXPECTED_R1_WORKFLOW_ID,
        }
    )
    return bound


def validate_acquisition(
    acquisition: dict[str, Any],
    r1_summary: dict[str, Any],
) -> dict[str, Any]:
    need(acquisition.get("experiment") == "Exp073R1", "acquisition experiment drift")
    need(
        acquisition.get("route") == "v0.7_transport_stabilized_exact_byte_replay",
        "acquisition route drift",
    )
    need(acquisition.get("authoritative_url") == EXPECTED_METACAL_URL, "acquisition URL drift")
    need(acquisition.get("expected_bytes") == EXPECTED_METACAL_BYTES, "acquisition expected bytes drift")
    need(acquisition.get("expected_sha256") == EXPECTED_METACAL_SHA256, "acquisition expected SHA256 drift")
    need(acquisition.get("http_range_requests") == 0, "acquisition used Range requests")
    need(acquisition.get("whole_object_attempts_from_zero") is True, "acquisition did not restart from zero")

    attempts = acquisition.get("attempts")
    need(isinstance(attempts, list) and attempts, "acquisition attempts missing")
    for index, attempt in enumerate(attempts, start=1):
        need(isinstance(attempt, dict), f"acquisition attempt {index} is not an object")
        need(attempt.get("attempt") == index, f"acquisition attempt sequence drift at {index}")
        need(attempt.get("started_from_byte") == 0, f"acquisition attempt {index} did not start at zero")
        need(attempt.get("range_header_sent") is False, f"acquisition attempt {index} sent Range")
        need(attempt.get("content_range") is None, f"acquisition attempt {index} received Content-Range")
        observed = attempt.get("observed_bytes")
        need(
            isinstance(observed, int) and not isinstance(observed, bool) and observed >= 0,
            f"acquisition attempt {index} byte count invalid",
        )
        if index < len(attempts):
            need(
                attempt.get("outcome") == "INFRASTRUCTURE_TRANSPORT_FAILURE",
                f"acquisition nonterminal attempt {index} classification drift",
            )
            need(observed < EXPECTED_METACAL_BYTES, f"acquisition failed attempt {index} was complete")

    last = attempts[-1]
    need(last.get("http_status") == 200, "acquisition terminal HTTP status drift")
    need(last.get("content_length") in (None, EXPECTED_METACAL_BYTES), "acquisition terminal Content-Length drift")
    need(last.get("outcome") == "PASS_EXACT_OBJECT_IDENTITY", "acquisition terminal identity PASS absent")
    need(last.get("observed_bytes") == EXPECTED_METACAL_BYTES, "acquisition terminal bytes drift")
    need(last.get("sha256") == EXPECTED_METACAL_SHA256, "acquisition terminal SHA256 drift")
    need(acquisition.get("authorized_for_replay") is True, "acquisition replay authorization absent")
    need(
        acquisition.get("terminal_status") == "PASS_EXACT_OBJECT_IDENTITY_FOR_REPLAY",
        "acquisition terminal status drift",
    )
    need(acquisition.get("final_bytes") == EXPECTED_METACAL_BYTES, "acquisition final bytes drift")
    need(acquisition.get("final_sha256") == EXPECTED_METACAL_SHA256, "acquisition final SHA256 drift")
    need(
        r1_summary.get("observed_bytes_metacal") == acquisition["final_bytes"],
        "acquisition/R1 byte cross-binding failed",
    )
    need(
        r1_summary.get("metacal_sha256") == acquisition["final_sha256"],
        "acquisition/R1 SHA256 cross-binding failed",
    )
    for key in ("science_gate_scored", "f_invalid_computed", "covariance_read", "G8_read"):
        need(acquisition.get(key) is False, f"acquisition no-leakage flag {key!r} drift")
    need(acquisition.get("gate_state") == EXPECTED_GATE_STATE, "acquisition gate state drift")
    return {
        "route": acquisition["route"],
        "attempt_count": len(attempts),
        "final_bytes": acquisition["final_bytes"],
        "final_sha256": acquisition["final_sha256"],
        "terminal_status": acquisition["terminal_status"],
    }


def _require_file_record(record: Any, basename: str, where: str) -> dict[str, Any]:
    need(isinstance(record, dict), f"payload {where} record missing")
    need(record.get("basename") == basename, f"payload {where} basename drift")
    size = record.get("bytes")
    need(isinstance(size, int) and not isinstance(size, bool) and size > 0, f"payload {where} empty")
    need(_is_sha256(record.get("sha256")), f"payload {where} SHA256 invalid")
    return record


def validate_payload_manifest(
    manifest: dict[str, Any],
    r1_summary: dict[str, Any],
    r1_summary_sha256: str,
    acquisition: dict[str, Any],
    acquisition_sha256: str,
) -> dict[str, Any]:
    need(manifest.get("schema") == PAYLOAD_SCHEMA, "payload manifest schema drift")
    need(manifest.get("experiment") == "Exp073P-v0.3-R1-payload-normalizer", "payload manifest experiment drift")
    need(manifest.get("status") == PAYLOAD_PASS, "payload completeness PASS absent")
    need(manifest.get("complete_payload") is True, "payload not marked complete")
    need(manifest.get("duplicate_basenames_rejected") is True, "payload duplicate firewall absent")
    need(manifest.get("extra_bin_identities_rejected") is True, "payload extra-bin firewall absent")

    files = manifest.get("files")
    need(isinstance(files, dict), "payload file registry missing")
    need(set(files) == {"summary", "acquisition", "runtime", "records", "masks"}, "payload file registry drift")
    summary_file = _require_file_record(
        files["summary"],
        "exp073r1_desy1_transport_stabilized_replay_v0_7_summary.json",
        "summary",
    )
    acquisition_file = _require_file_record(
        files["acquisition"],
        "exp073r1_v0_7_remote_acquisition_provenance.json",
        "acquisition",
    )
    _require_file_record(files["runtime"], "exp073r1_v0_7_runtime_provenance.txt", "runtime")
    need(summary_file["sha256"] == r1_summary_sha256, "payload summary byte SHA256 drift")
    need(acquisition_file["sha256"] == acquisition_sha256, "payload acquisition byte SHA256 drift")

    records = files["records"]
    masks = files["masks"]
    need(isinstance(records, dict) and set(records) == {"0", "1", "2", "3"}, "payload record-bin set drift")
    need(isinstance(masks, dict) and set(masks) == {"0", "1", "2", "3"}, "payload mask-bin set drift")
    summary_records = r1_summary.get("pixel_records")
    summary_masks = r1_summary.get("masks")
    selected = r1_summary.get("selected_rows_per_bin")
    need(isinstance(summary_records, dict) and set(summary_records) == set(records), "R1 pixel-record set drift")
    need(isinstance(summary_masks, dict) and set(summary_masks) == set(masks), "R1 mask set drift")
    need(isinstance(selected, dict) and set(selected) == set(records), "R1 selected-bin set drift")

    for b in ("0", "1", "2", "3"):
        record_basename = f"exp073r1_v05_bin{b}_pixel_indices_le_u32.bin"
        mask_basename = f"exp073r1_v05_source_bin{b}_mask_ring_nside4096_bitpack_little.bin"
        record = _require_file_record(records[b], record_basename, f"record bin {b}")
        mask = _require_file_record(masks[b], mask_basename, f"mask bin {b}")
        sr = summary_records[b]
        sm = summary_masks[b]
        need(isinstance(sr, dict) and isinstance(sm, dict), f"R1 summary payload bin {b} invalid")
        need(Path(str(sr.get("path"))).name == record_basename, f"R1 record path drift for bin {b}")
        need(Path(str(sm.get("path"))).name == mask_basename, f"R1 mask path drift for bin {b}")
        need(record["bytes"] == sr.get("file_bytes") == selected[b] * 4, f"record byte count drift for bin {b}")
        need(record["sha256"] == sr.get("sha256"), f"record SHA256 drift for bin {b}")
        need(mask["bytes"] == sm.get("file_bytes") == 25_165_824, f"mask byte count drift for bin {b}")
        need(mask["sha256"] == sm.get("sha256"), f"mask SHA256 drift for bin {b}")
        need(sm.get("nside") == 4096 and sm.get("ordering") == "RING", f"mask geometry drift for bin {b}")
        need(sm.get("selected_rows") == selected[b], f"mask selected rows drift for bin {b}")
        unique = sm.get("unique_pixels")
        need(isinstance(unique, int) and 0 < unique <= selected[b], f"mask unique-pixel count drift for bin {b}")

    for key in (
        "support_fraction_evaluated", "f_invalid_computed", "retained_dimension_evaluated",
        "covariance_read", "whitening_read", "nuisance_svd_read", "relation_null_read",
        "heldout_read", "G8_read",
    ):
        need(manifest.get(key) is False, f"payload manifest no-leakage flag {key!r} drift")
    need(manifest.get("gate_state") == EXPECTED_GATE_STATE, "payload manifest gate state drift")
    need(acquisition.get("final_sha256") == r1_summary.get("metacal_sha256"), "payload semantic cross-binding drift")
    return {
        "summary_sha256": summary_file["sha256"],
        "acquisition_sha256": acquisition_file["sha256"],
        "runtime_sha256": files["runtime"]["sha256"],
        "record_sha256": {b: records[b]["sha256"] for b in sorted(records)},
        "mask_sha256": {b: masks[b]["sha256"] for b in sorted(masks)},
    }


def _v03_receipt(out: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(out)
    out["experiment"] = "Exp073P-aggregate-prerequisite-join-v0.3"
    out["supersedes"] = {
        "evaluators": [
            "Exp073P-aggregate-prerequisite-join-v0.1",
            "Exp073P-aggregate-prerequisite-join-v0.2",
        ],
        "reason": "v0.1/v0.2 remain permanently bound to failed v0.6 R1 authorities",
    }
    out["r1_authority"] = {
        "run_id": EXPECTED_R1_RUN_ID,
        "run_attempt": EXPECTED_RUN_ATTEMPT,
        "job_id": EXPECTED_R1_JOB_ID,
        "head_sha": EXPECTED_R1_HEAD,
        "head_branch": EXPECTED_R1_HEAD_BRANCH,
        "event": EXPECTED_R1_EVENT,
        "workflow_id": EXPECTED_R1_WORKFLOW_ID,
        "artifact_name": R1_ARTIFACT_NAME,
    }
    return out


def validate_join(
    metadata: dict[str, Any],
    records: dict[str, tuple[dict[str, Any], str]],
    *,
    synthetic: bool,
) -> dict[str, Any]:
    expected = {
        "preflight", "large_source", "large_metacal", "p2", "s0", "r1", "boss",
        "r1_acquisition", "r1_payload_manifest",
    }
    need(set(records) == expected, "v0.3 record set drift")
    bound_metadata = validate_metadata(metadata)
    acquisition = validate_acquisition(records["r1_acquisition"][0], records["r1"][0])
    payload = validate_payload_manifest(
        records["r1_payload_manifest"][0],
        records["r1"][0],
        records["r1"][1],
        records["r1_acquisition"][0],
        records["r1_acquisition"][1],
    )
    base_records = {key: value for key, value in records.items() if key not in {"r1_acquisition", "r1_payload_manifest"}}
    out = _base.validate_join(metadata, base_records, synthetic=synthetic)
    out = _v03_receipt(out)
    out["parent_metadata"] = bound_metadata
    out["record_sha256"]["r1_acquisition"] = records["r1_acquisition"][1]
    out["record_sha256"]["r1_payload_manifest"] = records["r1_payload_manifest"][1]
    out["r1_acquisition"] = acquisition
    out["r1_complete_payload"] = payload
    return out


def valid_metadata_fixture() -> dict[str, Any]:
    metadata = _base.valid_metadata_fixture()
    metadata["parents"]["r1"]["run"].update(
        {
            "run_attempt": EXPECTED_RUN_ATTEMPT,
            "head_branch": EXPECTED_R1_HEAD_BRANCH,
            "event": EXPECTED_R1_EVENT,
            "workflow_id": EXPECTED_R1_WORKFLOW_ID,
        }
    )
    metadata["parents"]["r1"]["jobs"][0]["run_attempt"] = EXPECTED_RUN_ATTEMPT
    return metadata


def valid_acquisition_fixture() -> dict[str, Any]:
    return {
        "experiment": "Exp073R1",
        "route": "v0.7_transport_stabilized_exact_byte_replay",
        "authoritative_url": EXPECTED_METACAL_URL,
        "expected_bytes": EXPECTED_METACAL_BYTES,
        "expected_sha256": EXPECTED_METACAL_SHA256,
        "http_range_requests": 0,
        "whole_object_attempts_from_zero": True,
        "attempts": [
            {
                "attempt": 1,
                "started_from_byte": 0,
                "range_header_sent": False,
                "http_status": 200,
                "content_range": None,
                "content_length": EXPECTED_METACAL_BYTES,
                "observed_bytes": EXPECTED_METACAL_BYTES,
                "sha256": EXPECTED_METACAL_SHA256,
                "outcome": "PASS_EXACT_OBJECT_IDENTITY",
            }
        ],
        "authorized_for_replay": True,
        "final_bytes": EXPECTED_METACAL_BYTES,
        "final_sha256": EXPECTED_METACAL_SHA256,
        "terminal_status": "PASS_EXACT_OBJECT_IDENTITY_FOR_REPLAY",
        "science_gate_scored": False,
        "f_invalid_computed": False,
        "covariance_read": False,
        "G8_read": False,
        "gate_state": copy.deepcopy(EXPECTED_GATE_STATE),
    }


def _json_fixture_record(value: dict[str, Any]) -> tuple[dict[str, Any], str]:
    return value, sha256_bytes(json.dumps(value, sort_keys=True).encode())


def valid_record_fixture() -> dict[str, tuple[dict[str, Any], str]]:
    records = _base.valid_record_fixture()
    r1 = records["r1"][0]
    r1["pixel_records"] = {}
    for b in range(4):
        key = str(b)
        record_sha = hashlib.sha256(f"record-{b}".encode()).hexdigest()
        r1["pixel_records"][key] = {
            "path": f"data/derived/g7/exp073r1_v05_records/exp073r1_v05_bin{b}_pixel_indices_le_u32.bin",
            "selected_rows": 1,
            "file_bytes": 4,
            "sha256": record_sha,
        }
        r1["masks"][key].update(
            {
                "path": f"data/derived/g7/exp073r1_v05_masks/exp073r1_v05_source_bin{b}_mask_ring_nside4096_bitpack_little.bin",
                "nside": 4096,
                "ordering": "RING",
                "selected_rows": 1,
                "unique_pixels": 1,
                "file_bytes": 25_165_824,
            }
        )
    records["r1"] = _json_fixture_record(r1)
    acquisition = valid_acquisition_fixture()
    records["r1_acquisition"] = _json_fixture_record(acquisition)
    manifest = {
        "schema": PAYLOAD_SCHEMA,
        "experiment": "Exp073P-v0.3-R1-payload-normalizer",
        "status": PAYLOAD_PASS,
        "complete_payload": True,
        "duplicate_basenames_rejected": True,
        "extra_bin_identities_rejected": True,
        "files": {
            "summary": {
                "basename": "exp073r1_desy1_transport_stabilized_replay_v0_7_summary.json",
                "bytes": 1,
                "sha256": records["r1"][1],
            },
            "acquisition": {
                "basename": "exp073r1_v0_7_remote_acquisition_provenance.json",
                "bytes": 1,
                "sha256": records["r1_acquisition"][1],
            },
            "runtime": {
                "basename": "exp073r1_v0_7_runtime_provenance.txt",
                "bytes": 1,
                "sha256": hashlib.sha256(b"runtime").hexdigest(),
            },
            "records": {},
            "masks": {},
        },
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "retained_dimension_evaluated": False,
        "covariance_read": False,
        "whitening_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "heldout_read": False,
        "G8_read": False,
        "gate_state": copy.deepcopy(EXPECTED_GATE_STATE),
    }
    for b in range(4):
        key = str(b)
        manifest["files"]["records"][key] = {
            "basename": f"exp073r1_v05_bin{b}_pixel_indices_le_u32.bin",
            "bytes": r1["pixel_records"][key]["file_bytes"],
            "sha256": r1["pixel_records"][key]["sha256"],
        }
        manifest["files"]["masks"][key] = {
            "basename": f"exp073r1_v05_source_bin{b}_mask_ring_nside4096_bitpack_little.bin",
            "bytes": r1["masks"][key]["file_bytes"],
            "sha256": r1["masks"][key]["sha256"],
        }
    records["r1_payload_manifest"] = _json_fixture_record(manifest)
    return records


def _must_reject(mutator: Callable[[dict[str, Any], dict[str, tuple[dict[str, Any], str]]], None]) -> None:
    metadata = valid_metadata_fixture()
    records = valid_record_fixture()
    mutator(metadata, records)
    try:
        validate_join(metadata, records, synthetic=True)
    except JoinError:
        return
    raise AssertionError("mutant unexpectedly crossed Exp073P v0.3")


def selftest() -> dict[str, Any]:
    _base.selftest()
    out = validate_join(valid_metadata_fixture(), valid_record_fixture(), synthetic=True)
    assert out["status"] == SYNTHETIC_PASS
    assert out["support_executor_authorized"] is False
    assert out["support_fraction_evaluated"] is False
    assert out["covariance_read"] is False and out["G8_read"] is False

    mutations: list[Callable[[dict[str, Any], dict[str, tuple[dict[str, Any], str]]], None]] = [
        lambda m, r: m["parents"]["r1"]["run"].__setitem__("run_attempt", 1),
        lambda m, r: m["parents"]["r1"]["run"].__setitem__("head_branch", "other"),
        lambda m, r: m["parents"]["r1"]["run"].__setitem__("event", "workflow_dispatch"),
        lambda m, r: m["parents"]["r1"]["run"].__setitem__("workflow_id", 1),
        lambda m, r: m["parents"]["r1"]["run"].__setitem__("id", 33_222_848_695),
        lambda m, r: m["parents"]["r1"]["jobs"][0].__setitem__("id", 99_068_879_596),
        lambda m, r: m["parents"]["r1"]["jobs"][0].__setitem__("run_attempt", 1),
        lambda m, r: m["parents"]["r1"]["artifacts"][0].__setitem__("name", "exp073r1-v06-invalid"),
        lambda m, r: r["r1_acquisition"][0].__setitem__("http_range_requests", 1),
        lambda m, r: r["r1_acquisition"][0].__setitem__("whole_object_attempts_from_zero", False),
        lambda m, r: r["r1_acquisition"][0]["attempts"][0].__setitem__("started_from_byte", 1),
        lambda m, r: r["r1_acquisition"][0]["attempts"][0].__setitem__("range_header_sent", True),
        lambda m, r: r["r1_acquisition"][0]["attempts"][0].__setitem__("content_range", "bytes 1-2/3"),
        lambda m, r: r["r1_acquisition"][0]["attempts"][0].__setitem__("sha256", "0" * 64),
        lambda m, r: r["r1_acquisition"][0].__setitem__("authorized_for_replay", False),
        lambda m, r: r["r1_acquisition"][0].__setitem__("f_invalid_computed", True),
        lambda m, r: r["r1_payload_manifest"][0].__setitem__("complete_payload", False),
        lambda m, r: r["r1_payload_manifest"][0].__setitem__("duplicate_basenames_rejected", False),
        lambda m, r: r["r1_payload_manifest"][0]["files"]["records"].pop("3"),
        lambda m, r: r["r1_payload_manifest"][0]["files"]["masks"]["2"].__setitem__("bytes", 0),
        lambda m, r: r["r1_payload_manifest"][0]["files"]["summary"].__setitem__("sha256", "0" * 64),
        lambda m, r: r["r1_payload_manifest"][0]["files"]["records"]["1"].__setitem__("sha256", "0" * 64),
        lambda m, r: r["r1_payload_manifest"][0].__setitem__("covariance_read", True),
    ]
    for mutation in mutations:
        _must_reject(mutation)
    out["v03_failclosed_mutations"] = len(mutations)
    return out


def _error_receipt(status: str, error: str) -> dict[str, Any]:
    return _v03_receipt(_base.base_receipt(status, synthetic=False, error=error))


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
    parser.add_argument("--r1-acquisition", type=Path)
    parser.add_argument("--r1-payload-manifest", type=Path)
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
        "metadata", "preflight", "large_source", "large_metacal", "p2", "s0", "r1",
        "r1_acquisition", "r1_payload_manifest", "boss",
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
            "r1_acquisition": load_record(args.r1_acquisition),
            "r1_payload_manifest": load_record(args.r1_payload_manifest),
            "boss": load_record(args.boss),
        }
        receipt = validate_join(metadata, records, synthetic=False)
    except JoinIncomplete as exc:
        receipt = _error_receipt(INCOMPLETE, str(exc))
        write_json(args.out, receipt)
        print(INCOMPLETE)
        raise SystemExit(3) from exc
    except (JoinError, OSError) as exc:
        receipt = _error_receipt(REJECTED, str(exc))
        write_json(args.out, receipt)
        print(REJECTED)
        raise SystemExit(2) from exc

    write_json(args.out, receipt)
    print(PASS)


if __name__ == "__main__":
    main()
