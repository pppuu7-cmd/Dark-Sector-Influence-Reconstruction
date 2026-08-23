"""Experiment 014 — source-level GDM -> CDM regression.

Pinned upstream: s-ilic/gdm_class_public @
4c87916aab5ca124a68f1dd16f31846fc13d1829

This experiment verifies the algebraic zero-closure limit of the pinned source.
It also records an important finite-start caveat: when GDM is enabled, the
upstream code uses simplified radiation-era initial conditions with some
O(omega*tau) corrections deliberately omitted. Therefore the eventual full
Boltzmann regression must demonstrate convergence with earlier start time,
not demand bitwise equality at one finite start.
"""
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dsir.gdm_source_control import (
    cdm_leading_adiabatic_ic,
    cdm_rhs,
    class_finite_start_photon_delta,
    dynamic_shear_rhs,
    gdm_adiabatic_ic,
    gdm_branch_photon_delta,
    gdm_rhs,
    rho_zero_w,
)


def main():
    rng = np.random.default_rng(20260824)

    # Background: all w bins = 0 implies rho ~ a^-3 exactly.
    a = np.geomspace(1e-7, 1.0, 500)
    omega0 = 0.265
    rho = rho_zero_w(a, omega0)
    rho_ref = omega0 * a**-3
    bg_rel = np.max(np.abs(rho - rho_ref) / rho_ref)

    # Perturbation RHS: w=ca2=cs2=0, shear=0 must reduce to pressureless CDM.
    rhs_err = 0.0
    shear_err = 0.0
    for _ in range(1000):
        delta, theta, metric_cont, metric_euler = rng.normal(size=4)
        aH = abs(rng.normal()) + 1e-4
        k = 10.0 ** rng.uniform(-4, 1)
        s2 = rng.uniform(0.5, 1.5)
        got = gdm_rhs(delta, theta, 0.0, aH, k, metric_cont, metric_euler, s2)
        ref = cdm_rhs(theta, aH, metric_cont, metric_euler)
        rhs_err = max(rhs_err, float(np.max(np.abs(got - ref))))
        shear_err = max(
            shear_err,
            abs(dynamic_shear_rhs(0.0, theta, rng.normal(), aH, cv2=0.0, w=0.0)),
        )

    # Leading adiabatic GDM IC become CDM IC when all closure parameters vanish.
    ic_err = 0.0
    for fracnu in np.linspace(0.0, 0.9, 10):
        for ktau in np.logspace(-8, -2, 25):
            got = gdm_adiabatic_ic(ktau, 0.1, 1.2, fracnu, w=0.0, cs2=0.0, cv2=0.0)
            ref = cdm_leading_adiabatic_ic(ktau, 1.2)
            ic_err = max(ic_err, float(np.max(np.abs(got - ref))))

    # Finite-start caveat. Standard CLASS retains a first O(omega*tau)
    # correction in photon IC, whereas the GDM branch intentionally omits it.
    # Relative discrepancy from this particular term should be omega_tau/5.
    omega_tau = np.logspace(-9, -2, 40)
    ktau = 1e-3
    curv = 1.0
    lead = abs(gdm_branch_photon_delta(ktau, curv))
    rel = np.array([
        abs(gdm_branch_photon_delta(ktau, curv) - class_finite_start_photon_delta(ktau, curv, ot)) / lead
        for ot in omega_tau
    ])
    finite_start_scaling_err = float(np.max(np.abs(rel - omega_tau / 5.0)))

    assert bg_rel < 1e-15
    assert rhs_err < 1e-14
    assert shear_err < 1e-14
    assert ic_err < 1e-20
    assert finite_start_scaling_err < 1e-14

    outdir = ROOT / "data" / "derived" / "gdm"
    outdir.mkdir(parents=True, exist_ok=True)
    text = (
        "Experiment 014 — GDM zero-limit source regression\n"
        f"background max relative error = {bg_rel:.6e}\n"
        f"zero-closure perturbation RHS max error = {rhs_err:.6e}\n"
        f"zero-cv2 zero-shear RHS max error = {shear_err:.6e}\n"
        f"leading adiabatic IC max error = {ic_err:.6e}\n"
        f"finite-start O(omega*tau) scaling max error = {finite_start_scaling_err:.6e}\n"
        "PASS: pinned GDM source has the CDM zero-closure limit at background, evolution-equation, and leading-IC level.\n"
        "CAVEAT: full GDM_CLASS-vs-CLASS spectra must be convergence-tested versus earlier start time because GDM initial conditions omit finite-start O(omega*tau) terms.\n"
        "STATUS: source-level regression only; full Boltzmann G3B regression remains open.\n"
    )
    (outdir / "experiment_014_output.txt").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
