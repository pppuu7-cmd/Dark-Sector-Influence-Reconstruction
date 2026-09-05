# Exp073DT attempt 3 external runner shutdown; same frozen attempt 4 dispatched

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Classification of attempt 3
Run `33940588308`, attempt 3, self-hosted job `101274118640` terminated before scientific completion. Raw decoded job log shows:

- runner `DSIR-HOME-PC`, machine `win-ws338`;
- frozen workflow head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`;
- frozen source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- live exclusivity PASS;
- PyMaster 2.7 PASS;
- runtime `DSIR_OMP_TEAM=8` PASS;
- first causal failure at `2026-09-05T09:27:06Z`: `The runner has received a shutdown signal`;
- science step conclusion CANCELLED;
- terminal science evidence upload SKIPPED.

Therefore attempt 3 is `INFRASTRUCTURE_INCOMPLETE +0/+0`, not scientific FAIL and not resource/performance FAIL. No Wm or WW scientific authority changes.

## Checkpoint preservation
Durable root remains `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`. Existing frozen driver semantics remain authoritative: only complete stage payloads whose identity/provenance/hashes verify may restore; interrupted or incomplete stages recompute; malformed or mismatched state fails closed. No verified expensive stage is intentionally recomputed.

## Noncompetition reconciliation and resume
After attempt 3 became terminal, repository-wide live Actions reconciliation showed `0 in_progress / 0 queued`. No competing self-hosted DSIR workload existed. The failed self-hosted job of the same original frozen run was re-run; no new workflow, science implementation, arithmetic, tolerance, domain, or provenance rule was created.

Current attempt 4:
- run `33940588308`;
- hosted preflight job `101288015425`: SUCCESS;
- self-hosted science job `101288014666`: QUEUED at dispatch reconciliation;
- frozen head/source/contract/durable root unchanged;
- expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`;
- runner ownership: `DSIR-HOME-PC RESERVED BY Exp073DT attempt 4` while queued/in_progress.

## Exact next action
When `101288014666` becomes terminal, consume raw logs and artifacts in the same iteration. A scientific PASS requires the frozen token plus independently verified A/B selected `EE<-EE` canonical `<f8 [39,12288]` whole-file SHA equality and `numpy.array_equal=true`, valid replica receipts and checkpoint provenance, with no tolerance rescue. Exact A/B inequality is scientific repeatability FAIL. Infrastructure/runtime/checkpoint/provenance/artifact failures remain `+0/+0` and trigger diagnosis/resume rather than scientific reinterpretation.
