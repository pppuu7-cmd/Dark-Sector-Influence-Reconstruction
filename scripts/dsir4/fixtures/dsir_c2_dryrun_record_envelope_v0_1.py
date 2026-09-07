#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

EXPECTED_CONTRACT_SHA256 = "6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b"
EXPECTED_SOLVER_HEAD = "ac627d54e9ce196a08878d1ba33999819925d19c"
EXPECTED_RECORDER_BLOB = "c6144598b9f75908ee27a517d31eda509f7947f6"
EXPECTED_FIELDS = ["tau", "k", "a", "H", "delta_m", "theta_m", "rho_idm_iv", "rho_iv"]
EXPECTED_STATUS = "AWAITING_EXACT_RUNTIME_RECORD"


def _canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _load_emitter():
    path = Path(__file__).with_name("dsir_c2_runtime_request_emitter_v0_1.py")
    spec = importlib.util.spec_from_file_location("dsir_c2_runtime_request_emitter_v0_1", path)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError("emitter loader unavailable")
    spec.loader.exec_module(module)
    return module


def _validate_contract(contract_path):
    contract = json.loads(Path(contract_path).read_text(encoding="utf-8"))
    digest = hashlib.sha256(_canonical(contract)).hexdigest()
    if digest != EXPECTED_CONTRACT_SHA256:
        raise RuntimeError("contract fingerprint mismatch")
    checks = {
        "solver_head": EXPECTED_SOLVER_HEAD,
        "recorder_blob_sha1": EXPECTED_RECORDER_BLOB,
        "record_fields": EXPECTED_FIELDS,
        "record_field_count": 8,
        "record_bytes": 64,
        "ordering": "z_major_k_minor",
        "expected_request_count": 28,
    }
    for key, expected in checks.items():
        if contract.get(key) != expected:
            raise RuntimeError(f"contract field mismatch: {key}")
    if contract.get("k_Mpc^-1") != [0.00067, 0.00201, 0.0067, 0.0201]:
        raise RuntimeError("k grid mismatch")
    if contract.get("z") != [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]:
        raise RuntimeError("z grid mismatch")
    for flag in ["interpolation", "extrapolation", "smoothing", "averaging", "tolerance_matching", "nearest_neighbour", "rounding_rescue", "effective_coordinate_substitution", "fiducial_P_shortcut"]:
        if contract.get(flag) is not False:
            raise RuntimeError(f"prohibited transformation enabled: {flag}")
    return contract


def assemble_envelopes(contract_path, requests=None):
    contract = _validate_contract(contract_path)
    emitter = _load_emitter()
    admitted = emitter.emit_requests(Path(contract_path))
    if requests is None:
        requests = admitted
    if requests != admitted:
        raise RuntimeError("request sequence differs from admitted Exp073GS sequence")
    envelopes = []
    for req in requests:
        envelopes.append({
            "ordinal": req["ordinal"],
            "z": req["z"],
            "k_Mpc^-1": req["k_Mpc^-1"],
            "record_schema": contract["recorder_schema"],
            "record_fields": list(EXPECTED_FIELDS),
            "record_field_count": 8,
            "record_bytes": 64,
            "solver_head": EXPECTED_SOLVER_HEAD,
            "recorder_blob_sha1": EXPECTED_RECORDER_BLOB,
            "runtime_status": EXPECTED_STATUS,
            "record_payload": None,
        })
    return envelopes


def build_manifest(contract_path, requests=None):
    envelopes = assemble_envelopes(contract_path, requests=requests)
    manifest = {
        "schema": "dsir.c2.dryrun_record_envelope_manifest.v0.1",
        "contract_sha256": EXPECTED_CONTRACT_SHA256,
        "request_count": len(envelopes),
        "runtime_status": EXPECTED_STATUS,
        "envelopes": envelopes,
    }
    manifest["manifest_sha256"] = hashlib.sha256(_canonical(manifest)).hexdigest()
    return manifest
