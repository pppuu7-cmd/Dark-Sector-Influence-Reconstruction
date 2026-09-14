# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Closed numerical-runtime chain through V0.22

V0.18R/V0.19 false-invalid intervention outcomes were traced to the wrong NumPy validation observable: raw non-dispatch AVX-512 `__cpu_features__` bits were incorrectly treated as runtime-dispatch state. V0.19D diagnosed the defect; V0.20 response-free validated the correct NumPy 1.26.4 mask; V0.21 causally established `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`.

V0.22 terminal authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.json`, creation commit `2b3cb46863fb85e6456a5a11e30183acf3b6de10`.
Run `34875798025` terminal success; decision job `104089235776`; artifact `10360469338`; digest `sha256:12769549f5d44da9dc01ee82d426dd07e171cefe27282e92e40df15b43ea2ba0`.
Classification `FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_SUPPORTED`, effect `+0/+0`.
All 32 hosted lanes were eligible; native classes were 10 AVX512-active and 22 AVX512-inactive. Both frozen replay-failure witness cells and anchor had cross-host spread `0.0`; native-class mean separation on both failure cells was `0.0`; both failure responses matched the frozen alternate branch with relative mismatch `0.0`. The forced NumPy non-AVX512 baseline therefore repairs the observed hosted numerical branch on the frozen witness object.

## Active authoritative frontier — V0.23 production-h replay revalidation

Parent-authorized stage: `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_AUDIT`.

Preregistration: `prereg/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_V0_23.md`, commit `24b09db3069acbe875459f7ad6f2d2aea9f25830`.
Executor: `ci/layerb_beta_forced_baseline_production_h_replay_revalidation_v0_23.py`, hardened pre-freeze commit `c96e80a0e075bd21b41351aa158ef997f0cc05cd`, blob `aa6c3aa298fc12aa65f4de2919ba9cc3f39a7fbe`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_V0_23.json`, commit `d5d5665671fbfedaaf77022b0f7164ada90d49ee`.
Workflow: `.github/workflows/layerb-beta-forced-baseline-production-h-replay-revalidation-v0-23.yml`, commit `a7ce06dc9cef76c934d5b5c2c289a0729aa64e04`.
Launch/head: `ad5472244fdcffa05ecfd3826ac9c83db06f32ef`.
Authoritative run: `34878651714`; exactly one run exists. GitHub currently has invariant + matrix jobs queued; no competing run exists.

V0.23 revalidates the complete V0.12 **production-h** pure-grid replay set: five frozen grids (`GRID512,640,768,896,1024`) × three frozen V0.12 targets = exactly 15 cells at `h=1e-4`. It is not a selected witness test. The exact V0.20 NumPy mask is validated response-free before any substantive solve; no unmasked substantive response is allowed. Each eligible lane performs exactly 10 CLASS constructions (plus/minus production h for each of five grids).

Frozen power: total eligible n>=6, with n>=3 native AVX512-active and n>=3 native AVX512-inactive. Supported classification requires all 15 cells to have cross-host max pairwise relative spread `<1e-5` and native-class mean separation `<1e-5` with all controls passing.

Historical unforced V0.10/V0.11/V0.12 numeric values are explicitly non-gating because they may belong to different runtime-dispatch branches. The two original V0.13 production-h failure cells are tracked as frozen sub-controls, but V0.23 PASS requires the full 15-cell object.

If supported, the only authorized next stage is `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_AUDIT`.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; technical replay/intervention/reproducibility threshold `<1e-5`; exact binding `<=1e-12`; native `k_per_decade_for_pk=20`; production sampling `0.00035`; `tol_perturb_integration=1e-12`. Full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and all physical-science gates remain closed. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
