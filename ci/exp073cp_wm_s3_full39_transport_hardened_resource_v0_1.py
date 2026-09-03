#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

import numpy as np
import exp073cn_wm_s3_8worker_checkpoint_resource_v0_1 as cn

L = cn.L
EDGES = cn.EDGES
BANDS = tuple(range(39))
OUTER_WORKERS = 8
CPU_FRACTION_MIN = 0.90
PREREG_COMMIT = '451e947d44b325b1089441a0a62c24b1dcdeba5e'
POLICY_COMMIT = cn.POLICY_COMMIT
CN_DRIVER_COMMIT = '6cd0016d061df0156ef64b705fee339c55d5ed9f'
SYNC_V03_COMMIT = 'c20127b6762c6fc9b21875a321aecd7a4cd5f88e'
UPSTREAM_CM_HEAD = cn.UPSTREAM_CM_HEAD
UPSTREAM_CM_FINGERPRINT = cn.UPSTREAM_CM_FINGERPRINT
PCL_SHA = cn.PCL_SHA
REFERENCE_SHA = cn.REFERENCE_SHA
PASS = 'PASS_EXP073CP_WM_S3_FULL39_8WORKER_TRANSPORT_HARDENED_RESOURCE_V0_1'
FAIL_EXACT = 'FAIL_EXP073CP_WM_S3_FULL39_EXACT_EQUIVALENCE_V0_1'
FAIL_SWAP = 'FAIL_EXP073CP_WM_S3_FULL39_SWAP_SAFETY_V0_1'
FAIL_CPU = 'FAIL_EXP073CP_WM_S3_FULL39_CPU_TARGET_V0_1'


def canon(x): return np.ascontiguousarray(np.asarray(x, dtype='<f8'))
def chash(x):
    a = canon(x)
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()
def jhash(obj): return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
def atomic_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    os.replace(tmp, path)


def exact_array(path: Path, shape, label):
    a = np.load(path, allow_pickle=False)
    if a.dtype.str != '<f8' or not a.flags.c_contiguous or tuple(a.shape) != tuple(shape) or not np.all(np.isfinite(a)):
        raise RuntimeError(f'{label}: invalid canonical payload')
    return a


def contract(source_head: str, driver_commit: str):
    d = {
        'format': 'DSIR_UNIVERSAL_SELF_HOSTED_CHECKPOINT_V0_1',
        'experiment': 'Exp073CP', 'version': 'v0.1', 'task': 'Wm_S3',
        'source_head': source_head, 'driver_commit': driver_commit,
        'prereg_commit': PREREG_COMMIT, 'policy_commit': POLICY_COMMIT,
        'cn_worker_lineage_commit': CN_DRIVER_COMMIT,
        'checkpoint_sync_v0_3_commit': SYNC_V03_COMMIT,
        'checkpoint_namespace': 'checkpoints/exp073cp-wm-s3-full39-resource-v0-1',
        'source_bin': 3, 'signature': [0, 2, 0, 2], 'lmax': L - 1, 'row_length': L,
        'bands': list(BANDS), 'outer_workers': 8, 'max_inflight_futures': 8, 'nested_threads': 1,
        'cpu_fraction_min': CPU_FRACTION_MIN, 'dtype': '<f8',
        'upstream_cm_checkpoint_head': UPSTREAM_CM_HEAD,
        'upstream_cm_contract_fingerprint': UPSTREAM_CM_FINGERPRINT,
        'pcl_sha256': PCL_SHA, 'reference_sha256': REFERENCE_SHA,
        'checkpoint_boundary': 'complete_upstream_import_or_exact_remote_admitted_complete_band_or_telemetry_or_final_only',
        'scheduler': 'bounded_dynamic_process_pool_refill_before_band_remote_postcheck_abort_on_exhausted_transport',
        'cpu_metric': 'sum_worker_numerical_cpu_seconds_div_earliest_start_to_latest_end_full39',
        'transport_metric': 'separate_end_to_end_checkpoint_push_latency_and_recovered_transport_events',
        'verified_delta': 0.0, 'draft_data_delta': 0.0,
    }
    d['fingerprint'] = jhash(d)
    return d


