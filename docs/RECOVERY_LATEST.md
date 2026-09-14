# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this numerical diagnostic chain.

## Closed chain through V0.18R/V0.18D

V0.12 `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE` -> V0.13 `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED` -> V0.14 `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED` -> V0.15 `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED` -> V0.16 `HOST_FACTOR_ISOLATION_INCOMPLETE_SAME_CPU_MODEL_VARIATION` -> V0.17 `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED`.

V0.18R terminal authority: `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_18R.json`, commit `e192492b5c56fdae91632447cc02d9bfdac942a5`. Run `34861893888`; decision job `104045296799`; decision artifact `10355468958`, digest `sha256:953a2f0472452828b155dee1ff9b47833ba0c92859ae39c69220de6f82065868`. Classification `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`, effect `+0/+0`; 7 eligible exact-target hosts, minimum 3; numerical invariant and exact binding passed. This is neither causal support nor no-effect.

V0.18D terminal diagnostic authority: `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_VALIDATION_DIAGNOSIS_V0_18D.json`, commit `728987ddfbc9caddc1202234662b964c6f034b5b`. Diagnosis `NUMPY_AVX512_MASK_INCOMPLETE_AND_VALIDATOR_OVERBROAD`. The old NumPy mask disabled only a subset of the exact native-active 15-feature AVX-512 dispatch set while the validator required zero active AVX-512 features. Native and glibc-only controls validated on all 7 eligible hosts; NumPy-only and combined were invalid by construction. Binary identity was constant. No substantive V0.18R failure-cell responses were read for the diagnosis. Authorized successor exactly: `PROSPECTIVELY_FROZEN_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## V0.19 — active repaired prospectively frozen intervention

Preregistration: `prereg/LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_19.md`, commit `a7fc1d1740f64d197fcc269cdd7bf95a5fda080b`.
Executor: `ci/layerb_beta_repaired_controlled_cpu_capability_dispatch_intervention_v0_19.py`, final commit `b385cc3b2719e8672672c595a40181814ba0a0ee`, blob `6df0890f5646df1c309aa8369232b77c0120dce0`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_19.json`, commit `996f0b0657dda4bc84a62d020cba89c599e8b509`.
Workflow: `.github/workflows/layerb-beta-repaired-controlled-cpu-capability-dispatch-intervention-v0-19.yml`, commit `94e39c2ab35b1172e9d145b413e015297a9be2d4`.
Launch/head: `8f04577d97e62ed4273ef5e5ea2bb41382582e5b`.
Authoritative active run: `34868672661`; exactly one run exists. Invariant source-identity/repair-scope checks and py_compile passed. Thirty-two independent host lanes are running with `max-parallel:32`.

Eligibility is prospectively stricter: exact AMD EPYC 9V74, native AVX512F, glibc x86-64-v4 active, and the exact frozen native NumPy active AVX-512 set: `AVX512BITALG,AVX512BW,AVX512CD,AVX512DQ,AVX512F,AVX512IFMA,AVX512VBMI,AVX512VBMI2,AVX512VL,AVX512VNNI,AVX512VPOPCNTDQ,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_SKX`.

Every eligible lane performs four response-free condition fingerprints first. NumPy-only and combined must have zero active NumPy AVX-512 features; glibc-only must disable x86-64-v4 while preserving the exact 15-feature NumPy set. If preflight fails, no substantive response is computed and the terminal classifier returns `INVALID`. Only preflight-valid lanes perform the four paired solver conditions. Scientific hypothesis, diagnostic cells, V0.17 branch references, thresholds, target model, minimum eligible `n=3` and decision semantics are unchanged from V0.18.

## Exact next order

1. Continue only V0.19 run `34868672661`; do not launch a duplicate.
2. Do not inspect partial substantive V0.19 response values or use lane timing/identity as a classifier.
3. Wait for invariant + all 32 lanes + single decision barrier.
4. Verify terminal decision artifact ID/digest and materialize a V0.19 authority from the frozen decision.
5. Follow only its encoded `next_stage`.
6. Keep full Layer-B, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 and science gates closed unless a later terminal authority explicitly opens them.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
