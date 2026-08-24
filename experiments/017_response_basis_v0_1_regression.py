#!/usr/bin/env python3
"""Experiment 017: regression tests for frozen DSIR response basis v0.1."""
from __future__ import annotations

import numpy as np

from dsir.response_basis import (
    ap_log_response,
    matter_power_response,
    project_constant_log_amplitude,
    relative_expansion_response,
)


def main() -> None:
    # Frozen DESI-oriented nodes.
    z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33])
    H_ref = 70.0 * np.sqrt(0.3 * (1.0 + z) ** 3 + 0.7)

    # A model with a physical redshift-dependent response plus an arbitrary
    # common H calibration. Anchoring must remove the calibration exactly.
    H = 1.17 * H_ref * np.exp(0.03 * (z - 0.51))
    r1 = relative_expansion_response(z, H, H_ref, z_anchor=0.51)
    r2 = relative_expansion_response(z, 5.0 * H, H_ref, z_anchor=0.51)
    calibration_error = float(np.max(np.abs(r1 - r2)))
    assert calibration_error < 1e-13
    assert abs(r1[np.argmin(np.abs(z - 0.51))]) < 1e-14

    # Exact AP log-response identity: F_AP=D_M H/c.
    D_M_ref = np.array([1000.0, 1500.0, 2000.0])
    D_M = D_M_ref * np.exp([0.01, -0.02, 0.03])
    H_ref_ap = np.array([89.0, 118.0, 158.0])
    H_ap = np.array([90.0, 120.0, 160.0])
    lhs = ap_log_response(D_M, H_ap, D_M_ref, H_ref_ap)
    rhs = np.log((D_M * H_ap) / (D_M_ref * H_ref_ap))
    ap_error = float(np.max(np.abs(lhs - rhs)))
    assert ap_error < 1e-14

    # Fixed-primordial matter power must preserve a real multiplicative
    # amplitude response; it is not normalized away model by model.
    P_ref = np.array([100.0, 80.0, 40.0, 10.0])
    expected = np.array([0.2, 0.1, -0.05, -0.1])
    P = P_ref * np.exp(expected)
    rP = matter_power_response(P, P_ref)
    power_error = float(np.max(np.abs(rP - expected)))
    assert power_error < 1e-14

    # Covariance-aware constant-amplitude quotient must be orthogonal to the
    # constant mode in the supplied precision metric.
    W = np.array(
        [
            [2.0, 0.2, 0.0, 0.0],
            [0.2, 1.5, 0.1, 0.0],
            [0.0, 0.1, 1.2, 0.1],
            [0.0, 0.0, 0.1, 1.0],
        ]
    )
    q = project_constant_log_amplitude(rP + 0.7, precision=W)
    orthogonality = float(abs(np.ones(4) @ W @ q))
    assert orthogonality < 1e-13

    print("Experiment 017 PASS")
    print(f"calibration invariance max error = {calibration_error:.3e}")
    print(f"AP identity max error          = {ap_error:.3e}")
    print(f"fixed-As power response error  = {power_error:.3e}")
    print(f"W-orthogonality residual       = {orthogonality:.3e}")


if __name__ == "__main__":
    main()
