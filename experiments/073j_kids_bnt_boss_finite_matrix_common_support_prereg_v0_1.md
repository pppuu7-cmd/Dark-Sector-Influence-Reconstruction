# Exp073J — KiDS-BNT + BOSS finite-matrix common physical-support audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073J SUPPORT FRACTION IS EVALUATED

## Parent binding

Bind `PASS_FINITE_TRUE_K_WINDOW_MATRIX_SOURCE_BINDING_EXP073I` and preserve Exp073G/Exp073H negative operator results unchanged. Exp073I authorizes only this support audit.

## Frozen support domain

Use exactly the inherited common C3+C5 physical rectangle:

- `0.295 <= z <= 2.33`;
- `0.000704833374744468 <= k <= 0.06664762008318016 Mpc^-1`;
- maximum positive invalid-support fraction per retained observational coordinate: `0.05`.

No threshold, unit convention or support boundary may be changed after observing Exp073J output.

## Frozen operators

- Wm/WW: the already-bound KiDS-1000+BNT lens/source operators from the Exp073F/G chain, with signed Wm semantics preserved;
- mm: BOSS DR12 z3 (`0.5<z<0.75`) NGC/SGC finite matrices bound by Exp073I, using publication-linked `W` and `M` objects and pinned `fbeutler/pk_tools@707eb2a6a4691c34eae19d7f72047ca4892f528e` semantics.

No covariance value, nuisance fit, relation/null result or G8 output may influence coordinate selection.

## Positive support rule

For every candidate coordinate, construct only operator-based non-negative domination weights. For BOSS, use absolute finite matrix contributions on the explicit theory-k grid; do not multiply by a fiducial `P(k)`. For KiDS-BNT, retain the previously frozen positive kernel-envelope construction. Convert all k coordinates to physical `Mpc^-1` before applying the rectangle; roundtrip unit tolerance remains `2e-8`.

The invalid fraction is positive operator weight outside the inherited rectangle divided by total positive operator weight. No post-hoc k cutoff, covariance weighting or cosmology-dependent damping is allowed.

## Frozen coordinate rule

A coordinate is retained iff every required block for that coordinate has invalid fraction `<=0.05`. Preserve the previously frozen minimum nominal retained dimension of `15`. Candidate coordinates and block membership must be enumerated before classification and may not be selected using their measured values or downstream performance.

## Frozen controls J1-J8

J1 exact Exp073I matrix hashes/shapes and KiDS-BNT operator provenance reproduce.  
J2 all support weights are finite, non-negative and have strictly positive normalization.  
J3 all k/redshift coordinates have explicit unit provenance and unit roundtrip discrepancy `<=2e-8`.  
J4 signed Wm semantics are preserved; support masking uses positive domination only and does not replace the physical signed cross spectrum.  
J5 no fiducial `P(k)`, nonlinear boost/damping or post-hoc cutoff enters support weights.  
J6 no covariance numerical values or nuisance SVD/rank are read.  
J7 no relation/null or G8/held-out information is read.  
J8 retained dimension and all per-coordinate/block invalid fractions are recorded machine-readably.

## Frozen classifications

If J1-J8 pass and retained dimension is at least 15, classify

`PASS_KIDS_BNT_BOSS_FINITE_MATRIX_COMMON_SUPPORT_EXP073J`.

If J1-J8 are trustworthy but retained dimension is below 15, classify

`FAIL_KIDS_BNT_BOSS_FINITE_MATRIX_COMMON_SUPPORT_EXP073J`.

If provenance/reproduction prevents a trustworthy support decision, classify

`FAIL_EXP073J_REPRODUCTION_OR_PROVENANCE`.

Infrastructure interruption before complete evaluation is `INCOMPLETE_EXP073J` and is not a scientific support result.

## Downstream boundary

Only `PASS_KIDS_BNT_BOSS_FINITE_MATRIX_COMMON_SUPPORT_EXP073J` may authorize a separately frozen covariance restriction/whitening step. No nuisance tangent SVD, relation/null calculation or G8 family selection may precede that covariance gate.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
