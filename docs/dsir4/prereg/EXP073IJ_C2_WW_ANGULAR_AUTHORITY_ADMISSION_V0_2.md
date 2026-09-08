# Exp073IJ — C2 WW angular-authority admission v0.2

Status: prospectively frozen before execution. Scope: DSIR only. This supersedes the v0.1 execution binding only because fail-closed artifact verification exposed candidate-receipt metadata transcription errors for S1_S1 and S2_S3. No historical scientific authority, arithmetic, domain, tolerance, semantics, or acceptance criterion is changed.

## Inputs
- `docs/dsir4/DSIR4_ANGULAR_AUTHORITY_BINDING_CONTRACT_V0_1.md`, blob `af2cdbfa03e0a68c24df8d1009c723d411d2d0a2`.
- Artifact-verified candidate-local receipt `docs/dsir4/authority/C2_WW_ANGULAR_AUTHORITY_RECEIPT_V0_3.json`, blob `681503a7ac8376801e997f0e2e4ba2ebdace87da`.
- Upstream domain authority `PASS_EXP073IH_C2_G_DOMAIN_MAPPING_V0_1`, run/job `34251721583 / 102147505217`.

## Exact gate
Fail closed unless all ten WW authorities are independently bound to their recorded authority-admission raw logs and frozen source artifacts. For every pair verify: exact pair set and relation; admission run/job/head; exact admission token; `classification=SCIENTIFIC_AUTHORITY_ADMITTED`; pair-specific `ww_*_authority_created=true`; source artifact ID and GitHub digest; and by downloading that exact frozen artifact, recompute SHA256 of the canonical `EE<-EE` `<f8 [39,12288]` payload and require exact equality to the receipt. Require DES NSIDE=4096, ell 0..12287, 39 bands and exact 19,327,352,832-byte file-backed MCM contract. Both A/B canonical copies, when present, must be byte-identical by SHA.

No workflow-success inference, candidate-only evidence, tolerance, rounding, smoothing, averaging, effective ell/z/k, fiducial-P substitute, source-pair substitute, or home recomputation is allowed.

## Classification
If and only if every exact check passes, emit:
`PASS_EXP073IJ_C2_G_ANGULAR_AUTHORITY_V0_2`
`classification=SCIENTIFIC_GATE_PASS`
`G_DOMAIN_MAPPING=PASS`
`G_ANGULAR_AUTHORITY=PASS`
`angular_authority_receipt_created=true`
`scientific_model_authority_created=false`
`overall_status=NOT_YET_TESTABLE`

Any missing authority/evidence is `NOT_YET_TESTABLE`, not scientific FAIL. Infrastructure/API/transport defects are infrastructure failure `+0/+0`.

## Downstream
Only a raw-log validated v0.2 PASS permits prospective `G_ORDERED_JOIN`. All later funnel gates remain `NOT_YET_TESTABLE` until separately frozen and evaluated.
