# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JF_VALIDATED_JG_CURVATURE_RUNNING_V72.md`, creation commit `c9a8afa93abecfee282d1163cb4ee0b8e749436a`.

## Newly closed
- Repaired Exp073IR `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`; exact convergence maximum `0.9998247463807295 > 1e-3`; 0 invalid rows, f_B=0, retained 107; covariance unauthorized.
- Exp073JF repaired run `34480349238 / 102881291672` is validated support-only `SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0`; artifact `10153458465`; independently verified ZIP SHA256 `f71c1603f46e622a6c71ebab6733d30e9633cc92e9dc50a98cecdf364b28fffb`; result JSON SHA256 `a18d46f6a6e62c3009df92344c97f8f41d8f61ebad172e18b0e519704398a3e6`; durable authority creation commit `ad335d5117125ff57354311eb491e1db8d163972`.
- JF has no scaling candidate. N=384 errors `(alpha,beta)=(0.0007790941263871595,0.031479742832626514)` and N=512 `(0.00010245604306152275,0.026575285704422986)`; kpd10-vs-kpd20 discrepancy is exactly zero for both probes. Simple global geomspace density through N=512 is therefore inadequate under the unchanged frozen criterion.

## Current authoritative process — Exp073JG
- workflow: `exp073jg-article3-layerb-local-interpolation-curvature-v0-1`;
- run ID: `34485992147`;
- job ID: `102900288767`;
- branch/head: `main / a89dd256644b2c2f7827372e43c43bdb9c5f0adf`;
- preregistration commit: `3277273682e9fac01253160d089f987e09fa424e`;
- implementation commit: `73d437963b8808e50ff80c67c75d7f06dcbab7e7`;
- workflow/launch commit: `a89dd256644b2c2f7827372e43c43bdb9c5f0adf`;
- checkpoint namespace / last durable checkpoint: N/A (GitHub-hosted support diagnostic);
- start/registration: `2026-09-10T13:58:15Z`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- current state: IN_PROGRESS at last inspection;
- last completed gate: prospective contract/JF-authority enforcement SUCCESS;
- current step at last inspection: frozen stack/static audit;
- expected support classifications: `LOCAL_INTERPOLATION_CURVATURE_OBSERVED_PLUS_0_PLUS_0` or `INVALID_INFRA_PLUS_0_PLUS_0`;
- frozen diagnostic: N=512 shared physical-k grid; same two historical probes; exact kpd={10,20}; h=1e-4; unchanged REL_TOL=1e-3; local ln(k) rules linear bracket, left/right quadratic and centered cubic;
- scientific effect: always +0/+0; no Layer-B/covariance/model/Wm_S3 authority.

### Exact next transitions
Terminal valid observation: independently verify raw log and artifact ZIP/result hashes. Linear interpolation must exactly reproduce validated JF N=512. If one or more higher-order rules satisfy the frozen exact-reference and kpd criteria for both probes, only nominate a separate prospectively frozen full-support grid-invariant feasibility audit; do not promote JG itself. If no rule qualifies or the higher-order rules disagree/oscillate, continue mechanism isolation.

Infrastructure invalid: diagnose the first causal defect and repair only the support diagnostic. Never alter Exp073IR science, REL_TOL=1e-3, h=1e-4, k/z domains, source definitions, atomization or covariance firewall.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective ell/z/k/fiducial-P shortcut.
