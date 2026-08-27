# Exp073J — BOSS finite-matrix component pre-output binding v0.1

**Date frozen:** 2026-08-27  
**Status:** FROZEN BEFORE ANY BOSS COMPONENT SUPPORT FRACTION IS EVALUATED

## Purpose

This document fixes the remaining BOSS finite-matrix semantics inside the already-preregistered Exp073J common KiDS-BNT+BOSS support audit. It does **not** alter the Exp073J 5% acceptance threshold, minimum retained dimension, common provider rectangle, or final classification rule. It is a non-classifying component audit; only the full Exp073J result can authorize covariance restriction/whitening.

## Immutable parent rules

Preserve:

- Exp073I classification `PASS_FINITE_TRUE_K_WINDOW_MATRIX_SOURCE_BINDING_EXP073I`;
- common provider rectangle `0.295 <= z <= 2.33` and `0.000704833374744468 <= k_phys <= 0.06664762008318016 Mpc^-1`;
- maximum positive invalid support fraction `0.05`;
- G7/G8/G9 remain OPEN;
- no covariance, nuisance SVD, relation/null, held-out or G8 information may be read.

## Public matrix source and composition

Use the exact Beutler & McDonald BOSS DR12 z3 products already bound by Exp073I:

- `W_BOSS_DR12_NGC_z3_V6C_1_1_1_1_1_10_200_2000_averaged_v1.matrix.gz`;
- `W_BOSS_DR12_SGC_z3_V6C_1_1_1_1_1_10_200_2000_averaged_v1.matrix.gz`;
- `M_BOSS_DR12_NGC_z3_V6C_1_1_1_1_1_1200_2000.matrix.gz`;
- `M_BOSS_DR12_SGC_z3_V6C_1_1_1_1_1_1200_2000.matrix.gz`;
- semantics pinned to `fbeutler/pk_tools@707eb2a6a4691c34eae19d7f72047ca4892f528e`.

The pinned `wide_angle_tools.py` contract defines `M` as a `5*Nk x 3*Nk` map from input `(P0,P2,P4)` to `(P0,P1,P2,P3,P4)`, with `Nk=400`. The released matrices therefore compose as

`C = W @ M`,

where `W` is `200 x 2000`, `M` is `2000 x 1200`, and `C` is `200 x 1200`.

The true-theory k grid is frozen exactly as the pinned matrix generator: 400 midpoint bins on `0 <= k_h < 0.4 h/Mpc`,

`k_h[i] = 0.0005 + 0.001*i h/Mpc`, `i=0,...,399`.

The 1200 input columns are three consecutive copies of this grid for `(P0,P2,P4)`.

## Physical-unit conversion

Freeze the BOSS DR12 fiducial coordinate conversion at `h_fid = 0.676`. Convert every true-theory support coordinate by

`k_phys = h_fid * k_h`.

No AP remapping, fitted cosmology, or posterior-dependent h is permitted in this support audit.

The BOSS z3 sample is the already-bound high-z sample `0.5<z<0.75`; its radial selection lies inside the frozen `0.295<=z<=2.33` interval, so this component tests k-support only. No effective-z approximation is being used to rescue radial leakage; the sample selection itself was frozen before support output.

## Output-row selection

Use only the observed even multipole blocks corresponding to `ell = 0,2,4`, preserving all 40 released observed-k rows per multipole and both NGC and SGC caps. In the 200-row `(P0,P1,P2,P3,P4)` ordering these are rows:

- `0:40` for P0;
- `80:120` for P2;
- `160:200` for P4.

This gives 120 BOSS component coordinates per cap, 240 total before the support mask. Odd multipoles generated internally by wide-angle mixing remain inside `C` through `M`; they are not separately treated as observed coordinates.

## Positive support envelope

For every selected row r use the preregistered full-composed positive envelope

`w_r(j) = abs(C[r,j])`.

Define invalid true-theory columns solely by the unchanged common physical-k interval. The BOSS component invalid fraction is

`f_invalid(r) = sum_{j invalid} w_r(j) / sum_j w_r(j)`.

A row is component-retained iff `f_invalid <= 0.05`. No cancellation in signed matrix entries is allowed to reduce invalid support. No `P(k)` weighting, covariance weighting, nuisance weighting, clipping, row renormalization by selected support, or post-hoc k cutoff is allowed.

## Controls

The evaluator must verify exact matrix dimensions, finite values, finite positive `abs(C)` row sums, deterministic repeatability, identical k-column ordering across the three input multipoles, and explicit `h_fid=0.676` conversion. It must emit per-cap/per-multipole invalid-fraction summaries and the 240-row component mask.

This component output is descriptive and non-classifying for Exp073J. It may identify whether BOSS itself is compatible with the common support rectangle, but it cannot authorize covariance and cannot compensate for a failing KiDS-BNT block.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
