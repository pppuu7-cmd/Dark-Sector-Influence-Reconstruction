# DSIR AutoGuard turn 11 — Exp073FW terminal comparator failure and repair

Date: 2026-09-07. Scope: DSIR only.

Exp073FW recovery run `34135965569`, head `f7e925e782983824b7e916ce8437fcf924ec5760`, became terminal FAILURE during this turn. Hosted audit job `101786894169` had succeeded; home job `101786993129` failed only after both replica chains were complete; hosted provenance admission `101817055237` was correctly skipped.

Raw home log showed `PASS_EXP073FW_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1` and `PASS_EXP073FW_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`, then the first causal exception in `ci/exp073fw_compare_terminal_receipts_v0_1.py`: `RuntimeError: fail-closed receipt identity mismatch A:checkpoint_namespace`.

Artifact `10027545256` was downloaded independently. GitHub digest and locally recomputed ZIP SHA256 both equal `0be01af5b522821fcdcd52be9fb2ef4ae5849efd2c4e439b9d7ad8462765cfb4`. It contains complete A and B durable chains plus both canonical selected arrays. A and B `selected_ee.bin` are each 3,833,856 bytes, SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`, shape `<f8 [39,12288]`; independent exact comparison gave `numpy.array_equal=true`, all finite, max absolute difference `0.0`.

Both receipts bind `source_pair=S2->S2`, `ordered_source_indices=[2,2]`, `same_field_object_handoff=true`, frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, and exact file-backed MCM proof `19,327,352,832` bytes. Actual checkpoint namespaces are `checkpoints/exp073fw-ww-s2-s2-a-v0-1` and `...-b-v0-1`.

The comparator wrapper transformed `exp073fm->exp073fw` and underscore `ww_s1_s1->ww_s2_s2` but omitted the hyphenated namespace transform `ww-s1-s1->ww-s2-s2`; therefore it expected stale S1S1 namespace strings and failed before scoring exact A/B equality. Classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`; no WW_S2_S2 authority created and no scientific FAIL recorded.

Minimal prospective repair commit `ced70da68cd148cfba4c7dec33b8140989557bee` adds only the missing hyphenated transform and explicit correct/stale namespace invariants. Repaired comparator blob is `b5b828bd71eaf6da360c8ebfa279888165531e49`. No frozen arithmetic, source semantics, domain, tolerance policy or acceptance criterion changed.

Workflow binding/static regression commit `3835072cf580fc0a0950794385c028012f60a5cb` freezes the repaired blob and audits both A/B namespace literals. It launched exactly one recovery run `34145888831`. Hosted audit job `101817723744` raw-validated `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_6`, classification `SUPPORT_PLUS_0_PLUS_0`; home job `101817765818` is in progress under the same durable checkpoint namespace.

The recovery run must reuse both completed replicas and perform only fail-closed verification/terminal comparison as needed. `WW_S2_S2` remains NOT ADMITTED until the run completes and frozen Exp073FX provenance admission succeeds.