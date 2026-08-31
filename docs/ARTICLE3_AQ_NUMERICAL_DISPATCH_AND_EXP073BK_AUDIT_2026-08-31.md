# Article-3 AQ numerical-dispatch root-cause audit and Exp073BK result — 2026-08-31

**Project:** DSIR only.  
**Classification:** nonclassifying root-cause / numerical-infrastructure audit.  
**Authority:** false.  
**Scientific readiness increment:** `+0`.  
**Draft/data readiness increment:** `+0`.

This audit cannot alter the permanent Exp073AQ scientific FAIL and cannot alter the active Exp073BJ criteria.

## 1. Permanent Exp073AQ authority remains unchanged

Hosted run `33327372191` remains:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Frozen selected-window facts remain:

- replica A SHA `979c61faea99cf60146078ccdd5a9c75547dcc5a689ee48c4c5f309cf6a10b69`;
- replica B SHA `5b02a691607dd21ede7601f081767ac3713e300abd5a9e358e4593a6ec486225`;
- differing entries `472997 / 479232`;
- maximum absolute difference `2.0816681711721685e-17`;
- mean absolute difference `2.5248672723363528e-20`.

No numerical closeness can rescue this exact FAIL.

## 2. AQ post-authority ULP / spectral diagnostic

Local inspection of the two immutable AQ selected windows gives:

- differing fraction `0.9869896000267094`;
- Frobenius norm of A-B `1.6322811908586484e-16`;
- positive differing entries `238681`, negative `234316`;
- median ULP distance among differing entries `193`;
- 90th percentile ULP distance `2559`;
- 99th percentile about `28395`;
- 99.9th percentile about `279084`;
- maximum ULP distance `338924841` (large ULP counts occur near extremely small values and are not evidence of large physical error).

SVD of the full `[39,12288]` difference matrix shows a distributed, not rank-one, error:

- 50% difference-energy rank: `5`;
- 90% difference-energy rank: `20`;
- 99% difference-energy rank: `33`;
- effective energy rank about `13.82`;
- first singular mode contains about `14.82%` of total difference energy.

A best left-multiplication model `D ≈ M @ W_B` explains about `55.2%` of the difference Frobenius energy. This is diagnostic only: it is compatible with a substantial inversion/row-mixing contribution, but the remaining residual also permits upstream coupling-level bit drift.

## 3. AQ runtime SIMD exposure was not actually identical

The historical environment receipts used the same Ubuntu image family, Python `3.11.16`, PyMaster/NaMaster `2.7`, NumPy `2.4.6`, Healpy `1.20.0`, Astropy `8.0.1`, and the same nominal one-thread controls.

However runtime CPU-feature dispatch differed materially:

- AQ replica A: AMD EPYC 7763; NumPy runtime SIMD found through `X86_V3`, without X86_V4/AVX-512;
- AQ replica B: AMD EPYC 9V74; NumPy runtime SIMD exposed `X86_V3`, `X86_V4`, `AVX512_ICL` and AVX-512 CPU flags.

Therefore the frozen thread controls and package versions did **not** pin the complete floating-point execution environment. This is candidate root-cause evidence only; it is not itself proof of the AQ causal path.

## 4. Local causal BLAS-microkernel experiment on a real DES-derived compact A

Using the immutable provisional Exp073BD Wm_S2 branch-B compact array, SHA

`a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e`,

the exact same `K=AQ` and `W=numpy.linalg.solve(K,A)` was executed while changing only OpenBLAS microkernel dispatch.

Observed canonical W SHA groups:

- `OPENBLAS_CORETYPE=Haswell` or `Zen` -> `ae2b070b84e5f763d77216fe35aab2921074469a881845c015302918018d03aa`;
- `OPENBLAS_CORETYPE=SkylakeX`, `Zen2`, or `Cooperlake` -> `63199de7f8cbf8662866d1262f5068a0852cb938fd31034b3fc11fe21e518186`.

The second SHA exactly equals the stored hosted Exp073BD branch-B final W SHA.

Haswell versus SkylakeX on the identical compact A:

- differing entries `393792 / 479232` (`82.17%`);
- maximum absolute difference `2.7755575615628914e-17`;
- mean absolute difference `1.3877068844913707e-20`;
- Frobenius difference `1.4353781913012518e-16`;
- median ULP distance `3`;
- 90th percentile `35`;
- 99th percentile `423`.

This is a direct causal demonstration that runtime BLAS dispatch alone can alter final float64 window bits at the same absolute scale as the historical AQ mismatch. It does **not** prove that AQ itself was caused solely by NumPy/OpenBLAS because AQ used the stock NaMaster workspace/finalizer path rather than the later Python low-memory solve.

