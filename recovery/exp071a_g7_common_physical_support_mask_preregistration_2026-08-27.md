# DSIR Exp071A preregistration — common physical support-validity mask

Date frozen: 2026-08-27
Stage: G7, immediately after validated physical forward/power-input bridges
Status: PREREGISTERED; mask not yet evaluated

## Purpose

Freeze the rules for the common physical support-validity mask before inspecting any downstream quotient/relation/null statistic. The mask is a domain/physical-validity object only. It must not be optimized for model separation, rank, singular values, null strength, residual size, desired signs, or downstream significance.

## Inputs authorized

Only already-certified G7 physical providers may enter this mask:

- C3/GDM: Exp070C certified provider.
- C5/designer-f(R): Exp069H q=3 unmodified-upstream provider.

Previously failed/non-certified providers (including Exp069B q=1) are provenance/control evidence only and may not define accepted support.

The physical blocks are frozen as `[P_mm, signed P_Wm, P_WW]`. Provider-native metadata, units, variable definitions, k convention and redshift convention must be retained. No nonlinear correction may be silently introduced.

## Canonical support construction

1. Start from the pre-existing G7 target coordinates requested by the certified providers. The canonical candidate support is the exact intersection of coordinates simultaneously covered by every certified provider. Do not extrapolate beyond a provider's native/requested domain.
2. A coordinate may be mapped to the canonical support only by an interpolation rule already used by that provider's certification or by exact coordinate identity. No new smoothing, denoising, renormalization, floor subtraction, clipping, or response-dependent interpolation is allowed.
3. Masking is block-aware. A `(z,k,block)` cell is retained only when the corresponding provider quantity is available and physically interpretable for every certified provider. A failure in one block does not authorize silently substituting another block.
4. The common mask is the logical AND over providers for each `(z,k,block)` cell.

## Frozen validity predicates

For every provider and candidate cell, all applicable predicates below must pass:

V1. Execution/provenance validity: the provider record is from its certified pinned solver/source state and requested settings are read back consistently.

V2. Domain validity: finite z and k; k>0; coordinate lies inside the provider's certified/requested support; no extrapolation.

V3. Numerical validity: reported power is finite (not NaN/Inf); no solver error flag or failed accessor; repeated access where available is consistent with the provider certification.

V4. Auto-power physicality: `P_mm > 0` and `P_WW > 0` wherever those autos are used to interpret the cross block. Exact zero is invalid for the corresponding cross-coherence test rather than repaired by a denominator floor.

V5. Signed-cross physicality: preserve the sign of `P_Wm`. Where all three blocks are simultaneously available, require the 2x2 spectral matrix to be positive semidefinite within numerical tolerance, equivalently `P_Wm^2 <= P_mm P_WW * (1 + 1e-6)`. No absolute-value replacement of the signed cross spectrum is allowed.

V6. Certified-boundary integrity: for provider-specific control points used to establish a GR/zero boundary, the already-frozen certification criteria remain binding. The support mask may not rescue a failed provider limit by dropping cells responsible for the certification failure.

V7. No signal-amplitude selection: a cell may not be removed because a model response is small, large, inconvenient, sign-changing, similar to another family, or unfavorable to a later statistic. Production-signal thresholds belong to provider certification, not support selection.

V8. No covariance/rank selection: covariance condition number, whitening behavior, nuisance tangent rank, singular values, relation/null residuals, or held-out performance may not be consulted when constructing this mask.

## Frozen outputs

The evaluation must emit, before any covariance restriction:

- canonical coordinate table and block order;
- per-provider Boolean validity flags V1–V8 (or N/A where logically inapplicable) for every candidate cell;
- final common Boolean mask = AND of provider-valid flags;
- explicit reason codes for every rejected cell;
- retained/rejected counts globally and by block/redshift/k;
- hashes/SHAs and exact artifact/run provenance of all provider inputs;
- an assertion that no downstream covariance, SVD, relation/null, or G8 quantity was read to construct the mask.

## Acceptance / failure semantics

`PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1` requires a non-empty common mask containing physically valid cells in all three frozen blocks (`mm`, `Wm`, `WW`) and at least two distinct redshifts and two distinct k values, with all output/provenance assertions satisfied.

If the intersection is empty or loses an entire required block, or has fewer than two redshifts or two k values, classify as scientific `FAIL_COMMON_PHYSICAL_SUPPORT_MASK_V0_1`; do not loosen these conditions retrospectively. Infrastructure failures remain separate and may be rerun without changing this preregistration.

A PASS authorizes only the next G7 stage: restrict the covariance to this already-frozen mask and preregister/execute whitening. It does not itself authorize nuisance SVD, quotient/relation/null statistics, or G8.

## Ordering lock

Current required order remains:

validated physical providers -> **Exp071A common support-validity mask** -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family.
