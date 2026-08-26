# Exp066A — solver-neutral ACT × unWISE raw projection contract v0.1

Date: 2026-08-26

## Purpose

Exp065B established that the official ACT DR6 × unWISE `XCorrACT` selected `Clgg + Clkg` covariance is reproducible and strictly positive definite without regularization. The remaining prerequisite before any G7 law search is to separate the public survey/projection operator from the pinned likelihood package's CAMB-specific provider layer.

Exp066A freezes and validates only the **raw line-of-sight projection basis**. It does not fit ACT data, does not select a dark-sector family, does not define a G7 law, and does not change F31 or Exp065A/Exp065B.

## Pinned external source

`ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`

The reference implementation is `unWISExLens_lklh/theory_modules/unWISExkappa_model.py`, method `unWISExLens_theory_model.compute_raw_spectra`.

## Solver-neutral theory interface

A theory solver is admissible at this layer iff it can provide the following objects in the same explicit conventions:

### Geometry

- `chi(z)` in Mpc;
- `z_of_chi(chi)`;
- `H(z)` in Mpc^-1;
- `f_K(chi) = comoving_angular_diameter_distance(chi)` in Mpc;
- `H0` in Mpc^-1;
- dimensionless `h`;
- `Omega_m` using the same matter convention as the supplied spectra;
- spatial `curvature` in Mpc^-2 as used by the pinned projection formula;
- `chi_star` in Mpc.

### Dynamic spectra

Three callable/interpolated spectra evaluated at physical `k` in Mpc^-1 and redshift `z`:

- `P_WW(k,z)` = Weyl-potential auto spectrum in the pinned solver convention;
- `P_Wm(k,z)` = Weyl × matter-without-neutrinos cross spectrum;
- `P_mm(k,z)` = matter-without-neutrinos auto spectrum.

The adapter must not infer one of these spectra from another via a GR Poisson equation. They are independent inputs to the bridge so modified-gravity/slip information is not quotiented away by construction.

### Tracer kernels

For each tracer sample:

- `dNdz(z)` cross-match redshift distribution;
- `bdNdz(z, pcs=True)` cross-correlation redshift distribution and optional dN/dz PC columns;
- integer `n_pcs`.

## Frozen projection scope

Exp066A tests the no-CLEFT raw basis, i.e. the exact branch of the pinned `compute_raw_spectra` with

- `cleft_interpolations_dtot_dnonu = None`;
- `cleft_interpolations_dnonu_dnonu = None`;
- no cross-sample `gg` spectrum;
- no redshift-cosmology correction (`cross_correlation_redshift_correction=None`).

This does **not** claim that CLEFT is unnecessary for the published baseline likelihood. It isolates the cosmological projection basis before nonlinear/nuisance closure. Exp066B must later bind nuisance/CLEFT and survey bandwindows separately.

The raw outputs compared are exactly:

- `kg.kg_b`;
- `kg.kg_nob` (zero in this frozen no-CLEFT branch);
- `kg.kmu`;
- `gg.gg_bsq`;
- `gg.gg_b` (zero in this branch);
- `gg.gg_nob` (zero in this branch);
- `gg.gmu_b`;
- `gg.gmu_nob` (zero in this branch);
- `gg.mumu`;
- `bdndz_norm`.

## Frozen numerical regression

Use deterministic analytic mock inputs, not a cosmological theory-family output:

- flat geometry with monotonic analytic `chi(z)` / exact inverse;
- positive analytic `H(z)`;
- fixed `Omega_m`, `H0`, `h`, `chi_star`;
- two positive smooth tracer kernels, one with no dN/dz PCs and one with exactly one PC;
- smooth positive analytic `P_WW`, `P_mm` and sign-fixed nonzero `P_Wm` over the full sampled `(k,z)` domain;
- `ell = [10, 30, 80, 150, 300]`;
- `zmin=0`, `zmax=3`, `kmax` chosen above the maximum sampled Limber k;
- Gauss-Legendre order `N=96`.

The official reference source is loaded from the pinned upstream commit. The DSIR adapter and upstream method receive the **same mock objects and quadrature settings**.

## Frozen PASS criteria

`PASS_SOLVER_NEUTRAL_RAW_PROJECTION_EQUIVALENCE_V0_1` iff:

1. pinned upstream commit is exact;
2. source audit confirms the reference method still requests/uses the three independent spectra and the geometry operations listed above;
3. every compared raw array has exactly the same shape;
4. all reference and DSIR outputs are finite;
5. for every non-identically-zero raw component,
   `max_abs(DSIR-reference) <= 5e-13 * max(1, max_abs(reference))`;
6. every branch expected to be algebraically zero in the frozen no-CLEFT setup is exactly zero in both implementations;
7. changing only `P_WW`, only `P_Wm`, and only `P_mm` in three independent deterministic perturbation controls changes the expected disjoint raw component groups, proving the adapter did not collapse the three inputs into one GR-derived spectrum.

No tolerance, ell node, tracer kernel, quadrature order, component list or perturbation control may change after first regression output.

Any failure is preserved as `FAIL_SOLVER_NEUTRAL_RAW_PROJECTION_EQUIVALENCE_V0_1`.

## Scientific consequence

A PASS establishes algebraic solver-neutrality of the raw projection basis only. It does not validate a new cosmology solver against ACT data and does not close G7.

After PASS, Exp066B may freeze nuisance/CLEFT handling plus released bandwindow/transfer operators and test full selected-bandpower equivalence on a reference cosmology. Only after that may one training-only covariance-whitened cross-channel relation and null statistic be preregistered.

Top-level state remains **G7 OPEN, G8 OPEN, G9 OPEN**.
