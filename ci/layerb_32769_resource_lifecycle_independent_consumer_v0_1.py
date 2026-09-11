#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path

SOURCE_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
CONSUMER_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"
CONSUMER_FAIL = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_FAIL_PLUS_0_PLUS_0"
HOSTED_MEMTOTAL_KB = 16372440
FINE_NODE_SHA = "82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"
FINE_TEXT_SHA = "7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2"
BUILD_AUTH_BLOB = "ec773d9f5cbed652c52c52b5a4fae74efd5ecd0d"
ISOLATION_CONTRACT_BLOB = "d9d910d89889f6d3a27461a73c3dd72c2a9d2096"
REQUIRED_LABEL = "dsir-32769-highmem"
CLASS_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
EXPECTED_CAPACITY_PRE_SHA = "c83749338e435d85caf8f0cfb713aa9a77782a91072de93633187d9dc53a0876"
EXPECTED_CAPACITY_POST_SHA = "e6221887e19c0a576f77bbfcb2a030ff9cf8d84c62a2193ce52b8e3b541a8f0a"
EXPECTED_PARSER_PRE_SHA = "2c17690a5549e12c8fac485281ca214a20c376e1e3beba714af0e1b84cdbb0eb"
EXPECTED_PARSER_POST_SHA = "e35d53f58e0c00fa66c12d92903eb46a0862beca25167a140f0ad5ae236c25d2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_key_values(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(errors="replace").splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def parse_telemetry(path: Path) -> dict:
    text = path.read_text(errors="replace")
    samples = []
    for line in text.splitlines():
        if not line.startswith("TELEMETRY "):
            continue
        vals = {}
        for key in ("MemTotal", "MemAvailable", "SwapTotal", "SwapFree"):
            m = re.search(rf"{key}:=(\d+)kB", line)
            if m:
                vals[key] = int(m.group(1))
        if vals:
            samples.append(vals)
    if not samples:
        return {"sample_count": 0}
    memtotals = [s["MemTotal"] for s in samples if "MemTotal" in s]
    avail = [s["MemAvailable"] for s in samples if "MemAvailable" in s]
    swapfree = [s["SwapFree"] for s in samples if "SwapFree" in s]
    return {
        "sample_count": len(samples),
        "memtotal_min_kb": min(memtotals) if memtotals else None,
        "memtotal_max_kb": max(memtotals) if memtotals else None,
        "memavailable_min_kb": min(avail) if avail else None,
        "swapfree_min_kb": min(swapfree) if swapfree else None,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    root = Path(args.artifact_dir)
    required = {
        "result": root / "result.json",
        "capacity_patch": root / "capacity_patch.json",
        "candidate_memtotal": root / "candidate_memtotal_kb.txt",
        "host_before": root / "host_envelope_before.txt",
        "host_after": root / "host_envelope_after.txt",
        "stale": root / "stale_job_snapshot.json",
        "telemetry": root / "telemetry.log",
    }
    errors: list[str] = []
    for name, p in required.items():
        if not p.is_file():
            errors.append(f"missing_{name}")
    if errors:
        result = {
            "schema": "LAYERB_32769_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_V0_1",
            "classification": CONSUMER_FAIL,
            "effect": "+0/+0",
            "valid": False,
            "errors": errors,
            "scientific_response_read": False,
            "scientific_authority_created": False,
            "token": CONSUMER_FAIL,
        }
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        return 31

    src = json.loads(required["result"].read_text())
    patch = json.loads(required["capacity_patch"].read_text())
    stale = json.loads(required["stale"].read_text())
    before = parse_key_values(required["host_before"])
    after_text = required["host_after"].read_text(errors="replace")
    telemetry = parse_telemetry(required["telemetry"])

    try:
        mem_file = int(required["candidate_memtotal"].read_text().strip())
    except Exception:
        mem_file = -1
        errors.append("candidate_memtotal_parse")

    if src.get("classification") != SOURCE_PASS:
        errors.append("source_classification")
    if src.get("canonical_32769_node_sha256") != FINE_NODE_SHA or src.get("canonical_32769_text_sha256") != FINE_TEXT_SHA:
        errors.append("canonical_identity")
    if src.get("build_authority_classification") != "LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_PASS_PLUS_0_PLUS_0":
        errors.append("build_authority_classification")
    if src.get("runner_isolation_contract_git_blob") != ISOLATION_CONTRACT_BLOB or src.get("required_custom_label") != REQUIRED_LABEL:
        errors.append("runner_isolation_binding")
    if src.get("capacity") != 32769 or src.get("parser_capacity") != 524288:
        errors.append("capacity")
    if src.get("candidate_memtotal_kb") != mem_file or mem_file <= HOSTED_MEMTOTAL_KB:
        errors.append("candidate_memory")
    if src.get("candidate_strictly_higher_memory_than_exhausted_hosted") is not True:
        errors.append("higher_memory_guard")

    life = src.get("execution_lifecycle", {})
    if life.get("total_solver_constructions") != 4 or life.get("max_live_instances") != 1 or life.get("final_live_instances") != 0:
        errors.append("lifecycle")
    receipts = src.get("role_receipts")
    if not isinstance(receipts, list) or len(receipts) != 4:
        errors.append("role_receipts")
        receipts = []
    else:
        roles = [x.get("role") for x in receipts]
        if roles != ["reference", "alpha_plus", "alpha_minus", "beta_plus"]:
            errors.append("role_order")
        for x in receipts:
            if x.get("compute_completed") is not True:
                errors.append("role_compute")
            if x.get("scientific_transfer_values_read") is not False or x.get("scientific_response_computed") is not False or x.get("scientific_response_serialized") is not False:
                errors.append("role_response_blind")
            rss = x.get("ru_maxrss_kb_after_compute")
            if not isinstance(rss, int) or rss <= 0:
                errors.append("role_rss")

    for k in ("scientific_transfer_values_read", "scientific_response_read", "scientific_response_computed", "convergence_metric_computed", "convergence_classification_created", "scientific_authority_created", "successor_execution_authorized", "covariance_restriction_authorized", "Wm_S3_opened"):
        if src.get(k) is not False:
            errors.append(k)

    if patch.get("source_commit") != CLASS_COMMIT or patch.get("new_capacity") != 32769 or patch.get("parser_new_argument_capacity") != 524288:
        errors.append("capacity_patch_identity")
    if patch.get("pre_sha256") != EXPECTED_CAPACITY_PRE_SHA or patch.get("post_sha256") != EXPECTED_CAPACITY_POST_SHA:
        errors.append("capacity_patch_hash")
    if patch.get("parser_pre_sha256") != EXPECTED_PARSER_PRE_SHA or patch.get("parser_post_sha256") != EXPECTED_PARSER_POST_SHA:
        errors.append("parser_patch_hash")

    if stale.get("id") != 103112190909 or stale.get("status") == "in_progress":
        errors.append("stale_job_ownership")
    if before.get("required_custom_label") != REQUIRED_LABEL:
        errors.append("host_label_receipt")
    if before.get("candidate_memtotal_kb") != str(mem_file):
        errors.append("host_memory_receipt")
    if not after_text.strip():
        errors.append("host_after_empty")

    if telemetry.get("sample_count", 0) < 1:
        errors.append("telemetry_missing")
    if telemetry.get("memtotal_min_kb") is not None and telemetry["memtotal_min_kb"] != mem_file:
        errors.append("telemetry_memtotal")

    peak_role_rss = max((x.get("ru_maxrss_kb_after_compute", 0) for x in receipts), default=0)
    valid = not errors
    classification = CONSUMER_PASS if valid else CONSUMER_FAIL
    out = {
        "schema": "LAYERB_32769_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "valid": valid,
        "errors": errors,
        "source_result_sha256": sha256(required["result"]),
        "capacity_patch_sha256": sha256(required["capacity_patch"]),
        "host_envelope_before_sha256": sha256(required["host_before"]),
        "host_envelope_after_sha256": sha256(required["host_after"]),
        "stale_job_snapshot_sha256": sha256(required["stale"]),
        "telemetry_sha256": sha256(required["telemetry"]),
        "candidate_memtotal_kb": mem_file,
        "candidate_strictly_higher_memory_than_exhausted_hosted": mem_file > HOSTED_MEMTOTAL_KB,
        "required_custom_label": REQUIRED_LABEL,
        "runner_name": before.get("runner_name"),
        "runner_os": before.get("runner_os"),
        "runner_arch": before.get("runner_arch"),
        "execution_lifecycle": life,
        "peak_role_ru_maxrss_kb": peak_role_rss,
        "telemetry_summary": telemetry,
        "stale_job_status": stale.get("status"),
        "canonical_32769_node_sha256": FINE_NODE_SHA,
        "class_build_authority_git_blob": BUILD_AUTH_BLOB,
        "runner_isolation_contract_git_blob": ISOLATION_CONTRACT_BLOB,
        "scientific_response_read": False,
        "scientific_authority_created": False,
        "successor_execution_authorized": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": classification,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(classification)
    if errors:
        print("ERRORS", ",".join(errors))
    return 0 if valid else 31


if __name__ == "__main__":
    raise SystemExit(main())
