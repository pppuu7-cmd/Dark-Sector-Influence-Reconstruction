# DSIR authoritative recovery — latest

Updated: 2026-09-13. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth. Older recovery notes are immutable history and must not reopen superseded Layer-B work.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; response-stability threshold `<1e-3`; requested-node/exact-target mismatch `<=1e-12`; production `perturb_sampling_stepsize=0.00035`. Covariance/whitening/nuisance/relation-null remain unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this chain.

## Closed chain through V0.8

V0.5 run `34717972131`: `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`, with 20/23 failing exact-target coordinates h-unstable.

V0.6 authority `docs/dsir4/authority/LAYERB_BETA_FD_REPAIR_V0_6.json`, commit `4b62f4bf4057d34eff2b7cc1ceef98d63f8eafa7`: `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`; Richardson recovered only 4/20.

V0.7 authority `docs/dsir4/authority/LAYERB_BETA_SOLVER_CONDITIONING_V0_7.json`, commit `b84dbcfd08046792866270d9b1dea7b2dfc6c955`, run `34719555760`: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, specifically `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`. Sampling-only tightening recovered 0/20; integration-tolerance tightening reached 14/20 and ~7x median stabilization.

V0.8 authority `docs/dsir4/authority/LAYERB_BETA_TOLERANCE_ISOLATION_V0_8.json`, commit `1ae1d93199b61f66a7b23f945d586b580e5bc3bd`, run `34719854763`: `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`. TOL300=`1e-12` and TOL1000=`3e-13` each reached 16/20 recovery, but intermediate TOL30=`1e-11` produced one control with h-spread `0.0012003119264226171 > 1e-3`, so no stabilized profile could be promoted before localization/replication.

## V0.9 — terminal local TOL30 resonance with independently replicated TOL300

Authority: `docs/dsir4/authority/LAYERB_BETA_TOL30_RESONANCE_V0_9.json`, creation commit `87a5ce2d16f2186ac3159a1aa6e089e116cad9eb`.

Run `34740781222`, head `4004e876d0311654da2153ded992834ff83adf49`; all 16 science lanes and decision job `103680387202` terminal success. Decision artifact `10311599722`, ZIP SHA256 `c15759d860b8b95c4ca3889555c612d7f3f7533e0c674481e1dc002a6e5a4132`.

Classification: `REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300`, effect `+0/+0`.

Both independent exact TOL30=`1e-11` replicas reproduce the identical single unstable control coordinate `[C,D,3fdab851eb851eb8,3f8a474c7a7b57bd]` with max h-spread `0.0012003119264226171`. Every preregistered neighbor is stable: `2e-11 -> 2.250728286084143e-05`, `1.5e-11 -> 0.0001319984497407242`, `1.2e-11 -> 0.0007578124275447409`, `8e-12 -> 1.1453456129948862e-05`, `6e-12 -> 8.852316280511897e-05`. The instability is therefore sharply localized rather than broad over the tested tolerance neighborhood.

Independent full TOL300R=`1e-12` exactly reproduces V0.8 TOL300: 16/20 recovered (`0.8`), median parent-unstable h-spread `0.000510732305940965`, control max `5.0840057663462765e-05`, all controls stable. Exact-target mismatch max remains `1.2517848722592053e-16`.

The only authorized successor is `PROSPECTIVELY_FROZEN_STABILIZED_TOL300_LOCAL_COMMON_GRID_VALIDATION`. This does not itself authorize covariance, Wm_S3, global 65537 or a science gate.

## V0.10 — stabilized TOL300 local common-grid validation active

Executor: `ci/layerb_beta_tol300_common_grid_v0_10.py`, creation commit `5adee9adc18fee045688b75ee0aeced665e635dd`, blob `9737349b1f171c5772f1d8d6b6bf94cef58e3d07`.

Prospectively frozen contract: `docs/dsir4/contracts/LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_V0_10.json`, creation commit `b3c194c9bd5abc0cfa7fa7696056ab20357f6afb`.

Workflow: `.github/workflows/layerb-beta-tol300-common-grid-v0-10.yml`, creation commit `130ae270f2ae0dd783e1764a1b77b321039b7abc`.

Launch commit `8f295e06d94d30297f12c5e59da797f5d559083d`; active run `34741342346`.

V0.10 computes four independent hosted lanes: `GRID512_D`, `GRID512_B`, `GRID1024_D`, `GRID1024_B`. Both grids use the already frozen guarded common-grid geometry and cubic log-k interpolation engine; only the same 46 frozen probe coordinates are evaluated, so scope stays local. Stabilized `tol_perturb_integration=1e-12`, production sampling and the five-h ladder remain fixed. Technical CLASS capacities are reproduced as 1152 k-output entries and parser length 32768, matching the prior common-grid machinery.

The direct-k TOL300 comparator is **not recomputed**: V0.10 reuses exact V0.9 TOL300R D/B artifacts by immutable IDs and SHA256. Frozen validation requires both common grids to remain adequate (>=75% recovery, median `<1e-3`, controls `<1e-3`), no unsupported target, requested-node binding `<=1e-12`, GRID512-vs-GRID1024 signed beta responses `<1e-3` across all five h values and all 46 coordinates, GRID1024-vs-direct TOL300 production-h response `<1e-3` everywhere, recovery count within 1 and median ratio <=1.25.

At the latest write, V0.10 invariant-audit is terminal PASS and all four common-grid science lanes are in progress. Do not inspect partial numerical results or retune frozen thresholds.

## Exact next order

1. Continue only V0.10 run `34741342346`; no duplicate common-grid run.
2. Wait for all four common-grid lanes and the frozen decision barrier.
3. Verify decision artifact provenance and promote a durable V0.10 authority.
4. If and only if V0.10 classifies `STABILIZED_TOL300_LOCAL_COMMON_GRID_VALIDATED`, the authorized successor is a separately prospectively frozen stabilized-TOL300 **full Layer-B common-grid reevaluation**. It still does not directly open covariance/Wm_S3/global 65537.
5. If V0.10 is not validated, localize the common-grid discrepancy only; do not weaken thresholds post hoc.

## Publication/readiness locks

Last frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; diagnostic progress alone does not change them. Article-II real cross-family G5 ACT×unWISE remains a separate unresolved publication gate.

## Automation / ownership

Repository state must win over any stale automation prompt. At the last explicit task inspection QGR, MSQGR, KMQGB and RQIR-CG were active; DSIR automation enabling encountered the platform active-task limit and therefore must not be assumed enabled unless a later task-state check confirms it. `DSIR Auto-Research Guard` should remain disabled to avoid a duplicate control plane.

V0.10 is GitHub-hosted diagnostic compute, not a self-hosted `DSIR-HOME-PC` heavy-science run.
