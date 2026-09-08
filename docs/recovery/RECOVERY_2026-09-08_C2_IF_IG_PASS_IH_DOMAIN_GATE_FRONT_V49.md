# DSIR recovery V49 — C2 IF/IG PASS / IH G_DOMAIN_MAPPING front

Updated: 2026-09-08. Scope: DSIR only. RTK/RQIR excluded.

## Preserved authority
All prior DSIR authority is preserved unchanged. In particular admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. C2 has no complete model authority and no overall DSIR PASS.

C2 admitted numerical tangent authority remains Exp073ID `34249671091 / 102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`, admitted base step `1e-4`.

## Newly closed: Exp073IF mapping admission
Exp073IF run `34250714613`, job `102144147469`, head `4be871236e01c4f39813a5902f241b3d10431cfe` completed SUCCESS and its raw log was consumed.

Exact token: `PASS_EXP073IF_C2_RESIDUAL_MAPPING_ARTIFACT_ADMISSION_V0_1`.
Classification: `MAPPING_ARTIFACT_ADMITTED_PLUS_0_PLUS_0`.
State created by IF only: `six_component_source_mapping_ready=true`, `mapping_artifact_created=true`, `mapping_ready=true`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=TESTABLE_NOT_EVALUATED`.

Authoritative mapping artifact:
- path `docs/dsir4/mappings/C2_IDE_LOCAL_TANGENT_CONE_MAPPING_V0_1.md`;
- creation commit `543661eb745e075ffcaf6a00b8d7f4b13842740d`;
- git blob `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`;
- SHA256 `7f660b6806494b00d17caed50b7cc66d01d9d02bc4cb1d66f333c1c12e1386df`.

## Newly closed: Exp073IG prediction admission
A versioned local-tangent prediction artifact was frozen only after IF PASS.

Prediction basis payload:
- path `docs/dsir4/predictions/C2_IDE_LOCAL_TANGENT_CONE_PREDICTION_BASIS_V0_1.jsonl`;
- creation commit `4924802be6e668351d203531d45a6f202ab96db1`;
- git blob `b3c5dc5ec6aefb79f215c5e01d7baef566cc5251`;
- SHA256 `2836a3665e6bab75587957228fbd3b9e152ef7d6e667966c308d81bf666c7c56`;
- exact record count `28`, z-major/k-minor ordering.

Prediction metadata artifact:
- path `docs/dsir4/predictions/C2_IDE_LOCAL_TANGENT_CONE_PREDICTION_V0_1.md`;
- creation commit `b69c1ca1b55fdaf935fae53e0c22ee25442db8d7`;
- blob `7e244010ca65050d0c8edff8fe90a9583845a568`.

It binds the exact local rule `Delta_pred = Delta_ref + alpha*dDelta_dalpha + beta*dDelta_dbeta`, with alpha one-sided negative derivative and beta symmetric derivative from the ID-admitted `h=1e-4` tangent. It explicitly forbids finite-distance extrapolation, interpolation and other rescue approximations.

Exp073IG prereg commit `8b8156f55a415f9a1e839b3805eed24e582e74e9`; prereg blob `5da4b65f26eeacd862a98e3e8e18d6036d0da143`; workflow/head `28833c7836265be29d1927e3b5336f43804b6936`.

Exp073IG run `34251593341`, job `102147045097`. Raw job log was consumed after every substantive step completed. It independently re-downloaded and hash-verified HW reference artifact, IC response artifact and ID admission artifact, reconstructed the 28 prediction rows exactly, required byte equality to the frozen payload and emitted:
`PASS_EXP073IG_C2_LOCAL_TANGENT_PREDICTION_ARTIFACT_ADMISSION_V0_1`.

Classification: `PREDICTION_ARTIFACT_ADMITTED_PLUS_0_PLUS_0`.
State after IG: `mapping_ready=true`, `prediction_artifact_created=true`, `prediction_ready=true`, `numerically_evaluated=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=TESTABLE_NOT_EVALUATED`.

## Current process: Exp073IH G_DOMAIN_MAPPING scientific gate
Prospectively frozen prereg:
- `docs/dsir4/prereg/EXP073IH_C2_G_DOMAIN_MAPPING_SCIENTIFIC_GATE_V0_1.md`;
- prereg creation commit `03208ce2b4cffba352dc927471594ea65873cb14`;
- prereg blob `63ea9e9c11b1f77353af613eb8236b5c5961b1fd`.

Workflow/head commit: `08a3750cbbd59ad41102c59896231769b65eff93`.
Run: `34251721583`.
Job: `102147505217`.
Runner: GitHub-hosted `ubuntu-24.04`; home/self-hosted runner has no owner and remains free.
State at note creation: QUEUED.
Expected exact token: `PASS_EXP073IH_C2_G_DOMAIN_MAPPING_V0_1`.

The frozen machine-checkable decision rule permits `G_DOMAIN_MAPPING=PASS` only if IF/IG raw authorities, six-component total-residual mapping, exact full DSIR certified applicability envelope, pinned solver/gauge/regime identities, immutable prediction identity, and anti-extrapolation restrictions all verify. The gate explicitly does not assert that the 28-point payload supplies continuous support for later angular/radial gates.

On IH PASS only: `G_DOMAIN_MAPPING=PASS`, while `G_ANGULAR_AUTHORITY` and every later mandatory gate remain `NOT_YET_TESTABLE`; therefore `overall_status=NOT_YET_TESTABLE` and `scientific_model_authority_created=false`.

On execution/provenance failure: diagnose and repair only the first causal implementation/provenance defect; do not rewrite the frozen gate criterion. On genuine scientific/domain failure apply the preregistered `FAIL`/`OUTSIDE_DOMAIN`/`NUMERICALLY_UNRESOLVED` semantics exactly.

## Exact next transition
Consume IH terminal raw log. If scientific PASS, record the first closed DSIR-4 C2 funnel gate and proceed only to the next prospectively admissible mandatory gate (`G_ANGULAR_AUTHORITY`) after auditing whether C2 has a correctly bound required angular observational authority set. Do not substitute theory-space tangent evidence for angular authority.

Global frozen DSIR boundaries remain unchanged.