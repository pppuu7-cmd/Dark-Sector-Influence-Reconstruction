# DSIR immutable recovery — Exp073FL S1S1 driver-generation static audit PASS while Exp073FG runs

Date: 2026-09-06. Scope: DSIR only. RTK/RQIR excluded.

## Preserved science authority

No scientific authority changed in this iteration. Preserved admitted WW authority remains `WW_S0_S0`, `WW_S0_S1`, `WW_S0_S2`. Current numerical frontier remains Exp073FG `WW_S0_S3` run `34034377795`, head `4a02952ee3bcb368a088d87608f61243cd9f7056`; home job `101489679508` remains in progress in the frozen S0-to-S3 A/B science step. Partial numerical output was not inspected. `DSIR-HOME-PC` remains exclusively owned by that job and no competing self-hosted workload was launched.

## Exp073FL frozen support contract

Preregistration remains immutable: `experiments/073fl_ww_s1_s1_driver_generation_static_audit_v0_1_prereg.md`, blob `e578cac17048f73193ff73c97ca38cb1d644d202`, creation commit `8b59dd08cd79af594198b038bd96bd69910cab5f`.

Hosted workflow added at commit `dc7d59400664bedf2f197fe43b6bdc9a8cc378e1`. It binds Exp073FH/FJ/FK frozen same-field semantics and hardened Exp073FG implementation blobs, compiles a deterministic non-science S1S1 contract skeleton, verifies exactly one authoritative S1 reconstruction, exactly one spin-2 field construction, exact same-object coupling handoff, dedicated future S1S1 checkpoint identities, absence of stale S0/S2/S3 and tolerance/rescue semantics, and synthetically rejects an equal-but-distinct second-field mutation.

## Historical first run — implementation-static FAIL +0/+0

Exp073FL run/job `34043934290 / 101515496355`, head `25ef2ecccac9e79a3de1395b31cf7402e52c6277`, completed FAILURE before any science. The first causal failure was an over-strict textual assertion in the hosted audit: it required unformatted literals `[0,3]/S0->S3` and `[1,1]/S1->S1`, whereas the immutable Exp073FK prereg records the same frozen transformation with markdown separators/backticks: `cross source pair [0,3] / S0->S3 -> auto pair [1,1] / S1->S1`. Classification: `IMPLEMENTATION_STATIC_FAIL_PLUS_0_PLUS_0`. No numerical workspace, no self-hosted computation, and no authority creation occurred.

Minimal prospective repair commit: `37180c62451731e87bf7e1f2ea17892da5d28070`. The only change was to bind the exact immutable Exp073FK formatting; no science criterion, source index, arithmetic, storage semantics, tolerance, checkpoint rule or authority boundary changed. Reactivation commit: `cdbcf0019df9ef6ec9b71abc32dc12bee2ff0579`.

## Repaired run — exact support PASS +0/+0

Exp073FL repaired run/job `34043987159 / 101515646656`, head `cdbcf0019df9ef6ec9b71abc32dc12bee2ff0579`, completed SUCCESS. Raw job log was inspected and contains exactly:

- `PASS_EXP073FL_WW_S1_S1_DRIVER_GENERATION_STATIC_AUDIT_V0_1`
- `classification=SUPPORT_PLUS_0_PLUS_0`
- `ww_s1_s1_authority_created=false`
- `self_hosted_science_started=false`

Therefore Exp073FL is CLOSED as hosted static/support PASS `+0/+0`. Workflow success is not scientific PASS and creates no `WW_S1_S1` authority. It only qualifies the deterministic future same-field driver-generation boundary; a future production driver/home envelope remains forbidden until Exp073FG is terminal and fully consumed.

## Current process and next permitted action

Authoritative heavy process remains Exp073FG `34034377795 / 101489679508`, head `4a02952ee3bcb368a088d87608f61243cd9f7056`, state IN_PROGRESS. Exact current durable checkpoint stage remains `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING` by anti-bias policy.

On Exp073FG terminal state, consume raw artifact/job evidence immediately: verify independent ZIP SHA256, six-stage/prune provenance, source/contract/R1/driver/patch identities, regular-file-backed MCM size `19,327,352,832` bytes plus `/proc/self/maps`, canonical `<f8 [39,12288]` `EE<-EE`, exact A/B SHA and `numpy.array_equal`, finiteness and no rescue. Candidate PASS alone cannot create `WW_S0_S3` authority; a separate prospectively frozen provenance-admission gate remains mandatory.
