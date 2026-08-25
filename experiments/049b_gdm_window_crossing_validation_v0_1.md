# Experiment 049B — withheld GDM window-crossing validation v0.1

**Date:** 2026-08-26  
**Status:** prediction frozen before intermediate solver outputs  
**Parent:** Exp048B + Exp049A source audit.

## Motivation

Exp048B already showed the endpoints of a finite-amplitude GDM viscosity ray: `k_I_geo` is almost stationary through small `cv2`, then shifts downward between `cv2=1e-5` and `1e-4`. Exp049A source audit derives the dynamic-shear quasi-steady scale

\[
k_{v,\mathrm{QS}}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2}.
\]

At the fixed frozen reference redshift `z=1.317`, the immutable CLASS background gives the crossing of `k_v_QS=0.1 h/Mpc` at approximately

\[
\boxed{c_v^2\simeq1.08\times10^{-5}}.
\]

The previous endpoint data therefore suggest a concrete, independently testable interpolation prediction once the physical scale has entered the DSIR low-k window.

## Withheld amplitude grid

The following models had not been generated when the prediction was frozen:

\[
\boxed{c_v^2=1.5\times10^{-5},\;2\times10^{-5},\;3\times10^{-5},\;5\times10^{-5},\;7\times10^{-5}}.
\]

All other C3 settings, pinned GDM_CLASS SHA, p8 precision, cosmology, redshift nodes and k nodes are identical to the validated C3 viscosity workflow.

The source-derived quasi-steady scales at `z=1.317`, computed before these P(k,z) outputs exist, are approximately

| cv2 | k_v_QS [h/Mpc] |
|---:|---:|
| 1.5e-5 | 0.08485 |
| 2e-5 | 0.07348 |
| 3e-5 | 0.06000 |
| 5e-5 | 0.04647 |
| 7e-5 | 0.03928 |

Thus the entire withheld grid is predicted to sample progressive penetration of the viscous transition into `k<=0.1 h/Mpc`.

## Pre-frozen prediction

Only one scientific directional prediction is made:

\[
\boxed{k_I^{geo}(c_{v,i+1}^2)\le k_I^{geo}(c_{v,i}^2)+10^{-6}\;h/{\rm Mpc}}.
\]

In words: **the interaction-energy scale centroid must be non-increasing as `cv2` increases over the withheld grid.**

The `1e-6 h/Mpc` positive-step allowance is a numerical tolerance, not a fit to the intermediate outputs.

No prediction is made for

- the magnitude of the shift;
- equality of `k_I_geo` and `k_v_QS`;
- `z_I` monotonicity;
- `chi_I` monotonicity;
- metric-slip response.

Those would either overfit the already seen endpoints or require a more complete eigenmode analysis.

## Operator

Each same-run response is

\[
r_\Delta(k,z)=\ln\frac{P(k,z;c_v^2)}{P(k,z;0)}.
\]

As in Exp048, decompose

\[
r_\Delta=\mu+T(k)+\tau(z)+I(k,z),
\]

then define

\[
q_k(k)=\frac{\sum_z I^2}{\|I\|^2},
\qquad
k_I^{geo}=\exp\sum_k q_k\ln k.
\]

Algebraic decomposition, orthogonality and profile-normalization controls remain at `1e-12`.

## Interpretation

- If the monotonic prediction passes, the physical-window-crossing explanation gains genuinely independent support because the intermediate response fields were withheld when the direction was frozen.
- If it fails, the explanation is weakened and the failure is a scientific negative result; thresholds must not be changed afterward.
- A pass still does not establish `k_v_QS` as an exact eigenmode scale, a universal dark-sector law, a field count, G7, or G8.

This experiment deliberately predicts scale localization only. Exp048B already showed that time localization can behave differently across mechanisms, so no universal temporal flow is assumed.
