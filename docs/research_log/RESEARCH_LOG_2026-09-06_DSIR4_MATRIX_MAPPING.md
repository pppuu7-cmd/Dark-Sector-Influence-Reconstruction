# DSIR research log — 2026-09-06 — DSIR-4 matrix/mapping infrastructure

Scope: DSIR only.

Parallel work was performed while Exp073FM / WW_S1_S1 remained the sole active self-hosted science job. No partial FM numerical result was consumed.

## Completed

1. Frozen `docs/dsir4/DSIR4_MODEL_FUNNEL_MATRIX_CONTRACT_V0_1.md`.
2. Added machine-readable `data/dsir4/model_funnel_inventory_v0_1.json` with nine class-level inventory entries and no evaluated hypotheses.
3. Added fail-closed validator `ci/validate_dsir4_model_funnel_v0_1.py`.
4. Exp073GD v0.1 exposed a shell-only quoting defect after the Python validator had already passed; no science/model authority was affected.
5. Minimal prospective repair produced Exp073GD v0.2 SUCCESS, run/job `34058689801 / 101555187453`, token `PASS_EXP073GD_DSIR4_MODEL_FUNNEL_MATRIX_STATIC_AUDIT_V0_1`, support `+0/+0`.
6. Frozen `docs/dsir4/DSIR4_MODEL_MAPPING_ARTIFACT_CONTRACT_V0_1.md` and `data/dsir4/model_mapping_artifact_template_v0_1.json`.
7. Added mapping-template negative-test validator `ci/validate_dsir4_model_mapping_template_v0_1.py`.
8. Exp073GE SUCCESS, run/job `34058778331 / 101555427506`, token `PASS_EXP073GE_DSIR4_MODEL_MAPPING_ARTIFACT_STATIC_AUDIT_V0_1`, support `+0/+0`.

## Scientific boundary

No existing cosmological model received PASS/FAIL. All initial model-class inventory entries remain `NOT_YET_TESTABLE`. No DSIR-derived new model was introduced. Mapping/prediction readiness is explicitly separated from scientific gate status.

## New infrastructure consequences

- Full DSIR PASS cannot be emitted unless every mandatory funnel gate is PASS with bound authority.
- NOT_YET_TESTABLE cannot be converted to fractional/percentage PASS or counted as evidence for/against a model.
- OUTSIDE_DOMAIN and NUMERICALLY_UNRESOLVED remain distinct statuses.
- The common mapping artifact requires explicit total residual `X_munu = M0^2 G_munu - T_known_munu`, six background/scalar decomposition records, certified domain, prediction provenance, interaction bookkeeping and modified-gravity rearrangement provenance.
- Static mapping validation is support-only and cannot itself authorize scientific PASS.

Immutable recovery: `docs/recovery/RECOVERY_2026-09-06_DSIR4_MATRIX_MAPPING_INFRASTRUCTURE.md`.
