# DSIR research log — Experiment 046 scale-time interaction morphology

**Date:** 2026-08-25  
**Branch:** `research/scale-time-interaction-morphology-v0-1`  
**Purpose:** continue cross-family model comparison after Exp045A falsified the simple additive `(G,T,tau)` response core.

## Chronology

1. Exp045A established the orthogonal decomposition
   \[
   R(z,k)=\mu+T(k)+\tau(z)+I(z,k)
   \]
   and showed a large irreducible interaction for C5 designer f(R), moderate interaction for C3 GDM, weak interaction for C1 smooth-w and near-null interaction for the current C2 IDE directions.
2. Before looking at new pairwise targets, Exp046 froze an exact pairwise decomposition based on normalized response directions and the same orthogonal projector.
3. No scientific threshold on `eta_I` or interaction-shape angles was defined. Only numerical operator controls could fail the workflow.
4. Interaction-shape angles were allowed only above the pre-frozen morphology floor `chi_I>=1e-6`; below that, interaction is reported near-null rather than normalized into an unstable direction.
5. Hard run `32884761188` completed successfully.
6. Artifact `9577142860`, SHA256 `6e2c7026efe17a81bee10c9a9904c78f5299dce1bf594535be5ded600a3d2834`.

## Mathematics

For one model direction,

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2}.
\]

For two response directions,

\[
u_A=R_A/\|R_A\|,\quad u_B=R_B/\|R_B\|,
\]

\[
s=\mathrm{sign}\langle u_A,u_B\rangle,\quad d=u_A-su_B.
\]

Because the core and interaction subspaces are orthogonal,

\[
d=d_C+d_I,
\]

\[
\|d\|^2=\|d_C\|^2+\|d_I\|^2.
\]

Define

\[
\eta_I=\frac{\|d_I\|^2}{\|d\|^2}.
\]

This is an exact fraction of normalized pairwise response-shape separation power, not a significance or detectability statistic.

## Hard controls

- max unit norm error: `5.421e-20`;
- max core/interaction orthogonality residual: `1.012e-14`;
- max pairwise Pythagorean residual: `3.253e-19`;
- max acute-angle/chord identity residual: `4.759e-15`.

All are below the frozen `1e-12` ceiling.

## Direction-level interaction strength

- C1 smooth-w: `chi_I=0.0010805071`;
- C2 IDE alpha: `1.5727e-11`;
- C2 IDE beta: `5.4945e-11`;
- C3 GDM cs2: `0.0453054334`;
- C3 GDM cv2: `0.0436336888`;
- C5 designer f(R): `0.2998564797`.

Working hierarchy on this frozen local grid:

`IDE near-null -> smooth-w weak -> GDM moderate -> f(R) strong`.

This hierarchy is a hypothesis for the next stability tests, not a law.

## Pairwise interaction localization

- GDM cs2/cv2: `eta_I=0.73113854`, total acute angle `0.322616 deg`;
- GDM cs2/f(R): `eta_I=0.61198209`, total acute angle `25.181845 deg`;
- GDM cv2/f(R): `eta_I=0.61382909`, total acute angle `25.488143 deg`;
- IDE alpha/f(R): `eta_I=0.57194600`, total acute angle `42.450273 deg`;
- IDE beta/f(R): `0.30533964`;
- smooth-w/f(R): `0.28035371`;
- IDE alpha/GDM cs2: `0.24302738`;
- IDE alpha/GDM cv2: `0.23682167`;
- IDE alpha/beta: `1.486e-11`.

## Interaction morphology

- GDM cs2/cv2 interaction-shape angle: `0.742556 deg`;
- GDM cs2/f(R): `10.985703 deg`;
- GDM cv2/f(R): `11.710540 deg`;
- smooth-w versus GDM/f(R): approximately `69.6-70.0 deg`.

## Scientific interpretation

**Hard:** a substantial fraction of the GDM/f(R) low-k structure separation is specifically localized in nonseparable scale-time response: about `61%` of normalized pairwise separation power.

**Hard refinement:** `eta_I` alone is not a discriminator or significance. GDM pressure/viscosity have the largest `eta_I` (`73%`) but remain almost identical overall and also have nearly identical interaction shapes. Metric slip remains necessary for that microphysical distinction.

**Supported hypothesis:** `chi_I` plus interaction morphology may form a useful mechanism-classification layer. The next tests must determine whether this survives parameter amplitude, solver precision and grid/domain perturbation.

## Exact next actions

1. Exp047A: amplitude/finite-step stability of `chi_I` and interaction morphology.
2. Exp047B: leave-one-k/leave-one-z-node stability of `chi_I` and key `eta_I`.
3. If stable, pre-freeze an independent confirmatory classification gate rather than thresholding these observed values post hoc.
4. Build a time-dependent high-k C4 WDM atlas before any family-complete interaction claim.
5. Continue slip/lensing and observation-space shape/RSD work in parallel.
6. G7/G8 remain open.
