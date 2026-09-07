# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_FU_SCHEMA_VALIDATION_PASS_RESUME_ACTIVE_V04.md` (creation commit `b48d275a1d4d58f7bdacbec9637f1d480b266146`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities remain `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`. `WW_S1_S3` is **not admitted**.

`WW_S1_S2` authority remains created only by Exp073FT inside run `34067352681`, job `101632852284`, exact token `PASS_EXP073FT_WW_S1_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Underlying Exp073FS attempt-2 artifact `10005532345`, ZIP SHA256 `f878a49241dde97eb0ef1d24561719cf896a77d111c3a3b91725d4989b894d23`; canonical A/B SHA256 `77f3e314d76f85cb95ed8edade672575bfa0e40c3b10a831f380a6c6d5f977fd`.

## Exp073FU repair validation — closed support +0/+0

Historical Exp073FU run `34089383137` remains implementation/infrastructure FAIL `+0/+0`; it created no `WW_S1_S3` authority. Preserved checkpoint A was proven valid. The causal pruner defect was missing underscore schema transform `ww_s1_s2 -> ww_s1_s3`.

Prospective repair commit `dabb334aecaf924ad5a48ac495a5447deb4c6583`, repaired pruner blob `b9ed7d7178424fb656b4a7c7bfb2ee370c751cb0`.

Read-only validation run `34103206078`, job `101682164394`, completed SUCCESS and raw-log verification confirmed:

- `PASS_EXP073FU_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`;
- `original_checkpoint_mutated=false`;
- `PASS_EXP073FU_REPLICA_A_REPAIRED_PRUNER_READONLY_VALIDATION_V0_6`.

Classification is support/implementation `+0/+0` only; no science authority was created.

## Current heavy frontier — repaired Exp073FU checkpoint resume

Newer repository authority from another DSIR process was reconciled and accepted:

- production wrapper binding commit `cfd67ce78428bf029a42a922bdb202112f77ce07`, wrapper blob `b6ac5d8ba4472b04efedb4b1a732980428cf4c82`;
- resume workflow/head commit `85eb20e70a9fa6d8d444aaaf368dd396e164769c`;
- research-log commit `c731d499413739c7be38382242547599f16ce852`.

Authoritative current process:

- Exp073FU run `34103803637`;
- hosted launch audit job `101684090730`: SUCCESS;
- home-science job `101684145754`: IN_PROGRESS at latest reconciliation;
- active step: frozen `WW_S1_S3 A/B gate with durable checkpoints`;
- checkpoint root: `~/.cache/dsir/exp073fu-ww-s1-s3-filebacked-ab-v0-1`, A/B durable trees;
- predecessor admitted run: Exp073FS/FT `34067352681`;
- queued DSIR runs: 0; in-progress DSIR runs: exactly 1 (`34103803637`);
- no partial numerical output inspected and no competing home job launched.

The workflow currently retains a temporary path-scoped push trigger used for this one-shot resume. Do not edit that workflow while the active run is executing if doing so could generate a duplicate. Restore dispatch-only semantics at a safe terminal/authority transition.

Exact next action: on terminal `34103803637`, consume raw jobs/logs/artifact; verify artifact digest, complete checkpoint/provenance chain, restored-versus-new work, ordered `[1,3]`, distinct fields, frozen identities, exact file-backed proof, canonical `<f8 [39,12288] EE<-EE`, finiteness and exact A/B equality. Workflow success alone is not scientific PASS. Only validated candidate PASS permits Exp073FV admission; only FV may create `WW_S1_S3` authority.

## Independent C2 support frontier

C2 IDE remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. Exp073GL repaired hosted support PASS and Exp073GM hosted observation-only extraction-patch specification PASS remain support-only and create no model authority. No C2 numerical generation is authorized merely by these static audits.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
