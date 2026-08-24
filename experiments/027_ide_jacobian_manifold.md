# Experiment 027 — interacting-vacuum alpha-beta Jacobian manifold

Date: 2026-08-24
Status: CALIBRATION DEFINED; RUN PENDING
Gate: G3B / C2 perturbation-manifold construction

## Purpose

The earlier interacting-vacuum work established the zero-coupling closure and the exact background degeneracy of a one-parameter beta-like interaction with constant-w CDM. That is not enough for DSIR: the full source-authored model contains two interaction coefficients,

\[
\boxed{Q=\alpha H\rho_{idm}+\beta H\rho_{iv}},
\]

and their local response directions must be measured rather than assumed.

The first goal is to ask whether alpha and beta are observationally distinct in the frozen response basis and whether any background degeneracy is broken by the structure channel.

## Solver and composition

Pinned source:

`kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`

with the already assertion-checked compile-only repair in

`patches/apply_class_iv_ac627d54_compile_fix.py`.

Use

`f_idm_iv=1`, `f_iv=1`.

In the pinned source this converts the input CDM density into the interacting-DM component (apart from the tiny synchronous-gauge residual required by the legacy solver) and converts the implicit Lambda density into the interacting-vacuum component. The physical composition is therefore held fixed while alpha and beta are varied.

## Common baseline

- `h=0.67`
- `omega_b=0.0224`
- source `omega_cdm=0.1200`
- `N_ur=3.046`, no massive neutrinos
- `A_s=2.10e-9`
- `n_s=0.965`
- `YHe=0.2404`
- flat geometry
- synchronous gauge
- linear matter power
- matched p8 precision preset used by the CLASS-family response bridge

## Symmetric calibration axes

Reference:

\[
(\alpha,\beta)=(0,0).
\]

Alpha-only axis:

\[
(\pm10^{-4},0),\ (\pm10^{-3},0),\ (\pm10^{-2},0).
\]

Beta-only axis:

\[
(0,\pm10^{-4}),\ (0,\pm10^{-3}),\ (0,\pm10^{-2}).
\]

The smallest symmetric pair is used for the first central-difference tangent estimate. Larger pairs diagnose tangent rotation and nonlinearity. This is calibration only: no singular-value or angle threshold for declaring rank two is pre-frozen.

## Response channels

Background expansion:

\[
\boxed{r_H(z)=\ln\frac{H_{\alpha,\beta}(z)}{H_{0,0}(z)}}.
\]

Matter clustering:

\[
\boxed{r_\Delta(k,z)=\ln\frac{P_{\alpha,\beta}(k,z)}{P_{0,0}(k,z)}}.
\]

Frozen nodes:

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\ h/{\rm Mpc}.
\]

The extractor reads redshift from each CLASS P(k) header and interpolates H from the solver background table.

## Local Jacobian

At central step `h=1e-4`, estimate

\[
t_\alpha=\frac{r(+h,0)-r(-h,0)}{2h},
\]

\[
t_\beta=\frac{r(0,+h)-r(0,-h)}{2h}.
\]

For both `H` and `P` channels record:

- tangent norms;
- angle between alpha and beta tangents;
- two-row Jacobian singular spectrum;
- even/odd ratio of the symmetric pair as a local nonlinearity/numerical-offset diagnostic.

For `h=1e-3` and `1e-2`, compare the finite-difference P-channel tangent to the `1e-4` tangent to measure curvature/nonlinearity along each interaction axis.

## Physical validity mask

The full background table exposes both interacting densities. Every successful model is additionally checked for

\[
\rho_{idm}>0,\qquad \rho_{iv}\ge0
\]

over the full background history returned by the solver.

A point with a solver failure or negative interacting density is recorded as invalid. It is never converted to a zero vector and never imputed into rank analysis.

## Why this experiment matters

If alpha and beta are nearly parallel in `r_H` but clearly non-parallel in `r_Delta`, the growth/structure channel becomes an explicit discriminant edge for an otherwise background-degenerate interaction family. That would be a concrete DSIR example of the general principle that model names are not observational classes and that extra channels are required to break dark degeneracies.

This result would still be known-model response geometry, not a new dark-sector law.

## Next steps after calibration

1. Inspect which symmetric points are physically valid.
2. Quantify alpha-beta tangent angle separately in H and P.
3. If calibration is stable, pre-freeze a Jacobian-conditioning/rank threshold and repeat a fresh hard run.
4. Add the valid C2 tangent patch to the family-balanced atlas.
5. Compare its tangent directions with GDM, WDM and designer-f(R) response directions only on common valid cells/channels.
