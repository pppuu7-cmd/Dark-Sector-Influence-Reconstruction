# Exp073IJ — C2 WW angular-authority admission v0.1

Status: prospectively frozen before execution. Scope: DSIR only.

## Inputs
- `docs/dsir4/DSIR4_ANGULAR_AUTHORITY_BINDING_CONTRACT_V0_1.md`, blob `af2cdbfa03e0a68c24df8d1009c723d411d2d0a2`.
- Corrected candidate-local receipt `docs/dsir4/authority/C2_WW_ANGULAR_AUTHORITY_RECEIPT_V0_2.json`, blob `5c381d6d212a8bc774338511c4dca6e13a4fdfae`.
- Upstream domain authority `PASS_EXP073IH_C2_G_DOMAIN_MAPPING_V0_1`, run/job `34251721583 / 102147505217`.

## Exact gate
The gate must fail closed unless all ten exact WW authorities in the receipt are independently bound to their recorded authority-admission raw logs and source-artifact metadata. For every pair it must verify: exact pair set; exact relation (`same_object` or `ordered_distinct`); admission run/job/head; exact admission token; `classification=SCIENTIFIC_AUTHORITY_ADMITTED`; pair-specific `ww_*_authority_created=true`; canonical selected `EE<-EE` SHA256; source artifact ID and exact GitHub digest; common `<f8 [39,12288]`, DES NSIDE=4096, ell 0..12287, 39 bands, exact 19,327,352,832-byte file-backed MCM contract.

No workflow-success inference, candidate-only evidence, tolerance, rounding, smoothing, averaging, effective ell/z/k, fiducial-P substitute, source-pair substitute, or home recomputation is allowed.

## Classification
If and only if every exact check passes, emit:
`PASS_EXP073IJ_C2_G_ANGULAR_AUTHORITY_V0_1`
`classification=SCIENTIFIC_GATE_PASS`
`G_DOMAIN_MAPPING=PASS`
`G_ANGULAR_AUTHORITY=PASS`
`angular_authority_receipt_created=true`
`scientific_model_authority_created=false`
`overall_status=NOT_YET_TESTABLE`

Any missing authority/evidence is `NOT_YET_TESTABLE`, not scientific FAIL. Infrastructure/API/transport defects are infrastructure failure `+0/+0`. This gate may not create complete model authority and may not dispatch self-hosted work.

## Downstream
Only a raw-log validated Exp073IJ PASS permits prospective `G_ORDERED_JOIN`. All later funnel gates remain `NOT_YET_TESTABLE` until separately frozen and evaluated.
