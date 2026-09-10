# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JE_VALIDATED_JF_RUNNING_V70.md`, creation commit `29e438d438a34e7f45a3731fbaa3dc2f48b6eb78`. Earlier notes remain immutable history.

## Preserved authority
All prior admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107 coordinate rows, atomic production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. Exp073CM remains historical resource/performance `+0/+0`; Wm_S3 remains unopened.

## Exp073JE validated support result
Repaired Exp073JE run/job `34474978911 / 102863474356`, head `3f74511a78724ac11e64d98284321df12cc7d1a8`, is validated support-only `SHARED_FIXED_K_GRID_SCALING_OBSERVED_PLUS_0_PLUS_0`. Artifact `10151168583`; independently verified ZIP SHA256 `cf2e70a8bb35dcdb782d49fe5a29b908f6897169d6fe2c055c9b92eb1bfa01af`; result JSON SHA256 `c55e71faa6a8a43a61f6910908bb161deb2075d5212b5851d1551a078fbd5a33`; capacity-patch JSON SHA256 `f7d8d33232908f5f90f557ef42eeead4acc9dcc58a92f69629857aece2e1889b`. Durable authority commit `169da05db02bdeee7cccb3a62bd5aad4ca275cad`.

At N={64,128,256}, both probes have exact kpd10-vs-kpd20 discrepancy 0.0, but no N reaches unchanged REL_TOL=1e-3 against exact-k references for both probes. Relative errors (alpha,beta): N64=(0.02180944307037863,0.010271933047184831), N128=(0.002948331371014129,0.15002287750650692), N256=(0.0016209539350102622,0.021933644441162473). `scaling_candidates=[]`. No Layer-B/covariance authority is created.

Historical JE attempts 1 and 2 remain infrastructure `+0/+0`: malloc corruption from parser-capacity mismatch, then static-audit ordering before numpy installation. The prospective repairs remain infrastructure-only and do not alter science.

## Current process — Exp073JF
Exp073JF prospectively extends only the common-grid node ladder to N={384,512}; all physics, estimator, exact-k references, h=1e-4, kpd={10,20}, REL_TOL=1e-3, and audited capacity patches remain unchanged. Prereg commit `34136c87f49bf990d16670ca984c239194056db2`; implementation commit `579dab75cd78d19ca05cb406c2c8852b52bc7f3e`; workflow/head `a99465377e0d070bce43982906d29ba21b1eb06b`.

Authoritative workflow/run/job: `exp073jf-article3-layerb-shared-fixed-k-grid-extended-density-v0-1 / 34480017627 / 102880180988`; branch/head `main / a99465377e0d070bce43982906d29ba21b1eb06b`; GitHub-hosted `ubuntu-24.04`; checkpoint N/A; home/self-hosted ownership none. Last observed state IN_PROGRESS; contract/JE-authority checks succeeded and frozen stack/capacity regression was running.

Exact next action: terminal-consume `34480017627`, verify raw log/artifact/hash/provenance. If N=384 or 512 qualifies, nominate the smallest only for a separate prospectively frozen full-support feasibility audit. If neither qualifies, simple global geomspace density through current exact capacity is numerically inadequate at the frozen worst probes; continue with interpolation phase/curvature or another grid-invariant mechanism diagnostic without tolerance rescue.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
