# DSIR recovery V48 — C2 IE PASS / IF mapping admission front

Updated: 2026-09-08. Scope: DSIR only. Never mix RTK or RQIR.

## Preserved scientific authority
All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. No C2 prediction/model scientific authority exists.

C2 admitted numerical tangent authority from Exp073ID remains preserved: `34249671091 / 102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`, `tangent_response_ready=true`, admitted base step `1e-4`.

## Exp073IE terminal consumption
Exp073IE run `34250165394`, job `102142253548`, head `83f997a52fe6c297599a3eaf04539c63e50a8b6f` completed SUCCESS. Raw log was consumed; workflow status alone was not used.

Raw PASS token: `PASS_EXP073IE_C2_SIX_COMPONENT_RESIDUAL_MAPPING_SOURCE_AUDIT_V0_1`.
Classification: `SUPPORT_PLUS_0_PLUS_0`.

Source fingerprints independently present in the raw log:
- `background.c` SHA256 `7a6ad5d44c316c886fc15c3439e04217c6c480f0dc251e8080aa64643ce1c6fc`;
- `perturbations.c` SHA256 `61e73ed7d5b785ea5f49620e782c58ec552d2735640a1c1241d5ef354e7e0cbe`;
- pinned solver `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

IE source-proved all six residual components in the pinned synchronous representation:
- `rho_X=rho_idm_iv+rho_iv`;
- `p_X=-rho_iv`;
- `delta_rho_X=rho_idm_iv*delta_idm_iv`;
- `q_X=0` structural zero;
- `delta_p_X=0` structural zero;
- `pi_X=0` structural zero.

It also source-proved `Q=alpha*H*rho_idm_iv+beta*H*rho_iv`, total residual `idm_iv+iv`, and the 28-request domain within `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`.

IE terminal state remains support-only: `six_component_source_mapping_ready=true`, `mapping_artifact_created=false`, `mapping_ready=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Prospectively frozen mapping artifact and Exp073IF
A new mapping artifact was frozen after IE PASS and before mapping admission:
- `docs/dsir4/mappings/C2_IDE_LOCAL_TANGENT_CONE_MAPPING_V0_1.md`;
- creation commit `543661eb745e075ffcaf6a00b8d7f4b13842740d`;
- blob `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`.

The artifact binds all six source formulas, total-sector/Q convention, synchronous gauge, exact source/config identities, the frozen DSIR coordinate domain and admitted tangent-response provenance. It explicitly creates no prediction or scientific PASS.

Exp073IF mapping-admission prereg:
- `docs/dsir4/prereg/EXP073IF_C2_RESIDUAL_MAPPING_ARTIFACT_ADMISSION_V0_1.md`;
- creation commit `da8ba6ee84f5cecafa7e631be4b6975346edd987`;
- blob `52677fe6b0d73d62d01c1f39e8b434ceda0f7e01`.

Workflow/head commit: `4be871236e01c4f39813a5902f241b3d10431cfe`.
Run: `34250714613`.
Job: `102144147469`.
Runner: GitHub-hosted `ubuntu-24.04`; home/self-hosted runner free.
State at note creation: `IN_PROGRESS`.
Expected token: `PASS_EXP073IF_C2_RESIDUAL_MAPPING_ARTIFACT_ADMISSION_V0_1`.

On IF PASS only: `classification=MAPPING_ARTIFACT_ADMITTED_PLUS_0_PLUS_0`, `mapping_artifact_created=true`, `mapping_ready=true`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=TESTABLE_NOT_EVALUATED`.

On IF failure: diagnose first provenance/static mismatch only; do not weaken formulas/domain/gauge/source identities and do not infer a scientific FAIL.

## Exact next transition
Consume IF terminal raw log. If PASS, freeze the next prediction-artifact construction/admission prospectively; mapping admission alone is not an observational evaluation. If IF fails, repair only the first causal implementation/provenance defect under the already-frozen mapping content.

Global frozen DSIR boundaries remain unchanged.