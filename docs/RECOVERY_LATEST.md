# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JE_REPAIR_ORDERING_FIXED_RERUNNING_V69.md`, creation commit `6e00b0633fc0f38ecc4314ae687e6d152cf7b739`. Earlier notes remain immutable history.

## Preserved authority
All prior admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107 coordinate rows, atomic production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. Exp073CM remains historical resource/performance `+0/+0`; Wm_S3 remains unopened.

## Exp073JD provenance correction
JD remains validated support-only `EXACT_K_ORIGINAL_PAIR_OBSERVED_PLUS_0_PLUS_0`, run/job `34472918931 / 102856790715`, artifact `10150322510`. V0_1 authority contained incorrect SHA256 fields. Corrected immutable V0_2 commit `1fcc02d6d252d3f47184be565218cf29355c3c8c` records GitHub/downloaded ZIP SHA256 `310939a4b4ef8d75cb027630e5f43f88003ab92045c0af6e83ab83764bcb6365` and contained JSON SHA256 `ba26c2a89a41d67e65bbf0b630659fccae33d85a7d05c2d0d4d493f8b33dfccb`. Numerical result/classification unchanged.

## Exp073JE infrastructure history
Attempt 1 `34474514433 / 102861967751` failed before artifact creation with `malloc(): corrupted top size`, exit 134. Root capacity mismatch: `_MAX_NUMBER_OF_K_FILES_` had been enlarged to 512 while parser `_ARGUMENT_LENGTH_MAX_` remained 1024; N=256 exact k-output serialization exceeds the original parser storage. This is infrastructure `+0/+0`, not science.

Prospective infrastructure repair commit `16f984a9a81ac5e3d559d67e191f7bb9f6ffd85b` adds only `_ARGUMENT_LENGTH_MAX_ 1024 -> 32768` plus exact replacement/hash and serialized-length regression checks. No JE numerical/scientific criterion changes.

Attempt 2 `34474839354 / 102863020808`, head `6090af1b41b86bd878c4e348874a496c04a09053`, failed before dependencies/build/science because the new regression imported numpy before the install step: `ModuleNotFoundError: No module named 'numpy'`. Infrastructure `+0/+0`. The smallest repair moved the unchanged static audit after dependency installation, commit `3f74511a78724ac11e64d98284321df12cc7d1a8`.

## Current process
Authoritative workflow/run/job: `exp073je-article3-layerb-shared-fixed-k-grid-scaling-v0-1 / 34474978911 / 102863474356`; head `3f74511a78724ac11e64d98284321df12cc7d1a8`; GitHub-hosted `ubuntu-24.04`; checkpoint N/A; home/self-hosted ownership none. Last observed state IN_PROGRESS. Contract/repair/JD-lineage succeeded; dependency install plus parser-capacity regression was running.

Exact next action: terminal-consume `34474978911`. On valid output, independently verify raw artifact and both capacity-patch provenance records and classify only under frozen JE. On failure, diagnose first causal defect before any rerun. JE cannot retroactively PASS Exp073IR or authorize covariance restriction/Wm_S3/model/manuscript authority.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
