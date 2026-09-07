#!/usr/bin/env python3
import hashlib

GT_MANIFEST_SHA256 = "d86a034988fd42b98e40f68f176a1b834844d1e18208f938542c69f979d048f8"
GR_CONTRACT_SHA256 = "6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b"
SOLVER_HEAD = "ac627d54e9ce196a08878d1ba33999819925d19c"
RECORDER_BLOB = "c6144598b9f75908ee27a517d31eda509f7947f6"
GU_HANDOFF_SHA256 = "5ed0b924379f8ae961acd5d5b14171f96b3692972b2348cba3022d669a343931"
GU_RECEIPT_SET_SHA256 = "bbcfffbc9845dfb74ef4b8fffbcd5f9851cc45d27272cf39595d62ce9f0d8075"
Z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]
K = [0.00067, 0.00201, 0.0067, 0.0201]


def expected_coordinate(ordinal):
    if type(ordinal) is not int or not (0 <= ordinal < 28):
        raise RuntimeError("fail-closed ordinal")
    return Z[ordinal // 4], K[ordinal % 4]


def validate(packet, record):
    if not isinstance(packet, dict) or not isinstance(record, (bytes, bytearray)):
        raise RuntimeError("fail-closed packet type")
    if packet.get("schema") != "dsir.c2.record_packet.v0.1":
        raise RuntimeError("fail-closed schema")
    ordinal = packet.get("ordinal")
    z, k = expected_coordinate(ordinal)
    if packet.get("z") != z or packet.get("k_Mpc^-1") != k:
        raise RuntimeError("fail-closed coordinate")
    required = {
        "gt_manifest_sha256": GT_MANIFEST_SHA256,
        "gr_contract_sha256": GR_CONTRACT_SHA256,
        "solver_head": SOLVER_HEAD,
        "recorder_blob_sha1": RECORDER_BLOB,
        "gu_handoff_sha256": GU_HANDOFF_SHA256,
        "gu_receipt_set_sha256": GU_RECEIPT_SET_SHA256,
        "record_encoding": "little_endian_binary64_x8",
        "record_bytes": 64,
    }
    for key, value in required.items():
        if packet.get(key) != value:
            raise RuntimeError("fail-closed identity " + key)
    if len(record) != 64:
        raise RuntimeError("fail-closed record length")
    digest = hashlib.sha256(bytes(record)).hexdigest()
    if packet.get("record_sha256") != digest:
        raise RuntimeError("fail-closed record digest")
    return True


def synthetic_packet(ordinal=0):
    record = bytes(range(64))
    z, k = expected_coordinate(ordinal)
    packet = {
        "schema": "dsir.c2.record_packet.v0.1",
        "ordinal": ordinal,
        "z": z,
        "k_Mpc^-1": k,
        "gt_manifest_sha256": GT_MANIFEST_SHA256,
        "gr_contract_sha256": GR_CONTRACT_SHA256,
        "solver_head": SOLVER_HEAD,
        "recorder_blob_sha1": RECORDER_BLOB,
        "gu_handoff_sha256": GU_HANDOFF_SHA256,
        "gu_receipt_set_sha256": GU_RECEIPT_SET_SHA256,
        "record_encoding": "little_endian_binary64_x8",
        "record_bytes": 64,
        "record_sha256": hashlib.sha256(record).hexdigest(),
    }
    return packet, record
