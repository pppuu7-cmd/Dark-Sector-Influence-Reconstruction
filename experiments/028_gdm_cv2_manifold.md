# Experiment 028 — GDM viscosity and two-axis local Jacobian

Date: 2026-08-24
Status: CALIBRATION DEFINED; RUN PENDING
Gate: G3B / C3 multi-axis perturbation-manifold construction

## Purpose

Experiment 025 established a genuine nonzero GDM sound-speed response axis and showed why local tangent rank must be separated from global SVD span. The next required step is to add a second independent GDM microphysical direction rather than treating the one-parameter sound-speed curve as the whole family.

Pinned GDM_CLASS documents three independently binned GDM functions: equation of state `w`, sound speed `cs2`, and viscosity `cv2`. This experiment holds

\[
w=0,
\]

uses dynamic shear, and varies constant viscosity while retaining the same zero-closure reference, cosmology, p8 precision preset, redshift nodes and k nodes as Experiment 025.

## Solver and grid

Pinned solver:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`

Frozen response grid:

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\ h/{\rm Mpc}.
\]

Reference:

\[
w=c_s^2=c_v^2=0.
\]

Viscosity scan:

\[
c_v^2=10^{-8},10^{-7},10^{-6},10^{-5},10^{-4}.
\]

The response is

\[
\boxed{r_\Delta(k,z;c_v^2)=\ln\frac{P(k,z;c_v^2)}{P(k,z;0)}}.
\]

## Same-run sound-speed control

To measure the angle between GDM sound-speed and viscosity directions without importing an artifact from a different CI environment, the workflow also recomputes the local sound-speed controls

\[
c_s^2=10^{-8},10^{-7},10^{-6}
\]

against the same zero reference in the same build and p8 environment.

For each axis a local tangent is estimated by averaging the scaled local responses,

\[
t_s\simeq\langle r(c_s^2)/c_s^2\rangle,
\qquad
t_v\simeq\langle r(c_v^2)/c_v^2\rangle,
\]

for parameter values no larger than `1e-6`.

The two-axis Jacobian diagnostic is

\[
J_{GDM}=\begin{pmatrix}t_s\\t_v\end{pmatrix}.
\]

The workflow reports the tangent angle and the two singular values of this local sampled Jacobian.

## Interpretation rule

This is calibration only. No threshold for declaring the two directions statistically or physically resolved is chosen from this run. In particular,

- local non-collinearity is not automatically a new degree-of-freedom discovery;
- the two singular values are response-geometry diagnostics, not a microscopic field count;
- any future PASS threshold for local GDM Jacobian rank must be frozen before a fresh regression run;
- this is known-model response geometry, not a new dark-sector law.

## Scientific use

If the sound-speed and viscosity tangents are non-collinear, C3 becomes the first DSIR control family with an explicitly measured multi-axis local response patch. This will be used later to ask whether cross-family directions (WDM, interacting vacuum, designer f(R)) lie inside or outside the local GDM tangent span on common valid cells.
