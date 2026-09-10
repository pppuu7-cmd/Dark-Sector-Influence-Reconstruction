# DSIR recovery V73 — Exp073JG validated; Exp073JH full-support feasibility active

Date: 2026-09-10. Scope: DSIR only; RTK/RQIR excluded.

Preserve all earlier authority. Repaired Exp073IR `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: retained 107, f_B=0, max production-vs-dense component discrepancy `0.9998247463807295 > 1e-3`; covariance restriction and Wm_S3 remain unauthorized. Exp073CM remains historical resource/performance +0/+0.

## Exp073JF validated
Repaired JF `34480349238 / 102881291672`, artifact `10153458465`, independently verified ZIP SHA256 `f71c1603f46e622a6c71ebab6733d30e9633cc92e9dc50a98cecdf364b28fffb`, is support-only `SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0`. N=384 and 512 have exact kpd10-vs20 equality but no exact-reference scaling candidate. Simple global linear ln(k) interpolation on the shared geomspace grid is inadequate through N=512 under unchanged REL_TOL=1e-3.

## Exp073JG terminal consumption
JG run/job `34485992147 / 102900288767`, head `a89dd256644b2c2f7827372e43c43bdb9c5f0adf`, completed successfully. Raw log was inspected and artifact `10155745915` downloaded. GitHub digest and independent ZIP SHA256 are exactly `e3282ea5f145a273aff63cd70ff74e23cbf6f19960bb83f8390c2c855ae70dbb`; result JSON SHA256 `3e9cd6c4395e4fc67fafd4805b8e1a0ade7e6f4239a1234be50910ff021869cf`; capacity patch SHA256 `f7d8d33232908f5f90f557ef42eeead4acc9dcc58a92f69629857aece2e1889b`.

Raw token `PASS_EXP073JG_LOCAL_INTERPOLATION_CURVATURE_OBSERVED_V0_1`; classification validated support-only `LOCAL_INTERPOLATION_CURVATURE_OBSERVED_PLUS_0_PLUS_0`.

At N=512, linear bracket exactly reproduces JF and remains noncandidate: alpha error `0.00010245604306152275`, beta `0.026575285704422986`. All three prospectively frozen higher-order rules are candidates under unchanged REL_TOL=1e-3 and exact kpd10-vs20 equality: quadratic-left errors `(alpha,beta)=(1.6655427759553507e-06,6.801424456717797e-05)`; quadratic-right `(2.7311728168928298e-06,0.0002303585618472267)`; centered cubic `(1.2105247820888992e-07,0.00016088505716613062)`. Thus local interpolation curvature is strongly implicated as the residual shared-grid linear-interpolation error at the historical worst probes. No Layer-B scientific authority is created.

Durable JG authority file creation commit: `da6f566b67872ac505c44181446b015ddffbed4c`.

## Exp073JH prospective full-support audit
Exp073JH label was collision-checked before use. Preregistration commit `57065961d9b49290ccdfd6f23f6e5290c4d7a292`; implementation commit `88d669ee567e85c5363d09db32fa2bcb9ceb08ab`; workflow/launch head `0834a45f5e767d411ce694d081069403ea6fd908`.

Architecture is prospectively selected centered cubic at N=512 because it is a balanced two-sided four-node stencil, not because it minimized the two-probe numerical error. It reuses the complete unchanged Exp073IR real-support reconstruction for all 107 retained Layer-A rows, all original atomization/operators, exact parent/radial/angular/BOSS authorities, h=1e-4, kpd10 production and kpd20 dense control, and unchanged REL_TOL=1e-3. Targets lacking a complete four-node shared-grid stencil propagate non-finite response and count against feasibility; clipping/extrapolation is forbidden. No covariance/whitening/nuisance/relation-null/held-out data may be read. All JH outcomes are +0/+0.

## Current authoritative process
Workflow `exp073jh-article3-layerb-full-support-grid-invariant-feasibility-v0-1`; run/job `34487047656 / 102903883547`; branch/head `main / 0834a45f5e767d411ce694d081069403ea6fd908`; checkpoint N/A; GitHub-hosted ubuntu-24.04; home/self-hosted ownership none. Last observed state IN_PROGRESS; prospective contract/JG authority step SUCCESS; frozen numerical/build-stack installation running.

Exact next action: terminal-consume JH, inspect first causal failure if any, otherwise independently verify raw artifact/hash/provenance and classify strictly as `FULL_SUPPORT_GRID_INVARIANT_FEASIBLE_PLUS_0_PLUS_0` or `FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_PLUS_0_PLUS_0`. Even FEASIBLE creates no scientific authority; it only permits a separately preregistered complete scientific Layer-B rerun. NOT_FEASIBLE requires boundary/grid mechanism work with no tolerance/density rescue.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; REL_TOL=1e-3; h=1e-4; exact-threshold ambiguity numerically_unresolved; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
