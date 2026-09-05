# Exp073EO — WW_S0_S0 file-backed provenance authority admission v0.1

Prospectively preregistered on 2026-09-06 while Exp073EN v0.2 full-resolution science candidate is still in progress. This document freezes the final authority-admission criteria before the Exp073EN numerical outcome is known.

## Scope
Exp073EN may produce a full-resolution exact A/B science-candidate PASS. Exp073EO is a separate provenance-consumption gate. `WW_S0_S0` authority must remain false until EO independently consumes the uploaded EN evidence and verifies the complete chain below. EO must never repair, recompute, round, tolerance-rescue, or silently replace EN numerical payloads.

## Inputs to bind after EN terminates
EO activation must bind immutable IDs/digests rather than mutable paths:
- exact Exp073EN workflow run ID, attempt and home job ID;
- run head SHA and workflow blob;
- uploaded EN evidence artifact ID and GitHub artifact digest;
- Exp073EM hosted artifact `9977333691`, digest `sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1`;
- NaMaster source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- storage patch SHA256 `9a80a756960afa8b4ddf61b5fbba7fba6ad5ed9ac919e093bb1365a636c789f0`;
- frozen source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- R1 artifact ID `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

The concrete EN IDs are intentionally not guessed in this preregistration. They must be inserted only after a terminal run exists and must match GitHub API metadata exactly.

## Mandatory evidence checks
EO PASS requires all of the following without exception:

1. **Terminal EN classification**
   - EN terminal receipt token is exactly `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1`.
   - EN class is a science-candidate PASS, not BLOCKED, resource fail, storage qualifier fail, or numerical repeatability fail.
   - no tolerance rescue is true.

2. **Frozen science identity**
   - source authority, contract fingerprint, R1 digest, driver/adapter/downstream/task-runner identities equal the frozen preregistered identities.
   - selected semantics are `EE<-EE`, canonical dtype `<f8`, shape `[39,12288]`; full BPW semantics are `[4,39,4,12288]`.

3. **Storage qualification and local activation**
   - immutable hosted Exp073EM PASS identity/digest matches the values above.
   - EN local stock-vs-patched activation receipt is terminal `PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1` with no tolerance rescue.
   - patched native binary/build identity and storage patch/source identities are present and bound.

4. **Full-resolution regular-file proof**
   - every newly computed A and B workspace records `DSIR_NMT_FILEBACKED_MCM` use with a regular-file mapped MCM of exactly `19,327,352,832` bytes and 49,152 rows.
   - evidence must exclude tmpfs/memfd/anonymous backing for the full MCM.
   - no mapped backing file survives replica teardown.

5. **Durable A/B reconstruction provenance**
   - A and B are distinct replica namespaces and each has a complete durable receipt/manifest.
   - completed checkpoint payload hashes recompute to their recorded values.
   - no historical WW numerical payload was imported as a fresh replica result.
   - any pruning of huge FITS/MCM intermediates occurred only after their identity/hashes were bound by the complete replica receipt.

6. **Exact numerical repeatability**
   - both selected canonical payloads exist and are exactly `39*12288*8` bytes.
   - recomputed SHA256(A) == SHA256(B) == the hashes recorded by EN.
   - `numpy.array_equal(A,B)` is true after canonical `<f8 [39,12288]` interpretation.
   - all values are finite.
   - no `allclose`, tolerance, rounding, smoothing, averaging or alternate-operation rescue.

7. **Run integrity**
   - hosted preflight and required home execution belong to the bound EN workflow attempt.
   - no competing self-hosted DSIR science owner was admitted by the EN exclusivity contract.
   - resource telemetry and terminal evidence are internally consistent with the bound attempt; infrastructure warnings cannot be rewritten as science evidence.

## Terminal classification
Only if every mandatory check passes may EO emit:

`PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_AUTHORITY_V0_1`

with classification `SCIENTIFIC_AUTHORITY_ADMITTED`, `science_gate_scored=true`, `ww_s0_s0_authority_created=true`.

Any provenance/identity/evidence incompleteness is `BLOCKED_EXP073EO_PROVENANCE +0/+0` and creates no authority. A genuine EN exact A/B numerical mismatch remains the scientific repeatability failure classified by EN and cannot be converted by EO.

## Frontier effect
Only EO authority PASS advances the ordered Article-3 frontier from `WW_S0_S0` to `WW_S0_S1`. Hosted support qualifiers such as Exp073EM, Exp073EK and Exp073EP remain `+0/+0` even if exact.
