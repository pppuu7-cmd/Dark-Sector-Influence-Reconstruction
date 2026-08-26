# Exp068A — physical ACT DR6 × unWISE forward-operator reproduction v0.1

**Date:** 2026-08-26  
**Status:** scientific contract frozen before the first Exp068A physical forward comparison.

## Purpose

Exp066A proved algebraic equivalence of the solver-neutral no-CLEFT raw projector to the pinned ACT×unWISE upstream implementation on analytic mock geometry, mock spectra and mock tracers. Exp067E then prospectively certified the physical CAMB↔CLASS Weyl/matter power convention over the frozen LambdaCDM reference envelope.

Before any 26D nuisance tangent quotient or G7 relation is constructed, Exp068A asks the missing physical bridge question:

> On one pinned linear LambdaCDM reference, using real CAMB `P_WW`, `P_Wm`, `P_mm` and the released Blue/Green unWISE redshift kernels and PCA modes, does `src/dsir/act_unwise_projection.py::compute_raw_no_cleft` reproduce the pinned upstream `compute_raw_spectra` output over the full 6144-mode ACT multipole input support?

This is a physical forward-adapter gate only. It does not fit ACT data, does not use a dark-sector family, does not define a G7 law and does not select a G8 withheld family.

## Immutable provenance

Pinned upstream likelihood:

`ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`.

Pinned CAMB:

`cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`.

Official ACT×unWISE data archive:

`data_unWISExLens.tar.gz`, SHA256

`1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`.

Any provenance mismatch is a hard Exp068A FAIL.

## Frozen physical cosmology

Use the Exp067B/067E R0 flat, massless-neutrino LambdaCDM reference:

- `H0=67 km/s/Mpc`, `h=0.67`;
- `ombh2=0.0224`;
- `omch2=0.1200`;
- `omk=0`;
- `mnu=0`, `nnu=3.046`;
- `TCMB=2.7255 K`;
- `YHe=0.24`;
- `As=2.10e-9` at `k_pivot=0.05 Mpc^-1`;
- `ns=0.965`;
- `w=-1`;
- adiabatic scalar initial conditions;
- linear matter/Weyl spectra only; no HALOFIT/HMcode/CLEFT.

CAMB may compute an internal interpolation grid out to `k=12 Mpc^-1`; the projector itself is frozen to `kmax=10 Mpc^-1` and must mask larger Limber k values exactly as the pinned upstream helper does.

## Frozen released tracer inputs

Use the official archive files, with the pinned upstream normalization/interpolation semantics:

Blue:

- `aux_data/dndz/unWISE_blue_xmatch_dndz.txt`;
- `aux_data/dndz/unWISE_blue_xcorr_bdndz.txt`;
- `aux_data/dndz/unWISE_blue_delta_bdndz_pcs.dat`.

Green:

- `aux_data/dndz/unWISE_green_xmatch_dndz.txt`;
- `aux_data/dndz/unWISE_green_xcorr_bdndz.txt`;
- `aux_data/dndz/unWISE_green_delta_bdndz_pcs.dat`.

The expected PCA counts are frozen to Blue `n_pcs=3` and Green `n_pcs=5`. The exact upstream `dN_dz_Helper`, `dNdz` and `cosmo_from_camb` class definitions are to be executed from the pinned source for the reference side; no hand-fitted tracer surrogate is allowed.

## Frozen forward domain

- raw multipoles: every integer `ell=0,1,...,6143` (6144 modes);
- projection redshift interval: `0 <= z <= 3`;
- projector `kmax=10 Mpc^-1`;
- Gauss-Legendre projection order: `N_integration=96`.

The order 96 is deliberately inherited from the already validated Exp066A equivalence path to keep the full 6144-mode physical regression memory-bounded. Exp068A is an implementation-equivalence gate, not a quadrature-convergence claim. Both upstream and DSIR sides must use exactly the same frozen order.

## Physical spectra

From the pinned CAMB R0 result request three independent linear power interpolators in physical units (`hubble_units=False`, `k_hunit=False`):

- `('Weyl','Weyl') -> P_WW`;
- `('Weyl','delta_nonu') -> P_Wm`;
- `('delta_nonu','delta_nonu') -> P_mm`.

The Weyl convention is the Exp067E-certified CAMB convention `W=k^2(phi+psi)/2`. No Poisson reconstruction or forced rank-one replacement is allowed.

## Exact upstream reference

The reference raw projector must be the exact pinned `unWISExLens_theory_model.compute_raw_spectra` no-CLEFT branch, with exact pinned `evaluate_pk_kmax` semantics. The DSIR side is the repository implementation

`src/dsir/act_unwise_projection.py::compute_raw_no_cleft`.

Both receive the same physical CAMB cosmology object, the same released tracer objects and the same three CAMB power interpolators.

## Hard tests

### A1 — provenance

Require exact pinned upstream commit, CAMB commit and official archive SHA256.

### A2 — real tracer binding

Require all six released tracer files to exist and be finite. Require exact PCA counts Blue `3`, Green `5` and finite evaluations of xmatch, xcorr and PCA-expanded `bdNdz` on the frozen projection nodes.

### A3 — physical provider sanity

At fixed probe cells `z={0.5,1.0,2.0}`, `k={0.02,0.10,0.20} Mpc^-1` require finite `P_WW`, `P_Wm`, `P_mm`, with the auto powers strictly positive and cross power nonzero.

### A4 — full raw-component equivalence

For every returned Blue/Green raw component and `bdndz_norm`, require:

1. identical key set;
2. identical array shape;
3. identical finite/non-finite pattern;
4. for finite values,

`max_abs(DSIR-reference) <= 5e-13 * max(1, max_abs(reference))`.

The tolerance is inherited from Exp066A and is frozen before this physical comparison.

If a reference component is identically zero, the DSIR component must be identically zero as well.

### A5 — nontrivial physical signal control

For each real tracer sample require the physical no-CLEFT signal-bearing blocks to be nonzero:

- `kg/kg_b`;
- `kg/kmu`;
- `gg/gg_bsq`;
- `gg/gmu_b`;
- `gg/mumu`;
- `bdndz_norm`.

Require the no-CLEFT-only slots to remain exactly zero:

- `kg/kg_nob`;
- `gg/gg_b`;
- `gg/gg_nob`;
- `gg/gmu_nob`.

This prevents a trivial all-zero equivalence from passing.

## Hard outcome

PASS iff A1–A5 all pass:

`PASS_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1`.

Otherwise:

`FAIL_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1`.

## Anti-retuning

After the first physical comparison, do not change the solver commits, archive, cosmology, tracer files, PCA counts, ell support, z interval, projector kmax, integration order, Weyl/matter variables, no-CLEFT scope or equivalence tolerance to rescue the result.

Infrastructure failures that occur before any physical reference-vs-DSIR comparison may be repaired only if the frozen scientific contract remains unchanged.

## Gate semantics and next step

A PASS validates the missing physical ΛCDM ACT×unWISE raw forward adapter on the full 6144-mode input support. It still does not close G7/G8/G9.

Only after a PASS may DSIR freeze the 26D nuisance tangent quotient using the already bound Exp067A covariance/whitener and the selected `[Blue gg6, Blue kg7, Green gg6, Green kg7]` ordering. The nuisance-rank rule must be preregistered before any dark-sector relation is fitted.

A FAIL must be preserved and diagnosed in a separately numbered experiment; the nuisance quotient and G7 law search remain blocked.

Top-level state entering Exp068A: **G7 OPEN, G8 OPEN, G9 OPEN**.