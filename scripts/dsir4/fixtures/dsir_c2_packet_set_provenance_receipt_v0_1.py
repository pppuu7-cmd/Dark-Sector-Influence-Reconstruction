#!/usr/bin/env python3
import hashlib

SCHEMA = "dsir.c2.packet_set_provenance_receipt.v0.1"
KEYS = [
    "schema","packet_set_aggregate_sha256","packet_count","record_bytes_total",
    "gt_manifest_sha256","gr_contract_sha256","solver_head","recorder_blob_sha1",
    "gu_handoff_sha256","gu_receipt_set_sha256","coordinate_order",
    "decoded_field_values_inspected","scientific_mapping_applied",
]
FIXED = {
    "schema": SCHEMA,
    "packet_set_aggregate_sha256": "a98f9ca1f10a9b2bfc957fac81ed837d85bbb203a5f5f0d7ff369a2061bc78b7",
    "packet_count": 28,
    "record_bytes_total": 1792,
    "gt_manifest_sha256": "d86a034988fd42b98e40f68f176a1b834844d1e18208f938542c69f979d048f8",
    "gr_contract_sha256": "6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b",
    "solver_head": "ac627d54e9ce196a08878d1ba33999819925d19c",
    "recorder_blob_sha1": "c6144598b9f75908ee27a517d31eda509f7947f6",
    "gu_handoff_sha256": "5ed0b924379f8ae961acd5d5b14171f96b3692972b2348cba3022d669a343931",
    "gu_receipt_set_sha256": "bbcfffbc9845dfb74ef4b8fffbcd5f9851cc45d27272cf39595d62ce9f0d8075",
    "coordinate_order": "z-major/k-minor",
    "decoded_field_values_inspected": False,
    "scientific_mapping_applied": False,
}

def canonical_bytes(receipt):
    if not isinstance(receipt, dict) or set(receipt) != set(KEYS):
        raise RuntimeError("fail-closed receipt keys")
    lines=[]
    for k in KEYS:
        v=receipt[k]
        if isinstance(v,bool): s="true" if v else "false"
        elif isinstance(v,(str,int)): s=str(v)
        else: raise RuntimeError("fail-closed receipt value type")
        if "\n" in s or "\r" in s or "=" in s:
            raise RuntimeError("fail-closed receipt encoding")
        lines.append(f"{k}={s}\n")
    return "".join(lines).encode("utf-8")

def receipt_digest(receipt):
    return hashlib.sha256(canonical_bytes(receipt)).hexdigest()

def validate(receipt, digest):
    if receipt != FIXED:
        raise RuntimeError("fail-closed receipt identity")
    if receipt["decoded_field_values_inspected"] is not False or receipt["scientific_mapping_applied"] is not False:
        raise RuntimeError("fail-closed forbidden science flag")
    if digest != receipt_digest(receipt):
        raise RuntimeError("fail-closed receipt digest")
    return True

def synthetic_receipt():
    r=dict(FIXED)
    return r, receipt_digest(r)
