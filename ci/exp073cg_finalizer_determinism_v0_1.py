#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import glob
import hashlib
import io
import json
import os
import pathlib
import platform
import subprocess
import sys
from typing import Any

import numpy as np

EXPECTED_A_SHA = "963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd"
EXPECTED_SHAPE = (39, 12288)


def canon(x: np.ndarray) -> np.ndarray:
    return np.ascontiguousarray(x, dtype="<f8")


def ahash(x: np.ndarray) -> str:
    y = canon(x)
    return hashlib.sha256(memoryview(y).cast("B")).hexdigest()


def find_compact(path: pathlib.Path) -> pathlib.Path:
    if path.is_file():
        return path
    hits = [pathlib.Path(p) for p in glob.glob(str(path / "**" / "*compact_a_v0_1.npz"), recursive=True)]
    if len(hits) != 1:
        raise AssertionError(("compact_hits", [str(x) for x in hits]))
    return hits[0]


def load_a(path: pathlib.Path) -> tuple[pathlib.Path, np.ndarray]:
    p = find_compact(path)
    with np.load(p, allow_pickle=False) as z:
        if "A" not in z.files:
            raise AssertionError(("missing_A", z.files))
        a = canon(z["A"])
    if a.shape != EXPECTED_SHAPE:
        raise AssertionError(("shape", a.shape))
    if not np.isfinite(a).all():
        raise AssertionError("nonfinite_A")
    h = ahash(a)
    if h != EXPECTED_A_SHA:
        raise AssertionError(("compact_sha", h, EXPECTED_A_SHA))
    return p, a


def source_k_from_a(a: np.ndarray) -> np.ndarray:
    # Import the frozen production implementation rather than reimplementing it.
    from exp073az_article3_low_memory_general_coupling_v0_1 import k_from_a
    return canon(k_from_a(a))


def solve_once(a: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    k = source_k_from_a(a)
    if k.shape != (39, 39) or not np.isfinite(k).all():
        raise AssertionError(("K", k.shape, bool(np.isfinite(k).all())))
    w = canon(np.linalg.solve(k, a))
    if w.shape != EXPECTED_SHAPE or not np.isfinite(w).all():
        raise AssertionError(("W", w.shape, bool(np.isfinite(w).all())))
    return k, w


def capture_stdout(fn) -> str:
    s = io.StringIO()
    try:
        with contextlib.redirect_stdout(s):
            fn()
    except Exception as e:  # diagnostic metadata must not hide the main exact test
        return f"ERROR:{type(e).__name__}:{e}"
    return s.getvalue()


def runtime_metadata() -> dict[str, Any]:
    try:
        lscpu = subprocess.run(["lscpu"], check=False, text=True, capture_output=True, timeout=30).stdout
    except Exception as e:
        lscpu = f"ERROR:{type(e).__name__}:{e}"
    cpu_model = None
    try:
        for line in pathlib.Path("/proc/cpuinfo").read_text(errors="replace").splitlines():
            if line.lower().startswith("model name"):
                cpu_model = line.split(":", 1)[1].strip()
                break
    except Exception:
        pass
    show_runtime = getattr(np, "show_runtime", None)
    return {
        "python": sys.version,
        "numpy": np.__version__,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_model": cpu_model,
        "lscpu": lscpu,
        "numpy_config": capture_stdout(np.__config__.show),
        "numpy_runtime": capture_stdout(show_runtime) if show_runtime else "UNAVAILABLE",
        "env": {k: os.environ.get(k) for k in [
            "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS", "OMP_DYNAMIC",
            "OPENBLAS_VERBOSE"
        ]},
    }


def child_record(compact: pathlib.Path) -> dict[str, Any]:
    _, a = load_a(compact)
    k, w = solve_once(a)
    return {
        "compact_sha": ahash(a),
        "k_sha": ahash(k),
        "w_sha": ahash(w),
        "norm_min": float(np.min(np.sum(np.abs(w), axis=1))),
    }


def cmd_child(args: argparse.Namespace) -> None:
    print(json.dumps(child_record(pathlib.Path(args.compact)), sort_keys=True))


def cmd_worker(args: argparse.Namespace) -> None:
    out = pathlib.Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    compact, a = load_a(pathlib.Path(args.compact))

    k = source_k_from_a(a)
    k_sha = ahash(k)
    same_ws = [canon(np.linalg.solve(k, a)) for _ in range(3)]
    same_shas = [ahash(w) for w in same_ws]
    same_exact = all(np.array_equal(same_ws[0], w) for w in same_ws[1:]) and len(set(same_shas)) == 1

    child_records = []
    for _ in range(3):
        cp = subprocess.run(
            [sys.executable, str(pathlib.Path(__file__).resolve()), "child", "--compact", str(compact)],
            check=True, text=True, capture_output=True,
            env=os.environ.copy(), timeout=600,
        )
        lines = [x.strip() for x in cp.stdout.splitlines() if x.strip().startswith("{")]
        if len(lines) != 1:
            raise AssertionError(("child_stdout", cp.stdout, cp.stderr))
        child_records.append(json.loads(lines[0]))

    child_k_same = all(x["k_sha"] == k_sha for x in child_records)
    child_w_same = all(x["w_sha"] == same_shas[0] for x in child_records)
    fresh_process_exact = child_k_same and child_w_same

    np.save(out / f"exp073cg_worker_{args.worker}_K.npy", k, allow_pickle=False)
    np.save(out / f"exp073cg_worker_{args.worker}_window.npy", same_ws[0], allow_pickle=False)

    rec = {
        "experiment": "Exp073CG",
        "version": "v0_1",
        "stage": "hosted_worker_finalizer_determinism",
        "worker": args.worker,
        "input_artifact_id": 9841348367,
        "input_compact_path": str(compact),
        "compact_shape": list(a.shape),
        "compact_sha": ahash(a),
        "k_shape": list(k.shape),
        "k_sha": k_sha,
        "same_process_w_shas": same_shas,
        "same_process_exact": bool(same_exact),
        "fresh_process_records": child_records,
        "fresh_process_exact": bool(fresh_process_exact),
        "reference_w_sha": same_shas[0],
        "reference_norm_min": float(np.min(np.sum(np.abs(same_ws[0]), axis=1))),
        "runtime": runtime_metadata(),
        "no_tolerance_used": True,
        "scientific_authority": False,
        "readiness_delta": [0, 0],
    }
    (out / f"exp073cg_worker_{args.worker}_v0_1.json").write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: rec[k] for k in ["worker", "compact_sha", "k_sha", "same_process_exact", "fresh_process_exact", "reference_w_sha"]}, indent=2, sort_keys=True))


