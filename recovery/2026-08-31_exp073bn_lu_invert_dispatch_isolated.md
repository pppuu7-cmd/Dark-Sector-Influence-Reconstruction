# DSIR recovery checkpoint — Exp073BN isolates cross-host divergence in GSL LU/inversion

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Classification:** nonclassifying numerical/root-cause QA, `+0/+0`.

## Terminal result

Exp073BN run `33384893419` completed successfully with eight valid replicas and comparator job `99465710967`.

Comparator artifact:

- ID `9755237055`;
- digest `sha256:978ae7f3d0dda3f09ead558a92f61b5dc0455064f57a2790dced5faf5a3d7642`.

Prospective diagnosis:

`BN_D1_DIVERGENCE_ENTERS_GSL_LU_OR_INVERT`.

All eight replicas used byte-identical A and K inherited from Exp073BM diagnostics.

## Exact stage results

### Default runtime

`invK_default.bin` is **not** cross-host exact. Two SHA classes:

- X86_V3-class hosts: `bef9f57bc94f1b86002d079653b974a5222cb7df571947c339f35d5a35594e36`;
- sampled X86_V4/AVX-512 hosts: `45cfeb0a6ee1bd61ac72ad2151a89ca82624b8ab375a54b4fc06e9ee61af5a8e`.

Therefore divergence exists before the final matrix multiplication.

`W_scalar_default.bin`, computed with an explicit scalar fixed-order C multiplication from the already-divergent invK, also has two classes:

- `6e14a1a3b9d59e6b4981dab3d5a08bece693d5151c9fc50f884b6f3a45dace96`;
- `f45d3f6c13bcb77e50eae3ff192bcbb28b6a0ec1ef9307139825fc3b42b2ac57`.

`W_dgemm_default.bin` reproduces the two Exp073BM classes:

- `cb88ff680d6c75e3f7d4491c06e6604e7fd01bd6c6b486740999eb9e32b6899a`;
- `616a0e58e4b2c609674aac126da8ac742da3babc0e4cd251e5255f585ce0d850`.

### Forced Haswell runtime

With `OPENBLAS_CORETYPE=Haswell` set from child-process start, all eight hosts become exact for every isolated stage:

- `invK_haswell.bin` one SHA: `bef9f57bc94f1b86002d079653b974a5222cb7df571947c339f35d5a35594e36`;
- `W_scalar_haswell.bin` one SHA: `6e14a1a3b9d59e6b4981dab3d5a08bece693d5151c9fc50f884b6f3a45dace96`;
- `W_dgemm_haswell.bin` one SHA: `cb88ff680d6c75e3f7d4491c06e6604e7fd01bd6c6b486740999eb9e32b6899a`.

Thus pinning the lower microkernel removes the sampled cross-host divergence not only in dgemm but already in the GSL inversion output.

## CPU/SIMD sample

The eight hosts included multiple families. X86_V4/AVX-512 exposure appeared on sampled Intel hosts and mapped to the alternate default invK SHA. X86_V3-only hosts mapped to the Haswell-class SHA. CPU model string alone remains insufficient numerical provenance.

## Interpretation

Exp073BN directly isolates the first observed cross-host divergence to `gsl_linalg_LU_decomp/LU_invert` or lower-level operations invoked by that path, before the final `gsl_blas_dgemm`.

Because exact NaMaster v2.7 stock bandpower windows use GSL LU/inversion followed by dgemm, this is strong causal-class evidence for the kind of last-bit nondeterminism seen in the permanent Exp073AQ FAIL. It is still not a retroactive proof that all AQ mismatch arose only here because AQ intermediate MCM/inverse artifacts were not archived.

The forced-Haswell result and Exp073BL fixed-operation LU PASS independently show two viable prospective reproducibility controls:

1. pin the numerical microkernel/runtime lineage;
2. remove runtime-dispatched solve/inversion entirely with a fixed-operation finalizer.

Neither may be applied retroactively to AQ or active BJ.

## Scientific accounting

- Exp073AQ remains permanent scientific FAIL.
- Exp073BN is nonclassifying `+0/+0`.
- `Verified: 52.0% | Draft/data: 53.7%`.
- Layer A/B, covariance/whitening, G7/G8/G9 remain unauthorized; no G8 jump.

## Exact next root-cause / architecture work

1. Preserve active Exp073BJ unchanged and do not duplicate it while running.
2. Build a prospectively frozen small-scale exact row-wise general-coupling QA against NaMaster v2.7 stock `get_general_coupling_matrix`.
3. Only after exact row-generator equivalence may a checkpointable/full-scale streaming successor be considered.
