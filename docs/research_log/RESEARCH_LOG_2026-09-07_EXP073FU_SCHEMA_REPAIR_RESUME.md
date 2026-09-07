# DSIR research log — Exp073FU schema repair and checkpoint resume

Date: 2026-09-07
Scope: DSIR only.

## Incident classification

Historical Exp073FU `WW_S1_S3` run `34089383137` attempt 2 terminated with workflow conclusion `failure` because the self-hosted `home-science` job `101676974877` stopped in the fail-closed pruner with:

`RuntimeError: fail-closed stage identity fresh_sources_complete`

This occurred before hosted provenance admission. The job still uploaded compact partial evidence as artifact `10010836998` (ZIP digest reported by Actions: `b86f561a485603001ee151b5841a059f17c582418a98e065fabd5cc1ddbf488c`). `hosted-provenance-admission` was skipped. Therefore this is **implementation/infrastructure FAIL, accounting +0/+0**, not a scientific FAIL and not a `WW_S1_S3` result.

The preserved A checkpoint manifest was subsequently audited and shown to have the correct frozen stage identity. The causal defect was the transformed FU pruner omitting the underscore schema transform `ww_s1_s2 -> ww_s1_s3`; no frozen science arithmetic, source/domain semantics, acceptance threshold, tolerance, hypothesis ID, source head, or contract fingerprint was implicated.

## Repair validation

Prospective schema-only pruner repair exists as `ci/exp073fu_verify_and_prune_replica_v0_2.py`, blob:

`b9ed7d7178424fb656b4a7c7bfb2ee370c751cb0`

Read-only validation run `34103206078`, job `101682164394`, completed SUCCESS and emitted both required evidence lines:

- `original_checkpoint_mutated=false`
- `PASS_EXP073FU_REPLICA_A_REPAIRED_PRUNER_READONLY_VALIDATION_V0_6`

It also emitted `PASS_EXP073FU_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`. This permits checkpoint resume but creates no scientific authority.

## Production binding and resume

Production wrapper was prospectively rebound from the defective pruner to the validated repaired pruner only:

- wrapper commit: `cfd67ce78428bf029a42a922bdb202112f77ce07`
- wrapper blob: `b6ac5d8ba4472b04efedb4b1a732980428cf4c82`

No science parameters or frozen gates changed.

The FU workflow was then rebound to the repaired pruner/blob identities and resumed via a one-shot push trigger because no generic workflow-dispatch connector action was available in this guard turn:

- resume workflow commit/head: `85eb20e70a9fa6d8d444aaaf368dd396e164769c`
- active resume run: `34103803637`
- hosted launch audit job: `101684090730` — SUCCESS
- self-hosted home-science job: `101684145754` — IN_PROGRESS at logging time
- predecessor admitted run remains `34067352681` (`WW_S1_S2` authority)

The resume is required to reuse the valid durable checkpoint tree under the same Exp073FU checkpoint root; it must not intentionally repeat completed heavy stages. No second heavy run is permitted while `34103803637` is active.

## Scientific status

- `WW_S1_S3`: **NOT YET ADMITTED**.
- Run `34089383137` failure: **infrastructure/implementation +0/+0**, not scientific FAIL.
- Repaired-pruner validation: **support +0/+0**.
- Run `34103803637`: **in progress; no scientific interpretation before terminal artifact and Exp073FV provenance admission**.
- Exact numerical mismatch, if eventually produced by the frozen A/B comparison, remains a scientific FAIL and must not be tolerance-rescued.
- `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, and `OUTSIDE_DOMAIN` remain distinct non-FAIL classifications.

## Next allowed action

Do not start any duplicate heavy run. On terminal success of `34103803637`, independently verify artifact digest, complete checkpoint/provenance chain, exact A/B equality and finiteness, then allow Exp073FV admission and only after authority creation dispatch the next frozen DSIR4 target. On technical failure, preserve durable checkpoints and repair only the first causal infrastructure defect prospectively.
