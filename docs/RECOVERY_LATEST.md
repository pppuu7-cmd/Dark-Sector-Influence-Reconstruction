# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_GA_PRUNER_REPAIR_RESUME_V28.md` (creation commit `9e708c7aab8b2b00ee3e3fcf637728e289ac0159`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, and **`S2_S3`**. `WW_S3_S3` remains **NOT_YET_ADMITTED**.

Preserved Exp073FY/HE/HF provenance remains authoritative for `WW_S2_S3`; HF run `34189183845`, job `101943539978`, emitted the exact FZ admission token, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s2_s3_authority_created=true`.

## Consumed Exp073GA failure

Exp073GA run `34189540992`, head `10e6fb67af7d6485fca3d1ecf2362e4622883417`: hosted job `101944582891 SUCCESS`, home job `101944608861 FAILURE`, GB skipped. Evidence artifact `10043979600` has GitHub digest `sha256:b859e658e1046c4d9905d589003a1d26aaf3e2601c51d9db361b48176226906a`; independently downloaded ZIP SHA256 matched.

First causal failure occurred only after Replica A completed its expensive six-stage chain and receipt: `RuntimeError: fail-closed missing GA pruner token 'WW_S1_S1'`. The pinned FM base contains no such uppercase literal. Classification: **implementation/infrastructure FAIL `+0/+0`**, not scientific FAIL.

Preserved A evidence is valid and must not be recomputed: namespace `checkpoints/exp073ga-ww-s3-s3-a-v0-1`; source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; same-field `S3->S3/[3,3]`; exact `19,327,352,832`-byte file-backed proof; canonical `<f8 [39,12288] EE<-EE` SHA256 `e4aad74b8b733d280f4abfd6654778f0e037ab6060b12a908d30f8ec34c36c07`, independently confirmed all finite. Replica B had not started.

## Prospective repair and active recovery

Minimal pruner repair commit `f52fa856eb029c64f744926eecf55f506fcf1da5`, blob `fc3e4d8444630e4b5a2dde0a052e1069b7887c01`, removes only the false absent-token requirement. Workflow rebinding/regression commit `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d` pins that blob and adds a hosted static regression proving the real pinned FM token set and absence of `WW_S1_S1`. Frozen science/arithmetic/domain/order/checkpoints/tolerances are unchanged.

Current single heavy workflow: Exp073GA recovery run **`34197207582`**, head **`f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`**. Hosted audit job **`101967492875 SUCCESS`** with `PASS_EXP073GA_PRUNER_TRANSFORM_SOURCE_STATIC_REGRESSION_V0_1`, `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_3`, classification `SUPPORT_PLUS_0_PLUS_0`. Home job **`101967543808 IN_PROGRESS`** on the frozen A/B gate. Do not launch competing home-heavy work.

Checkpoint root: `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`; last verified durable checkpoint is Replica A `replica_receipt_complete` from run `34189540992`, to be restored/verified rather than recomputed. Candidate token remains `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Only frozen GB output `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s3_s3_authority_created=true` may create final WW authority.

Research log: `docs/research_log/RESEARCH_LOG_2026-09-08_GA_PRUNER_REPAIR_RESUME_V28.md` (creation commit `b96e3aee00bb60a4228f22a9a09b30e284bc89dc`). Process ledger update commit `f6317eacb717540c95102157ccc1954d2e323246`.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
