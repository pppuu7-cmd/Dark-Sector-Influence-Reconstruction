# DSIR authoritative recovery — latest

Updated: 2026-09-13. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth. Older recovery notes are immutable history and must not reopen superseded Layer-B work.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; response-stability threshold `<1e-3`; requested-node/exact-target mismatch `<=1e-12`; production `perturb_sampling_stepsize=0.00035`; stabilized `tol_perturb_integration=1e-12`. Covariance/whitening/nuisance/relation-null remain unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this chain.

## Closed chain through V0.9

V0.5 run `34717972131`: `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`, with 20/23 failing exact-target coordinates h-unstable.

V0.6 authority `docs/dsir4/authority/LAYERB_BETA_FD_REPAIR_V0_6.json`: `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`; Richardson recovered only 4/20.

V0.7 authority `docs/dsir4/authority/LAYERB_BETA_SOLVER_CONDITIONING_V0_7.json`: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, attribution `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`; integration-tolerance tightening reached 14/20 while sampling-only tightening recovered 0/20.

V0.8 authority `docs/dsir4/authority/LAYERB_BETA_TOLERANCE_ISOLATION_V0_8.json`: `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`; TOL300=`1e-12` and TOL1000=`3e-13` each reached 16/20 but TOL30=`1e-11` produced one unstable control.

V0.9 authority `docs/dsir4/authority/LAYERB_BETA_TOL30_RESONANCE_V0_9.json`, run `34740781222`: `REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300`. Two exact TOL30 replicas reproduce the same single unstable control while all preregistered neighboring tolerances are stable. Independent TOL300R=`1e-12` reproduces 16/20 recovery, median parent-unstable h-spread `0.000510732305940965`, control max `5.0840057663462765e-05`.

## V0.10 — terminal local common-grid validation

Authority: `docs/dsir4/authority/LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_V0_10.json`, creation commit `f7f87ed3d624c8bf7125d9d5dfeee8cbe35ec015`.

Run `34741342346`, head `8f295e06d94d30297f12c5e59da797f5d559083d`; decision job `103683155104`; decision artifact `10313180649`, ZIP SHA256 `040292a748472123626e0de1d4cbbf577c21550e10ed63a6701b24466f9d240e`.

Classification: `STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED`, effect `+0/+0`.

`GRID512`: 16/20 recovered (`0.8`), median h-spread `0.0005157877273103107`, control max `1.1041926145113362e-05`, adequate true.

`GRID1024`: 14/20 recovered (`0.7`), median h-spread `0.0005134714477118745`, control max `0.0001745861154644251`, adequate false.

Maximum GRID512-vs-GRID1024 relative signed beta-response discrepancy over all five h values and 46 coordinates is `0.0108331289703319`; the worst point is `[F,D,3ff047ae147ae148,3f93adf194593fb0]` at h=`2.5e-5`. In contrast, GRID1024-vs-independent-direct TOL300 at production h differs by at most `0.00010217977189246786`, safely below `1e-3`. All coordinate keysets are exact, unsupported targets are zero, max requested-node mismatch is `1.6551974349255386e-16`, invariant PASS.

V0.10 therefore authorizes **only** `PROSPECTIVELY_FROZEN_COMMON_GRID_DISCREPANCY_LOCALIZATION_AUDIT`. It does not authorize full Layer-B promotion, covariance, Wm_S3, global 65537 or a science gate.

## V0.11 — active common-grid discrepancy localization

Executor: `ci/layerb_beta_common_grid_discrepancy_v0_11.py`, creation commit `10cad1811bfe66f298bed60cd910d9a1335b0492`, blob `57301e4f30253dd729c93c77dc90452cc797a623`.

Prospectively frozen contract: `docs/dsir4/contracts/LAYERB_BETA_COMMON_GRID_DISCREPANCY_V0_11.json`, creation commit `962bd4f907ea70cf46af3ee703336d423913dc91`.

Workflow: `.github/workflows/layerb-beta-common-grid-discrepancy-v0-11.yml`, creation commit `ebe73f501de97ef4ebd3141a00c8329e33c8ecbf`.

Launch commit `1a2825cdb91319f9da13a2b446f3cc0447d1690c`; active run `34748453026`.

V0.11 reuses immutable V0.10 `GRID512_D/B` and `GRID1024_D/B` artifacts plus V0.9 direct `TOL300R_D/B`. It computes only six new hosted lanes in parallel: `GRID640_D/B`, `GRID768_D/B`, `GRID896_D/B`. The frozen resolution trajectory is `512 -> 640 -> 768 -> 896 -> 1024`; grid sizes may not be changed after results.

The frozen classifier distinguishes: isolated GRID1024 small-h resonance; broader sub-production-h grid sensitivity; production-h common-grid discrepancy; unresolved grid-transition pattern; or invariant failure. Production-h response disagreement `>=1e-3` is a separate hard failure class. Full 107-row Layer-B traversal is explicitly forbidden during V0.11.

At the latest write, V0.11 invariant-audit is terminal PASS and all six localization lanes are running concurrently. Do not inspect partial science results and do not launch duplicate lanes.

## Exact next order

1. Continue only V0.11 run `34748453026`; no duplicate V0.11 run.
2. Wait for all six new grid lanes and the frozen decision barrier.
3. Verify decision artifact provenance and promote a durable V0.11 authority.
4. Follow only the decision's encoded `next_stage`; do not jump directly to full Layer-B unless a later prospectively frozen chain explicitly authorizes it.
5. Keep covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 and the science gate closed.

## Publication/readiness locks

Last frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; diagnostic progress alone does not change them. Article-II real cross-family G5 ACT×unWISE remains a separate unresolved publication gate.

## Automation / ownership

Repository/Actions state wins over any stale automation prompt. DSIR scheduled automation must not be assumed enabled unless a later explicit task-state check confirms it. Avoid a duplicate DSIR control plane while this chat is actively advancing V0.11.

V0.11 is GitHub-hosted diagnostic compute, not a self-hosted `DSIR-HOME-PC` heavy-science run.
