# Exp073EO — WW_S0_S0 file-backed checkpoint provenance admission v0.2 preregistration

This prospectively supersedes only the v0.1 auditor's JSON representation bug discovered after the first real terminal Exp073EN artifact was consumed. It does not change any frozen scientific, provenance, storage, hash, geometry, checkpoint, or exact-equality criterion.

## Immutable observed defect
Exp073EO v0.1 real run `34005304226 / 101411264696` reached the frozen auditor after live GitHub metadata binding and independent ZIP-digest verification, then fail-closed with `RuntimeError: terminal EM identity`. The authoritative Exp073EN artifact records `hosted_exp073em_artifact_id` as JSON string `"9977333691"`; the v0.1 auditor constant was Python integer `9977333691`. Artifact identity value and hosted Exp073EM digest are otherwise the prospectively frozen values. This is a serialization-type mismatch, not missing or conflicting provenance.

## Sole v0.2 change
For comparisons of `hosted_exp073em_artifact_id` only, v0.2 requires exact lexical identity after canonical string representation: `str(value) == "9977333691"`. The digest must still equal exactly `sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1`. No alternate artifact ID is accepted.

All other v0.1 requirements remain byte-for-byte semantically unchanged: authoritative EN run/head/workflow and artifact digest; source `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; R1 authority; NaMaster head; storage patch; six-stage A/B chains; pruning evidence; regular-file mmap proof `19327352832` bytes and `49152` rows; exact 8-CPU proof; canonical `<f8 [39,12288]` `EE<-EE`; SHA equality plus `numpy.array_equal`; finiteness; and no tolerance/allclose/rounding/smoothing/averaging rescue.

The implementation must reuse the frozen v0.1 auditor module and alter only the in-memory representation of its `EM_ID` constant from integer to the exact string `"9977333691"` before invoking the unchanged `main()` logic. Any other behavioral change is forbidden.

Classification remains:
- `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2` only if every unchanged gate passes after the representation-only repair;
- provenance/infrastructure defects remain BLOCKED `+0/+0` and never become scientific FAIL;
- `WW_S0_S0` authority may be created only by this real admission PASS.
