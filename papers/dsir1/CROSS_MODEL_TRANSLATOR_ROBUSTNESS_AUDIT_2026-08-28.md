# DSIR-I cross-model translator robustness audit

**Date:** 2026-08-28  
**Status:** RETROSPECTIVE ROBUSTNESS AUDIT ON IMMUTABLE FROZEN SUMMARIES  
**Paper role:** strengthen the Paper-I statement that cross-model translation is channel/subspace conditional and generically non-bijective; this is not G7/G8/G9 evidence.

## 1. Frozen inputs

No new Boltzmann solve is used. The audit reads only repository-frozen summary products:

- `data/derived/comparison_readiness/experiment_047a_finite_amplitude_interaction_curvature_v0_1_summary.json`;
- `data/derived/comparison_readiness/experiment_048b_finite_amplitude_localization_flow_v0_1_summary.json`;
- the prior descriptive architecture record `docs/CROSS_MODEL_TRANSLATOR_LIGHTWEIGHT_AUDIT_2026-08-27.md`.

The two finite rays are

- C3 GDM viscosity: `cv2={1e-8,1e-7,1e-6,1e-5,1e-4}`;
- C5 designer-`f(R)`: `B0={1e-6,1e-5,1e-4,1e-3}`.

The response coordinate is

`q = [ln(k_geo), z_centroid, ln(chi_I)]`.

Because this is retrospective, the metric family below is a robustness family, not a preregistered discovery test.

## 2. Metric-family robustness

To test whether the earlier `2/5` cycle result was an accident of pooled z-scoring plus Euclidean distance, recompute finite-grid nearest-neighbour translation under the Cartesian product

- coordinate scalings: pooled z-score, pooled min-max, pooled median/MAD;
- norms: `L1`, `L2`, `Linf`.

This gives **9 full-coordinate translator variants**.

### Hard summary-level result

For **all 9/9 variants**, the `C3 -> C5 -> C3` cycle closes on exactly **2/5** C3 grid points.

Thus the observed 40% cycle closure is invariant over this deliberately broad family of common diagonal rescalings and standard `Lp` norms.

The nearest C5 identities are also strongly but not perfectly stable:

- in **8/9** full-coordinate variants, the first four C3 points (`cv2=1e-8..1e-5`) collapse to `B0=1e-6`, while `cv2=1e-4` maps to `B0=1e-3`;
- only the min-max + `Linf` variant changes the shared low/mid representative, sending the first four C3 points to `B0=1e-4`;
- `cv2=1e-4 -> B0=1e-3` is stable in **9/9** variants.

Therefore the robust statement is **not** a unique parameter correspondence. The robust statement is the topology of the finite sampled translation: a many-to-one low/mid-amplitude collapse plus a distinct large-amplitude endpoint, with incomplete cycle recovery.

## 3. Coordinate-ablation audit

Repeat the same 3 scalings x 3 norms after leaving out one coordinate.

### `[ln(k_geo), z_centroid]`

- cycle closure: **2/5 in 9/9 variants**;
- C3-to-C5 mapping: `[1e-6,1e-6,1e-6,1e-6,1e-3]` in **9/9 variants**.

This two-coordinate localization pair preserves the robust finite-grid collapse seen in the full three-coordinate audit.

### `[z_centroid, ln(chi_I)]`

- cycle closure: **1/5 in 9/9 variants**;
- every C3 point maps to `B0=1e-3` in **9/9 variants**.

Removing scale localization therefore destroys most of the cross-family resolution for this C3/C5 pair.

### `[ln(k_geo), ln(chi_I)]`

- cycle closure: **2/5 in 7/9 variants** and **3/5 in 2/9 variants**;
- nearest-partner identities vary with metric/scaling.

This projection retains more resolving power than `(time, amplitude)` but is less stable than `(scale, time)`.

## 4. One-coordinate control

Using a single coordinate reproduces the qualitative result already recorded in the lightweight audit:

- `ln(k_geo)` resolves multiple C5 representatives and gives **3/5** cycle closures on the finite sampled grid;
- `z_centroid` alone collapses all five C3 points onto `B0=1e-3` and gives **1/5** closure;
- `ln(chi_I)` alone also collapses all five C3 points onto `B0=1e-3` and gives **1/5** closure.

This is a direct numerical demonstration of response-subspace dependence: changing the retained observable coordinate changes the inferred cross-model equivalent.

## 5. Relation to finite-amplitude curvature

The robustness result has a physical reason not to be interpreted as a mere nearest-neighbour pathology. The frozen finite-amplitude record shows substantial trajectory turning for precisely these two families:

- GDM viscosity: maximum response-space turning `~7.18 deg`, interaction turning `~12.19 deg`;
- designer-`f(R)`: maximum response-space turning `~12.14 deg`, interaction turning `~13.00 deg`.

The localization-flow record also shows that both families move to lower `k_geo` at large amplitude while their temporal motion differs: GDM viscosity moves nearly monotonically to higher `z_centroid`, whereas designer-`f(R)` is non-monotonic.

Therefore a global scalar parameter conversion is not expected from the frozen geometry; local, multicoordinate, channel-conditioned translation is the scientifically consistent object.

## 6. What is now robustly supported for Paper I

The existing translator proof-of-concept is strengthened to the following summary-level statements:

1. **Parameter equivalence is response-subspace conditional.** The nearest equivalent changes when scale, time or interaction-amplitude information is retained/removed.
2. **Non-bijectivity is metric-robust on the sampled C3/C5 rays.** The full-coordinate cycle closure is exactly `2/5` for all 9 tested scaling/norm variants.
3. **Scale localization carries essential cross-family discrimination for this pair.** Removing `ln(k_geo)` collapses the map to one C5 representative in all 9 variants.
4. **The large-amplitude endpoint is unusually stable.** `cv2=1e-4 -> B0=1e-3` in all 9 full-coordinate variants.
5. **A translator should be local rather than a global microscopic identity.** Frozen Jacobian-sign differences and finite-amplitude trajectory curvature independently support this boundary.

## 7. Non-claims

This audit does **not** establish:

- a unique one-to-one `cv2 <-> B0` mapping;
- a universal scalar translator;
- an observational likelihood/Fisher improvement;
- a covariance/nuisance-quotiented equivalence class;
- a prospective translator test;
- G7, G8 or G9.

The inputs are rounded repository summaries, so the audit intentionally reports discrete nearest-neighbour identities and closure counts rather than overstating distance precision.

## 8. Paper-I verdict

`PASS_RETROSPECTIVE_TRANSLATOR_METRIC_AND_COORDINATE_ROBUSTNESS_V0_1`

For the DSIR-I thesis, the cross-model translator block is now scientifically adequate as a **channel-conditional, local, non-bijective response-space construction**. A prospective observational translator is a later-paper strengthening, not a scientific blocker for DSIR-I.
