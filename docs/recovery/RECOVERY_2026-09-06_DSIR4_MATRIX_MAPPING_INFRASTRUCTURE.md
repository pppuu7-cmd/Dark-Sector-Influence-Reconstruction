# Recovery — DSIR-4 Model Funnel Matrix + model mapping infrastructure

Date: 2026-09-06. Scope: DSIR only.

## Context

Exp073FM / WW_S1_S1 remains the sole active self-hosted science job (`34050657030 / 101533574294`). No partial numerical output was consumed while building the DSIR-4 infrastructure below. The autonomous WW heavy queue through S3S3 remains unchanged.

## Model Funnel Matrix contract

Created/frozen:
- `docs/dsir4/DSIR4_MODEL_FUNNEL_MATRIX_CONTRACT_V0_1.md`, blob `2ad6d26381119442ccd3811b29f24522f5f6eeff`;
- `data/dsir4/model_funnel_inventory_v0_1.json`, blob `0817a4243c67cd5e198829996040074ee061c0c9`;
- `ci/validate_dsir4_model_funnel_v0_1.py`, blob `d0db9da8b8c94ae3eb8e97a0701c39e95a2469b9`;
- Exp073GD prereg `experiments/073gd_dsir4_model_funnel_matrix_static_audit_v0_1_prereg.md`, blob `f97e21083f5e11db45c0ad48d48567870f049597`.

Frozen scientific-status vocabulary:
`PASS / FAIL / OUTSIDE_DOMAIN / NOT_YET_TESTABLE / NUMERICALLY_UNRESOLVED`.

Mandatory v0.1 gate IDs:
`G_DOMAIN_MAPPING`, `G_ANGULAR_AUTHORITY`, `G_ORDERED_JOIN`, `G_RADIAL_SUPPORT`, `G_PHYSICAL_SUPPORT`, `G_COV_WHITENING`, `G_NUISANCE_QUOTIENT`, `G_RELATION_NULL`, `G_FINAL_MODEL`.

Aggregation is fail-closed:
- full PASS only if every mandatory gate PASS and every gate has bound authority;
- any mandatory FAIL -> overall FAIL;
- OUTSIDE_DOMAIN remains distinct and cannot be extrapolated;
- NUMERICALLY_UNRESOLVED remains distinct and is not tolerance rescue;
- otherwise missing mandatory authority -> NOT_YET_TESTABLE;
- NOT_YET_TESTABLE cannot count as PASS/FAIL or fractional PASS.

Initial class-level inventory: LambdaCDM/GR baseline, wCDM, w0wa, canonical quintessence-like, interacting dark sector, f(R), DGP-like, Horndeski/EFT-like, plus an explicit additional-class placeholder. All current entries remain `NOT_YET_TESTABLE`, with zero frozen hypothesis/parameter-point evaluations.

### Exp073GD audit history

- v0.1 run/job `34058614540 / 101554983550`: infrastructure/static failure only. Python validator itself emitted `PASS_DSIR4_MODEL_FUNNEL_MATRIX_VALIDATOR_V0_1`; failure occurred afterward in a shell quoting/count helper (`grep: 'NOT_YET_TESTABLE': No such file or directory`). Classification: support/infrastructure `+0/+0`; no scientific model authority.
- prospective minimal repair changed only the shell helper to parse JSON in Python; frozen matrix semantics/blobs remained unchanged.
- v0.2 run/job `34058689801 / 101555187453`: SUCCESS, raw token `PASS_EXP073GD_DSIR4_MODEL_FUNNEL_MATRIX_STATIC_AUDIT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `self_hosted_science_started=false`, `scientific_model_authority_created=false`.

## Model mapping artifact contract

Created/frozen:
- `docs/dsir4/DSIR4_MODEL_MAPPING_ARTIFACT_CONTRACT_V0_1.md`, blob `03fd11d8536b9743eb82f92f9a0d5386444079ed`;
- `data/dsir4/model_mapping_artifact_template_v0_1.json`, blob `1f815dfaae7ed9c0a825d251b8c904dd544170cd`;
- `ci/validate_dsir4_model_mapping_template_v0_1.py`, blob `c3d6e77070f1572b9178ab25cc2ff4beb0d6b954`;
- Exp073GE prereg `experiments/073ge_dsir4_model_mapping_artifact_static_audit_v0_1_prereg.md`, blob `55f0c225376add809e3b576930892ce4f4a27571`.

Common interface remains
`X_munu = M0^2 G_munu - T_known_munu`.

Every future frozen hypothesis mapping must explicitly record six background/scalar residual components: background density-like, background pressure-like, scalar density perturbation, scalar momentum/velocity, scalar isotropic pressure perturbation, scalar anisotropic stress. A genuine structural zero must be distinguished from NOT_YET_MAPPED and OUTSIDE_DOMAIN.

Interacting-sector bookkeeping must preserve total residual under sector relabeling. Modified-gravity effective-source rearrangements must bind to the original field equations and cannot become distinct hypotheses merely by moving terms across the equation. Mapping readiness, prediction readiness, numerical evaluation and scientific gate status are separate concepts.

Exp073GE run/job `34058778331 / 101555427506`: SUCCESS, raw token `PASS_EXP073GE_DSIR4_MODEL_MAPPING_ARTIFACT_STATIC_AUDIT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `self_hosted_science_started=false`, `scientific_model_authority_created=false`.

## Scientific interpretation

These results advance DSIR-4 infrastructure only. They do **not** establish PASS/FAIL for LambdaCDM, wCDM, w0wa, quintessence, IDE, f(R), DGP, Horndeski/EFT, or any other model. Complete model status remains unavailable until required DSIR-3 observational authorities and later funnel gates exist.

No DSIR-derived new model has been added to the existing-model inventory. DSIR-5 remains conditional on DSIR-4.
