# Exp071E — K2 joint metric-direction specificity control preregistration v0.1

**Frozen before any Exp071E science output is computed.**

Date: 2026-08-28

## Scientific question

Exp071C established that the known-sector K2 family — baryon/CDM redistribution at fixed total physical matter density — reproduces the frozen matter-only F30 criterion. Exp071D then established that the scalar ratio `||Delta_slip||/||r_W||` overlaps at least the GDM sound-speed-like axis. Exp071E asks the stricter geometric question:

> Does the *full joint direction* in `(r_W, Delta_slip)` separate the smallest-step K2 known-sector control from both frozen local GDM axes `cs2` and `cv2`?

This is a mechanism-space specificity control. It is not an observational likelihood test and cannot close G7, G8 or G9.

## Immutable parent bindings

- Exp071C run: `33020201997`; its successful immutable result must report `F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL` and K2 full + all leave-one-z PASS.
- GDM Weyl/slip hard-regression run: `32774198185`; its immutable result must report `PASS_GDM_SLIP_BREAKS_LOW_K_DEGENERACY`.
- Exp071D run: `33176559280`; its immutable result is contextual only and must report `K2_SLIP_TO_WEYL_RATIO_OVERLAPS_GDM_AXES_EXP071D`. No Exp071D number is allowed to tune the Exp071E metric or threshold.
- Official CLASS is pinned to commit `e85808324f51fc694d12e3ed7439552a3c3f9540`.

## Frozen known-sector family

Reference:

- `omega_b = 0.0224`
- `omega_cdm = 0.1200`
- `omega_m = 0.1424`

K2 points, all at fixed `omega_m = 0.1424`:

| point | omega_b | omega_cdm |
|---|---:|---:|
| bar1 | 0.0228 | 0.1196 |
| bar2 | 0.0232 | 0.1192 |
| bar3 | 0.0236 | 0.1188 |
| bar4 | 0.0240 | 0.1184 |
| bar5 | 0.0244 | 0.1180 |

The **primary K2 tangent is frozen to bar1**, the smallest positive step from the reference. Larger steps are robustness diagnostics only and cannot change the primary classification rule.

## Frozen response grid and definitions

Redshifts:

`z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`

Wavenumbers:

`k = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`

At every `(z,k)` point, using CLASS transfer-function columns `phi` and `psi`:

- `W = phi + psi`
- `r_W = ln |W_model / W_ref|`
- `slip = (phi - psi)/(phi + psi)`
- `Delta_slip = slip_model - slip_ref`

Interpolation is linear in `log(k)` for signed `phi` and `psi`, exactly following the existing GDM Weyl/slip extractor.

All response arrays are flattened in ascending redshift, then the frozen k order.

## Tangents

For K2 point `i`, define

`delta_f_b = (omega_b_i - omega_b_ref)/omega_m`.

Then

- `t_W,K2 = r_W / delta_f_b`
- `t_S,K2 = Delta_slip / delta_f_b`.

The primary tangent is the `bar1` tangent.

For GDM, use the **1e-7 local tangents only** from the immutable parent artifact:

- `t_W,cs = r_W(cs2_1e-7)/1e-7`
- `t_S,cs = Delta_slip(cs2_1e-7)/1e-7`
- `t_W,cv = r_W(cv2_1e-7)/1e-7`
- `t_S,cv = Delta_slip(cv2_1e-7)/1e-7`.

## Frozen joint-channel equalization

Use exactly the equalization convention of the existing GDM combined-metric separator:

- `s_W = max(||t_W,cs||, ||t_W,cv||, 1e-300)`
- `s_S = max(||t_S,cs||, ||t_S,cv||, 1e-300)`

Construct joint vectors

- `u_K2 = [t_W,K2/s_W, t_S,K2/s_S]`
- `u_cs = [t_W,cs/s_W, t_S,cs/s_S]`
- `u_cv = [t_W,cv/s_W, t_S,cv/s_S]`.

No scale may be recomputed from K2, because that would allow the known-sector family to tune the metric.

## Primary frozen statistic

Compute the Euclidean angles

- `theta_K2_cs = angle(u_K2_bar1, u_cs)`
- `theta_K2_cv = angle(u_K2_bar1, u_cv)`.

The threshold is frozen to **45 degrees**, inherited unchanged from the prior GDM equalized combined-metric hard gate.

Primary classification:

- if **both** angles are `>= 45 deg`:
  `K2_DIRECTION_SEPARATED_FROM_BOTH_GDM_AXES_EXP071E`
- otherwise:
  `K2_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071E`

The threshold and classification rule must not be changed after seeing Exp071E output.

## Frozen robustness diagnostics — non-classifying

For bar2 through bar5, report:

- joint angle to the primary bar1 K2 vector;
- joint angle to GDM `cs2`;
- joint angle to GDM `cv2`;
- channel-specific `r_W` and `Delta_slip` angle to bar1;
- K2-family centered SVD in the equalized joint space.

These diagnose curvature / finite-step stability only. They cannot rescue a primary FAIL or overturn a primary PASS.

## Integrity requirements

The run must fail closed unless:

1. all parent classifications match the immutable expected statuses;
2. the CLASS upstream SHA is exact;
3. all 7 transfer-function redshifts exist for reference and all five K2 points;
4. all frozen k points lie inside every transfer grid;
5. Weyl denominators are nonzero on the frozen grid;
6. the GDM parent supplies both `cs2_1e-7` and `cv2_1e-7` response arrays;
7. all primary tangent norms are finite and nonzero.

## Interpretation boundary

A PASS would show that this specific known-sector matter-morphology mimic points in a different **joint local response direction** from both tested GDM axes under a metric frozen from the GDM control. It would not prove uniqueness of the dark sector, identify a microscopic model, or constitute observational evidence.

A FAIL would show that adding the present joint `(r_W, Delta_slip)` direction is still insufficient for generic mechanism specificity against this known-sector control. It would strengthen the need for additional channels/observables rather than falsify DSIR's channel-conditioned framework.

Irrespective of outcome:

- `G7 = OPEN`
- `G8 = OPEN`
- `G9 = OPEN`
