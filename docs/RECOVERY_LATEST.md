# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JF_VALIDATED_JG_CURVATURE_RUNNING_V72.md`, creation commit `c9a8afa93abecfee282d1163cb4ee0b8e749436a`. Earlier notes remain immutable history.

## Preserved authority
All prior admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107 coordinate rows, atomic production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. Exp073CM remains historical resource/performance `+0/+0`; Wm_S3 remains unopened.

## Exp073JF validated support result
Repaired Exp073JF run/job `34480349238 / 102881291672`, head `2e5e43de2abaec3be93f5fe1a2fbe909b6e86048`, is validated support-only `SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0`. Artifact `10153458465`; GitHub digest and independently computed ZIP SHA256 both `f71c1603f46e622a6c71ebab6733d30e9633cc92e9dc50a98cecdf364b28fffb`; result JSON SHA256 `a18d46f6a6e62c3009df92344c97f8f41d8f61ebad172e18b0e519704398a3e6`. N=384 errors: alpha `0.0007790941263871595`, beta `0.031479742832626514`; N=512: alpha `0.00010245604306152275`, beta `0.026575285704422986`; kpd10-vs-kpd20 discrepancy is exactly 0.0 for both probes at both N. `scaling_candidates=[]`. Durable JF authority creation commit `ad335d5117125ff57354311eb491e1db8d163972`.

Prospective consequence only: simple global geomspace density through current exact N=512 capacity is numerically inadequate for the frozen worst probes. No Layer-B/covariance/Wm_S3 authority is created.

## Current process — Exp073JG
Exp073JG local-interpolation-curvature diagnostic was collision-checked and prospectively frozen before numerical output. Preregistration commit `3277273682e9fac01253160d089f987e09fa424e`; implementation commit `73d437963b8808e50ff80c67c75d7f06dcbab7e7`; workflow/launch head `a89dd256644b2c2f7827372e43c43bdb9c5f0adf`.

Authoritative workflow/run/job: `exp073jg-article3-layerb-local-interpolation-curvature-v0-1 / 34485992147 / 102900288767`; branch/head `main / a89dd256644b2c2f7827372e43c43bdb9c5f0adf`; GitHub-hosted `ubuntu-24.04`; checkpoint N/A; home/self-hosted ownership none. Last observed state IN_PROGRESS. Contract/JF authority step succeeded; frozen stack/static audit was running.

Exp073JG holds N=512, h=1e-4, kpd={10,20}, physical-k domain, exact references and REL_TOL=1e-3 fixed while comparing prospectively frozen local ln(k) interpolation stencils: linear bracket, left/right quadratic and centered cubic. Linear must exactly reproduce JF N=512 or the run is infrastructure-invalid. All JG outcomes are support-only +0/+0.

Exact next action: terminal-consume `34485992147`, verify raw log/artifact/hash/provenance and classify strictly under frozen JG. If a higher-order rule qualifies for both probes and both kpd values, only nominate a separate prospectively frozen full-support feasibility audit. If none qualifies or the higher-order rules disagree/oscillate, continue mechanism isolation. Never rescue by changing `REL_TOL=1e-3`.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
