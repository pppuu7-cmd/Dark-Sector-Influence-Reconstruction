# Exp071G — K2 finite-bin growth direction control preregistration v0.1

**Frozen before any Exp071G K2-vs-GDM growth-angle result is computed.**

Date: 2026-08-28

## Scientific question

Exp071F showed that adding the raw matter-power tangent to Weyl+slip leaves a strong K2↔GDM-`cs2` local response ambiguity. Exp040 already validated a finite-bin temporal operator on the same frozen 7-z × 5-k matter-response grid:

`Delta fbar_P(k;i->j) = [r_P(k,z_late)-r_P(k,z_early)]/[2 Delta ln a]`,

with `r_P = ln(P_model/P_ref)`.

Exp071G asks whether the **temporal evolution of the matter response**, rather than the raw matter-response shape, separates the K2 known-sector control from the two local GDM axes.

This is a theory-space temporal-response test. It is explicitly **not tracer RSD**, not `f sigma8`, not an observational likelihood, and cannot close G7/G8/G9.

## Immutable parent bindings

- Exp071C run `33020201997`, artifact `9626235928`: K2 known-sector family and official-CLASS matter spectra; K2 must pass full F30 + all leave-one-z controls.
- GDM Weyl/slip run `32774198185`, artifact `9537340616`: immutable GDM `gdm0`, `cs2_1e-7`, `cv2_1e-7` matter spectra.
- Exp040 terminal result: `data/derived/comparison_readiness/experiment_040_finite_bin_growth_response_v0_1.json`; status must be `PASS_FINITE_BIN_GROWTH_RESPONSE_V0_1`.
- Exp071F terminal result: `data/derived/exp071f_known_sector_matter_weyl_slip_direction_summary_v0_1.json`; classification must be `K2_3CHANNEL_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071F`.

No Exp071G threshold, operator, node ordering, or primary K2 step may be altered after seeing Exp071G output.

## Frozen grid

`z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`

`k = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`

Matter response at each node:

`r_P(z,k) = ln[P_model(z,k)/P_ref(z,k)]`.

Positive matter power is interpolated linearly in `ln(k)` for `ln(P)`, exactly as Exp071C/F.

## Frozen temporal operator

For ascending z, with `a=1/(1+z)`, each adjacent interval is early `z[i+1]` to late `z[i]`:

`g_P(i,k) = [r_P(z[i],k)-r_P(z[i+1],k)] / [2 ln(a[i]/a[i+1])]`.

This is copied from `ci/finite_bin_growth_response_v0_1.py` without modification.

The flattened growth vector has `6 × 5 = 30` entries, ordered by adjacent redshift interval then frozen k order.

## Frozen tangents

Primary K2 point: **bar1 only**.

`delta_f_b = (omega_b_bar1 - omega_b_ref)/omega_m`, with `omega_m=0.1424`.

`t_g,K2 = g_P(bar1)/delta_f_b`.

GDM local tangents:

- `t_g,cs = g_P(cs2_1e-7)/1e-7`
- `t_g,cv = g_P(cv2_1e-7)/1e-7`.

Because angle is homogeneous, no amplitude equalization is required for this single-channel test.

## Primary frozen statistics

Compute oriented Euclidean angles:

- `theta_growth_K2_cs = angle(t_g,K2, t_g,cs)`
- `theta_growth_K2_cv = angle(t_g,K2, t_g,cv)`.

For continuity with the prospectively frozen directional-separation controls Exp071E/F, the separator threshold is inherited unchanged:

**45 degrees**.

Primary classification:

- if both angles are `>=45 deg`:
  `K2_FINITE_BIN_GROWTH_SEPARATED_FROM_BOTH_GDM_AXES_EXP071G`
- otherwise:
  `K2_FINITE_BIN_GROWTH_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071G`.

No post-result retuning is allowed.

## Mandatory integrity cross-checks

Before the K2 classification is accepted:

1. Exp040 status must be PASS.
2. Recomputed GDM `cs2` vs `cv2` finite-bin growth acute angle must reproduce the Exp040 stored value `1.3340128035605052 deg` within `1e-8 deg`.
3. The finite-bin endpoint reconstruction identity must hold to `1e-12` for K2 and both GDM axes:
   `2 sum_i g_i Delta ln a = r_P(z_low)-r_P(z_high)` at every k.
4. Constant-mode annihilation and linearity controls copied from Exp040 must satisfy its frozen thresholds (`1e-14` and `1e-12`).
5. All 7 matter-power redshifts must exist for reference/K2/GDM parents, cover all frozen k nodes, and remain positive on interpolation support.
6. All three primary growth tangent norms must be finite and nonzero.

## Frozen robustness diagnostics — non-classifying

For K2 bar2..bar5 report:

- angle of growth tangent to K2 bar1;
- angle to GDM cs2;
- angle to GDM cv2;
- K2 growth-family centered SVD;
- maximum finite-step drift.

Also report raw-matter primary angles and require them to reproduce Exp071F matter-only values within `1e-8 deg`:

- K2 bar1 vs GDM cs2: `19.223081503733017 deg`
- K2 bar1 vs GDM cv2: `19.037102938963482 deg`.

These robustness quantities cannot change the primary bar1 classification.

## Interpretation boundary

A PASS would show that the **temporal evolution** of the common matter response separates this specific K2 known-sector mimic from both tested local GDM axes even though the raw matter direction does not. It would not imply observational RSD distinguishability or generic dark-sector uniqueness.

A FAIL would show that the K2↔sound-speed-like ambiguity survives not only raw matter/Weyl/slip geometry but also this finite-bin temporal derivative. That would move the next required discriminator toward a genuinely velocity/tracer or other independent response block, subject to a verified common variable convention.

Irrespective of outcome:

- `G7 = OPEN`
- `G8 = OPEN`
- `G9 = OPEN`
