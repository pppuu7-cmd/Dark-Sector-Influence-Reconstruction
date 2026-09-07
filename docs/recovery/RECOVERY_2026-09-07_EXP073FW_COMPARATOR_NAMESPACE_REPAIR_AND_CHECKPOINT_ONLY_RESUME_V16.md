# DSIR recovery V16 — Exp073FW comparator namespace repair and checkpoint-only resume

Date: 2026-09-07. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved authority

All earlier admitted DSIR authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`. `WW_S2_S2` remains **NOT ADMITTED**.

## Terminal Exp073FW run 34135965569

Run `34135965569`, head `f7e925e782983824b7e916ce8437fcf924ec5760`, completed FAILURE. Hosted audit job `101786894169` was SUCCESS; home job `101786993129` failed after both replicas completed; provenance admission `101817055237` was skipped.

Raw log proves both `PASS_EXP073FW_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1` and `PASS_EXP073FW_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`. First causal failure is terminal comparator exception `fail-closed receipt identity mismatch A:checkpoint_namespace`.

Artifact `10027545256` was independently downloaded and verified. GitHub digest and recomputed ZIP SHA256 both equal `0be01af5b522821fcdcd52be9fb2ef4ae5849efd2c4e439b9d7ad8462765cfb4`. The artifact contains complete A and B durable chains. Both canonical `<f8 [39,12288] EE<-EE` payloads are 3,833,856 bytes and SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`; independent exact array comparison is true, both arrays are finite, max absolute difference is `0.0`.

Both receipts preserve frozen `S2->S2`, ordered `[2,2]`, same-field handoff, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, public EE route, and exact `19,327,352,832`-byte file-backed MCM proof.

This run is **INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0**, not scientific FAIL and not scientific PASS, because the frozen terminal comparator did not complete and Exp073FX did not admit authority.

## First cause and minimal repair

`ci/exp073fw_compare_terminal_receipts_v0_1.py` transformed `exp073fm->exp073fw`, underscore `ww_s1_s1->ww_s2_s2`, source-pair and indices, but omitted hyphenated checkpoint namespace `ww-s1-s1->ww-s2-s2`. Thus transformed comparator expected stale `checkpoints/exp073fw-ww-s1-s1-{a,b}-v0-1` instead of actual `checkpoints/exp073fw-ww-s2-s2-{a,b}-v0-1`.

Minimal prospective repair commit `ced70da68cd148cfba4c7dec33b8140989557bee`; repaired comparator blob `b5b828bd71eaf6da360c8ebfa279888165531e49`. It adds only the missing hyphenated transform plus fail-closed correct/stale namespace assertions. Frozen science arithmetic, source semantics, domain, tolerances, threshold policy and acceptance criteria are unchanged.

Workflow binding/static regression commit `3835072cf580fc0a0950794385c028012f60a5cb` freezes the repaired comparator and explicit A/B namespace audit. The path-scoped trigger launched exactly one recovery run.

## Authoritative current process

Exp073FW recovery run **`34145888831`**, head **`3835072cf580fc0a0950794385c028012f60a5cb`**.

- hosted audit job **`101817723744`**: SUCCESS; raw token `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_6`; support `+0/+0`;
- home job **`101817765818`**: IN_PROGRESS at latest reconciliation;
- runner owner: `DSIR-HOME-PC-2` / `win-ws338`;
- durable root unchanged: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- both A and B are already complete and independently verified from artifact `10027545256`; no expensive replica may be recomputed unless fail-closed restore verification rejects its checkpoint.

Exact next action: terminal-consume run `34145888831`. Verify raw comparator output, checkpoint restore provenance, exact A/B equality and the uploaded artifact digest. Only if the frozen candidate completes successfully may Exp073FX provenance admission create `WW_S2_S2` scientific authority. On implementation/infrastructure failure preserve both complete replicas and repair only the first causal defect.

## C2 reconciliation preserved

Exp073GY run `34141294357 / 101803642167` remains validated `SUPPORT_PLUS_0_PLUS_0` only. It creates no scientific record-set/model authority. The next meaningful C2 step remains real 28-packet runtime generation/admission and must not compete with the active FW home process.

## Frozen boundaries

All global frozen boundaries and no-rescue rules from V15 remain unchanged.