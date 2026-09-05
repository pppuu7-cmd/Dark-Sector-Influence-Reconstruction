# Exp073DT terminal provenance gap audited; Exp073EB armed

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Live authority at audit time
Exp073DT run `33940588308`, attempt 4, hosted preflight `101288015425` is SUCCESS and self-hosted science job `101288014666` remains QUEUED. Frozen workflow head remains `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`; source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`. No competing heavy DSIR process was launched.

## Prospective provenance audit finding
Before any attempt-4 terminal science output exists, source review found that the frozen DQ driver's `validated_finished()` fast path accepts a completed replica after validating `replica_receipt_complete`, receipt SHA and selected-EE SHA, without rereading every earlier checkpoint-stage manifest. The Exp073DT terminal classifier independently recomputes exact A/B selected-payload equality, size, finiteness and SHA flags, but its terminal artifact package contains only the final replica receipts and selected payloads, not all six stage manifests.

The frozen Exp073DT preregistration, however, requires all source/contract/component/checkpoint provenance checks and stage-order verification to pass. Therefore workflow SUCCESS or the frozen PASS token alone cannot satisfy the complete provenance clause. This is a support/governance evidence gap, not a scientific arithmetic result and not a reason to alter the already frozen Exp073DT computation.

## Prospective repair without changing frozen science
Exp073EB was preregistered in commit `664aab881b898cef2b0e4eebf2043aed2bc28138` as support-only `+0/+0` terminal provenance audit. Event-driven workflow was added in commit `00d2a3c94511486af56867a6218192f28866ee5c`.

Exp073EB:
- triggers only on completion of the named Exp073DT workflow;
- proceeds to self-hosted provenance reread only for exact upstream run `33940588308`, head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`, conclusion `success`;
- acquires the same Exp073DT flock and fails closed on competing self-hosted runs;
- performs no `compute_coupling_matrix`, no WW adapter execution, no checkpoint regeneration and no science arithmetic;
- rereads the complete ordered six-stage chain for A and B, verifies exact identities, canonical S0 SHA, workspace SHA chain, full-window and selected-EE SHA/shape/size, terminal receipt SHA and cross-stage selected-EE consistency;
- writes evidence only under runner temp and uploads it;
- can emit only support token `PASS_EXP073EB_EXP073DT_FULL_CHECKPOINT_PROVENANCE_AUDIT_V0_1` with `science_gate_scored=false` and `ww_s0_s0_authority_created=false`.

Hosted-only Exp073EC static governance audit was added in commit `c9014c2763e542f22aa5c01583e5e8011ccdf7b7`. Run/job `33962004169 / 101295382699` completed SUCCESS and raw log emitted `PASS_EXP073EC_EXP073EB_STATIC_GOVERNANCE_AUDIT_V0_1`. This validates the support-only/fail-closed/no-recompute structure; it creates no science authority.

## Authority consequence
If Exp073DT later succeeds scientifically, `WW_S0_S0` must not be admitted from workflow status or token alone. Normal terminal artifact consumption must independently verify A/B exact equality and frozen receipt fields, and full checkpoint provenance must also be verified by Exp073EB PASS or an equivalently strict direct reread of the durable root. If Exp073DT is scientific FAIL, Exp073EB cannot rescue it. If Exp073DT is infrastructure incomplete, Exp073EB does not run its self-hosted evidence job.

## Exact next action
Keep `DSIR-HOME-PC` reserved for Exp073DT attempt 4 while job `101288014666` is queued/in_progress. On terminal SUCCESS, consume the Exp073DT artifact and the automatically chained Exp073EB provenance evidence before creating any `WW_S0_S0` authority. On terminal infrastructure failure, diagnose the first cause and preserve verified stages; do not reinterpret as science.
