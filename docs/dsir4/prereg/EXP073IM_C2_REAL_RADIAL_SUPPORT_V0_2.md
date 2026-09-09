# Exp073IM — C2 real radial-support execution preregistration v0.2

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN BEFORE ANY REAL EXP073IM OUTPUT IS INSPECTED.

This document amends `EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_1.md` only to restore compatibility with the earlier Article-3 broad-row representation already frozen on 2026-08-30. It does not change the scientific radial question, any physical-support threshold, any upstream authority, any DES-Y1 payload, or any downstream firewall.

## Binding

Use exactly:

- original preregistration `docs/dsir4/prereg/EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_1.md` for upstream authority, payload hashes, pinned observation semantics, classification taxonomy, and anti-leakage rules;
- corrected interface `docs/dsir4/contracts/DSIR4_C2_RADIAL_EXECUTOR_INTERFACE_V0_2.md` for the output representation;
- broad-row authority `docs/ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md`;
- exact factorized Layer-A evaluator `docs/ARTICLE3_LAYERA_FACTORIZED_DES_SUPPORT_EVALUATOR_2026-08-30.md`;
- Exp073Z2 stable-direct radial authority recorded in `docs/DSIR_ARTICLE3_EXP073Z2_RADIAL_PASS_ANGULAR_FRONTIER_2026-08-30.md`.

## Representation correction

The v0.1 requirement for one scalar row-level `z`, one scalar row-level `k_Mpc^-1`, and row-level `final_response_abs_values` is superseded for the current DES Wm/WW broad-observation route.

The real radial output instead consists of exactly 1170 deterministic broad observation rows:

- Wm: 4 source angular authorities x 5 lens radial bins x 39 bandpowers = 780;
- WW: 10 unordered source-pair angular/radial authorities x 39 bandpowers = 390.

Each row binds an exact angular bandpower window to an exact Exp073Z2 radial kernel and records the factorized broad-support representation. No effective ell/z/k scalarization is admissible.

## Scientific question

`G_RADIAL_SUPPORT` asks only whether the admitted exact angular authority can be joined to the frozen real DES-Y1 LOS/radial authority to construct every mandatory broad observation row deterministically, with finite non-empty positive radial support and exact provenance.

It does not ask whether those rows pass the physical rectangle. That is the separately frozen Layer-A/Layer-B physical-support stage.

## Frozen classification

Positive token:

`PASS_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_2`

Scientific negative token:

`FAIL_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_2`

Invalid/incomplete execution remains separate:

- `INVALID_FOR_SCIENCE_EXP073IM`;
- `INCOMPLETE_EXP073IM`.

A PASS requires all ten criteria in section 6 of `DSIR4_C2_RADIAL_EXECUTOR_INTERFACE_V0_2.md`.

A scientific FAIL is permitted only after all exact provenance/interface checks pass and one or more mandatory frozen radial kernels are genuinely empty, zero-normalization, or non-finite.

## Downstream thresholds unchanged

This amendment does not alter and cannot inspect:

- Article-3 physical rectangle `0.295 <= z <= 2.33`, `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `f_op <= 0.05`;
- Layer-B invalid-row fraction `<=0.05`;
- minimum retained observation-row count `15`;
- covariance/whitening rules;
- nuisance quotient rules;
- relation/null rules;
- any later model/falsification conclusion.

No threshold or classification rule in this v0.2 preregistration may be changed after a real Exp073IM v0.2 output is inspected.