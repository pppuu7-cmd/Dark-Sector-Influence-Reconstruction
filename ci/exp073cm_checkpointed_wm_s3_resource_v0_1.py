#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ctypes
import hashlib
import importlib
import json
import os
import resource
import shutil
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
PREREG_COMMIT = '914a57e45ee98b6ebbb8830a524ec59bfef0c78b'
PCL_HELPER_COMMIT = '8a5f9f5e0341d24ee843f3097199075c50ab2d02'
RANGE_HELPER_COMMIT = 'fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22'
POLICY_COMMIT = 'f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427'
R1_RUN = 33270843577
R1_ARTIFACT = 'exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536'
MASK_RUN = 33683175039
MASK_ARTIFACT = 'exp073cl-exact-des-mask-9a7b1c19aa130c5b11f68c2d9ea73ff9a2f6c105'
MASK_SHA = 'a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55'

PASS = 'PASS_EXP073CM_WM_S3_EIGHTBAND_DIRECT8_RESOURCE_V0_1'
FAIL_EXACT = 'FAIL_EXP073CM_WM_S3_EIGHTBAND_DIRECT8_EXACT_EQUIVALENCE_V0_1'
FAIL_SWAP = 'FAIL_EXP073CM_WM_S3_DIRECT8_SWAP_SAFETY_V0_1'
FAIL_CPU = 'FAIL_EXP073CM_WM_S3_DIRECT8_CPU_TARGET_V0_1'


def canon(x: np.ndarray) -> np.ndarray:
    return np.ascontiguousarray(np.asarray(x, dtype='<f8'))


