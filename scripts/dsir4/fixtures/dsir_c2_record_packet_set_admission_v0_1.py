#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
from pathlib import Path

GV_PATH = Path(__file__).with_name("dsir_c2_record_packet_admission_v0_1.py")
_spec = importlib.util.spec_from_file_location("exp073gv_packet", GV_PATH)
gv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gv)

SET_SCHEMA = "dsir.c2.record_packet_set.v0.1"
PACKET_COUNT = 28
RECORD_BYTES_TOTAL = 28 * 64


def aggregate_sha256(pairs):
    stream = bytearray()
    for packet, _record in pairs:
        digest = packet.get("record_sha256") if isinstance(packet, dict) else None
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise RuntimeError("fail-closed aggregate record digest syntax")
        stream.extend(digest.encode("ascii"))
        stream.extend(b"\n")
    return hashlib.sha256(bytes(stream)).hexdigest()


def manifest_for(pairs):
    return {
        "schema": SET_SCHEMA,
        "packet_count": PACKET_COUNT,
        "record_bytes_total": RECORD_BYTES_TOTAL,
        "aggregate_record_sha256": aggregate_sha256(pairs),
    }


def validate_set(manifest, pairs):
    if not isinstance(manifest, dict) or not isinstance(pairs, list):
        raise RuntimeError("fail-closed set type")
    if manifest.get("schema") != SET_SCHEMA:
        raise RuntimeError("fail-closed set schema")
    if manifest.get("packet_count") != PACKET_COUNT or len(pairs) != PACKET_COUNT:
        raise RuntimeError("fail-closed packet count")
    if manifest.get("record_bytes_total") != RECORD_BYTES_TOTAL:
        raise RuntimeError("fail-closed total record bytes")
    ordinals = []
    for packet, record in pairs:
        if gv.validate(packet, record) is not True:
            raise RuntimeError("fail-closed inherited packet validator")
        ordinals.append(packet["ordinal"])
    if ordinals != list(range(PACKET_COUNT)):
        raise RuntimeError("fail-closed ordinal completeness/order")
    expected = aggregate_sha256(pairs)
    if manifest.get("aggregate_record_sha256") != expected:
        raise RuntimeError("fail-closed aggregate digest")
    return True


def synthetic_set():
    pairs = []
    for ordinal in range(PACKET_COUNT):
        packet, _ = gv.synthetic_packet(ordinal)
        record = bytes(((ordinal * 17 + i) & 0xff) for i in range(64))
        packet = copy.deepcopy(packet)
        packet["record_sha256"] = hashlib.sha256(record).hexdigest()
        pairs.append((packet, record))
    return manifest_for(pairs), pairs
