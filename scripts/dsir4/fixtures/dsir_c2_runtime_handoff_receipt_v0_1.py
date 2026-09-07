#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

GT_MANIFEST_SHA256 = "d86a034988fd42b98e40f68f176a1b834844d1e18208f938542c69f979d048f8"
GR_CONTRACT_SHA256 = "6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b"
SOLVER_HEAD = "ac627d54e9ce196a08878d1ba33999819925d19c"
RECORDER_BLOB = "c6144598b9f75908ee27a517d31eda509f7947f6"
REQUEST_COUNT = 28
RECORD_BYTES = 64
FIELD_COUNT = 8


def _canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _load_gt_module():
    p = Path(__file__).with_name("dsir_c2_dryrun_record_envelope_v0_1.py")
    spec = importlib.util.spec_from_file_location("gt_env", p)
    if spec is None or spec.loader is None:
        raise RuntimeError("fail-closed GT module import failure")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _validate_gt_manifest(manifest):
    embedded = manifest.get("manifest_sha256")
    unsigned = dict(manifest)
    unsigned.pop("manifest_sha256", None)
    recomputed = hashlib.sha256(_canonical(unsigned)).hexdigest()
    if embedded != GT_MANIFEST_SHA256 or recomputed != GT_MANIFEST_SHA256:
        raise RuntimeError("fail-closed GT manifest content fingerprint mismatch")


def build_handoff_and_receipts(contract_path):
    gt = _load_gt_module()
    manifest = gt.build_manifest(contract_path)
    _validate_gt_manifest(manifest)
    envs = manifest.get("envelopes")
    if not isinstance(envs, list) or len(envs) != REQUEST_COUNT:
        raise RuntimeError("fail-closed envelope count mismatch")
    if [e.get("ordinal") for e in envs] != list(range(REQUEST_COUNT)):
        raise RuntimeError("fail-closed envelope ordering mismatch")

    handoff = {
        "schema": "dsir.c2.runtime_handoff.v0.1",
        "gt_manifest_sha256": GT_MANIFEST_SHA256,
        "gr_contract_sha256": GR_CONTRACT_SHA256,
        "solver_head": SOLVER_HEAD,
        "recorder_blob_sha1": RECORDER_BLOB,
        "request_count": REQUEST_COUNT,
        "record_bytes": RECORD_BYTES,
        "record_field_count": FIELD_COUNT,
        "ordering": "z_major_k_minor",
        "payload_state": "ABSENT_BY_CONTRACT",
        "prediction_ready": False,
    }
    handoff["handoff_sha256"] = hashlib.sha256(_canonical(handoff)).hexdigest()

    receipts = []
    for e in envs:
        if e.get("record_payload") is not None:
            raise RuntimeError("fail-closed GT payload unexpectedly present")
        if e.get("runtime_status") != "AWAITING_EXACT_RUNTIME_RECORD":
            raise RuntimeError("fail-closed GT runtime status mismatch")
        receipts.append({
            "schema": "dsir.c2.runtime_receipt.v0.1",
            "ordinal": e["ordinal"],
            "z": e["z"],
            "k_Mpc^-1": e["k_Mpc^-1"],
            "gt_manifest_sha256": GT_MANIFEST_SHA256,
            "gr_contract_sha256": GR_CONTRACT_SHA256,
            "solver_head": SOLVER_HEAD,
            "recorder_blob_sha1": RECORDER_BLOB,
            "expected_record_bytes": RECORD_BYTES,
            "received_record_bytes": 0,
            "receipt_status": "DRY_RUN_NO_PAYLOAD",
        })
    if len(receipts) != REQUEST_COUNT:
        raise RuntimeError("fail-closed receipt count mismatch")
    receipt_sha256 = hashlib.sha256(_canonical(receipts)).hexdigest()
    return handoff, receipts, receipt_sha256
