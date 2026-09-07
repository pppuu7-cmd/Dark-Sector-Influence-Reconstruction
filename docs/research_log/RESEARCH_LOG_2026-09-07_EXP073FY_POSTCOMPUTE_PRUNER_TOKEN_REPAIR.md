# DSIR4 Exp073FY post-compute pruner token repair — 2026-09-07

## Classification

- Target: `Exp073FY / WW_S2_S3`.
- Scientific status after this incident: `WW_S2_S3 = NOT_YET_ADMITTED`.
- Incident classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`.
- Scientific FAIL created by this incident: **no**.
- This record does not alter frozen scientific logic, equations, hypothesis IDs, thresholds, contract fingerprint, source ordering, exact-equality comparator, or provenance admission requirements.

## Failed run

- Workflow run: `34147009217` (`Exp073FY WW_S2_S3 autonomous audited home science v0.1`).
- Head SHA: `f04346a8e6909cb4342e536a0e7328f5ca5e54c9`.
- Hosted launch audit job: `101821110137` — `SUCCESS`.
- Self-hosted `home-science` job: `101821144414` — `FAILURE`.
- Provenance admission job: `101850590762` — `SKIPPED`, as required after producer failure.
- Partial evidence artifact: `10031272604`, zip digest `sha256:624a44f05b2762a58d1191b58df41c194b86bcc7ceb5622517c0a55f64405a6c`.

The expensive Replica A calculation reached the post-compute verify/prune boundary. The failure was then raised by `ci/exp073fy_verify_and_prune_replica_v0_1.py`:

`RuntimeError: fail-closed missing FY pruner token 'WW_S1_S2'`

The pinned frozen FS-base pruner has the real lowercase/schema/path/source-pair tokens (`ww_s1_s2`, `ww-s1-s2`, `S1->S2`, `[1,2]`) but no literal uppercase `WW_S1_S2`. Therefore the uppercase-token requirement was a lexical transformation guard bug, not a scientific gate result.

## Safe repair

- Repair commit: `c28396aa4cba6206f737cfd683b9f27f9cbe5273` — `Fix Exp073FY pruner absent uppercase token guard`.
- Repaired FY pruner blob: `8c0e7ae30a80c6d74e6a1fbc079c1d2bc4eef773`.
- Binding commit: `3217ea05f5ab8a45bc237f34a8fa894e8c49df38` — `Bind repaired Exp073FY pruner for checkpoint resume`.

The repair only removes the demand to transform a token absent from the pinned base. Existing fail-closed checks for source identities/order, reconstruction counts, distinct-field handoff, stage-manifest identities, payload SHA chains, workspace/full-window/selected-EE/receipt integrity, adapter evidence, and no-tolerance-rescue remain in force.

## Recovery state

A single recovery run was created by the workflow binding push:

- Recovery run: `34157571794`.
- Head SHA: `3217ea05f5ab8a45bc237f34a8fa894e8c49df38`.
- Hosted audit job: `101852463413` — `SUCCESS`.
- Self-hosted `home-science` job: `101852500796` — `IN_PROGRESS` at the time of this record.

No second `Exp073FY` heavy-run is launched. The recovery uses the existing durable checkpoint namespace; completed valid stages must be reused by the frozen durable driver rather than intentionally recomputed. Scientific authority remains fail-closed until a successful terminal A/B artifact and `Exp073FZ` provenance admission explicitly emit `classification=SCIENTIFIC_AUTHORITY_ADMITTED` and `ww_s2_s3_authority_created=true`.

## Next allowed transition

Do not dispatch `Exp073GA / WW_S3_S3` until `Exp073FY` is terminal-success and the same run's `Exp073FZ` admission succeeds. Infrastructure failure, `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, and `OUTSIDE_DOMAIN` remain distinct from scientific FAIL.
