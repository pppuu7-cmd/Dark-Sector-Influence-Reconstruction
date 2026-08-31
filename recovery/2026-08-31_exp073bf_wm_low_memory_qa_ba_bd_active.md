# DSIR recovery checkpoint — Exp073BF Wm low-memory QA launched; BA/BD heavy runs active

**Date:** 2026-08-31  
**Authority scope:** Article 3 / G7 pre-support angular production  
**Scientific authority readiness:** **52.0% — unchanged**  
**Draft/data readiness:** **53.7% — unchanged**

Repository/hosted authority outranks chat wording. RTK/RQIR are excluded.

## Exact chronology

1. Read prior authority checkpoint `recovery/2026-08-31_exp073be_ba_harness_rerun_wms2_active.md` and `docs/RECOVERY_LATEST.md`.
2. Re-checked frozen Exp073BA preregistration and dual-readiness ledger. No scientific acceptance threshold was modified.
3. Exp073BA clean rerun `33345968620` was inspected. Both replica jobs had passed freeze enforcement, NaMaster installation, AZ artifact download and exact admitted-PCL binding. Both were in `Compute low-memory compact Wm_S1 replica`; no authority artifact existed yet. Therefore no scientific PASS/FAIL classification was made.
4. Exp073BD provisional Wm_S2 run `33342265114` was inspected. Both branches A/B remained in `Compute independent Wm_S2 provisional branch`; no preferred branch was selected and no duplicate heavy run was launched.
5. Independent implementation-QA gap identified: existing low-memory self-test covers spin-2 x spin-2 WW algebra, while BA uses Wm spin-0 x spin-2. This gap is methodological/infrastructure only.
6. Prospectively preregistered Exp073BF in commit `99db0c8b7444ade7eb65df7626398a034bf16fda`.
7. Added hosted Exp073BF workflow in commit `bbb4ecb14c01d2d7bafe37f0ae01377b2d81223b`.
8. Triggered Exp073BF in commit `47fab566ac115b83745fffdd60db8f937e043621`; hosted run `33349183295` started.
9. Added recovery-manual addendum in commit `5a11111d102d4dd2be1b88ec339bf3804c55062f`.

## Exp073BF frozen role

Exp073BF is synthetic numerical/infrastructure QA only. It compares a small deterministic Wm spin-0 x spin-2 low-memory reconstruction against stock NaMaster and tests exact repeated `G02` generation. Its tolerance is confined to synthetic stock-equivalence QA and can never rescue an exact scientific comparator.

PASS token if all frozen QA conditions hold:

`PASS_EXP073BF_WM_STOCK_EQUIVALENCE_QA_V0_1`

Failure token:

`INFRASTRUCTURE_NUMERICAL_QA_FAIL_EXP073BF_WM_STOCK_EQUIVALENCE_V0_1`

Both classes yield `+0` scientific readiness and `+0` draft/data readiness.

## Immutable historical state

Exp073AQ remains permanently:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

No tolerance/rounding/ULP/preferred-replica reinterpretation is permitted.

## Current shorthand

- ✅ Exp073AZ exact mask-PCL predecessor authority: PASS, +0 readiness.
- ✅ Exp073BC immutable AZ->BA binding receipt: frozen.
- ✅ Exp073BE provenance diagnostic: PASS, +0 readiness.
- 🟡 Exp073BA run `33345968620`: both heavy compact replicas actively computing; no authority artifact yet.
- 🟡 Exp073BD run `33342265114`: both provisional Wm_S2 branches actively computing.
- 🟡 Exp073BF run `33349183295`: independent lightweight Wm stock-equivalence QA launched.
- ❌ Exp073AQ historical exact Wm_S1 repeatability remains permanent scientific FAIL.
- ❌ Layer A/B, covariance/whitening, G7, G8, G9 remain open/not authorized.

`Verified: 52.0% | Draft/data: 53.7%`

## Exact next gate

First consume terminal Exp073BA authority if run `33345968620` completes. If still active, inspect Exp073BF terminal QA and Exp073BD branch completion without duplicating heavy work. Only an exact hosted BA PASS may authorize prospective Track-A Wm_S2; provisional BD cannot substitute for it.