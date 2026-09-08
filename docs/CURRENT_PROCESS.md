# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

All prior scientific authority remains unchanged, including scientifically admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HR_INTERVAL_HOOK_FAIL_HS_GUARD_FRONT_V38.md`, creation commit `bf7b091e566bb47b1197d703e1e58bfb6fb79c6c`.

## Terminal C2 runtime result

Exp073HR v0.2 run `34230309394`, job `102074480794`, head `acb71f5d0584c4b64a86cb691f9f28f1c1482037`, terminal `FAILURE`. Binding and post-HQ build passed; unchanged first request `z00k00`, z `0.295`, k `0.00067 Mpc^-1` failed before serialization/artifact with exact `tau != dsir_c2_diag_tau_target` in `dsir_c2_diag_arm_terminal(tfinal,...)`.

Refined source diagnosis: `perturb_solve` invokes `generic_evolver` once per approximation interval, so `done==TRUE` also occurs at non-final approximation-switch boundaries. HR/HQ therefore invoked the diagnostic endpoint hook on an interval-local `tfinal`, not necessarily the overall literal-z target. Classification is **implementation/control-flow FAIL `+0/+0`**, not scientific FAIL. No raw candidate exists.

## Current process — Exp073HS exact final-interval endpoint guard audit

- prereg `docs/dsir4/prereg/EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1.md`;
- prereg blob `d3a135cce56124ead0c4c5cc4a6a830767420be4`;
- prereg commit `cdc89b729e04ea604d6d950fb3259605489e44c2`;
- patch blob `57cd2b9c0e07c7e6c066cae46f6bc368f5086e35`;
- workflow blob `8e834ad1fceebb21d6d64f298f0d1f8301d4816b`;
- binding/head commit `68567340d5164d5554dbb5f770fe2d1b755227ba`;
- run `34230896860`;
- job `102076459069`;
- runner ownership GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at ledger update: **IN_PROGRESS**;
- expected token `PASS_EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1`;
- classification ceiling `SUPPORT_PLUS_0_PLUS_0`;
- no cosmological run/raw packet/scientific authority permitted.

HS changes diagnostic control flow only: endpoint hook executes only when `done==TRUE` and current exact `tfinal == dsir_c2_diag_tau_target`; earlier approximation intervals are ignored as non-terminal observations. Existing accepted `ynew`, equations, integration arithmetic, tolerances, model, z/k, baseline, p8, 64-byte ABI, field order and provenance rules are unchanged. No tolerance/rounding/nearest-time/interpolation rescue is introduced.

### Exact next action

On HS raw-log PASS: freeze a separately versioned `(0,0)` raw runtime producer using exact post-HS source hashes and unchanged 28-node model/grid/config/ABI, then execute it. On HS FAIL: diagnose the first causal static/build defect and repair only the smallest implementation cause prospectively.

C2 remains `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Global frozen DSIR boundaries remain unchanged.
