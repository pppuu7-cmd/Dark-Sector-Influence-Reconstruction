# Exp072A — ACT×unWISE angular support/leakage mask preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp072A LEAKAGE FRACTIONS ARE EVALUATED

## Purpose

Exp071A established `PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1` for the certified C3/GDM and C5/designer-f(R) provider coordinates. Per the pre-existing boundary in `docs/G7_LINEAR_OBSERVATIONAL_VALIDITY_MASK_BOUNDARY_2026-08-26.md` and the pre-execution clarification `docs/EXP071A_PHYSICAL_SUPPORT_VS_OBSERVATIONAL_LEAKAGE_BOUNDARY_2026-08-27.md`, provider-space support is not itself an ACT×unWISE observable mask.

Exp072A therefore freezes, before inspecting any 26-coordinate support fraction, a model-amplitude-independent positive operator-support statistic using the released Blue/Green tracer kernels and released ACT bandwindow/transfer operators. Its only scientific output is a deterministic angular-coordinate eligibility mask for the existing 26 selected observables.

Exp072A does **not** fit ACT data, inspect covariance conditioning, compute a Cholesky factor, inspect nuisance singular values, fit a G7 relation, select a G8 family, or make a dark-sector/new-physics claim.

## Immutable upstream/data provenance

Use exactly:

