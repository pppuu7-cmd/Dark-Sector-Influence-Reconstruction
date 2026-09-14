# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Parent terminal authority — V0.17

Terminal authority: `docs/dsir4/authority/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.json`, creation commit `ae9d1532d7ad7479a8eee52d04e974ebf9ab7d17`.

Run `34817501445`: invariant + 32 runtime-state lanes + decision terminal `success`; decision job `103894789121`; decision artifact `10337134088`, digest `sha256:24bf51b3993353dceefe4908955d0e14eb48de06675174e1b7b9ede3ab3f7ae4`.

Classification: `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED`, effect `+0/+0`. In the exact AMD EPYC 9V74 subgroup, `cpu_capability_key` is the first preregistered stable observational stratifier; FPU-control and exact binary identity do not explain the branch, while NumPy dispatch remains correlated. V0.17 authorizes exactly `PROSPECTIVELY_FROZEN_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## Active authoritative frontier — V0.18R controlled dispatch intervention

Scientific preregistration: `prereg/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_18.md`, commit `34c955fcdfca7429b033e8c194de090f4ced8701`.

The original unexecuted V0.18 contract (`288adc096449e72264273937e68ebe1a687b9faa`) was superseded before any workflow/run because its lane implementation computed a native response before eligibility. No V0.18 substantive result exists. V0.18R is a control-only pre-execution sequencing repair; the preregistered science and classifier are unchanged.

Active contract: `docs/dsir4/contracts/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_18R.json`, commit `59ff8aca5360c849fb9e7bba7b314a6009b64444`.
Executor: `ci/layerb_beta_controlled_cpu_capability_dispatch_intervention_v0_18r.py`, commit `7dbcc2dcf30d8351c4d8504226231ff205a5fe94`, blob `820154ac8d121f0eb44904db55640d08ab7fb03a`; substantive child/decision base executor blob `279925c25f2db17ba59d7cbe76f4d2043026da06`.
Workflow: `.github/workflows/layerb-beta-controlled-cpu-capability-dispatch-intervention-v0-18r.yml`, commit `3a0e07263ce1f528c6045c1ff9c3719ef45ea3f4`.
Launch/head: `698b62dab1ecda77724dd6d7def36342cb4372dd`.
Authoritative active run: `34861893888`; exactly one V0.18R run exists. Invariant audit is terminal `success`.

V0.18R has 32 independent host lanes with `max-parallel: 32`. Each lane fingerprints first. Only exact AMD EPYC 9V74 hosts with native AVX512F, native glibc x86-64-v4 and native NumPy AVX512 dispatch are eligible. Ineligible hosts emit provenance-only SKIP and no response values. Eligible lanes execute four paired child conditions on the same host and exact binaries: `NATIVE`, `NUMPY_NO_AVX512`, `GLIBC_NO_AVX512`, `COMBINED_NO_AVX512`. Minimum eligible paired lanes is frozen at 3.

Do not inspect partial substantive response values. Wait for all 32 lanes + single decision barrier, then consume only the frozen decision.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/intervention threshold `<1e-5`; exact binding `<=1e-12`; production sampling `0.00035`; `tol_perturb_integration=1e-12`. Full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
