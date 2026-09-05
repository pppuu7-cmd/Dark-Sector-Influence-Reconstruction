# DSIR immutable recovery — Exp073DS v0.2 readiness PASS; Exp073DT WW_S0_S0 science launched

Date: 2026-09-05. DSIR only; RTK/RQIR excluded.

## Preserved authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact PASS remain unchanged. Historical Exp073CM resource FAIL and original Exp073BU runner-loss remain immutable `+0/+0`.

## Reconciled closed WW support chain
Exp073DP repaired hosted exact-equivalence run/job `33938446310 / 101230897808` is raw-artifact PASS `+0/+0`: artifact `9960969007`, GitHub and independent ZIP SHA256 `e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8`, token `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1`, official NaMaster v2.7 source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`; all three deterministic cases have exact full and selected-EE SHA equality, `numpy.array_equal=true`, and max absolute difference `0.0`.

Exp073DQ durable A/B driver static PASS `+0/+0`: run/job `33938583879 / 101231302981`, artifact `9961000737`, driver SHA256 `0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b`.

Exp073DR activation/resource PASS `+0/+0`: run/job `33938637212 / 101231459805`, artifact `9961019381`; it admitted a home-readiness preflight, not science.

Exp073DS v0.1 is permanently governance-invalid `+0/+0` because its flock was acquired in a separate Actions shell step and therefore did not cover the readiness body. Prospective v0.2 repair commit/head `b6a6f2bd501b2b388a125dc069b3b720643ad347` moved the entire readiness body under one continuous nonblocking flock. Repaired run `33938789513`, attempt 2, jobs `101233076119 / 101233097355`, terminal SUCCESS; artifact `9961211035`; GitHub and independent ZIP SHA256 `d12693ce2b2ec17abfef7008e82eca2bf9f9a29b99f43b00c83e30b2313df53d`. Raw receipt token `PASS_EXP073DS_WW_S0_S0_HOME_READINESS_EXCLUSIVITY_V0_1`, `classification=SUPPORT_HOME_READINESS_PASS_PLUS_0_PLUS_0`, `continuous_lock_scope_verified=true`, affinity CPUs=8, PyMaster 2.7, OMP threads/runtime team=8, nested BLAS/MKL/OpenBLAS/NumExpr/BLIS/VECLIB threads=1, no full workspace or selected WW payload, no WW authority.

## Exp073DT prospective science gate
Preregistration commit `946964121f12c67e053514109bf974050eeb0cc9`; workflow activation commit/head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`. Contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; frozen source authority head `de83e20a68f79ccf25b89b0d33eb4206e294c757`.

Science target is exactly `WW_S0_S0`: S0 spin-2 auto, no lens mask, DES NSIDE=4096, ell 0..12287, 39 bands, full stock `[4,39,4,12288]`, selected `EE<-EE`, canonical `<f8 [39,12288]`. It reuses the admitted Exp073DQ durable driver and Exp073DO adapter without arithmetic changes. Replica manifests remain the frozen independent DQ namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `...-b-v0-1`; durable root is `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`. Verified complete stages must be resumed rather than recomputed.

Live workflow run `33940588308`: hosted preflight job `101237102962` SUCCESS after exact component binding and noncompetition. Home science job `101237118421` is `IN_PROGRESS` at this note, executing `Full fail-closed WW_S0_S0 A/B science under one continuous flock`. DSIR-HOME-PC is therefore RESERVED BY Exp073DT. No competing self-hosted run may be launched.

Scientific PASS token is prospectively frozen as `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`. It is allowed only when the DQ terminal comparator has exact SHA equality, exact `numpy.array_equal=true`, no tolerance rescue, independently re-read A/B `<f8 [39,12288]` selected payloads have identical SHA and arrays, and all provenance/checkpoint bindings pass. Exact A/B inequality is scientific repeatability FAIL; infrastructure/runtime/checkpoint/provenance failures are `+0/+0`.

## Next action
Consume terminal run/job `33940588308 / 101237118421` without duplication. Inspect raw artifact, digest, terminal receipt, both selected payloads, A/B comparator, replica receipts and checkpoint provenance before creating any `WW_S0_S0` scientific authority. On PASS the next frozen angular object is `WW_S0_S1`; on infrastructure failure diagnose the first cause and preserve verified checkpoints.