- `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764` only for the same frozen R0 geometry used by Exp068B;
- official `data_unWISExLens.tar.gz`;
- archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`.

Any provenance mismatch is a hard Exp072A FAIL. Data download failure before evaluation is infrastructure `INCOMPLETE_EXP072A`, not scientific FAIL.

## Training-family set frozen before evaluation

The eventual G7 training-side physical families represented by this common support are frozen as:

### C3 / GDM

The three Exp070C-certified cases:

- `cs2=0`;
- `cs2=1e-6`;
- `cs2=1e-5`.

### C5 / designer f(R)

The Exp069H-certified production case:

- `B0=1e-6`;
- q=3 general-accuracy provider;
- unmodified pinned upstream solver.

No fresh withheld family enters Exp072A. No G8 response may be inspected.

## Exp071A common support input

The immutable Exp071A rerun is:

- run `33027562195`;
- artifact `9629064009`;
- artifact digest `sha256:4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675`;
- classification `PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1`;
- 495/495 provider cells retained;
- blocks `[mm, Wm, WW]`;
- common redshift nodes `[0.295, 0.51, 0.934, 1.491, 2.33]`;
- 33 common physical k nodes, from `0.000704833374744468` through `0.06664762008318016 Mpc^-1`.

The evaluator must bind these values exactly and may not substitute a later support result.

## Support-envelope interpretation frozen here

Exp071A certified provider values on discrete nodes. Exp072A requires only a **coordinate support indicator** for survey-operator geometry; it does not authorize interpolation of physical power amplitudes.

For the nominal support indicator `V0`, use only the closed node-spanned coordinate envelope of the Exp071A retained grid:

- `0.295 <= z <= 2.33`;
- `0.000704833374744468 <= k <= 0.06664762008318016 Mpc^-1`;
- all three physical blocks `mm`, signed `Wm`, `WW` are available.

This envelope is not a new amplitude provider. No `P_mm`, `P_Wm`, or `P_WW` value may be interpolated or extrapolated in Exp072A.

For the frozen tightening/robustness indicator `V1`, remove exactly one retained boundary layer in both coordinates:

- `0.51 <= z <= 1.491`;
- `0.0008873326465464519 <= k <= 0.06436130985291577 Mpc^-1`.

No other tightening may be chosen after output inspection.

## Frozen ACT×unWISE candidate coordinates

Use exactly the 26 Exp065B-selected coordinates in the original released covariance ordering:

1. Blue ACT `Clgg`: midpoints `[126.5, 176.5, 226.5, 276.5, 326.5, 376.5]`;
2. Blue ACT `Clkg`: midpoints `[76.5, 126.5, 176.5, 226.5, 276.5, 326.5, 376.5]`;
3. Green ACT `Clgg`: the same six `Clgg` midpoints;
4. Green ACT `Clkg`: the same seven `Clkg` midpoints.

The official scale cuts remain exactly:

- `Clgg: [100, 402]`;
- `Clkg: [51, 402]`.

No coordinate may be added or removed before its preregistered leakage statistic is evaluated.

## Frozen survey geometry and integration

Exactly inherit the validated Exp068B no-CLEFT survey geometry:

- R0 flat LCDM geometry: `H0=67 km/s/Mpc`, `ombh2=0.0224`, `omch2=0.1200`, `mnu=0`, `nnu=3.046`, `TCMB=2.7255 K`, `YHe=0.24`, `As=2.10e-9`, `ns=0.965`, `w=-1`;
- raw multipoles `ell=0,...,6143`;
- `zmin=0`, `zmax=3`;
- Gauss-Legendre order `N=96`;
- physical mapping `k=(ell+1/2)/f_K(chi)`;
- released Blue/Green xmatch/cross-correlation/mean+PCA tracer files bound under the literal Exp068B convention.

Use the exact released ACT files selected by pinned `binning_setup.yaml`:

- Blue transfer `transfer_unWISExACT-DR6_blue_baseline.dat`;
- Blue bandwindow `bandwindow_unWISExACT-DR6_Clgg+Clkg.npy`;
- Green transfer `transfer_unWISExACT-DR6_green_baseline.dat`;
- Green bandwindow `bandwindow_unWISExACT-DR6_Clgg+Clkg.npy`.

For the signal part use the exact effective released operator already validated in DSIR:

`bandpower = transfer * (bandwindow @ raw_Cl)`.

No coupling-matrix inversion is needed for the signal contribution, and no shot-noise template enters this support statistic.

## Positive nuisance-envelope kernel statistic

The support statistic must be independent of model power amplitudes and independent of fitted nuisance values.

At each Gauss-Legendre node `i`, raw multipole `ell`, sample `s`, and physical block, construct nonnegative survey-kernel envelopes from the full no-CLEFT raw basis used by Exp068B:

### `Clkg`

- `Wm` envelope: sum over every literal `bdNdz(z, pcs=True)` column of `abs(bdndz_h_col * kappa_kernel)`;
- `WW` envelope: `abs(mu_kernel * kappa_kernel)`;
- `mm` envelope: zero / not used by `Clkg` in the frozen no-CLEFT basis.

### `Clgg`

- `mm` envelope: sum over every ordered pair of literal `bdNdz(z, pcs=True)` columns of `abs(bdndz_h_a * bdndz_h_b)`;
- `Wm` envelope: sum over every literal `bdNdz(z, pcs=True)` column of `abs(mu_kernel * bdndz_h_col)` with the physical factor-of-two multiplicity retained;
- `WW` envelope: `abs(mu_kernel^2)`;

The algebraically zero CLEFT slots remain zero and contribute no support weight.

Include the positive Gauss-Legendre quadrature factor and the common `Delta chi / 2`. Do not multiply by any model `P(k,z)` amplitude.

For each released bandpower row `b`, raw multipole `ell`, and survey component, multiply the nonnegative kernel envelope by

`abs(transfer_b * bandwindow[b,ell])`.

Signed bandwindow lobes are therefore counted by absolute operator weight rather than allowed to cancel. This is intentional: the statistic measures dependence on physical support, not net signal cancellation.

## Frozen invalid-support fraction

For candidate coordinate `j`, let `w_j(i,ell,block) >= 0` be the complete positive operator weight defined above.

For support indicator `V`, define

`L_j(V) = sum w_j * 1[(z_i,k_iell,block) not in V] / sum w_j`.

Requirements:

- denominator must be finite and strictly positive;
- every `L_j` must be finite and satisfy `0 <= L_j <= 1` up to a numerical guard `64*eps(float64)`;
- no signal amplitude, covariance element, nuisance singular value, relation residual, or held-out result may enter `L_j`.

The **nominal frozen leakage threshold is**

`L_j(V0) <= 0.05`.

This 5% maximum invalid-support fraction is frozen before evaluating the 26 fractions and may not be relaxed after seeing how many coordinates survive.

The nominal observable mask is

`M0_j = [L_j(V0) <= 0.05]`.

## Frozen robustness check

Using the already-frozen one-layer-tightened support `V1`, compute

`L_j(V1)`

with the identical operator weights and threshold 0.05.

Define

`M1_j = [L_j(V1) <= 0.05]`.

Require as an implementation/ordering control that `M1` is a subset of `M0` and that `L_j(V1) >= L_j(V0) - 64*eps(float64)` for every coordinate.

The tightened-mask retained count and per-channel counts are reported as a **robustness diagnostic only**. They do not change the nominal 5% mask and are not grounds to retune `V0` or the threshold.

## Hard acceptance semantics

Exp072A scientific PASS requires all of the following:

A1. exact upstream/CAMB/archive provenance;

A2. exact binding of the immutable Exp071A PASS support coordinates and its 495/495 retained-cell result;

A3. exact 26-coordinate ordering and official scale cuts from Exp065B;

A4. finite/nonzero positive survey-operator denominators and finite leakage fractions for all 26 coordinates;

A5. nominal 5% leakage mask computed exactly as frozen;

A6. the nominal mask retains at least one `Clgg` and one `Clkg` coordinate for each of Blue and Green;

A7. total nominal retained dimension is at least 15. This cardinality is frozen from the pre-existing no-CLEFT structural nuisance-direction upper bound of 14, so that the retained observation space is not guaranteed to be exhausted by nuisance directions before their numerical rank is inspected;

A8. tightened-support monotonicity/subset controls pass;

A9. evaluator asserts that covariance conditioning/Cholesky, nuisance SVD/rank, G7 relation/null, G8 responses and article-selection quantities were not read.

PASS label:

`PASS_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`.

If A1-A9 are evaluated and any hard criterion fails, classify:

`FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`.

A scientific FAIL must be preserved and must **not** be rescued by relaxing 5%, changing the support envelope, dropping a sample/channel, reducing the required dimension, or switching to signed cancellation weights.

Infrastructure failure before the complete scientific evaluation is `INCOMPLETE_EXP072A` and may be rerun only with the frozen contract unchanged.

## Downstream authorization

A scientific PASS authorizes only:

1. construction of the deterministic selection matrix `S_M` from `M0`;
2. a separately preregistered covariance-submatrix/no-repair Cholesky experiment on `Sigma_M = S_M Sigma S_M^T`.

Exp072A does not itself authorize nuisance SVD, quotienting, G7 fitting, G8 selection, or G9.

A scientific FAIL means the present certified C3+C5 support is insufficient for the frozen ACT×unWISE G7 observable route. The next corrective experiment, if any, must extend/certify physical provider support or change the observational route under a new prospective contract; it may not retune Exp072A.

## Gate state

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
