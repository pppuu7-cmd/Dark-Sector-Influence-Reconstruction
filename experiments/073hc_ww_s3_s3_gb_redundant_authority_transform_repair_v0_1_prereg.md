# Exp073HC — WW_S3_S3 GB redundant authority-token transform repair v0.1 preregistration

Date: 2026-09-08
Classification: SUPPORT_PLUS_0_PLUS_0 / IMPLEMENTATION_REPAIR

## Trigger

Exp073HB hosted static audit run `34168722516` failed while emulating the exact repaired GB transform at the token `ww_s2_s2_authority_created`. This is a deterministic transform-order defect: the earlier required replacement `ww_s2_s2 -> ww_s3_s3` has already converted `ww_s2_s2_authority_created=true` to `ww_s3_s3_authority_created=true`, so requiring the longer old token later in the same sequential transform is impossible.

This is infrastructure/provenance verifier behavior only. No GA numerical result was produced or inspected, and this is not a scientific WW_S3_S3 failure.

## Prospectively allowed repair

Only the following implementation change is allowed:
- remove the now-redundant required pair `ww_s2_s2_authority_created -> ww_s3_s3_authority_created` from the sequential GB replacement list;
- retain the earlier exact `ww_s2_s2 -> ww_s3_s3` replacement, which deterministically performs the authority-key transformation as a substring;
- retain the final explicit invariant requiring `ww_s3_s3_authority_created=true` in the transformed verifier;
- retain the exact pinned FX base verifier blob and all scientific/provenance checks.

No GA driver, pruner, comparator, home wrapper, source ordering, numerical threshold, domain, exact-equality rule, artifact validation rule, or scientific authority condition may change. The GA workflow may change only its `ADMIT_VERIFY_BLOB` binding to the repaired GB verifier blob.

## Required hosted audit

A hosted-only static audit must emulate the repaired sequential transform against the exact pinned FX base and verify:
- both pre-prune proof tokens;
- exact GA A/B PASS and live-exclusivity proof;
- `S3->S3`, `[3,3]`, `{'s3':1}`, same-field handoff;
- 19327352832-byte file-backed MCM and exact adapter route;
- complete stage-manifest SHA binding;
- exact byte equality and finiteness;
- no tolerance/rounding/smoothing/averaging rescue;
- final GB admission token and `ww_s3_s3_authority_created=true`;
- exact repaired GB blob binding in the GA workflow.

It must not use the self-hosted runner, dispatch GA, inspect any numerical WW payload, or create scientific authority.

Required PASS token:
`PASS_EXP073HC_WW_S3_S3_GB_REDUNDANT_AUTHORITY_TRANSFORM_REPAIR_STATIC_AUDIT_V0_1`