## 5. Exp073BK prospectively frozen hosted cross-host QA

Preregistration commit:

`96a9c3747571f56f41ab88a1b08f195486ac0033`

Implementation commit:

`1a4886b49d2638e07d447be946ff82033eac3419`

Workflow commit:

`11c8a55ab7574b98c75a0c8056cd7d328d697704`

Trigger/head:

`d0d21bc0a551b12934e4d8fc95b72b8b23e123f7`

Hosted run:

`33383770182`

Replica jobs:

- A `99461686927` — AMD EPYC 9V74;
- B `99461686872` — AMD EPYC 9V74;
- C `99461686803` — AMD EPYC 7763;
- D `99461686678` — AMD EPYC 7763.

Comparator job `99461909878` completed successfully.

Comparator artifact:

- ID `9754784036`;
- digest `sha256:8ac37cbcb504f57ce19dd88274a5b04d8076d3a29580b532aa208d6d6cef7f98`.

All four frozen policies were exactly equal across all four hosted replicas:

- `default_t1`: `EXACT_CROSSHOST_EQUAL`;
- `haswell_t1`: `EXACT_CROSSHOST_EQUAL`;
- `default_t2`: `EXACT_CROSSHOST_EQUAL`;
- `haswell_t2`: `EXACT_CROSSHOST_EQUAL`.

All 16 resulting windows had exactly the same canonical SHA:

`ae2b070b84e5f763d77216fe35aab2921074469a881845c015302918018d03aa`.

Thus pinned NumPy `2.4.6` plus pinned conda-forge OpenBLAS lineage produced exact finalizer reproducibility across the two hosted CPU model families in this run, for both one and two threads.

## 6. Important virtualization nuance

The Exp073BK EPYC 9V74 replica inspected locally did **not** expose AVX-512 to NumPy; its runtime feature set was effectively X86_V3. This differs from historical AQ replica B, where an EPYC 9V74 runner exposed X86_V4/AVX-512.

Therefore CPU model name is not a sufficient numerical-lineage identifier. The hypervisor-exposed feature set and actual BLAS/runtime dispatch must be captured and, where exact reproducibility is required, prospectively pinned or replaced by a fixed-operation implementation.

Exp073BK does not isolate an X86_V4 versus X86_V3 cross-host pair because all four BK workers were effectively in the same lower SIMD class. Its strongest result is instead that an explicitly pinned numerical runtime removes model-family differences for this real compact finalizer case.

## 7. Deterministic fixed-operation LU prototype — local diagnostic

A fixed-order partial-pivot LU implementation was tested on the same real `[39,12288]` compact A without using BLAS for the solve itself.

Across local forced `Haswell`, `SkylakeX`, and `Zen2` runtime policies it produced the same canonical W SHA:

`f3a22c35dff1f3b27f5f22e7966c1c926fbbc3a965293f88a9bf0b84fa97cf79`.

Numerical checks:

- `max(abs(WQ-I)) = 1.2212453270876722e-15`;
- Frobenius `||WQ-I|| = 2.946830402219245e-15`;
- `||KW-A||/||A|| ≈ 4.0e-16`.

A 100-digit mpmath reference on ten representative ell columns showed the deterministic LU and the two BLAS variants all remain at the same ordinary float64 accuracy scale. This is sufficient to justify a separate hosted cross-host QA, but not scientific authority.

## 8. AQ-specific route warning

The historical AQ frozen runner `ci/exp073aa_article3_des_angular_task_runner_v0_1.py` did not use the later Python low-memory `numpy.linalg.solve` route. It called stock:

`NmtWorkspace.compute_coupling_matrix(...)` followed by `get_bandpower_windows()`.

Therefore AQ-specific causal attribution requires inspection of the exact NaMaster 2.7 stock workspace construction and inversion path. The BLAS microkernel experiment proves that this class of runtime dispatch can matter at the relevant bit scale; it does not identify which AQ internal operation generated the mismatch.

## 9. Scientific accounting

- Exp073AQ remains permanent exact-repeatability scientific FAIL.
- Exp073BK is nonclassifying `+0/+0`.
- active Exp073BJ is unchanged.
- Article-3 Verified readiness remains `52.0%`.
- Article-3 Draft/data readiness remains `53.7%`.
- Layer A/B and covariance/whitening remain unauthorized.
- G7/G8/G9 remain OPEN; G8 jump remains forbidden.
