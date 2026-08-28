# Exp071L — two-sided K2 velocity-shape nuisance control v0.1

**Preregistered:** 2026-08-28, after terminal Exp071K and before any negative-K2 velocity response is calculated.

## Motivation

Exp071I/J/K establish strong separation for the **oriented positive K2 displacement** (`Delta omega_b > 0`, `Delta omega_cdm < 0`) relative to the two tested positive GDM directions. However the K2 known-sector control is an ordinary baryon/CDM redistribution around an interior reference point, so a physically admissible nuisance can also move in the opposite direction.

An oriented tangent angle is therefore not by itself sufficient to claim separation from a two-sided known-sector nuisance line. Exp071L prospectively tests the opposite physical K2 displacement with a genuinely fresh solver evaluation.

This is a theory-space falsification control, not tracer RSD, covariance whitening, nuisance marginalization in data space, or survey distinguishability.

## Frozen reference and negative K2 point

Reference:

- `omega_b = 0.0224`
- `omega_cdm = 0.1200`
- fixed total `omega_m(h^2) = 0.1424`

Fresh negative K2 point:

- `omega_b = 0.0220`
- `omega_cdm = 0.1204`
- `Delta omega_b = -0.0004`
- `Delta omega_cdm = +0.0004`

All other cosmological, primordial, gauge, redshift, k-support and transfer-output settings are inherited unchanged from Exp071I.

Official CLASS is pinned to:

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.

Output is the Exp071I I/O contract:

`mPk,mTk,vTk`.

Frozen redshifts:

`[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`.

Frozen k nodes:

`[0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`.

## Immutable parent

Use the Exp071I artifact only for the positive K2 and positive GDM parents:

- run `33181895623`
- artifact `9690064470`
- SHA256 `ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14`

The workflow must bind this exact artifact before scoring.

## Fresh-reference integrity gate

A fresh CLASS reference run with the exact Exp071I reference configuration must reproduce the immutable Exp071I K2 reference matter-power files on their stored grids with

`max_abs_relative_P_difference <= 1e-10`.

The fresh reference `t_tot` values on the frozen `(z,k)` nodes must also reproduce the immutable Exp071I K2 reference values to

`max_abs_relative_ttot_difference <= 1e-10`.

Failure of either condition makes Exp071L `INVALID_FOR_SCIENCE`.

## Frozen displacement response

For any model/reference pair define the actual allowed displacement response

`r_ttot = ln(abs(t_tot_model/t_tot_ref))`.

For K2 negative displacement, divide only by the **positive magnitude** `abs(Delta omega_b)=0.0004`; do not multiply by the sign of the parameter step. This preserves the physical orientation of the negative displacement.

For the positive K2 parent use the immutable Exp071I `bar1` response divided by `0.0004`.

For GDM use the immutable positive `cs2=1e-7` and `cv2=1e-7` displacements divided by `1e-7`.

At every node require finite values, nonzero reference support and sign preservation exactly as in Exp071I.

## Frozen velocity-shape quotient

For every displacement tangent matrix `R(z,k)` apply the Exp071J quotient

`R_shape(z,k) = R(z,k) - mean_k R(z,k)`

independently at every redshift with equal k weights.

Every projected vector must satisfy

`norm(R_shape) > 1e-12 * norm(R)`.

## Frozen primary statistic

Compute four oriented Euclidean angles:

1. positive K2 vs positive GDM cs2;
2. positive K2 vs positive GDM cv2;
3. **negative K2 displacement** vs positive GDM cs2;
4. **negative K2 displacement** vs positive GDM cv2.

The first two must reproduce Exp071J to `1e-8 deg` before the fresh negative direction is interpreted.

Inherited separator: `45 degrees`.

Two-sided K2 nuisance is classified as separated only if **all four** angles are `>=45 deg`.

Frozen classifications:

- `K2_TWO_SIDED_VELOCITY_SHAPE_SEPARATED_FROM_BOTH_GDM_AXES_EXP071L`
- `K2_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071L`

No absolute-angle, projective-angle or average-angle criterion may replace this rule after execution.

## Quantitative summaries

Report without changing the primary classification:

- minimum of the four primary angles;
- negative-K2 vs positive-K2 mutual angle;
- nonlinear antisymmetry error between the positive and negative K2 displacement shapes, defined by `||R_plus + R_minus|| / ((||R_plus||+||R_minus||)/2)` after equal `|Delta omega_b|` normalization;
- per-node sign/resolvability diagnostics;
- the positive-parent Exp071J reproduction values.

## Interpretation

If two-sided separation PASS:

> Both physically allowed local K2 displacement orientations remain separated from both tested positive GDM directions under the frozen velocity-shape response.

If overlap:

> The oriented positive-K2 Exp071I/J/K results remain numerically valid, but they do not establish specificity against a two-sided known-sector K2 nuisance: an allowed opposite K2 displacement approaches at least one tested positive GDM response direction within the frozen 45-degree criterion.

This distinction must be propagated into Article 2 rather than hidden by tangent-orientation conventions.

## Gate boundary

Regardless of outcome:

- G7 OPEN
- G8 OPEN
- G9 OPEN
- no survey likelihood claim
- no covariance/whitening authorization
- no observational nuisance quotient authorization
