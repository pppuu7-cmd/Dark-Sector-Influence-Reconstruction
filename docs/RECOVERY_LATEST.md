# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_IH_DOMAIN_PASS_II_ANGULAR_INVENTORY_FRONT_V50.md` (creation commit `5f5874ac5b1551444c7ee2cf85988f9efd7201fe`). Earlier recovery notes remain immutable history.

## Preserved scientific authority
All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

C2 admitted tangent numerical authority remains Exp073ID `34249671091 / 102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`, base step `1e-4`.

## C2 mapping/prediction authority preserved
Exp073IF `34250714613 / 102144147469` raw-log PASS admitted the six-component C2 mapping artifact: `mapping_ready=true`. Mapping blob `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`, SHA256 `7f660b6806494b00d17caed50b7cc66d01d9d02bc4cb1d66f333c1c12e1386df`.

Exp073IG `34251593341 / 102147045097` is now terminal SUCCESS and raw-log PASS: `PASS_EXP073IG_C2_LOCAL_TANGENT_PREDICTION_ARTIFACT_ADMISSION_V0_1`; `prediction_ready=true`, `scientific_model_authority_created=false`. Frozen 28-record payload blob `b3c5dc5ec6aefb79f215c5e01d7baef566cc5251`, SHA256 `2836a3665e6bab75587957228fbd3b9e152ef7d6e667966c308d81bf666c7c56`.

## First closed C2 scientific funnel gate
Exp073IH run `34251721583`, job `102147505217`, head `08a3750cbbd59ad41102c59896231769b65eff93` is terminal SUCCESS and its raw log emitted exact scientific token `PASS_EXP073IH_C2_G_DOMAIN_MAPPING_V0_1`.

Authoritative C2 funnel state now includes:
- `G_DOMAIN_MAPPING=PASS`;
- `mapping_ready=true`;
- `prediction_ready=true`;
- `numerically_evaluated=true` only for `G_DOMAIN_MAPPING`;
- `G_ANGULAR_AUTHORITY=NOT_YET_TESTABLE`;
- all later mandatory gates `NOT_YET_TESTABLE`;
- `overall_status=NOT_YET_TESTABLE`;
- `scientific_model_authority_created=false`.

This is not a complete C2/model PASS.

## Current frontier — Exp073II WW angular-authority inventory
The current authoritative binding contract is `docs/dsir4/DSIR4_ANGULAR_AUTHORITY_BINDING_CONTRACT_V0_1.md`, git blob `af2cdbfa03e0a68c24df8d1009c723d411d2d0a2`. Newest repository authority supersedes stale chat summaries: this contract requires the complete symmetric **WW** authority set `S0_S0,S0_S1,S0_S2,S0_S3,S1_S1,S1_S2,S1_S3,S2_S2,S2_S3,S3_S3`, with exact authority-admission provenance and canonical `EE<-EE <f8 [39,12288]`, DES NSIDE=4096, ell 0..12287, 39 bands.

A consolidated C2 angular receipt was not present, so no angular PASS has been asserted.

Prospective Exp073II prereg: `docs/dsir4/prereg/EXP073II_C2_WW_ANGULAR_AUTHORITY_INVENTORY_AUDIT_V0_1.md`; creation commit `7d25f5a402ad7c0c10586b30dd380504c76e7d50`; blob `53b447675ec3af6c9327f1504a243c9681532c6b`. Workflow/head commit `6f75e323cc938ec861e9cc659fbb6710f9d571e0`; run `34252435914`; job `102149881007`; GitHub-hosted `ubuntu-24.04`; home/self-hosted runner free. State at pointer update: QUEUED.

II is support-only and will inventory repository/history evidence for all ten WW pairs. Even on PASS it must preserve `G_ANGULAR_AUTHORITY=NOT_YET_TESTABLE`, `angular_authority_receipt_created=false`, `scientific_model_authority_created=false` until exact pair authorities are individually recovered and bound in a later frozen receipt.

## Exact next transition
Consume Exp073II terminal raw log plus artifact (`inventory.tsv`, `matches.txt`, `history.txt`, `SUMMARY.txt`). Trace each of the ten pair evidence sets to exact admitted run/job/head/artifact/checkpoint authority. Only if all exact required authorities are recoverable may a separate prospectively frozen candidate-local angular receipt/admission gate be created. Otherwise record exact missing pair(s) as `NOT_YET_TESTABLE` and restore original source authority without surrogate/tolerance rescue.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.