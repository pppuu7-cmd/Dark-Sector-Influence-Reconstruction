# DSIR recovery V72 — Exp073JF validated; Exp073JG curvature diagnostic active

Date: 2026-09-10. Scope: DSIR only. Never mix RTK or RQIR.

All earlier admitted DSIR authority and frozen boundaries remain unchanged. Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: retained 107, f_B=0, exact production-vs-dense maximum 0.9998247463807295 > REL_TOL=1e-3. Covariance restriction and Wm_S3 remain unauthorized. Exp073CM remains historical resource/performance +0/+0.

## Exp073JF terminal consumption
Repaired Exp073JF run/job `34480349238 / 102881291672`, head `2e5e43de2abaec3be93f5fe1a2fbe909b6e86048`, completed SUCCESS and was consumed from raw job log plus downloaded artifact rather than workflow conclusion alone.

Artifact `10153458465`, name `exp073jf-shared-fixed-k-extended-density-v0-1`, GitHub digest and independently computed ZIP SHA256 are exactly `f71c1603f46e622a6c71ebab6733d30e9633cc92e9dc50a98cecdf364b28fffb`. Extracted result JSON SHA256 is `a18d46f6a6e62c3009df92344c97f8f41d8f61ebad172e18b0e519704398a3e6`; capacity-patch JSON SHA256 is `f7d8d33232908f5f90f557ef42eeead4acc9dcc58a92f69629857aece2e1889b`.

Raw token: `PASS_EXP073JF_SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_V0_1`. Classification: validated support-only `SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0`.

At N=384, alpha exact-reference relative error is 0.0007790941263871595 and beta is 0.031479742832626514. At N=512, alpha is 0.00010245604306152275 and beta is 0.026575285704422986. For both N and both probes, kpd10-vs-kpd20 relative difference is exactly 0.0. `scaling_candidates=[]`; no Layer-B scientific authority or covariance authorization is created.

Therefore the preregistered conclusion applies: simple global geomspace density through current exact capacity is numerically inadequate for the frozen worst probes. Further brute-force density extrapolation is not authorized from JF alone.

Durable JF authority file creation commit: `ad335d5117125ff57354311eb491e1db8d163972`.

## Prospectively frozen Exp073JG
Next experiment label was collision-checked before use. Exp073JG preregistration commit `3277273682e9fac01253160d089f987e09fa424e`; implementation commit `73d437963b8808e50ff80c67c75d7f06dcbab7e7`; workflow/launch head `a89dd256644b2c2f7827372e43c43bdb9c5f0adf`.

Purpose: isolate local interpolation curvature at N=512, holding exact pinned CLASS-IV, shared physical-k grid, h=1e-4, kpd={10,20}, target probes, physics and REL_TOL=1e-3 fixed. Frozen counterfactual rules are linear bracket, left/right local quadratic, and centered cubic interpolation in ln(k). Linear output must exactly reproduce the validated JF N=512 parent response; otherwise the diagnostic is infrastructure-invalid. All outcomes are +0/+0.

## Current authoritative process
Workflow `exp073jg-article3-layerb-local-interpolation-curvature-v0-1`; run/job `34485992147 / 102900288767`; branch/head `main / a89dd256644b2c2f7827372e43c43bdb9c5f0adf`; checkpoint N/A; GitHub-hosted ubuntu-24.04; home/self-hosted ownership none. Last observed state IN_PROGRESS. Contract/JF authority step succeeded; frozen stack/static audit was running.

Exact next action: terminal-consume `34485992147`, inspect raw job log and independently verify artifact ZIP/result hashes. If a higher-order rule satisfies the unchanged exact-reference and kpd criteria for both probes, nominate only a separate prospectively frozen full-support feasibility audit; do not authorize Layer-B from JG. If no rule qualifies or higher-order rules disagree/oscillate, continue mechanism isolation without density or tolerance rescue.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; REL_TOL=1e-3; h=1e-4; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
