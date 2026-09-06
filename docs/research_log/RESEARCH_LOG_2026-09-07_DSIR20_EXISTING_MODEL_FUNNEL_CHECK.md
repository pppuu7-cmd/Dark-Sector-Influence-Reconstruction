# DSIR research log — DSIR20 existing-model funnel status check

Date: 2026-09-07. Scope: DSIR only.

## Question

Do already-known cosmological model hypotheses currently pass the prospectively frozen DSIR-4 Model Funnel Matrix?

## Governing contract

The authoritative DSIR-4 funnel is `docs/dsir4/DSIR4_MODEL_FUNNEL_MATRIX_CONTRACT_V0_1.md`. Its mandatory gates are, in order:

1. `G_DOMAIN_MAPPING`
2. `G_ANGULAR_AUTHORITY`
3. `G_ORDERED_JOIN`
4. `G_RADIAL_SUPPORT`
5. `G_PHYSICAL_SUPPORT`
6. `G_COV_WHITENING`
7. `G_NUISANCE_QUOTIENT`
8. `G_RELATION_NULL`
9. `G_FINAL_MODEL`

Overall `PASS` requires every mandatory gate to be admitted `PASS`. Missing authority is `NOT_YET_TESTABLE`, never a partial PASS or a FAIL.

## Current audited hypotheses

| hypothesis | G_DOMAIN_MAPPING | next blocking gate | overall DSIR-4 status | evidence boundary |
|---|---|---|---|---|
| `C0_LCDM_REFERENCE` | `PASS` (Exp073GH admission) | `G_ANGULAR_AUTHORITY=NOT_YET_TESTABLE` | `NOT_YET_TESTABLE` | explicit frozen C0 residual mapping exists |
| `C1_SMOOTH_W_LOCAL_EPS1E4` | `PASS` (Exp073GH admission) | `G_ANGULAR_AUTHORITY=NOT_YET_TESTABLE` | `NOT_YET_TESTABLE` | explicit frozen C1 residual mapping exists |
| `C2_IDE_LOCAL_TANGENT_CONE` | `NOT_YET_TESTABLE` | mapping admission | `NOT_YET_TESTABLE` | legacy theory evidence only; no admitted DSIR-4 mapping artifact |
| `C3_GDM_CS2_CV2_LOCAL_PAIR` | `NOT_YET_TESTABLE` | mapping admission | `NOT_YET_TESTABLE` | legacy theory evidence only; metric-slip separator is not observational model authority |
| `C4_WDM_3KEV` | `NOT_YET_TESTABLE` | mapping admission | `NOT_YET_TESTABLE` | low-k DSIR block is intentionally weak; high-k block remains distinct |
| `C5_FR_B0_1E5` | `NOT_YET_TESTABLE` | mapping admission | `NOT_YET_TESTABLE` | official H-EFTCAMB theory response exists but is not DSIR-4 observational authority |
| `C5_FR_B0_1E4` | `NOT_YET_TESTABLE` | mapping admission | `NOT_YET_TESTABLE` | same boundary as B0=1e-5 |
| `C6_DCDM_DR_GAMMA_H0_1` | `NOT_YET_TESTABLE` | mapping admission | `NOT_YET_TESTABLE` | withheld-family mechanism support exists but did not close legacy G7/G8 |

## Scientific conclusion

No already-known hypothesis currently has a complete DSIR-4 `PASS`, and none of the pilot hypotheses has a DSIR-4 scientific `FAIL` either.

The strongest current funnel progress belongs to C0 LambdaCDM and the frozen C1 smooth-w control: both have admitted `G_DOMAIN_MAPPING=PASS` and have legitimately entered the second mandatory gate. The second gate remains unavailable because `G_ANGULAR_AUTHORITY` is still `NOT_YET_TESTABLE`; Exp073GI was support/infrastructure only and explicitly created no angular or model authority.

C2–C6 remain behind the first DSIR-4 gate despite mature legacy theory-atlas evidence. Per the anti-circularity contract, those results cannot be promoted retroactively. Their next valid step is prospective construction and admission of exact six-component residual mapping artifacts under the common DSIR-4 convention.

## Interpretation boundary

This result does not mean that all known cosmological models are viable, nor that none can be rejected by external datasets. It means only that the complete DSIR-4 observational funnel has not yet generated a PASS or FAIL for these frozen hypotheses. External observational constraints may be used as context, but cannot substitute for a missing DSIR authority gate.

## Next non-circular priority

After terminal consumption of the already-running Exp073FM authority work, continue prospective model conversion in a fixed, non-cherry-picked order: C2 IDE -> C3 GDM -> C5 designer-f(R) -> C6 DCDM -> C4 WDM/block-aware mapping, with each hypothesis receiving a new mapping artifact/admission rather than inheriting legacy status.
