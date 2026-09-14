# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Active authoritative frontier — V0.16 host-factor isolation

Parent terminal authority: `docs/dsir4/authority/LAYERB_BETA_CROSS_HOST_FINGERPRINT_V0_15.json`, creation commit `e974d09d9fc4a687da582384da290c8fcb3989e6`.

Parent classification: `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED`, effect `+0/+0`; authorized successor exactly `PROSPECTIVELY_FROZEN_HOST_FACTOR_ISOLATION_AUDIT`.

Prospective V0.16 contract: `docs/dsir4/contracts/LAYERB_BETA_HOST_FACTOR_ISOLATION_V0_16.json`, commit `32061462eda85f3e9a7dc6e648e0327c2269901f`.
Executor: `ci/layerb_beta_host_factor_isolation_v0_16.py`, commit `1ca9b1b711e09b3d34abd03d7932091b5e44682d`, blob `ceeaea50dccb9c7cfcf136f6c0e686cb078af4c2`.
Workflow: `.github/workflows/layerb-beta-host-factor-isolation-v0-16.yml`, commit `ebc858e961e309b6934b0b17bf8120c39810a401`.
Launch/head: `cb30b8bad9dbebd22138e3a8a73c974e4625c0e3`.

Authoritative active run: `34793440750`. Exactly one V0.16 run exists. It contains one invariant job plus 24 independent `GRID1024 PURE_PAIR` host lanes (`R01..R24`) and a single decision barrier. Hosted-runner capacity may queue lanes; do not launch duplicates.

## Frozen V0.16 object

Two exact GRID1024 V0.15 replay-failure cells plus the exact GRID1024 anchor are recomputed on 24 new independent GitHub-hosted jobs under unchanged numerical identities. Primary prospective factor is runtime `AVX512F_PRESENT` versus `AVX512F_ABSENT` from `/proc/cpuinfo`; secondary factor is exact CPU model key. NumPy config/runtime SIMD hashes are recorded correlated signatures only. Stable OS/kernel/compiler/Python/NumPy/SciPy signature is a control.

Minimum class size is frozen at four jobs in each AVX512F class. Anchor spread must remain `<1e-5`; exact binding `<=1e-12`; all values finite. CPU vendor alone and ephemeral runner/job IDs are forbidden classifiers.

Frozen decision distinguishes: invariant failure; V0.15 stratification not reproduced; software-control confounding; insufficient AVX512F class coverage; same-CPU-model variation; stable AVX512F class stratification; or mixed/finer CPU-model requirement. Even an AVX512F result is observational stratification only and can authorize only a separate controlled dispatch intervention audit.

## Frozen boundaries / anti-duplication

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/determinism threshold `<1e-5`; production sampling `0.00035`; `tol_perturb_integration=1e-12`; exact binding `<=1e-12`; CLASS/baseline/precision/JJ/extraction identities frozen. No full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 or downstream science gate is authorized.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and scientific frontier `67%`. No active DSIR ChatGPT automation or repository cron research loop was found in the explicit check.

Do not inspect partial substantive lane values. Consume only the terminal frozen decision after invariant plus all 24 lanes complete, then materialize V0.16 authority and follow only its encoded `next_stage`.
