# DSIR recovery checkpoint — Exp073P v0.3 production route integrated with canonical main guards

**Date:** 2026-08-29

**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`

**Scope:** DSIR only. RTK was not read, changed, or used.

## Recovery headline

Repository state was fetched repeatedly before this iteration was recorded.
While PR #166 was being developed, `main` first advanced independently from
`3ebcd03` to `72c02784a0d67226a2533a6868628c4812e65b83`, then advanced again
during integration to `f2d1043577b3e0cc1280992c1df9e0d1c3991dd9`. The new
main history already contained a stricter prospective Exp073P v0.3
preregistration and four hosted supplemental fail-closed guards. PR #166 was
therefore not merged blindly and no duplicate PR was opened. Instead, the
branch was merged with each current main head and the actual v0.3 production
route was conformed to the canonical main authority.

At `2026-08-29T14:27:27Z`, the sole heavy candidate was still Exp073R1 v0.7
run `33240490287`, attempt `2`, job `99080934021`: `queued`,
`conclusion=null`, with an empty run artifact list. No duplicate heavy run and
no real aggregate join were dispatched. Exp073R1 reproduction therefore
remains INCOMPLETE. This queue state is infrastructure availability, not a
scientific result.

## Canonical authority reconciliation

The canonical preregistration is the file merged to main by commit
`e58bddf`:

`experiments/073p_aggregate_prerequisite_join_v07_r1_authority_prereg_v0_3.md`

Its byte identities are:

- Git blob `6dd4ba0df9ed2be321b7f69966d7636d940e40d1`;
- SHA256 `e27761b2db4a81283bb9fbac1decb95f62fadb785c40cb3e3f676f8651711f40`.

Those bytes were preserved exactly during conflict resolution. The earlier
independent PR-branch preregistration commit `940fbca` remains historical
chronology, but its different file bytes are not the canonical authority and
must not be restored. This reconciliation is not a post-hoc threshold or
authority change: both preregistrations were created while the same frozen
attempt-2 job was queued with no artifact, and the stricter main version was
already merged before this integration.

The canonical authority admits only:

- repository `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`;
- run `33240490287`, `run_attempt=2`;
- exact job set `{99080934021}` and job `run_attempt=2`;
- job name `transport-stabilized-replay`;
- head `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- branch `main`, event `push`, workflow ID `345172058`;
- workflow path/name and byte-frozen workflow/evaluator identities;
- exactly one non-expired artifact with the frozen name;
- the independently supplied numeric artifact ID and canonical
  `sha256:<64 lowercase hex>` digest matching live metadata.

Attempt 1, later attempts, replacement jobs, changed event/branch/workflow,
incomplete pagination, duplicate jobs, duplicate or expired same-name
artifacts, and ID/digest mismatch all fail closed.

## Main guards preserved in the integrated branch

Current main contributed the following additive implementation-validation
guards without changing the frozen science contract:

- authority contract self-test: hosted run `33250019007`, job `99093989267`,
  success, 15 negative mutations rejected;
- live metadata-set guard: hosted run `33252122146`, job `99099482735`,
  success, 15 negative mutations rejected;
- archive-member guard: hosted run `33254539043`, job `99105858678`, success,
  13 negative mutations rejected.

Their recovery records are preserved unchanged:

- `recovery/2026-08-29_exp073p_v03_v07_authority_prereg_and_attempt_aware_selftest.md`;
- `recovery/2026-08-29_exp073p_v03_live_metadata_set_guard_and_r1_v07_queue_checkpoint.md`;
- `recovery/2026-08-29_exp073p_v03_archive_member_guard_pass_and_r1_v07_queue_checkpoint.md`.

Current main then added the cross-member consistency guard:

- hosted run `33257187305`: success, 19 negative mutations rejected;
- `ci/exp073p_v03_cross_member_consistency_failclosed_selftest.py`;
- `recovery/2026-08-29_exp073p_v03_cross_member_consistency_guard_pass_r1_v07_queued.md`.

It independently requires summary/acquisition agreement on the exact metacal
bytes and SHA256, frozen source identities, exact row accounting, acquisition
authorization/from-zero/no-Range semantics, nonempty runtime provenance, and
no downstream leakage. These requirements are consistent with the actual
route's existing acquisition cross-binding and payload/runtime checks.

All four are synthetic/provenance PASS results only and retain
`support_executor_authorized=false`.

