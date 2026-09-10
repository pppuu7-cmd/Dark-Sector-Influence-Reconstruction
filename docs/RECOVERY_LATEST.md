# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JF_IMPORT_REPAIR_RERUNNING_V71.md`, creation commit `f223905c0a501aa5d6b6624353945f29e6f37647`. Earlier notes remain immutable history.

## Preserved authority
All prior admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107 coordinate rows, atomic production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. Exp073CM remains historical resource/performance `+0/+0`; Wm_S3 remains unopened.

## Exp073JE validated support result
Exp073JE run/job `34474978911 / 102863474356` is validated support-only `SHARED_FIXED_K_GRID_SCALING_OBSERVED_PLUS_0_PLUS_0`; artifact `10151168583`, independently verified ZIP SHA256 `cf2e70a8bb35dcdb782d49fe5a29b908f6897169d6fe2c055c9b92eb1bfa01af`, durable authority commit `169da05db02bdeee7cccb3a62bd5aad4ca275cad`. N={64,128,256} gives exact kpd10-vs-kpd20 equality at both probes but no exact-reference scaling candidate under unchanged REL_TOL=1e-3.

## Exp073JF infrastructure history and repair
Exp073JF attempt 1 `34480017627 / 102880180988`, head `a99465377e0d070bce43982906d29ba21b1eb06b`, is infrastructure/software failure `+0/+0`. Contract/dependencies/capacity regression and exact patched CLASS-IV build succeeded; before any JF numerical calculation the script failed with `ModuleNotFoundError: No module named 'ci'`. No artifact/scientific result was created.

Smallest repair commit `1cd0692454e238162be0235f56e49453b4f40999` changes only sibling-module import resolution. Workflow commit `2e5e43de2abaec3be93f5fe1a2fbe909b6e86048` adds a reproducible post-dependency import regression and triggers the repaired run. No frozen numerical or scientific setting changed.

## Current process
Authoritative workflow/run/job: `exp073jf-article3-layerb-shared-fixed-k-grid-extended-density-v0-1 / 34480349238 / 102881291672`; branch/head `main / 2e5e43de2abaec3be93f5fe1a2fbe909b6e86048`; GitHub-hosted `ubuntu-24.04`; checkpoint N/A; home/self-hosted ownership none. Last observed state IN_PROGRESS.

Exact next action: terminal-consume `34480349238`, verify raw log/artifact/hash/provenance and classify only under frozen Exp073JF. If a candidate exists, nominate only the smallest for a separate full-support feasibility audit. If none exists, continue prospectively with interpolation phase/curvature or another grid-invariant mechanism diagnostic; never rescue by changing `REL_TOL=1e-3`.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
