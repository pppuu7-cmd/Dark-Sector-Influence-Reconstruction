#!/usr/bin/env python3
"""Reusable 8-core dynamic complete-band scheduler for DSIR heavy jobs.

Engineering-only orchestration layer. It does not alter scientific arithmetic.
Tasks are complete independent band ids. The worker callable is supplied by the
experiment driver and must preserve the experiment's frozen per-band math.
"""

from __future__ import annotations

import concurrent.futures as cf
import os
import time
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Sequence, Tuple, TypeVar

T = TypeVar("T")

INNER_THREAD_ENV = {
    "OMP_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
    "VECLIB_MAXIMUM_THREADS": "1",
}


@dataclass(frozen=True)
class BandResult:
    band_id: int
    payload: object
    wall_seconds: float


def pin_inner_thread_pools() -> None:
    for key, value in INNER_THREAD_ENV.items():
        os.environ[key] = value


def _timed_worker(worker: Callable[[int], T], band_id: int) -> BandResult:
    pin_inner_thread_pools()
    t0 = time.perf_counter()
    payload = worker(band_id)
    return BandResult(band_id=band_id, payload=payload, wall_seconds=time.perf_counter() - t0)


def run_dynamic_bands(
    band_ids: Sequence[int],
    worker: Callable[[int], T],
    *,
    max_workers: int = 8,
) -> Tuple[List[BandResult], float]:
    """Run complete bands dynamically on exactly ``max_workers`` processes.

    Results are returned sorted by band id so completion order cannot affect
    canonical assembly.  A worker exception fails closed and cancels pending
    futures where possible.
    """
    if max_workers != 8:
        raise ValueError("DSIR 8-core standard requires max_workers=8")
    visible = os.cpu_count() or 0
    if visible != 8:
        raise RuntimeError(f"Expected exactly 8 visible CPUs, found {visible}")
    if not band_ids:
        raise ValueError("band_ids must be non-empty")
    if len(set(band_ids)) != len(band_ids):
        raise ValueError("band_ids must be unique")

    pin_inner_thread_pools()
    t0 = time.perf_counter()
    completed: List[BandResult] = []
    with cf.ProcessPoolExecutor(max_workers=max_workers) as pool:
        futures: Dict[cf.Future, int] = {
            pool.submit(_timed_worker, worker, int(band_id)): int(band_id)
            for band_id in band_ids
        }
        try:
            for future in cf.as_completed(futures):
                result = future.result()
                if result.band_id != futures[future]:
                    raise RuntimeError("Worker returned mismatched band id")
                completed.append(result)
        except BaseException:
            for future in futures:
                future.cancel()
            raise
    wall = time.perf_counter() - t0
    completed.sort(key=lambda x: x.band_id)
    return completed, wall


def effective_core_fraction(sum_worker_cpu_or_wall: float, wall_seconds: float, workers: int = 8) -> float:
    if workers != 8:
        raise ValueError("DSIR 8-core standard requires workers=8")
    if wall_seconds <= 0:
        raise ValueError("wall_seconds must be positive")
    return float(sum_worker_cpu_or_wall) / (float(workers) * float(wall_seconds))
