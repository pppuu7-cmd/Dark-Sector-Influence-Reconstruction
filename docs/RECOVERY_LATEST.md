# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HR_INTERVAL_HOOK_FAIL_HS_GUARD_FRONT_V38.md` (creation commit `bf7b091e566bb47b1197d703e1e58bfb6fb79c6c`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

All prior scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW authority through scientifically admitted `S3_S3` remains preserved; `WW_S3_S3` authority is run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

C2 remains `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Terminal runtime history

Exp073HO v0.1 `34229170304 / 102070681656` remains historical implementation/runtime exact-endpoint failure `+0/+0` with no raw artifact.

Exp073HR v0.2 `34230309394 / 102074480794`, head `acb71f5d0584c4b64a86cb691f9f28f1c1482037`, is also terminal `FAILURE`. Frozen binding, post-HQ reconstruction and build all passed. The unchanged first request `z00k00`, `z=0.295`, physical `k=0.00067 Mpc^-1` failed before serialization/receipt/artifact with exact chain `perturb_init -> perturb_solve -> evolver_ndf15 -> dsir_c2_diag_arm_terminal(tfinal,...)` and exact condition `tau != dsir_c2_diag_tau_target`.

No raw candidate exists. HR is **implementation/control-flow FAIL `+0/+0`**, not scientific FAIL.

## Refined causal diagnosis

Pinned `perturb_solve` invokes `generic_evolver` separately for every approximation interval and passes each interval's `interval_limit[index_interval+1]` as its `tfinal`. The diagnostic hook had been executing whenever each individual evolver call reached `done==_TRUE_`. Therefore the first non-final approximation-switch boundary was incorrectly treated as the overall literal-z terminal endpoint. This fully explains why HQ's per-evolver exact `tfinal` remained unequal to the frozen overall target without implicating numerical tolerance or physics.

## Current C2 frontier — Exp073HS exact final-interval guard audit

Exp073HS is prospectively frozen in `docs/dsir4/prereg/EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1.md`, blob `d3a135cce56124ead0c4c5cc4a6a830767420be4`, creation commit `cdc89b729e04ea604d6d950fb3259605489e44c2`.

Patch blob `57cd2b9c0e07c7e6c066cae46f6bc368f5086e35`; workflow blob `8e834ad1fceebb21d6d64f298f0d1f8301d4816b`; binding/head commit `68567340d5164d5554dbb5f770fe2d1b755227ba`.

Authoritative process: run `34230896860`, job `102076459069`, GitHub-hosted `ubuntu-24.04`, state at pointer update **IN_PROGRESS**. No self-hosted/home heavy owner exists.

HS changes diagnostic control flow only: it allows the endpoint hook only when `done==_TRUE_` and the current exact `tfinal == dsir_c2_diag_tau_target` by strict binary64 equality. Earlier approximation intervals are ignored as non-terminal observations. The already accepted `ynew`, equations, integration arithmetic, tolerances, model, frozen z/k grid, baseline, p8, packet ABI, field order and provenance rules remain unchanged. No tolerance, rounding, nearest-time or interpolation rescue is introduced.

Expected exact token: `PASS_EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1`, classification ceiling `SUPPORT_PLUS_0_PLUS_0`; HS is build/static only and cannot create a raw record set or scientific authority.

## Exact next transition

On HS raw-log PASS, freeze a separately versioned raw `(0,0)` producer using exact post-HS source hashes and the unchanged 28-node model/grid/config/64-byte ABI, then execute it. On HS FAIL, diagnose and repair only the smallest causal implementation/static-build defect prospectively.

Global frozen DSIR science boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
