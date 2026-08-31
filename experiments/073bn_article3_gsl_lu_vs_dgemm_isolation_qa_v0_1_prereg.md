# Exp073BN — Article-3 GSL LU/invert versus CBLAS dgemm isolation QA v0.1

**Project:** DSIR only.  
**Classification:** nonclassifying numerical/root-cause QA.  
**Scientific readiness:** `52%`; increment `+0`.  
**Draft/data readiness increment:** `+0`.

## Motivation

Exp073BM held real DES-derived A and fixed-order K byte-identical across eight hosted replicas but the exact NaMaster-v2.7-class sequence `gsl_linalg_LU_decomp -> gsl_linalg_LU_invert -> gsl_blas_dgemm` produced two W byte classes aligned with sampled X86_V3 versus X86_V4 hosts.

Exp073BN isolates whether the first cross-host divergence appears in GSL LU/inversion or only in the CBLAS matrix multiplication.

This experiment cannot alter Exp073AQ, active Exp073BJ, or any scientific readiness.

## Frozen input and K

Use the same immutable provisional Exp073BD Wm_S2 branch-B compact A used by BM:

- run `33342265114`;
- compact A `<f8 [39,12288]` SHA `a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e`.

Construct K with the same frozen fixed-order scalar accumulation as BM. Required K byte SHA from BM is:

`cba43cfe070758476606dff90e7618b4cc6c80b1426d5d5fa07c086948374c37`.

Any mismatch in input hashes is infrastructure invalid.

## Frozen operations

For each fresh hosted replica, in a separate process for each runtime mode:

### Mode D — default runtime

1. GSL `LU_decomp(K)`;
2. GSL `LU_invert` -> emit raw row-major float64 `invK_default.bin` and SHA;
3. GSL/CBLAS `dgemm(invK,A)` -> `W_dgemm_default.bin` and SHA;
4. independently compute `W_scalar_default = invK * A` using explicit scalar C loops in fixed order: output row i ascending, RHS column c ascending, inner j=0..38 ascending, expression accumulated as `s = s + invK[i,j]*A[j,c]` -> SHA.

### Mode H — forced Haswell CBLAS dispatch

Run a fresh child process with `OPENBLAS_CORETYPE=Haswell` from process start and perform the identical four steps, emitting `invK_haswell`, `W_dgemm_haswell`, `W_scalar_haswell`.

All thread controls remain one. No FMA contraction assumptions are changed post hoc; compiled C implementation and compiler flags are prospectively frozen in the workflow.

## Eight hosted replicas

Require replicas A-H on ubuntu-24.04 with the exact BM environment creation lineage:

`conda create ... python=3.11 namaster=2.7 healpy astropy numpy`.

Record CPU model, NumPy runtime CPU feature exposure, A/K hashes and all six output hashes.

## Frozen interpretation

For each object independently:

- one SHA across eight complete hosts -> exact cross-host equal;
- more than one SHA -> exact cross-host mismatch.

Root-cause inference:

- `invK` mismatch => divergence already enters GSL LU/inversion;
- `invK` equal and scalar product equal, but default dgemm mismatch => divergence isolated to CBLAS dgemm;
- forced-Haswell dgemm equality after default mismatch => runtime CBLAS microkernel dispatch is directly implicated;
- scalar product mismatch with identical invK/A would indicate compiler/CPU scalar-operation variability and requires separate isolation.

No outcome can rescue AQ or alter BJ criteria. All outcomes `+0/+0`.

## Firewalls

No support/covariance/whitening/nuisance/relation/null/G8 information. No tolerance, ULP acceptance, rounding, averaging, majority vote or preferred replica.
