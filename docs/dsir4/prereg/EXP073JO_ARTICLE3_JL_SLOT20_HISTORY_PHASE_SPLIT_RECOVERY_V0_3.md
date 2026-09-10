# Exp073JO — slot20 history-control phase-split recovery v0.3

Date frozen: 2026-09-10. Scope: DSIR Article III / Exp073JO infrastructure only.

Status: PROSPECTIVELY FROZEN AFTER TWO EXTERNAL `history_slot20` HOSTED-RUNNER SHUTDOWNS AND BEFORE ANY VALID SLOT20 HISTORY-INDEPENDENCE RESULT OR JL NUMERICAL RESULT EXISTS.

## Triggering infrastructure failures

The original combined JO v0.1 preflight was externally interrupted before any result. JO split-v0.2 then preserved exact PASS artifacts for `history_slot10` and `cache_roundtrip_slot10`, but the unchanged `history_slot20` part was externally interrupted twice:

- run `34506027292`, job `102968325017`: hosted runner shutdown during exact numerical control, no result/artifact;
- unchanged failed-job retry, job `102985819424`: hosted runner shutdown at `2026-09-10T18:02:14Z` during exact numerical control, no result/artifact.

Both events are `INVALID_INFRA_PLUS_0_PLUS_0`, not negative history-independence evidence. No slot20 response value from either failed attempt exists in an admitted artifact.

## Preserved v0.2 exact PASS receipts

The following independently verified v0.2 parts remain valid and MUST be reused rather than recomputed:

1. `history_slot10`: artifact `10164136352`, ZIP SHA256 `0a06f375ba59f4da33172d3d9f742af7b29c82263c600c2e7696fd6676af41cc`, `part_result.json` SHA256 `a85061de4d6b1d0953b60fdc083389a7fc6851100fc8e1b3a310fc7b5c8a1c55`, classification `HISTORY_INDEPENDENCE_PART_PASS_PLUS_0_PLUS_0`.
2. `cache_roundtrip_slot10`: artifact `10164156389`, ZIP SHA256 `5facd22fbf6edca62b0ff37e7457d411d232525aeead20738de8cb68c9bca735`, `part_result.json` SHA256 `275683c8f3c03eda9656e96f1b8124a91c5d25291b1940002b075e61f2ae5046`, classification `CACHE_ROUNDTRIP_PART_PASS_PLUS_0_PLUS_0`.

Both bind wrapper Git blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894` through the v0.2 workflow identity guard. Reusing these successful receipts is process persistence only and cannot add scientific weight.

## Minimal v0.3 repair

Only the still-missing original `history_slot20` control is decomposed into two independent compute receipts so one hosted runner need not contain both expensive suite constructions.

The original mathematical decision is unchanged. Frozen slot20 settings remain:

- inherited slot `20`, native CLASS `k_per_decade_for_pk=20`;
- guarded JL fine lattice: base N=4096 plus one response-blind upper guard, exactly 4097 requested nodes;
- capacity 4608; parser capacity 131072;
- pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c` with the same build-compat and public `d_m` exposure patches;
- exact baseline and precision inputs;
- history pre-z `0x1.3851eb851eb85p-1` and pre-target binary64 values produced from `[0.0013,0.0047,0.013,0.041]`;
- tail-z `0x1.1c28f5c28f5c3p+0` and tail-target binary64 values produced from `[0.0019,0.0073,0.021,0.057]`;
- h=1e-4, REL_TOL=1e-3, centered-cubic ln(k) response engine unchanged.

### Receipt A — `slot20_after_history`

Construct one otherwise ordinary frozen slot20 `ResolutionSuite`. Execute the exact pre-query `response(pre_z, pre_targets)`, then the exact trailing `response(tail_z, tail_targets)` on the SAME suite. Persist the trailing response as exact contiguous little-endian `<f8` bytes with shape `(4,2)`, nbytes 64, SHA256, exact finite mask and exact positive mask. No response transformation is allowed.

### Receipt B — `slot20_fresh_tail`

In an independent clean hosted process/build, construct one otherwise identical fresh frozen slot20 `ResolutionSuite`, execute ONLY `response(tail_z, tail_targets)`, and persist the trailing response under the same exact byte/shape/mask rules.

A fresh suite need not share the Python process with Receipt A: the original JO prereg requires a "fresh otherwise identical suite without those earlier queries" and does not require process co-residency. Process separation strengthens freshness while leaving the compared solver call and equality criterion unchanged.

## Hosted aggregation / exact decision

A hosted v0.3 aggregate MUST:

1. verify exact artifact IDs, ZIP SHA256 and inner JSON SHA256 for the two preserved v0.2 PASS receipts above;
2. verify both new slot20 receipts bind the same v0.3 contract, wrapper blob, exact frozen lattice/node SHA, z/target identities, response shape/dtype/nbytes and pinned numerical constants;
3. reconstruct both slot20 trailing arrays exactly from persisted `<f8` bytes;
4. apply the unchanged v0.2 decision:
   - `np.array_equal(after_history, fresh_tail)` must be true;
   - finite masks must be exactly equal;
   - positive masks must be exactly equal;
5. fail closed on any artifact/hash/shape/provenance/order mismatch.

Raw-byte equality may additionally be reported but MUST NOT replace `np.array_equal`, because identical NaN payload bytes would not satisfy the original array-equality rule.

Only if all preserved v0.2 controls and reconstructed slot20 control PASS may the aggregate emit:

`DURABLE_RESPONSE_CHECKPOINT_PREFLIGHT_PASS_PLUS_0_PLUS_0`

under schema `EXP073JO_ARTICLE3_JL_DURABLE_RESPONSE_CHECKPOINT_PREFLIGHT_RESULT_V0_3`.

The aggregate remains process-only `+0/+0`, `scientific_authority_created=false`, `covariance_restriction_authorized=false`.

## Wrapper/science identity

The tested recovery wrapper MUST remain Git blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894`. Frozen Exp073JL science remains guarded 2049->4097 nodes, centered-cubic ln(k), native kpd=20, h=1e-4, REL_TOL=1e-3, exact Exp073IR traversal/support. No covariance, Wm_S3, nuisance, relation/null or model-selection read is authorized.

## Anti-rescue

This v0.3 change is execution decomposition only. It may not alter target/redshift values, lattice density, solver, interpolation, finite-difference definitions, tolerance, masks, domain, atom inclusion, rounding, averaging, clipping, denominator treatment or scientific classification logic. Any such change requires a new scientific preregistration and cannot inherit JO preflight authority.
