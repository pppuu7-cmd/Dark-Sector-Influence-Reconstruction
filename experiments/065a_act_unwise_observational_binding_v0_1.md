# Exp065A — ACT DR6 × unWISE observational-kernel binding audit v0.1

Date: 2026-08-26

## Scientific purpose

F31/Exp064A excluded the simplest covariance-aware linear relation inside the five-bin DESI ShapeFit AP/growth/shape block. The next admissible step is **not** to add functional flexibility to the same block. It is to bind a genuinely independent lensing/Weyl-sensitive observable block to an explicit survey response operator and covariance.

Exp065A is an **eligibility/provenance audit only**. It does not search for a DSIR law, does not inspect a fresh theory-family response, and cannot close G7/G8/G9.

## Why ACT DR6 × unWISE

The physically closest target would be the ACT DR6 + BOSS `E_G` statistic because it combines lensing, clustering and RSD/velocity information. However, for DSIR a paper-level compressed `E_G` number is not sufficient: the forward operator, scale bins and covariance must be independently reproducible. As of this audit, the exact ACT+BOSS `E_G` analysis is therefore treated as **physics-motivating but not yet machine-binding eligible** until a public scale-bin/covariance/kernel package is identified and validated.

The official ACT `unWISExLens_lklh` release is selected for the first lensing observational binding because it explicitly provides an executable likelihood for the `C_ell^{gg}` and `C_ell^{kappa g}` data vector, covariance blocks including Blue/Green cross-covariance, transfer functions and band-window operators. The likelihood also exposes an ACT-only configuration, avoiding unnecessary Planck mixing in the first binding audit.

## Frozen external provenance before data inspection

Official repository:

`https://github.com/ACTCollaboration/unWISExLens_lklh`

Pinned commit:

`6302c30d9e70f8e4ff2d4a84a9977b4471705179`

Pinned code version declared by that commit: `1.0.2`.
Pinned data version declared by that commit: `1.0`.

Official archive URL declared by the repository:

`https://portal.nersc.gov/project/act/act_x_unWISE_xcorr+3x2pt/data_unWISExLens.tar.gz`

The first successful Exp065A run must record the archive SHA256. A later hard pin may use that recorded digest; the digest may not be invented before the archive is downloaded.

## Frozen ACT-only observable block

Samples:

- `Blue_ACT`
- `Green_ACT`

Observable channels required in each sample:

- galaxy auto-correlation `C_ell^{gg}`;
- CMB-lensing × galaxy cross-correlation `C_ell^{kappa g}`.

The first audit excludes `C_ell^{kappa kappa}` and excludes Planck. This keeps the binding minimal while still coupling a matter-tracer block to a lensing/Weyl-sensitive block.

## Hard eligibility checks

The audit is PASS only if all conditions hold on the official archive and pinned code:

1. pinned Git commit matches exactly;
2. code declares `__version__ = 1.0.2` and `__data_version__ = 1.0`;
3. extracted data expose `bandpowers`, `covariances`, and `aux_data` under one data root;
4. official ACT Blue/Green bandpower files exist and are finite, with strictly increasing effective multipole and at least the four columns expected by the likelihood (`ell`, `gg`, auxiliary/kk slot, `kg`);
5. Blue and Green covariance matrices are finite, symmetric and positive definite;
6. the official `Blue_ACT_X_Green_ACT` cross-covariance exists with compatible shape, and the assembled Blue+Green covariance is symmetric and positive definite;
7. the ACT band-window file required by both samples exists and contains finite `gg` and `kg` `coupling` and `bandwindow` matrices;
8. both ACT transfer-function files exist, are finite and expose at least `(ell, gg, kg)` columns;
9. at least two redshift-distribution / dN/dz auxiliary files are discoverable in the official auxiliary tree;
10. the pinned likelihood source explicitly loads `gg` and `kg` from the same sample data vector and constructs provided cross-covariance blocks rather than silently assuming them zero.

No missing required cell may be replaced by zero.

## Output and interpretation

The run emits a JSON summary containing the archive SHA256, discovered data root, dimensions/eigenvalue controls and required-file inventory. Scientific state after either PASS or FAIL remains:

- `G7 = OPEN`
- `G8 = OPEN`
- `G9 = OPEN`

A PASS means only: **ACT DR6 × unWISE is eligible as a reproducible observational kernel/covariance block for a later DSIR forward-binding experiment.** It is not evidence for a residual law.

A FAIL is preserved and the release is not used for G7 until the specific reproducibility problem is resolved without weakening the frozen checks.