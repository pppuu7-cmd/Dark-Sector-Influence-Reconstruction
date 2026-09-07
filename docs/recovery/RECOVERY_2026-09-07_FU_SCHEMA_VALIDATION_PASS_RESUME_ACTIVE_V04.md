# DSIR recovery — Exp073FU schema validation PASS / checkpoint resume active v0.4

Date: 2026-09-07. Scope: DSIR only; never mix RTK/RQIR.

## Preserved scientific authority

All previously admitted Wm and WW authorities remain unchanged. `WW_S1_S2` remains admitted only by Exp073FT. `WW_S1_S3` remains NOT ADMITTED.

## Read-only repair validation — CLOSED SUPPORT PASS +0/+0

Run `34103206078`, job `101682164394`, on `DSIR-HOME-PC-2` completed SUCCESS. Raw job log was independently consumed and contains all required evidence:

- repaired pruner blob `b9ed7d7178424fb656b4a7c7bfb2ee370c751cb0`;
- preserved A manifest schema `dsir.exp073fu.ww_s1_s3.durable_ab_production.v0.1.checkpoint`;
- stage `fresh_sources_complete`, complete=true, replica=A;
- checkpoint namespace `checkpoints/exp073fu-ww-s1-s3-a-v0-1`;
- source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- `historical_ww_numerical_import=false`;
- `other_replica_output_read=false`;
- `PASS_EXP073FU_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`;
- `original_checkpoint_mutated=false`;
- exact token `PASS_EXP073FU_REPLICA_A_REPAIRED_PRUNER_READONLY_VALIDATION_V0_6`.

Classification: SUPPORT / implementation validation `+0/+0`. This closes the underscore-schema pruner repair blocker only; it creates no `WW_S1_S3` scientific authority.

## Production resume — AUTHORITATIVE CURRENT PROCESS

Repository commits from the other DSIR process were reconciled and accepted as newer authority:

- wrapper binding commit `cfd67ce78428bf029a42a922bdb202112f77ce07`;
- repaired wrapper blob `b6ac5d8ba4472b04efedb4b1a732980428cf4c82`;
- resume workflow/head commit `85eb20e70a9fa6d8d444aaaf368dd396e164769c`;
- research-log commit `c731d499413739c7be38382242547599f16ce852`.

Live Actions reconciliation:

- workflow/run: Exp073FU `34103803637`;
- event: one-shot `push`;
- head: `85eb20e70a9fa6d8d444aaaf368dd396e164769c`;
- hosted launch audit job `101684090730`: SUCCESS;
- home-science job `101684145754`: IN_PROGRESS;
- active step: `Run frozen WW_S1_S3 A/B gate with durable checkpoints`;
- checkpoint root remains `~/.cache/dsir/exp073fu-ww-s1-s3-filebacked-ab-v0-1` with A/B durable checkpoint trees;
- queued DSIR workflow runs at reconciliation: 0;
- in-progress DSIR workflow runs at reconciliation: exactly 1 (`34103803637`).

No duplicate heavy run was launched and no partial numerical output was inspected.

## Trigger safety

The default-branch Exp073FU workflow currently still contains the temporary path-scoped push trigger used to start this resume. Do NOT edit that workflow while run `34103803637` is active unless a mechanism is in place to prevent/cancel the resulting duplicate. Repository/doc-only commits do not match that path filter and are safe. Restore dispatch-only semantics prospectively after the active run reaches a safe terminal/authority transition, without allowing a competing heavy computation.

## Exact next action

1. While `34103803637` is IN_PROGRESS, do not duplicate it and do not inspect partial numerical output.
2. On terminal state, consume jobs/logs/artifact in the same iteration.
3. Verify artifact digest, checkpoint identities, restored-versus-new stage provenance, ordered `[1,3] = S1->S3`, distinct fields, frozen source/contract/implementation identities, exact file-backed proof, canonical `<f8 [39,12288] EE<-EE`, finiteness and exact A/B equality.
4. Workflow SUCCESS alone is not scientific PASS.
5. Only a fully validated FU candidate permits the frozen Exp073FV provenance-admission gate; only FV may create `WW_S1_S3` authority.
6. On infrastructure/software failure, preserve valid durable checkpoints, diagnose the first causal failure and repair only prospectively. On exact numerical mismatch under the frozen contract, classify scientific FAIL without tolerance rescue.
