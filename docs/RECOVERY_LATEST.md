# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JE_INFRA_REPAIRED_RERUNNING_V68.md`, creation commit `3ad9b6159d419f3a9dc2ba290c0703795b05614d`. Earlier notes remain immutable history.

## Preserved authority
All earlier admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107 coordinate rows, atomic production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. No tolerance rescue.

Historical Exp073CM remains resource/performance `+0/+0`, not Wm_S3 scientific arithmetic authority. Wm_S3 remains unopened.

## Exp073JD — validated support result with corrected provenance
Exp073JD run/job `34472918931 / 102856790715`, artifact `10150322510`, raw token `PASS_EXP073JD_EXACT_K_ORIGINAL_PAIR_OBSERVED_V0_1`, remains support-only `EXACT_K_ORIGINAL_PAIR_OBSERVED_PLUS_0_PLUS_0`. Authority V0_1 had incorrect SHA256 provenance fields; immutable V0_2 in commit `1fcc02d6d252d3f47184be565218cf29355c3c8c` corrects metadata only. Correct GitHub/downloaded ZIP SHA256: `310939a4b4ef8d75cb027630e5f43f88003ab92045c0af6e83ab83764bcb6365`; contained JSON SHA256: `ba26c2a89a41d67e65bbf0b630659fccae33d85a7d05c2d0d4d493f8b33dfccb`. JD numerical observations/classification are unchanged.

## Exp073JE attempt 1 — infrastructure failure
Run/job `34474514433 / 102861967751`, head `257ef3295e09870df02e681275f828c9bceab8bf`, failed at first diagnostic execution with raw `malloc(): corrupted top size`, exit 134, before result artifact creation. Contract, dependencies and pinned CLASS-IV build had succeeded. This is infrastructure/software failure `+0/+0`, not scientific PASS/FAIL.

First causal architecture defect: JE enlarged `_MAX_NUMBER_OF_K_FILES_ 30 -> 512` while CLASS-IV parser `FileArg` remained `_ARGUMENT_LENGTH_MAX_=1024`; the exact N=256 comma-separated `k_output_values` serialization exceeds the original parser capacity.

## Current — prospectively repaired Exp073JE
Repair preregistration commit `16f984a9a81ac5e3d559d67e191f7bb9f6ffd85b`; workflow repair/head `6090af1b41b86bd878c4e348874a496c04a09053`. The added infrastructure-only patch is exactly `_ARGUMENT_LENGTH_MAX_ 1024 -> 32768`, with replacement/hash checks and a static serialized-length regression. Original JE node grids N={64,128,256}, physical domain, kpd={10,20}, interpolation, `h=1e-4`, `REL_TOL=1e-3`, source definitions and all science criteria are unchanged.

Authoritative current workflow/run/job: `exp073je-article3-layerb-shared-fixed-k-grid-scaling-v0-1 / 34474839354 / 102863020808`; GitHub-hosted `ubuntu-24.04`; checkpoint N/A; home/self-hosted ownership none; last observed state IN_PROGRESS.

Exact next action: terminal-consume `34474839354`. On success, independently verify artifact/hash/patch provenance and every frozen scaling-candidate condition. On failure, diagnose the first causal defect before any rerun. A JE candidate only nominates a separately preregistered full atomic-support audit; it cannot retroactively PASS Exp073IR or authorize covariance restriction/Wm_S3/model/manuscript authority.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
