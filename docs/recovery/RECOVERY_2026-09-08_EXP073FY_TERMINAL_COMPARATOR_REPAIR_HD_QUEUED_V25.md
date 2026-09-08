# DSIR recovery — FY terminal comparator repair / Exp073HD queued V25

Date: 2026-09-08. Scope: DSIR only.

Exp073FY namespace-repair V0.3 run `34160898921` is terminal FAILURE, but not a scientific arithmetic failure. Hosted audit job `101862362835` succeeded. Home job `101862390771` completed both expensive replicas and emitted `PASS_EXP073FY_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1` and `PASS_EXP073FY_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`. The first terminal causal failure occurred afterward in `ci/exp073fy_compare_terminal_receipts_v0_1.py`: `RuntimeError: fail-closed receipt identity A:checkpoint_namespace`.

Artifact `10040351900`, digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`, preserves both complete post-prune chains and canonical EE payloads. Independent consumption verified both receipts carry correct namespaces `checkpoints/exp073fy-ww-s2-s3-{a,b}-v0-1`, source pair `S2->S3`, ordered indices `[2,3]`, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, and selected EE SHA256 `3a787a12152ec023b6747145ec96345bc805ab0c96b5a26d0b528a9d68672de2` for both A and B. The two canonical `selected_ee.bin` payloads are byte-identical. This evidence is not authority until the frozen comparator and FZ admission both pass.

Root cause: the FY comparator wrapper transformed underscore science tokens but did not transform the hyphenated namespace literal inherited from Exp073FS. Therefore it incorrectly expected an S1-S2 namespace despite correct preserved S2-S3 checkpoint identity. Classification: implementation/provenance FAIL `+0/+0`, not scientific FAIL.

Prospective minimal repair commit `950bf2334ce192b18bf96df7498c68a3e4a7a52e`, comparator blob `5ccce6c459a5ce541fcccc6b576e78c531fea01f`, adds the exact hyphenated namespace transform and static stale/correct namespace assertions only. No arithmetic, domain, source ordering, payload, tolerance, rounding, smoothing or averaging changed.

Exp073HD was preregistered in commit `293d56e9c7e0cca24875b42586a47076163ef4f0`, prereg blob `531253189d9e250cc4617564c44256d2e4ba27c0`. Hosted-only recovery/admission workflow commit `2f99b9f9d8d078675731c30a080afaba66e04be9` launched run `34188871787`. It is queued at this recovery snapshot. The gate pins artifact `10040351900`, its digest, repaired comparator blob, and frozen FZ verifier blob `c3f967c8fc9efed017bb6d5794d53433afefd4ac`; it reuses the exact original source-job log markers and performs no home recomputation.

`WW_S2_S3` remains NOT ADMITTED until Exp073HD emits exact candidate token `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, exact admission token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, and `ww_s2_s3_authority_created=true` from validation of the frozen artifact bytes.

No self-hosted heavy run is currently authoritative. Do not launch GA or C2 runtime until Exp073HD is consumed. On HD PASS, `WW_S2_S3` becomes admitted and the already preregistered/hardened Exp073GA `WW_S3_S3` successor is the next heavy gate. On HD infrastructure/provenance failure, preserve the FY artifact and diagnose only the first causal defect. On genuine exact comparator inequality/non-finiteness with otherwise valid evidence, classify scientific FAIL and do not repair the science.
