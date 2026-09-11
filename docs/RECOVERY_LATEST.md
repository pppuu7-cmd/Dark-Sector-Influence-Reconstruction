# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_TOP64_CONFOUNDER_ROBUSTNESS_CLOSED_V125.md`, creation commit `2f518aaf0b7e9dc96925bec962dbc3e528f43b4c`. V124 and all earlier recovery notes remain immutable history; V125 supersedes them for current-front recovery.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged.

No 32769 execution is authorized. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Top-64 support branch — terminal for this cycle
The single permitted unchanged retry of run `34614119149` passed on attempt 2/job `103331912096`. All 64 ordered atoms were exactly reproduced at the primary guard; `21/64` have cross-grid discrepancy `>=1e-3`.

Population/confounder robustness was then independently closed. Corrected source run `34628562363` and terminal consumer run `34628673923` establish:
- `64 -> 58` unique physical atoms after exact duplicate collapse;
- Spearman cancellation-scale/discrepancy `-0.5341210955390675` before collapse and `-0.5163800793626381` after collapse;
- DES-only Spearman `-0.5078643578643579` with `18/55` atoms `>=1e-3`;
- strict-threshold exceedances by cancellation-scale quartile `13/16`, `6/16`, `1/16`, `1/16` from lowest to highest scale;
- high/low discrepancy median cancellation-scale ratio `0.13484119009229173`.

Durable confounder authority:
`docs/dsir4/authority/LAYERB_POST_16385_TOP64_CONFOUNDER_TERMINAL_AUTHORITY_V0_1.json`, creation commit `be81a67ed93f4e640e79532f85fda90d32c33afe`.

A separate post-hoc/exploratory unique-atom stress test, run `34628932658`, gives lowest-scale quartile vs rest odds ratio `20.571428571428573` with one-sided Fisher `p=1.6168593301143046e-05`, and lower-half vs upper-half odds ratio `19.125` with `p=2.3321946203480245e-05`. This is descriptive support only, not preregistered confirmatory inference.

Durable exploratory authority:
`docs/dsir4/authority/LAYERB_POST_16385_TOP64_UNIQUE_ASSOCIATION_EXPLORATORY_AUTHORITY_V0_1.json`, creation commit `629ca6dd4bec25e374467b7d06a2d555354688f8`.

## Interpretation / boundary
The finite-difference cancellation/ill-conditioning diagnosis is now population-distributed rather than a top-1 anecdote: it survives duplicate collapse, DES-only stratification and cancellation-scale enrichment tests. This materially strengthens the numerical-conditioning explanation for the observed plateau.

It remains support-only `+0/+0`. It does not change the canonical non-convergence classification, authorize 32769, authorize covariance restriction or open Wm_S3.

## Automation
`DSIR Continuous Research` remains enabled hourly and was rechecked during V125. It must resume from V125/current repository state and must not duplicate the now-closed top-64 support branch.

Stale superseded self-hosted run `34550495778 / 103112190909` must not receive home-runner ownership.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%**.

The percentages intentionally stay unchanged because the new results are diagnostic support-only `+0/+0`; the frozen scientific frontier did not move.

## Exact next action
Treat the top-64 cancellation/confounder branch as support-complete for the current Article III cycle. Integrate the validated distributed cancellation-conditioning failure mode into the Article III methods/limitations/funnel ledger, then audit remaining repository-readiness blockers and separate documentary/reproducibility gaps from any still-missing scientific gate. Any new numerical discriminant must be prospectively frozen before execution and may not alter the frozen `h`, tolerance, grid family, interpolation, masks or estimator to rescue the gate.
