# Exp073FL — WW_S0_S3 provenance admission v0.1 preregistration

Date: 2026-09-06. Scope: **DSIR only**.

Purpose: independently admit or reject the already completed Exp073FG WW_S0_S3 candidate. This is a GitHub-hosted evidence/provenance gate only; it must perform no heavy numerical science.

Frozen candidate authority inputs:

- candidate workflow run: `34034377795`
- candidate home job: `101489679508`
- candidate head: `4a02952ee3bcb368a088d87608f61243cd9f7056`
- artifact id: `9993520467`
- artifact name: `exp073fg-ww-s0-s3-filebacked-ab-v0-1`
- artifact size: `7382890` bytes
- artifact digest: `sha256:8ddd1e1b81e5fa9c3a4de16c6d72b35353cb42bba04bb77c736aa4998340bde0`
- exact candidate token: `PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`
- replica A verification token: `PASS_EXP073FG_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`
- replica B verification token: `PASS_EXP073FG_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`
- frozen source head: `de83e20a68f79ccf25b89b0d33eb4206e294c757`
- contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`
- R1 artifact/digest: `9720335366`, `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`
- NaMaster head: `24365fa59a38c15732f4f37e8b29265b75c442d5`

PASS requirements:

1. Candidate run and all three jobs are completed SUCCESS.
2. Home-job raw log contains both replica full-chain verification tokens and the exact candidate token.
3. Artifact metadata exactly matches the frozen id/name/size/digest/head.
4. Candidate log preserves file-backed MCM evidence at exactly `19327352832` bytes for both replicas and the same frozen NaMaster lineage.
5. No tolerance/allclose/rounding/smoothing/averaging rescue is used by this admission gate.
6. This gate creates no numerical result; it only verifies already frozen evidence.

If all requirements pass, emit exactly:

`PASS_EXP073FL_WW_S0_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`

and classify `SCIENTIFIC_AUTHORITY_ADMITTED` for `WW_S0_S3`.

Any mismatch is fail-closed and must not be repaired by changing the candidate evidence. A later corrected admission implementation may be prospectively versioned, but it must continue to target the same frozen candidate evidence.
