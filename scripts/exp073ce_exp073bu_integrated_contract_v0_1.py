#!/usr/bin/env python3
"""Exp073CE v0.1 static integration contract for future Exp073BU A/B science.

SUPPORT ONLY: this module performs no Wm_S3 numerical computation and creates no
scientific authority. It freezes fail-closed orchestration invariants that a later
explicitly activated driver must satisfy.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, Mapping

CONTRACT_ID = "EXP073CE_V0_1_EXP073BU_INTEGRATED_DRIVER"
NA_MASTER_VERSION = "2.7"
NSIDE = 4096
ELL_MIN = 0
ELL_MAX = 12287
NBANDS = 39
CANONICAL_DTYPE = "<f8"
CANONICAL_SHAPE = (39, 12288)
WM_COMPONENT = "TE<-TE"
WW_COMPONENT = "EE<-EE"
OUTER_WORKERS = 8
NESTED_THREAD_ENV = {
    "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
}
CHECKPOINT_STAGES = (
    "fresh_masks_complete",
    "fresh_workspace_mcm_complete",
    "mcm_fits_verified",
    "full_window_complete",
    "selected_te_complete",
    "replica_receipt_complete",
)
REPLICAS = ("A", "B")
FORBIDDEN_NUMERICAL_IMPORTS = (
    "historical_wm_s3_pcl",
    "historical_reference_bands",
    "historical_wm_s3_checkpoint",
    "historical_candidate_output",
)
FORBIDDEN_MCM_API = "get_coupling_matrix"
REQUIRED_PERSISTENCE_API = "write_to"
MCM_CONSUMER = "read_only_os_mmap_row_stream"
FULL_STOCK_ARITHMETIC = "namaster_2_7_full_ncls2_stock_operation_order"


def canonical_json(obj: Mapping[str, Any]) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def checkpoint_namespace(replica: str) -> str:
    if replica not in REPLICAS:
        raise ValueError("unknown replica")
    return f"checkpoints/exp073bu/{replica.lower()}"


def validate_manifest(manifest: Mapping[str, Any], *, replica: str, stage: str,
                      contract_fingerprint: str, source_head_sha: str,
                      provenance_sha256: str, payload_sha256: str) -> None:
    """Fail closed on any checkpoint identity mismatch."""
    if replica not in REPLICAS or stage not in CHECKPOINT_STAGES:
        raise RuntimeError("invalid checkpoint identity")
    expected = {
        "contract_id": CONTRACT_ID,
        "replica": replica,
        "checkpoint_namespace": checkpoint_namespace(replica),
        "stage": stage,
        "contract_fingerprint": contract_fingerprint,
        "source_head_sha": source_head_sha,
        "provenance_sha256": provenance_sha256,
        "payload_sha256": payload_sha256,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise RuntimeError(f"checkpoint restore mismatch: {key}")


def validate_stage_transition(previous: str | None, current: str) -> None:
    idx = CHECKPOINT_STAGES.index(current)
    expected_prev = None if idx == 0 else CHECKPOINT_STAGES[idx - 1]
    if previous != expected_prev:
        raise RuntimeError("noncanonical checkpoint transition")


def validate_replica_isolation(replica: str, restore_namespace: str) -> None:
    if restore_namespace != checkpoint_namespace(replica):
        raise RuntimeError("cross-replica numerical restore forbidden")


def pin_nested_threads() -> None:
    for key, value in NESTED_THREAD_ENV.items():
        os.environ[key] = value


def validate_fresh_replica_inputs(receipt: Mapping[str, Any], replica: str) -> None:
    if receipt.get("replica") != replica:
        raise RuntimeError("replica mismatch")
    if receipt.get("fresh_masks") is not True or receipt.get("fresh_replica_local_pcl") is not True:
        raise RuntimeError("fresh independent input construction not proven")
    imported = set(receipt.get("numerical_imports", ()))
    if imported.intersection(FORBIDDEN_NUMERICAL_IMPORTS):
        raise RuntimeError("historical Wm_S3 numerical import forbidden")


def validate_mcm_lifecycle(receipt: Mapping[str, Any]) -> None:
    if receipt.get("persistence_api") != REQUIRED_PERSISTENCE_API:
        raise RuntimeError("stock write_to persistence not proven")
    if receipt.get("workspace_destroyed_before_consume") is not True:
        raise RuntimeError("workspace must be destroyed before mmap consumption")
    if receipt.get("mcm_consumer") != MCM_CONSUMER:
        raise RuntimeError("verified read-only OS mmap row-stream route required")
    if receipt.get("second_full_mcm_heap_copy") is not False:
        raise RuntimeError("second full MCM heap copy forbidden")
    if FORBIDDEN_MCM_API in set(receipt.get("apis_used", ())):
        raise RuntimeError("get_coupling_matrix materialization forbidden")


def classify_final_ab(a: Mapping[str, Any], b: Mapping[str, Any]) -> str:
    """Machine-checkable final classifier. Never uses tolerance."""
    required = ("valid", "provenance_sha256", "contract_fingerprint", "source_head_sha",
                "canonical_sha256", "array_equal_peer", "dtype", "shape", "stage")
    if any(key not in a or key not in b for key in required):
        return "INFRASTRUCTURE_INCOMPLETE"
    if a["valid"] is not True or b["valid"] is not True:
        return "BLOCKED_INVALID_REPLICA_RECEIPT"
    identity_keys = ("provenance_sha256", "contract_fingerprint", "source_head_sha")
    if any(a[k] != b[k] for k in identity_keys):
        return "BLOCKED_PROVENANCE_OR_SOURCE_MISMATCH"
    if a["dtype"] != CANONICAL_DTYPE or b["dtype"] != CANONICAL_DTYPE:
        return "INFRASTRUCTURE_INCOMPLETE"
    if tuple(a["shape"]) != CANONICAL_SHAPE or tuple(b["shape"]) != CANONICAL_SHAPE:
        return "INFRASTRUCTURE_INCOMPLETE"
    if a["stage"] != "replica_receipt_complete" or b["stage"] != "replica_receipt_complete":
        return "INFRASTRUCTURE_INCOMPLETE"
    exact_sha = a["canonical_sha256"] == b["canonical_sha256"]
    exact_array = a["array_equal_peer"] is True and b["array_equal_peer"] is True
    if exact_sha and exact_array:
        return "SCIENTIFIC_REPEATABILITY_PASS"
    return "SCIENTIFIC_REPEATABILITY_FAIL"


def contract_fingerprint() -> str:
    frozen = {
        "contract_id": CONTRACT_ID,
        "namaster": NA_MASTER_VERSION,
        "nside": NSIDE,
        "ell": [ELL_MIN, ELL_MAX],
        "nbands": NBANDS,
        "dtype": CANONICAL_DTYPE,
        "shape": list(CANONICAL_SHAPE),
        "wm_component": WM_COMPONENT,
        "ww_component": WW_COMPONENT,
        "workers": OUTER_WORKERS,
        "nested_threads": NESTED_THREAD_ENV,
        "stages": list(CHECKPOINT_STAGES),
        "replicas": list(REPLICAS),
        "stock_arithmetic": FULL_STOCK_ARITHMETIC,
        "persistence": REQUIRED_PERSISTENCE_API,
        "mcm_consumer": MCM_CONSUMER,
    }
    return sha256_bytes(canonical_json(frozen))


if __name__ == "__main__":
    print(json.dumps({"contract_id": CONTRACT_ID, "fingerprint": contract_fingerprint()}, sort_keys=True))
