# Exp073IH — C2 G_DOMAIN_MAPPING scientific gate v0.1

Status: PROSPECTIVELY FROZEN after separate mapping/prediction admission gates and before any `G_DOMAIN_MAPPING` scientific result is emitted.

## Scientific gate
This is the first DSIR-4 Model Funnel Matrix scientific-status gate for hypothesis `C2_IDE_LOCAL_TANGENT_CONE`. It evaluates **only** `G_DOMAIN_MAPPING` as defined by `DSIR4_MODEL_FUNNEL_MATRIX_CONTRACT_V0_1`: mapping into the common DSIR residual interface plus a certified applicability domain. It does not evaluate angular authority or any later observational gate.

## Frozen governing contracts / identities
- funnel contract blob `2ad6d26381119442ccd3811b29f24522f5f6eeff`.
- mapping contract blob `03fd11d8536b9743eb82f92f9a0d5386444079ed`.
- common residual convention blob `9ab68fe254891a076e24757de724e32e2190bfb6`.
- mapping artifact blob `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`, SHA256 `7f660b6806494b00d17caed50b7cc66d01d9d02bc4cb1d66f333c1c12e1386df`.
- mapping admission Exp073IF `34250714613 / 102144147469`, exact PASS `PASS_EXP073IF_C2_RESIDUAL_MAPPING_ARTIFACT_ADMISSION_V0_1`.
- prediction artifact blob `7e244010ca65050d0c8edff8fe90a9583845a568`.
- deterministic local tangent prediction payload blob `b3c5dc5ec6aefb79f215c5e01d7baef566cc5251`, SHA256 `2836a3665e6bab75587957228fbd3b9e152ef7d6e667966c308d81bf666c7c56`.
- prediction admission Exp073IG run `34251593341`, job `102147045097`, required exact PASS `PASS_EXP073IG_C2_LOCAL_TANGENT_PREDICTION_ARTIFACT_ADMISSION_V0_1`.

## Prospectively frozen decision rule
The gate is machine-checkable and fail-closed.

`G_DOMAIN_MAPPING=PASS` iff ALL of the following are exactly verified:
1. the common residual convention and mapping/funnel contracts have the frozen identities above;
2. Exp073IF raw authority is PASS and `mapping_ready=true`;
3. the admitted mapping artifact explicitly provides all six scalar residual components, with zeros distinguished as structural zeros, and binds the interacting-sector total `idm_iv+iv` plus internal transfer-Q convention;
4. the mapping's certified applicability envelope is exactly `0.295<=z<=2.33` and `0<k<=0.06664762008318016 Mpc^-1`, i.e. it covers the entire frozen DSIR mapping domain without extrapolation;
5. its regime/branch assumptions are explicit: pinned CLASS-IV implementation/commit, synchronous intermediate representation, linear scalar regime, local tangent hypothesis, and no QS/sub-horizon/effective-coordinate/smoothing/rounding/averaging/fiducial-P rescue;
6. Exp073IG raw authority is PASS and `prediction_ready=true` for the separately frozen local tangent prediction artifact; its payload identity/hash and local first-order parameter rule are immutable;
7. the gate makes no claim that the 28-point prediction payload supplies continuous numerical support for later radial/angular gates. `G_DOMAIN_MAPPING` concerns validity of the common-interface mapping and certified applicability envelope only. Later gates must independently prove the numerical support they require.

If the mapping cannot cover part of the mandatory domain under its frozen hypothesis assumptions, classify `OUTSIDE_DOMAIN` rather than extrapolating. If a required mapping component/provenance identity is absent or inconsistent, classify `FAIL` for `G_DOMAIN_MAPPING` only if the defect is scientific/definition-level under this frozen hypothesis; implementation/provenance execution defects of this workflow remain `+0/+0` and must be repaired prospectively. Exact-threshold numerical ambiguity, if any, is `NUMERICALLY_UNRESOLVED`; no tolerance rescue is allowed.

## PASS token and consequences
Exact scientific token: `PASS_EXP073IH_C2_G_DOMAIN_MAPPING_V0_1`.

On PASS only:
- `hypothesis_id=C2_IDE_LOCAL_TANGENT_CONE`
- `G_DOMAIN_MAPPING=PASS`
- `mapping_ready=true`
- `prediction_ready=true`
- `numerically_evaluated=true` for **this structural/domain gate only**
- `G_ANGULAR_AUTHORITY=NOT_YET_TESTABLE`
- all later mandatory funnel gates remain `NOT_YET_TESTABLE`
- `overall_status=NOT_YET_TESTABLE`
- `scientific_model_authority_created=false`

A PASS here is not a complete DSIR PASS and not model acceptance. The funnel aggregation rule still requires every mandatory gate to PASS for overall PASS.