# Exp073FN — WW_S0_S3 provenance admission v0.1 preregistration

Date: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR.

Purpose: independently admit or reject the already completed Exp073FG `WW_S0_S3` candidate. This is a GitHub-hosted evidence/provenance gate only; it performs no heavy numerical science.

Governance correction: experiment label `Exp073FL` is already occupied by the earlier `WW_S1_S1` driver-generation static audit. Later commits accidentally reused `Exp073FL` for an S0S3 provenance-admission implementation. That collision is preserved historically but is not authoritative. This preregistration prospectively assigns the S0S3 provenance-admission gate to the previously unused label **Exp073FN**. The frozen candidate evidence and scientific acceptance criteria are unchanged.

Frozen candidate authority inputs:

- candidate workflow run: `34034377795`
- candidate home job: `101489679508`
- candidate head: `4a02952ee3bcb368a088d87608f61243cd9f7056`
- artifact id: `9993520467`
- artifact name: `exp073fg-ww-s0-s3-filebacked-ab-v0-1`
- artifact size: `7382890` bytes
- artifact digest: `sha256:8ddd1e1b81e5fa9c3a4de16c6d72b35353cb42bba04bb77c736aa4998340bde0`
- independently re-downloaded ZIP SHA256 must equal that digest exactly
- exact candidate token: `PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`
- replica A verification token: `PASS_EXP073FG_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`
- replica B verification token: `PASS_EXP073FG_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`
- frozen source head: `de83e20a68f79ccf25b89b0d33eb4206e294c757`
- contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`
- R1 artifact/digest: `9720335366`, `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`
- NaMaster head: `24365fa59a38c15732f4f37e8b29265b75c442d5`

PASS requirements:

1. Candidate run and all three candidate jobs are completed SUCCESS.
2. Home-job raw log contains both replica full-chain verification tokens, live-exclusivity token, and exact candidate token.
3. Artifact metadata exactly matches frozen id/name/size/digest/head.
4. Artifact payload independently validates both complete six-stage manifests before prune, dedicated A/B checkpoint namespaces, frozen source head and contract fingerprint.
5. Both selected arrays are canonical `<f8 [39,12288]`, `EE<-EE`, finite, byte-identical, SHA-identical and exact `numpy.array_equal` equivalent; no tolerance rescue.
6. Both replica receipts prove public `get_bandpower_windows()` after `read_from(..., read_unbinned_MCM=True)`, regular-file-backed MCM exactly `19,327,352,832` bytes and `/proc/self/maps` proof.
7. `source_pair=S0->S3`, ordered indices `[0,3]`, distinct-field semantics (`same_field_object_handoff=false`), no historical WW numerical import and no cross-replica output read.
8. No tolerance/allclose/isclose/rounding/smoothing/averaging/manual-reconstruction/effective-coordinate/fiducial rescue is permitted.

The historical collided `Exp073FL` admission run `34047839320 / 101525992295` is classified `INFRASTRUCTURE_LOG_TRANSPORT_FAIL_PLUS_0_PLUS_0`: its first causal failure was `gh api .../logs` refusing terminal escape sequences. It created no authority and does not alter Exp073FG candidate evidence.

If all requirements pass, emit exactly:

`PASS_EXP073FN_WW_S0_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`

and classify `SCIENTIFIC_AUTHORITY_ADMITTED` for `WW_S0_S3`.

Any mismatch is fail-closed. Candidate evidence and frozen scientific criteria must never be altered to obtain PASS.