## Actual production route completed

PR #166's prospective v0.3 implementation now applies the canonical main
authority end to end.

### Exact live metadata

`ci/exp073p_actions_metadata_bundle_v0_3.py` uses the attempt-specific jobs
endpoint and requires the exact latest/attempt-2 job registry to agree. It now
normalizes and validates `run_attempt`, `head_branch`, `event`, `workflow_id`,
the exact job set, and job-level `run_attempt`, in addition to the inherited
complete-pagination and artifact-set checks.

### Exact raw ZIP identity

`ci/exp073p_v03_artifact_zip_download_v0_1.py` downloads the artifact by the
frozen numeric artifact ID rather than selecting by name. It streams at most
5,000,000,000 bytes, requires a nonempty body, verifies the SHA256 of the raw
ZIP against the live canonical artifact digest, and atomically publishes the
file only after success. The GitHub bearer token is sent only to the GitHub API
request; it is deliberately not forwarded to the signed HTTPS redirect.

### Exact archive and payload

`ci/exp073p_v07_r1_payload_bundle_v0_3.py` validates the raw ZIP before
extraction. The member set must be exactly 11 files:

- three root authority files: summary, acquisition provenance, runtime
  provenance;
- four exact pixel-record members under `exp073r1_v05_records/`;
- four exact masks under `exp073r1_v05_masks/`.

The validator rejects malformed/encrypted archives, duplicate names,
directories, absolute/traversal/backslash paths, empty or extra members,
unexpected record identities, oversized authority files, invalid record byte
bounds, and masks not exactly `25,165,824` bytes. Extraction uses the inspected
member objects and exact paths. The existing semantic validator then requires
one copy of every basename, recomputes every byte count and SHA256, cross-binds
them to the terminal R1 summary, and preserves the validated bytes.

### Unchanged semantic and scientific boundary

`ci/exp073p_aggregate_prerequisite_join_v0_3.py` continues to privately load
and byte-freeze v0.1. Historical v0.1/v0.2 authority and evaluator files were
not repointed. All nine non-R1 parents and the R1 scientific/admissibility
checks remain unchanged. The production workflow is manual-only, read-only,
and requires `refs/heads/main`.

## Integrated byte identities

- evaluator v0.3:
  `bb7b485a8249790ee9ed3586a1d65ac3255ecc67aafede806e0e472fa2118114`;
- live metadata collector v0.3:
  `3bb52c9c7245e46b8a7308e9be501468784d1e03607d714e7370fd2df1b4b0f1`;
- raw artifact ZIP downloader v0.1:
  `3d9b40602661d339504ad1cebadaef41cbe6bf3743e1008a12dae7dd6885186b`;
- payload/archive validator v0.3:
  `7083d15db6f8ab0b89d756b53349731ed70efc4b70c8569cb18c6c3fb2d0ee67`;
- production workflow v0.3:
  `dd372979822eaa512352ae2689c580e18ee92c0e7a3fbd5e3ea6a5c0ba993b9a`;
- synthetic route workflow v0.3:
  `425c82fe8bc497e577bec4ec3b894af4033fbaa965edf8f874e488c6b5dd1df4`;
- canonical preregistration:
  `e27761b2db4a81283bb9fbac1decb95f62fadb785c40cb3e3f676f8651711f40`.

## Local verification

The integrated prospective route passed:

- evaluator v0.3 synthetic suite: 23 new fail-closed mutations;
- live route v0.3 suite: 9 attempt/route mutations, in addition to the
  inherited 10 metadata mutations;
- exact ZIP downloader: 4 delivery mutations;
- complete payload: 4 file/multiplicity mutations;
- raw archive integration: 3 archive mutations;
- canonical main authority guard: PASS, 15 mutations;
- canonical main live metadata-set guard: PASS, 15 mutations;
- canonical main archive-member guard: PASS, 13 mutations;
- canonical main cross-member guard: PASS, 19 mutations;
- integrated no-leakage assertions: PASS;
- repository tests: `44 passed`.

The synthetic receipts all retain `support_executor_authorized=false`, no
physical-support quantity was evaluated, and the gate state remains
`{G7: OPEN, G8: OPEN, G9: OPEN}`.

## Hosted integration verification

