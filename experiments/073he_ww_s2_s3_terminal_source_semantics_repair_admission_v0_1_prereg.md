# Exp073HE — WW_S2_S3 terminal source-semantics repair/admission v0.1 preregistration

Scope: DSIR only.

Purpose: consume the already-computed Exp073FY recovery evidence from run 34160898921 without any home/heavy recomputation. Exp073HD run 34188961637 proved its exact NumPy dependency repair, then stopped fail-closed before numerical comparison because the transformed FS comparator still required stale `reconstruction_counts={'s1':1,'s2':1}` although the prospectively frozen FY source pair is S2->S3 and the preserved artifact records `{'s2':1,'s3':1}` for both replicas.

Frozen evidence source: Actions run 34160898921, home job 101862390771, artifact 10040351900, artifact digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

Frozen repair comparator blob: `7698487dd137ec4c2b4f3f2faa158aeb6846ef78`. It is derived from the same frozen FS comparator blob `826fcefc8ce64a26e8c8205b1898f63c42ffc0f0` and changes only two exact implementation identities required for FY: checkpoint namespace `exp073fs-ww-s1-s2` -> `exp073fy-ww-s2-s3`, and reconstruction-count semantics `{'s1':1,'s2':1}` -> `{'s2':1,'s3':1}`. Generic frozen label/source transforms remain the same. No arithmetic, selected payload bytes, source ordering, domain, tolerance, rounding, smoothing, averaging, contract fingerprint, source head, or hypothesis identity may change.

Frozen provenance verifier remains `ci/exp073fz_verify_fy_candidate_v0_1.py` blob `c3f967c8fc9efed017bb6d5794d53433afefd4ac`.

Gate procedure: hosted-only. Pin prereg/comparator/FZ blobs; verify source run/job/artifact identity and digest; require original run log markers `PASS_EXP073FY_LIVE_EXCLUSIVITY`, `PASS_EXP073FY_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`, `PASS_EXP073FY_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`, and the known post-compute namespace failure; download the same artifact; run HE comparator over the preserved bytes; require exact candidate PASS `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; append comparator token to the original log and execute the frozen FZ verifier.

Classification: blob/artifact/provenance/source-semantics mismatch is INFRASTRUCTURE/IMPLEMENTATION/PROVENANCE failure +0/+0 and creates no scientific authority. Only after all frozen provenance/source checks pass, exact selected-array inequality or non-finiteness is a scientific FAIL. PASS authority requires exact FZ token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s2_s3_authority_created=true`.

No home runner or heavy computation is permitted by Exp073HE.
