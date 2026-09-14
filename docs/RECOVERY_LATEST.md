# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention/reproducibility threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this numerical diagnostic chain.

## Root cause of repeated invalid intervention iterations

V0.18R and V0.19 were terminal `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`, although their GitHub Actions infrastructure completed. The repeated defect was the validation observable: the executors treated every AVX-512-labelled raw NumPy `__cpu_features__` capability bit as if it had to be disabled by `NPY_DISABLE_CPU_FEATURES`.

V0.19D authority (`f29190ead75225d8e8862e44ba06b51555c580b2`) diagnosed `NUMPY_RAW_CAPABILITY_BITS_NOT_RUNTIME_DISPATCH_VALIDATION_TARGET`. In NumPy 1.26.4, runtime SIMD dispatch is governed by the dispatchable set `__cpu_dispatch__`; runtime-active dispatch is evaluated from dispatch membership plus its corresponding `__cpu_features__` value. Several raw hardware capability bits can correctly remain true because they are not active members of the NumPy dispatch set. Therefore V0.18R/V0.19 rejected a functioning mask with the wrong positive control. Their failure-cell results remain scientifically unusable and were not salvaged.

V0.20 separated semantics validation from the scientific intervention and response-free validated the correct dispatch observable. Authority `docs/dsir4/authority/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, commit `e1357e18bf95109e5b05b5e188d8f1e137f761e1`; classification `NUMPY_AVX512_RUNTIME_DISPATCH_MASK_VALIDATED`. Exact validated mask: `AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.

## V0.21 terminal causal mechanism authority

Authority: `docs/dsir4/authority/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.json`, creation commit `7b6fc404e70ab75f1a7b7053123e7cf5dc46967e`.
Preregistration `2620148106a66e462e239fb25ab15f8ab800ef52`; executor `110fc5b7b33b9ae2cc1baa9e8d8c0e91e7252e0f`; contract `a305c2e8e5106e031e0f7b5d6f3ee9d742b9cf39`; workflow `7f0c8e876105fe9cf7de87b37553b268f1489194`; launch/head `3f522ec7ae9308745905be8657bdb2e5c2117f13`.

Run `34870133635` terminal `success`: invariant + all 32 lanes + decision. Decision job `104071826031`; artifact `10359787747`; digest `sha256:5b85934b23cc01cd6a4c6f3c3662d9d196a491d52addf129127e5d63e8ca6e13`.
Classification `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`, effect `+0/+0`.
Eligible/preflight-valid exact AMD EPYC 9V74 lanes `R03,R15,R19,R22,R28` (`n=5`, minimum 3). NumPy-only branch switch supported; glibc-only branch switch not supported; combined branch switch supported. Exact binding maximum `1.6551974349255386e-16`; anchor condition spread `1.0758876522574515e-6`.

Interpretation ceiling: V0.21 causally localizes the numerical response branch to NumPy AVX-512 runtime dispatch under the frozen numerical object. It does not validate full Layer-B and is not dark-sector evidence.

V0.21 authorizes exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT`.

## Exact next order

1. Do not repeat the invalid V0.18R/V0.19 validation design.
2. Prospectively preregister the forced-baseline cross-host reproducibility audit.
3. Fingerprint native host/NumPy dispatch response-free and require representation of distinct native dispatch classes.
4. Before substantive response, validate that the exact V0.20 NumPy mask yields the frozen non-AVX512 active dispatch profile.
5. Compute only the forced-baseline object across eligible hosts and test cross-host replay-failure/anchor spread against `<1e-5` and frozen alternate-branch agreement.
6. If reproducibility is supported, only a later prospectively frozen production-h replay revalidation may be opened; no full Layer-B or physical gate is implied.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
