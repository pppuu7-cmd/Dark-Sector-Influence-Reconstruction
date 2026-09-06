# DSIR recovery — Exp073FL prereg while Exp073FG runs

Date: 2026-09-06. Scope: DSIR only; never mix RTK/RQIR.

## Live authoritative process

Exp073FG `WW_S0_S3` remains the only in-progress DSIR workflow: run `34034377795`, head `4a02952ee3bcb368a088d87608f61243cd9f7056`; hosted lineage job `101489652912` SUCCESS; hosted code/checkpoint job `101489652945` SUCCESS; home science job `101489679508` IN_PROGRESS in the frozen ordered `S0->S3` A/B step. `DSIR-HOME-PC` is exclusively owned by job `101489679508`. Exact durable checkpoint stage remains `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`; no partial numerical output was inspected. Live queued DSIR workflow count was checked as zero.

## Newly frozen support

Exp073FL preregistration was created prospectively at commit `8b59dd08cd79af594198b038bd96bd69910cab5f`; file `experiments/073fl_ww_s1_s1_driver_generation_static_audit_v0_1_prereg.md`, blob `e578cac17048f73193ff73c97ca38cb1d644d202`.

Exp073FL is support/static only. It freezes the future `WW_S1_S1` generated-driver qualification boundary established by Exp073FH/FJ/FK: source indices `[1,1]`; reconstruct authoritative S1 exactly once; construct one spin-2 field; reuse the exact same Python field object on both workspace sides; `same_field_object_handoff=true`; reject any stale S0/S2/S3 or cross-pair semantics; preserve the hardened complete-stage/checkpoint/prune evidence architecture and all existing full-resolution numerical/storage semantics; reject tolerance/rescue paths; compile generated code and synthetically reject an equal-but-distinct second-field mutation.

Frozen support token: `PASS_EXP073FL_WW_S1_S1_DRIVER_GENERATION_STATIC_AUDIT_V0_1`. Permitted PASS classification is only `SUPPORT_PLUS_0_PLUS_0`; `ww_s1_s1_authority_created=false`; `self_hosted_science_started=false`.

No Exp073FL workflow or self-hosted S1S1 science was launched in this recovery step. The current Exp073FG result remains blinded while running.

## Exact next actions

1. If Exp073FG becomes terminal, consume it immediately: inspect jobs/logs/artifact; independently verify ZIP SHA256, six-stage/prune evidence, source/contract/R1/driver/patch identities, 19,327,352,832-byte mmap proof, canonical `<f8 [39,12288]` `EE<-EE`, exact A/B identity and finiteness; classify strictly under its frozen contract.
2. Candidate Exp073FG PASS creates no authority; only a separate prospectively frozen provenance-admission gate may admit `WW_S0_S3`.
3. If Exp073FG is still running, continue only independent hosted/static S1S1 preparation. Exp073FL may be implemented/audited hosted-only; never launch a competing home run.
4. Any infrastructure failure must be diagnosed at its first causal defect and repaired minimally without changing frozen science.
