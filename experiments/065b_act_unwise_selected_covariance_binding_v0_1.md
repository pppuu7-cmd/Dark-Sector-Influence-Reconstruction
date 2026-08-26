# Exp065B — ACT DR6 × unWISE selected-covariance binding v0.1

Date: 2026-08-26

## Purpose

Correct one precisely identified eligibility mismatch exposed by Exp065A without changing Exp065A's result. Exp065A permanently failed because it tested positive-definiteness of the *unselected* full Blue+Green 236×236 covariance. A post-failure source audit of the pinned official likelihood showed that the actual likelihood first applies its configured `ell` selections to each auto- and cross-covariance via `select_from_matrix`, then assembles the covariance used in the likelihood.

Exp065B asks only whether that **officially selected ACT Blue+Green `Clgg + Clkg` covariance block** is numerically valid and reproducibly bound to the published bandpower/window products.

This is an eligibility/infrastructure experiment, not a G7 law search and not a withheld-family test.

## Immutable provenance

- External likelihood: `ACTCollaboration/unWISExLens_lklh`
- Commit: `6302c30d9e70f8e4ff2d4a84a9977b4471705179`
- Expected code version: `1.0.2`
- Expected data version: `1.0`
- Official data archive URL: `https://portal.nersc.gov/project/act/act_x_unWISE_xcorr+3x2pt/data_unWISExLens.tar.gz`
- Exp065A observed archive SHA256: `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`; Exp065B requires the same digest.

## Frozen samples and channels

Use only the ACT cross-correlation block:

- `Blue_ACT`
- `Green_ACT`

and only the two channels already bound in Exp065A:

- galaxy auto-correlation `Clgg`;
- CMB-lensing × galaxy cross-correlation `Clkg`.

No Planck sample and no `Clkk` is added in this corrective audit.

## Exact official selection semantics

Read the default `lranges_gg` and `lranges_kg` from the pinned `unWISExLensLklh.yaml` and the bin edges from `config_files/binning_setup.yaml`.

For each sample, reproduce the pinned likelihood conditions exactly:

`cond_gg = (lmin_gg <= left_edge) & (right_edge < lmax_gg)`

`cond_kg = (lmin_kg <= left_edge) & (right_edge < lmax_kg)`

The selected covariance index vector is

`selection = concatenate(cond_gg, cond_kg)`.

The audit must also verify that the number of bandpower rows equals the number of bins and that the default pinned ACT ranges are unchanged from the source-audited values:

- `Clgg: [100, 402]`
- `Clkg: [51, 402]`.

No scale cut may be changed after seeing the covariance result.

## Exact matrix selection

Reproduce pinned `select_from_matrix` semantics:

- auto covariance: select rows/columns with the same Boolean selection;
- Blue×Green cross covariance: select Blue rows and Green columns;
- assemble

`C = [[C_Blue, X], [X.T, C_Green]]`.

No eigenvalue clipping, jitter, diagonal loading, shrinkage, projection to nearest PSD matrix, or covariance regularisation is allowed.

## Frozen eligibility criteria

Exp065B is `PASS_ACT_UNWISE_SELECTED_COVARIANCE_ELIGIBLE_V0_1` iff all are true:

1. external git commit and data archive digest match the immutable provenance;
2. the source/config default ACT scale cuts equal the frozen values above;
3. each selected Blue and Green covariance is finite, symmetric, and strictly positive definite (`lambda_min > 0`);
4. the assembled selected Blue+Green covariance is finite, symmetric, and strictly positive definite (`lambda_min > 0`);
5. an unregularised Cholesky decomposition of the assembled selected covariance succeeds;
6. direct inversion succeeds and `||C C^{-1}-I||_inf <= 1e-8`;
7. both samples retain at least one selected `Clgg` and at least one selected `Clkg` bandpower;
8. the pinned likelihood source still contains the same `select_from_matrix` auto/cross-covariance construction.

Any failure gives `FAIL_ACT_UNWISE_SELECTED_COVARIANCE_ELIGIBILITY_V0_1` and is preserved.

## Scientific consequence

A PASS means only that ACT DR6 × unWISE provides a reproducible observational lensing+clustering block with a usable selected covariance and explicit bandwindow/transfer binding. It does **not** itself establish a dark-sector law.

If PASS, the next admissible step is to freeze a solver-neutral forward response/operator and one training-only cross-channel relation/null statistic before selecting any fresh withheld theory family for G8.

If FAIL, this ACT×unWISE route remains ineligible for G7 until a new separately justified observational block is introduced.

Top-level state remains **G7 OPEN, G8 OPEN, G9 OPEN** regardless of the Exp065B eligibility outcome.
