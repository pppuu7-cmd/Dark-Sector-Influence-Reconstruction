# DSIR current-process ledger

Updated: 2026-09-06. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0` Exp073EO, `S0_S1` Exp073EZ, `S0_S2` Exp073FF, `S0_S3` **Exp073FN `34050154578 / 101532191756`**, token `PASS_EXP073FN_WW_S0_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

Exp073FG candidate provenance remains run/job `34034377795 / 101489679508`, artifact `9993520467`, exact ZIP SHA256 `8ddd1e1b81e5fa9c3a4de16c6d72b35353cb42bba04bb77c736aa4998340bde0`, selected exact A/B SHA `db58af980e2997ebbe327ce91dfafb682c38fda1ba841c3d5acba78e429007d3`. Historical collided S0S3 admission run `34047839320 / 101525992295` remains `INFRASTRUCTURE_LOG_TRANSPORT_FAIL_PLUS_0_PLUS_0`; canonical Exp073FL remains the earlier S1S1 static audit.

## Newly closed hosted support for WW_S1_S1

- Exp073FO `34050224161 / 101532385479`: `PASS_EXP073FO_WW_S1_S1_PRODUCTION_TRANSFORMATION_READINESS_V0_1`, `SUPPORT_PLUS_0_PLUS_0`.
- Exp073FP `34050445433 / 101532983406`: `PASS_EXP073FP_WW_S1_S1_EXACT_PRODUCTION_DRIVER_STATIC_AUDIT_V0_1`, `SUPPORT_PLUS_0_PLUS_0`.
- Exp073FQ `34050588344 / 101533366352`: `PASS_EXP073FQ_WW_S1_S1_HOME_ENVELOPE_STATIC_AUDIT_V0_1`, `SUPPORT_PLUS_0_PLUS_0`.
- Exp073FM hosted-launch job `101533554310`: raw token `PASS_EXP073FM_HOSTED_LAUNCH_AUDIT_V0_1`, `SUPPORT_PLUS_0_PLUS_0`.
None of these support gates creates WW_S1_S1 authority.

Frozen committed Exp073FM implementation blobs: driver v0.1 `477647c5164264665cc16e20d1577fb25cd245f4`; driver v0.2 `8e3edff39aae95d3abc3196806802c5f0ae59832`; verify/prune `8e04e99084aed582f9586e3f316c023650ce6c63`; terminal comparator `02d69d5d517c676b3ec0963380f93d13f2b9874e`; home envelope `873232cc96f9a97afefeff1ff0a433fd5b49a5a2`.

## Authoritative current process — Exp073FM WW_S1_S1 home science

- workflow/run: **`34050657030`**;
- home job: **`101533574294`**;
- branch/head: `main` / **`f0caca0c3e812710e5958ee13348a150d045a7d8`**;
- state at latest reconciliation: **IN_PROGRESS** step `Run frozen WW_S1_S1 A/B gate with durable checkpoints`;
- runner ownership: **`DSIR-HOME-PC` exclusively owned by job `101533574294`**;
- live Actions at reconciliation: exactly **1 in-progress DSIR run and 0 queued runs**;
- no competing self-hosted/home task may be launched;
- science checkpoint namespaces: `checkpoints/exp073fm-ww-s1-s1-a-v0-1`, `checkpoints/exp073fm-ww-s1-s1-b-v0-1`;
- last durable checkpoint: **UNKNOWN_NOT_INSPECTED_WHILE_RUNNING**; partial numerical output must not be inspected;
- expected candidate token: `PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- next action on terminal SUCCESS: download artifact, independently verify ZIP digest, both complete six-stage/prune chains, S1 same-object semantics, exact file-backed MCM proof, exact A/B canonical arrays, and frozen source/contract/checkpoint identities, then classify candidate; a separate provenance admission is mandatory before authority;
- next action on infrastructure/resource FAIL: inspect first causal failure, preserve any verified complete-stage checkpoints, make only the smallest prospective repair, and resume from the last verified checkpoint without changing frozen science;
- next action on genuine exact numerical mismatch: record `SCIENTIFIC_FAIL`; never rescue with tolerance/rounding/smoothing/averaging.

## Prospectively frozen next authority gate — canonical Exp073FR

While Exp073FM remains in progress and before reading any partial/terminal numerical result, Exp073FR was preregistered as the sole prospective `WW_S1_S1` provenance-admission gate.

- prereg path: `experiments/073fr_ww_s1_s1_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`;
- creation commit: `55fa8c56ec8bb7e7cb0d278870a05619c5a59f67`;
- prereg blob: `aa08636426dd48142c3a3da7c032f1075a1be1f9`;
- frozen admission PASS token: `PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- Exp073FR must not run until Exp073FM is terminal and independently consumed;
- Exp073FR is hosted-only, creates no home-runner ownership, and may create authority only if every frozen terminal artifact/checkpoint/source/same-object/file-backed/exact-equality check passes.

A later pre-terminal automatic/duplicate Exp073FR implementation was removed from active `main`; the active workflow path `.github/workflows/exp073fr-ww-s1-s1-provenance-admission-and-dispatch-v0-1.yml` is intentionally absent while FM runs. Canonical prereg above remains authority.

## Reconciled future successor staging — support only

Another DSIR process prospectively staged successor transforms/workflows while Exp073FM runs. These do not supersede the current frontier and do not create authority.

- Exp073FS future `WW_S1_S2` queue/static audit `34054103704 / 101542730121`: raw `PASS_EXP073FS_AUTONOMOUS_QUEUE_STATIC_AUDIT_V0_1`, `SUPPORT_PLUS_0_PLUS_0`, `self_hosted_science_started=false`. Its heavy workflow is `workflow_dispatch` only and requires an explicit successful Exp073FR admission predecessor before a home job can start.
- Exp073FU future `WW_S1_S3` static audit v0.1 `34054723711 / 101544419091`: implementation/static FAIL `+0/+0`, first causal failure `AssertionError: Exp073FS`; no science ran. Minimal transform-only repair commit `5c0d75a57c909b0a0b699bbe79a5b5ab15c0f852` preserved science. Repaired v0.2 `34054859313 / 101544834479`: raw `PASS_EXP073FU_WW_S1_S3_TRANSFORMATION_STATIC_AUDIT_V0_2`, `SUPPORT_PLUS_0_PLUS_0`, `self_hosted_science_started=false`.
- Later staged Exp073FW/FX (`WW_S2_S2`), Exp073FY/FZ (`WW_S2_S3`) and Exp073GA/GB (`WW_S3_S3`) commits are prereg/transformation preparation only. Their presence on `main` is not scientific PASS and they are not running.

Immutable reconciliation note: `docs/recovery/RECOVERY_2026-09-06_EXP073FS_FU_STAGED_FM_RUNNING.md`. Research-log supplement: `docs/research_log/RESEARCH_LOG_2026-09-06_EXP073FS_FU_STAGING.md`.

## Frozen WW_S1_S1 science

Target `[1,1]`: authoritative S1 reconstructed exactly once per replica; exactly one spin-2 field; identical Python field object passed on both coupling sides; equal-but-distinct field forbidden; NSIDE=4096; ell `0..12287`; 39 bands; public file-backed BPW; canonical `<f8 [39,12288]` `EE<-EE`; exact SHA + `numpy.array_equal`; no tolerance/rounding/smoothing/averaging/manual/effective-coordinate/fiducial rescue. Candidate creates no authority.

## Global frozen boundaries

Unless prospectively superseded: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
