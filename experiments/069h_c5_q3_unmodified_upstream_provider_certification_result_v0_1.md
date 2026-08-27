# Exp069H — C5 q=3 unmodified-upstream physical-provider certification result v0.1

**Date:** 2026-08-27  
**Execution status:** `COMPLETE_C5_Q3_UNMODIFIED_UPSTREAM_PROVIDER_CERTIFICATION_V0_1`  
**Scientific classification:** `PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`

## Immutable provenance

- preregistration was merged before every Exp069H solver execution;
- implementation merge/head: `26162b0f2472dc1862eeb60b564a3563eaae12f9`;
- workflow run: `33024638764`;
- artifact: `9628053962`;
- artifact digest: `sha256:fa61b504d31edeba2afcbed0f4b14bda688df82a96d2cba55eac034682b5382f`;
- pinned upstream: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Exp069B remains permanently `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`. Exp069F remains the separate mechanism result `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`. Exp069H does not rewrite either experiment.

## Frozen C1 — exact-zero closure

At q=3 and literal public `EFTB0=0`:

- target-grid maximum relative discrepancy: `1.7011186858522977e-6`;
- solver-native same-node maximum relative discrepancy: `2.8421302380756537e-6`;
- frozen hard limit for each: `5e-6`.

Both pass.

## Frozen C2 — tiny-positive continuity

For `B0 = 1e-12, 1e-10, 1e-8`, direct comparisons to the q=3 zero branch satisfy the frozen target/raw continuity criterion `<=5e-6`. In the immutable artifact the reported maxima are numerically `0.0` for these points at the stored precision.

No point was inserted, removed or retuned after inspection.

## Frozen C3 — production signal

At `B0=1e-6` the target-grid production response is

`S_prod = 0.0132491...`,

well above the frozen nontrivial-signal requirement `1e-3`.

Thus the certified route does not obtain zero closure by collapsing the positive-B0 branch onto GR.

## Frozen C4 — signed cross-power semantics

`P_Wm` is obtained directly as the signed `Weyl × delta_nonu` cross-power. No absolute value or square-root reconstruction is used.

On the frozen 7×5 target support, `P_Wm` is negative at all 35 cells for the audited cases and remains unchanged under reverse accessor traversal.

## Frozen C5 — repeatability/state integrity

- forward `[mm,Wm,WW]` and reverse `[WW,Wm,mm]` accessor traversals are array-identical under the frozen test;
- an independent second `B0=0` solver run gives target and raw repeatability residuals `0.0`;
- frozen repeatability limit: `1e-12`;
- pinned upstream SHA is unchanged before/after;
- no upstream source modification is used.

## Frozen C6/C7

No floor subtraction, fitted normalization, smoothing, source patch, support-cell selection, q substitution or tolerance change is used. The literal public `EFTB0=0` branch is the provider under test; the analytic `A=0` GR theorem is context only and is not substituted for the numerical provider.

## Scientific consequence

C5 now has a prospectively certified unmodified-upstream q=3 provider for

- `P_mm`,
- signed `P_Wm`,
- `P_WW`.

Together with the already certified C3 native provider from Exp070C, this satisfies the two-provider prerequisite of the Exp069G ordering.

However a common physical support-validity mask is **not yet applied**. Before constructing it, a newly identified raw-k unit-label provenance issue in the historical Exp069F/H code must be audited separately: the target interpolator explicitly used `k_hunit=False`, while the raw `get_linear_matter_power_spectrum` call omitted `k_hunit` and pinned CAMB documents its default as `True` (`k/h`). This does not alter Exp069H's target closure or same-node raw ratios, but the raw coordinate label must not be propagated into a physical support mask without correction.

## Gate boundary

- C3 physical provider: `CERTIFIED`;
- C5 physical provider: `CERTIFIED`;
- common C3+C5 support-validity mask: `NOT YET APPLIED`;
- covariance/nuisance G7 advance: blocked until the common support unit/provenance audit and prospective mask;
- G7: `OPEN`;
- G8: `OPEN`;
- G9: `OPEN`.
