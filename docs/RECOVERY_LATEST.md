# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this diagnostic chain.

## Closed reproducibility chain through V0.17

V0.12 `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE` -> V0.13 `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED` -> V0.14 `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED` -> V0.15 `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED` -> V0.16 `HOST_FACTOR_ISOLATION_INCOMPLETE_SAME_CPU_MODEL_VARIATION`.

V0.17 terminal authority: `docs/dsir4/authority/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.json`, creation commit `ae9d1532d7ad7479a8eee52d04e974ebf9ab7d17`, run `34817501445`, decision job `103894789121`, artifact `10337134088`, digest `sha256:24bf51b3993353dceefe4908955d0e14eb48de06675174e1b7b9ede3ab3f7ae4`.

V0.17 classification: `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED`, effect `+0/+0`. Exact AMD EPYC 9V74 target subgroup `n=8`. Failure spreads `1.4832557923366384e-4` and `1.0478978062540487e-5`; anchor spread `1.0758876522574515e-6`. `cpu_capability_key` is the first frozen-hierarchy factor with stable repeated groups separated on both failure cells. FPU-control and exact binary/runtime-library identity are non-explanatory; NumPy runtime dispatch also stratifies and remains correlated. This is observational numerical-runtime stratification only.

V0.17 authorizes exactly `PROSPECTIVELY_FROZEN_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## V0.18R — active prospectively frozen controlled intervention

Preregistration: `prereg/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_18.md`, commit `34c955fcdfca7429b033e8c194de090f4ced8701`.

The first unexecuted V0.18 implementation/contract was superseded before any run because it violated preregistered eligibility sequencing by computing NATIVE response before eligibility. No result was observed and no scientific predicate was changed. V0.18R is the durable pre-execution repair.

Contract: `docs/dsir4/contracts/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_18R.json`, commit `59ff8aca5360c849fb9e7bba7b314a6009b64444`.
Executor: `ci/layerb_beta_controlled_cpu_capability_dispatch_intervention_v0_18r.py`, commit `7dbcc2dcf30d8351c4d8504226231ff205a5fe94`, blob `820154ac8d121f0eb44904db55640d08ab7fb03a`; base child/decision executor blob `279925c25f2db17ba59d7cbe76f4d2043026da06`.
Workflow: `.github/workflows/layerb-beta-controlled-cpu-capability-dispatch-intervention-v0-18r.yml`, commit `3a0e07263ce1f528c6045c1ff9c3719ef45ea3f4`.
Launch/head: `698b62dab1ecda77724dd6d7def36342cb4372dd`.
Authoritative active run: `34861893888`; exactly one run exists; invariant audit is terminal `success`.

Each of 32 independent host lanes fingerprints before substantive work. Only exact AMD EPYC 9V74 + native AVX512F + native glibc x86-64-v4 + native NumPy AVX512 hosts are eligible. Ineligible lanes are provenance-only. Eligible lanes compare four fresh child-process conditions on the same host/binaries: native, NumPy AVX512 disabled, glibc AVX512 hwcaps disabled, and combined disabled. Minimum eligible paired lanes is 3. Branch references and all thresholds were frozen before execution.

## Exact next order

1. Continue only V0.18R run `34861893888`; do not launch a duplicate.
2. Do not inspect partial substantive response values.
3. Wait for invariant + all 32 lanes + single decision barrier.
4. Verify terminal artifact identity/digest and materialize V0.18R authority from the frozen classifier.
5. Follow only its encoded `next_stage`.
6. Keep full Layer-B, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 and science gates closed unless later authority explicitly opens them.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
