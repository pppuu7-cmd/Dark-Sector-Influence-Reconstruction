# Exp073HD — WW_S2_S3 terminal comparator namespace repair/admission v0.1 preregistration

Scope: DSIR only.

Purpose: consume Exp073FY recovery run 34160898921 after both A and B completed and were independently full-chain verified before prune, but the terminal comparator failed only because its transformed namespace expectation remained `exp073fy-ww-s1-s2-*` while the preserved valid checkpoint identity is `exp073fy-ww-s2-s3-*`.

Frozen evidence source: Actions run 34160898921, home job 101862390771, artifact 10040351900, artifact digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

Frozen repair: comparator blob `5ccce6c459a5ce541fcccc6b576e78c531fea01f` changes only exact hyphenated namespace transformation and adds stale/correct namespace regression checks. No arithmetic, domain, source ordering, payload bytes, tolerance, rounding, smoothing or averaging may change.

Gate procedure: hosted-only. Verify exact artifact metadata/digest and exact pinned blobs; download artifact 10040351900; execute repaired comparator over the frozen artifact; require exact candidate PASS `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; verify original run log contains live exclusivity and both pre-prune full-chain PASS markers; execute frozen FZ verifier blob `c3f967c8fc9efed017bb6d5794d53433afefd4ac` against the same bytes and combined log.

PASS authority requires exact FZ token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s2_s3_authority_created=true`. Any artifact/blob/provenance mismatch is infrastructure/provenance FAIL +0/+0. Comparator exact inequality/non-finiteness under otherwise valid frozen evidence is scientific FAIL. No home computation is permitted or required by this gate.