def chash(x: np.ndarray) -> str:
    a = canon(x)
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def jhash(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def atomic_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    os.replace(tmp, path)


def contract_dict(source_head: str, resource_helper_commit: str) -> dict:
    base = {
        'format': 'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1',
        'experiment': 'Exp073CM',
        'task': 'Wm_S3',
        'source_head': source_head,
        'prereg_commit': PREREG_COMMIT,
        'policy_commit': POLICY_COMMIT,
        'pcl_helper_commit': PCL_HELPER_COMMIT,
        'resource_helper_commit': resource_helper_commit,
        'range_helper_commit': RANGE_HELPER_COMMIT,
        'source_bin': 3,
        'signature': list(SIGNATURE),
        'lmax': LMAX,
        'row_length': L,
        'band_range': [IB_LO, IB_HI],
        'reference_threads': REFERENCE_THREADS,
        'target_threads': TARGET_THREADS,
        'cpu_fraction_min': CPU_FRACTION_MIN,
        'dtype': '<f8',
        'r1_run': R1_RUN,
        'r1_artifact': R1_ARTIFACT,
        'mask_run': MASK_RUN,
        'mask_artifact': MASK_ARTIFACT,
        'mask_sha256': MASK_SHA,
        'checkpoint_boundary': 'complete_stage_only',
    }
    base['fingerprint'] = jhash(base)
    return base


def bind_contract(root: Path, source_head: str, resource_helper_commit: str) -> dict:
    root.mkdir(parents=True, exist_ok=True)
    p = root / 'contract.json'
    expected = contract_dict(source_head, resource_helper_commit)
    if p.exists():
        got = json.loads(p.read_text(encoding='utf-8'))
        if got != expected:
            raise RuntimeError('checkpoint contract mismatch; fail closed')
    else:
        atomic_json(p, expected)
    return expected


def load_contract(root: Path) -> dict:
    p = root / 'contract.json'
    if not p.exists():
        raise RuntimeError('checkpoint contract absent')
    c = json.loads(p.read_text(encoding='utf-8'))
    fp = c.get('fingerprint')
    tmp = dict(c); tmp.pop('fingerprint', None)
    if fp != jhash(tmp):
        raise RuntimeError('checkpoint contract fingerprint invalid')
    return c


def stage_dir(root: Path, stage: str) -> Path:
    return root / 'stages' / stage


def exact_loaded_payload(path: Path, expected_shape: tuple[int, ...], stage: str) -> np.ndarray:
    a = np.load(path, allow_pickle=False)
    if a.dtype.str != '<f8':
        raise RuntimeError(f'{stage}: checkpoint dtype mismatch {a.dtype.str}')
    if not a.flags.c_contiguous:
        raise RuntimeError(f'{stage}: checkpoint not C-contiguous')
    if tuple(a.shape) != tuple(expected_shape):
        raise RuntimeError(f'{stage}: checkpoint shape mismatch {a.shape}')
    if not np.all(np.isfinite(a)):
        raise RuntimeError(f'{stage}: checkpoint non-finite payload')
    return a


def expected_final_status(ref: np.ndarray, target: np.ndarray, target_receipt: dict) -> tuple[str, dict]:
    href, ht = chash(ref), chash(target)
    array_equal = bool(np.array_equal(ref, target))
    exact = array_equal and href == ht
    finite = bool(np.all(np.isfinite(ref)) and np.all(np.isfinite(target)))
    swap_inc = int(target_receipt['swap_increase_kib'])
    resource_safe = finite and swap_inc == 0
    cpu_fraction = float(target_receipt['cpu_fraction_of_8'])
    cpu_target = cpu_fraction >= CPU_FRACTION_MIN
    if not exact: status = FAIL_EXACT
    elif not resource_safe: status = FAIL_SWAP
    elif not cpu_target: status = FAIL_CPU
    else: status = PASS
    return status, {
        'href': href, 'ht': ht, 'array_equal': array_equal, 'finite': finite,
        'swap_inc': swap_inc, 'resource_safe': resource_safe,
        'cpu_fraction': cpu_fraction, 'cpu_target': cpu_target,
    }


def load_stage(root: Path, stage: str) -> dict | None:
    c = load_contract(root)
    p = stage_dir(root, stage) / 'receipt.json'
    if not p.exists():
        return None
    r = json.loads(p.read_text(encoding='utf-8'))
    if r.get('contract_fingerprint') != c['fingerprint'] or r.get('stage') != stage or r.get('complete') is not True:
        raise RuntimeError(f'{stage}: receipt contract/stage mismatch')
    if stage in ('pcl', 'reference', 'target'):
        a_path = stage_dir(root, stage) / 'payload.npy'
        if not a_path.exists():
            raise RuntimeError(f'{stage}: payload absent')
        expected_shape = (L,) if stage == 'pcl' else (IB_HI - IB_LO, L)
        a = exact_loaded_payload(a_path, expected_shape, stage)
        if r.get('dtype') != '<f8' or r.get('shape') != list(expected_shape):
            raise RuntimeError(f'{stage}: receipt dtype/shape mismatch')
        if r.get('payload_sha256') != chash(a):
            raise RuntimeError(f'{stage}: payload SHA mismatch')
    elif stage == 'final':
        rr = load_stage(root, 'reference'); tr = load_stage(root, 'target')
        if rr is None or tr is None:
            raise RuntimeError('final: prerequisite checkpoint absent')
        ref = exact_loaded_payload(stage_dir(root, 'reference') / 'payload.npy', (IB_HI - IB_LO, L), 'reference')
        target = exact_loaded_payload(stage_dir(root, 'target') / 'payload.npy', (IB_HI - IB_LO, L), 'target')
        status, x = expected_final_status(ref, target, tr)
        checks = [
            r.get('reference_sha256') == x['href'],
            r.get('target_sha256') == x['ht'],
            r.get('array_equal') is x['array_equal'],
            r.get('sha_equal') is (x['href'] == x['ht']),
            r.get('finite') is x['finite'],
            int(r.get('swap_increase_target_kib', -1)) == x['swap_inc'],
            r.get('resource_safe') is x['resource_safe'],
            abs(float(r.get('cpu_fraction_of_8')) - x['cpu_fraction']) <= 0.0,
            r.get('cpu_target_met') is x['cpu_target'],
            r.get('status') == status,
        ]
        if not all(checks):
            raise RuntimeError('final: restored comparator receipt does not recompute exactly')
    return r


def store_array_stage(root: Path, stage: str, arr: np.ndarray, extra: dict) -> dict:
    c = load_contract(root)
    d = stage_dir(root, stage)
    d.mkdir(parents=True, exist_ok=True)
    a = canon(arr)
    tmp = d / 'payload.tmp.npy'
    np.save(tmp, a, allow_pickle=False)
    os.replace(tmp, d / 'payload.npy')
    rec = {
        'format': 'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1',
        'experiment': 'Exp073CM',
        'task': 'Wm_S3',
        'stage': stage,
        'complete': True,
        'contract_fingerprint': c['fingerprint'],
        'shape': list(a.shape),
        'dtype': '<f8',
        'payload_sha256': chash(a),
        **extra,
    }
    atomic_json(d / 'receipt.json', rec)
    return rec


def runtime_nmtlib() -> bytes:
    ext = importlib.import_module('_nmtlib')
    return str(Path(ext.__file__).resolve()).encode()


def load_ca(path: Path):
    lib = ctypes.CDLL(str(path.resolve()))
    dptr = ctypes.POINTER(ctypes.c_double)
    iptr = ctypes.POINTER(ctypes.c_int)
    f = lib.exp073ca_stream_compress_range
    f.argtypes = [ctypes.c_char_p, dptr, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                  ctypes.c_int, ctypes.c_int, iptr, ctypes.c_int, ctypes.c_int,
                  ctypes.c_int, ctypes.c_int, dptr]
    f.restype = ctypes.c_int
    return f


def call_range(f, pcl: np.ndarray, threads: int) -> np.ndarray:
    pcl = canon(pcl)
    edges = np.ascontiguousarray(EDGES, dtype=np.int32)
    out = np.zeros((IB_HI - IB_LO, L), dtype=np.float64)
    s1, s2, n1, n2 = SIGNATURE
    rc = f(runtime_nmtlib(), pcl.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
           LMAX, s1, s2, n1, n2, edges.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
           len(edges) - 1, IB_LO, IB_HI, threads,
           out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
    if rc != 0:
        raise RuntimeError(('range_helper_rc', rc, threads))
    return canon(out)


def cpu_seconds() -> float:
    r = resource.getrusage(resource.RUSAGE_SELF)
    return float(r.ru_utime + r.ru_stime)


def maxrss_kib() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def swap_used_kib() -> int:
    vals = {}
    with open('/proc/meminfo', 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                k, v = line.split(':', 1)
                p = v.strip().split()
                if p and p[0].isdigit(): vals[k] = int(p[0])
    return max(0, vals.get('SwapTotal', 0) - vals.get('SwapFree', 0))


def store_pcl(root: Path, src_npy: Path, src_json: Path) -> None:
    pcl = exact_loaded_payload(src_npy, (L,), 'fresh-pcl')
    upstream = json.loads(src_json.read_text(encoding='utf-8'))
    rec = store_array_stage(root, 'pcl', pcl, {
        'upstream_receipt': upstream,
        'checkpointed_immediately_after_atomic_pcl': True,
    })
    print(json.dumps(rec, indent=2, sort_keys=True), flush=True)


def compute(root: Path, stage: str, ca_so: Path) -> None:
    if stage not in ('reference', 'target'):
        raise ValueError(stage)
    pcl_rec = load_stage(root, 'pcl')
    if pcl_rec is None:
        raise RuntimeError('PCL checkpoint required before coupling')
    pcl = exact_loaded_payload(stage_dir(root, 'pcl') / 'payload.npy', (L,), 'pcl')
    threads = REFERENCE_THREADS if stage == 'reference' else TARGET_THREADS
    f = load_ca(ca_so)
    swap0 = swap_used_kib(); rss0 = maxrss_kib(); c0 = cpu_seconds(); t0 = time.monotonic()
    out = call_range(f, pcl, threads)
    wall = time.monotonic() - t0; cpu = cpu_seconds() - c0
    swap1 = swap_used_kib(); rss1 = maxrss_kib()
    effective = (cpu / wall) if wall > 0 else 0.0
    extra = {
        'threads': threads,
        'wall_seconds': wall,
        'process_cpu_seconds': cpu,
        'effective_cpu_cores': effective,
        'cpu_fraction_of_8': (effective / 8.0) if stage == 'target' else None,
        'swap_used_kib_before': swap0,
        'swap_used_kib_after': swap1,
        'swap_increase_kib': max(0, swap1 - swap0),
        'ru_maxrss_kib_before': rss0,
        'ru_maxrss_kib_after': rss1,
        'band_lo': IB_LO,
        'band_hi_exclusive': IB_HI,
        'signature': list(SIGNATURE),
    }
    rec = store_array_stage(root, stage, out, extra)
    print(json.dumps(rec, indent=2, sort_keys=True), flush=True)


def finalize(root: Path) -> dict:
    c = load_contract(root)
    rr = load_stage(root, 'reference'); tr = load_stage(root, 'target')
    if rr is None or tr is None:
        raise RuntimeError('reference and target checkpoints required')
    ref = exact_loaded_payload(stage_dir(root, 'reference') / 'payload.npy', (IB_HI - IB_LO, L), 'reference')
    target = exact_loaded_payload(stage_dir(root, 'target') / 'payload.npy', (IB_HI - IB_LO, L), 'target')
    status, x = expected_final_status(ref, target, tr)
    rec = {
        'format': 'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1',
        'experiment': 'Exp073CM', 'task': 'Wm_S3', 'stage': 'final', 'complete': True,
        'contract_fingerprint': c['fingerprint'], 'reference_sha256': x['href'],
        'target_sha256': x['ht'], 'array_equal': x['array_equal'],
        'sha_equal': x['href'] == x['ht'], 'finite': x['finite'],
        'swap_increase_target_kib': x['swap_inc'], 'resource_safe': x['resource_safe'],
        'cpu_fraction_of_8': x['cpu_fraction'], 'cpu_fraction_min': CPU_FRACTION_MIN,
        'cpu_target_met': x['cpu_target'], 'reference_wall_seconds': rr['wall_seconds'],
        'target_wall_seconds': tr['wall_seconds'],
        'speedup_diagnostic_only': (float(rr['wall_seconds']) / float(tr['wall_seconds'])) if float(tr['wall_seconds']) > 0 else None,
        'status': status, 'verified_delta': 0.0, 'draft_data_delta': 0.0,
        'no_tolerance_rescue': True,
    }
    atomic_json(stage_dir(root, 'final') / 'receipt.json', rec)
    print(json.dumps(rec, indent=2, sort_keys=True), flush=True)
    return rec


def export_all(root: Path, out_dir: Path) -> None:
    for stage in ('pcl', 'reference', 'target', 'final'):
        r = load_stage(root, stage)
        if r is None:
            raise RuntimeError(f'cannot export absent stage {stage}')
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / 'contract.json', out_dir / 'exp073cm_checkpoint_contract_v0_1.json')
    for stage in ('pcl', 'reference', 'target', 'final'):
        d = stage_dir(root, stage)
        shutil.copy2(d / 'receipt.json', out_dir / f'exp073cm_{stage}_receipt_v0_1.json')
        if (d / 'payload.npy').exists():
            shutil.copy2(d / 'payload.npy', out_dir / f'exp073cm_{stage}_payload_v0_1.npy')


def main() -> None:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    p = sp.add_parser('init'); p.add_argument('--checkpoint-dir', required=True); p.add_argument('--source-head', required=True); p.add_argument('--resource-helper-commit', required=True)
    p = sp.add_parser('check'); p.add_argument('--checkpoint-dir', required=True); p.add_argument('--stage', required=True, choices=['pcl','reference','target','final'])
    p = sp.add_parser('store-pcl'); p.add_argument('--checkpoint-dir', required=True); p.add_argument('--src-npy', required=True); p.add_argument('--src-json', required=True)
    p = sp.add_parser('compute'); p.add_argument('--checkpoint-dir', required=True); p.add_argument('--stage', required=True, choices=['reference','target']); p.add_argument('--ca-so', required=True)
    p = sp.add_parser('finalize'); p.add_argument('--checkpoint-dir', required=True)
    p = sp.add_parser('enforce-final'); p.add_argument('--checkpoint-dir', required=True)
    p = sp.add_parser('export'); p.add_argument('--checkpoint-dir', required=True); p.add_argument('--out-dir', required=True)
    a = ap.parse_args(); root = Path(a.checkpoint_dir)

    if a.cmd == 'init':
        c = bind_contract(root, a.source_head, a.resource_helper_commit); print(json.dumps(c, indent=2, sort_keys=True), flush=True)
    elif a.cmd == 'check':
        r = load_stage(root, a.stage)
        if r is None: raise SystemExit(3)
        print(f'CHECKPOINT stage={a.stage} valid sha={r.get("payload_sha256", "NA")}', flush=True)
    elif a.cmd == 'store-pcl': store_pcl(root, Path(a.src_npy), Path(a.src_json))
    elif a.cmd == 'compute': compute(root, a.stage, Path(a.ca_so))
    elif a.cmd == 'finalize':
        if load_stage(root, 'final') is None: finalize(root)
        else: print('CHECKPOINT stage=final valid and recomputed exactly; reuse', flush=True)
    elif a.cmd == 'enforce-final':
        r = load_stage(root, 'final')
        if r is None: raise RuntimeError('final checkpoint absent')
        print(json.dumps(r, indent=2, sort_keys=True), flush=True)
        if r.get('status') != PASS: raise SystemExit(42)
    elif a.cmd == 'export': export_all(root, Path(a.out_dir))


if __name__ == '__main__':
    main()
