# DSIR current-process ledger

Updated: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Preserved scientific authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0` and original Exp073BU runner-loss infrastructure `+0/+0` remain immutable.

## Reconciled WW support authority
- Exp073DP repaired exact-equivalence PASS `+0/+0`: run/job `33938446310 / 101230897808`, artifact `9960969007`, ZIP SHA256 `e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8`, token `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1`, NaMaster source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`.
- Exp073DQ durable A/B driver static PASS `+0/+0`: `33938583879 / 101231302981`, artifact `9961000737`, driver SHA256 `0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b`.
- Exp073DR activation/resource PASS `+0/+0`: `33938637212 / 101231459805`, artifact `9961019381`.
- Exp073DS v0.1 is governance-invalid `+0/+0` because flock scope ended before the readiness body.
- Exp073DS v0.2 readiness PASS `+0/+0`: run `33938789513` attempt 2, jobs `101233076119 / 101233097355`, artifact `9961211035`, GitHub + independent ZIP SHA256 `d12693ce2b2ec17abfef7008e82eca2bf9f9a29b99f43b00c83e30b2313df53d`, token `PASS_EXP073DS_WW_S0_S0_HOME_READINESS_EXCLUSIVITY_V0_1`; continuous lock verified, affinity=8, PyMaster 2.7, runtime OMP team=8, nested threads=1, no scientific payload.

## Current authoritative process — Exp073DT WW_S0_S0 full-resolution exact A/B science
Preregistration commit `946964121f12c67e053514109bf974050eeb0cc9`; activation workflow/head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`.

- workflow/run: `Exp073DT WW_S0_S0 full-resolution A/B exact science v0.1` / `33940588308`;
- hosted preflight job `101237102962`: SUCCESS;
- self-hosted science job `101237118421`: IN_PROGRESS at latest reconciliation;
- run start: `2026-09-05T02:59:11Z`;
- frozen source authority head: `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable science root: `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- checkpoint namespaces inside the frozen DQ driver: `checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected scientific token: `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`;
- current state: `Full fail-closed WW_S0_S0 A/B science under one continuous flock`;
- runner ownership: **DSIR-HOME-PC RESERVED BY Exp073DT**.

Frozen science: task exactly `WW_S0_S0`; no lens mask; DES NSIDE=4096; ell 0..12287; 39 bands; full `[4,39,4,12288]`; selected `EE<-EE`; canonical `<f8 [39,12288]`. Exactly 8 OpenMP workers with nested BLAS/MKL/OpenBLAS/NumExpr/BLIS/VECLIB threads pinned to 1. No tolerance/allclose/rounding/ULP/smoothing/averaging rescue.

On SUCCESS: download and independently inspect terminal artifact/digest, terminal receipt, A/B selected payloads, comparator, replica receipts, source/contract/component/checkpoint provenance. Only exact SHA equality plus `numpy.array_equal=true` under the frozen contract creates `WW_S0_S0` scientific authority and advances frontier to `WW_S0_S1`.

On exact A/B inequality: classify `SCIENTIFIC_REPEATABILITY_FAIL`, preserve it as a scientific result, and proceed according to the frozen frontier without repair of arithmetic.

On runner loss, dependency/runtime/checkpoint/provenance/artifact failure: classify infrastructure/BLOCKED `+0/+0`, diagnose the first cause, preserve verified complete stages, prospectively repair only infrastructure, then resume from verified checkpoints.

## Frozen frontier
`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

## Exact next action
Do not duplicate the home workload. Consume terminal `33940588308 / 101237118421` immediately when available; while it runs, only independent non-biasing audits/documentation are permitted.
