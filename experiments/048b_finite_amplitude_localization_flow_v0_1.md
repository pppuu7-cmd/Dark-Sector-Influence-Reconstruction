# Experiment 048B — finite-amplitude interaction-localization flow v0.1

**Date:** 2026-08-26  
**Status:** protocol frozen before first workflow target output  
**Parent:** Exp047A and Exp048A.

## Question

Exp047A showed that `chi_I` decreases at large GDM-viscosity and designer-f(R) amplitude while their one-parameter response trajectories bend. Exp048A localized the interaction energy through `q_k` and `q_z`.

This experiment asks:

> Does finite-amplitude bending coincide with a systematic migration of interaction-energy localization through the fixed `(k,z)` window?

The aim is to test the hypothesis that `chi_I` is partly a **window-localized transition descriptor** rather than a monotonic proxy for microscopic coupling strength.

## Inputs

Use the same immutable solver products as Exp047A:

- C1 smooth-w run `32771133024`;
- C3 GDM run `32759738560`;
- C5 designer-f(R) run `32759477319`.

IDE is not used for normalized localization flow because its `chi_I` remains below the pre-existing `1e-6` morphology floor across Exp047A. C4 is excluded by domain contract.

## Definitions

For each finite response, recompute

\[
R=\mu+T+\tau+I,
\qquad
\chi_I=\frac{\|I\|^2}{\|R\|^2},
\]

and

\[
q_k=\frac{\sum_z I^2}{\|I\|^2},\qquad q_z=\frac{\sum_k I^2}{\|I\|^2}.
\]

Report

\[
k_I^{geo}=\exp\left(\sum_kq_k\ln k\right),\qquad z_I=\sum_zq_zz,
\]

plus `q_k`/`q_z` turning angles relative to the smallest valid amplitude on each branch and the peak-energy cell.

For descriptive trend bookkeeping only, also report Pearson coefficients between:

- `log10(amplitude)` and `log10(k_I^geo)`;
- `log10(amplitude)` and `z_I`;
- `chi_I` and `log10(k_I^geo)`;
- `chi_I` and `z_I`.

With only 3-5 points these coefficients are **not statistical significance tests**.

## Hard controls

Only operator/algebraic controls can fail:

1. decomposition reconstruction `<=1e-12`;
2. core/I orthogonality `<=1e-12`;
3. zero-mean component residual `<=1e-12`;
4. localization-profile normalization residual `<=1e-12`;
5. finite nonnegative profiles for all morphology-valid points.

## Scientific-threshold discipline

The finite-amplitude centroid motion was inspected while designing this protocol. Therefore no monotonicity, minimum shift or correlation threshold is allowed as a scientific PASS gate now. The workflow will establish reproducible descriptive trajectories only.

## Interpretation boundary

A moving centroid on this sparse finite grid does not by itself prove a physical Compton/free-streaming/sound-horizon transition scale. The correct claim, if seen, is that the **response localization migrates within the chosen DSIR window**. A physical transition-scale interpretation requires solver-level/domain follow-up.

No survey detectability, intrinsic rank, universal law, G7 or G8 claim follows.