def pair_metrics(a: np.ndarray, b: np.ndarray) -> dict[str, Any]:
    d = np.abs(a - b)
    nz = d > 0
    scale = np.maximum(np.abs(a), np.abs(b))
    rel = np.divide(d, scale, out=np.zeros_like(d), where=scale > 0)
    return {
        "differing_count": int(np.count_nonzero(nz)),
        "total_count": int(d.size),
        "max_abs": float(np.max(d)),
        "mean_abs": float(np.mean(d)),
        "median_nonzero_abs": float(np.median(d[nz])) if np.any(nz) else 0.0,
        "max_rel": float(np.max(rel)),
        "median_nonzero_rel": float(np.median(rel[nz])) if np.any(nz) else 0.0,
    }


def cmd_compare(args: argparse.Namespace) -> None:
    root = pathlib.Path(args.root)
    js = sorted(root.rglob("exp073cg_worker_*_v0_1.json"))
    if len(js) != 4:
        raise AssertionError(("worker_json_count", len(js), [str(x) for x in js]))
    recs = [json.loads(p.read_text()) for p in js]
    by = {r["worker"]: r for r in recs}
    if set(by) != {"R1", "R2", "R3", "R4"}:
        raise AssertionError(("workers", sorted(by)))

    k_shas = {w: by[w]["k_sha"] for w in sorted(by)}
    w_shas = {w: by[w]["reference_w_sha"] for w in sorted(by)}
    k_cross_exact = len(set(k_shas.values())) == 1
    within_exact = all(by[w]["same_process_exact"] and by[w]["fresh_process_exact"] for w in by)

    arrays = {}
    for w in sorted(by):
        hits = list(root.rglob(f"exp073cg_worker_{w}_window.npy"))
        if len(hits) != 1:
            raise AssertionError((w, hits))
        arrays[w] = canon(np.load(hits[0], allow_pickle=False))
        if ahash(arrays[w]) != w_shas[w]:
            raise AssertionError(("saved_window_sha", w))
    ref = arrays["R1"]
    cross_array_equal = {w: bool(np.array_equal(ref, arrays[w])) for w in sorted(arrays)}
    w_cross_exact = len(set(w_shas.values())) == 1 and all(cross_array_equal.values())

    if not k_cross_exact:
        token = "EXP073CG_DIAG_K_CONSTRUCTION_NONDETERMINISM"
    elif not within_exact:
        token = "EXP073CG_DIAG_WITHIN_WORKER_SOLVE_NONDETERMINISM"
    elif not w_cross_exact:
        token = "EXP073CG_DIAG_CROSS_HOST_SOLVE_NONDETERMINISM_REPRODUCED"
    else:
        token = "EXP073CG_DIAG_CROSS_HOST_EXACT_STABLE_NOT_REPRODUCED"

    metrics = {f"R1_vs_{w}": pair_metrics(ref, arrays[w]) for w in ["R2", "R3", "R4"]}
    out = {
        "experiment": "Exp073CG",
        "version": "v0_1",
        "stage": "aggregate_exact_determinism_diagnostic",
        "status": token,
        "workers": sorted(by),
        "k_shas": k_shas,
        "w_shas": w_shas,
        "k_cross_exact": k_cross_exact,
        "within_worker_exact": within_exact,
        "w_cross_exact": w_cross_exact,
        "cross_array_equal_to_R1": cross_array_equal,
        "descriptive_pair_metrics": metrics,
        "exp073cf_terminal_fail_preserved": True,
        "no_tolerance_used": True,
        "scientific_authority": False,
        "readiness_delta": [0, 0],
    }
    p = pathlib.Path(args.out_json)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


def main() -> None:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("child")
    p.add_argument("--compact", required=True)
    p.set_defaults(fn=cmd_child)
    p = sp.add_parser("worker")
    p.add_argument("--compact", required=True)
    p.add_argument("--worker", choices=["R1", "R2", "R3", "R4"], required=True)
    p.add_argument("--out-dir", required=True)
    p.set_defaults(fn=cmd_worker)
    p = sp.add_parser("compare")
    p.add_argument("--root", required=True)
    p.add_argument("--out-json", required=True)
    p.set_defaults(fn=cmd_compare)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