The exact remote merge commit is
`17a4551290e2a1a97979215fb71d69c7a8352290`, with parents PR head
`614a2b6956e9fdd273f182e3fa2265d46f0ff493` and current main
`72c02784a0d67226a2533a6868628c4812e65b83`. Its tree
`805034b2b5d04716970db888a26d65b37888f76f` matches the locally validated
integration tree exactly.

Hosted PR self-test run `33257888770`, job `99114673638`, completed
`success`. Every step passed, including lineage hashes, evaluator mutations,
attempt-specific metadata mutations, full payload/archive mutations, exact ZIP
download mutations, synthetic no-leakage assertions, and artifact upload.

The immutable synthetic artifact is:

- ID `9716362579`;
- name
  `exp073p-aggregate-join-v0-3-synthetic-selftest-869d097d0ac732e7e4873508c50b05cb45e81bed`;
- digest
  `sha256:f78ed9f12c54bd585c9f5b8022e8fcb468dee7583e842c0c76363af2dfde7b33`;
- size `6,343` bytes;
- `expired=false` at verification time.

This is hosted implementation validation only. It is not a real prerequisite
receipt and cannot authorize physical support.

## Exact recovery and continuation method

1. Read `docs/RECOVERY_MANUAL.md`, `docs/RECOVERY_LATEST.md`, then this file.
2. Fetch both `main` and PR #166 before editing. Verify that the canonical
   preregistration still has SHA256 `e27761...1711f40`; never restore the old
   branch preregistration bytes.
3. Verify the active R1 run, exact attempt-2 job, and full artifact set. Do not
   create another heavy run while job `99080934021` is queued/running.
4. Reproduce the prospective route checks:

   ```text
   python3 ci/exp073p_aggregate_prerequisite_join_v0_3.py --selftest --out /tmp/exp073p-evaluator-v03.json
   python3 ci/exp073p_actions_metadata_bundle_v0_3.py --selftest --workflow .github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-3.yml --out /tmp/exp073p-route-v03.json
   python3 ci/exp073p_v03_artifact_zip_download_v0_1.py --selftest --out /tmp/exp073p-download-v01.json
   python3 ci/exp073p_v07_r1_payload_bundle_v0_3.py --selftest --manifest-out /tmp/exp073p-payload-v03.json
   python3 ci/exp073p_v03_v07_authority_contract_selftest.py --out /tmp/exp073p-authority.json
   python3 ci/exp073p_v03_live_metadata_set_failclosed_selftest.py --out /tmp/exp073p-metadata-set.json
   python3 -W ignore::UserWarning ci/exp073p_v03_archive_member_failclosed_selftest.py
   python3 ci/exp073p_v03_cross_member_consistency_failclosed_selftest.py
   uv run --with pytest pytest -q
   ```

5. Confirm hosted v0.3 run `33257888770` and job `99114673638` remain
   `completed/success`. If executable bytes change on a later head, require a
   new hosted self-test; do not rely on this older receipt for changed code.
6. If R1 attempt 2 ends in runner, transport, acquisition, workflow, or
   artifact failure, preserve the exact evidence as infrastructure and do not
   dispatch the real aggregate join.
7. If Actions reaches success, that alone is insufficient. Require exactly one
   frozen-name artifact, exact ID/digest, complete 11-member ZIP, exact
   acquisition identity, every payload byte/hash cross-binding, and internal
   `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.
8. Only after PR #166 is merged to main may the production workflow be manually
   dispatched with the independently copied artifact ID and digest. Never run
   or repoint v0.1/v0.2.
9. Only a genuine real receipt
   `PASS_EXP073P_PREREQUISITE_BINDING_V0_3` may set
   `support_executor_authorized=true`. A synthetic PASS never authorizes it.
10. After genuine prerequisite PASS, preserve the frozen order: physical
    support -> covariance/whitening -> nuisance SVD/rank ->
    quotient/relation/null -> fresh G8.

## Frozen scientific boundaries

No value was changed or inspected post hoc. Preserve:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- `nside=4096`, RING, celestial C, `lonlat=True`;
- positive absolute final-response support envelope while production Wm stays
  signed;
- invalid radial tails outside the rectangle;
- no crop-before-normalization, effective ell, fiducial-P/model weighting, or
  post-hoc cuts;
- no covariance, nuisance, relation/null, held-out, or G8 leakage into
  prerequisite/support selection.

No physical result is claimed. `support_executor_authorized=false`; G7/G8/G9
remain OPEN.
