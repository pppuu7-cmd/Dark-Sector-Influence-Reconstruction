# DSIR recovery checkpoint — Exp073BM exact GSL cross-host mismatch

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Classification:** nonclassifying numerical/root-cause QA, `+0/+0`.

## Terminal result

Exp073BM run `33384490894` completed with eight valid replicas and a valid comparator.

Comparator job: `99464335152`.
Comparator artifact:

- ID `9755067300`;
- digest `sha256:a367efb34b709e6ee5aa9c0da1a6ce6c0bce2d5a0f33cd9869cbecd80f19e4d5`.

Terminal status:

`BM_Q2_GSL_EXACT_CROSSHOST_FAIL`.

All eight replicas bound identical inputs:

- compact A SHA `a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e`;
- fixed-order K SHA `cba43cfe070758476606dff90e7618b4cc6c80b1426d5d5fa07c086948374c37`.

Nevertheless the exact GSL sequence `LU_decomp -> LU_invert -> gsl_blas_dgemm` produced two W byte classes:

- `cb88ff680d6c75e3f7d4491c06e6604e7fd01bd6c6b486740999eb9e32b6899a` on A,D,E,F,G,H;
- `616a0e58e4b2c609674aac126da8ac742da3babc0e4cd251e5255f585ce0d850` on B,C.

CPU/SIMD split:

- A: AMD EPYC 9V74, X86_V3, no AVX-512 -> `cb88...`;
- B,C: Intel Xeon Platinum 8573C, X86_V4/AVX-512 -> `616a...`;
- D,F,G,H: AMD EPYC 7763, X86_V3 -> `cb88...`;
- E: AMD EPYC 9V74, X86_V3 -> `cb88...`.

Thus the two exact W classes align with the sampled SIMD class, not merely CPU model string.

## Local post-terminal difference diagnostic

Comparing immutable A-class and B-class W payloads:

- differing entries `89331 / 479232 = 0.18640449719551283`;
- maximum absolute difference `6.938893903907228e-18`;
- mean absolute difference `7.105254016931556e-22`;
- Frobenius difference `3.604075161165764e-17`;
- median differing-entry ULP distance `2`;
- 90th percentile ULP distance `21`;
- 99th percentile ULP distance `256`.

This is smaller than but qualitatively compatible with the last-bit cross-host phenomenon seen in the permanent Exp073AQ FAIL. It cannot reclassify AQ.

## Linkage audit

The actual NaMaster-2.7 conda environment shows:

- `_nmtlib` -> `libgsl.so.25` and `libcblas.so.3`;
- `libgsl.so.25` -> the same conda `libcblas.so.3`;
- the exact tagged NaMaster v2.7 bandpower-window path uses `gsl_linalg_LU_invert` followed by `gsl_blas_dgemm`.

Therefore Exp073BM directly demonstrates cross-host nondeterminism inside the same low-level GSL/CBLAS finalizer class present in the historical AQ stock route when K/A are held byte-identical.

It does not yet identify whether the divergence occurs in GSL LU/inversion or in CBLAS dgemm. Exp073BN is the exact next root-cause isolator.

## Scientific accounting

- Exp073AQ remains permanent scientific FAIL.
- Exp073BM is nonclassifying `+0/+0`.
- Exp073BJ remains the sole active heavy Track-A Wm_S1 run unless terminal state changes.
- `Verified: 52.0% | Draft/data: 53.7%`.
- Layer A/B, covariance/whitening, G7/G8/G9 remain unauthorized; no G8 jump.
