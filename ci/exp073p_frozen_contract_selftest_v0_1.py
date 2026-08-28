#!/usr/bin/env python3
"""Exp073P frozen-contract self-tests.

This module deliberately does *not* build DES/NaMaster support rows and does not
classify Exp073P.  It freezes and executable-tests only semantics that were
already preregistered in experiments/073p_*_prereg_v0_1.md, so the later
classifying executor cannot silently drift at threshold/unit/failure boundaries.
"""
from __future__ import annotations

import math

Z_MIN = 0.295
Z_MAX = 2.33
K_MAX_MPC_INV = 0.06664762008318016
F_INVALID_MAX = 0.05
MIN_RETAINED_FULL_COORDINATES = 15
NSIDE_CLASSIFYING = 4096

PASS = "PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P"
FAIL_DIMENSION = "FAIL_COMMON_PHYSICAL_SUPPORT_DIMENSION_EXP073P"
FAIL_REPRO = "FAIL_EXP073P_REPRODUCTION_OR_NUMERICAL_COMPLETENESS"
INCOMPLETE = "INCOMPLETE_EXP073P"

FORBIDDEN_DOWNSTREAM_KEYS = {
    "covariance",
    "whitening",
    "nuisance_svd",
    "nuisance_rank",
    "quotient",
    "relation",
    "null_residual",
    "g8",
    "withheld_family",
    "article_selection",
}


def physical_support_valid(z: float, k_mpc_inv: float) -> bool:
    """Frozen rectangle membership; no lower-k cut is introduced by Exp073P."""
    return (
        math.isfinite(z)
        and math.isfinite(k_mpc_inv)
        and Z_MIN <= z <= Z_MAX
        and k_mpc_inv <= K_MAX_MPC_INV
    )


def support_fraction(invalid_positive_weight: float, total_positive_weight: float) -> float:
    """Return f_invalid, rejecting nontrustworthy normalization numerically."""
    if not math.isfinite(total_positive_weight) or total_positive_weight <= 0.0:
        raise ValueError(FAIL_REPRO)
    if not math.isfinite(invalid_positive_weight) or invalid_positive_weight < 0.0:
        raise ValueError(FAIL_REPRO)
    f = invalid_positive_weight / total_positive_weight
    eps = 64.0 * 2.220446049250313e-16
    if not math.isfinite(f) or f < -eps or f > 1.0 + eps:
        raise ValueError(FAIL_REPRO)
    return f


def coordinate_passes(f_invalid: float) -> bool:
    """Frozen inclusive threshold: exactly 0.05 passes."""
    if not math.isfinite(f_invalid) or f_invalid < 0.0:
        raise ValueError(FAIL_REPRO)
    return f_invalid <= F_INVALID_MAX


def assert_no_downstream_leakage(record: dict) -> None:
    """Reject any future support-input record carrying downstream information."""
    lowered = {str(k).lower() for k in record}
    leaked = sorted(lowered & FORBIDDEN_DOWNSTREAM_KEYS)
    if leaked:
        raise ValueError(f"{FAIL_REPRO}: downstream leakage keys={leaked}")


def _expect_raises(fn, *args) -> None:
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError(f"expected ValueError from {fn.__name__}{args!r}")


def selftest() -> None:
    # Frozen constants / unit convention.
    assert Z_MIN == 0.295
    assert Z_MAX == 2.33
    assert K_MAX_MPC_INV == 0.06664762008318016
    assert F_INVALID_MAX == 0.05
    assert MIN_RETAINED_FULL_COORDINATES == 15
    assert NSIDE_CLASSIFYING == 4096

    # Rectangle boundaries are inclusive; just-outside points fail.
    assert physical_support_valid(Z_MIN, K_MAX_MPC_INV)
    assert physical_support_valid(Z_MAX, K_MAX_MPC_INV)
    assert not physical_support_valid(math.nextafter(Z_MIN, -math.inf), K_MAX_MPC_INV)
    assert not physical_support_valid(math.nextafter(Z_MAX, math.inf), K_MAX_MPC_INV)
    assert not physical_support_valid(1.0, math.nextafter(K_MAX_MPC_INV, math.inf))

    # Positive-envelope fraction and exact inclusive 5% threshold.
    assert support_fraction(5.0, 100.0) == 0.05
    assert coordinate_passes(0.05)
    assert coordinate_passes(math.nextafter(0.05, -math.inf))
    assert not coordinate_passes(math.nextafter(0.05, math.inf))
    assert coordinate_passes(0.0)
    assert not coordinate_passes(1.0)

    # P4: bad normalization is reproduction/numerical failure, not support FAIL.
    for den in (0.0, -1.0, math.nan, math.inf):
        _expect_raises(support_fraction, 0.0, den)
    for num in (-1.0, math.nan, math.inf):
        _expect_raises(support_fraction, num, 1.0)

    # P8: support evaluation must be downstream-blind.
    assert_no_downstream_leakage({"support_rows": [], "provenance": {}})
    for key in sorted(FORBIDDEN_DOWNSTREAM_KEYS):
        _expect_raises(assert_no_downstream_leakage, {key: None})

    # Preserve the preregistered result taxonomy literally.
    assert PASS.startswith("PASS_")
    assert FAIL_DIMENSION.startswith("FAIL_")
    assert FAIL_REPRO.startswith("FAIL_")
    assert INCOMPLETE.startswith("INCOMPLETE_")
    assert len({PASS, FAIL_DIMENSION, FAIL_REPRO, INCOMPLETE}) == 4


if __name__ == "__main__":
    selftest()
    print("PASS_EXP073P_FROZEN_CONTRACT_SELFTEST_V0_1")
