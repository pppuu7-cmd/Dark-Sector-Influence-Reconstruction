# Exp073DT attempt 3 — same frozen checkpoint-preserving resume dispatched

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

After attempt 2 terminated by external runner shutdown (`2026-09-05T07:49:54Z`) with no terminal artifact, live Actions reconciliation showed `0 in_progress / 0 queued`. A direct single-job rerun request was blocked by the connector/runtime before GitHub execution; no alternate workflow was created.

A subsequent supported `rerun failed jobs` request on the same original run `33940588308` succeeded. This did not create a new workflow, new science implementation, new head, or competing DSIR control plane. It created run attempt 3 under the exact same frozen workflow/head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`.

Attempt 3 identities at dispatch:
- run `33940588308`, attempt `3`;
- hosted preflight job `101274119122`: SUCCESS;
- self-hosted science job `101274118640`: QUEUED at latest reconciliation;
- frozen source authority head `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`.

Checkpoint policy is unchanged: only complete stage state whose namespace, source head, contract fingerprint and payload hashes validate exactly may be restored. Interrupted/incomplete stages must recompute. Any malformed/mismatched state fails closed. Scientific arithmetic, DES domain, `EE<-EE` semantics, 39x12288 canonical payload, OpenMP=8 and no-tolerance rule remain frozen.

Runner ownership is RESERVED BY Exp073DT attempt 3 while job `101274118640` is queued/in progress. Do not launch a competing self-hosted DSIR task.

On terminal completion, consume raw artifact/digest, terminal receipt, A/B selected payloads, comparator, replica receipts and checkpoint provenance before classifying. Workflow success alone is not scientific PASS.
