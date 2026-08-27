# Exp071A — common physical provider-support execution binding v0.1

**Date frozen:** 2026-08-27  
**Status:** PROSPECTIVE EXECUTION BINDING — no Exp071A support-mask output has been evaluated before this file.

This file does not replace or weaken the already-frozen V1–V8 criteria in
`recovery/exp071a_g7_common_physical_support_mask_preregistration_2026-08-27.md`.
It resolves only implementation choices that were not numerically explicit there.

## Inputs

Only immutable certified provider artifacts are admissible provenance:

### C3 / GDM

- Exp070C classification: `PASS_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1`;
- run `33017214292`;
- artifact `9625032179`;
- digest `sha256:34cf89f2207c72b4e3d669f7e4e6419753b6b046ed7de9e3a9fa7fb144b4c081`;
- solver `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

### C5 / designer-f(R)

- Exp069H classification: `PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`;
- run `33024638764`;
- artifact `9628053962`;
- digest `sha256:fa61b504d31edeba2afcbed0f4b14bda688df82a96d2cba55eac034682b5382f`;
- solver `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`;
- raw-k unit provenance corrected by Exp069I PASS, run `33026608144`, artifact `9628710949`.

## Canonical coordinate rule

The C3 provider is certified only on its native physical k nodes and forbids amplitude interpolation. Therefore the canonical k coordinate at each retained redshift is frozen as **the complete C3 native physical `k_Mpc^-1` array**, with no thinning, nearest-neighbour replacement or response-dependent selection.

The canonical redshift set is the exact numerical intersection of the certified provider redshift coordinates. No redshift interpolation is permitted.

A canonical C3 native k node is retained as a candidate only if it lies inside the C5 explicit physical raw-k support after applying the Exp069I unit provenance result. No extrapolation is allowed.

## C5 mapping rule

C5 is the only provider allowed to map onto the C3-native canonical k nodes.

Use the same public CAMB interpolation operator class used in Exp069H certification:

`get_matter_power_interpolator(nonlinear=False, var1=..., var2=..., hubble_units=False, k_hunit=False, log_interp=True)`

with the certified q=3 unmodified-upstream settings.

Evaluate only at canonical C3-native k nodes lying inside the explicit C5 physical raw support and only at exact common redshifts.

No new interpolation rule, smoothing, fitted normalization or floor correction is permitted.

## Cases entering validity

### C3

All three Exp070C certified cases enter the provider-validity AND:

- `cs2=0`;
- `cs2=1e-6`;
- `cs2=1e-5`.

A candidate cell is C3-valid only if V1–V8 are satisfied for every applicable certified C3 case.

### C5

The production provider point is frozen as

`B0=1e-6`

for candidate-cell V2–V5 evaluation, because this is the nontrivial production branch certified by Exp069H. V1 and V6 additionally require the complete Exp069H certification record, including its exact-zero and continuity controls, to remain PASS.

No B0 point is selected by response magnitude after evaluation.

## Blocks

Frozen order:

`[P_mm, signed P_Wm, P_WW]`.

For every candidate `(z,k)` and every applicable case require:

- finite values;
- `P_mm>0`;
- `P_WW>0`;
- signed `P_Wm` preserved;
- positive-semidefinite 2x2 spectral condition from the original preregistration:

`P_Wm^2 <= P_mm*P_WW*(1+1e-6)`.

No denominator floor is allowed.

## Candidate and mask cardinality

The implementation must emit every candidate cell, including rejected cells, with reason codes. The final common mask is the literal logical AND over applicable V1–V8/provider checks.

No downstream covariance, whitening, nuisance SVD, relation/null statistic, G8 quantity, article figure or desired retained count may be consulted.

## Acceptance

Use the original frozen Exp071A acceptance semantics unchanged:

`PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1`

iff the resulting provider-space common mask is non-empty, contains all three blocks, and has at least two distinct redshifts and at least two distinct physical k values.

Otherwise classify

`FAIL_COMMON_PHYSICAL_SUPPORT_MASK_V0_1`.

Infrastructure/data-download failures are `INCOMPLETE_EXP071A` and are not scientific FAILs.

## Downstream boundary

Per `docs/EXP071A_PHYSICAL_SUPPORT_VS_OBSERVATIONAL_LEAKAGE_BOUNDARY_2026-08-27.md`, even a PASS establishes only the common **provider-space** physical domain. It does not yet authorize covariance restriction.

The next step after PASS is a separately prospectively frozen ACT×unWISE released-kernel/bandwindow support-leakage audit that selects angular observable coordinates. G7/G8/G9 remain OPEN.
