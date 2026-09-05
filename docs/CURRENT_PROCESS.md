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

## Current authoritative process — Exp073DT WW_S0_S0 checkpoint-preserving resume
Preregistration commit `946964121f12c67e053514109bf974050eeb0cc9`; frozen activation workflow/head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`.

Attempt 1 of run `33940588308`: hosted preflight `101237102962` SUCCESS; self-hosted science `101237118421` terminated FAILURE because the runner received a shutdown signal at `2026-09-05T03:56:42Z`; science step CANCELLED; evidence upload SKIPPED. Classification is `INFRASTRUCTURE_INCOMPLETE +0/+0`, not science.

Attempt 2 is now authoritative:
- run `33940588308`, attempt `2`;
- hosted preflight job `101244675822`: SUCCESS;
- self-hosted resume job `101244660215`: **IN_PROGRESS** at latest reconciliation;
- active step: `Full fail-closed WW_S0_S0 A/B science under one continuous flock`;
- frozen head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`;
- frozen source authority head `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable science root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- checkpoint namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`;
- runner ownership: **DSIR-HOME-PC RESERVED BY Exp073DT resume**.

The retry was dispatched only after first-cause diagnosis. No code/science repair was made because the cause is external runner shutdown, not a code or numerical defect. The frozen DQ driver must restore only hash/identity-verified complete stages and recompute interrupted/incomplete stages. Any malformed/mismatched checkpoint fails closed.

Frozen science remains exactly `WW_S0_S0`, no lens mask, DES NSIDE=4096, ell 0..12287, 39 bands, full `[4,39,4,12288]`, selected `EE<-EE`, canonical `<f8 [39,12288]`, exactly 8 OpenMP workers, nested numerical-library threads pinned to 1, no tolerance rescue.

## Independent non-biasing preparation while Exp073DT runs
Commit `2f9c2950dc118aa281b938d58f444fcfed3b8d18` adds Exp073DU, a small-NSIDE distinct-field `WW_S0_S1` cross-field adapter qualifier. It is preparation only: `science_gate_scored=false`, `ww_s0_s1_authority_created=false`, and it must not launch or alter the frozen Exp073DT result. It records ordered cross-field behavior and requires the production adapter to match direct PyMaster `EE<-EE` exactly without tolerance rescue.

On Exp073DT SUCCESS: independently inspect terminal artifact/digest, receipt, A/B selected payloads, comparator, replica receipts and checkpoint provenance. Only exact SHA equality plus `numpy.array_equal=true` creates `WW_S0_S0` authority. Then consume/validate any prospectively frozen Exp073DU qualifier result before deciding the full-resolution `WW_S0_S1` science launch. On exact A/B inequality: scientific repeatability FAIL. On new infrastructure/checkpoint failure: `+0/+0`, diagnose first new cause and preserve verified stages.

## Frozen frontier
`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
