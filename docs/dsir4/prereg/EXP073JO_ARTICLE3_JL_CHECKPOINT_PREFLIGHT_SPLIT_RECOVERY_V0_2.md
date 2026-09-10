# Exp073JO — split exact-build preflight recovery v0.2

Date frozen: 2026-09-10. Scope: DSIR Article III / Exp073JO infrastructure only.

Status: PROSPECTIVELY FROZEN AFTER THE FIRST JO PREFLIGHT WAS EXTERNALLY INTERRUPTED AND BEFORE ANY VALID JO PREFLIGHT RESULT OR JL NUMERICAL RESULT EXISTS.

## Triggering failure
Exp073JO v0.1 preflight run/job `34504474368 / 102963111387`, head `374184d1b2e9f31628ab930bc271951569ce2bf9`, passed prereg/static guards, frozen numerical stack, exact pinned CLASS-IV capacity/parser patch and build. During the combined exact history-independence/cache-roundtrip step, at `2026-09-10T17:03:11Z`, the GitHub-hosted runner received an external shutdown signal and the operation was cancelled. No assertion failure, CLASS traceback, preflight result JSON, or scientific artifact was produced.

This event is `INVALID_INFRA_PLUS_0_PLUS_0`. It is not a negative history-independence result and has no scientific effect.

## Minimal process repair
The exact already-frozen controls are unchanged, but they are split into independent hosted jobs so no single control job needs to keep one hosted runner alive for the combined duration.

The three required control parts are:
1. `history_slot10`: exact v0.1 history-independence control for inherited suite slot 10 only;
2. `history_slot20`: exact v0.1 history-independence control for inherited suite slot 20 only;
3. `cache_roundtrip_slot10`: exact v0.1 cache miss->hit byte/audit roundtrip control for slot 10 only.

Each part MUST use the exact pinned CLASS-IV commit/build compatibility and public d_m exposure patch, frozen JL guarded lattices, baseline/precision inputs, native kpd=20, h=1e-4, and the same fixed v0.1 z/target values already encoded in `ci/exp073jo_article3_jl_durable_response_checkpoint_recovery_v0_1.py`:
- history pre-z `0x1.3851eb851eb85p-1` and tail-z `0x1.1c28f5c28f5c3p+0`;
- history pre-target decimal values `[0.0013,0.0047,0.013,0.041]` and tail targets `[0.0019,0.0073,0.021,0.057]` as exact binary64 values produced by the existing code;
- roundtrip z `0x1.a8f5c28f5c28fp-1` with targets `[0.0016,0.0081,0.023,0.052]` as exact binary64 values produced by the existing code.

No target, redshift, tolerance, equality rule, model, grid, parser/capacity, or solver identity may be changed after seeing a part result.

## Part decisions
A history part passes only with exact `np.array_equal` equality of the trailing `<f8` response arrays and identical finite/nonzero pattern between history and fresh suites for its frozen slot.

The roundtrip part passes only with exact response byte equality, exact dynamic audit restoration, exactly one cache miss and one cache hit, and no checkpoint schema/hash mismatch.

Any assertion/numerical mismatch is a valid negative infrastructure result for checkpoint replay and forbids JO heavy recovery. External runner shutdown/cancellation remains infrastructure interruption and may be retried only for the affected unchanged part.

## Aggregation
A v0.2 JO preflight PASS authority requires all three part artifacts from the same workflow contract version, each independently hash-verified, plus a hosted aggregation step that checks exact part identities and produces one aggregate JSON. Workflow green alone is insufficient.

The aggregate may be classified `DURABLE_RESPONSE_CHECKPOINT_PREFLIGHT_PASS_PLUS_0_PLUS_0` only if all three required part classifications are PASS. It remains process-only `+0/+0`, with `scientific_authority_created=false` and `covariance_restriction_authorized=false`.

## Tested recovery-wrapper binding
The recovery wrapper itself remains unchanged from the v0.1 tested code and MUST retain Git blob SHA `aa4c544c1e3e81137010fcdbd34f20567e1eb894`. If that wrapper changes, this split preflight no longer authorizes heavy recovery without a new preflight version.

## Unchanged science
Exp073JL science remains untouched: guarded 2049->4097 requested nodes, centered-cubic ln(k), native kpd=20 for both inherited slots, h=1e-4, REL_TOL=1e-3, exact Exp073IR traversal/support, no covariance/Wm_S3 authorization. This split is an execution-only repair and cannot alter JL classification.
