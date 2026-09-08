# Exp073HE — WW_S3_S3 materialized terminal recompare + GB admission v0.1

Status: **prospectively frozen before execution**. Scope: DSIR only.

## Motivation

Exp073GA recovery run `34197207582` completed both expensive frozen replicas through `PASS_EXP073GA_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1` and `PASS_EXP073GA_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`, then failed in the terminal comparator before scientific scoring with `RuntimeError: fail-closed receipt identity mismatch A:checkpoint_namespace`. Artifact `10051382493` was uploaded with GitHub digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

The defect is implementation/provenance `+0/+0`: the GA wrapper transformed `exp073fm` to `exp073ga` but did not transform the hyphenated embedded namespace token `ww-s1-s1` to `ww-s3-s3`. The materialized receipts themselves use the intended frozen namespaces `checkpoints/exp073ga-ww-s3-s3-{a,b}-v0-1`. Minimal prospective comparator repair commit is `becbbb58dc59a9f548ddb2c2628cbc5cb1404616`.

## Frozen input authority

- GA source run: `34197207582`.
- GA home job: `101967543808`.
- GA artifact ID: `10051382493`.
- GA artifact digest: `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.
- Frozen source head: `de83e20a68f79ccf25b89b0d33eb4206e294c757`.
- Frozen contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.
- Repaired GA comparator blob: `6e7b45578c647a70233fec7db7d0a1d3c88d1774`.
- GB verifier blob: `cc815737e658a850452d9b0f9488e703f8de84ea`.

## Gate

Hosted-only. No home computation and no regeneration of A or B are permitted.

1. Download exactly artifact `10051382493` and require exact SHA256 digest above.
2. Download the exact source home-job log `101967543808` and require both full-chain-before-prune PASS tokens plus `PASS_EXP073GA_LIVE_EXCLUSIVITY`.
3. Re-run only the repaired terminal comparator over the immutable materialized artifact, writing `terminal_receipt.json`.
4. Candidate PASS requires exactly `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, `classification=SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`, exact namespaces `checkpoints/exp073ga-ww-s3-s3-{a,b}-v0-1`, `S3->S3/[3,3]`, same-field handoff, canonical `<f8 [39,12288] EE<-EE`, exact SHA equality, `numpy.array_equal=true`, all finite, complete stage-manifest SHA validation and no tolerance rescue.
5. Only after candidate PASS, run the already-frozen GB verifier over the same materialized artifact and combined source/candidate log.
6. Scientific authority is admitted only if the verifier emits all three exact lines:
   - `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
   - `classification=SCIENTIFIC_AUTHORITY_ADMITTED`
   - `ww_s3_s3_authority_created=true`

Any digest, provenance, namespace, stage hash, payload hash, exact equality, finiteness or verifier mismatch is fail-closed. No tolerance, rounding, smoothing, averaging, effective-coordinate, arithmetic, domain, source-order or checkpoint-identity weakening is permitted.

## Accounting

The historical GA run failure remains implementation/infrastructure FAIL `+0/+0` and is never rewritten. Exp073HE may create `WW_S3_S3` authority only by validating the already completed frozen A/B materialized evidence through the prospectively repaired comparator and unchanged GB gate.
