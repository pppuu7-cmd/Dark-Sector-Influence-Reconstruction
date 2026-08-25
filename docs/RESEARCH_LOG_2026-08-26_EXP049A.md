# DSIR research log — 2026-08-26 — Experiment 049A

## Goal

Bridge the Exp048B interaction-localization flow to characteristic scales derived from the exact pinned C3/C5 solver equations, without fitting a post-hoc response scale.

## Source audit completed before CI

### C3 GDM

Pinned source: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Frozen C3 uses `w=0`, `Omega_k=0`, and dynamic shear for the viscosity ray. The exact source contains the Euler `-k^2 sigma` term and dynamic shear equation `sigma'=-3 Hconf sigma +(8/3) cv2(theta+metric_shear)`.

This fixes two diagnostic crossings:

- pressure: `k_s = Hconf/sqrt(cs2)`;
- viscosity quasi-steady: `k_v_QS = sqrt(9/8) Hconf/sqrt(cv2)`.

Using the immutable run-32759738560 CLASS background locally, before the formal CI run:

| ray | amplitude | source-derived scale at Exp048B z-centroid [h/Mpc] | relation to k<=0.1 window |
|---|---:|---:|---|
| GDM cs2 | 1e-8 | 3.06268 | outside |
| GDM cs2 | 1e-7 | 0.96850 | outside |
| GDM cs2 | 1e-6 | 0.30625 | outside |
| GDM cv2 | 1e-8 | 3.25407 | outside |
| GDM cv2 | 1e-7 | 1.02904 | outside |
| GDM cv2 | 1e-6 | 0.32546 | outside |
| GDM cv2 | 1e-5 | 0.10311 | reaches upper edge |
| GDM cv2 | 1e-4 | 0.03316 | inside |

At `cv2=1e-4`, Exp048B measured `k_I_geo=0.040627 h/Mpc`, while the source-derived quasi-steady scale is `0.033156 h/Mpc`. This proximity is descriptive only; no alignment threshold is introduced after seeing it.

### C5 designer-f(R)

Pinned source: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

The source stores `Omega_EFT=f_R` and computes the designer `B` parameter in a form algebraically equal to

`B = f_R'/(1+f_R) * H/H' = f_RR R'/(1+f_R) * H/H'`.

This yields a source-native inverse Compton scale and, with the curvature correction, the scalaron mass scale. A diagnostic-only writer is used because the normal EFTCAMB background table does not emit `B(a)`.

## Methodological boundary

The first formal Exp049A CI run may hard-fail only source/provenance/algebra controls. Whether the characteristic transition lies near `k_I_geo` is not a hard gate in this experiment because Exp048B localization had already been inspected.

## Next

Run the instrumented frozen C5 production manifold, compare exact `B(a)` characteristic scales to Exp048B, then record either support or falsification as a separate finding. No G7/G8 or universal-model claim is permitted from this experiment alone.
