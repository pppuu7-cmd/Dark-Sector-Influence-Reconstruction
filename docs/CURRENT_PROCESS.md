# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Latest terminal scientific/numerical authority — V0.18R

V0.17 authority `docs/dsir4/authority/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.json` established observational `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED` and authorized a controlled dispatch intervention.

V0.18R terminal authority: `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_18R.json`, creation commit `e192492b5c56fdae91632447cc02d9bfdac942a5`.
Run `34861893888` is terminal `success`: invariant + 32 dispatch lanes + decision all completed. Decision job `104045296799`; decision artifact `10355468958`, digest `sha256:953a2f0472452828b155dee1ff9b47833ba0c92859ae39c69220de6f82065868`.
Classification: `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`, effect `+0/+0`. Eligible exact-target paired hosts `n=7` exceeded the frozen minimum `n=3`; exact binding and anchor invariants passed. The result is not interpretable as support or no-effect because an intervention positive control failed.

## Terminal validation diagnosis — V0.18D

Authority: `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_VALIDATION_DIAGNOSIS_V0_18D.json`, commit `728987ddfbc9caddc1202234662b964c6f034b5b`.
Diagnosis: `NUMPY_AVX512_MASK_INCOMPLETE_AND_VALIDATOR_OVERBROAD`.

All seven V0.18R eligible hosts had the same native active NumPy AVX-512 set:
`AVX512BITALG, AVX512BW, AVX512CD, AVX512DQ, AVX512F, AVX512IFMA, AVX512VBMI, AVX512VBMI2, AVX512VL, AVX512VNNI, AVX512VPOPCNTDQ, AVX512_CLX, AVX512_CNL, AVX512_ICL, AVX512_SKX`.
The V0.18R NumPy mask disabled only a subset and left nine native-active AVX-512 features enabled, while its validator required zero active AVX-512 features. Native and glibc-only controls validated; NumPy-only and combined controls therefore failed by construction. Binary identities were constant; no V0.18R failure-cell response values were inspected for this diagnosis. V0.18D authorizes exactly `PROSPECTIVELY_FROZEN_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## Active authoritative frontier — V0.19 repaired controlled dispatch intervention

Preregistration: `prereg/LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_19.md`, commit `a7fc1d1740f64d197fcc269cdd7bf95a5fda080b`.
Final executor: `ci/layerb_beta_repaired_controlled_cpu_capability_dispatch_intervention_v0_19.py`, commit `b385cc3b2719e8672672c595a40181814ba0a0ee`, blob `6df0890f5646df1c309aa8369232b77c0120dce0`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_19.json`, commit `996f0b0657dda4bc84a62d020cba89c599e8b509`.
Workflow: `.github/workflows/layerb-beta-repaired-controlled-cpu-capability-dispatch-intervention-v0-19.yml`, commit `94e39c2ab35b1172e9d145b413e015297a9be2d4`.
Launch/head: `8f04577d97e62ed4273ef5e5ea2bb41382582e5b`.
Authoritative active run: `34868672661`; exactly one run exists. Invariant identity/repair-scope checks and py_compile passed; the 32-host matrix is active with `max-parallel:32`.

V0.19 preserves the V0.18 hypothesis, exact cells, V0.17 branch references, all thresholds, target CPU and minimum eligible `n=3`. The only intervention repair is a complete prospectively frozen 15-feature NumPy AVX-512 mask plus exact validation. Every eligible host first performs a **response-free four-condition preflight**; a failed preflight produces `INVALID` without computing substantive response. Only successful preflight lanes execute paired `NATIVE`, `NUMPY_NO_AVX512`, `GLIBC_NO_AVX512`, `COMBINED_NO_AVX512` solver conditions.

Do not inspect partial substantive V0.19 response values. Consume only the single terminal decision after all 32 lanes.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/intervention threshold `<1e-5`; exact binding `<=1e-12`; production sampling `0.00035`; `tol_perturb_integration=1e-12`. Full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
