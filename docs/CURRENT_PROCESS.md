# DSIR current-process ledger

Updated: 2026-09-13. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Active frontier — V0.10 stabilized TOL300 local common-grid validation

Authoritative active run: `34741342346`, launch commit `8f295e06d94d30297f12c5e59da797f5d559083d`.

Parent authority: `docs/dsir4/authority/LAYERB_BETA_TOL30_RESONANCE_V0_9.json`, creation commit `87a5ce2d16f2186ac3159a1aa6e089e116cad9eb`. Parent classification is `REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300`.

V0.9 terminal evidence: run `34740781222`, decision job `103680387202`, decision artifact `10311599722`, SHA256 `c15759d860b8b95c4ca3889555c612d7f3f7533e0c674481e1dc002a6e5a4132`. Both exact `1e-11` replicas reproduce the same single unstable DES control; all frozen neighboring tolerances are stable. Independent full TOL300R=`1e-12` reproduces 16/20 recovery, median `0.000510732305940965`, control max `5.0840057663462765e-05`.

Prospectively frozen V0.10 contract: `docs/dsir4/contracts/LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_V0_10.json`, creation commit `b3c194c9bd5abc0cfa7fa7696056ab20357f6afb`.

Executor: `ci/layerb_beta_tol300_common_grid_v0_10.py`, creation commit `5adee9adc18fee045688b75ee0aeced665e635dd`, blob `9737349b1f171c5772f1d8d6b6bf94cef58e3d07`.

Workflow: `.github/workflows/layerb-beta-tol300-common-grid-v0-10.yml`, creation commit `130ae270f2ae0dd783e1764a1b77b321039b7abc`.

V0.10 has four hosted science lanes in parallel: `GRID512_D`, `GRID512_B`, `GRID1024_D`, `GRID1024_B`. They use frozen guarded common grids and cubic log-k interpolation on the same 46 probe coordinates, with stabilized `tol_perturb_integration=1e-12`. Direct-k TOL300 is reused from exact V0.9 immutable artifacts, not recomputed.

Frozen validation requires: both grids >=75% recovery of the immutable 20-coordinate parent-unstable subset, median h-spread `<1e-3`, controls `<1e-3`; no unsupported interpolation target; requested common-grid node binding `<=1e-12`; GRID512-vs-GRID1024 signed beta-response relative difference `<1e-3` across all five h values and 46 coordinates; GRID1024-vs-direct TOL300 production-h response `<1e-3` everywhere; fine recovered-count difference <=1 and median ratio <=1.25 versus direct TOL300.

Frozen boundaries: production `h=1e-4`, five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`, native kpd20, response threshold `1e-3`, production sampling `0.00035`. No covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 or science gate is authorized.

At the latest ledger update invariant-audit is terminal PASS and all four common-grid lanes are in progress. Do not inspect partial science output and do not alter V0.10 thresholds.

## Closed parent — V0.9 localized TOL30 resonance

The TOL30=`1e-11` instability is reproducible but narrow: both replicas identify `[C,D,3fdab851eb851eb8,3f8a474c7a7b57bd]` with h-spread `0.0012003119264226171`; neighbor maxima are all below threshold (`2e-11`: `2.2507e-05`, `1.5e-11`: `1.31998e-04`, `1.2e-11`: `7.57812e-04`, `8e-12`: `1.14535e-05`, `6e-12`: `8.85232e-05`). This resolves the V0.8 all-controls blocker sufficiently to authorize local common-grid validation of TOL300 only.

## Closed parents — V0.8/V0.7

V0.8 run `34719854763`: `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`; observed TOL300/TOL1000 16/20 recovery but TOL30 control violation blocked promotion.

V0.7 run `34719555760`: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, attribution `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`; sampling-only axis had no material recovery.

## Anti-duplication / exact next gate

Do not launch another V0.10. When run `34741342346` becomes terminal, consume the single decision artifact and verify hashes/provenance. If classification is `STABILIZED_TOL300_LOCAL_COMMON_GRID_VALIDATED`, write a durable V0.10 authority and only then prospectively freeze/launch `STABILIZED_TOL300_FULL_LAYERB_COMMON_GRID_REEVALUATION`. If not validated, run only a common-grid discrepancy-localization audit. No outcome directly opens covariance or Wm_S3.

## Recovery/readiness

`docs/RECOVERY_LATEST.md` advanced to V0.9 terminal + V0.10 active in commit `003b961566c5fd1a1020a1452785104c1ecc17ba`.

Last frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`. Article-II real G5 ACT×unWISE remains a separate unresolved publication gate.

## Automation

Do not assume DSIR scheduled automation is enabled: the last enable attempt hit the platform active-task limit. Repository/Actions state remains authoritative. Avoid a second DSIR control plane while this chat is actively advancing V0.10.
