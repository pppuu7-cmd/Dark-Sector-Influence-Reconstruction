#!/usr/bin/env python3
"""Exp073P prospective support-executor contract self-tests.

This module contains only frozen, synthetic contract checks. It does not read
DES/BOSS observables, does not evaluate the real Exp073P support mask, does not
read covariance/downstream products, and cannot authorize covariance/whitening.
It makes already-preregistered P3--P8 semantics executable before the
classifying executor exists.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence

Z_MIN = 0.295
Z_MAX = 2.33
K_MAX_MPC_INV = 0.06664762008318016
F_INVALID_MAX = 0.05
MIN_RETAINED_FULL_COORDINATES = 15
NSIDE_CLASSIFYING = 4096

ELL_EDGES = (
    0, 30, 60, 90, 120, 150, 180, 210, 240, 272, 309, 351, 398, 452,
    513, 582, 661, 750, 852, 967, 1098, 1247, 1416, 1608, 1826, 2073,
    2354, 2673, 3035, 3446, 3914, 4444, 5047, 5731, 6508, 7390, 8392,
    9529, 10821, 12288,
)

R1_PASS = "PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1"
PASS = "PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P"
FAIL_DIMENSION = "FAIL_COMMON_PHYSICAL_SUPPORT_DIMENSION_EXP073P"
FAIL_REPRO = "FAIL_EXP073P_REPRODUCTION_OR_NUMERICAL_COMPLETENESS"

FORBIDDEN_SUPPORT_INPUT_KEYS = {
    "covariance", "whitening", "nuisance_svd", "nuisance_rank", "quotient",
    "relation", "null_residual", "g8", "withheld_family", "article_selection",
    "fiducial_p", "fiducial_pk", "model_weight", "effective_ell", "ell_eff",
    "ell_cut", "k_cut",
}


@dataclass(frozen=True)
class SupportCell:
    """One explicit finite response cell in the support-bookkeeping domain."""

    ell: int
    z: float
    k_mpc_inv: float
    signed_response: float
    radial_kernel_weight: float


def physical_support_valid(z: float, k_mpc_inv: float) -> bool:
    return (
        math.isfinite(z)
        and math.isfinite(k_mpc_inv)
        and Z_MIN <= z <= Z_MAX
        and k_mpc_inv <= K_MAX_MPC_INV
    )


def validate_support_input_record(record: Mapping[str, object]) -> None:
    """Fail closed on preregistered downstream/model/cut shortcuts."""
    lowered = {str(k).lower() for k in record}
    leaked = sorted(lowered & FORBIDDEN_SUPPORT_INPUT_KEYS)
    if leaked:
        raise ValueError(f"{FAIL_REPRO}: forbidden support inputs={leaked}")


def assert_exact_finite_operator_coverage(
    explicit_operator_ells: Sequence[int], consumed_ells: Sequence[int]
) -> None:
    """No effective-ell compression, hidden ell cut, or tail extrapolation."""
    if not explicit_operator_ells:
        raise ValueError(f"{FAIL_REPRO}: empty finite operator")
    if tuple(consumed_ells) != tuple(explicit_operator_ells):
        raise ValueError(f"{FAIL_REPRO}: finite operator coverage changed")
    if any(not isinstance(ell, int) or ell < 0 for ell in explicit_operator_ells):
        raise ValueError(f"{FAIL_REPRO}: invalid ell")
    if max(explicit_operator_ells) >= ELL_EDGES[-1]:
        raise ValueError(f"{FAIL_REPRO}: ell exceeds frozen finite lmax")


def signed_observable_response(cells: Iterable[SupportCell]) -> float:
    """Preserve signed Wm response; no abs is allowed in the measured response."""
    total = 0.0
    for cell in cells:
        if not math.isfinite(cell.signed_response):
            raise ValueError(f"{FAIL_REPRO}: non-finite signed response")
        total += cell.signed_response
    return total


def positive_support_fraction(cells: Sequence[SupportCell]) -> tuple[float, float, float]:
    """Compute support from the full positive |response| radial envelope.

    The denominator is accumulated over every supplied finite-domain cell before
    rectangle membership is applied. Thus low/high-z and high-k tails remain in
    the denominator and contribute to the invalid numerator; crop-before-
    normalization cannot reproduce this function.
    """
    if not cells:
        raise ValueError(f"{FAIL_REPRO}: empty support row")

    denominator = 0.0
    invalid = 0.0
    for cell in cells:
        if not isinstance(cell.ell, int) or cell.ell < 0 or cell.ell >= ELL_EDGES[-1]:
            raise ValueError(f"{FAIL_REPRO}: invalid finite ell")
        if not math.isfinite(cell.z) or not math.isfinite(cell.k_mpc_inv):
            raise ValueError(f"{FAIL_REPRO}: non-finite physical coordinate")
        if not math.isfinite(cell.signed_response):
            raise ValueError(f"{FAIL_REPRO}: non-finite signed response")
        if not math.isfinite(cell.radial_kernel_weight) or cell.radial_kernel_weight < 0.0:
            raise ValueError(f"{FAIL_REPRO}: invalid radial kernel weight")

        weight = abs(cell.signed_response) * cell.radial_kernel_weight
        denominator += weight
        if not physical_support_valid(cell.z, cell.k_mpc_inv):
            invalid += weight

    if not math.isfinite(denominator) or denominator <= 0.0:
        raise ValueError(f"{FAIL_REPRO}: non-positive envelope normalization")
    if not math.isfinite(invalid) or invalid < 0.0:
        raise ValueError(f"{FAIL_REPRO}: invalid numerator")
    fraction = invalid / denominator
    if not math.isfinite(fraction) or fraction < 0.0 or fraction > 1.0:
        raise ValueError(f"{FAIL_REPRO}: invalid f_invalid")
    return invalid, denominator, fraction


def coordinate_passes(f_invalid: float) -> bool:
    if not math.isfinite(f_invalid) or not 0.0 <= f_invalid <= 1.0:
        raise ValueError(FAIL_REPRO)
    return f_invalid <= F_INVALID_MAX


def complete_coordinate_intersection(
    block_masks: Mapping[str, Mapping[str, bool]],
    required_blocks: Sequence[str] = ("Wm", "WW", "BOSS_mm"),
) -> tuple[str, ...]:
    """Apply P7 only after block-local masks exist; use intersection, never union."""
    if tuple(required_blocks) != ("Wm", "WW", "BOSS_mm"):
        raise ValueError(f"{FAIL_REPRO}: required blocks changed")
    if set(block_masks) != set(required_blocks):
        raise ValueError(f"{FAIL_REPRO}: incomplete or extra block mask set")
    coordinate_sets = [set(block_masks[name]) for name in required_blocks]
    common = set.intersection(*coordinate_sets)
    return tuple(sorted(
        coord for coord in common
        if all(bool(block_masks[name][coord]) for name in required_blocks)
    ))


def classify_from_trustworthy_masks(
    retained_complete_coordinates: Sequence[str], reproduction_complete: bool
) -> str:
    """Frozen taxonomy only; infrastructure handling belongs to the executor."""
    if not reproduction_complete:
        return FAIL_REPRO
    if len(tuple(retained_complete_coordinates)) >= MIN_RETAINED_FULL_COORDINATES:
        return PASS
    return FAIL_DIMENSION


def authorize_real_support_executor(parent_statuses: Mapping[str, str]) -> bool:
    """R1 final PASS is necessary, never replaceable by manifests/checksums."""
    return parent_statuses.get("weak_lensing_mask_reproduction_r1") == R1_PASS


def _expect_raises(fn, *args) -> None:
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError(f"expected ValueError from {fn.__name__}{args!r}")


def selftest() -> None:
    assert Z_MIN == 0.295 and Z_MAX == 2.33
    assert K_MAX_MPC_INV == 0.06664762008318016
    assert F_INVALID_MAX == 0.05
    assert MIN_RETAINED_FULL_COORDINATES == 15
    assert NSIDE_CLASSIFYING == 4096
    assert ELL_EDGES[0] == 0 and ELL_EDGES[-1] == 12288
    assert len(ELL_EDGES) == 40
    assert all(a < b for a, b in zip(ELL_EDGES, ELL_EDGES[1:]))

    # P3: exact finite multipole coverage, no effective ell/cut/tail substitution.
    explicit = (0, 1, 2, 29, 30, 31, 12286, 12287)
    assert_exact_finite_operator_coverage(explicit, explicit)
    _expect_raises(assert_exact_finite_operator_coverage, explicit, explicit[:-1])
    _expect_raises(assert_exact_finite_operator_coverage, explicit, (0, 1, 2, 30))
    _expect_raises(assert_exact_finite_operator_coverage, (0, 12288), (0, 12288))

    # P8 plus no fiducial/model/effective-cut shortcuts.
    validate_support_input_record({"response_cells": (), "provenance": {}})
    for key in sorted(FORBIDDEN_SUPPORT_INPUT_KEYS):
        _expect_raises(validate_support_input_record, {key: object()})

    # Signed Wm production is distinct from the positive support envelope.
    signed_cells = (
        SupportCell(30, 1.0, 0.01, -2.0, 1.0),
        SupportCell(31, 1.0, 0.01, +1.0, 1.0),
    )
    assert signed_observable_response(signed_cells) == -1.0
    assert positive_support_fraction(signed_cells) == (0.0, 3.0, 0.0)

    # Full radial tails are counted before normalization: exactly 5% low-z tail.
    tail_row = (
        SupportCell(60, 0.10, 0.01, +5.0, 1.0),
        SupportCell(60, 1.00, 0.01, +95.0, 1.0),
    )
    assert positive_support_fraction(tail_row) == (5.0, 100.0, 0.05)
    assert coordinate_passes(positive_support_fraction(tail_row)[2])
    just_over = (
        SupportCell(60, 0.10, 0.01, math.nextafter(5.0, math.inf), 1.0),
        SupportCell(60, 1.00, 0.01, 95.0, 1.0),
    )
    assert not coordinate_passes(positive_support_fraction(just_over)[2])

    # High-k and high-z tails count invalid too; there is no lower-k cut.
    mixed = (
        SupportCell(90, 1.0, 0.0, 1.0, 1.0),
        SupportCell(90, 1.0, math.nextafter(K_MAX_MPC_INV, math.inf), 1.0, 1.0),
        SupportCell(90, math.nextafter(Z_MAX, math.inf), 0.01, 1.0, 1.0),
    )
    assert positive_support_fraction(mixed) == (2.0, 3.0, 2.0 / 3.0)

    # P4: zero support normalization is a reproduction failure.
    _expect_raises(positive_support_fraction, (SupportCell(30, 1.0, 0.01, 0.0, 1.0),))

    # P7: complete coordinates are an intersection after block-local evaluation.
    masks = {
        "Wm": {"c00": True, "c01": True, "c02": False},
        "WW": {"c00": True, "c01": False, "c02": True},
        "BOSS_mm": {"c00": True, "c01": True, "c02": True},
    }
    assert complete_coordinate_intersection(masks) == ("c00",)
    _expect_raises(complete_coordinate_intersection, {"Wm": {"c00": True}, "WW": {"c00": True}})

    # Frozen dimension boundary is exact and inclusive at 15.
    assert classify_from_trustworthy_masks([f"c{i}" for i in range(14)], True) == FAIL_DIMENSION
    assert classify_from_trustworthy_masks([f"c{i}" for i in range(15)], True) == PASS
    assert classify_from_trustworthy_masks([f"c{i}" for i in range(99)], False) == FAIL_REPRO

    # R1 manifests/checksums are not a substitute for the final mask PASS.
    assert not authorize_real_support_executor(
        {"weak_lensing_mask_reproduction_r1": "PASS_CANONICAL_ROOT_MANIFESTS_ONLY"}
    )
    assert authorize_real_support_executor(
        {"weak_lensing_mask_reproduction_r1": R1_PASS}
    )


if __name__ == "__main__":
    selftest()
    print("PASS_EXP073P_SUPPORT_EXECUTOR_CONTRACT_SELFTEST_V0_1")
