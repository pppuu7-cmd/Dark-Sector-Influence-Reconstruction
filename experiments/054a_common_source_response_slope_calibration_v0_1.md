# Experiment 054A — common source-response slope calibration v0.1

Date: 2026-08-26
Status: PREREGISTERED CALIBRATION BEFORE C7 OUTPUTS
Gate relevance: prospective G7/G8 preparation only

## Question

Can two already validated transition-scale mechanisms, C3 GDM dynamic shear and C5 designer f(R), be expressed with one common **full-response** localization law that does not depend on the interaction residual `I`?

This calibration is performed entirely on immutable Exp049B and Exp049C products. It must finish before any C7 IDM-DR matter-power response is generated.

## Common response operator

For a response matrix

\[
R(z,k)=\ln[P_{model}(k,z)/P_{ref}(k,z)],
\]

define full response-power scale weights

\[
q_k^R(k)=\frac{\sum_z R(z,k)^2}{\sum_{z,k}R(z,k)^2},
\qquad
k_R^{geo}=\exp\left[\sum_k q_k^R(k)\ln k\right].
\]

This operator is valid even when the additive interaction residual is nearly zero; it therefore avoids making `I` a universal coordinate.

## Mechanism-native source scales

C3 uses the already frozen Exp049B dynamic-shear quasi-steady scale at `z=1.317`,

\[
k_*^{C3}=k_{v,QS}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2}.
\]

C5 uses the already source-derived Exp049C exact designer-f(R) Compton-scale summary,

\[
k_*^{C5}=k_{C,min}
\]

over the frozen redshift nodes. No response quantity is used to define either source scale.

## Common dimensionless slope

For consecutive amplitude points ordered along each physical ray,

\[
\boxed{\mathcal C_i=\frac{\Delta\ln k_R^{geo}}{\Delta\ln k_*}}.
\]

The candidate common relation is **co-motion in logarithmic scale space**, `C_i>0`.

## Frozen branching rule before calibration output

1. Recompute `k_R_geo` directly from immutable Exp049B/Exp049C response matrices, never from the previously reported `k_I_geo` values.
2. If **any** eligible adjacent C3 or C5 slope is non-finite or `<=0`, mark the common-slope calibration `REJECTED` and do not launch a C7 test under this law.
3. If all slopes are positive, define the prospective C7 acceptance band mechanically as

\[
C_{low}=0.5\min_i C_i,\qquad C_{high}=2\max_i C_i.
\]

4. The C7 test must freeze its source-scale definition, parameter grid, response domain and requirement that every adjacent C7 slope lies inside this band **before the first C7 P(k,z) output**.
5. No recalibration after C7 is allowed.

The factors `0.5` and `2` are frozen now as a deliberately broad factor-two extrapolation margin; they are not chosen from calibration or C7 outputs.

## Inputs

- Exp049B run `32904158849`, C3 GDM withheld dynamic-shear artifact.
- Exp049C run `32907619613`, C5 designer-f(R) withheld artifact.
- frozen low-k nodes `{0.001,0.003,0.01,0.03,0.1} h/Mpc`;
- frozen seven DSIR redshift nodes.

## Boundaries

- Calibration is retrospective by construction; it cannot itself close G7 or G8.
- A positive calibration only authorizes a prospective C7 test.
- `k_v_QS` remains a quasi-steady proxy, while the C5 Compton diagnostic is source-native to the pinned designer solver.
- No fundamental parameter count, no-hair theorem, observation-space detectability or universal rank follows.
- C4 WDM is not silently inserted: its current withheld cutoff coordinate is response-defined rather than a separately validated source-native scale. It can be bridged later only with an explicit thermal free-streaming source operator.
