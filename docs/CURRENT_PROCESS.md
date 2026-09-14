# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Latest terminal intervention authority — V0.19

V0.17 established observational `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED` and authorized a controlled dispatch intervention. V0.18R was terminal `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`; its diagnosis V0.18D identified an incomplete NumPy mask plus an overbroad raw-feature validator.

V0.19 attempted a repaired causal intervention with response-free preflight. Terminal authority: `docs/dsir4/authority/LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_19.json`, creation commit `3d4542b3c3514092fdc99566bed01c877eb77003`.
Run `34868672661` is terminal `success`: invariant + 32 lanes + decision all completed. Decision job `104060026580`; decision artifact `10358292041`, digest `sha256:a4725493e504c4f3c4f2a3bae5a1927abd58fde8ba22e90546d32d3bce0a8d87`.
Classification: `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`, effect `+0/+0`. Eligible exact-target lanes were `R20,R24,R27` (n=3, frozen minimum 3), and all three failed only the response-free intervention preflight. `substantive_response_computed=false` for all invalid-preflight lanes. Therefore V0.19 neither supports nor rejects the dispatch mechanism.

## Terminal validation diagnosis — V0.19D

Authority: `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_VALIDATION_DIAGNOSIS_V0_19D.json`, commit `f29190ead75225d8e8862e44ba06b51555c580b2`.
Diagnosis: `NUMPY_RAW_CAPABILITY_BITS_NOT_RUNTIME_DISPATCH_VALIDATION_TARGET`.

All three eligible preflights reproduced the same pattern: native and glibc-only controls valid; NumPy-only and combined invalid under the V0.19 raw-feature criterion; binary identity constant; no substantive response computed. NumPy 1.26.4 `show_runtime()` treats `__cpu_dispatch__` as the dispatchable non-baseline feature list and reads `__cpu_features__[feature]` only for those dispatch entries. Therefore residual raw AVX-512 capability bits outside `__cpu_dispatch__` are not themselves proof of active runtime dispatch. V0.19D authorizes exactly `PROSPECTIVELY_FROZEN_NUMPY_RUNTIME_DISPATCH_SEMANTICS_AUDIT`.

## Active authoritative frontier — V0.20 response-free NumPy dispatch semantics audit

Preregistration: `prereg/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.md`, commit `032ef809a934c4ac0ae8dfb4cb9d2d7b4d35386b`.
Executor: `ci/layerb_beta_numpy_runtime_dispatch_semantics_v0_20.py`, commit `865c241675d18af8e76d4fd632cc803cd6c99869`, blob `1d31907a488224cc510afc7908c888da4bfe08ff`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, commit `de9eae11c49a82b8d01ec405540258927a6a4a43`.
Workflow: `.github/workflows/layerb-beta-numpy-runtime-dispatch-semantics-v0-20.yml`, commit `216677ba6d5733339a634afcf9546cac00343b22`.
Launch/head: `596fbdc15f99a4709756c3df3770fce721b93635`.
Authoritative active run: `34869578874`; exactly one run exists. Invariant audit is terminal `success`; 32 independent lightweight NumPy-only lanes are active with `max-parallel:32`.

V0.20 computes **no CLASS/DSIR response**. Each lane records NumPy 1.26.4 `__cpu_baseline__`, `__cpu_dispatch__`, `__cpu_features__`; exact-target EPYC 9V74 lanes derive `NPY_DISABLE_CPU_FEATURES` only from native AVX-512 members of `__cpu_dispatch__`, then verify in a fresh masked interpreter that those dispatch targets are inactive while non-AVX512 dispatch is preserved. Raw non-dispatch AVX-512 capability bits are allowed to remain true. Minimum eligible lanes is frozen at 3.

Exact next order: do not duplicate V0.20; wait for all 32 lanes + single decision barrier; materialize V0.20 authority from the frozen classifier; follow only its `next_stage`. If mask validation passes, only then may a separately preregistered validated causal intervention reopen the numerical response test.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/intervention threshold `<1e-5`; exact binding `<=1e-12`; production sampling `0.00035`; `tol_perturb_integration=1e-12`. Full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
