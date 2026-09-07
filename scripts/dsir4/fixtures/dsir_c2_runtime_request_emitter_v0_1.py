from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List

EXPECTED_CONTRACT_SHA256 = "6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b"
EXPECTED_SOLVER_REPOSITORY = "kaeonikc/class_iv"
EXPECTED_SOLVER_HEAD = "ac627d54e9ce196a08878d1ba33999819925d19c"
EXPECTED_RECORDER_BLOB = "c6144598b9f75908ee27a517d31eda509f7947f6"
EXPECTED_ORDERING = "z_major_k_minor"
EXPECTED_UNITS = "k_Mpc^-1"
EXPECTED_REQUEST_COUNT = 28
EXPECTED_RECORD_BYTES = 64
EXPECTED_FIELD_COUNT = 8

PROHIBITED_FLAGS = (
    "interpolation",
    "extrapolation",
    "smoothing",
    "averaging",
    "tolerance_matching",
    "nearest_neighbour",
    "rounding_rescue",
    "effective_coordinate_substitution",
    "fiducial_P_shortcut",
)


def _canonical_bytes(contract: Dict[str, Any]) -> bytes:
    return json.dumps(
        contract, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def load_frozen_contract(path: str | Path) -> Dict[str, Any]:
    contract = json.loads(Path(path).read_text(encoding="utf-8"))
    digest = hashlib.sha256(_canonical_bytes(contract)).hexdigest()
    if digest != EXPECTED_CONTRACT_SHA256:
        raise RuntimeError("fail-closed contract fingerprint mismatch")
    if contract.get("solver_repository") != EXPECTED_SOLVER_REPOSITORY:
        raise RuntimeError("fail-closed solver repository mismatch")
    if contract.get("solver_head") != EXPECTED_SOLVER_HEAD:
        raise RuntimeError("fail-closed solver head mismatch")
    if contract.get("recorder_blob_sha1") != EXPECTED_RECORDER_BLOB:
        raise RuntimeError("fail-closed recorder blob mismatch")
    if contract.get("ordering") != EXPECTED_ORDERING:
        raise RuntimeError("fail-closed ordering mismatch")
    if contract.get("expected_request_count") != EXPECTED_REQUEST_COUNT:
        raise RuntimeError("fail-closed request-count mismatch")
    if contract.get("record_bytes") != EXPECTED_RECORD_BYTES:
        raise RuntimeError("fail-closed record-width mismatch")
    if contract.get("record_field_count") != EXPECTED_FIELD_COUNT:
        raise RuntimeError("fail-closed field-count mismatch")
    for key in PROHIBITED_FLAGS:
        if contract.get(key) is not False:
            raise RuntimeError(f"fail-closed prohibited flag enabled: {key}")
    return contract


def emit_requests(path: str | Path) -> List[Dict[str, float | int]]:
    contract = load_frozen_contract(path)
    out: List[Dict[str, float | int]] = []
    ordinal = 0
    for z in contract["z"]:
        for k in contract[EXPECTED_UNITS]:
            out.append({"ordinal": ordinal, "z": z, EXPECTED_UNITS: k})
            ordinal += 1
    if len(out) != EXPECTED_REQUEST_COUNT:
        raise RuntimeError("fail-closed emitted request-count mismatch")
    return out


def build_provenance_manifest(path: str | Path) -> Dict[str, Any]:
    contract = load_frozen_contract(path)
    manifest: Dict[str, Any] = {
        "schema": "dsir.c2.runtime_request_emitter.provenance.v0.1",
        "contract_sha256": EXPECTED_CONTRACT_SHA256,
        "solver_repository": EXPECTED_SOLVER_REPOSITORY,
        "solver_head": EXPECTED_SOLVER_HEAD,
        "recorder_blob_sha1": EXPECTED_RECORDER_BLOB,
        "ordering": EXPECTED_ORDERING,
        "units": EXPECTED_UNITS,
        "request_count": EXPECTED_REQUEST_COUNT,
        "record_bytes": EXPECTED_RECORD_BYTES,
        "record_field_count": EXPECTED_FIELD_COUNT,
        "prohibited_transformations": {key: contract[key] for key in PROHIBITED_FLAGS},
    }
    canonical = json.dumps(
        manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    manifest["manifest_sha256"] = hashlib.sha256(canonical).hexdigest()
    return manifest
