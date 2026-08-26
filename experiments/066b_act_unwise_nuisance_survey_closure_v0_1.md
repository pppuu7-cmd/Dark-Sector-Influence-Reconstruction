# Exp066B — ACT × unWISE nuisance + survey-operator closure v0.1

Date: 2026-08-26

## Purpose

Exp065B established a valid selected 26-dimensional ACT DR6 × unWISE covariance. Exp066A established a solver-neutral raw projection interface with independent `P_WW`, `P_Wm`, and `P_mm` inputs. Exp066B freezes the next layer only:

`raw cosmological basis -> nuisance/CLEFT algebra -> pixel window -> released NaMaster bandwindow/coupling -> released transfer -> official XCorrACT selected bins`.

This is an algebraic closure regression. It uses deterministic synthetic raw basis arrays so that every nuisance/CLEFT term is nonzero and separately testable. It does not fit ACT data, does not generate a dark-sector family response, and does not define a G7 law.

## Immutable provenance

- upstream: `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- data archive SHA256: `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`;
- samples: `Blue_ACT`, `Green_ACT` only;
- official selected cuts inherited unchanged from Exp065B: `Clgg=[100,402]`, `Clkg=[51,402]`;
- pixel-window nside: 2048, matching the pinned likelihood.

## Frozen synthetic nuisance/CLEFT contract

Use the full raw multipole grid required by the released ACT NaMaster operators. Construct two deterministic synthetic raw-spectrum dictionaries with no stochasticity:

- Blue synthetic dN/dz basis: `n_pcs=0` (`kg_b` has one column);
- Green synthetic dN/dz basis: `n_pcs=2` (`kg_b` has three columns), exercising the PCA branch;
- CLEFT coefficient-vector length: exactly 3;
- every nonzero raw basis term varies smoothly with ell and is nonzero:
  `kg_b`, `kg_nob`, `kmu`, `gg_bsq`, `gg_b`, `gg_nob`, `gmu_b`, `gmu_nob`, `mumu`, `bdndz_norm`;
- nonzero deterministic noise-bias arrays are supplied for `kg_b`, `gg_bsq`, `gg_b`, and `gmu_b`;
- frozen nuisance values:
  - bias `[1.37, 1.82]`;
  - magnification slopes `[0.31, 0.47]`;
  - Green PCA user coefficient list `[0.23]`, so the upstream `pca_coeff_final` is `[1,1,0.23]`; Blue uses `[1]`;
  - fake CLEFT coefficient provider returns `[0.71,-0.29,0.43]` for both samples, independent of kwargs;
  - shot noise passed to survey binning: `[2.4e-7, 3.1e-7]`.

All `cl_*` switches are left at their upstream default inclusive state. `want_gg_cross=False`.

The synthetic arrays and nuisance values above are frozen before first closure output and may not be changed based on the result.

## Frozen nuisance-combination equations

The DSIR implementation must reproduce the pinned upstream `evaluate(..., get='all')` semantics exactly, including:

- dN/dz PCA coefficient construction;
- `b -> b / dot(bdndz_norm,pca_coeff_final)` normalization;
- CLEFT contraction order;
- magnification factor `(5s-2)`;
- default `b_gmu=b`;
- noise-bias subtraction positions;
- all leading/CLEFT/magnification terms in `gg` and `kg`.

The reference is the exact pinned class executed from source with a deterministic fake CLEFT helper; no reimplementation is used as the reference.

## Frozen survey-operator order

For each sample, use the released ACT NaMaster coupling/bandwindow matrices and transfer functions exactly as the pinned likelihood does.

For `gg`:

1. use the final synthetic theory `C_ell^gg` on the released input-ell grid;
2. multiply by `healpy.pixwin(2048)^2` on those input ells;
3. call NaMaster binning with the frozen white-noise value;
4. multiply the resulting bandpowers by the released `gg` transfer column;
5. retain only the official Exp065B `Clgg` selection.

For `kg`:

1. use the final synthetic theory `C_ell^{kappa g}` on the released input-ell grid;
2. no lensing-likelihood correction is used in this frozen closure test;
3. multiply by `healpy.pixwin(2048)`;
4. NaMaster-bin with no white noise;
5. multiply by the released `kg` transfer column;
6. retain only the official Exp065B `Clkg` selection.

The DSIR survey implementation is compared to the exact pinned `NaMasterPowerSpectrumBinning` source loaded from upstream. The released matrices/transfer files are shared inputs, not re-fitted quantities.

## Frozen PASS criteria

`PASS_ACT_UNWISE_NUISANCE_SURVEY_CLOSURE_V0_1` iff all are true:

1. pinned upstream commit and archive SHA256 match;
2. source audit confirms the frozen nuisance formulas and survey-order tokens remain in the pinned files;
3. DSIR nuisance-combined `gg` and `kg` arrays match exact upstream `evaluate` with identical shape and
   `max_abs(delta) <= 5e-13 * max(1,max_abs(reference))`;
4. DSIR NaMaster+transfer selected bandpowers match the exact upstream binning helper with the same tolerance;
5. exactly 6 selected `gg` and 7 selected `kg` bins per sample are produced (26 total);
6. all outputs are finite;
7. four deterministic sensitivity controls have the expected locality:
   - changing only shot noise changes selected `gg` and not selected `kg`;
   - changing only a `kg_nob` CLEFT raw term changes `kg` but not `gg`;
   - changing only `mumu` changes `gg` but not `kg`;
   - changing only Green's PCA coefficient changes Green outputs but leaves Blue outputs unchanged.

No tolerance, operator order, selected bins, nuisance values, synthetic basis, CLEFT vector, or sensitivity definition may change after first output.

A failure is preserved as `FAIL_ACT_UNWISE_NUISANCE_SURVEY_CLOSURE_V0_1` and does not trigger retuning.

## Scientific consequence

A PASS establishes a reproducible algebraic route from the solver-neutral raw basis to the exact selected ACT × unWISE observable coordinates, with nuisance and survey operations explicit. It still does not validate a non-GR solver on a real cosmology and does not close G7.

If PASS, the next experiment may perform one fixed reference-cosmology end-to-end backend regression (Exp066C) before a covariance-whitened G7 relation search. A fresh G8 withheld theory family remains forbidden until the G7 relation/statistic is frozen.

Top-level state remains **G7 OPEN, G8 OPEN, G9 OPEN**.
