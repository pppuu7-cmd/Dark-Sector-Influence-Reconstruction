# RECOVERY — Exp073EO hosted provenance auditor self-test PASS while Exp073EN remains running

Date: 2026-09-06

## Status
This note is support/provenance only. It does not create `WW_S0_S0` science authority and does not change Article-3 readiness.

Authoritative science process remains Exp073EN run `33994398927`, self-hosted job `101382229273`, still `IN_PROGRESS` at this reconciliation. Partial numerical output was not inspected.

## Auditor frozen before real EN terminal evidence
Prospective admission preregistration remains `experiments/073eo_ww_s0_s0_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`, blob `490e1f44a7d7bb9b42dc00a72e0b39961da1692a`.

Hosted admission auditor:
- `ci/exp073eo_ww_s0_s0_provenance_admission_v0_1.py`
- blob `4403d3e140acd14f0b95a31a8b2851f3229c1da3`
- created before any terminal Exp073EN artifact existed.

Corrected synthetic fixture:
- `ci/exp073eo_make_synthetic_fixture_v0_1.py`
- blob `ce45c34be6aae3914824d0b9cdfb073d2c24f143`.

Self-test workflow:
- `.github/workflows/exp073eo-auditor-selftest-v0-1.yml`
- run/job `34000601753 / 101398655101`
- head `ecd53e0df713ef618666c22ae973a8bf83493549`
- conclusion `SUCCESS`.

## Positive-path proof
A synthetic artifact carrying the exact frozen source authority, contract fingerprint, stage schemas, semantic namespaces, storage identity, local Exp073EM identity, A/B selected shape/dtype/semantics, workspace/prune hash chains, full-resolution mmap log proof and 8-thread downstream proof was admitted with:

`PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1`

This is a self-test token only. It is not an admission of real EN evidence.

## Negative fail-closed proof
After the positive test, the workflow flipped exactly one byte in the synthetic B `selected_ee.bin` and reran the same frozen auditor. The auditor returned exit code 4 and:

`BLOCKED_EXP073EO_PROVENANCE_ADMISSION_V0_1`

The workflow then emitted:

`PASS_EXP073EO_AUDITOR_FAIL_CLOSED_SELFTEST_V0_1`

Thus the auditor demonstrably rejects payload corruption instead of falling back to tolerance, approximate comparison, or metadata-only trust.

## Historical self-test repair
The preceding self-test run `34000555575 / 101398530716` correctly blocked its nominal positive fixture because the fixture itself contained a typo in the frozen contract fingerprint (`...ce4bd...` instead of the authoritative `...ce4bc2bd...`). The science contract and auditor were not weakened. Only the synthetic fixture was corrected and rebound by blob before rerun.

## Admission architecture
Exp073EO can be hosted-only. The Exp073EN compact collector copies all JSON provenance/checkpoint records under the science root, A/B selected payloads, A/B driver logs, AB comparison stdout, resource telemetry, tiny downstream stderr, and local Exp073EM logs. Huge workspace/canonical MCM payloads are intentionally pruned only after their hashes are verified and final replica receipts exist; prune receipts preserve the hash chain.

The real EO activation must additionally download the immutable EN artifact ZIP, verify the ZIP SHA256 against the GitHub artifact `digest`, extract it, fetch authoritative EN run/artifact metadata, and pass all of them into the frozen auditor. Workflow success alone is insufficient.

Accounting: support-only `+0/+0`. `ww_s0_s0_authority_created=false` until a real terminal EN candidate and real Exp073EO PASS exist.
