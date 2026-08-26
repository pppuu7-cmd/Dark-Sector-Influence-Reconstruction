# DSIR erratum — CAMB Weyl power-variable convention (2026-08-26)

## Correction

Several earlier DSIR bridge/recovery notes used the shorthand statement that CAMB `Weyl` is the Weyl potential `(Phi+Psi)/2`. That shorthand is insufficient and is **not the operational convention of CAMB's matter-power variable used by the ACT×unWISE likelihood**.

Pinned/source-audited CAMB documentation states:

`Weyl = k^2 Psi_W = k^2 (phi+psi)/2`.

This is the quantity used as a matter-power-spectrum variable by CAMB's `get_matter_power_interpolator` / `Pk_interpolator` interfaces.

CAMB separately documents that `get_matter_transfer_data` returns the listed transfer variables divided by `k^2`. Consequently the raw transfer-table `Transfer_Weyl` column is not numerically the same object as the `Weyl` variable entering the matter-power interpolator.

## Why this matters for DSIR

The pinned ACT×unWISE theory layer asks CAMB for three independent spectra:

- `P(Weyl,Weyl)`;
- `P(Weyl,delta_nonu)`;
- `P(delta_nonu,delta_nonu)`.

Therefore a solver-neutral CLASS adapter must reproduce the **power-interpolator** convention, including the `k^2` Weyl scaling, sign, physical-k convention, primordial normalization and matter-species definition. Directly inserting CLASS `phi`, `psi`, `(phi+psi)/2`, or a raw CAMB transfer-table column would be a convention error.

## Matter convention

CAMB documents

`delta_nonu = (rho_c Delta_c + rho_b Delta_b)/(rho_c+rho_b)`

for CDM+baryon matter excluding massive neutrinos. The solver-neutral bridge must declare and reproduce this species weighting; generic `delta_m`, `delta_tot`, or a neutrino-inclusive field cannot be silently substituted.

## Scientific status

This erratum changes no prior scientific PASS/FAIL result whose tested quantities did not depend on a real CLASS→CAMB ACT projection. In particular, Exp066A's analytic-mock algebraic independence test remains valid as an algebraic bridge test.

It **does** supersede any operational reading of earlier prose that identified ACT/CAMB `Weyl` with the unscaled potential alone. No G7 law search using CLASS-family ACT projections is admissible until a separately preregistered LambdaCDM physical convention regression passes.

The correction was recorded before any fresh withheld G8 family was selected and before any covariance-whitened G7 law was fit.
