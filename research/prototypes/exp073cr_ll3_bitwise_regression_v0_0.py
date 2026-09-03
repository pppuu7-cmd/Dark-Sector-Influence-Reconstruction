#!/usr/bin/env python3
"""NON-AUTHORITATIVE Exp073CR ll3 shard bitwise-regression prototype.

No scientific/resource authority. Intended only for a future post-Exp073CQ
successor after prospective preregistration and binding.
"""
from __future__ import annotations

import argparse
import ctypes
import hashlib
import importlib
import json
from pathlib import Path

import numpy as np

L = 12288
LMAX = L - 1
EDGES = np.array([
    0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,
    661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,
    3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288
], dtype=np.int32)
SIGNATURE = (0, 2, 0, 2)
PCL_SHA = 'ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d'


def canon(x):
    return np.ascontiguousarray(np.asarray(x, dtype='<f8'))


def chash(x):
    a = canon(x)
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def exact_array(path: Path, shape, label):
    a = np.load(path, allow_pickle=False)
    if a.dtype.str != '<f8' or not a.flags.c_contiguous or tuple(a.shape) != tuple(shape):
        raise RuntimeError(f'{label}: noncanonical dtype/shape/contiguity')
    if not np.all(np.isfinite(a)):
        raise RuntimeError(f'{label}: nonfinite')
    return a


def runtime_nmtlib() -> bytes:
    ext = importlib.import_module('_nmtlib')
    return str(Path(ext.__file__).resolve()).encode()


def bind(proto_so: Path):
    lib = ctypes.CDLL(str(proto_so.resolve()))
    f = lib.exp073cr_stream_compress_band_ll3_range_v0_1
    dptr = ctypes.POINTER(ctypes.c_double)
    iptr = ctypes.POINTER(ctypes.c_int)
    f.argtypes = [
        ctypes.c_char_p, dptr,
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
        iptr, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
        ctypes.c_int, dptr,
    ]
    f.restype = ctypes.c_int
    return f, dptr, iptr


def shard_call(f, dptr, iptr, pcl, band: int, lo3: int, hi3: int):
    edges = np.ascontiguousarray(EDGES, dtype=np.int32)
    out = np.zeros((hi3-lo3,), dtype='<f8')
    s1, s2, n1, n2 = SIGNATURE
    rc = f(
        runtime_nmtlib(), pcl.ctypes.data_as(dptr),
        LMAX, s1, s2, n1, n2,
        edges.ctypes.data_as(iptr), len(edges)-1,
        band, lo3, hi3, 1, out.ctypes.data_as(dptr),
    )
    if rc != 0:
        raise RuntimeError(f'prototype helper rc={rc} band={band} ll3=[{lo3},{hi3})')
    return canon(out)


def parse_partitions(text: str):
    obj = json.loads(text)
    if not isinstance(obj, list) or not obj:
        raise ValueError('partitions must be a nonempty JSON list of boundary lists')
    out = []
    for bounds in obj:
        q = [int(x) for x in bounds]
        if q[0] != 2 or q[-1] != L or any(a >= b for a, b in zip(q, q[1:])):
            raise ValueError(f'invalid partition {q}')
        out.append(q)
    return out


def first_difference(ref, got):
    neq = np.flatnonzero(ref != got)
    if not len(neq):
        return None
    i = int(neq[0])
    ru = int(ref.view(np.uint64)[i])
    gu = int(got.view(np.uint64)[i])
    return {
        'index': i,
        'reference_float': float(ref[i]),
        'candidate_float': float(got[i]),
        'reference_uint64': f'0x{ru:016x}',
        'candidate_uint64': f'0x{gu:016x}',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--checkpoint-root', required=True,
                    help='exact restored Exp073CP checkpoint root containing upstream/ and bands/')
    ap.add_argument('--prototype-so', required=True)
    ap.add_argument('--bands', default='0,7,15')
    ap.add_argument(
        '--partitions',
        default='[[2,3072,6144,9216,12288],[2,1024,4097,7777,10000,12288]]',
        help='JSON list of complete ll3 boundary lists; every list must cover [2,12288)'
    )
    a = ap.parse_args()

    root = Path(a.checkpoint_root)
    bands = [int(x) for x in a.bands.split(',') if x.strip()]
    if not bands or any(b < 0 or b >= 39 for b in bands):
        raise SystemExit('invalid bands')
    partitions = parse_partitions(a.partitions)

    pcl = exact_array(root/'upstream/pcl.npy', (L,), 'PCL')
    if chash(pcl) != PCL_SHA:
        raise RuntimeError('PCL SHA mismatch')

    f, dptr, iptr = bind(Path(a.prototype_so))
    results = []
    for b in bands:
        ref = exact_array(root/f'bands/band_{b:02d}/payload.npy', (L,), f'reference band {b}')
        ref_sha = chash(ref)
        for bounds in partitions:
            got = np.zeros((L,), dtype='<f8')
            # Frozen helper leaves indices below lstart=max(s1,s2)=2 exactly zero.
            for lo3, hi3 in zip(bounds, bounds[1:]):
                got[lo3:hi3] = shard_call(f, dptr, iptr, pcl, b, lo3, hi3)
            got = canon(got)
            eq = bool(np.array_equal(ref, got))
            same_sha = chash(got) == ref_sha
            rec = {
                'band': b,
                'partition': bounds,
                'array_equal': eq,
                'sha_equal': same_sha,
                'reference_sha256': ref_sha,
                'candidate_sha256': chash(got),
                'finite': bool(np.all(np.isfinite(got))),
                'first_difference': first_difference(ref, got),
            }
            print(json.dumps(rec, sort_keys=True), flush=True)
            results.append(rec)

    ok = all(r['array_equal'] and r['sha_equal'] and r['finite'] for r in results)
    if not ok:
        print('FAIL_EXP073CR_RESEARCH_LL3_BITWISE_REGRESSION_V0_0', flush=True)
        raise SystemExit(42)
    print('PASS_EXP073CR_RESEARCH_LL3_BITWISE_REGRESSION_V0_0', flush=True)


if __name__ == '__main__':
    main()
