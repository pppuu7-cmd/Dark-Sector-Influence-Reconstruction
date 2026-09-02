#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path
import tempfile

import numpy as np

from dsir_remote_band_checkpoint_v0_1 import BandCheckpointStore, CheckpointContract
import exp073cf_continuation_wm_s2_v0_1 as cont


def contract(replica: str, source: str = cont.HISTORICAL_SOURCE_COMMIT,
             sync: str = cont.HISTORICAL_CHECKPOINT_SYNC_COMMIT) -> CheckpointContract:
    return CheckpointContract(
        experiment="Exp073CA",
        source_commit=source,
        helper_commit="fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22",
        prereg_commit="564a8d48f2af26d4394521f3fb55d51d80bcafe9",
        task="Wm_S2",
        lmax=7,
        nbands=3,
        row_length=8,
        threads=8,
        extra={
            "replica": replica,
            "pcl_sha256": "synthetic-nonclassifying",
            "bw_helper_commit": "9fb0ecb79986cf5f542760377533a685745b31e2",
            "checkpoint_utility_commit": "0b0324afb69acb16cbea97bb924b9be48f303dde",
            "checkpoint_sync_commit": sync,
            "chunk_bands": 4,
            "edges": [0, 2, 5, 8],
            "signature": [0, 2, 0, 2],
            "checkpoint_boundary": "complete_band_only",
        },
    )


def expect_contract_mismatch(root: Path, c: CheckpointContract) -> None:
    try:
        BandCheckpointStore(root, c)
    except RuntimeError as e:
        assert "contract mismatch" in str(e)
    else:
        raise AssertionError("changed historical contract did not fail closed")


def test_replica(replica: str) -> dict:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / replica
        c = contract(replica)
        s = BandCheckpointStore(root, c)
        row0 = np.arange(8, dtype="<f8") + (0 if replica == "A" else 100)
        sha0 = s.save_completed_band(0, row0, ell_lo=0, ell_hi_exclusive=2, wall_seconds=1.0)
        before = (root / "rows/band_000.bin").read_bytes()
        fp = c.fingerprint()

        # Exact historical-form restore.
        s2 = BandCheckpointStore(root, contract(replica))
        restored, done = s2.restore_matrix()
        assert done == [0]
        assert restored[0].tobytes(order="C") == before
        assert s2.contract.fingerprint() == fp

        # Synthetic continuation adds a complete row without rewriting row0 or contract.
        row1 = np.arange(8, dtype="<f8") + (10 if replica == "A" else 110)
        s2.save_completed_band(1, row1, ell_lo=2, ell_hi_exclusive=5, wall_seconds=1.0)
        assert (root / "rows/band_000.bin").read_bytes() == before
        assert json.loads((root / "contract.json").read_text())["fingerprint"] == fp
        assert s2.completed_bands() == [0, 1]

        # Historical provenance changes must fail closed.
        expect_contract_mismatch(root, contract(replica, source="0" * 40))
        expect_contract_mismatch(root, contract(replica, sync="1" * 40))
        return {"replica": replica, "row0_sha": sha0, "fingerprint": fp, "completed": [0, 1]}


def test_wrapper_binding() -> dict:
    cont._assert_historical_contract_constants()
    source = Path(cont.__file__).read_text()
    assert "dsir_checkpoint_git_sync_v0_1.sh" not in source
    assert cont.TRANSPORT_HELPER == "ci/dsir_checkpoint_git_sync_v0_2.sh"
    assert cont.HISTORICAL_SOURCE_COMMIT == "f9cb1eec582276776ddac3b1207686b1e01d3b6a"
    assert cont.HISTORICAL_CHECKPOINT_SYNC_COMMIT == "96886916b41dce7f0a40807622928c841ef5fc58"
    return {
        "historical_source_commit": cont.HISTORICAL_SOURCE_COMMIT,
        "historical_checkpoint_sync_commit": cont.HISTORICAL_CHECKPOINT_SYNC_COMMIT,
        "transport_helper": cont.TRANSPORT_HELPER,
        "continuation_transport_commit": cont.CONTINUATION_TRANSPORT_COMMIT,
    }


def main() -> None:
    receipt = {
        "experiment": "Exp073CF",
        "stage": "versioned_continuation_hosted_synthetic_compatibility_qa",
        "classification": "SYNTHETIC_NONCLASSIFYING_INFRASTRUCTURE_QA",
        "readiness_delta": "+0/+0",
        "replicas": [test_replica("A"), test_replica("B")],
        "wrapper_binding": test_wrapper_binding(),
        "status": "EXP073CF_CONTINUATION_V0_1_SYNTHETIC_COMPATIBILITY_PASS",
    }
    out = Path(os.environ.get("DSIR_QA_RECEIPT", "exp073cf_continuation_v0_1_qa_receipt.json"))
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
