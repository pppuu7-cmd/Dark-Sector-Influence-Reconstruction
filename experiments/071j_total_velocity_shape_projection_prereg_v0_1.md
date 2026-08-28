# Exp071J — total-velocity per-redshift shape projection control v0.1

**Preregistered:** 2026-08-28, after the terminal Exp071I raw-velocity result and before any Exp071J projected angle is calculated.

## Motivation

Exp071I found a strong raw same-definition total-velocity separation between K2 bar1 and both tested GDM axes:

- `165.945494 deg` to GDM `cs2=1e-7`;
- `164.711329 deg` to GDM `cv2=1e-7`.

Because an oriented raw-vector angle can be dominated by a scale-independent response amplitude, Exp071J asks a narrower follow-up question: **does the separation survive after removing, independently at each redshift, the constant-in-k velocity-response mode?**

Exp071J does not alter or rescore Exp071I. It is a prospectively frozen robustness/falsification test motivated by Exp071I.

## Immutable input

Use only the terminal Exp071I artifact:

- run `33181895623`
- artifact `9690064470`
- artifact ZIP SHA256 `ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14`
- head `49996b5053b6b15428a2ff936efb4fd21fac266c`

No new solver run is allowed for the primary test.

The evaluator must first reconstruct the raw Exp071I `t_tot` responses from the immutable transfer files and reproduce the terminal raw angles to `1e-8 deg`. Otherwise Exp071J is INVALID_FOR_SCIENCE.

Frozen grids:

- `z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`
- `k = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`

Raw response definition inherited unchanged from Exp071I:

`r_ttot = ln(abs(t_tot_model/t_tot_ref))`.

K2 tangent denominators:

- bar1 `Delta omega_b = 0.0004`
- bar2 `0.0008`
- bar3 `0.0012`
- bar4 `0.0016`
- bar5 `0.0020`

GDM tangent denominator: `1e-7`.

## Frozen primary projection

For each 7x5 tangent matrix `R(z,k)`, define the per-redshift constant-k projection

`R_shape(z,k) = R(z,k) - mean_k R(z,k)`.

The mean uses equal weights over the five already-frozen k nodes. No fitted weights, covariance, survey window or model-dependent scaling is allowed.

This removes one scale-independent amplitude mode independently from each redshift slice while retaining all residual k-shape and its redshift evolution.

Numerical resolvability condition, not a science threshold:

`norm(R_shape) > 1e-12 * norm(R_raw)`

for K2 bar1 and both GDM primary vectors. If not, classify the projection as numerically unresolved and do not score the science separator.

## Frozen primary statistic

Primary K2 point remains **bar1**.

Compute oriented Euclidean angles in the projected 35-dimensional space:

- `theta(K2_bar1_shape, GDM_cs2_shape)`
- `theta(K2_bar1_shape, GDM_cv2_shape)`

The science separator is inherited unchanged from Exp071E/F/H/I:

`45 degrees`.

Primary PASS iff both projected angles are at least 45 degrees.

Frozen classifications:

- `K2_VELOCITY_SHAPE_SEPARATED_FROM_BOTH_GDM_AXES_EXP071J`
- `K2_VELOCITY_SHAPE_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071J`

Interpretation if PASS: the Exp071I K2/GDM total-velocity separation is not solely a per-redshift scale-independent amplitude effect on the frozen k support.

Interpretation if FAIL: raw Exp071I separation remains valid, but at least one GDM ambiguity returns after quotienting the per-redshift constant-k mode.

Neither outcome is tracer RSD or survey distinguishability.

## Frozen non-classifying diagnostics

These cannot change the primary classification:

1. retained shape norm fraction `||R_shape||/||R_raw||` for K2 bar1 and both GDM axes;
2. K2 bar2-bar5 shape-direction drift relative to bar1;
3. GDM `cs2` vs `cv2` projected shape angle;
4. global scalar-mean projection `R - mean_all(R)`;
5. per-k temporal projection `R(z,k) - mean_z R(z,k)`;
6. the same per-redshift shape projection applied to the common `t_b` sensitivity channel;
7. centered SVD of the five K2 projected `t_tot` directions.

No diagnostic may modify the 45-degree primary rule.

## Fail-closed conditions

Any artifact identity mismatch, missing transfer file/column, sign violation, denominator failure, raw-angle reproduction mismatch, non-finite projected value or primary projected norm below the numerical resolvability floor makes Exp071J INVALID_FOR_SCIENCE.

## Boundary

Regardless of outcome:

- G7 remains OPEN;
- G8 remains OPEN;
- G9 remains OPEN;
- this is a theory-space amplitude projection, **not** the observational nuisance quotient of Article 3;
- covariance/whitening remains unauthorized by this test;
- no tracer-RSD or `f sigma_8` claim is authorized.
