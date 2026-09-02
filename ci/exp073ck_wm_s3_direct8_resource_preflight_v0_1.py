#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import resource
import time

import numpy as np

import exp073ca_checkpoint_streaming_wm_s2_v0_1 as stream

BAND_INDEX = 20
REFERENCE_THREADS = 1
TARGET_THREADS = 8
PASS = 'PASS_EXP073CK_WM_S3_DIRECT8_RESOURCE_QUALIFICATION_V0_1'
FAIL = 'FAIL_EXP073CK_WM_S3_DIRECT8_EXACT_EQUIVALENCE_V0_1'


def canon(x):
    return np.ascontiguousarray(np.asarray(x, dtype='<f8'))


def chash(x):
    return hashlib.sha256(canon(x).tobytes(order='C')).hexdigest()


def swap_used_kib():
    vals = {}
    with open('/proc/meminfo', 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                k, v = line.split(':', 1)
                parts = v.strip().split()
                if parts and parts[0].isdigit():
                    vals[k] = int(parts[0])
    return max(0, vals.get('SwapTotal', 0) - vals.get('SwapFree', 0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pcl-npy', required=True)
    ap.add_argument('--ca-so', required=True)
    ap.add_argument('--out-json', required=True)
    ap.add_argument('--out-reference-npy', required=True)
    ap.add_argument('--out-target-npy', required=True)
    a = ap.parse_args()

    pcl = canon(np.load(a.pcl_npy, allow_pickle=False))
    if pcl.shape != (stream.L,) or not np.all(np.isfinite(pcl)):
        raise AssertionError(('real_wm_s3_pcl', pcl.shape))
    f = stream.load_ca(Path(a.ca_so))
    swap0 = swap_used_kib()
    rss0 = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    t0 = time.monotonic()
    ref = stream.call_ca(f, pcl, stream.EDGES, BAND_INDEX, BAND_INDEX + 1, REFERENCE_THREADS)
    t_ref = time.monotonic() - t0
    swap1 = swap_used_kib()
    rss1 = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    t0 = time.monotonic()
    target = stream.call_ca(f, pcl, stream.EDGES, BAND_INDEX, BAND_INDEX + 1, TARGET_THREADS)
    t_target = time.monotonic() - t0
    swap2 = swap_used_kib()
    rss2 = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    href, htarget = chash(ref), chash(target)
    exact = bool(np.array_equal(ref, target)) and href == htarget
    finite = bool(np.all(np.isfinite(ref)) and np.all(np.isfinite(target)))
    swap_increase_target = max(0, swap2 - swap1)
    resource_safe = finite and swap_increase_target == 0
    ok = exact and resource_safe

    Path(a.out_reference_npy).parent.mkdir(parents=True, exist_ok=True)
    np.save(a.out_reference_npy, canon(ref), allow_pickle=False)
    np.save(a.out_target_npy, canon(target), allow_pickle=False)
    rec = {
        'experiment': 'Exp073CK',
        'task': 'Wm_S3',
        'stage': 'direct8_resource_qualification',
        'lmax': stream.LMAX,
        'row_length': stream.L,
        'band_index': BAND_INDEX,
        'ell_lo': int(stream.EDGES[BAND_INDEX]),
        'ell_hi_exclusive': int(stream.EDGES[BAND_INDEX + 1]),
        'signature': list(stream.SIGNATURE),
        'reference_threads': REFERENCE_THREADS,
        'target_threads': TARGET_THREADS,
        'reference_wall_seconds': t_ref,
        'target_wall_seconds': t_target,
        'speedup_diagnostic_only': (t_ref / t_target) if t_target > 0 else None,
        'reference_sha256': href,
        'target_sha256': htarget,
        'array_equal': bool(np.array_equal(ref, target)),
        'sha_equal': href == htarget,
        'finite': finite,
        'swap_used_kib_before_reference': swap0,
        'swap_used_kib_after_reference': swap1,
        'swap_used_kib_after_target': swap2,
        'swap_increase_target_kib': swap_increase_target,
        'ru_maxrss_kib_before': rss0,
        'ru_maxrss_kib_after_reference': rss1,
        'ru_maxrss_kib_after_target': rss2,
        'resource_safe': resource_safe,
        'status': PASS if ok else FAIL,
        'verified_delta': 0.0,
        'draft_data_delta': 0.0,
        'no_tolerance_rescue': True,
    }
    Path(a.out_json).write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(rec, indent=2, sort_keys=True), flush=True)
    if not ok:
        raise SystemExit(42)


if __name__ == '__main__':
    main()
