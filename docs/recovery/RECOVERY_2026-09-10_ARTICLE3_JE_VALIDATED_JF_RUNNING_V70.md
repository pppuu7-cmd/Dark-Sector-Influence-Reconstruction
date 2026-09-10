# DSIR recovery V70 — Exp073JE validated; Exp073JF extended-density diagnostic active

Date: 2026-09-10. Scope: DSIR only. Never mix RTK or RQIR.

All earlier admitted DSIR scientific authority and frozen boundaries remain unchanged. Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 107 retained rows, f_B=0, production-vs-dense maximum 0.9998247463807295 > REL_TOL=1e-3; covariance restriction and Wm_S3 remain unauthorized. Exp073CM remains historical resource/performance +0/+0.

## Exp073JE terminal consumption
Authoritative repaired JE run/job `34474978911 / 102863474356`, head `3f74511a78724ac11e64d98284321df12cc7d1a8`, completed SUCCESS. Scientific classification was determined from raw output/artifact, not workflow status: `SHARED_FIXED_K_GRID_SCALING_OBSERVED_PLUS_0_PLUS_0`, token `PASS_EXP073JE_SHARED_FIXED_K_GRID_SCALING_OBSERVED_V0_1`.

Artifact `10151168583` was independently downloaded. GitHub and local ZIP SHA256 both equal `cf2e70a8bb35dcdb782d49fe5a29b908f6897169d6fe2c055c9b92eb1bfa01af`; result JSON SHA256 `c55e71faa6a8a43a61f6910908bb161deb2075d5212b5851d1551a078fbd5a33`; capacity-patch JSON SHA256 `f7d8d33232908f5f90f557ef42eeead4acc9dcc58a92f69629857aece2e1889b`.

Capacity provenance is valid: pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`; `_MAX_NUMBER_OF_K_FILES_ 30->512`; parser `_ARGUMENT_LENGTH_MAX_ 1024->32768`; exact one-replacement records and pre/post hashes retained.

Numerically, common injected grids make kpd10-vs-kpd20 discrepancy exactly 0.0 for both historical worst probes at N=64,128,256. However no N satisfies the unchanged exact-reference threshold for both probes: relative errors (alpha,beta) are N64=(0.02180944307037863,0.010271933047184831), N128=(0.002948331371014129,0.15002287750650692), N256=(0.0016209539350102622,0.021933644441162473). Thus `scaling_candidates=[]`; no Layer-B/covariance authority is created.

Durable JE authority commit `169da05db02bdeee7cccb3a62bd5aad4ca275cad`.

## Next prospective gate — Exp073JF
Because JE prospectively required continued scaling/mechanism isolation when no N qualifies, Exp073JF was frozen before output. Preregistration commit `34136c87f49bf990d16670ca984c239194056db2`; implementation commit `579dab75cd78d19ca05cb406c2c8852b52bc7f3e`; workflow/launch head `a99465377e0d070bce43982906d29ba21b1eb06b`.

Exp073JF changes only the shared-grid density ladder to N={384,512}; it preserves the identical common-grid estimator, target probes, h=1e-4, kpd={10,20}, REL_TOL=1e-3, pinned CLASS-IV source, public d_m route, and repaired storage/parser capacities. It is support-only +0/+0.

Current authoritative process: workflow `exp073jf-article3-layerb-shared-fixed-k-grid-extended-density-v0-1`; run/job `34480017627 / 102880180988`; branch/head `main / a99465377e0d070bce43982906d29ba21b1eb06b`; checkpoint N/A; GitHub-hosted ubuntu-24.04; home/self-hosted ownership none. Last observed state IN_PROGRESS. Contract/JE-authority checks succeeded; frozen stack/capacity regression was active.

Exact next action: terminal-consume `34480017627`; independently verify raw log and artifact hashes/provenance. If N=384 or 512 qualifies under the frozen rule, nominate the smallest qualifying N only for a separate prospectively frozen full-support feasibility audit. If neither qualifies, record simple global geomspace density through current exact capacity as numerically inadequate and move to interpolation phase/curvature or another grid-invariant mechanism diagnostic without tolerance rescue.
