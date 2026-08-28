# Exp073P classifying-executor readiness gap — 2026-08-28

## Scope

Prospective implementation/readiness audit performed while Exp073R1 run `33108733415` is still in progress. This note does **not** evaluate any Exp073P support fraction and does not alter any frozen scientific criterion.

## Bound frozen contract

Authoritative preregistration remains:

`experiments/073p_cosmotheka_desy1_boss_exact_common_physical_support_prereg_v0_1.md`

The classifying implementation must preserve, without modification:

- common physical rectangle `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- coordinate support acceptance `f_invalid <= 0.05`;
- minimum retained complete-coordinate dimension `15`;
- classifying `nside=4096`;
- P1–P8 exactly as frozen;
- no covariance, whitening, nuisance SVD/rank, quotient/relation/null, G8 or article-selection reads before Exp073P classification.

## Current prerequisite chain verified

Repository currently contains the prospective preparation lineage:

1. DES public input checksum/preflight workflows (`exp073p-*checksum*`);
2. DES FITS schema/row-layout probes (`exp073q*`);
3. Exp073S0 redMaGiC mask+n(z) reproduction;
4. Exp073R0 raw-row→HEALPix equivalence;
5. Exp073R1 full one-pass weak-lensing-mask reproduction.

At audit time, Exp073R1 run `33108733415` has completed R0 parent binding and runtime installation and remains inside `Execute frozen Exp073R1 one-pass construction`. No duplicate R1 run is authorized while it is active.

## Readiness gap found

The current default-branch workflow inventory contains the preparation workflows above, but no workflow implementing the **classifying Exp073P common physical-support evaluation** itself. In particular, no existing `exp073p-*` workflow presently performs all of the following in one immutable classifying record:

- bind a genuine successful Exp073R1 artifact;
- bind the frozen BOSS finite-matrix mm component;
- reconstruct the pinned Cosmotheka finite NaMaster response/window semantics for DES Wm/WW;
- propagate positive absolute response envelopes through the frozen lens/source kernels to `(k,z)`;
- compute denominator and out-of-rectangle numerator for each complete coordinate;
- compute `f_invalid` and apply only the frozen 5% criterion;
- combine per-block valid-support masks only after block-local evaluation;
- count retained complete observation coordinates and apply the frozen dimension `>=15` rule;
- emit one of the frozen Exp073P classifications while retaining coordinate-level diagnostics and provenance;
- attest `covariance_read=false`, `whitening_read=false`, `nuisance_read=false`, `quotient_read=false`, `G8_read=false`.

This is an **implementation/readiness gap**, not a scientific FAIL and not an infrastructure failure.

## Exact next admissible implementation package

After Exp073R1 completes successfully and its artifact passes the already-frozen post-R1 integrity checks, the next scientific implementation must be a dedicated Exp073P executor with these hard boundaries:

1. refuse execution unless the supplied parent run is completed/successful and corresponds to `.github/workflows/exp073r1-desy1-full-onepass-weak-lensing-mask-v0-1.yml`;
2. download exactly one non-expired `exp073r1-desy1-full-mask-*` artifact and verify its internal `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` contract, source/metacal row counts and recomputed SHA256 values;
3. bind all other prospectively frozen DES release checksums and the pinned Cosmotheka commit before any support fraction is computed;
4. compute support fractions using only positive response-envelope weight and frozen physical-unit bookkeeping; no fiducial `P(k)` or downstream statistical weighting may enter support evaluation;
5. preserve numerator, denominator, `f_invalid`, pass/fail bit and provenance for every candidate coordinate;
6. classify reproduction/numerical incompleteness separately from trustworthy support-dimension FAIL;
7. upload the immutable record even on failure where possible;
8. do **not** trigger covariance/whitening unless the exact classification is `PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P`.

## Gate state

- validated physical-forward/input reproduction lineage: active, final Exp073R1 prerequisite still running;
- preregistered physical-support validity mask: frozen but not yet evaluated;
- covariance restriction/whitening: BLOCKED;
- nuisance tangent rank/SVD: BLOCKED;
- quotient/relation/null control: BLOCKED;
- fresh G8 withheld family: BLOCKED.

No scientific acceptance criterion was changed by this audit.