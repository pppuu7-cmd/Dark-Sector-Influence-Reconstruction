# Exp070B — C3/GDM D_m normalization mechanism audit v0.1

Date frozen: 2026-08-27 (Europe/Moscow)

## Purpose

Exp070A is permanently classified `FAIL_C3_GDM_READONLY_DM_PHYSICAL_POWER_BRIDGE_V0_1`. Its read-only accessor, native mPk invariance, signed Weyl construction, same-mode coherence, repeatability and no-state-mutation controls passed, while the frozen D_m→mPk reconstruction missed native mPk by about 4.75% and the aggregate post-build patch-scope check also failed because it counted a generated extension module. Exp070B is a mechanism audit only. It must not reclassify Exp070A or relax any Exp070A acceptance threshold.

The sole scientific question is why the source-normalized reconstruction

`P_mm^recon(k,z) = (2*pi^2/k^3) * P_R(k) * D_m(k,z)^2`

differs from the pinned solver's native linear `mPk` by O(4.75%).

## Frozen provenance

- DSIR base: merge commit `375cbb6eeb08a1fdafe47b77851a49794613b937`.
- Pinned external solver: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.
- Exp070A preregistration: `c07e1dc73df2ee0bb9faad46ec8a8877d683a5d9`.
- Exp070A scientific FAIL is immutable.
- Same cosmology, GDM parameterization, p8 precision preset and adiabatic scalar initial conditions as Exp070A.

## Frozen support

Use the same redshift set as Exp070A:

`z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`.

Use each solver-native source k node that lies within the intersection of:

1. the public D_m accessor grid,
2. the standard transfer grid,
3. the domain accepted by native `pk_lin(k,z)`, and
4. `0.001 <= k/(h Mpc^-1) <= 0.1`.

No new support point may be added after seeing Exp070B output.

GDM cases remain exactly:

- `cs2 = 0`,
- `cs2 = 1e-6`,
- `cs2 = 1e-5`.

## Audit decomposition

For every frozen model/redshift/native-k cell, record:

1. public accessor `D_m`, with no interpolation;
2. standard transfer quantities exposed by the pinned wrapper, including `d_tot`, `phi`, `psi` and any native matter-transfer column corresponding to the same source when present;
3. native `pk_lin(k,z)` at the identical physical k;
4. the analytic primordial factor used by the run;
5. `R_raw = P_native / [(2*pi^2/k^3) P_R D_m^2]`;
6. signed amplitude ratio `A_raw = sign(D_m)*sqrt(P_native / [(2*pi^2/k^3)P_R]) / D_m` whenever finite;
7. the same quantities for `d_tot` as a deliberately wrong comparator.

No interpolation is permitted in the primary native-node audit.

## Frozen mechanism tests

M1 — native-node mismatch persists:

Compute the maximum relative error between native mPk and the direct native-node D_m reconstruction. This is diagnostic only; there is no PASS threshold for reclassifying Exp070A.

M2 — interpolation attribution:

Independently reproduce the Exp070A target-grid signed-linear-in-log-k interpolation and compare its mismatch to the native-node mismatch. Classify the 4.75% effect as interpolation-dominated only if the native-node maximum error is at least 10 times smaller than the Exp070A target-grid maximum. This 10x classification factor is frozen before output.

M3 — multiplicative normalization signature:

For each model, compute the coefficient of variation of `R_raw` over all retained native cells and the spread of model-median `R_raw`. Classify a common multiplicative-normalization signature only if both are <= 5e-3. This 5e-3 diagnostic bound is frozen before output.

M4 — source identity check:

If the pinned standard transfer API exposes a matter source intended to match `index_tp_delta_m`, compare it directly at common native nodes. If no such public column exists, record `NOT_PUBLICLY_EXPOSED` rather than inferring equality.

M5 — wrong-source separation:

Record the native-node d_tot reconstruction error. `d_tot` must not be promoted to the physical bridge even if it happens to reduce a subset of residuals.

M6 — no mutation / repeatability:

Repeat D_m reads bitwise and verify native mPk before/after the read-only accessor is unchanged to the inherited Exp070A `1e-12` no-state-mutation tolerance. This inherited control is not retuned.

## Allowed implementation changes

Exp070B may add DSIR-side audit code/workflow/result/checkpoint files. It may reuse the already validated read-only accessor patch, but it may not alter perturbation, transfer, spectra, nonlinear, primordial or background physics in the external solver.

The external-tree source patch remains limited to `python/cclassy.pxd` and `python/classy.pyx`. Generated build products are provenance, not a scientific correction; Exp070A's V1 FAIL remains preserved exactly as recorded.

## Classification

Exp070B produces one of these mechanism labels, not a G7 PASS:

- `INTERPOLATION_DOMINATED`
- `COMMON_MULTIPLICATIVE_NORMALIZATION_SIGNATURE`
- `SOURCE_IDENTITY_MISMATCH`
- `MIXED_OR_UNRESOLVED_MECHANISM`

Multiple evidence flags may be recorded, but exactly one primary label must be chosen by the frozen precedence:

1. `INTERPOLATION_DOMINATED` if M2 condition passes;
2. else `COMMON_MULTIPLICATIVE_NORMALIZATION_SIGNATURE` if M3 condition passes;
3. else `SOURCE_IDENTITY_MISMATCH` if M4 establishes a direct mismatch above `5e-4`;
4. else `MIXED_OR_UNRESOLVED_MECHANISM`.

The `5e-4` M4 comparison bound is inherited from Exp070A's frozen V3 tolerance and is not a new bridge acceptance threshold.

## G7 boundary

Exp070B cannot close G7 and cannot authorize the support-validity mask. After Exp070B, any corrective C3 provider must be separately preregistered before execution. C5 also remains unvalidated after Exp069A/069B scientific FAILs. Therefore the mandatory order remains:

validated physical forward/power-input bridges -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family.

G7/G8/G9 remain OPEN.
