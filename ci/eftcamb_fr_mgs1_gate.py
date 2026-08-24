#!/usr/bin/env python3
"""Hard gate for the high-precision common-baseline designer-f(R) manifold.

Thresholds in this script are intended to be frozen before the hard rerun.
B0=1e-7 is deliberately a transition-control point and is excluded from the
production manifold because it sits near the solver GR-threshold regime.
"""
from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

import numpy as np


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--glob", required=True)
    ap.add_argument("--zero-max", type=float, required=True)
    ap.add_argument("--production-min-b0", type=float, required=True)
    ap.add_argument("--production-min-response", type=float, required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    models = []
    for f in sorted(glob.glob(args.glob)):
        d = json.loads(Path(f).read_text())
        arr = np.asarray(d["r_Delta"], float)
        models.append({
            "file": f,
            "B0": float(d["B0"]),
            "max_abs": float(np.max(np.abs(arr))),
            "all_finite": bool(np.all(np.isfinite(arr))),
        })
    models.sort(key=lambda x: x["B0"])
    by = {m["B0"]: m for m in models}
    if 0.0 not in by:
        raise SystemExit("missing exact-zero model")

    failures = []
    zero = by[0.0]
    if not zero["all_finite"]:
        failures.append("exact-zero response contains non-finite values")
    if zero["max_abs"] > args.zero_max:
        failures.append(f"exact-zero max {zero['max_abs']} > {args.zero_max}")

    production = [m for m in models if m["B0"] >= args.production_min_b0]
    if not production:
        failures.append("no production B0 points found")
    for m in production:
        if not m["all_finite"]:
            failures.append(f"B0={m['B0']} has non-finite response")
        if m["max_abs"] < args.production_min_response:
            failures.append(
                f"B0={m['B0']} max response {m['max_abs']} < resolved-production floor {args.production_min_response}"
            )
    amps = [m["max_abs"] for m in production]
    if any(b <= a for a, b in zip(amps, amps[1:])):
        failures.append("production maximum response is not strictly increasing with B0")

    transition = [m for m in models if 0.0 < m["B0"] < args.production_min_b0]
    out = {
        "thresholds_frozen_before_run": {
            "zero_max_abs_r_Delta": args.zero_max,
            "production_min_B0": args.production_min_b0,
            "production_min_max_abs_response": args.production_min_response,
            "production_max_response_must_increase_with_B0": True,
        },
        "models": models,
        "production_models": production,
        "transition_controls_excluded_from_production_gate": transition,
        "pass": not failures,
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
