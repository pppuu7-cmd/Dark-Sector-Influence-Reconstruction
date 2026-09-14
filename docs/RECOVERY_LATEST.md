# DSIR authoritative recovery — latest

Updated: 2026-09-14. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; scientific response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; technical replay/intervention/reproducibility threshold `<1e-5`. Covariance/whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this numerical diagnostic chain.

## Root cause of repeated invalid intervention iterations

V0.18R and V0.19 were terminal `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID` despite successful GitHub Actions execution. The common defect was the validator: it treated every raw AVX-512-labelled NumPy `__cpu_features__` capability bit as if `NPY_DISABLE_CPU_FEATURES` had to turn it false.

V0.19D (`f29190ead75225d8e8862e44ba06b51555c580b2`) diagnosed `NUMPY_RAW_CAPABILITY_BITS_NOT_RUNTIME_DISPATCH_VALIDATION_TARGET`. NumPy 1.26.4 runtime dispatch is determined by `__cpu_dispatch__` membership and the corresponding `__cpu_features__` state. Raw non-dispatch hardware bits may correctly remain true. V0.18R/V0.19 therefore rejected a functioning mask with the wrong positive control; their scientific results remain invalid and were not salvaged.

V0.20 separated mask-semantics validation from science and response-free validated the exact runtime-dispatch mask. Authority `docs/dsir4/authority/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, commit `e1357e18bf95109e5b05b5e188d8f1e137f761e1`; classification `NUMPY_AVX512_RUNTIME_DISPATCH_MASK_VALIDATED`.

## V0.21 terminal causal mechanism authority

Authority `docs/dsir4/authority/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.json`, creation commit `7b6fc404e70ab75f1a7b7053123e7cf5dc46967e`.
Run `34870133635` terminal success; decision job `104071826031`; artifact `10359787747`; digest `sha256:5b85934b23cc01cd6a4c6f3c3662d9d196a491d52addf129127e5d63e8ca6e13`.
Classification `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`, effect `+0/+0`.
Five exact-target valid lanes `R03,R15,R19,R22,R28`. NumPy-only switch supported, glibc-only not supported, combined supported. Maximum exact binding mismatch `1.6551974349255386e-16`; anchor condition spread `1.0758876522574515e-6`.

This causally localizes the hosted numerical branch to NumPy AVX-512 runtime dispatch under the frozen numerical object. It is not Layer-B validation or dark-sector evidence.

## V0.22 — active forced-baseline cross-host reproducibility audit

Preregistration `prereg/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.md`, commit `20403f5dbd2a3772752852c0c84ce306d7971c43`.
Executor `ci/layerb_beta_forced_baseline_cross_host_reproducibility_v0_22.py`, commit `82684fa591911761720e744e5462e51902569fa2`, blob `7921f856f468d9b73889130df39148ccca3d048d`.
Contract `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.json`, commit `bc10698aa746747955d27ce2099867de236ef598`.
Workflow `.github/workflows/layerb-beta-forced-baseline-cross-host-reproducibility-v0-22.yml`, commit `8c36fdeece4cfc6b6f6c8477282a40c9a2ccff25`.
Launch/head `d2e4e2cfbc122683d2390369dc087b55e89fb2fc`.
Authoritative run `34875798025`; exactly one run exists. Invariant audit is terminal success. Thirty-two independent hosted lanes use `max-parallel:32`.

V0.22 contains an explicit anti-regression control against the V0.18R/V0.19 bug: raw non-dispatch AVX-512 capability bits are forbidden as validation targets. Native and forced NumPy fingerprints are response-free. Candidate hosts must share the frozen NumPy 1.26.4 baseline/dispatch build profile. Under the exact V0.20 mask, forced active AVX-512 dispatch must be empty and active non-AVX512 dispatch must remain exactly `AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`. No unmasked substantive response is computed.

Power is frozen at total eligible n>=6, with at least n>=3 `NATIVE_AVX512_ACTIVE` and n>=3 `NATIVE_AVX512_INACTIVE`. Supported classification requires both replay-failure cross-host spreads, both native-class mean separations and anchor cross-host spread `<1e-5`, plus every forced failure response within `<1e-5` of the frozen V0.17 alternate branch.

## Exact next order

1. Continue only run `34875798025`; no duplicate.
2. Do not inspect partial substantive V0.22 values.
3. Wait for all 32 lanes and one decision barrier.
4. Verify decision artifact ID/digest and materialize V0.22 authority.
5. Follow only its encoded `next_stage`.
6. If supported, the only allowed successor is `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_AUDIT`.
7. Full Layer-B and physical-science gates remain closed.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
