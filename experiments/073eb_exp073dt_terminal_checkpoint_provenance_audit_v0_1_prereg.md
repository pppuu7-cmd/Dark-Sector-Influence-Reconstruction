# Exp073EB — Exp073DT terminal full checkpoint-provenance audit v0.1

Frozen 2026-09-05 while Exp073DT run `33940588308`, attempt 4, self-hosted job `101288014666` is still queued and before any attempt-4 terminal scientific output exists.

Scope: support/evidence only (`+0/+0`). Exp073EB cannot create, rescue, weaken, reinterpret, or supersede `WW_S0_S0` scientific authority. It performs no NaMaster workspace construction and no WW window computation.

## Motivation / prospective audit finding
The frozen Exp073DT preregistration requires all source/contract/component/checkpoint provenance checks to pass before authority can be admitted. The frozen DQ driver's `validated_finished()` fast path verifies the terminal `replica_receipt_complete` manifest, receipt SHA and selected-EE SHA, but it does not itself reread every earlier stage manifest before returning a completed replica. The Exp073DT terminal classifier independently rereads A/B selected payloads and exact comparator state, but its artifact package does not contain all six checkpoint stage manifests. Therefore workflow SUCCESS and even the frozen PASS token are not, by themselves, sufficient evidence of the preregistered full stage-order provenance condition.

This finding is prospective with respect to attempt-4 terminal output and changes no frozen scientific arithmetic or acceptance criterion. It only makes the already-frozen provenance requirement explicitly machine-checkable.

## Frozen upstream identity
- upstream workflow name: `Exp073DT WW_S0_S0 full-resolution A/B exact science v0.1`;
- upstream run: `33940588308` only;
- upstream head: `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd` only;
- frozen source authority: `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable science root: `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- replica roots: `checkpoints/A` and `checkpoints/B`;
- checkpoint namespaces: `checkpoints/exp073dq-ww-s0-s0-a-v0-1`, `checkpoints/exp073dq-ww-s0-s0-b-v0-1`.

Event-driven execution is permitted only after that exact upstream run becomes terminal with GitHub conclusion `success`. Any other run/head/conclusion must fail closed or skip without touching the durable root.

## Frozen six-stage chain
For each replica independently, require exactly the ordered stages:
1. `fresh_s0_mask_complete`
2. `fresh_workspace_mcm_complete`
3. `mcm_fits_verified`
4. `full_window_complete`
5. `selected_ee_complete`
6. `replica_receipt_complete`

Every manifest must exist and have `complete=true`, exact stage, replica, checkpoint namespace, source head and contract fingerprint, plus `historical_ww_numerical_import=false` and `other_replica_output_read=false`.

Payload verification is exact and fail-closed:
- `s0_count_map.npy`: `<f8`, expected NSIDE=4096 pixel length where encoded by the payload, and canonical array SHA256 equal to the first-stage manifest;
- `fresh_workspace.fits`: file SHA256 equal to `fresh_workspace_mcm_complete`, and the `mcm_fits_verified` manifest must repeat the same workspace SHA;
- `exact_route/full_window.bin`: exact file SHA256 from its manifest and exact byte size implied by `<f8 [4,39,4,12288]`;
- `exact_route/selected_ee.bin`: exact file SHA256 from its manifest and exact byte size implied by `<f8 [39,12288]`;
- `replica_receipt.json`: exact file SHA256 from the terminal manifest; receipt must repeat the same selected-EE SHA, source head, contract fingerprint, checkpoint namespace and `science_gate_scored=false`.

The audit must also require the selected-EE SHA recorded at `selected_ee_complete`, in `replica_receipt.json`, and in `replica_receipt_complete` to be identical within each replica. No tolerance, allclose, rounding, smoothing, averaging or ULP rescue is permitted.

## Output and classification
On exact success emit only:
`PASS_EXP073EB_EXP073DT_FULL_CHECKPOINT_PROVENANCE_AUDIT_V0_1`

with `science_gate_scored=false`, `ww_s0_s0_authority_created=false`, classification `SUPPORT_PROVENANCE_PASS_PLUS0_PLUS0`.

Any missing/malformed/mismatched stage, payload, identity, hash, size or receipt is `INFRASTRUCTURE_PROVENANCE_FAIL_PLUS0_PLUS0`; it is not scientific arithmetic FAIL. Exp073EB must never alter, delete or regenerate durable checkpoints.

## Authority rule after Exp073DT terminal
`WW_S0_S0` may be admitted only after normal independent terminal consumption verifies the frozen Exp073DT raw artifact and exact A/B equality **and** the complete checkpoint provenance requirement is independently evidenced (Exp073EB PASS or an equivalently strict direct reread). Exp073EB cannot turn an Exp073DT scientific FAIL into PASS.
