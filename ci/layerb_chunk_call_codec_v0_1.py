#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, struct
import numpy as np

SCHEMA = 'LAYERB_CHUNK_CALL_CODEC_V0_1'

def f64_u64hex(x: float) -> str:
    return format(struct.unpack('<Q', struct.pack('<d', float(x)))[0], '016x')

def u64hex_f64(x: str) -> float:
    return struct.unpack('<d', struct.pack('<Q', int(x, 16)))[0]

def arr_u64hex(a) -> list[str]:
    a = np.ascontiguousarray(np.asarray(a, dtype='<f8'), dtype='<f8')
    return [format(int(x), '016x') for x in a.view('<u8')]

def u64hex_arr(xs) -> np.ndarray:
    u = np.asarray([int(x,16) for x in xs], dtype='<u8')
    return np.ascontiguousarray(u.view('<f8'), dtype='<f8')

def calls_digest(calls) -> str:
    h = hashlib.sha256()
    h.update(SCHEMA.encode() + b'\0')
    h.update(struct.pack('<Q', len(calls)))
    for z, targets in calls:
        t = np.ascontiguousarray(np.asarray(targets, dtype='<f8'), dtype='<f8')
        h.update(struct.pack('<dQ', float(z), int(t.size)))
        h.update(t.tobytes())
    return h.hexdigest()

def encode_calls(calls) -> list[dict]:
    return [
        {'z_u64hex': f64_u64hex(z), 'targets_u64hex': arr_u64hex(t)}
        for z,t in calls
    ]

def decode_calls(rows) -> list[tuple[float,np.ndarray]]:
    return [(u64hex_f64(r['z_u64hex']), u64hex_arr(r['targets_u64hex'])) for r in rows]

def f8_b64(a) -> str:
    a = np.ascontiguousarray(np.asarray(a, dtype='<f8'), dtype='<f8')
    return base64.b64encode(a.tobytes()).decode('ascii')

def b64_f8(s: str, n: int) -> np.ndarray:
    b = base64.b64decode(s.encode('ascii'), validate=True)
    if len(b) != 8*n:
        raise RuntimeError(f'f8 payload length mismatch {len(b)} != {8*n}')
    return np.frombuffer(b, dtype='<f8').copy()

def bool_b64(a) -> str:
    a = np.asarray(a, dtype=np.bool_).reshape(-1)
    return base64.b64encode(np.packbits(a, bitorder='little').tobytes()).decode('ascii')

def b64_bool(s: str, n: int) -> np.ndarray:
    b = base64.b64decode(s.encode('ascii'), validate=True)
    x = np.unpackbits(np.frombuffer(b, dtype=np.uint8), bitorder='little')[:n]
    if x.size != n:
        raise RuntimeError('bool payload length mismatch')
    return x.astype(bool, copy=False)
