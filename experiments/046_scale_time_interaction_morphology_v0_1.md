# Experiment 046 — scale-time interaction morphology v0.1

**Date:** 2026-08-25  
**Status:** `PASS_SCALE_TIME_INTERACTION_MORPHOLOGY_CONTROLS_V0_1`  
**Scope:** common frozen low-k C1/C2/C3/C5 structure atlas; C4 WDM excluded until a high-k time-dependent atlas exists.

## Motivation

Experiment 045A falsified the simple additive `G+T+tau` core and identified an irreducible scale-time interaction

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k).
\]

The comparative question is: **how much of each model direction, and how much of each pairwise model distinction, lives specifically in `I(k,z)`?**

This experiment does not declare `I` a new fundamental parameter. It is a hard-controlled descriptive morphology comparison.

## Input

`data/derived/comparison_readiness/local_response_tangents_v0_1.json`

on the frozen common grid

- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Directions: C1 smooth-w, C2 IDE negative-alpha/beta, C3 GDM cs2/cv2, C5 designer-f(R).

## Direction-level statistic

\[
\boxed{\chi_I=\frac{\|I\|^2}{\|R\|^2}}.
\]

`chi_I` is invariant under an overall rescaling of a tangent direction.

## Pairwise interaction contribution

Normalize each response:

\[
u_A=R_A/\|R_A\|,\qquad u_B=R_B/\|R_B\|.
\]

Choose `s=sign(<u_A,u_B>)` and define

\[
d=u_A-su_B.
\]

Because the additive-core and interaction projectors are linear and orthogonal,

\[
d=d_C+d_I,
\]

\[
\boxed{\|d\|^2=\|d_C\|^2+\|d_I\|^2}.
\]

Define

\[
\boxed{\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}},\qquad \eta_C=1-\eta_I.
\]

`eta_I` is the fraction of normalized pairwise shape-separation power that lives in scale-time nonseparability. It is **not** a significance, Bayes factor, S/N, or detectability measure.

## Frozen morphology floor and hard controls

Interaction-shape angles are emitted only when `chi_I >= 1e-6`. This is a numerical morphology-validity floor, not a discovery/mechanism threshold.

Hard controls, all frozen before target interpretation:

1. normalized response norm error `<=1e-12`;
2. additive/interaction orthogonality `<=1e-12`;
3. pairwise Pythagorean residual `<=1e-12`;
4. acute-angle/chord identity residual `<=1e-12`.

No scientific threshold was frozen on `eta_I` or interaction-shape angles.

## Hard run and provenance

- workflow run: `32884761188`;
- source head: `d292cb90245c3e472dcbffd076947181fd6ed7cf`;
- artifact ID: `9577142860`;
- artifact name: `scale-time-interaction-morphology-v0-1-a6740dc1006954941e54b83658658b2e2c3fce54`;
- artifact SHA256: `6e2c7026efe17a81bee10c9a9904c78f5299dce1bf594535be5ded600a3d2834`;
- repo result summary: `data/derived/comparison_readiness/experiment_046_scale_time_interaction_morphology_v0_1.json`.

Controls:

- max unit-norm error `5.42e-20`;
- max core/interaction orthogonality residual `1.01e-14`;
- max pairwise Pythagorean residual `3.25e-19`;
- max angle/chord identity residual `4.76e-15`.

All controls pass comfortably.

## Direction morphology

| Direction | `chi_I` | Interpretation on frozen block |
|---|---:|---|
| C1 smooth-w | `1.0805e-3` | small but valid interaction |
| C2 IDE negative-alpha | `1.5727e-11` | interaction near-null |
| C2 IDE beta | `5.4945e-11` | interaction near-null |
| C3 GDM cs2 | `4.53054e-2` | material interaction |
| C3 GDM cv2 | `4.36337e-2` | material interaction |
| C5 designer f(R) | **`2.99856e-1`** | **large interaction component** |

This confirms the striking mechanism ordering first exposed by Exp045A: local IDE directions are essentially additive on the current grid, smooth-w has weak nonseparability, GDM has moderate nonseparability, and designer f(R) has strong nonseparability.

## Pairwise separation decomposition

Highest descriptive `eta_I` values:

| Pair | full acute angle | `eta_I` |
|---|---:|---:|
| GDM cs2 / GDM cv2 | `0.322616 deg` | **`0.731139`** |
| GDM cv2 / f(R) | `25.488143 deg` | **`0.613829`** |
| GDM cs2 / f(R) | `25.181845 deg` | **`0.611982`** |
| IDE alpha / f(R) | `42.450273 deg` | **`0.571946`** |
| IDE beta / f(R) | `59.404101 deg` | `0.305340` |
| smooth-w / f(R) | `60.942974 deg` | `0.280354` |
| IDE alpha / GDM cs2 | `24.934547 deg` | `0.243027` |
| IDE alpha / GDM cv2 | `24.786398 deg` | `0.236822` |
| IDE alpha / IDE beta | `58.933798 deg` | `1.49e-11` |

### Critical interpretation rule

A large `eta_I` does **not** imply a large total model separation. The clearest counterexample is GDM cs2/cv2: `73.1%` of their separation power resides in `I`, but the total acute angle is only `0.323 deg`. Thus interaction carries most of a **tiny** distinction.

For GDM/f(R), by contrast, the total separation is already material at theory-response level (`~25 deg`) and `~61%` of that separation power resides in interaction. Here `I(k,z)` materially carries cross-mechanism discrimination within the frozen theory block.

## Interaction-shape geometry

For valid interaction components:

- GDM cs2/cv2 interaction shapes: `0.742556 deg` acute — still extremely similar;
- GDM cs2/f(R): `10.985703 deg`;
- GDM cv2/f(R): `11.710540 deg`;
- smooth-w vs GDM/f(R) interaction shapes: roughly `69.6-70.0 deg`.

This says two different things simultaneously:

1. GDM pressure and viscosity share almost the same interaction morphology, so `I` alone does not solve their microphysical degeneracy;
2. GDM and designer f(R) have related but measurably different interaction morphology, while smooth-w interaction is qualitatively different.

## Scientific interpretation

**HARD on this frozen unwhitened theory block:** scale-time interaction is not merely a residual bookkeeping term. It carries a large fraction of pairwise response-shape separation for several cross-mechanism comparisons, especially GDM/f(R) and IDE-alpha/f(R).

**HARD negative refinement:** interaction is not a universal discriminator by itself. It dominates the tiny GDM cs2/cv2 separation power but leaves those mechanisms almost collinear; metric slip remains the established separator.

**Supported hypothesis:** the pair `(interaction strength chi_I, interaction morphology)` may be a useful mechanism-classification coordinate system, but this must survive tangent-step, solver-precision, domain, observation-kernel and withheld-family tests before any broader claim.

## Claim boundary

This is unwhitened theory-response geometry. It is not survey distinguishability, an intrinsic-rank estimate, a universal fourth parameter, a no-hair theorem, a residual law, or a discovery. C4 is missing by domain contract, not zero.
