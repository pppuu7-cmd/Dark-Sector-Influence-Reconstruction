# Exp073BM — Article-3 exact-GSL stock-finalizer cross-host QA v0.1

**Project:** DSIR only.  
**Classification:** nonclassifying numerical/root-cause QA.  
**Scientific readiness:** `52%`; increment `+0`.  
**Draft/data readiness increment:** `+0`.

## Purpose

Isolate the exact low-level linear-algebra class used by NaMaster v2.7 `nmt_compute_bandpower_windows`: GSL LU decomposition/inversion followed by `gsl_blas_dgemm`.

Test whether this GSL sequence is byte-reproducible across fresh hosted CPU environments when the input `K` and `A` are exactly identical.

This experiment cannot alter or rescue Exp073AQ, cannot authorize Wm_S2, and cannot modify active Exp073BJ.

## Frozen source basis

Exact public NaMaster tag `v2.7`, `src/nmt_master.c`, contains:

- `gsl_linalg_LU_decomp` for the binned MCM;
- `gsl_linalg_LU_invert` in `nmt_compute_bandpower_windows`;
- `gsl_blas_dgemm` to form bandpower windows from inverse binned MCM and binned-by-unbinned MCM.

Exp073BM reproduces this linear-algebra sequence only. It does not claim to reproduce the full stock unbinned-MCM construction.

## Frozen input

Use immutable provisional Exp073BD Wm_S2 branch-B compact artifact from run `33342265114`, artifact `9746250767`.

Required `A`:

- `<f8 [39,12288]`;
- SHA256 `a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e`.

Construct `K=AQ` using frozen Article-3 edges and ascending-ell fixed-order scalar accumulation before invoking GSL. Write canonical raw little-endian float64 `K` and `A` inputs and bind their SHA256 values in every replica receipt.

## Frozen GSL computation

Compile a small C program against the exact GSL libraries installed inside a fresh conda environment created with:

`python=3.11 namaster=2.7 healpy astropy numpy`

C sequence:

1. read exact 39x39 K and 39x12288 A;
2. copy K into a mutable GSL matrix;
3. `gsl_linalg_LU_decomp`;
4. `gsl_linalg_LU_invert`;
5. `gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,1,invK,A,0,W)`;
6. write raw row-major float64 W.

No tolerance, rounding or rescue.

## Hosted replication

Use eight independent ubuntu-24.04 replicas A-H to increase the chance of heterogeneous CPU/SIMD exposure. Record:

- CPU model and lscpu flags;
- NumPy runtime SIMD feature set;
- exact package versions;
- `ldd` for `libgsl.so`, `libgslcblas.so` if present, and PyMaster extension;
- GSL and GSL-CBLAS library hashes where available;
- A, K and W canonical hashes.

## Frozen result classes

- eight complete identical W arrays and one SHA -> `BM_Q1_GSL_EXACT_CROSSHOST_PASS`;
- any complete exact mismatch -> `BM_Q2_GSL_EXACT_CROSSHOST_FAIL`;
- fewer than eight valid outputs -> `BM_Q3_INFRASTRUCTURE_INCOMPLETE`.

All outcomes are nonclassifying `+0/+0`.

## Interpretation discipline

`BM_Q1` would show that the GSL LU/invert/dgemm stage is deterministic across the sampled hosts for identical K/A, shifting the likely AQ-specific source upstream toward differences already present in the unbinned/binned MCM inputs. It would not prove upstream causation universally.

`BM_Q2` would directly demonstrate cross-host nondeterminism inside the GSL finalizer class itself.

Neither outcome changes Exp073AQ or Exp073BJ.
