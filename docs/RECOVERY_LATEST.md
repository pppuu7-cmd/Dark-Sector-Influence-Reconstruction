# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this numerical diagnostic chain.

## Closed chain through V0.20

V0.12 `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE` -> V0.13 `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED` -> V0.14 `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED` -> V0.15 `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED` -> V0.16 `HOST_FACTOR_ISOLATION_INCOMPLETE_SAME_CPU_MODEL_VARIATION` -> V0.17 `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED`.

V0.18R and V0.19 were terminal `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID` validation outcomes and were not scientifically interpreted. V0.19D authority, commit `f29190ead75225d8e8862e44ba06b51555c580b2`, diagnosed `NUMPY_RAW_CAPABILITY_BITS_NOT_RUNTIME_DISPATCH_VALIDATION_TARGET`; no invalid-gate failure-cell response was used.

V0.20 terminal authority: `docs/dsir4/authority/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, commit `e1357e18bf95109e5b05b5e188d8f1e137f761e1`. Run `34869578874`, decision job `104062350580`, decision artifact `10358203034`, digest `sha256:397e2da8f05b92d300bf244f81ee411045508988ad04762ed3868615a66c4002`. Classification `NUMPY_AVX512_RUNTIME_DISPATCH_MASK_VALIDATED`, effect `+0/+0`. Four exact-target eligible hosts shared one exact NumPy 1.26.4 baseline/dispatch profile and all validated masks passed. No CLASS or DSIR response was computed.

Validated NumPy mask: `AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.
Native active AVX-512 dispatch: `AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_SKX`.
Native active non-AVX512 dispatch: `AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`.
V0.20 authorizes exactly `PROSPECTIVELY_FROZEN_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## V0.21 — active validated controlled intervention

Preregistration: `prereg/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.md`, commit `2620148106a66e462e239fb25ab15f8ab800ef52`.
Executor: `ci/layerb_beta_validated_controlled_cpu_capability_dispatch_intervention_v0_21.py`, commit `110fc5b7b33b9ae2cc1baa9e8d8c0e91e7252e0f`, blob `5edfe04950b9c8e2e859eed590312e78a01f8386`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.json`, commit `a305c2e8e5106e031e0f7b5d6f3ee9d742b9cf39`.
Workflow: `.github/workflows/layerb-beta-validated-controlled-cpu-capability-dispatch-intervention-v0-21.yml`, commit `7f0c8e876105fe9cf7de87b37553b268f1489194`.
Launch/head: `3f522ec7ae9308745905be8657bdb2e5c2117f13`.
Authoritative active run: `34870133635`; exactly one run exists. Invariant frozen source/profile/blob verification passed; 32 independent host lanes are running with `max-parallel:32`.

Eligibility requires exact AMD EPYC 9V74, native glibc x86-64-v4, NumPy 1.26.4 and the exact V0.20 baseline/dispatch/active-dispatch profile. Eligible lanes first perform four response-free condition fingerprints. NumPy-only/combined must eliminate active AVX-512 members of `__cpu_dispatch__` while preserving non-AVX512 active dispatch; glibc-only/combined must disable glibc x86-64-v4. Binary identity must remain constant. Invalid-preflight lanes compute no substantive response. Only fully valid lanes compute the four paired solver conditions.

The original V0.18 scientific hypothesis remains frozen: exact two replay-failure cells + one anchor, V0.17 native/alternate branch references, minimum eligible n=3, replay/intervention `<1e-5`, exact binding `<=1e-12`, production h/sampling/tolerance unchanged. No partial V0.21 substantive response may be inspected before the terminal decision.

## Exact next order

1. Continue only V0.21 run `34870133635`; do not launch a duplicate.
2. Do not inspect partial substantive lane values.
3. Wait for invariant + all 32 lanes + the single decision barrier.
4. Verify terminal decision artifact ID/digest and materialize V0.21 authority from the frozen classifier.
5. Follow only its encoded `next_stage`.
6. Even a supported intervention is a numerical mechanism result only; full Layer-B and all physical-science gates remain closed unless a later authority explicitly opens them.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
