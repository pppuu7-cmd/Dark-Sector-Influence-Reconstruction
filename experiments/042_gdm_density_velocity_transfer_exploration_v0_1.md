# Experiment 042 — GDM density/velocity transfer exploration v0.2

**Date:** 2026-08-25  
**Status:** gauge-bridge threshold frozen; Newtonian target output pending; scientific velocity separation remains exploratory  
**Scope:** frozen C3 `w_gdm=0` cs2/cv2 manifold

## Purpose

The frozen C3 manifold has three established facts:

1. `cs2` and `cv2` are nearly collinear in low-k matter-power response (`~0.3226 deg`);
2. they are exactly background/AP-null in Experiment 037;
3. metric slip strongly separates them.

Experiment 042 asks whether the velocity sector contains additional mechanism information between the almost-degenerate density block and the strongly separating metric-slip block.

Pairwise velocity angles and `D_RSD` remain deliberately exploratory. The only hard threshold introduced in v0.2 is a **gauge bridge** that must pass before Newtonian velocities may be interpreted.

## Immutable provenance

Pinned upstream:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Exact frozen C3 manifold artifact:

- source run `32759738560`;
- artifact ID `9532247349`;
- artifact name `gdm-cv2-manifold-15c7128d4220b954783a8ba7cce7c06744f7f0ac`;
- digest `sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d`.

The workflow reuses the exact INIs and precision file `dsir_p8.pre`. The synchronous diagnostic changes only requested outputs from `mPk` to `mPk,mTk,vTk` and redirects the output root. The Newtonian bridge additionally changes only

`gauge = synchronous -> gauge = newtonian`.

No cosmological or GDM microphysical parameter changes.

## Matter-field reconstruction

The pinned GDM_CLASS source provides `d_b,d_gdm,t_b,t_gdm`. The frozen C3 models use

`omega_cdm=0`, `omega_gdm=0.1200`, `omega_b=0.0224`, `w_gdm=0`, `N_ncdm=0`.

Thus

\[
\delta_m=\frac{\rho_b\delta_b+\rho_{gdm}\delta_{gdm}}{\rho_b+\rho_{gdm}},
\qquad
\theta_m=\frac{\rho_b\theta_b+\rho_{gdm}\theta_{gdm}}{\rho_b+\rho_{gdm}},
\]

with constant weights on the frozen `w=0` background, and

\[
\boxed{\Delta_m=\delta_m+3{\cal H}\frac{\theta_m}{k^2}}.
\]

For the velocity leg define

\[
\Theta_m=-\frac{\theta_m}{\mathcal H}.
\]

An overall k-independent sign/normalization of `Theta` does not affect the representability defect.

## Chronology: why synchronous theta is rejected for RSD

The first successful exploratory transfer run used the exact frozen synchronous-gauge configurations. It reproduced the expected density behavior, but the reference dark-matter velocity is almost gauge-fixed away in synchronous gauge. Consequently ratios such as `Theta_model/Theta_ref` become enormous and ill-conditioned even when the physical perturbation response is small.

**This synchronous velocity result is a gauge artifact for the RSD purpose and is not interpreted scientifically.** It is retained as a negative methodological finding.

## Chronology: pinned N-body transfer route is incomplete upstream

The pinned CLASS branch exposes `Nbody gauge transfer functions = yes` and contains explicit N-body density/velocity gauge corrections. A direct output-only N-body attempt was therefore made.

The solver stopped before target output with its own source-level error:

> `We need to compute the derivative of H_T_Nb_prime numerically. Written by T. Tram but not yet propagated here.`

This is an upstream capability limitation in the pinned GDM_CLASS branch, not a C3 scientific failure. DSIR will not patch the missing N-body evolution/output physics merely to force a result.

## v0.2 solution: independent synchronous/Newtonian gauge bridge

The same frozen physical models are now run once in synchronous gauge and once in Newtonian gauge. The reconstructed comoving matter field must agree:

\[
\Delta_m^{(S)}(k,z)=\Delta_m^{(N)}(k,z).
\]

The check is performed at the frozen DSIR nodes

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`

and

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

### Gauge-bridge thresholds frozen before the first Newtonian target output

- maximum transfer-k-grid mismatch `<=1e-12`;
- maximum absolute `ln|Delta_S/Delta_N|` at the frozen nodes `<=1e-6`;
- maximum absolute difference between model/reference `Delta` log responses in the two gauges `<=1e-6`.

If this bridge fails, Newtonian velocity angles and `D_RSD` are not interpreted. These thresholds were fixed after the synchronous diagnostic and failed built-in N-body attempt, but **before any Newtonian target output was inspected**.

## Frozen models

Reference: `gdm0`.

Pressure direction:

- `gdmcs2_1em8`;
- `gdmcs2_1em7`;
- `gdmcs2_1em6`.

Viscosity direction:

- `gdmcv2_1em8`;
- `gdmcv2_1em7`;
- `gdmcv2_1em6`;
- `gdmcv2_1em5`;
- `gdmcv2_1em4`.

All retain the frozen seven redshifts and `P_k_max_h/Mpc=0.25`.

## Exploratory velocity/RSD outputs after bridge PASS

For the Newtonian run inspect:

1. reconstructed `Delta_m(k,z)` and `Theta_m(k,z)`;
2. `g(k,z)=Theta_m/Delta_m`;
3. `D_RSD` for `kmax=0.10` and `0.24 h/Mpc`;
4. cs2/cv2 `1e-6` acute angles in:
   - `Delta` response;
   - `Theta` response;
   - an equalized `Delta+Theta` two-block response.

The scalar-compression diagnostic is

\[
{\cal D}_{RSD}=1-\frac{S_{\Delta\Theta}^2}{S_{\Delta\Delta}S_{\Theta\Theta}},
\]

with the same top-hat `R=8 h^-1 Mpc` in this background-null C3 closure manifold.

**No pairwise-angle or nonzero-`D_RSD` scientific threshold is frozen in Experiment 042.** If an interesting velocity separator or compression defect appears, it must be reproduced by a later independent confirmatory experiment whose scientific threshold is fixed before the new target output.

## Interpretation targets

Possible outcomes remain open:

- Newtonian velocity remains nearly collinear between `cs2/cv2`: RSD adds little and slip remains indispensable;
- Newtonian velocity substantially separates them: a dynamical separator exists before metric slip;
- pressure and viscosity show different scalar-compression defects: a one-number growth compression erases additional microphysical information.

Any outcome is useful, provided the gauge bridge passes first.
