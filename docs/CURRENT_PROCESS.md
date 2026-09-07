# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`. `WW_S1_S3` is NOT ADMITTED.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-07_FU_SCHEMA_VALIDATION_PASS_RESUME_ACTIVE_V04.md`, creation commit `b48d275a1d4d58f7bdacbec9637f1d480b266146`.

## Newly closed support validation

Read-only repaired-pruner validation run `34103206078`, job `101682164394`, completed SUCCESS on `DSIR-HOME-PC-2`. Raw log independently verified exact tokens:

- `PASS_EXP073FU_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`
- `original_checkpoint_mutated=false`
- `PASS_EXP073FU_REPLICA_A_REPAIRED_PRUNER_READONLY_VALIDATION_V0_6`

Repaired pruner blob: `b9ed7d7178424fb656b4a7c7bfb2ee370c751cb0`. Classification: support/implementation `+0/+0`; no scientific authority.

## Authoritative current process — Exp073FU repaired checkpoint resume

- workflow/run: **Exp073FU `34103803637`**;
- event: one-shot path-scoped `push`;
- branch/head: `main` / **`85eb20e70a9fa6d8d444aaaf368dd396e164769c`**;
- production wrapper binding commit: `cfd67ce78428bf029a42a922bdb202112f77ce07`;
- wrapper blob: `b6ac5d8ba4472b04efedb4b1a732980428cf4c82`;
- repaired pruner blob: `b9ed7d7178424fb656b4a7c7bfb2ee370c751cb0`;
- hosted launch audit job: **`101684090730` SUCCESS**;
- home-science job: **`101684145754` IN_PROGRESS** at latest reconciliation;
- active step: `Run frozen WW_S1_S3 A/B gate with durable checkpoints`;
- runner ownership: self-hosted DSIR home runner is exclusively owned by job `101684145754` while active;
- checkpoint root: `~/.cache/dsir/exp073fu-ww-s1-s3-filebacked-ab-v0-1`, replicas `/checkpoints/A` and `/checkpoints/B`;
- predecessor authority run: Exp073FS/FT `34067352681`;
- frozen source head: `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- expected gate: ordered `[1,3] = S1->S3`, distinct fields, DES NSIDE=4096, ell `0..12287`, 39 bands, public file-backed BPW, canonical `<f8 [39,12288] EE<-EE`, exact A/B SHA and array equality, all finite;
- queued DSIR workflows: **0**;
- in-progress DSIR workflows: **exactly 1**, run `34103803637`;
- partial numerical output: **NOT INSPECTED**;
- competing heavy job: **NONE**.

Historical FU run `34089383137` remains implementation/infrastructure FAIL `+0/+0`, not scientific FAIL. Its valid durable checkpoints are being reused; verified expensive stages must not be recomputed unnecessarily.

Exact next action on terminal SUCCESS: consume raw jobs/logs/artifact; independently verify artifact digest, checkpoint and restore provenance, ordered S1->S3 distinct-field semantics, frozen identities, exact file-backed proof, canonical finiteness and exact A/B equality. Workflow success alone is not scientific PASS. Only a validated candidate permits frozen Exp073FV admission; only FV may create `WW_S1_S3` authority.

Exact next action on infrastructure/resource FAIL: preserve verified complete checkpoints, diagnose first causal failure, smallest prospective repair/resume. Exact numerical mismatch under frozen contract is a scientific FAIL with no tolerance rescue.

## Trigger safety

The Exp073FU workflow currently retains the temporary path-scoped push trigger used for this resume. Do not modify that workflow while `34103803637` is active if the change would trigger a competing FU run. Repository/doc-only commits are outside its path filter. Restore dispatch-only semantics at a safe terminal/authority transition.

## Independent C2 frontier

C2 IDE remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. Exp073GL and Exp073GM are support-only static PASSes and do not authorize model authority or numerical prediction generation by themselves.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
