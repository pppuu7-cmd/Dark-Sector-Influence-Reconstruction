#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess

import exp073ca_checkpoint_streaming_wm_s2_v0_1 as historical

HISTORICAL_SOURCE_COMMIT = "f9cb1eec582276776ddac3b1207686b1e01d3b6a"
HISTORICAL_CHECKPOINT_SYNC_COMMIT = "96886916b41dce7f0a40807622928c841ef5fc58"
CONTINUATION_TRANSPORT_COMMIT = "bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1"
CONTINUATION_PREREG_COMMIT = "36853b723b172a6038c6d3023805f08f37ffac72"
TRANSPORT_HELPER = "ci/dsir_checkpoint_git_sync_v0_2.sh"


def _assert_historical_contract_constants() -> None:
    expected = {
        "PREREG_COMMIT": "564a8d48f2af26d4394521f3fb55d51d80bcafe9",
        "HELPER_COMMIT": "fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22",
        "BW_HELPER_COMMIT": "9fb0ecb79986cf5f542760377533a685745b31e2",
        "CHECKPOINT_UTILITY_COMMIT": "0b0324afb69acb16cbea97bb924b9be48f303dde",
        "CHECKPOINT_SYNC_COMMIT": HISTORICAL_CHECKPOINT_SYNC_COMMIT,
        "L": 12288,
        "LMAX": 12287,
        "NB": 39,
        "THREADS": 8,
        "CHUNK": 4,
        "SIGNATURE": (0, 2, 0, 2),
    }
    for name, value in expected.items():
        observed = getattr(historical, name)
        if observed != value:
            raise RuntimeError(f"historical driver binding mismatch {name}: expected={value!r} observed={observed!r}")


def _remote_push_v02(checkpoint_dir: Path, branch: str, label: str) -> None:
    subprocess.run(
        ["bash", TRANSPORT_HELPER, "push", str(checkpoint_dir), branch, label],
        check=True,
    )


def _annotate_receipt(path: Path) -> None:
    rec = json.loads(path.read_text())
    if rec.get("status") != "COMPLETE_VALID_COMPARATOR_INPUT_EXP073CA_WM_S2_COMPACT_V0_1":
        raise RuntimeError("unexpected historical output status; fail closed")
    rec["continuation"] = {
        "mode": "EXP073CF_VERSIONED_CONTINUATION_V0_1",
        "historical_source_commit": HISTORICAL_SOURCE_COMMIT,
        "historical_checkpoint_sync_commit": HISTORICAL_CHECKPOINT_SYNC_COMMIT,
        "continuation_transport_helper": TRANSPORT_HELPER,
        "continuation_transport_commit": CONTINUATION_TRANSPORT_COMMIT,
        "continuation_prereg_commit": CONTINUATION_PREREG_COMMIT,
        "scientific_arithmetic_changed": False,
        "historical_checkpoint_payload_contract_rewritten": False,
    }
    path.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")


def run(args: argparse.Namespace) -> None:
    _assert_historical_contract_constants()

    # Historical payload authority is bound to attempt2 head.  The new workflow
    # head is deliberately NOT inserted into the resumed checkpoint fingerprint.
    os.environ["GITHUB_SHA"] = HISTORICAL_SOURCE_COMMIT

    # Only transport plumbing is replaced; all numerical functions, contract
    # construction, checkpoint validation, chunking, output and status semantics
    # execute in the frozen historical driver.
    historical.remote_push = _remote_push_v02
    historical.run_full(
        Path(args.pcl_npy),
        Path(args.ca_so),
        Path(args.checkpoint_dir),
        args.checkpoint_branch,
        args.replica,
        Path(args.out_npz),
        Path(args.out_json),
    )
    _annotate_receipt(Path(args.out_json))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pcl-npy", required=True)
    ap.add_argument("--ca-so", required=True)
    ap.add_argument("--checkpoint-dir", required=True)
    ap.add_argument("--checkpoint-branch", required=True)
    ap.add_argument("--replica", required=True, choices=["A", "B"])
    ap.add_argument("--out-npz", required=True)
    ap.add_argument("--out-json", required=True)
    run(ap.parse_args())


if __name__ == "__main__":
    main()
