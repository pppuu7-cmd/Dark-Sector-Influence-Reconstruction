# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_EXP073FY_TERMINAL_COMPARATOR_REPAIR_HD_QUEUED_V25.md` (creation commit `aa3c58f3054820dbd2bd8b5e7a2b9abbdabf40d3`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, and `S2_S2`. `WW_S2_S3` remains **NOT ADMITTED** pending the current frozen recovery/admission gate.

## Exp073FY terminal result

Exp073FY namespace-repair V0.3 run `34160898921` is terminal FAILURE, classified implementation/provenance `+0/+0`, not scientific FAIL. Hosted audit job `101862362835` succeeded. Home job `101862390771` completed both expensive replicas and emitted `PASS_EXP073FY_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1` and `PASS_EXP073FY_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`. The first causal failure occurred only in the terminal comparator: `RuntimeError: fail-closed receipt identity A:checkpoint_namespace`.

Artifact `10040351900`, digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`, preserves both complete chains. Independently checked A and B receipts have exact checkpoint namespaces `checkpoints/exp073fy-ww-s2-s3-{a,b}-v0-1`, ordered `S2->S3`, `[2,3]`, frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, and identical canonical `<f8 [39,12288] EE<-EE` SHA256 `3a787a12152ec023b6747145ec96345bc805ab0c96b5a26d0b528a9d68672de2`. Byte equality of the two preserved canonical payloads was independently confirmed. This is candidate evidence only; authority still requires the frozen comparator plus FZ admission.

Root cause: the FY comparator wrapper transformed underscore science tokens but omitted the inherited hyphenated namespace literal. Prospective minimal repair commit `950bf2334ce192b18bf96df7498c68a3e4a7a52e`, comparator blob `5ccce6c459a5ce541fcccc6b576e78c531fea01f`, adds only the exact namespace transform and stale/correct namespace regression assertions. No frozen science arithmetic/domain/order/tolerance changed.

## Authoritative current process — Exp073HD

Exp073HD preregistration commit `293d56e9c7e0cca24875b42586a47076163ef4f0`, prereg blob `531253189d9e250cc4617564c44256d2e4ba27c0`. Hosted-only workflow commit `2f99b9f9d8d078675731c30a080afaba66e04be9` launched run **`34188871787`**, queued at latest reconciliation. It pins source run/job/artifact `34160898921 / 101862390771 / 10040351900`, exact artifact digest, repaired comparator blob, and frozen FZ verifier blob `c3f967c8fc9efed017bb6d5794d53433afefd4ac`. It performs no home recomputation.

PASS requires exact candidate token `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, exact admission token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, and `ww_s2_s3_authority_created=true` from the same frozen artifact bytes. Only then may `WW_S2_S3` become admitted and Exp073GA `WW_S3_S3` become the next heavy gate.

## Prepared final heavy successor

Exp073GA/GB remains dispatch-only until valid S2-S3 admission. Current final GB verifier blob `cc815737e658a850452d9b0f9488e703f8de84ea`; current GA workflow blob `7c408b877a5c0ddc96346cff74efffc1a1985687`. Exp073HC hosted static audit remains PASS support-only and creates no S3-S3 authority.

## Independent C2 frontier

Exp073GZ hosted static audit remains PASS `SUPPORT_PLUS_0_PLUS_0`. The next C2 transition is real frozen 28-packet / 1792-byte runtime production/admission, but it must not compete with a permitted heavy successor.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
