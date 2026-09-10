# DSIR recovery V90 — JO v0.5 exact-negative; JQ same-run causal test active

Date: 2026-09-10. Scope: DSIR only.

## Stable readiness
Article III repository readiness **68%**. Overall funnel-to-freeze readiness **67%**. No process/diagnostic result in JO/JQ changes these scores by itself.

## Preserved science authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; JI support feasible; JJ/JK support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`. Frozen science domain/masks/traversal, `h=1e-4`, `REL_TOL=1e-3` and anti-rescue rules remain unchanged. Covariance restriction remains unauthorized; Wm_S3 unopened.

## JO v0.5 terminal authority
Canonical response run `34530745922`, workflow head `5c11549604f3254c51dbc180464deb77740a12b3`: static-equivalence and all eight canonical per-model shards completed SUCCESS. Every independently audited shard used canonical node SHA `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`; all eight ZIP digests and 32-byte payload SHA values matched GitHub metadata/receipts.

Aggregate job `103051590840` reached the preregistered exact comparison and emitted valid negative token `FAIL_EXP073JO_SLOT20_CANONICAL_SHARDED_HISTORY_EXACT_V0_5` with classification `SLOT20_CANONICAL_SHARDED_HISTORY_EXACT_FAIL_PLUS_0_PLUS_0`:
- exact array equality false;
- finite-mask equality true;
- positive-mask equality true;
- after-history response SHA256 `c584b9acc50d49182d0e4ec5db7e631af029017a762880c6503f19a0d7aa19cd`;
- fresh-tail response SHA256 `e4df13c0415250c5ec21a33baf010bab23f9eae9071f3e6df51be74f47c9b32c`;
- aggregate artifact `10173492396`, ZIP SHA256 `bffa951a13692c14c8d74651374d4651c321a9835718df0afd48501c22207637`;
- result JSON SHA256 `788a6c343f0e7497270e51b78a6761500697a279687d8ad1db32db48c64b9ce2`.

Independent reconstruction from all eight shard payloads exactly reproduced both aggregate 64-byte response arrays. Diagnostic-only max response difference: absolute `9.094947017729282e-09`, relative `3.985177923580332e-12`. These magnitudes do not relax the exact preregistered decision.

Durable negative authority: `docs/dsir4/authority/EXP073JO_SLOT20_CANONICAL_SHARDED_HISTORY_EXACT_NEGATIVE_V0_5.json`, creation commit `3c3be31babeef4dc83a08f9d8c5caf4c0043fbd7`. Checkpointed JL replay is unauthorized.

## Causal qualification
Post-result support-only audit `docs/dsir4/audits/EXP073JO_V05_CROSS_RUNNER_EXACT_REPRODUCIBILITY_DIAGNOSTIC_V0_1.md`, commit `38ee7ced55a3957a77c65b1425803f01938d7649`, compared only same phase/model pairs whose v0.4 and v0.5 node SHA was exactly the same canonical value. Two of six such pairs changed by `9.094947017729282e-13` in a tail interpolant, about machine-epsilon relative scale. Thus JO v0.5 validly proves failure of the exact cross-execution control but does not establish query history as the sole cause; cross-runner last-bit nondeterminism is a confounder.

## Exp073JQ active
Prospectively frozen JQ prereg `docs/dsir4/prereg/EXP073JQ_ARTICLE3_SLOT20_SAME_RUN_CAUSAL_DISCRIMINATION_V0_1.md`, creation commit `16dd5b3ccc55791d534134205f2a3210b000701d`, blob `a67f2e42df0fc04448a62b7cc22cb759841e7690`.

JQ helper `ci/exp073jq_slot20_same_run_causal_discrimination_v0_1.py`, creation commit `eb701cf699c52f4edcc4b5e8d60beb642f5e9936`, blob `636b7195e562f88ea548cde2598585c0f95c34bc`.

Workflow/head `8058c212372862c9dc59fa6fceb8defb17e22d93`; active run `34531670122`.

For each model on one runner it executes three fresh instances in frozen order `fresh_A -> after_history(pre->tail) -> fresh_B`. Exact decision precedence: fresh_A != fresh_B => same-run fresh reexecution nondeterminism; else history differs => same-run history dependence confirmed; else same-run history independence PASS. JQ is support-only and cannot authorize checkpointed JL by itself.

## Exact next action
Terminal-consume JQ run `34531670122`; independently verify four model artifacts and aggregate. Based only on the prospectively frozen JQ branch, preregister a self-contained same-run atomic Layer-B execution architecture so operands of the scientific convergence comparison never cross runner/process boundaries. No tolerance, grid, estimator, mask or science rescue.