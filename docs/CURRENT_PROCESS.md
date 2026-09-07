# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`. `WW_S2_S2` is **NOT ADMITTED**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_EXP073FW_A_PRESERVED_PRUNER_REPAIR_RESUME_V13.md`, creation commit `6940913d435609625ee52888e02915810f251c17`.

## Terminal predecessor — Exp073FW run 34125785882

- head `1c635f5192d26e76e0ec82a308363b666e5a248b`;
- hosted job `101754018941` SUCCESS;
- home job `101754061309` FAILURE;
- admission job `101785905987` SKIPPED;
- classification `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, first cause `fail-closed missing FW pruner token 'WW_S1_S1'` after complete Replica A;
- artifact `10023848524`, independently verified ZIP SHA256 `33b5999213247a9ad0c66957a021067f4f790f04d19eb1cf8d88910187eea66f`;
- complete preserved A checkpoint chain through `replica_receipt_complete`; selected A SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`; no B.

Repair authority: commit `2a6a06f9d468879ca814ced15a56f82169507b3a`, pruner blob `fb66e67d88a90b093a7da8b42ab0ac6fee13b504`; workflow binding `f7e925e782983824b7e916ce8437fcf924ec5760`, workflow blob `c7c651dfeac8a9d4a2d3da1dd6b11d7873af612a`. Frozen science unchanged.

## Authoritative current process — Exp073FW repaired checkpoint-first resume

- workflow/run: **`34135965569`**;
- branch/head: `main` / **`f7e925e782983824b7e916ce8437fcf924ec5760`**;
- hosted launch audit job: **`101786894169` SUCCESS**;
- hosted raw token: `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`, `classification=SUPPORT_PLUS_0_PLUS_0`;
- home-science job: **`101786993129` IN_PROGRESS**;
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`;
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- last verified durable checkpoint: complete Replica A as identified above;
- expected gate: frozen WW `S2->S2`, same-field semantics, canonical `<f8 [39,12288] EE<-EE`, exact A/B equality, exact `19,327,352,832`-byte file-backed MCM proof, no tolerance rescue;
- exact next action on SUCCESS: terminal-consume raw logs/artifact, independently verify restored-vs-new provenance and complete A/B evidence; only then permit frozen Exp073FX admission;
- exact next action on FAIL/BLOCKED: preserve complete checkpoints, diagnose first causal defect, smallest prospective repair/resume; genuine frozen numerical mismatch is a scientific FAIL and never repaired post hoc.

No competing heavy run is permitted. Do not inspect partial numerical output. Current workflow retains a path-scoped one-shot push trigger; do not edit it while `34135965569` is active because that could duplicate the run. Restore dispatch-only semantics at safe terminal transition.

## Independent C2 frontier

C2 remains support-only: `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, `+0/+0`. Exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`. No real C2 extraction while FW owns home.

Exp073GR/GS/GT/GU remain preserved support PASS. Exp073GV run `34135739339`, job `101786143296`, raw-validated token `PASS_EXP073GV_C2_IDE_RECORD_PACKET_ADMISSION_STATIC_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`; deterministic synthetic 64-byte vector only, scientific record/prediction/model authority false.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
