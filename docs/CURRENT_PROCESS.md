# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Closed numerical-runtime chain through V0.20

V0.17 terminal classification `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED` established observational host/runtime stratification only.
V0.18R and V0.19 terminal classifications were both `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`; their intervention-validation failures were diagnosed prospectively without salvaging or using invalid-gate failure-cell response values.

V0.19D authority `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_VALIDATION_DIAGNOSIS_V0_19D.json`, commit `f29190ead75225d8e8862e44ba06b51555c580b2`, identified that raw NumPy `__cpu_features__` AVX-512 capability bits were the wrong validation observable and authorized a response-free NumPy runtime-dispatch semantics audit.

V0.20 terminal authority: `docs/dsir4/authority/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, creation commit `e1357e18bf95109e5b05b5e188d8f1e137f761e1`.
Run `34869578874` is terminal success: invariant + 32 NumPy-only lanes + decision. Decision job `104062350580`; decision artifact `10358203034`, digest `sha256:397e2da8f05b92d300bf244f81ee411045508988ad04762ed3868615a66c4002`.
Classification: `NUMPY_AVX512_RUNTIME_DISPATCH_MASK_VALIDATED`, effect `+0/+0`; eligible exact-target lanes `R01,R15,R29,R32` (n=4, frozen minimum 3), one common runtime profile, all masks valid, no CLASS import and no DSIR response computation.
Validated NumPy 1.26.4 mask exactly: `AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.
Native active AVX-512 dispatch exactly: `AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_SKX`; active non-AVX512 dispatch exactly: `AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`.
V0.20 authorizes exactly `PROSPECTIVELY_FROZEN_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## Active authoritative frontier — V0.21 validated causal intervention

Preregistration: `prereg/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.md`, commit `2620148106a66e462e239fb25ab15f8ab800ef52`.
Executor: `ci/layerb_beta_validated_controlled_cpu_capability_dispatch_intervention_v0_21.py`, commit `110fc5b7b33b9ae2cc1baa9e8d8c0e91e7252e0f`, blob `5edfe04950b9c8e2e859eed590312e78a01f8386`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.json`, commit `a305c2e8e5106e031e0f7b5d6f3ee9d742b9cf39`.
Workflow: `.github/workflows/layerb-beta-validated-controlled-cpu-capability-dispatch-intervention-v0-21.yml`, commit `7f0c8e876105fe9cf7de87b37553b268f1489194`.
Launch/head: `3f522ec7ae9308745905be8657bdb2e5c2117f13`.
Authoritative active run: `34870133635`; exactly one run exists. Invariant identity/profile/blob checks passed. Thirty-two independent hosted lanes run with `max-parallel:32`.

Eligibility requires exact AMD EPYC 9V74 plus the exact V0.20 NumPy native dispatch profile and native glibc x86-64-v4. Every eligible lane performs a response-free four-condition preflight using the V0.20 validated NumPy mask and the already validated glibc mask. Only a preflight-valid lane computes paired `NATIVE`, `NUMPY_NO_AVX512`, `GLIBC_NO_AVX512`, `COMBINED_NO_AVX512` solver responses.

Scientific/numerical cells, V0.17 branch references, minimum eligible n=3, `<1e-5` intervention/replay threshold, anchor criterion, production h/sampling/tolerance and decision hierarchy were frozen before execution and remain unchanged from the original V0.18 hypothesis. Do not inspect partial substantive V0.21 response values; consume only the terminal decision.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/intervention threshold `<1e-5`; exact binding `<=1e-12`; production sampling `0.00035`; `tol_perturb_integration=1e-12`. Full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
