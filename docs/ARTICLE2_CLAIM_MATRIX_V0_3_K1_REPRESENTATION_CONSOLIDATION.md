# DSIR Article 2 — claim matrix v0.3: representation and nuisance consolidation

**Date:** 2026-08-28

**Status:** authoritative Article-2 consolidation after Exp071M/N. This document supersedes any v0.2 wording that could be read as implying generic known-sector specificity of a transfer-only or velocity-shape response.

The v0.2 ray/line/subspace geometry remains valid. Exp071M/N add a second, physically independent known-sector control family and establish a further requirement: a nuisance can only be compared in a response representation in which that nuisance actually acts.

## New or revised claims

| ID | Status | Paper-ready claim | Evidence | Forbidden stronger claim |
|---|---|---|---|---|
| A2-C14R | ✅ revised | The source-audited CLASS `t_tot` channel strongly separates the **positive-oriented K2 ray** from the tested positive GDM `cs2/cv2` rays, but this is not a statement about the whole two-sided K2 nuisance line. | Exp071I/J/K. | “Velocity generically removes K2 as a nuisance.” |
| A2-C17 | ✅ falsification | A fresh negative K2 displacement lies only `13.5503° / 15.0709°` from the positive GDM velocity-shape rays, so the physically two-sided K2 nuisance line overlaps both tested GDM rays. | Exp071L. | “The positive-ray angle is a nuisance-line separation.” |
| A2-C18 | ✅ method | For an interior scalar nuisance, equivalence is a **line** rather than an oriented ray; for several nuisances it is a metric subspace with projector `P_N = N (N^T M N)^+ N^T M`. | `DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md`, Exp071L numerical validation. | “A selected tangent sign represents the whole nuisance freedom.” |
| A2-C19 | ✅ representation boundary | Pure primordial tilt `n_s` is a **null direction of the transfer-only `t_tot` representation** on the frozen setup: fresh `n_s=0.970` and `n_s=0.960` runs have exactly zero `ln|t_tot/t_tot_ref|` response, so Exp071M correctly terminates `INVALID_FOR_SCIENCE` rather than assigning a meaningless angle. | Exp071M run `33185652795`, artifact `9691596312`, terminal summary `data/derived/exp071m_two_sided_k1_transfer_null_summary_v0_1.json`. | “Primordial tilt has no physical effect.” |
| A2-C20 | ✅ falsification | After adding the missing primordial-power contribution in a preregistered common linear velocity-power representation `Delta ln P_R + 2 Delta ln|t_tot|`, the physically independent two-sided primordial-tilt nuisance line still overlaps both tested positive GDM rays: line angles are `36.0622°` to `cs2` and `37.8458°` to `cv2`, below the frozen `45°` separator. | Exp071N prereg `cfaf9d14fa734e155cab5dca028bc1a14d0afd46`, run `33186048775`, job `98899204160`, artifact `9691720131`, SHA256 `19ce8623c64faf2e9ebd1d38ce2db5eb394d0a941457b18a8b59508d558d00eb`, terminal summary `data/derived/exp071n_two_sided_k1_velocity_power_shape_summary_v0_1.json`. | “Velocity-power shape is a unique dark-sector fingerprint.” |
| A2-C21 | ✅ integrity | Exp071N fresh reference reproduces immutable official-CLASS parent `P(k,z)` and `t_tot` with maximum relative difference `0.0`; K1 projected shape retains `0.6255` of raw norm, so the overlap is neither a reference drift nor an angle of a numerically vanishing vector. | Exp071N terminal artifact. | “The result is observationally distinguishable.” |

## Exp071M representation-null result

Exp071M was preregistered as a transfer-only `t_tot` test using the inherited K1 step `|Delta n_s|=0.005` from Exp071C:

- reference `n_s=0.965`;
- plus `n_s=0.970`;
- minus `n_s=0.960`.

All immutable bindings, source-contract checks, solver build, and fresh CLASS runs completed. The evaluator then stopped at the frozen nonzero-vector integrity gate because

`ln|t_tot(K1+)/t_tot(ref)| = 0`

on the full frozen support, and likewise for K1(-).

This is not an infrastructure failure and not a K1/GDM scientific PASS/FAIL. It identifies a **representation kernel**: pure primordial tilt acts through the primordial spectrum while the transfer function remains unchanged in this setup.

