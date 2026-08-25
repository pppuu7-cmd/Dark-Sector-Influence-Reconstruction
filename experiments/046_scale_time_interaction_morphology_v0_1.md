# Experiment 046 — scale-time interaction morphology v0.1

**Date:** 2026-08-25  
**Status:** protocol frozen before first Exp046 target output  
**Scope:** common frozen low-k C1/C2/C3/C5 structure atlas; C4 WDM excluded until a high-k time-dependent atlas exists.

## Motivation

Experiment 045A falsified the simple additive `G+T+tau` core and identified an irreducible scale-time interaction

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k).
\]

The new question is comparative: **how much of each model direction, and how much of each pairwise model distinction, lives specifically in `I(k,z)`?**

This experiment does not declare `I` a new fundamental parameter. It is a hard-controlled descriptive morphology comparison intended to discover whether a useful new cross-family pattern exists.

## Input

`data/derived/comparison_readiness/local_response_tangents_v0_1.json`

on the frozen common grid

- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Directions: C1 smooth-w, C2 IDE negative-alpha/beta, C3 GDM cs2/cv2, C5 designer-f(R).

## Direction-level statistic

For each response,

\[
\boxed{\chi_I=\frac{\|I\|^2}{\|R\|^2}}.
\]

`chi_I` is invariant under an overall rescaling of the tangent direction, so it is suitable for comparing mechanisms with different tangent normalizations.

## Pairwise interaction contribution

Normalize each response:

\[
u_A=R_A/\|R_A\|,\qquad u_B=R_B/\|R_B\|.
\]

Choose `s=sign(<u_A,u_B>)` so the pair uses the same acute/orientation convention as the existing comparison atlas, and define

\[
d=u_A-su_B.
\]

Because the additive-core and interaction projectors are linear and orthogonal,

\[
d=d_C+d_I,
\]

with

\[
\|d\|^2=\|d_C\|^2+\|d_I\|^2.
\]

Define

\[
\boxed{\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}},
\qquad
\eta_C=1-\eta_I.
\]

`eta_I` answers: *what fraction of the normalized pairwise shape-separation power resides specifically in scale-time nonseparability?*

## Interaction-shape morphology

A normalized interaction shape `I/||I||` is reported only when

`chi_I >= 1e-6`.

This is a pre-frozen **numerical morphology-validity floor**, not a discovery or mechanism threshold. Directions below it are labeled `INTERACTION_NEAR_NULL` and no unstable interaction-angle is produced.

No threshold is frozen on `eta_I` or interaction-shape angles. Those outputs are descriptive and may motivate a later independent confirmatory gate.

## Hard controls

Require:

1. normalized response norm error `<=1e-12`;
2. additive/interaction orthogonality `<=1e-12`;
3. pairwise Pythagorean decomposition residual `<=1e-12`;
4. acute-angle/chord identity residual `<=1e-12`;
5. all finite non-null pair distances handled without division by zero.

Only control failure fails the workflow. Scientific morphology is reported without post-hoc pass/fail thresholds.

## Claim boundary

This is unwhitened theory-response geometry. It is not survey distinguishability, an intrinsic-rank estimate, a universal `I` parameter, a no-hair theorem, a residual law, or a discovery. C4 is missing by domain contract, not zero.
