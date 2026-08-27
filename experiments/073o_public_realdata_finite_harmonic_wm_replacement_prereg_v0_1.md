# Exp073O — public real-data finite harmonic Wm replacement operator search — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073O CANDIDATE CLASSIFICATION

## 1. Motivation and parent preservation

Exp073N completed as `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE` because the exact frozen DES Y3 Wm real-data NaMaster realization could not be reproduced from the pinned public operator source before any support output.

Preserve permanently:

- Exp073M = `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M` as an operator-class landscape result;
- Exp073N = `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`;
- Exp073L = `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`;
- Exp073J KiDS component = `FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`;
- BOSS finite-matrix mm component = 54/240 retained and non-classifying;
- common physical rectangle exactly `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- future support threshold exactly `f_invalid <= 0.05` and minimum retained dimension exactly 15.

Exp073O is a source/operator landscape experiment only. It must not evaluate physical-support fractions.

## 2. Question

Does a **public, immutable, real-data** harmonic/pseudo-C_ell galaxy-shear cross operator exist that can replace the non-reproducible DES Y3 Wm realization while preserving finite positive support and signed Wm semantics?

The preferred search order is:

1. an exact DES Y1 real-data GGL implementation within or directly associated with the already-pinned public `hocamachoc/3x2hs_measurements` lineage;
2. another public survey harmonic galaxy-shear cross release with released finite bandpower windows/workspaces or enough public mask/bin/source information to reproduce them exactly;
3. no configuration-space finite-theta operator may be promoted merely by imposing a post-hoc ell cutoff.

## 3. Frozen O1–O8 criteria

### O1 — public immutable real-data provenance
The candidate must be bound to an exact public source commit/release and must expose a real-data execution/configuration path, not simulations only.

### O2 — finite operator
The candidate must define finite ell bins and a finite pseudo-C_ell/mode-coupling/bandpower response whose positive absolute envelope is normalizable without model weighting.

### O3 — exact public inputs bindable
Lens/source n(z), masks or released workspaces, ell-bin definitions and any catalogue-derived products needed to reproduce the operator must be publicly identifiable and prospectively checksum-bindable.

### O4 — signed Wm
The galaxy-shear cross observable remains signed through measurement/operator construction. Absolute values are permitted only for a later positive-support envelope.

### O5 — no GR closure
The Wm estimator must be a direct cross observable and not derived from matter power using a GR Poisson/slip closure.

### O6 — no model/downstream weighting
No fiducial P(k), C_ell, covariance, nuisance direction, relation/null residual or G8 information may be needed to make the support finite or choose the candidate.

### O7 — exact support audit remains possible
The public source must contain enough angular and redshift information for a later separately preregistered mapping into the unchanged common rectangle.

### O8 — provenance completeness
Every PASS claim must cite exact source paths/blobs/releases. Publication statements alone cannot override missing source behavior.

## 4. Frozen classifications

If a candidate passes O1–O8, classify

`PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`.

If the audited public landscape contains no candidate satisfying O1–O8, classify

`NO_PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`.

If source access or reproduction is too incomplete to trust the landscape audit, classify

`FAIL_EXP073O_REPRODUCTION_OR_PROVENANCE`.

Infrastructure interruption is `INCOMPLETE_EXP073O` and is not a scientific result.

## 5. Downstream boundary

A FOUND result authorizes only a new prospectively frozen exact physical-support audit using the replacement Wm operator, existing independent WW route if still reproducible, and frozen BOSS mm component.

It does not reopen Exp073N, does not authorize changing the 5% threshold/common rectangle/minimum dimension, and does not authorize covariance, SVD, relation/null or G8.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
