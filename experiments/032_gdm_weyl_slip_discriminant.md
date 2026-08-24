# Experiment 032 — GDM Weyl/slip discriminant for sound-speed vs viscosity

Date: 2026-08-24
Status: CALIBRATION DEFINED; RUN PENDING
Input degeneracy: Experiment 028 low-k matter-power angle `cs2` vs `cv2` = 0.3226 deg

## Question

Can an independent metric-potential channel break the near-degeneracy between GDM rest-frame sound speed and viscosity that remains in the low-k matter-power response?

## Source-level motivation

Pinned GDM_CLASS explicitly evolves or constructs GDM shear from `cv2_gdm`, and adds `(rho+p)*shear_gdm` to the total anisotropic stress entering the Einstein equations. Density-transfer output in CLASS format explicitly contains both `phi` and `psi` even when the integration gauge is synchronous, where the code reconstructs these potentials from synchronous metric variables.

This makes metric slip a physically distinct test channel rather than a relabeling of the matter-power response.

## Models

Use the same pinned GDM_CLASS commit, baseline, p8 precision and synchronous gauge as the validated C3 manifold.

Reference:

\[
w=c_s^2=c_v^2=0.
\]

Local one-axis controls:

\[
c_s^2=10^{-7},10^{-6},\qquad c_v^2=0,
\]

and

\[
c_v^2=10^{-7},10^{-6},\qquad c_s^2=0.
\]

Dynamic shear remains enabled for all runs, including the zero reference, so only the numerical value of `cv2` changes.

## Metric responses

From the `mTk` output reconstruct

\[
W=\Phi+\Psi,
\]

where the omitted factor 1/2 cancels in the same-solver ratio, and

\[
r_W(k,z)=\ln\left|\frac{W_{model}}{W_{ref}}\right|.
\]

Also define the dimensionless slip coordinate

\[
s(k,z)=\frac{\Phi-\Psi}{\Phi+\Psi},
\qquad
\Delta s=s_{model}-s_{ref}.
\]

The extractor requires the sign of `Phi+Psi` to remain unchanged relative to the reference on every retained cell; otherwise the log-Weyl response is invalid and the run must not silently take an absolute-value crossing as a smooth response.

## Geometry

For each channel independently estimate positive one-sided response tangents at `1e-7` and compare them with `1e-6` finite differences.

Report:

- `cs2` versus `cv2` angle in `r_W`;
- `cs2` versus `cv2` angle in `Delta slip`;
- convergence angle and relative L2 change from `1e-7` to `1e-6` for each axis;
- a combined metric angle after separately normalizing the Weyl and slip channel blocks, so arbitrary units do not decide which block dominates.

## Scientific rule

This first run is calibration only. No angular threshold for declaring the metric channel a proven separator is chosen in advance. If the calibration produces a stable large separation, a quantitative separator threshold must be frozen **before** a fresh hard rerun. Only then may this channel label the GDM `cs2`/`cv2` edge as broken in the discriminant graph.
