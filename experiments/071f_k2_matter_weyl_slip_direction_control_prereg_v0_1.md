# Exp071F — K2 matter + Weyl + slip direction control preregistration v0.1

**Frozen before any Exp071F science output is computed.**

Date: 2026-08-28

## Motivation

Exp071C showed that the K2 fixed-total-matter baryon/CDM family can reproduce the matter-only F30 morphology. Exp071D showed that a scalar slip/Weyl norm ratio overlaps the GDM sound-speed scale. Exp071E then showed that the full equalized `(r_W, Delta_slip)` K2 direction remains close to the GDM `cs2` axis (`18.93 deg`) while separating from the GDM `cv2` axis (`58.91 deg`).

Exp071F asks whether adding the independent **matter power response direction itself** to that same common-grid joint geometry breaks the residual K2-vs-`cs2` ambiguity.

This is a mechanism-space specificity control only. It cannot close G7, G8 or G9.

## Immutable parent bindings

- Exp071C run `33020201997`, artifact `9626235928`: known-sector matter spectra and frozen K2 family; must report K2 full + all leave-one-z F30 PASS.
- GDM Weyl/slip run `32774198185`, artifact `9537340616`: immutable GDM `gdm0`, `cs2_1e-7`, `cv2_1e-7` spectra/transfer functions and metric-response JSON; hard gate must report `PASS_GDM_SLIP_BREAKS_LOW_K_DEGENERACY`.
- Exp071E run `33177588360`, artifact `9688299959`: K2 transfer functions and terminal classification `K2_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071E`.
- Official CLASS upstream for all relevant generated spectra is pinned to `e85808324f51fc694d12e3ed7439552a3c3f9540` for K2 and the previously frozen pinned GDM_CLASS parent for the GDM local axes.

No Exp071F threshold or scaling may be tuned from the Exp071F result.

## Frozen grid

`z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`

`k = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`

All channels are flattened in ascending redshift and the frozen k order.

## Frozen channel definitions

### Matter channel

From positive matter power spectra:

`r_P(z,k) = ln(P_model(z,k) / P_ref(z,k))`.

Interpolation is linear in `ln(k)` for `ln(P)`, matching the existing F30/Exp071C response extraction.

### Weyl/slip channels

Exactly as Exp071E:

- `W = phi + psi`
- `r_W = ln |W_model/W_ref|`
- `slip = (phi-psi)/(phi+psi)`
- `Delta_slip = slip_model-slip_ref`.

Signed `phi` and `psi` are interpolated linearly in `ln(k)` before constructing the responses.

## Frozen tangents

Primary K2 tangent: **bar1 only**, using

`delta_f_b = (omega_b_bar1 - omega_b_ref)/omega_m`, with `omega_m=0.1424`.

For each channel `C in {P,W,S}`:

`t_C,K2 = response_C(bar1)/delta_f_b`.

GDM local tangents use the **1e-7** points only:

`t_C,cs = response_C(cs2_1e-7)/1e-7`

`t_C,cv = response_C(cv2_1e-7)/1e-7`.

## Frozen three-channel equalization

Each channel scale is determined **only from the two GDM parent axes**:

- `s_P = max(||t_P,cs||, ||t_P,cv||, 1e-300)`
- `s_W = max(||t_W,cs||, ||t_W,cv||, 1e-300)`
- `s_S = max(||t_S,cs||, ||t_S,cv||, 1e-300)`.

K2 is forbidden from setting or modifying any channel scale.

Construct

- `u_K2 = [t_P,K2/s_P, t_W,K2/s_W, t_S,K2/s_S]`
- `u_cs = [t_P,cs/s_P, t_W,cs/s_W, t_S,cs/s_S]`
- `u_cv = [t_P,cv/s_P, t_W,cv/s_W, t_S,cv/s_S]`.

## Frozen primary statistic and classification

Compute

- `theta_K2_cs_3ch = angle(u_K2, u_cs)`
- `theta_K2_cv_3ch = angle(u_K2, u_cv)`.

The separator threshold remains **45 degrees**, inherited unchanged from the previous equalized combined-metric separator and Exp071E.

Classification:

- if both angles are `>=45 deg`:
  `K2_3CHANNEL_DIRECTION_SEPARATED_FROM_BOTH_GDM_AXES_EXP071F`
- otherwise:
  `K2_3CHANNEL_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071F`.

No post-result threshold change is allowed.

## Frozen robustness diagnostics — non-classifying

For bar2..bar5, report three-channel angle to bar1 and to both GDM axes. Also report:

- matter-only K2-bar1 vs GDM `cs2` and `cv2` angles;
- the already-frozen two-channel `(r_W,Delta_slip)` angles recomputed as an integrity cross-check and required to reproduce Exp071E within `1e-8 deg`;
- three-channel K2-family centered SVD;
- maximum bar1-to-larger-step three-channel drift.

These diagnostics cannot change the bar1 classification.

## Fail-closed integrity conditions

The calculation is invalid unless:

1. all parent classifications/statuses match their immutable expected values;
2. all K2 and GDM matter spectra have exactly the frozen 7 redshift outputs and cover all frozen k nodes;
3. all positive matter spectra remain positive on the interpolation support;
4. all Weyl denominators are finite/nonzero on the common grid;
5. the recomputed two-channel primary angles match Exp071E to `1e-8 deg`;
6. all channel tangent norms and GDM-only equalization scales are finite and nonzero.

## Interpretation boundary

A PASS would establish only that adding the matter direction separates this specific K2 known-sector mimic from the two tested local GDM axes under the frozen three-channel metric. It would not establish generic dark-sector uniqueness or observational evidence.

A FAIL would demonstrate that even matter + Weyl + slip on this support retains a known-sector/local-GDM degeneracy, directly motivating still more independent channels or observational blocks.

Irrespective of outcome:

- `G7 = OPEN`
- `G8 = OPEN`
- `G9 = OPEN`
