#!/usr/bin/env python3
"""Exp073CN resource-only 8-core dynamic complete-band driver v0.1.

This driver intentionally reuses the frozen Exp073CM per-band arithmetic helper
instead of reimplementing scientific math.  It changes orchestration only:
complete bands are scheduled dynamically across eight outer processes with
inner numerical thread pools pinned to one thread.

The authoritative workflow supplies the frozen Wm_S3 inputs/checkpoint contract.
This module fails closed if the expected CM helper surface cannot be imported.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import pathlib
import resource
import sys
import time
from dataclasses import asdict
from typing import Any, Dict, Iterable, List

import numpy as np

from dsir_8core_band_scheduler_v0_1 import pin_inner_thread_pools, run_dynamic_bands

ROOT = pathlib.Path(__file__).resolve().parents[1]
CM = ROOT / "ci" / "exp073cm_checkpointed_wm_s3_resource_v0_1.py"


def _load_cm_module():
    if not CM.exists():
        raise RuntimeError(f"Missing frozen Exp073CM helper: {CM}")
    spec = importlib.util.spec_from_file_location("exp073cm_frozen", CM)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load frozen Exp073CM helper")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def canonical_sha(arr: np.ndarray) -> str:
    x = np.ascontiguousarray(arr, dtype="<f8")
    return hashlib.sha256(x.tobytes(order="C")).hexdigest()


def swap_kib() -> int:
    try:
        data = pathlib.Path("/proc/meminfo").read_text()
        values = {}
        for line in data.splitlines():
            key, rest = line.split(":", 1)
            values[key] = int(rest.strip().split()[0])
        return values.get("SwapTotal", 0) - values.get("SwapFree", 0)
    except Exception:
        return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, help="Frozen Exp073CN JSON contract")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    pin_inner_thread_pools()
    if (os.cpu_count() or 0) != 8:
        raise RuntimeError(f"Expected exactly 8 visible CPUs, got {os.cpu_count()}")

    contract_path = pathlib.Path(args.contract)
    contract = json.loads(contract_path.read_text())
    band_ids = [int(x) for x in contract["band_ids"]]
    if len(band_ids) < 16:
        raise RuntimeError("Resource gate requires enough complete bands for steady-state scheduling")
    if len(set(band_ids)) != len(band_ids):
        raise RuntimeError("Duplicate band ids in contract")
    if int(contract.get("workers", -1)) != 8:
        raise RuntimeError("Contract must freeze workers=8")
    if float(contract.get("cpu_fraction_min", -1.0)) != 0.90:
        raise RuntimeError("Contract must freeze cpu_fraction_min=0.90")

    cm = _load_cm_module()
    worker_name = contract.get("cm_band_worker")
    if not worker_name or not hasattr(cm, worker_name):
        available = sorted(name for name in dir(cm) if "band" in name.lower())
        raise RuntimeError(
            "Frozen contract names a missing Exp073CM per-band worker; "
            f"requested={worker_name!r}, band-like symbols={available}"
        )
    worker = getattr(cm, worker_name)

    swap0 = swap_kib()
    cpu0 = resource.getrusage(resource.RUSAGE_CHILDREN)
    t0 = time.perf_counter()
    results, scheduler_wall = run_dynamic_bands(band_ids, worker, max_workers=8)
    wall = time.perf_counter() - t0
    cpu1 = resource.getrusage(resource.RUSAGE_CHILDREN)
    swap1 = swap_kib()

    child_cpu = (cpu1.ru_utime + cpu1.ru_stime) - (cpu0.ru_utime + cpu0.ru_stime)
    cpu_fraction = child_cpu / (8.0 * wall) if wall > 0 else 0.0

    arrays: List[np.ndarray] = []
    per_band: List[Dict[str, Any]] = []
    for result in results:
        arr = np.asarray(result.payload, dtype="<f8")
        if not np.all(np.isfinite(arr)):
            raise RuntimeError(f"Non-finite output in band {result.band_id}")
        arrays.append(np.ascontiguousarray(arr))
        per_band.append({
            "band_id": result.band_id,
            "wall_seconds": result.wall_seconds,
            "sha256": canonical_sha(arr),
            "shape": list(arr.shape),
        })

    assembled = np.stack(arrays, axis=0)
    summary = {
        "experiment": "Exp073CN",
        "classification_scope": "resource_only_plus0_plus0",
        "workers": 8,
        "visible_cpus": os.cpu_count(),
        "band_ids": band_ids,
        "band_count": len(band_ids),
        "wall_seconds": wall,
        "scheduler_wall_seconds": scheduler_wall,
        "child_cpu_seconds": child_cpu,
        "cpu_fraction": cpu_fraction,
        "cpu_fraction_min": 0.90,
        "swap_increase_kib": max(0, swap1 - swap0),
        "finite": bool(np.all(np.isfinite(assembled))),
        "assembled_shape": list(assembled.shape),
        "assembled_sha256": canonical_sha(assembled),
        "per_band": per_band,
    }
    summary["resource_cpu_pass"] = bool(cpu_fraction >= 0.90)
    summary["resource_swap_pass"] = bool(summary["swap_increase_kib"] == 0)

    out = pathlib.Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))

    if summary["resource_cpu_pass"] and summary["resource_swap_pass"] and summary["finite"]:
        print("PASS_EXP073CN_WM_S3_8CORE_RESOURCE_V0_1")
        return 0
    print("FAIL_EXP073CN_WM_S3_8CORE_RESOURCE_V0_1")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
