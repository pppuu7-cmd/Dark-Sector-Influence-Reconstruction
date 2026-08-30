# DSIR Recovery Manual Addendum — Exp073AY

**Date:** 2026-08-30  
**Authority class:** repository prospective preregistration only  
**Scientific readiness effect:** +0; strict Article-3 readiness remains 52%

## What changed

While the only authorized heavy production, Exp073AQ run `33327372191` (`Wm_S1` controlled twins), remained in progress with no comparator artifact, the next angular task was prepared prospectively as Exp073AY.

Exp073AY freezes `Wm_S2` as a dormant successor task. It is deliberately not executable until Exp073AQ has a hosted immutable comparator artifact with exact terminal class `PASS_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Primary preregistration:

`experiments/073ay_article3_controlled_twin_wm_s2_dormant_prereg_v0_1.md`

Preregistration commit:

`9dd131d4610156d569b5b99659e13564b8a622cb`

## Recovery rule

On restart, do not launch a second Exp073AQ run and do not launch Wm_S2 merely because Exp073AY exists.

First inspect run `33327372191` and its artifacts.

- If no valid comparator authority exists: continue independent prerequisite/validation work only.
- If comparator authority is exact PASS: Exp073AY becomes eligible for implementation/final workflow freeze and hosted execution.
- If comparator authority is scientific repeatability FAIL: keep Exp073AY dormant.
- If the run terminates before comparator authority: classify infrastructure-INCOMPLETE; keep Exp073AY dormant.

## Frozen scientific boundaries preserved

All existing Article-3 support thresholds, exact-threshold ambiguity handling, signed-window treatment, no-fiducial-P rule, anti-leakage firewall, covariance/nuisance/quotient staging, and G7/G8 embargo remain unchanged.

No result from Exp073AQ was consumed in constructing Exp073AY.

## Readiness accounting

Exp073AY is prospective methodological infrastructure. It cannot increase scientific readiness and makes no physical claim. Strict Article-3 readiness remains **52%** until a later real-data scientific gate satisfies its own frozen hosted authority requirements.
