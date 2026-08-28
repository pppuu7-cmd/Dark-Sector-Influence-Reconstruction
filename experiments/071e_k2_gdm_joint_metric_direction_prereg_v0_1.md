# Exp071E — K2 vs GDM joint metric-direction control v0.1

**Frozen before any cross-family direction angle is evaluated:** 2026-08-28.

## Motivation

Two prospectively controlled results now coexist:

1. Exp071C: the known-sector K2 baryon/CDM redistribution family mimics the matter-only F30 morphology.
2. Exp071D: the scalar ratio `q_slip/W = ||Delta_slip||/||r_W||` for K2 overlaps the frozen GDM `cs2` scale under the preregistered ordering test, while remaining far below the GDM `cv2` ratio.

A scalar channel-norm ratio does not test whether the **full response direction** is the same. Exp071E therefore asks whether K2 is directionally close to either frozen GDM local axis in the identical joint `r_W + Delta_slip` representation.

This is a mechanism-specificity control, not an observational gate.

## Immutable input bindings

### Exp071D

Run `33176559280`, artifact `9687861012` must satisfy:

- `status = COMPLETE_K2_KNOWN_SECTOR_METRIC_SLIP_CONTROL_V0_1`;
- `classification = K2_SLIP_TO_WEYL_RATIO_OVERLAPS_GDM_AXES_EXP071D`;
- five K2 points in the frozen fixed-`omega_m` family;
- identical z and k grids to the parent GDM metric control.

### GDM metric/slip

Run `32774198185`, artifact `9537340616` must satisfy:

- hard gate `PASS_GDM_SLIP_BREAKS_LOW_K_DEGENERACY`;
- models `cs2_1e-7` and `cv2_1e-7` available with stored `r_W` and `delta_slip` arrays.

## Frozen common grid

Redshifts:

`[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`

Wave numbers:

`[0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`

The test is invalid if either input differs in ordering or support.

## Frozen tangent definitions

For GDM:

- `t_cs_W = r_W(cs2_1e-7)/1e-7`
- `t_cs_S = Delta_slip(cs2_1e-7)/1e-7`
- `t_cv_W = r_W(cv2_1e-7)/1e-7`
- `t_cv_S = Delta_slip(cv2_1e-7)/1e-7`

For K2 point `i`:

- `delta_f_b_i = (omega_b_i - 0.0224)/0.1424`
- `t_K2i_W = r_W_i/delta_f_b_i`
- `t_K2i_S = Delta_slip_i/delta_f_b_i`

No finite-difference subtraction between neighboring K2 points is introduced; the same one-sided reference tangent definition used by Exp071D is retained.

## Frozen channel equalization

Use **GDM-only** scales, fixed independently of K2:

- `s_W = max(||t_cs_W||_2, ||t_cv_W||_2)`
- `s_S = max(||t_cs_S||_2, ||t_cv_S||_2)`

Construct joint vectors

- `u_cs = concat(t_cs_W/s_W, t_cs_S/s_S)`
- `u_cv = concat(t_cv_W/s_W, t_cv_S/s_S)`
- `u_K2i = concat(t_K2i_W/s_W, t_K2i_S/s_S)`

This inherits the equalization principle of the earlier frozen GDM combined-metric separator while preventing the known-sector control from choosing its own favorable rescaling.

## Frozen angle

`theta(a,b) = arccos[(a·b)/(||a|| ||b||)]` in degrees, clipped only for floating-point roundoff.

Record for each K2 point:

- `theta(K2_i, cs2)`
- `theta(K2_i, cv2)`

and the minimum angle to each axis across the five K2 points.

## Prospective classification

The threshold is inherited unchanged from the already frozen GDM combined-metric separator: **45 degrees**.

- `K2_JOINT_DIRECTION_SEPARATED_FROM_BOTH_GDM_AXES_EXP071E` if both minima are `>=45°`.
- `K2_JOINT_DIRECTION_OVERLAPS_CS2_ONLY_EXP071E` if min-to-cs2 `<45°` but min-to-cv2 `>=45°`.
- `K2_JOINT_DIRECTION_OVERLAPS_CV2_ONLY_EXP071E` if min-to-cv2 `<45°` but min-to-cs2 `>=45°`.
- `K2_JOINT_DIRECTION_OVERLAPS_BOTH_GDM_AXES_EXP071E` if both minima are `<45°`.

The equality case belongs to “separated” because the inherited separator itself uses `>=45°`.

## Interpretation boundary

Even a separation from both tested GDM axes would not prove universal dark-sector specificity. It would show only that this exact known-sector K2 matter-space mimic is directionally separated from the two frozen local GDM axes in this joint metric representation.

An overlap with one or both axes must be kept as a falsification result; no retuning of the 45° threshold or channel scales is permitted after output.

## Forbidden operations

- no new CLASS/GDM solver runs;
- no retraining of F30;
- no K2-dependent channel normalization;
- no covariance weighting, nuisance fitting or survey window weighting;
- no dropping individual K2 points after seeing their angles;
- no absolute-value folding of vector signs beyond the already defined `r_W` construction;
- no G7/G8/G9 scoring.

## Gate state

G7/G8/G9 remain OPEN irrespective of outcome.
