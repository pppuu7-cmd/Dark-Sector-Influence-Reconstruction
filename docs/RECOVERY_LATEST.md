# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this numerical diagnostic chain.

## Closed chain through V0.19/V0.19D

V0.12 `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE` -> V0.13 `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED` -> V0.14 `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED` -> V0.15 `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED` -> V0.16 `HOST_FACTOR_ISOLATION_INCOMPLETE_SAME_CPU_MODEL_VARIATION` -> V0.17 `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED`.

V0.18R terminal authority `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_18R.json`, commit `e192492b5c56fdae91632447cc02d9bfdac942a5`: `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`, effect `+0/+0`. V0.18D commit `728987ddfbc9caddc1202234662b964c6f034b5b` diagnosed the first NumPy validation defect without reading failure-cell responses.

V0.19 terminal authority: `docs/dsir4/authority/LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_19.json`, commit `3d4542b3c3514092fdc99566bed01c877eb77003`. Run `34868672661`, decision job `104060026580`, decision artifact `10358292041`, digest `sha256:a4725493e504c4f3c4f2a3bae5a1927abd58fde8ba22e90546d32d3bce0a8d87`. Classification `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`, effect `+0/+0`. Exact-target eligible lanes `R20,R24,R27` met the frozen minimum n=3 but all failed response-free preflight; no substantive response was computed for any invalid-preflight lane.

V0.19D terminal diagnostic authority: `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_VALIDATION_DIAGNOSIS_V0_19D.json`, commit `f29190ead75225d8e8862e44ba06b51555c580b2`. Diagnosis `NUMPY_RAW_CAPABILITY_BITS_NOT_RUNTIME_DISPATCH_VALIDATION_TARGET`. NumPy 1.26.4 runtime reporting iterates `__cpu_dispatch__` and tests `__cpu_features__[feature]`; residual raw capability bits outside the dispatch list are diagnostic, not proof of active dispatch. V0.19D authorizes exactly `PROSPECTIVELY_FROZEN_NUMPY_RUNTIME_DISPATCH_SEMANTICS_AUDIT`.

## V0.20 — active response-free NumPy runtime dispatch semantics audit

Preregistration: `prereg/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.md`, commit `032ef809a934c4ac0ae8dfb4cb9d2d7b4d35386b`.
Executor: `ci/layerb_beta_numpy_runtime_dispatch_semantics_v0_20.py`, commit `865c241675d18af8e76d4fd632cc803cd6c99869`, blob `1d31907a488224cc510afc7908c888da4bfe08ff`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, commit `de9eae11c49a82b8d01ec405540258927a6a4a43`.
Workflow: `.github/workflows/layerb-beta-numpy-runtime-dispatch-semantics-v0-20.yml`, commit `216677ba6d5733339a634afcf9546cac00343b22`.
Launch/head: `596fbdc15f99a4709756c3df3770fce721b93635`.
Authoritative active run: `34869578874`; exactly one run exists. Invariant audit is terminal `success`. Thirty-two independent NumPy-only host lanes run with `max-parallel:32`.

V0.20 never builds/imports CLASS and never computes a DSIR response. Exact-target EPYC 9V74 lanes record NumPy 1.26.4 `__cpu_baseline__`, `__cpu_dispatch__`, `__cpu_features__`, define active dispatch only as dispatch-list members whose feature state is true, derive the AVX-512 mask only from native `__cpu_dispatch__`, and validate the fresh masked interpreter against that dispatch model. Raw non-dispatch AVX-512 capability bits may remain true. Minimum eligible n=3; profile consistency is frozen across baseline/dispatch/AVX512-dispatch/active-AVX512-dispatch.

## Exact next order

1. Continue only V0.20 run `34869578874`; do not launch a duplicate.
2. Wait for invariant + all 32 lanes + single terminal decision barrier. Technical lane fingerprints are response-free, but only the frozen terminal classifier determines promotion.
3. Verify terminal decision artifact ID/digest and materialize a V0.20 authority.
4. If `NUMPY_AVX512_RUNTIME_DISPATCH_MASK_VALIDATED`, follow only `PROSPECTIVELY_FROZEN_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT` using the exact common profile/mask recorded by V0.20 authority.
5. Otherwise follow only the encoded underpowered/heterogeneous/mask-diagnosis/inconclusive branch.
6. Do not read V0.18R/V0.19 failure-cell responses or salvage them post hoc.
7. Keep full Layer-B, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 and science gates closed unless a later terminal authority explicitly opens them.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
