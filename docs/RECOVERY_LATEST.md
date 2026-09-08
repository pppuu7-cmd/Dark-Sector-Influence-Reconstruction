# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_IF_IG_PASS_IH_DOMAIN_GATE_FRONT_V49.md` (creation commit `47ee3a9f79cf2a819d16c17fe8f28edb13a3b336`). Earlier recovery notes remain immutable history.

## Preserved scientific authority
All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

C2 admitted tangent numerical authority remains Exp073ID `34249671091 / 102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`, base step `1e-4`.

## Newly admitted C2 mapping and prediction infrastructure
Exp073IF run `34250714613 / 102144147469` raw-log PASS: `PASS_EXP073IF_C2_RESIDUAL_MAPPING_ARTIFACT_ADMISSION_V0_1`, classification `MAPPING_ARTIFACT_ADMITTED_PLUS_0_PLUS_0`, `mapping_ready=true`. Mapping artifact blob `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`, SHA256 `7f660b6806494b00d17caed50b7cc66d01d9d02bc4cb1d66f333c1c12e1386df`.

Exp073IG run `34251593341 / 102147045097` raw-log PASS: `PASS_EXP073IG_C2_LOCAL_TANGENT_PREDICTION_ARTIFACT_ADMISSION_V0_1`, classification `PREDICTION_ARTIFACT_ADMITTED_PLUS_0_PLUS_0`, `prediction_ready=true`, `numerically_evaluated=false`, `scientific_model_authority_created=false`. Frozen 28-record prediction-basis payload blob `b3c5dc5ec6aefb79f215c5e01d7baef566cc5251`, SHA256 `2836a3665e6bab75587957228fbd3b9e152ef7d6e667966c308d81bf666c7c56`; metadata artifact blob `7e244010ca65050d0c8edff8fe90a9583845a568`.

The frozen local rule is `Delta_pred = Delta_ref + alpha*dDelta_dalpha + beta*dDelta_dbeta`, with alpha left-sided at the origin, beta two-sided, admitted derivative step `1e-4`, and no finite-distance extrapolation/interpolation/rescue.

## Current frontier — Exp073IH C2 G_DOMAIN_MAPPING scientific gate v0.1
Prospective prereg: `docs/dsir4/prereg/EXP073IH_C2_G_DOMAIN_MAPPING_SCIENTIFIC_GATE_V0_1.md`; creation commit `03208ce2b4cffba352dc927471594ea65873cb14`; blob `63ea9e9c11b1f77353af613eb8236b5c5961b1fd`. Workflow/head commit `08a3750cbbd59ad41102c59896231769b65eff93`; run `34251721583`; job `102147505217`; GitHub-hosted ubuntu-24.04; home/self-hosted runner free. State at pointer update: QUEUED.

Expected exact scientific token: `PASS_EXP073IH_C2_G_DOMAIN_MAPPING_V0_1`. Frozen PASS rule requires exact IF/IG raw authority, complete six-component common residual mapping, total-sector/Q bookkeeping, exact pinned solver/gauge/regime provenance, certified envelope `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`, immutable local-tangent prediction identity, and explicit no-extrapolation rules. The gate does not claim the 28-point payload supplies continuous support for later angular/radial gates.

On IH PASS only: `G_DOMAIN_MAPPING=PASS`; `G_ANGULAR_AUTHORITY` and every later mandatory gate remain `NOT_YET_TESTABLE`; therefore `overall_status=NOT_YET_TESTABLE` and `scientific_model_authority_created=false`.

## Exact next transition
Consume IH terminal raw log. If PASS, record the first closed C2 DSIR-4 funnel gate, then audit the exact required angular observational authority set before prospectively defining `G_ANGULAR_AUTHORITY`. Never substitute theory-space tangent evidence for angular authority. On implementation/provenance failure, repair only the first causal defect without changing the frozen scientific criterion.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