Hence a general DSIR comparison must satisfy a resolvability condition before angular geometry is meaningful:

`||A r_nuisance|| > numerical_resolution_floor`,

where `A` denotes the chosen response/observation representation. If a nuisance lies in `ker(A)`, its angle in that representation is undefined for specificity purposes.

## Exp071N common velocity-power representation

Exp071N was frozen only after Exp071M was retained as invalid-for-science. It did not relax the transfer-null integrity gate. Instead it defined a new physical response shared by K1 and GDM:

`r_vv(z,k) = Delta ln P_R(k) + 2 Delta ln |t_tot(z,k)|`.

For pure tilt,

`Delta ln P_R(k) = Delta n_s * ln(k_phys/k_pivot)`.

The same per-redshift constant-in-k quotient used by Exp071J was then applied.

Primary oriented angles were:

- K1(+) vs GDM cs2: `36.0622372504 deg`;
- K1(+) vs GDM cv2: `37.8458122995 deg`;
- K1(-) vs GDM cs2: `143.9377627496 deg`;
- K1(-) vs GDM cv2: `142.1541877005 deg`.

K1 plus/minus are antiparallel to numerical precision:

- mutual angle `179.9999991462 deg`;
- antisymmetry error `0.0`.

Therefore the physically correct K1 line angles are

- `36.0622372504 deg` to GDM cs2;
- `37.8458122995 deg` to GDM cv2.

Both lie below the frozen `45 deg` separator, giving

`K1_TWO_SIDED_VELOCITY_POWER_SHAPE_OVERLAPS_GDM_EXP071N`.

### Diagnostic correction

The original Exp071N evaluator printed a non-classifying `line_angle_prediction_validation` that compared the positive-branch **line angle** to the raw oriented negative-branch angle. That comparison is geometrically mismatched and produced large diagnostic numbers. It never entered the frozen primary four-angle classification.

The corrected comparison applies `min(theta,180-theta)` to both branches and agrees at machine precision:

- cs2 line-angle branch discrepancy: about `2e-14 deg`;
- cv2 line-angle branch discrepancy: about `1e-14 deg`.

The terminal repo summary records this correction explicitly without changing the immutable run classification.

## Consolidated Article-2 scientific message

The strongest defensible Article-2 result is now **not a fingerprint claim**. It is a hierarchy of equivalence conditions:

1. static matter morphology can be mimicked by a known-sector baryon/CDM redistribution;
2. additional metric/slip channels add information but do not generically remove known-sector ambiguity;
3. temporal and transfer-velocity responses can sharply separate a chosen **oriented ray** while leaving the corresponding two-sided nuisance line overlapping after sign freedom is restored;
4. a physically independent primordial-tilt nuisance exposes a separate requirement: the chosen representation must first resolve that nuisance at all;
5. once primordial power is included so that K1 is resolvable, its two-sided line also overlaps the tested GDM rays in the examined velocity-power shape space;
6. therefore response equivalence is conditioned simultaneously on **representation, channel set, orientation/sign freedom, metric, and nuisance subspace**.

Compactly:

`response representation -> resolvability -> ray/line/subspace geometry -> channel-conditioned equivalence -> physical support -> observational quotient`.

This is a stronger methodological result than a model-fingerprint narrative because the framework records both where apparently new discriminatory information appears and where that discrimination disappears under a physically correct nuisance description.

## Article-3 handoff

The Article-3 nuisance quotient should use a basis `N` containing every **resolved signed nuisance direction** after the observational operator and covariance metric are defined. A parameter that is null in an intermediate theory representation must not be declared harmless; it must be evaluated in the final observation representation where its effect may re-enter through primordial, transfer, window, calibration, or tracer factors.

Nothing in Exp071M/N authorizes covariance whitening or closes G7.

## Article-2 remaining work after v0.3

The independent known-sector-control question is now closed for the declared Article-2 scope with both K2 and K1 examples. Remaining repository work is primarily article assembly and final audit:

- propagate v0.3 wording into the eventual manuscript abstract/discussion;
- produce a compact ray/line/representation-kernel figure and comparison table;
- perform one final claim/provenance/notation audit on the assembled Article-2 draft.

No further K1 or K2 variants are required merely to support the current Article-2 scientific scope.
