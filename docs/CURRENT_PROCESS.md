# DSIR current-process ledger

Updated: 2026-09-13. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Active frontier — V0.11 common-grid discrepancy localization

Authoritative active run: `34748453026`, launch commit `1a2825cdb91319f9da13a2b446f3cc0447d1690c`.

Parent authority: `docs/dsir4/authority/LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_V0_10.json`, creation commit `f7f87ed3d624c8bf7125d9d5dfeee8cbe35ec015`. Parent classification: `STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED`; authorized successor: `PROSPECTIVELY_FROZEN_COMMON_GRID_DISCREPANCY_LOCALIZATION_AUDIT`.

Prospectively frozen V0.11 contract: `docs/dsir4/contracts/LAYERB_BETA_COMMON_GRID_DISCREPANCY_V0_11.json`, creation commit `962bd4f907ea70cf46af3ee703336d423913dc91`.

Executor: `ci/layerb_beta_common_grid_discrepancy_v0_11.py`, creation commit `10cad1811bfe66f298bed60cd910d9a1335b0492`, blob `57301e4f30253dd729c93c77dc90452cc797a623`.

Workflow: `.github/workflows/layerb-beta-common-grid-discrepancy-v0-11.yml`, creation commit `ebe73f501de97ef4ebd3141a00c8329e33c8ecbf`.

V0.11 computes only six new hosted lanes in parallel: `GRID640_D/B`, `GRID768_D/B`, `GRID896_D/B`. Existing `GRID512_D/B` and `GRID1024_D/B` from V0.10 plus direct `TOL300R_D/B` from V0.9 are reused by immutable artifact identity and are forbidden to be recomputed. The resolution path is therefore `512 -> 640 -> 768 -> 896 -> 1024` with no post-result grid selection.

Frozen boundaries remain: production `h=1e-4`, five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`, native kpd20, response threshold `<1e-3`, exact node binding `<=1e-12`, production sampling `0.00035`, stabilized `tol_perturb_integration=1e-12`. Covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 and science gate remain closed.

Pre-registered V0.11 classes distinguish: isolated `GRID1024` small-h resonance, broader sub-production-h grid sensitivity, production-h common-grid discrepancy, unresolved transition pattern, or invariant failure. A full 107-row Layer-B traversal is explicitly forbidden in V0.11.

At this ledger update invariant-audit is terminal PASS and all six new localization lanes are running concurrently. Do not inspect partial numerical outputs and do not alter the frozen grid sequence or thresholds.

## Closed parent — V0.10 local common-grid validation

Run `34741342346`, head `8f295e06d94d30297f12c5e59da797f5d559083d`, decision job `103683155104`, decision artifact `10313180649`, ZIP SHA256 `040292a748472123626e0de1d4cbbf577c21550e10ed63a6701b24466f9d240e`.

Classification: `STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED`, effect `+0/+0`.

`GRID512` remained adequate: 16/20 recovered, median h-spread `0.0005157877273103107`, control max `1.1041926145113362e-05`. `GRID1024` was not adequate: 14/20 recovered, median `0.0005134714477118745`, control max `0.0001745861154644251`. The largest GRID512-vs-GRID1024 signed response discrepancy over all h was `0.0108331289703319`, at the smallest h=`2.5e-5`; yet GRID1024-vs-independent-direct TOL300 at production h agreed to `0.00010217977189246786`. All keysets were exact, unsupported targets zero, max node mismatch `1.6551974349255386e-16`, invariant PASS.

Interpretation is deliberately limited: the stabilized direct-k result has not yet transferred cleanly to common-grid h-stability, but the production-h response itself remains tightly consistent. This is why localization, not full promotion or threshold relaxation, is the only authorized successor.

## Closed parents — V0.9/V0.8/V0.7

V0.9 authority `docs/dsir4/authority/LAYERB_BETA_TOL30_RESONANCE_V0_9.json`: reproducible isolated TOL30=`1e-11` control resonance plus independently replicated TOL300=`1e-12` with 16/20 recovery.

V0.8: `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`; TOL300/TOL1000 reached 16/20 but TOL30 control violation blocked promotion. V0.7: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, attribution `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`.

## Anti-duplication / exact next gate

Do not launch duplicate V0.11 lanes and do not run full Layer-B traversal while V0.11 is active. Consume the single decision only after all six lanes and invariant are terminal. Follow only the `next_stage` encoded by the prospectively frozen V0.11 classifier.

## Recovery/readiness

Last frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; diagnostic compute does not raise these. Article-II real G5 ACT×unWISE remains a separate unresolved publication gate.
