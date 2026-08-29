#!/usr/bin/env python3
"""Fail-closed byte-identity guard for the frozen Exp073P v0.2 production route.

This guard is operational/reproducibility hardening only. It does not evaluate
physical support, covariance, nuisance tangents, quotient/null controls, or G8.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from pathlib import Path

FROZEN = {
    ".github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-2.yml":
        "e29eec8f9459cd361c707265ae858f843f6cf5537d32ac9c5a7a0c9652996307",
    "ci/exp073p_aggregate_prerequisite_join_v0_2.py":
        "5a17f622a4025eec82541688bded4bfedd3b6b96bc511f7d1a3327e886161cfd",
    "ci/exp073p_actions_metadata_bundle_v0_2.py":
        "aec7215a3b8cce8b1383f4cd8e49c37b22388ac6318088a3df794c8ecbd77810",
    "experiments/073p_aggregate_prerequisite_join_superseding_r1_authority_prereg_v0_2.md":
        "601f904200d72ebf5d483c973a92261eebd38b065a909220ccd8c6b86c46ad76",
}

PASS = "PASS_EXP073P_V02_ROUTE_BYTEFREEZE_GUARD"
REJECTED = "REJECTED_EXP073P_V02_ROUTE_BYTEFREEZE_GUARD"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def evaluate(root: Path) -> dict:
    rows = {}
    ok = True
    for rel, expected in FROZEN.items():
        path = root / rel
        exists = path.is_file()
        actual = sha256(path) if exists else None
        match = exists and actual == expected
        rows[rel] = {"expected_sha256": expected, "actual_sha256": actual, "match": match}
        ok &= match
    return {
        "schema": "dsir.exp073p.v02-route-bytefreeze-guard.v0.1",
        "status": PASS if ok else REJECTED,
        "scientific_classification": None,
        "frozen_files": rows,
        "support_executor_authorized": False,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "covariance_read": False,
        "whitening_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "heldout_read": False,
        "G8_read": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

def selftest(root: Path) -> dict:
    baseline = evaluate(root)
    assert baseline["status"] == PASS, baseline
    rejected = 0
    for rel in FROZEN:
        with tempfile.TemporaryDirectory() as td:
            troot = Path(td)
            for rel2 in FROZEN:
                dst = troot / rel2
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes((root / rel2).read_bytes())
            with (troot / rel).open("ab") as f:
                f.write(b"\n# BYTEFREEZE_MUTATION\n")
            out = evaluate(troot)
            assert out["status"] == REJECTED, (rel, out)
            rejected += 1
    baseline["synthetic"] = True
    baseline["mutations_rejected"] = rejected
    baseline["status"] = "PASS_EXP073P_V02_ROUTE_BYTEFREEZE_GUARD_SELFTEST"
    return baseline

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("."))
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    out = selftest(args.root) if args.selftest else evaluate(args.root)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(out["status"])
    if not args.selftest and out["status"] != PASS:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
