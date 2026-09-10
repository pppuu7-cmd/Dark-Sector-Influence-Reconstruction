# DSIR recovery — Article III JL attempt-1 runner shutdown / attempt-2 running — V79

Date: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved scientific authority
- Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; original native production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`.
- Exp073JI remains the validated shared-grid full-support feasibility authority: all 107 retained rows, zero unsupported targets, invalid fraction 0, native-kpd10-vs20 shared-grid discrepancy 0.0.
- Exp073JJ remains support-only valid NOT_CONVERGED at `0.037280144773915974` for base 512->1024.
- Exp073JK remains support-only valid `COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0` at `0.016330535730270664` for base 1024->2048; run/job `34495159732 / 102931623100`, artifact `10160083225`, independently verified ZIP SHA256 `a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99`, durable authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`.
- Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Exp073JL frozen contract
Prospective preregistration commit `608fbf5fd9912b9f0244283d940a7adfecc41ac8`; implementation commit `43e1d74e8216c1ff66bfe4d0eed372673d0e5b1b`; workflow/head `d556db87763637dd90ed919dbe5d85ef95b4beb1`.

JL compares guarded base N=2048 (2049 requested) against base N=4096 (4097 requested), with native CLASS kpd=20 for both, unchanged centered-cubic interpolation in ln(k), finite-difference h=1e-4, `REL_TOL=1e-3`, identical Exp073IR atom traversal/support and frozen physical domain. Infrastructure-only capacities are `_MAX_NUMBER_OF_K_FILES_=4608` and `_ARGUMENT_LENGTH_MAX_=131072`.

## Attempt 1 — invalid process outcome, no science
Workflow run `34497160814`, attempt 1, job `102938434376`, GitHub-hosted ubuntu-24.04.

All setup/lineage/build/input steps 1-9 completed successfully. Numerical step 10 began at `2026-09-10T15:42:59Z`. At `2026-09-10T15:56:49Z` the runner log emitted exactly: `The runner has received a shutdown signal. This can happen when the runner service is stopped, or a manually started runner is canceled.` It was followed by `The operation was canceled.` The numerical step concluded `cancelled`; artifact upload was skipped; no JL result JSON or scientific classification was produced.

Classification of attempt 1: **INVALID_PROCESS_RUNNER_SHUTDOWN_PLUS_0_PLUS_0**. It is neither CONVERGED nor NOT_CONVERGED and activates neither downstream conditional branch. There is no evidence in the available job log of a CLASS exception, Python traceback, numerical assertion failure, tolerance failure, or scientific result before shutdown.

The available GitHub run/job metadata does not identify the causal caller of the shutdown with enough specificity to attribute it to ChatGPT automation, a manual action, or platform orchestration. Do not speculate. The scientifically relevant fact is that the frozen computation was interrupted externally and produced no authority artifact.

## Attempt 2 — authoritative active process
The same frozen workflow run `34497160814` is now `run_attempt=2`, current job `102944693569`, same head `d556db87763637dd90ed919dbe5d85ef95b4beb1`. This is the only authorized active JL heavy computation. Last verified state: setup, checkout, prospective contract/JK/JI authority enforcement, numerical stack, CAMB, pinned CLASS-IV capacity/build, DES payload, Layer-A/angular/Exp073IM authorities, and BOSS inputs all passed; frozen numerical step 10 is in progress.

**Critical process rule:** while attempt 2 is queued/in_progress, do not cancel, rerun, retry, or launch another JL heavy computation. Consume it only after terminal state. A subsequent runner shutdown may justify another identical frozen retry only after the terminal failure log is diagnosed and recorded.

## Pre-result work frozen before JL output
Response-blind diagnostic standard: `docs/dsir4/methods/LAYERB_CONVERGENCE_ARGMAX_DIAGNOSTIC_STANDARD_V0_1.md`, commit `35282a723840c256168b752a86f54666c0cbb4e0`. It is decision-neutral and cannot change the relative-error metric, include/exclude atoms, floor denominators, alter tolerance, or retroactively change JL.

Two mutually exclusive post-JL branches were frozen before any JL numerical result:
- Exp073JM prereg `docs/dsir4/prereg/EXP073JM_ARTICLE3_LAYERB_COMMON_GRID_FOURTH_REFINEMENT_CONVERGENCE_V0_1.md`, commit `440e430465b783365a66c715c7a08e8c1c3a45f8`, only if JL is valid independently verified NOT_CONVERGED. It freezes base 4096->8192 (4097->8193 requested), same cubic/kpd20/h/tolerance, infrastructure capacities 9216/262144.
- Exp073JN prereg `docs/dsir4/prereg/EXP073JN_ARTICLE3_LAYERB_SHARED_GRID_SCIENTIFIC_CLOSURE_RERUN_V0_1.md`, commit `ee35861a7e383749288b61133bffaca333c60ced`, only if JL is valid independently verified CONVERGED. It repeats the exact JL 2049->4097 architecture under a fresh science-authorizing Layer-B contract; JL itself remains support-only +0/+0.

JM implementation was prepared response-blind at `ci/exp073jm_article3_layerb_common_grid_fourth_refinement_convergence_v0_1.py`, commit `3be509b3ac2ca325b8e2c099e91ef59bfbdd8a18`. Its first static-preflight run `34499055755 / 102944880115` failed before any geometry/metric test because the minimal hosted environment lacked NumPy (`ModuleNotFoundError: No module named 'numpy'`). This is infrastructure-only. The preflight workflow was repaired only by adding frozen `numpy==1.26.4`, commit `36c5132cbed6b63a09c664478bdb13f8e01215fb`; replacement static run `34499322858` was queued at last observation. No scientific contract changed.

## Exact next actions
1. Do not interfere with active JL attempt 2 `34497160814 / 102944693569`.
2. Consume the replacement JM static preflight when terminal; repair only static/infrastructure defects if needed.
3. When JL attempt 2 becomes terminal, inspect raw logs first. On workflow success, download the artifact independently, verify ZIP SHA256 and contained result/capacity hashes, and classify strictly against the pre-frozen JL contract.
4. On valid JL CONVERGED, instantiate/run only Exp073JN; JM is forbidden.
5. On valid JL NOT_CONVERGED, create durable JL negative authority and instantiate/run only the already-frozen Exp073JM, including decision-neutral argmax telemetry; JN is forbidden.
6. On infrastructure/process failure, neither branch is activated; diagnose and repair/resume the same frozen JL science without changing thresholds or arithmetic.

## Frozen global boundaries
`0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
