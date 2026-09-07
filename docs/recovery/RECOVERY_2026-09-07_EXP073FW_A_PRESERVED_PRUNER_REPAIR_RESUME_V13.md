# DSIR immutable recovery — Exp073FW Replica-A preserved, pruner repair, checkpoint-first resume V13

Date: 2026-09-07. Scope: DSIR only; RTK/RQIR excluded.

All previously admitted Wm/WW authority remains unchanged. `WW_S2_S2` remains NOT ADMITTED. Exp073GV remains hosted support PASS `+0/+0` exactly as recorded in V12.

## Terminal-consume of Exp073FW run 34125785882

Run `34125785882`, head `1c635f5192d26e76e0ec82a308363b666e5a248b`, completed FAILURE. Hosted launch audit job `101754018941` was SUCCESS; home job `101754061309` failed; provenance-admission job `101785905987` was correctly skipped. The first causal failure in the home log was post-compute verifier/pruner infrastructure:

`RuntimeError: fail-closed missing FW pruner token 'WW_S1_S1'`

The failed run therefore classifies as `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, not scientific arithmetic FAIL. No `WW_S2_S2` authority was created.

Compact evidence artifact id `10023848524` was independently downloaded and its ZIP SHA256 recomputed exactly as `33b5999213247a9ad0c66957a021067f4f790f04d19eb1cf8d88910187eea66f`, equal to GitHub's artifact digest.

## Preserved complete Replica A

The independently inspected artifact contains a complete durable A chain through `replica_receipt_complete`; B is absent. Preserved A identities:

- checkpoint namespace `checkpoints/exp073fw-ww-s2-s2-a-v0-1`;
- schema `dsir.exp073fw.ww_s2_s2.durable_ab_production.v0.1.checkpoint`;
- source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- ordered source indices `[2,2]`, `same_source_map_both_sides=true`, reconstruction counts `{'s2':1}`;
- field construction count `1`, identical field object ids on both sides, `same_field_object_handoff=true`;
- source-map SHA256 both sides `a4d96a32c72553b8f1c7704b745987f6f517a51fc78b628ea76fa9a669c6ef75`;
- workspace FITS SHA256 `dd51925859c5b8efdcde25d396bd44b276245dc4ec53f7ec3777485858f94e09`;
- exact file-backed MCM proof `19,327,352,832` bytes with public route `get_bandpower_windows_after_filebacked_fits_read` and full shape `[4,39,4,12288]`;
- full-window SHA256 `4a266e345911a4b6ed0b756bced2c94017ab39de1538fdd59e1eaa961690a511`;
- selected semantics `wins[0,:,0,:] = EE<-EE`, shape `[39,12288]`, `<f8` by frozen receipt;
- selected `selected_ee.bin` size `3,833,856` bytes and independently recomputed SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`, exactly matching all A receipts;
- `historical_ww_numerical_import=false`, `other_replica_output_read=false`, `science_gate_scored=false`.

Thus the expensive A stage is durably complete and must not be recomputed unless its fail-closed chain later fails verification. Scientific A/B equality is not yet scoreable because B does not yet exist.

## Root cause and prospective repair

The frozen FM base does not contain uppercase lexical token `WW_S1_S1`; it expresses the relevant frozen identities through lowercase schema/path tokens and explicit `S1->S1`, `[1,1]`, count-map and receipt invariants. The FW transformer incorrectly required the nonexistent uppercase token.

Another reconciled DSIR process applied the smallest prospective repair in commit `2a6a06f9d468879ca814ced15a56f82169507b3a`, removing only the nonexistent mandatory lexical token while retaining all actual transform/invariant/stale-token checks. Repaired pruner blob: `fb66e67d88a90b093a7da8b42ab0ac6fee13b504`. Workflow binding commit: `f7e925e782983824b7e916ce8437fcf924ec5760`, workflow blob `c7c651dfeac8a9d4a2d3da1dd6b11d7873af612a`. Frozen arithmetic, contract, source pair, thresholds, exact comparator and domain are unchanged.

## Authoritative current process

The workflow-binding push started exactly one recovery run: Exp073FW `34135965569`, head `f7e925e782983824b7e916ce8437fcf924ec5760`. Hosted audit job `101786894169` raw-validated SUCCESS with exact token `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5` and `classification=SUPPORT_PLUS_0_PLUS_0`; home job `101786993129` is IN_PROGRESS at this recovery point. No competing heavy run was observed.

Resume policy is checkpoint-first: verify and reuse complete Replica A, then compute only missing B / terminal comparison. Do not infer scientific PASS/FAIL from A alone. Only a complete candidate passing frozen provenance admission in Exp073FX may create `WW_S2_S2` authority.

The current FW workflow still has a path-scoped one-shot push trigger. Do not edit that workflow while `34135965569` is active because the old trigger could launch a duplicate. Restore dispatch-only semantics only at a safe terminal transition.
