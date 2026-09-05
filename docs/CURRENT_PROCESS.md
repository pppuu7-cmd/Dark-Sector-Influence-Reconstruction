# DSIR current-process ledger

Updated: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Preserved scientific authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0` and original Exp073BU runner-loss infrastructure `+0/+0` remain immutable.

## Reconciled WW support authority
- Exp073DP repaired exact-equivalence PASS `+0/+0`: run/job `33938446310 / 101230897808`, artifact `9960969007`, ZIP SHA256 `e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8`.
- Exp073DQ durable A/B driver static PASS `+0/+0`: `33938583879 / 101231302981`, artifact `9961000737`, driver SHA256 `0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b`.
- Exp073DR activation/resource PASS `+0/+0`: `33938637212 / 101231459805`, artifact `9961019381`.
- Exp073DS v0.1 governance-invalid `+0/+0`.
- Exp073DS v0.2 readiness PASS `+0/+0`: run `33938789513` attempt 2, jobs `101233076119 / 101233097355`, artifact `9961211035`, ZIP SHA256 `d12693ce2b2ec17abfef7008e82eca2bf9f9a29b99f43b00c83e30b2313df53d`.
- Exp073EA saved-LU official-reload-state exactness qualifier PASS `+0/+0`: run/job `33956292805 / 101280130448`, artifact `9966484239`, GitHub and independently downloaded ZIP SHA256 `7850d7c01ece7c2cb3ed8ea11b208a5600aea4a3fd68da81e2e17db9d06a1f61`, token `PASS_EXP073EA_SAVED_LU_EXACT_OFFICIAL_RELOAD_STATE_V0_1`. It establishes exact saved-LU equivalence to the official serialized/reloaded PyMaster state, not to the original pre-serialization in-memory state, and creates no WW science authority.

## Current authoritative process — Exp073DT WW_S0_S0 checkpoint-preserving resume
Preregistration commit `946964121f12c67e053514109bf974050eeb0cc9`; frozen activation workflow/head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`.

Attempt 1: run `33940588308`, hosted preflight `101237102962` SUCCESS; self-hosted `101237118421` external runner shutdown at `2026-09-05T03:56:42Z`; science CANCELLED; evidence SKIPPED; `INFRASTRUCTURE_INCOMPLETE +0/+0`.

Attempt 2: hosted preflight `101244675822` SUCCESS; self-hosted `101244660215` external runner shutdown at `2026-09-05T07:49:54Z`; science CANCELLED; evidence SKIPPED; no run artifacts; `INFRASTRUCTURE_INCOMPLETE +0/+0`. No numerical/scientific failure preceded the shutdown.

Attempt 3 is authoritative and live:
- run `33940588308`, attempt `3`;
- hosted preflight `101274119122`: SUCCESS;
- self-hosted science `101274118640`: **IN_PROGRESS** at latest reconciliation;
- active step: `Full fail-closed WW_S0_S0 A/B science under one continuous flock`;
- terminal evidence upload remains pending;
- runner ownership: **DSIR-HOME-PC RESERVED BY Exp073DT attempt 3**;
- live Actions reconciliation: exactly `1 in_progress / 0 queued` DSIR workflow runs.

Frozen identity remains unchanged:
- frozen head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`;
- frozen source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- checkpoint namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`.

Only complete hash/identity-verified stages may be restored; interrupted/incomplete stages recompute; malformed/mismatched state fails closed. Frozen science remains `WW_S0_S0`, DES NSIDE=4096, ell 0..12287, 39 bands, full `[4,39,4,12288]`, selected `EE<-EE`, canonical `<f8 [39,12288]`, OpenMP=8, nested numerical-library threads=1, no tolerance rescue.

Immutable reconciliation notes:
- `recovery/2026-09-05_exp073dt_runner_shutdown_infrastructure_resume.md`;
- `recovery/2026-09-05_exp073dt_attempt2_runner_shutdown_dispatch_block.md`;
- `recovery/2026-09-05_exp073dt_attempt3_same_frozen_resume_dispatched.md`;
- `recovery/2026-09-05_exp073ea_saved_lu_official_reload_exact_pass.md`.

## Independent non-biasing preparation
Commit `2f9c2950dc118aa281b938d58f444fcfed3b8d18` adds Exp073DU, a small-NSIDE distinct-field `WW_S0_S1` cross-field adapter qualifier. Later hosted-only diagnostics through Exp073EA remain support-only and cannot supersede Exp073DT or create science authority. Exp073EA specifically shows that the saved-LU path can reproduce the official serialized/reloaded PyMaster numerical state bit-for-bit, while the original in-memory state remains last-bit distinct; this boundary must be preserved prospectively in any future checkpoint route.

On Exp073DT terminal SUCCESS: independently inspect raw artifact/digest, receipt, A/B selected payloads, comparator, replica receipts and checkpoint provenance. Only exact SHA equality plus `numpy.array_equal=true` and frozen token create `WW_S0_S0` authority. Exact A/B inequality is scientific repeatability FAIL. Infrastructure/checkpoint/provenance/artifact failures are `+0/+0`.

## Frozen frontier
`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
