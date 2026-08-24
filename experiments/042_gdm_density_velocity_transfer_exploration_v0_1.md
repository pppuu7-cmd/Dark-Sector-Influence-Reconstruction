# Experiment 042 — GDM density/velocity transfer exploration v0.1

**Date:** 2026-08-25  
**Status:** exploratory protocol; no scientific separation threshold  
**Scope:** frozen C3 `w_gdm=0` cs2/cv2 manifold

## Purpose

The frozen C3 manifold has three established facts:

1. `cs2` and `cv2` are nearly collinear in low-k matter-power response (`~0.3226 deg`);
2. they are exactly background/AP-null in Experiment 037;
3. metric slip strongly separates them.

Experiment 042 asks whether the velocity sector contains additional mechanism information between the almost-degenerate density block and the strongly separating metric-slip block.

This is intentionally exploratory. It freezes only provenance and definitions, not a pairwise-angle or representability threshold. Any interesting numerical separation found here must be confirmed by a later threshold-frozen hard experiment.

## Immutable provenance

Pinned upstream:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Exact frozen C3 manifold artifact:

- source run `32759738560`;
- artifact ID `9532247349`;
- artifact name `gdm-cv2-manifold-15c7128d4220b954783a8ba7cce7c06744f7f0ac`;
- digest `sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d`.

The new workflow reuses the exact INIs and precision file `dsir_p8.pre`. It changes only the requested output from `mPk` to `mPk,mTk,vTk` and redirects the output root to a new directory. No cosmological or GDM parameter is changed.

## Why the pinned solver is sufficient

The pinned GDM_CLASS source explicitly supports velocity-transfer output. In CLASS-format transfer files:

- `d_gdm` is the GDM density transfer;
- `t_gdm` is the GDM velocity-divergence transfer;
- `d_b`, `t_b` are the baryon counterparts;
- `t_tot` is the enthalpy-weighted total velocity transfer.

The frozen C3 models use

`omega_cdm=0`, `omega_gdm=0.1200`, `omega_b=0.0224`, `w_gdm=0`, `N_ncdm=0`.

Hence the DSIR matter fields can be reconstructed directly from baryons+GDM:

\[
\delta_m(k,z)=\frac{\rho_b\delta_b+\rho_{gdm}\delta_{gdm}}{\rho_b+\rho_{gdm}},
\]

\[
\theta_m(k,z)=\frac{\rho_b\theta_b+\rho_{gdm}\theta_{gdm}}{\rho_b+\rho_{gdm}}.
\]

Because both components have `w=0` in the frozen background, the relative weights are constant and equal to their present physical densities.

The comoving matter contrast is then

\[
\boxed{\Delta_m=\delta_m+3{\cal H}\frac{\theta_m}{k^2}}.
\]

This preserves the already frozen DSIR gauge-safe density convention.

For a scalar RSD representability diagnostic, a dimensionless velocity amplitude may be defined as

\[
\Theta_m=-\frac{\theta_m}{\mathcal H}.
\]

The representability defect

\[
{\cal D}_{RSD}=1-\frac{S_{\Delta\Theta}^2}{S_{\Delta\Delta}S_{\Theta\Theta}}
\]

is invariant under any k-independent rescaling or sign convention of `Theta`, so the exploration is insensitive to an overall velocity normalization.

## Frozen models

Reference:

- `gdm0`.

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

All use the frozen seven redshifts

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`

and `P_k_max_h/Mpc=0.25`.

## Exploratory outputs to inspect

1. reconstructed `Delta_m(k,z)` and `Theta_m(k,z)`;
2. density/velocity ratio `Theta_m/Delta_m`;
3. `D_RSD` histories for cs2 and cv2 controls;
4. pairwise angles between pressure and viscosity in:
   - density response;
   - velocity response;
   - density+velocity joint response;
5. comparison with the already hard low-k density angle `0.322616 deg` and slip separation.

No angle or `D_RSD` value in this experiment is a hard scientific claim until an independent confirmatory protocol freezes thresholds before the target output.

## Interpretation targets

Interesting possibilities are deliberately left open:

- velocity remains nearly collinear with density: RSD adds little for cs2/cv2 and slip remains indispensable;
- velocity significantly separates cs2/cv2: an intermediate dynamical separator exists before metric slip;
- one direction fails scalar RSD representability more strongly than the other: compressed growth can itself erase microphysical information.

Any of these outcomes is scientifically useful.
