# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JG_VALIDATED_JH_FULL_SUPPORT_RUNNING_V73.md`, creation commit `b75e430e1194ff5d8b16a7b29b55879a4bc15db0`. Earlier notes remain immutable history.

## Preserved authority
All prior admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107 coordinate rows, atomic production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. Exp073CM remains historical resource/performance `+0/+0`; Wm_S3 remains unopened.

## Exp073JF and Exp073JG validated support results
Exp073JF repaired run/job `34480349238 / 102881291672` is validated `SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0`; artifact `10153458465`, independently verified ZIP SHA256 `f71c1603f46e622a6c71ebab6733d30e9633cc92e9dc50a98cecdf364b28fffb`. N=384/512 preserve exact kpd10-vs20 equality but no global-linear exact-reference candidate exists.

Exp073JG run/job `34485992147 / 102900288767`, head `a89dd256644b2c2f7827372e43c43bdb9c5f0adf`, is validated support-only `LOCAL_INTERPOLATION_CURVATURE_OBSERVED_PLUS_0_PLUS_0`. Artifact `10155745915`; independently verified ZIP SHA256 `e3282ea5f145a273aff63cd70ff74e23cbf6f19960bb83f8390c2c855ae70dbb`; result JSON SHA256 `3e9cd6c4395e4fc67fafd4805b8e1a0ade7e6f4239a1234be50910ff021869cf`. At N=512, linear beta error remains `0.026575285704422986`, whereas quadratic-left/right and centered-cubic beta errors are `6.801424456717797e-05`, `0.0002303585618472267`, and `0.00016088505716613062`; all three higher-order rules meet unchanged REL_TOL=1e-3 at both historical probes and have exact kpd10-vs20 equality. Durable JG authority creation commit `da6f566b67872ac505c44181446b015ddffbed4c`.

This establishes local interpolation curvature as the leading diagnosed residual mechanism at the frozen worst probes but creates no Layer-B/covariance/Wm_S3 authority.

## Current process — Exp073JH
Exp073JH full-support grid-invariant feasibility audit was collision-checked and prospectively frozen before numerical output. Preregistration commit `57065961d9b49290ccdfd6f23f6e5290c4d7a292`; implementation commit `88d669ee567e85c5363d09db32fa2bcb9ceb08ab`; workflow/launch head `0834a45f5e767d411ce694d081069403ea6fd908`.

Authoritative workflow/run/job: `exp073jh-article3-layerb-full-support-grid-invariant-feasibility-v0-1 / 34487047656 / 102903883547`; branch/head `main / 0834a45f5e767d411ce694d081069403ea6fd908`; GitHub-hosted `ubuntu-24.04`; checkpoint N/A; home/self-hosted ownership none. Last observed state IN_PROGRESS. Prospective contract/JG authority enforcement succeeded; frozen numerical/build stack was installing.

JH uses prospectively selected N=512 centered cubic because its stencil is structurally balanced, not because it numerically minimized JG probe error. It reuses the complete unchanged Exp073IR real-support reconstruction across the exact 107 retained Layer-A rows, same atomization/operators/authorities, h=1e-4, kpd10/20, z/k domain and REL_TOL=1e-3. Targets lacking a complete cubic stencil propagate non-finite support and cannot be clipped or extrapolated. All outcomes remain +0/+0; covariance/whitening/nuisance/relation-null/held-out reads are forbidden.

Exact next action: terminal-consume `34487047656`, inspect first causal failure if any, otherwise independently verify raw artifact/hash/provenance and classify strictly as `FULL_SUPPORT_GRID_INVARIANT_FEASIBLE_PLUS_0_PLUS_0` or `FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_PLUS_0_PLUS_0`. Even FEASIBLE only permits a separately preregistered complete scientific Layer-B rerun; it does not itself create scientific authority.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
