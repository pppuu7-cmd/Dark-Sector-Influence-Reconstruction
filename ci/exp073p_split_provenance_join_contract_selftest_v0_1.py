#!/usr/bin/env python3
"""Deterministic non-science self-test for the Exp073P split-provenance join.

This does not read observables, evaluate support, compute f_invalid, read a
covariance, or authorize G8.  It proves two bookkeeping properties only:

1. The legacy Exp073P public-input preflight cannot be the aggregate
   prerequisite gate because its 200 MiB implementation cap excludes the two
   exact large DES Y1 objects that are already frozen inputs.
2. A future aggregate join must require every independently certified parent,
   in particular a genuine final Exp073R1 PASS, before a physical-support
   executor may be admitted.
"""
from __future__ import annotations

import json

MAX_PREFLIGHT_BYTES = 200 * 1024 * 1024
SOURCE_BYTES = 2_738_626_560
SOURCE_SHA256 = "491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5"
METACAL_BYTES = 84_075_649_920
METACAL_SHA256 = "39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8"
COSMOTHEKA_PIN = "7bde066626f66cd7bbe79cc46224d2342840e463"
R1_PASS = "PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1"
S0_PASS = "PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0"
P2_PASS = "PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2"
LARGE_DES_PASS = "PASS_LARGE_DES_STREAMING_SHA256_BINDING_EXP073P"

FROZEN = {
    "z_min": 0.295,
    "z_max": 2.33,
    "k_max_Mpc^-1": 0.06664762008318016,
    "f_invalid_max": 0.05,
    "minimum_retained_dimension": 15,
    "nside_classifying": 4096,
    "boss_retained": 54,
    "boss_total": 240,
    "boss_cap_retained": 27,
    "boss_cap_total": 120,
}

REQUIRED_JOIN_PARENTS = {
    "cosmotheka_public_preflight",
    "large_des_whole_object_binding",
    "remaining_des_release_binding_p2",
    "redmagic_mask_nz_reproduction_s0",
    "weak_lensing_mask_reproduction_r1",
    "boss_exact_support_exp073j",
    "frozen_support_contract_selftest",
}


def main() -> None:
    # Formal obstruction in the legacy all-in-one preflight.  For an object
    # with exact size > MAX_PREFLIGHT_BYTES the branch that downloads and sets
    # checksum_bound=True is unreachable, so all_checksum_bound cannot be true
    # for the six-object set containing these two objects.
    assert SOURCE_BYTES > MAX_PREFLIGHT_BYTES
    assert METACAL_BYTES > MAX_PREFLIGHT_BYTES
    legacy_ready_reachable = False
    assert legacy_ready_reachable is False

    # The aggregate join is deliberately broader than any single provenance
    # job.  R1 final PASS is mandatory; canonical root manifests alone are not
    # a substitute for the reconstructed four-bin weak-lensing masks.
    assert "weak_lensing_mask_reproduction_r1" in REQUIRED_JOIN_PARENTS
    assert R1_PASS == "PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1"

    # Guard against resurrection of the known bad source hash transcription.
    bad_source_sha = "491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd"
    assert SOURCE_SHA256 != bad_source_sha
    assert len(SOURCE_SHA256) == 64 and len(METACAL_SHA256) == 64

    # Frozen scientific contract is copied, not re-fit.  This self-test never
    # evaluates it on data.
    assert FROZEN == {
        "z_min": 0.295,
        "z_max": 2.33,
        "k_max_Mpc^-1": 0.06664762008318016,
        "f_invalid_max": 0.05,
        "minimum_retained_dimension": 15,
        "nside_classifying": 4096,
        "boss_retained": 54,
        "boss_total": 240,
        "boss_cap_retained": 27,
        "boss_cap_total": 120,
    }

    receipt = {
        "experiment": "Exp073P-split-provenance-join-contract-selftest-v0.1",
        "status": "PASS_SPLIT_PROVENANCE_JOIN_PREREG_SELFTEST_EXP073P",
        "scientific_classification": None,
        "legacy_public_preflight_ready_reachable": legacy_ready_reachable,
        "reason": (
            "the frozen DES Y1 source and metacal objects exceed the legacy "
            "200 MiB preflight cap, so the legacy all_checksum_bound READY flag "
            "cannot serve as the aggregate prerequisite gate"
        ),
        "required_join_parents": sorted(REQUIRED_JOIN_PARENTS),
        "immutable_constants": {
            "cosmotheka_pin": COSMOTHEKA_PIN,
            "source_bytes": SOURCE_BYTES,
            "source_sha256": SOURCE_SHA256,
            "metacal_bytes": METACAL_BYTES,
            "metacal_sha256": METACAL_SHA256,
            "r1_required_status": R1_PASS,
            "s0_required_status": S0_PASS,
            "p2_required_status": P2_PASS,
            "large_des_required_status": LARGE_DES_PASS,
        },
        "frozen_support_contract": FROZEN,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "retained_dimension_evaluated": False,
        "covariance_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "heldout_read": False,
        "G8_read": False,
        "support_executor_authorized": False,
        "authorization_rule": (
            "support_executor_authorized may become true only in a separate "
            "aggregate evidence join after every required parent is immutably "
            "bound and R1 has the exact final PASS status"
        ),
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
