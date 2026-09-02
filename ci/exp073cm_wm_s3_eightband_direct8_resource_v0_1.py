#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ctypes
import hashlib
import importlib
import json
import resource
import time
from pathlib import Path

import numpy as np

L = 12288
LMAX = L - 1
EDGES = np.array([
    0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,
    852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,
    5047,5731,6508,7390,8392,9529,10821,12288
], dtype=np.int32)
SIGNATURE = (0, 2, 0, 2)
IB_LO = 0
IB_HI = 8
REFERENCE_THREADS = 1
TARGET_THREADS = 8
CPU_FRACTION_MIN = 0.90

PASS = 'PASS_EXP073CM_WM_S3_EIGHTBAND_DIRECT8_RESOURCE_V0_1'
FAIL_EXACT = 'FAIL_EXP073CM_WM_S3_EIGHTBAND_DIRECT8_EXACT_EQUIVALENCE_V0_1'
FAIL_SWAP = 'FAIL_EXP073CM_WM_S3_DIRECT8_SWAP_SAFETY_V0_1'
FAIL_CPU = 'FAIL_EXP073CM_WM_S3_DIRECT8_CPU_TARGET_V0_1'


def canon(x: np.ndarray) -> np.ndarray:
    return np.ascontiguousarray(np.asarray(x, dtype='<f8'))


def chash(x: np.ndarray) -> str:
    a = canon(x)
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def runtime_nmtlib() -> bytes:
    ext = importlib.import_module('_nmtlib')
    return str(Path(ext.__file__).resolve()).encode()


def load_ca(path: Path):
    lib = ctypes.CDLL(str(path.resolve()))
    dptr = ctypes.POINTER(ctypes.c_double)
    iptr = ctypes.POINTER(ctypes.c_int)
    f = lib.exp073ca_stream_compress_range
    f.argtypes = [
        ctypes.c_char_p, dptr, ctypes.c_int,
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
        iptr, ctypes.c_int, ctypes.c_int, ctypes.c_int,
        ctypes.c_int, dptr,
    ]
    f.restype = ctypes.c_int
    return f


def call_range(f, pcl: np.ndarray, threads: int) -> np.ndarray:
    pcl = canon(pcl)
    edges = np.ascontiguousarray(EDGES, dtype=np.int32)
    out = np.zeros((IB_HI - IB_LO, L), dtype=np.float64)
    s1, s2, n1, n2 = SIGNATURE
    rc = f(
        runtime_nmtlib(),
        pcl.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        LMAX, s1, s2, n1, n2,
        edges.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
        len(edges) - 1, IB_LO, IB_HI, threads,
        out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    )
    if rc != 0:
        raise RuntimeError(('range_helper_rc', rc, threads))
    return canon(out)


def swap_used_kib() -> int:
    vals = {}
    with open('/proc/meminfo', 'r', encoding='utf-8') as f:
        for line in f:
            if ':' not in line:
                continue
            k, v = line.split(':', 1)
            p = v.strip().split()
            if p and p[0].isdigit():
                vals[k] = int(p[0])
    return max(0, vals.get('SwapTotal', 0) - vals.get('SwapFree', 0))


def cpu_seconds() -> float:
    r = resource.getrusage(resource.RUSAGE_SELF)
    return float(r.ru_utime + r.ru_stime)


def maxrss_kib() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def load_pcl(path: str) -> np.ndarray:
    pcl = canon(np.load(path, allow_pickle=False))
    if pcl.shape != (L,) or not np.all(np.isfinite(pcl)):
        raise AssertionError(('real_wm_s3_pcl', pcl.shape, bool(np.all(np.isfinite(pcl)))))
    return pcl


def save_array(path: str, arr: np.ndarray) -> None:
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    np.save(p, canon(arr), allow_pickle=False)


def write_json(path: str, rec: dict) -> None:
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(rec, indent=2, sort_keys=True), flush=True)


