# Experiment 032 — GDM Weyl/slip discriminant for sound-speed vs viscosity

Date: 2026-08-24
Status: CALIBRATION PASS; HARD THRESHOLDS FROZEN; FRESH RERUN PENDING

Input degeneracy: Experiment 028 low-k matter-power angle `cs2` vs `cv2` = `0.322616 deg`.

## Question

Can an independent metric-potential channel break the near-degeneracy between GDM rest-frame sound speed and viscosity that remains in the low-k matter-power response?

## Source-level motivation

Pinned GDM_CLASS explicitly evolves/constructs GDM shear from `cv2_gdm`, and adds the GDM shear contribution to the total anisotropic stress entering the Einstein equations. Transfer output provides reconstructed `phi` and `psi`, allowing a metric response that is not a relabeling of the matter-power block.

## Models

Same pinned GDM_CLASS commit, common baseline, validated p8 precision and synchronous gauge as the C3 manifold.

Reference:

\[
w=c_s^2=c_v^2=0.
\]

Controls:

\[
c_s^2=10^{-7},10^{-6},\qquad c_v^2=0,
\]

and

\[
c_v^2=10^{-7},10^{-6},\qquad c_s^2=0.
\]

Dynamic shear is enabled in reference and all controls.

## Metric responses

Define

\[
W=\Phi+\Psi,
\qquad
r_W(k,z)=\ln\left|\frac{W_{model}}{W_{ref}}\right|,
\]

with an explicit sign-preservation requirement for `Phi+Psi` on all retained cells.

Define dimensionless slip

\[
s(k,z)=\frac{\Phi-\Psi}{\Phi+\Psi},
\qquad
\Delta s=s_{model}-s_{ref}.
\]

## Calibration result

The first run was intentionally threshold-free. It returned:

- `r_W` cs2/cv2 angle at `1e-7`: `0.300737 deg`;
- `r_W` cs2/cv2 angle at `1e-6`: `0.377256 deg`;
- `Delta slip` cs2/cv2 angle at `1e-7`: `137.943212 deg`;
- `Delta slip` cs2/cv2 angle at `1e-6`: `138.145199 deg`;
- equalized two-block angle at `1e-7`: `56.963212 deg`.

Tangent convergence from `1e-7` to `1e-6` remained below `0.4 deg`; all relative L2 changes were below `0.75%`.

Interpretation: Weyl-amplitude response remains almost degenerate, while slip strongly rotates the two positive physical rays. This is a candidate channel separator, not yet a hard result at the calibration stage.

## Frozen hard gate

The following thresholds are fixed **before** the fresh rerun and must not be changed in response to its outcome:

\[
\theta_{r_W}(c_s^2,c_v^2)\le1^\circ
\]

at both `1e-7` and `1e-6`;

\[
\theta_{\Delta s}(c_s^2,c_v^2)\ge120^\circ
\]

at both steps;

\[
\theta_{combined}\ge45^\circ;
\]

for every axis/channel tangent-convergence angle,

\[
\Delta\theta_{10^{-7}\to10^{-6}}\le1^\circ;
\]

and every relative L2 tangent change must satisfy

\[
\Delta_{L2}\le0.02.
\]

The machine checker is `ci/gdm_weyl_slip_hard_gate.py`.

## Scientific rule

A PASS means only that the calibrated `cs2`/`cv2` low-k degeneracy has a reproducible metric-slip separator in the pinned C3 setup. It is not an observational evidence ratio and is not a discovery claim. Observational sensitivity/covariance must still be applied before saying that real data can distinguish the mechanisms.
