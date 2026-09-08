# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities are `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, and `S2_S3`. `WW_S3_S3` remains **NOT_YET_ADMITTED**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-08_GA_PRUNER_REPAIR_RESUME_V28.md` (creation commit `9e708c7aab8b2b00ee3e3fcf637728e289ac0159`).

## Newly consumed Exp073GA failure

Historical run `34189540992`, hosted job `101944582891 SUCCESS`, home job `101944608861 FAILURE`, GB job skipped. Evidence artifact `10043979600`, digest `sha256:b859e658e1046c4d9905d589003a1d26aaf3e2601c51d9db361b48176226906a` was independently downloaded and hash-matched.

First causal error after expensive Replica A completed its six-stage chain: `RuntimeError: fail-closed missing GA pruner token 'WW_S1_S1'`. The pinned FM base does not contain that uppercase literal. Classification: **implementation/infrastructure FAIL +0/+0**, not scientific FAIL.

Preserved verified A checkpoint: namespace `checkpoints/exp073ga-ww-s3-s3-a-v0-1`; frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; ordered `[3,3]`, `S3->S3`, same-field handoff; exact `19,327,352,832`-byte file-backed proof; selected canonical `<f8 [39,12288] EE<-EE` SHA256 `e4aad74b8b733d280f4abfd6654778f0e037ab6060b12a908d30f8ec34c36c07`, independently confirmed all finite. Replica B had not started. Do not recompute verified A.

## Repair provenance

Minimal pruner repair commit: `f52fa856eb029c64f744926eecf55f506fcf1da5`; repaired pruner blob `fc3e4d8444630e4b5a2dde0a052e1069b7887c01`. Only the nonexistent uppercase transform requirement was removed.

Workflow rebinding/regression commit: `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`. Hosted regression now proves the actual pinned FM token set and `WW_S1_S1` absence before home compute. Science arithmetic/domain/order/checkpoints/tolerances unchanged.

## Authoritative current process — Exp073GA recovery

- workflow/run: **`34197207582`**;
- workflow: `.github/workflows/exp073ga-ww-s3-s3-home-science-v0-1.yml`;
- branch/head: `main` / **`f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`**;
- run start: `2026-09-08T07:00:11Z`;
- hosted launch-audit job: **`101967492875 SUCCESS`**;
- hosted tokens: `PASS_EXP073GA_PRUNER_TRANSFORM_SOURCE_STATIC_REGRESSION_V0_1`, `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_3`, classification `SUPPORT_PLUS_0_PLUS_0`;
- self-hosted home-science job: **`101967543808 IN_PROGRESS`**;
- active step: `Run frozen WW_S3_S3 A/B gate with durable checkpoints`;
- runner ownership: **single self-hosted DSIR owner; no competing home-heavy work**;
- checkpoint root: `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`;
- last verified durable checkpoint: Replica A `replica_receipt_complete` from historical run `34189540992`, to be restored/verified rather than recomputed;
- expected candidate token: `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- final authority token: `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` plus `classification=SCIENTIFIC_AUTHORITY_ADMITTED` and `ww_s3_s3_authority_created=true`.

SUCCESS action: consume raw home log/artifact and verify exact digest, code/source/contract/checkpoint identities, complete A+B chains, same-field `S3->S3/[3,3]`, exact file-backed MCM evidence, finite canonical arrays, exact SHA equality and `numpy.array_equal`; only then accept GB admission. FAIL action: diagnose first causal defect, preserve verified checkpoint stages, and never weaken science.

## Independent C2 frontier

Exp073GZ hosted static audit remains PASS `SUPPORT_PLUS_0_PLUS_0`. Real frozen 28-packet / 1792-byte runtime generation/admission remains blocked while GA owns the self-hosted heavy runner.

## Frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
