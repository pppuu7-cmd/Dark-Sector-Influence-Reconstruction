# Exp073N — DES harmonic Wm+WW + BOSS mm exact common physical-support audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073N PHYSICAL-SUPPORT OUTPUT

## 1. Parent binding

Bind permanently:

- Exp073M = `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M`;
- Exp073L = `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`;
- Exp073J KiDS component remains `FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`;
- BOSS finite-matrix mm component remains 54/240 retained and non-classifying;
- common C3+C5 physical rectangle remains exactly `0.295 <= z <= 2.33` and `k <= 0.06664762008318016 Mpc^-1`;
- positive invalid-support threshold remains exactly `f_invalid <= 0.05`;
- minimum retained full-observation dimension remains exactly 15.

No parent result or threshold may be weakened by Exp073N.

## 2. Frozen observational route

Use only:

- **mm:** the already frozen BOSS finite true-k matrix component from Exp073I/J, unchanged;
- **Wm:** DES Y3 harmonic galaxy-galaxy lensing operator from the public pseudo-C_ell measurement route bound in Exp073M;
- **WW:** DES Y1 harmonic cosmic-shear operator from the public pseudo-C_ell measurement route bound in Exp073M.

The operator source is pinned to `hocamachoc/3x2hs_measurements@21e589a3cfc3e30f1b06a4636ccc2da8aceda5ab`. No DES Y3 shear code available only by request may replace the chosen WW route inside Exp073N.

## 3. Mandatory pre-output source binding

Before evaluating any physical-support fraction, bind and record SHA256 (or immutable release identifiers plus SHA256 after download) for every public input actually used:

1. DES Y3 lens/source redshift distributions for the selected harmonic Wm analysis;
2. DES Y1 source redshift distributions for the harmonic WW analysis;
3. survey masks or exact released mask products required to reproduce the NaMaster coupling workspaces, if the workspaces themselves are not released;
4. every finite ell-bin definition;
5. every precomputed workspace/bandpower-window file if public files are used instead of recomputation;
6. exact NaMaster version/source identity used for a recomputed workspace;
7. BOSS finite-matrix parent identifiers already frozen in Exp073I/J.

If any required public source cannot be reproduced or bound before support output, classify `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`; do not substitute a private/request-only file or approximate mask.

## 4. Frozen operator semantics

For each DES Wm/WW tomographic pair:

1. construct or reproduce the finite signed pseudo-C_ell bandpower operator exactly from the pinned measurement semantics;
2. retain its finite ell response/mode-coupling structure, not an effective-ell or top-hat surrogate;
3. map each true ell contribution into `(k,z)` through the released lens/source kernels and the same distance convention frozen for the DSIR support audit;
4. define a **positive support envelope only after the signed observable operator exists**, using absolute operator weights times non-negative geometric/redshift quadrature weights;
5. normalize each positive envelope over its complete finite released/operator support.

No fiducial `P(k)`, `C_ell`, theory amplitude, covariance, nuisance direction or fitted cosmology may enter this support normalization.

## 5. Frozen support rule

For every observation-coordinate/block pair, define

`f_invalid = positive support outside the common C3+C5 rectangle / total positive support`.

A pair passes iff `f_invalid <= 0.05`.

A full observation coordinate is retained only when all blocks required by its already-defined observable semantics pass. Do not drop an inconvenient tomographic pair, ell band or block after seeing support results unless its exclusion was already part of the published estimator definition bound before output.

The combined route passes only if the block-aware retained full-observation dimension is at least 15 under the unchanged rule.

## 6. Frozen controls N1–N10

### N1 — parent/provenance reproduction
All parent classifications, source pins and required public-file hashes reproduce exactly.

### N2 — finite operator reproduction
Every used DES Wm/WW bandpower has a finite reproducible bandpower response/workspace under the pinned pseudo-C_ell semantics.

### N3 — signed Wm
The physical Wm operator remains signed. Absolute value is permitted only in the support envelope after operator construction.

### N4 — independent WW
WW is constructed from the shear-shear estimator and is not derived from matter by a GR closure.

### N5 — exact redshift kernels
Released DES source/lens redshift distributions and tomography are used without replacing them by effective redshifts.

### N6 — no post-hoc angular cutoff
No ell cutoff or band removal may be selected after inspecting support leakage.

### N7 — common physical rectangle
Use exactly `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`.

### N8 — unchanged acceptance
Use exactly `f_invalid <= 0.05` and minimum retained dimension 15.

### N9 — no downstream leakage
No covariance, whitening, nuisance SVD/rank, quotient/relation/null residual, G8 or held-out quantity may be read or used.

### N10 — deterministic/repeatable accounting
Repeated support evaluation from identical bound inputs must reproduce coordinate/block fractions and retained masks within a frozen numerical tolerance of `1e-10` absolute unless a stricter exact-array equality is available.

## 7. Frozen classifications

If N1–N10 pass and the combined block-aware retained full-observation dimension is at least 15, classify

`PASS_DES_HARMONIC_COMMON_PHYSICAL_SUPPORT_EXP073N`.

If N1–N10 are trustworthy but the retained dimension is below 15, classify

`FAIL_DES_HARMONIC_COMMON_PHYSICAL_SUPPORT_EXP073N`.

This is a scientific support FAIL and must be preserved.

If source/operator reproduction is insufficient to trust the support fractions, classify

`FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`.

Infrastructure interruption before complete evaluation is `INCOMPLETE_EXP073N` and is not a scientific result.

## 8. Downstream boundary

Only `PASS_DES_HARMONIC_COMMON_PHYSICAL_SUPPORT_EXP073N` authorizes the next G7 stage: preregistered covariance restriction/whitening on the retained observational coordinates.

A support FAIL does not authorize changing the 5% threshold, common rectangle, minimum dimension, ell range or survey/operator after output. Any new observational route requires a new prospective experiment.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
