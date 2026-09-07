# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_FU_SCHEMA_IDENTITY_REPAIR_V03.md` (creation commit `77474e39f9259d430be028bbc7466d919f689db4`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities remain `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`. `WW_S1_S3` is **not admitted**.

`WW_S1_S2` authority remains created only by Exp073FT inside run `34067352681`, job `101632852284`, exact token `PASS_EXP073FT_WW_S1_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Underlying Exp073FS attempt-2 artifact `10005532345`, ZIP SHA256 `f878a49241dde97eb0ef1d24561719cf896a77d111c3a3b91725d4989b894d23`; canonical A/B SHA256 `77f3e314d76f85cb95ed8edade672575bfa0e40c3b10a831f380a6c6d5f977fd`.

## Current heavy frontier — Exp073FU repair/resume

Exp073FU run `34089383137` is terminal implementation/infrastructure FAIL `+0/+0`; no `WW_S1_S3` scientific gate was admitted and no authority artifact was produced. Valid durable checkpoints under `~/.cache/dsir/exp073fu-ww-s1-s3-filebacked-ab-v0-1` remain preserved.

Read-only diagnostic run `34100007783` attempt 3 reached user code and failed on `fresh_sources_complete` stage identity. Follow-up diagnostic `34103112711 / 101681869890` proved the preserved A manifest is itself correct, including schema `dsir.exp073fu.ww_s1_s3.durable_ab_production.v0.1.checkpoint`, namespace `checkpoints/exp073fu-ww-s1-s3-a-v0-1`, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, and both historical/import flags false.

The first causal software defect was therefore isolated to the FU transformed pruner: it omitted underscore schema transform `ww_s1_s2 -> ww_s1_s3`. Prospective repair commit `dabb334aecaf924ad5a48ac495a5447deb4c6583`, repaired pruner blob `b9ed7d7178424fb656b4a7c7bfb2ee370c751cb0`; no science arithmetic/domain/acceptance/tolerance/source/contract semantics changed.

Read-only validation binding commit `2f5e33324ef032bb048e43acc27e8e6a94ccb2cc` launched run `34103206078`, job `101682164394`; at latest reconciliation it is the only permitted self-hosted validation process and was `IN_PROGRESS`. It operates on a symlink mirror and may not mutate canonical checkpoints.

Exact next action: consume run `34103206078` raw log. Only exact PASS token `PASS_EXP073FU_REPLICA_A_REPAIRED_PRUNER_READONLY_VALIDATION_V0_6` plus `original_checkpoint_mutated=false` permits a prospective FU resume from preserved durable checkpoints. Any failure remains infrastructure/implementation `+0/+0` until diagnosed. Only a future fully validated FU candidate can permit Exp073FV authority admission.

## Independent C2 support frontier

C2 IDE remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. Exp073GL repaired hosted support PASS and Exp073GM hosted observation-only extraction-patch specification PASS remain support-only and create no model authority. No C2 numerical generation is authorized merely by these static audits.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
