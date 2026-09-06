# Exp073FR — WW_S1_S1 provenance admission and successor dispatch v0.1

Date frozen: 2026-09-06. Scope: DSIR Article-3 angular authority only.

## Purpose

Prospectively admit or reject the already-running Exp073FM `WW_S1_S1` candidate without changing its scientific arithmetic. This gate is separate from the self-hosted science job. A successful admission may dispatch the already-frozen next heavy target `WW_S1_S2`; any non-success stops the autonomous heavy queue.

## Frozen predecessor

- workflow: `Exp073FM WW_S1_S1 audited home science v0.1`
- run: `34050657030`
- expected head: `f0caca0c3e812710e5958ee13348a150d045a7d8`
- home job name: `home-science`
- artifact name: `exp073fm-ww-s1-s1-filebacked-ab-v0-1`
- candidate token: `PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`
- source head: `de83e20a68f79ccf25b89b0d33eb4206e294c757`
- contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`

The GitHub artifact id, size and digest are unknown while this preregistration is frozen. They MUST be discovered only from the completed frozen run and bound fail-closed by: unique artifact name; workflow-run identity/head; non-expired status; downloaded ZIP SHA-256 exactly equal to GitHub artifact metadata `digest`.

## Mandatory admission checks

1. Exp073FM run and `home-science` must complete `success` at the frozen head.
2. Raw job log must contain both complete-chain replica PASS tokens and the exact A/B candidate PASS token.
3. Artifact ZIP metadata digest must equal independently computed ZIP SHA-256.
4. `terminal_receipt.json` must classify only `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`, with `science_gate_scored=true`, no pre-existing S1S1 authority, `[1,1]`, `S1->S1`, same-field-object handoff true, exact SHA equality, `numpy.array_equal=true`, all finite, public file-backed BPW route, and no tolerance rescue.
5. Both replicas must preserve all six complete stage manifests plus post-receipt prune binding. Stage-manifest SHA-256 values must re-hash exactly.
6. Source stage must bind exactly one S1 reconstruction, same source map on both sides, and authoritative source index `[1,1]`.
7. Workspace stage must bind one field construction and the same Python field identity on both coupling sides.
8. Replica adapter evidence must prove public `get_bandpower_windows()` after file-backed FITS read with exact MCM backing bytes `19,327,352,832`, canonical selected `EE<-EE`, shape `[39,12288]`, dtype `<f8`.
9. Preserved selected arrays A/B must be byte-identical, exact-SHA-identical, `numpy.array_equal`, and finite.
10. No `allclose`, `isclose`, rounding, smoothing, averaging, fiducial/effective-coordinate or other rescue is allowed.

## Classification

Only if every mandatory check passes:

- token: `PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
- classification: `SCIENTIFIC_AUTHORITY_ADMITTED`
- `ww_s1_s1_authority_created=true`

Otherwise the gate fails closed. Infrastructure/resource failures are not scientific numerical FAILs; exact candidate numerical mismatch remains scientific FAIL and is never tolerance-rescued.

## Autonomous successor rule

Only after the exact Exp073FR admission PASS, the workflow may dispatch the prospectively frozen `WW_S1_S2` heavy workflow. Dispatch failure is infrastructure-only and does not revoke the admitted S1S1 authority. No second self-hosted heavy run may be launched while Exp073FM is still active.
