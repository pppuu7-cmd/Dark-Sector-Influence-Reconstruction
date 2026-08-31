# Exp073BL — Article-3 fixed-operation LU cross-host finalizer QA v0.1

**Project:** DSIR only.  
**Classification:** nonclassifying numerical/infrastructure QA.  
**Scientific readiness:** `52%`; increment `+0`.  
**Draft/data readiness increment:** `+0`.

## Purpose

Test whether the frozen low-memory finalizer equation `K W = A`, with `K=AQ`, can be solved reproducibly across independent hosted CPU environments using a fixed-operation partial-pivot LU implementation that does not call BLAS/LAPACK solve routines.

This experiment may not alter or rescue Exp073AQ and may not modify active Exp073BJ.

## Frozen input

Use only the immutable real DES-derived provisional Exp073BD Wm_S2 branch-B compact artifact from run `33342265114`, artifact `9746250767` / name `exp073bd-wm-s2-B-70745b9eee87e3c196c4bb435a6770cf986ffe6b`.

Required compact payload:

- key `A`;
- canonical dtype/shape `<f8 [39,12288]`;
- canonical byte SHA256 `a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e`.

The payload remains Track-P and cannot be promoted by this QA.

## Frozen K construction

Construct `K=AQ` using the exact frozen Article-3 edges and the same ascending-ell scalar accumulation order used by the low-memory implementation. No BLAS reduction may be used to form K.

## Frozen LU algorithm

Use float64 only.

For pivot column `k=0..37`:

1. select pivot row as the first row at or below k having maximal `abs(LU[row,k])` using a deterministic Python scalar scan;
2. fail if the chosen pivot is exactly zero or nonfinite;
3. swap complete rows k and pivot in LU and the integer permutation vector;
4. for each row `i=k+1..38`, compute scalar `factor = LU[i,k]/LU[k,k]`, store it at `LU[i,k]`, then update each U entry in ascending column order `j=k+1..38` as the scalar float64 operation `LU[i,j] = LU[i,j] - factor*LU[k,j]`.

Solve for all 12288 RHS columns with the same fixed scalar operation order:

- apply the frozen permutation to A;
- forward substitution rows ascending, inner summation index ascending;
- backward substitution rows descending, inner summation index ascending;
- divide once by the diagonal pivot.

The classifying comparison is only exact byte equality across fresh replicas. Structural residuals are descriptive QA and cannot rescue a mismatch.

## Hosted replication

Require four independent ubuntu-24.04 replicas. Pin Python 3.11 and NumPy 2.4.6. Set all known thread controls to one and record CPU model, lscpu, NumPy runtime configuration and runtime SIMD feature exposure.

Each replica emits canonical `<f8 [39,12288]` W, SHA256, pivot permutation, `max(abs(WQ-I))`, and a deterministic scalar fixed-order `KW-A` residual summary on a frozen subset of columns `[0,29,30,272,309,967,3035,6508,10821,12287]` so that residual QA itself does not require BLAS.

## Frozen result classes

- all four complete W arrays exact and SHA-identical -> `BL_Q1_FIXED_LU_EXACT_CROSSHOST_PASS`;
- any complete exact mismatch -> `BL_Q2_FIXED_LU_EXACT_CROSSHOST_FAIL`;
- incomplete before four valid outputs -> `BL_Q3_INFRASTRUCTURE_INCOMPLETE`.

All classes give `+0/+0` and are nonclassifying for science.

## Firewalls

No tolerance/ULP/rounding/averaging/majority/preferred-replica rule. No support, covariance, whitening, nuisance, relation/null or G8 information. Exp073AQ remains permanent FAIL. Exp073BJ criteria remain unchanged.
