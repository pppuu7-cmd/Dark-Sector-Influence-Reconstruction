# DSIR V0.26 R1 sentinel runtime-chain schema blocker audit v0.2

Status: **FAIL-CLOSED BLOCKER — CORRECTION SCOPE EXPANDED**  
Date: 2026-09-15  
Effect: `+0/+0`.

## Scope

This audit extends the PR179 final-Q runtime-schema blocker after checking the complete frozen runtime consumer chain before any final-L creation. It does not rewrite the historical Q promotion qualification or the v0.1 fail-closed blocker. It narrows the admissible correction so that the next candidate repairs all currently observed governance-schema incompatibilities in one response-blind package.

Reviewed main: `88b69e808bafdeb89166949d31e7353018437966`.

## Blocker 1 — W consumes six top-level Q bindings

Active workflow W is exact blob `19907175f0f3417ddee2aba6916d961c6be02e26`. Its `authorize` job reads six top-level Q fields:

- `active_workflow_git_blob_sha1`
- `launch_authority_git_blob_sha1`
- `launch_descriptor_git_blob_sha1`
- `executor_git_blob_sha1`
- `decision_git_blob_sha1`
- `implementation_contract_git_blob_sha1`

Current final Q is exact blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd`. Those six values exist only in nested `acyclic_package` and `implementation_bindings` sections, not at the top level. Final L creation in this state would therefore fail closed in W `authorize` before any sentinel solve.

## Blocker 2 — executor consumes an A alias absent from exact A

Sentinel executor is exact blob `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`. Its `require_launch_authority()` requires:

`a.get('promotion_authority_git_blob_sha1') == cdbcea2622564d40aa9d1edc045a5808f8cdd1c4`.

Current final launch authority A is exact blob `4ba40e59e6a9d48636d95d07efab575e56ae0966`. A contains the same correct PR169 authority identity under the field `r1_promotion_authority_git_blob_sha1`, but it has no top-level `promotion_authority_git_blob_sha1` alias.

Thus even after a Q-only correction, each lane would pass W authorization and then fail closed inside executor `require_launch_authority()` before any CLASS construction.

## Downstream chain check

The executor's other launch-authority requirements are present in A: schema/status, sentinel authorization, full-107 false, exact R1 contract binding, and live contract identity. Its `load_contract()` PR169 post-promotion precondition is present in exact PR169 authority blob `cdbcea2622564d40aa9d1edc045a5808f8cdd1c4`.

Decision finalizer blob `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9` adds no launch-package schema dependency: it binds exact R1 contract and PR169 promotion authority, consumes lane receipts, and keeps full replay false.

No additional response-blind schema mismatch was identified in the frozen pre-solve chain after these two blockers.

## Minimal complete repair

The smallest complete repair is governance-only and preserves all scientific/executable code:

1. **A correction:** add exactly one alias `promotion_authority_git_blob_sha1 = cdbcea2622564d40aa9d1edc045a5808f8cdd1c4` while preserving all existing A fields.
2. **L correction:** because L binds exact A, update only `launch_authority_git_blob_sha1` to the corrected A blob.
3. **Q correction:** add the six W-required top-level bindings, and update its exact A/L bindings (top-level and nested) to the corrected A and corrected L blobs.

W, executor, decision, R1 scientific contract, numerical thresholds, target geometry and science inputs must not change.

Because A/L/Q exact blobs change, the corrected package requires a new response-blind static runtime-chain audit and independent funnel qualification before replacing final A/Q or creating final L.

## Historical scope preservation

The v0.1 blocker authority correctly blocked final L and science. Its statement that Q-only was the smallest repair is now superseded only as correction-scope guidance. Its blocking verdict remains valid and is not weakened.

The historical Q funnel `QUALIFIED` verdict remains scoped to inactive-Q promotion and is not rewritten.

## Verdict

`BLOCKED`

Classification: `SENTINEL_RUNTIME_CHAIN_SCHEMA_INCOMPATIBILITY_REQUIRES_GOVERNANCE_ONLY_A_L_Q_CORRECTION`.

Final L creation remains unauthorized. Sentinel science has not executed. Full 107-row replay and downstream science remain closed. Readiness remains `68%`; scientific frontier remains `67%`.
