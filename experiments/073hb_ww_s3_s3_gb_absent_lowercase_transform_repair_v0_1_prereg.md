# Exp073HB — WW_S3_S3 GB absent lowercase transform repair v0.1 preregistration

Date: 2026-09-08
Classification: SUPPORT_PLUS_0_PLUS_0 / IMPLEMENTATION_REPAIR

## Trigger

Exp073HA hosted static audit run `34168565710` failed before any scientific execution because the frozen `ci/exp073gb_verify_ga_candidate_v0_1.py` transform requires lowercase token `exp073fw` to exist in the exact pinned FX base verifier blob `eb907944eac68b9fd13c405399cf238a8cb5bc96`. That token is absent from the pinned base. The same requirement would therefore make a future real Exp073GB admission execution fail before reading the GA artifact.

This is an implementation/provenance verifier defect, not a scientific failure and not evidence about WW_S3_S3.

## Prospectively allowed repair

Only the following change is allowed:
- remove the nonexistent lowercase `exp073fw -> exp073ga` replacement from the required GB transform list;
- retain every transformation that is actually present in the exact pinned base and every S3_S3 invariant;
- retain the exact pinned FX verifier base blob;
- retain exact byte equality, finiteness, stage-manifest hashing, file-backed adapter identity, pre-prune proof requirements, live-exclusivity proof, no-tolerance-rescue rule, and all authority semantics;
- update the GA workflow's `ADMIT_VERIFY_BLOB` binding to the repaired GB verifier blob only.

No GA numerical driver, pruner, comparator, home wrapper, source pair, ordering, threshold, domain, or scientific admission criterion may change.

## Required hosted audit after repair

A separate hosted-only static audit must verify the repaired transform against the exact pinned FX base and the rebound GA workflow. It must not use the self-hosted runner, inspect a numerical WW payload, dispatch GA, or create scientific authority.

Required PASS token:
`PASS_EXP073HB_WW_S3_S3_GB_ABSENT_TOKEN_REPAIR_STATIC_AUDIT_V0_1`

Only a later real Exp073GB execution over a valid GA artifact may emit the GB provenance-admission scientific authority token.
