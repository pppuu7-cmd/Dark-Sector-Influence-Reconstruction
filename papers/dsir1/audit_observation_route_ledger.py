#!/usr/bin/env python3
"""Fail-closed semantic audit for the DSIR-I observation-route ledger."""

from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "OBSERVATION_ROUTE_LEDGER.md"
SNAPSHOT = HERE / "evidence" / "support_operator_eligibility_v0_1.json"


def require(cond: bool, message: str) -> None:
    if not cond:
        raise AssertionError(message)


def main() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    snap = SNAPSHOT.read_text(encoding="utf-8")

    for exp in [
        "Exp072A", "Exp072B", "Exp072C", "Exp073A", "Exp073B/C",
        "Exp073D/E", "Exp073L", "Exp073M", "Exp073N", "Exp073O",
        "Exp073P2", "Exp073S0", "Exp073R0", "Exp073R1",
    ]:
        require(exp in text, f"ledger stage missing: {exp}")

    for token in [
        "0/26",
        "7/64",
        "NONNORMALIZABLE",
        "PROVENANCE FAIL",
        "Cosmotheka DES Y1",
        "science_gate_scored=false",
        "RUNNING / PRE-RESULT",
        "G7=OPEN",
        "G8=OPEN",
        "G9=OPEN",
    ]:
        require(token in text, f"ledger boundary token missing: {token}")

    # The machine-readable snapshot, not prose, remains authoritative for these
    # three non-collapsible statuses.
    require('"status": "FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE"' in snap,
            "snapshot no longer preserves Exp073N provenance FAIL")
    require('"status": "PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O"' in snap,
            "snapshot no longer preserves Exp073O replacement status")
    require('"status": "PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0"' in snap,
            "snapshot no longer preserves Exp073R0 prerequisite PASS")
    require('"science_gate_scored": false' in snap,
            "snapshot no longer preserves the R0 pre-support boundary")
    require('"science_claim_included": false' in snap,
            "snapshot no longer excludes pre-result R1")

    print("PASS: observation-route ledger keeps candidate/FAIL/replacement/prerequisite statuses distinct")
    print("PASS: physical-support and downstream G7/G8/G9 boundaries remain closed")


if __name__ == "__main__":
    main()