def load_contract(root: Path):
    c = json.loads((root / 'contract.json').read_text())
    fp = c.get('fingerprint'); x = dict(c); x.pop('fingerprint', None)
    if fp != jhash(x): raise RuntimeError('contract fingerprint mismatch')
    return c


def init(root: Path, source_head: str, driver_commit: str):
    root.mkdir(parents=True, exist_ok=True)
    want = contract(source_head, driver_commit); p = root / 'contract.json'
    if p.exists() and json.loads(p.read_text()) != want: raise RuntimeError('checkpoint contract mismatch; fail closed')
    if not p.exists(): atomic_json(p, want)
    print(want['fingerprint'], flush=True)


def import_upstream(root: Path, cm: Path):
    c = load_contract(root); pcl, ref = cn.validate_cm(cm); d = root / 'upstream'; d.mkdir(parents=True, exist_ok=True)
    np.save(d / 'pcl.npy', canon(pcl), allow_pickle=False); np.save(d / 'reference_0_7.npy', canon(ref), allow_pickle=False)
    rec = {
        'format': c['format'], 'experiment': 'Exp073CP', 'stage': 'upstream', 'complete': True,
        'contract_fingerprint': c['fingerprint'], 'upstream_cm_head': UPSTREAM_CM_HEAD,
        'upstream_cm_contract_fingerprint': UPSTREAM_CM_FINGERPRINT,
        'pcl_sha256': chash(pcl), 'reference_sha256': chash(ref), 'dtype': '<f8',
    }
    atomic_json(d / 'receipt.json', rec); print(json.dumps(rec, sort_keys=True), flush=True)


def validate_upstream(root: Path):
    c = load_contract(root); d = root / 'upstream'; r = json.loads((d / 'receipt.json').read_text())
    if r.get('complete') is not True or r.get('contract_fingerprint') != c['fingerprint']: raise RuntimeError('upstream receipt mismatch')
    pcl = exact_array(d / 'pcl.npy', (L,), 'PCL'); ref = exact_array(d / 'reference_0_7.npy', (8, L), 'reference')
    if chash(pcl) != PCL_SHA or chash(ref) != REFERENCE_SHA: raise RuntimeError('upstream SHA mismatch')
    return pcl, ref


def band_dir(root: Path, b: int): return root / 'bands' / f'band_{b:02d}'
def load_band(root: Path, b: int):
    c = load_contract(root); d = band_dir(root, b); p = d / 'receipt.json'
    if not p.exists(): return None
    r = json.loads(p.read_text()); a = exact_array(d / 'payload.npy', (L,), f'band {b}')
    if r.get('complete') is not True or r.get('contract_fingerprint') != c['fingerprint'] or r.get('band') != b or r.get('payload_sha256') != chash(a):
        raise RuntimeError(f'band {b}: checkpoint mismatch')
    if r.get('ell_interval') != [int(EDGES[b]), int(EDGES[b + 1])]: raise RuntimeError(f'band {b}: ell interval mismatch')
    return r


def store_band(root: Path, b: int, a: np.ndarray, tel: dict):
    c = load_contract(root); d = band_dir(root, b); d.mkdir(parents=True, exist_ok=True); a = canon(a)
    np.save(d / 'payload.npy', a, allow_pickle=False)
    r = {
        'format': c['format'], 'experiment': 'Exp073CP', 'task': 'Wm_S3', 'stage': 'band', 'complete': True,
        'contract_fingerprint': c['fingerprint'], 'band': b,
        'ell_interval': [int(EDGES[b]), int(EDGES[b + 1])], 'shape': [L], 'dtype': '<f8',
        'payload_sha256': chash(a), 'pcl_sha256': PCL_SHA, 'outer_workers': 8, 'nested_threads': 1, **tel,
    }
    atomic_json(d / 'receipt.json', r)
    return r


def swap_used_kib():
    vals = {}
    for line in Path('/proc/meminfo').read_text().splitlines():
        if ':' in line:
            k, v = line.split(':', 1); q = v.strip().split()
            if q and q[0].isdigit(): vals[k] = int(q[0])
    return max(0, vals.get('SwapTotal', 0) - vals.get('SwapFree', 0))


