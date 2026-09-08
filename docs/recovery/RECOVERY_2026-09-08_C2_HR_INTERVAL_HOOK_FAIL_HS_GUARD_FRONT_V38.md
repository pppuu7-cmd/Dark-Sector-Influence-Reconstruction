# DSIR immutable recovery — C2 HR interval-hook FAIL, HS exact-final-interval guard front — V38

Date: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved scientific authority

All prior scientific authority remains unchanged, including scientifically admitted `WW_S3_S3`. C2 remains `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Exp073HR terminal consumption

Frozen Exp073HR v0.2 run `34230309394`, job `102074480794`, head `acb71f5d0584c4b64a86cb691f9f28f1c1482037`, is terminal `FAILURE`.

Raw log verification:
- runtime binding verification PASS;
- exact post-HQ source reconstruction/build PASS;
- post-HQ `source/perturbations.c` SHA256 remained `8c76c0b0ba8de6c0528980569ae748b24ff1b790a9f752ac11e90ca71d5b63de`;
- post-HQ `tools/evolver_ndf15.c` SHA256 was `7cfd7410b0abec61f679b365dde2af1b851843396aee5267de7873353b1e608b`;
- failure occurred on unchanged first frozen request `z00k00`, `z=0.295`, physical `k=0.00067 Mpc^-1`, before serialization/receipt/artifact;
- exact chain: `perturb_init -> perturb_solve -> evolver_ndf15 -> dsir_c2_diag_arm_terminal(tfinal,...)`;
- exact condition remained `tau != dsir_c2_diag_tau_target`.

No raw candidate artifact exists. Classification: **implementation/control-flow FAIL `+0/+0`**, not scientific FAIL.

## Refined causal diagnosis

Source reconciliation with pinned `perturb_solve` shows `generic_evolver` is invoked separately for every approximation interval, with each interval using `interval_limit[index_interval+1]` as its own `tfinal`. The diagnostic hook inserted in NDF15 runs whenever that individual evolver call reaches `done==_TRUE_`. Therefore the hook was incorrectly treating the end of a non-final approximation interval as the overall literal-z endpoint.

This explains why HQ's exact `tfinal` canonicalization could still fail: the first completed evolver interval had a valid exact `tfinal`, but it was an approximation-switch boundary rather than the overall frozen `background_tau_of_z` target. No tolerance, rounding, interpolation, coordinate or science defect is implicated.

## Current process — Exp073HS exact final-interval guard support audit

A new prospective support contract was frozen before implementation:

- prereg `docs/dsir4/prereg/EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1.md`;
- prereg blob `d3a135cce56124ead0c4c5cc4a6a830767420be4`;
- prereg creation commit `cdc89b729e04ea604d6d950fb3259605489e44c2`;
- patch `scripts/dsir4/exp073hs_c2_final_approximation_interval_endpoint_guard_patch_v0_1.py`, blob `57cd2b9c0e07c7e6c066cae46f6bc368f5086e35`;
- workflow blob `8e834ad1fceebb21d6d64f298f0d1f8301d4816b`;
- binding/head commit `68567340d5164d5554dbb5f770fe2d1b755227ba`;
- run `34230896860`;
- job `102076459069`;
- runner ownership GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner none;
- state at V38 creation: **IN_PROGRESS**.

HS changes only diagnostic control flow. It adds `dsir_c2_diag_is_exact_terminal_target(tau)`, true iff diagnostic mode is enabled and `tau == dsir_c2_diag_tau_target` by exact binary64 equality. The NDF15 hook condition changes from generic diagnostic-enabled completion to `done==_TRUE_ && dsir_c2_diag_is_exact_terminal_target(tfinal)!=0`. Existing HQ hook body remains exactly on `tfinal` and already accepted `ynew`.

This is not a tolerance/acceptance rescue. Non-final approximation intervals are simply not endpoint observations. No state, step, equations, tolerances, model, grid, baseline, p8, ABI, field order or provenance rule is changed.

Expected support token: `PASS_EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1`. Classification ceiling `SUPPORT_PLUS_0_PLUS_0`; no cosmological run or raw packet is permitted in HS.

## Exact next action

On HS raw-log PASS: freeze a new separately versioned reference raw-runtime producer using the unchanged `(0,0)` model/grid/config/ABI and the exact post-HS source identities, then execute it without inspecting partial scientific values. On HS FAIL: diagnose the first causal source/build/static-audit defect and repair only that smallest implementation defect prospectively.

No home/self-hosted heavy run is required or authorized for this C2 front. Global frozen DSIR scientific boundaries remain unchanged.
