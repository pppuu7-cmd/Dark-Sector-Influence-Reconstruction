"""Experiment 013 — source-level regression for pinned interacting-vacuum control.

Purpose
-------
Freeze the exact sign convention and analytic background used by the selected
`kaeonikc/class_iv` IDM_IV implementation before attempting a full external
Boltzmann run.

This experiment does NOT claim observational validation. It verifies that the
DSIR transcription of the pinned upstream source:
  1. has the exact Lambda+CDM zero-coupling limit alpha=beta=0;
  2. solves the ODE system implied by Q = H(alpha rho_m + beta rho_v);
  3. has power-law eigen-exponents matching the interaction matrix.
"""
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import solve_ivp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dsir.interacting_vacuum import (
    analytic_background,
    background_rhs_lna,
    eigen_exponents,
    lcdm_limit,
)


def main():
    a = np.geomspace(1.0e-3, 1.0, 400)
    omega_m0, omega_v0 = 0.25, 0.70
    cases = [(0.0, 0.0), (0.1, 0.0), (0.0, 0.1), (0.05, -0.02), (0.2, 0.1)]

    # Exact zero-coupling algebraic limit.
    rho_m, rho_v = analytic_background(a, omega_m0, omega_v0, 0.0, 0.0)
    ref_m, ref_v = lcdm_limit(a, omega_m0, omega_v0)
    zero_m = np.max(np.abs(rho_m - ref_m) / np.maximum(np.abs(ref_m), 1e-300))
    zero_v = np.max(np.abs(rho_v - ref_v))

    rows = []
    for alpha, beta in cases:
        ra, rv = analytic_background(a, omega_m0, omega_v0, alpha, beta)
        sol = solve_ivp(
            lambda x, y: background_rhs_lna(x, y, alpha, beta),
            (0.0, np.log(a[0])),
            (omega_m0, omega_v0),
            rtol=1e-12,
            atol=1e-14,
            dense_output=True,
        )
        yn = sol.sol(np.log(a))
        err_m = np.max(np.abs(yn[0] - ra)) / np.max(np.abs(ra))
        err_v = np.max(np.abs(yn[1] - rv)) / max(np.max(np.abs(rv)), 1e-300)

        matrix = np.array([[-3.0 - alpha, -beta], [alpha, beta]])
        lam_matrix = np.sort(np.linalg.eigvals(matrix).real)
        lam_closed = np.sort(eigen_exponents(alpha, beta))
        err_eig = np.max(np.abs(lam_matrix - lam_closed))
        rows.append((alpha, beta, err_m, err_v, err_eig))

    max_ode = max(max(r[2], r[3]) for r in rows)
    max_eig = max(r[4] for r in rows)

    assert zero_m < 1e-13
    assert zero_v < 1e-13
    assert max_ode < 1e-9
    assert max_eig < 1e-13

    outdir = ROOT / "data" / "derived" / "interacting_vacuum"
    outdir.mkdir(parents=True, exist_ok=True)
    output = (
        "Experiment 013 — interacting-vacuum source regression\n"
        f"zero-coupling max relative matter error = {zero_m:.6e}\n"
        f"zero-coupling max vacuum absolute error = {zero_v:.6e}\n"
        f"max analytic-vs-ODE normalized error = {max_ode:.6e}\n"
        f"max eigen-exponent error = {max_eig:.6e}\n"
        "PASS: source-level alpha/beta convention frozen.\n"
        "NOTE: full CLASS solver regression is still required for G3B closure.\n"
    )
    (outdir / "experiment_013_output.txt").write_text(output)
    print(output)


if __name__ == "__main__":
    main()