def sync(root: Path, branch: str, script: Path, label: str):
    t0 = time.monotonic()
    p = subprocess.run(['bash', str(script), 'push', str(root), branch, label], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    dt = time.monotonic() - t0
    out = p.stdout or ''
    if out: print(out, end='' if out.endswith('\n') else '\n', flush=True)
    recovered = out.count('UNKNOWN_TRANSPORT_FAILURE')
    push_attempts = [int(x) for x in re.findall(r'push_attempt=(\d+)', out)]
    extra_push_attempts = max(push_attempts, default=1) - 1
    if p.returncode != 0:
        raise subprocess.CalledProcessError(p.returncode, p.args, output=out)
    return {'wall_seconds': dt, 'recovered_transport_events': recovered, 'extra_push_attempts': max(0, extra_push_attempts)}


def timed_worker(b: int, pcl_path: str, ca_so: str):
    start_ns = time.time_ns(); b, a, tel = cn.worker(b, pcl_path, ca_so); end_ns = time.time_ns()
    tel = dict(tel); tel['numerical_start_epoch_ns'] = start_ns; tel['numerical_end_epoch_ns'] = end_ns
    return b, a, tel


def abort_executor(ex: cf.ProcessPoolExecutor, futures):
    for fut in list(futures): fut.cancel()
    procs = list(getattr(ex, '_processes', {}).values())
    ex.shutdown(wait=False, cancel_futures=True)
    for p in procs:
        try:
            if p.is_alive(): p.terminate()
        except Exception: pass
    for p in procs:
        try:
            p.join(timeout=5)
            if p.is_alive() and hasattr(p, 'kill'): p.kill()
        except Exception: pass


def compute(root: Path, ca_so: Path, branch: str, sync_script: Path):
    validate_upstream(root)
    for b in BANDS: load_band(root, b)
    missing = [b for b in BANDS if load_band(root, b) is None]
    if not missing:
        print('all bands already checkpointed; no compute', flush=True)
        return
    swap0 = swap_used_kib(); wall0 = time.monotonic(); transport = 0.0; recovered_events = 0; extra_push_attempts = 0
    worker_tels = []; admitted = []; todo = iter(missing)
    ex = cf.ProcessPoolExecutor(max_workers=OUTER_WORKERS); futs = {}

    def submit_one():
        try: b = next(todo)
        except StopIteration: return False
        futs[ex.submit(timed_worker, b, str(root / 'upstream/pcl.npy'), str(ca_so))] = b
        return True

    for _ in range(min(OUTER_WORKERS, len(missing))): submit_one()
    try:
        while futs:
            done, _ = cf.wait(tuple(futs), return_when=cf.FIRST_COMPLETED)
            for fut in done:
                expected_b = futs.pop(fut)
                b, a, tel = fut.result()
                if b != expected_b: raise RuntimeError(f'worker band identity mismatch expected={expected_b} got={b}')
                store_band(root, b, a, tel)
                # Refill before remote durability so at most eight numerical tasks remain in flight without an unbounded backlog.
                submit_one()
                s = sync(root, branch, sync_script, f'band-{b:02d}-complete')
                transport += float(s['wall_seconds']); recovered_events += int(s['recovered_transport_events']); extra_push_attempts += int(s['extra_push_attempts'])
                worker_tels.append(tel); admitted.append(b)
    except BaseException:
        abort_executor(ex, futs)
        raise
    else:
        ex.shutdown(wait=True)

    wall = time.monotonic() - wall0; swap1 = swap_used_kib()
    if sorted(admitted) != sorted(missing): raise RuntimeError('not all missing bands durably admitted')
    starts = [int(t['numerical_start_epoch_ns']) for t in worker_tels]; ends = [int(t['numerical_end_epoch_ns']) for t in worker_tels]
    cpus = [float(t['worker_cpu_seconds']) for t in worker_tels]
    active_span = (max(ends) - min(starts)) / 1e9 if starts else 0.0; cpu_sum = sum(cpus); eff = cpu_sum / active_span if active_span > 0 else 0.0
    seg = {
        'bands_completed': sorted(admitted), 'compute_active_wall_seconds': active_span,
        'sum_worker_numerical_cpu_seconds': cpu_sum, 'compute_active_effective_cores': eff,
        'cpu_fraction_of_8_compute': eff / 8.0, 'end_to_end_wall_seconds': wall,
        'checkpoint_transport_wall_seconds': transport, 'checkpoint_push_count': len(admitted),
        'recovered_transport_events': recovered_events, 'extra_push_attempts': extra_push_attempts,
        'swap_used_kib_before': swap0, 'swap_used_kib_after': swap1, 'swap_increase_kib': max(0, swap1 - swap0),
    }
    atomic_json(root / 'telemetry' / 'full39.json', seg)
    s = sync(root, branch, sync_script, 'full39-telemetry')
    seg['telemetry_checkpoint_wall_seconds'] = float(s['wall_seconds'])
    seg['recovered_transport_events'] += int(s['recovered_transport_events']); seg['extra_push_attempts'] += int(s['extra_push_attempts'])
    atomic_json(root / 'telemetry' / 'full39.json', seg)
    print(json.dumps(seg, sort_keys=True), flush=True)


def finalize(root: Path):
    c = load_contract(root); _, ref = validate_upstream(root); rows = []
    for b in BANDS:
        load_band(root, b); rows.append(exact_array(band_dir(root, b) / 'payload.npy', (L,), f'band {b}'))
    target = canon(np.stack(rows)); first8 = canon(target[:8])
    exact = bool(np.array_equal(first8, ref)) and chash(first8) == REFERENCE_SHA
    t = json.loads((root / 'telemetry' / 'full39.json').read_text()); cpu = float(t['cpu_fraction_of_8_compute']); swap = int(t['swap_increase_kib'])
    if not exact: status = FAIL_EXACT
    elif swap > 0: status = FAIL_SWAP
    elif cpu < CPU_FRACTION_MIN: status = FAIL_CPU
    else: status = PASS
    rec = {
        'format': c['format'], 'experiment': 'Exp073CP', 'task': 'Wm_S3', 'stage': 'final', 'complete': True,
        'contract_fingerprint': c['fingerprint'], 'target_shape': [39, L], 'dtype': '<f8',
        'array_equal_reference_0_7': bool(np.array_equal(first8, ref)), 'first8_sha256': chash(first8),
        'reference_sha256': REFERENCE_SHA, 'sha_equal_reference_0_7': chash(first8) == REFERENCE_SHA,
        'cpu_fraction_of_8_compute': cpu, 'cpu_fraction_min': CPU_FRACTION_MIN, 'swap_increase_kib': swap,
        'status': status, 'verified_delta': 0.0, 'draft_data_delta': 0.0, 'no_tolerance_rescue': True,
    }
    atomic_json(root / 'final' / 'receipt.json', rec); print(json.dumps(rec, indent=2, sort_keys=True), flush=True)
    return 0 if status == PASS else 42


def validate(root: Path):
    validate_upstream(root); missing = []
    for b in BANDS:
        if load_band(root, b) is None: missing.append(b)
    print(json.dumps({'missing_bands': missing, 'complete_bands': 39 - len(missing)}, sort_keys=True), flush=True)
    return 0 if not missing else 1


def main():
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest='cmd', required=True)
    p = sp.add_parser('init'); p.add_argument('--checkpoint-dir', required=True); p.add_argument('--source-head', required=True); p.add_argument('--driver-commit', required=True)
    p = sp.add_parser('import-upstream'); p.add_argument('--checkpoint-dir', required=True); p.add_argument('--cm-dir', required=True)
    p = sp.add_parser('validate'); p.add_argument('--checkpoint-dir', required=True)
    p = sp.add_parser('compute'); p.add_argument('--checkpoint-dir', required=True); p.add_argument('--ca-so', required=True); p.add_argument('--branch', required=True); p.add_argument('--sync-script', required=True)
    p = sp.add_parser('finalize'); p.add_argument('--checkpoint-dir', required=True)
    a = ap.parse_args(); root = Path(a.checkpoint_dir)
    if a.cmd == 'init': init(root, a.source_head, a.driver_commit); raise SystemExit(0)
    if a.cmd == 'import-upstream': import_upstream(root, Path(a.cm_dir)); raise SystemExit(0)
    if a.cmd == 'validate': raise SystemExit(validate(root))
    if a.cmd == 'compute': compute(root, Path(a.ca_so), a.branch, Path(a.sync_script)); raise SystemExit(0)
    if a.cmd == 'finalize': raise SystemExit(finalize(root))


if __name__ == '__main__': main()