def run_stage(mode: str, pcl_path: str, so_path: str, out_npy: str, out_json: str) -> None:
    threads = REFERENCE_THREADS if mode == 'reference' else TARGET_THREADS
    pcl = load_pcl(pcl_path)
    f = load_ca(Path(so_path))
    swap0 = swap_used_kib(); rss0 = maxrss_kib(); c0 = cpu_seconds(); t0 = time.monotonic()
    out = call_range(f, pcl, threads)
    wall = time.monotonic() - t0; cpu = cpu_seconds() - c0
    swap1 = swap_used_kib(); rss1 = maxrss_kib()
    finite = bool(np.all(np.isfinite(out)))
    if not finite:
        raise AssertionError((mode, 'nonfinite'))
    effective_cpu_cores = (cpu / wall) if wall > 0 else 0.0
    rec = {
        'experiment': 'Exp073CM', 'task': 'Wm_S3', 'stage': mode,
        'lmax': LMAX, 'row_length': L, 'band_lo': IB_LO, 'band_hi_exclusive': IB_HI,
        'bands': list(range(IB_LO, IB_HI)), 'ell_lo': int(EDGES[IB_LO]),
        'ell_hi_exclusive': int(EDGES[IB_HI]), 'signature': list(SIGNATURE),
        'threads': threads, 'wall_seconds': wall, 'process_cpu_seconds': cpu,
        'effective_cpu_cores': effective_cpu_cores,
        'cpu_fraction_of_8': (effective_cpu_cores / 8.0) if mode == 'target' else None,
        'swap_used_kib_before': swap0, 'swap_used_kib_after': swap1,
        'swap_increase_kib': max(0, swap1 - swap0),
        'ru_maxrss_kib_before': rss0, 'ru_maxrss_kib_after': rss1,
        'sha256': chash(out), 'shape': list(out.shape), 'dtype': '<f8', 'finite': finite,
    }
    save_array(out_npy, out); write_json(out_json, rec)


def final_stage(ref_path: str, target_path: str, ref_json: str, target_json: str, out_json: str) -> None:
    ref = canon(np.load(ref_path, allow_pickle=False)); target = canon(np.load(target_path, allow_pickle=False))
    if ref.shape != (8, L) or target.shape != (8, L):
        raise AssertionError(('shape', ref.shape, target.shape))
    rr = json.loads(Path(ref_json).read_text()); tr = json.loads(Path(target_json).read_text())
    href, htarget = chash(ref), chash(target)
    if href != rr.get('sha256') or htarget != tr.get('sha256'):
        raise AssertionError('stage receipt SHA mismatch')
    array_equal = bool(np.array_equal(ref, target)); exact = array_equal and href == htarget
    target_swap = int(tr['swap_increase_kib'])
    cpu_fraction = float(tr['cpu_fraction_of_8'])
    cpu_target_met = cpu_fraction >= CPU_FRACTION_MIN
    if not exact:
        status = FAIL_EXACT
    elif target_swap != 0:
        status = FAIL_SWAP
    elif not cpu_target_met:
        status = FAIL_CPU
    else:
        status = PASS
    rec = {
        'experiment': 'Exp073CM', 'task': 'Wm_S3',
        'stage': 'universal_checkpoint_eightband_direct8_resource_qualification',
        'lmax': LMAX, 'row_length': L, 'band_lo': IB_LO, 'band_hi_exclusive': IB_HI,
        'bands': list(range(IB_LO, IB_HI)), 'signature': list(SIGNATURE),
        'reference_threads': REFERENCE_THREADS, 'target_threads': TARGET_THREADS,
        'cpu_fraction_min': CPU_FRACTION_MIN, 'reference_sha256': href,
        'target_sha256': htarget, 'array_equal': array_equal, 'sha_equal': href == htarget,
        'target_swap_increase_kib': target_swap, 'target_cpu_fraction_of_8': cpu_fraction,
        'cpu_target_met': cpu_target_met, 'status': status,
        'verified_delta': 0.0, 'draft_data_delta': 0.0, 'no_tolerance_rescue': True,
    }
    write_json(out_json, rec)
    if status != PASS:
        raise SystemExit(42)


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='mode', required=True)
    for mode in ('reference', 'target'):
        p = sub.add_parser(mode)
        p.add_argument('--pcl-npy', required=True); p.add_argument('--ca-so', required=True)
        p.add_argument('--out-npy', required=True); p.add_argument('--out-json', required=True)
    p = sub.add_parser('final')
    p.add_argument('--reference-npy', required=True); p.add_argument('--target-npy', required=True)
    p.add_argument('--reference-json', required=True); p.add_argument('--target-json', required=True)
    p.add_argument('--out-json', required=True)
    a = ap.parse_args()
    if a.mode in ('reference', 'target'):
        run_stage(a.mode, a.pcl_npy, a.ca_so, a.out_npy, a.out_json)
    else:
        final_stage(a.reference_npy, a.target_npy, a.reference_json, a.target_json, a.out_json)


if __name__ == '__main__':
    main()
