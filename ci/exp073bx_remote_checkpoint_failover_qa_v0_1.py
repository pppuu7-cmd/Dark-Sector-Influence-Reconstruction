#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import time

import numpy as np

from ci.dsir_remote_band_checkpoint_v0_1 import (
    BandCheckpointStore,
    CheckpointContract,
    print_progress,
)

BRANCH = "checkpoints/exp073bx-v0-1"
ROOT = pathlib.Path(".dsir_checkpoint/exp073bx-v0-1")
THREADS = 8
NBANDS = 3
ROWLEN = 64
PREREG = "5cee2e0d8ec4cc5a3e9649e7bfaa9cedce39f2b7"
CHECKPOINT_IMPL = "0b0324afb69acb16cbea97bb924b9be48f303dde"
SYNC_IMPL = "96886916b41dce7f0a40807622928c841ef5fc58"


def contract() -> CheckpointContract:
    return CheckpointContract(
        experiment="Exp073BX",
        source_commit=CHECKPOINT_IMPL,
        helper_commit=SYNC_IMPL,
        prereg_commit=PREREG,
        task="synthetic_remote_checkpoint_failover_qa",
        lmax=63,
        nbands=NBANDS,
        row_length=ROWLEN,
        threads=THREADS,
        extra={"row_formula": "band + j/1024", "branch": BRANCH},
    )


def expected_matrix() -> np.ndarray:
    j = np.arange(ROWLEN, dtype="<f8")
    return np.vstack([np.asarray(b + j / 1024.0, dtype="<f8") for b in range(NBANDS)])


def matrix_sha(a: np.ndarray) -> str:
    x = np.ascontiguousarray(np.asarray(a, dtype="<f8"))
    return hashlib.sha256(x.tobytes(order="C")).hexdigest()


def sync(mode: str, label: str = "checkpoint") -> None:
    cmd = ["bash", "ci/dsir_checkpoint_git_sync_v0_1.sh", mode, str(ROOT), BRANCH]
    if mode == "push":
        cmd.append(label)
    subprocess.run(cmd, check=True)


def home() -> None:
    # Restore makes repeat execution idempotent and exercises real resume logic.
    sync("restore")
    store = BandCheckpointStore(ROOT, contract())
    matrix, done = store.restore_matrix()
    started = time.monotonic()
    done_set = set(done)
    print_progress(store, started, THREADS)
    expected = expected_matrix()
    for b in range(NBANDS):
        if b in done_set:
            continue
        t0 = time.monotonic()
        # Small delay makes progress/ETA human-visible without wasting compute.
        time.sleep(1.0)
        row = expected[b]
        wall = time.monotonic() - t0
        store.save_completed_band(b, row, ell_lo=b * 10, ell_hi_exclusive=(b + 1) * 10, wall_seconds=wall)
        matrix[b] = row
        sync("push", f"Exp073BX band {b+1}/{NBANDS}")
        print(f"CHECKPOINT remote durable band={b+1}/{NBANDS}", flush=True)
        print_progress(store, started, THREADS)

    restored, completed = store.restore_matrix()
    if completed != list(range(NBANDS)):
        raise RuntimeError(f"home completed list mismatch: {completed}")
    if not np.array_equal(restored, expected):
        raise RuntimeError("home final exact matrix mismatch")
    receipt = {
        "experiment": "Exp073BX",
        "stage": "home",
        "status": "HOME_REMOTE_CHECKPOINTS_DURABLE",
        "completed_bands": completed,
        "matrix_sha256": matrix_sha(restored),
        "branch": BRANCH,
        "authority": False,
        "scientific_readiness_increment": 0,
        "draft_data_readiness_increment": 0,
    }
    pathlib.Path("exp073bx_home_receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True), flush=True)


def hosted() -> None:
    sync("restore")
    store = BandCheckpointStore(ROOT, contract())
    restored, completed = store.restore_matrix()
    expected = expected_matrix()
    exact = completed == list(range(NBANDS)) and np.array_equal(restored, expected)
    got_sha = matrix_sha(restored)
    expected_sha = matrix_sha(expected)
    if not exact or got_sha != expected_sha:
        status = "BX_Q3_HOSTED_RESTORE_OR_SHA_FAIL"
    else:
        status = "BX_Q1_REMOTE_CHECKPOINT_FAILOVER_PASS"
    receipt = {
        "experiment": "Exp073BX",
        "stage": "hosted",
        "status": status,
        "completed_bands": completed,
        "array_equal": bool(exact),
        "matrix_sha256": got_sha,
        "expected_matrix_sha256": expected_sha,
        "sha_equal": got_sha == expected_sha,
        "branch": BRANCH,
        "authority": False,
        "scientific_readiness_increment": 0,
        "draft_data_readiness_increment": 0,
    }
    pathlib.Path("exp073bx_result.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True), flush=True)
    if status != "BX_Q1_REMOTE_CHECKPOINT_FAILOVER_PASS":
        raise SystemExit(1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["home", "hosted"])
    args = ap.parse_args()
    if args.mode == "home":
        home()
    else:
        hosted()


if __name__ == "__main__":
    main()
