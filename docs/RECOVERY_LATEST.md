# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/determinism threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this diagnostic chain.

## Closed reproducibility chain through V0.15

V0.12 remains `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`: cubic interpolation is strongly supported at the three actual offending cells, but the frozen replay invariant blocked scientific promotion.

V0.13 `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`: the same exact cells split across hosted jobs while anchors passed.

V0.14 `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED`: repeated identical solver sequences inside one runner/process are perfectly stable, excluding a same-process repeated-solver defect at the `<1e-5` threshold.

V0.15 terminal authority `docs/dsir4/authority/LAYERB_BETA_CROSS_HOST_FINGERPRINT_V0_15.json`, commit `e974d09d9fc4a687da582384da290c8fcb3989e6`, run `34792546153`: `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED`, effect `+0/+0`. Invariant + 16 host lanes + decision all succeeded. Decision artifact `10328836120`, SHA256 `147aedae7d660c7554078151ee5ed6ba5985b7317ad5b1f3e18e4cb0f75ca1a4`. Repeated identical recorded fingerprint groups have zero within-group failure-cell spread; distinct repeated fingerprints reproduce the exact response branches at/above `1e-5`. This is numerical host-environment stratification, not Layer-B validation and not a dark-sector signal.

V0.15 authorizes exactly `PROSPECTIVELY_FROZEN_HOST_FACTOR_ISOLATION_AUDIT`.

Post-terminal candidate selection found that AMD EPYC 9V74 and Intel Xeon Platinum 8573C can share a response/software-fingerprint branch while AMD EPYC 7763 occupies the alternate branch. CPU vendor alone is therefore not a sufficient candidate. The prospectively selected primary factor family is runtime AVX-512 capability versus finer CPU-model/runtime confounding; this candidate selection is not a causal conclusion.

## V0.16 — active prospectively frozen host-factor isolation

Contract: `docs/dsir4/contracts/LAYERB_BETA_HOST_FACTOR_ISOLATION_V0_16.json`, commit `32061462eda85f3e9a7dc6e648e0327c2269901f`.
Executor: `ci/layerb_beta_host_factor_isolation_v0_16.py`, commit `1ca9b1b711e09b3d34abd03d7932091b5e44682d`, blob `ceeaea50dccb9c7cfcf136f6c0e686cb078af4c2`.
Workflow: `.github/workflows/layerb-beta-host-factor-isolation-v0-16.yml`, commit `ebc858e961e309b6934b0b17bf8120c39810a401`.
Launch/head: `cb30b8bad9dbebd22138e3a8a73c974e4625c0e3`.
Authoritative active run: `34793440750`; exactly one V0.16 run exists.

The gate has 24 independent new GRID1024/PURE_PAIR hosted lanes, the exact two V0.15 GRID1024 failure witnesses and exact GRID1024 anchor. Primary factor is prospectively frozen `AVX512F_PRESENT` vs `AVX512F_ABSENT`; exact CPU model is secondary. NumPy config/runtime SIMD hashes are correlated signatures only. Minimum class size is four in each AVX512F class. Stable OS/kernel/compiler/Python/NumPy/SciPy signature is a required control. Causal AVX512 claims are forbidden from observational stratification.

## Exact next order

1. Continue only V0.16 run `34793440750`; no duplicate.
2. Wait for invariant + all 24 lanes + single decision barrier; do not inspect partial substantive values.
3. Verify all required job/artifact identities and hashes.
4. Materialize durable V0.16 authority from the frozen classifier.
5. Follow only its encoded `next_stage`.
6. Keep all downstream Layer-B/science gates closed unless later terminal authority explicitly opens them.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and scientific frontier `67%`; reproducibility work alone does not raise them.

No active DSIR ChatGPT automation and no repository cron/schedule research loop were found in the latest explicit check. Avoid duplicate production gates.
