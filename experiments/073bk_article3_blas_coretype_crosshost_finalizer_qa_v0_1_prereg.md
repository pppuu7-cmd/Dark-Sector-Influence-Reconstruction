# Exp073BK — Article-3 BLAS coretype cross-host finalizer QA v0.1

**Project:** DSIR only.  
**Classification:** nonclassifying numerical/infrastructure QA.  
**Scientific readiness:** `52%`; increment `+0`.  
**Draft/data readiness increment:** `+0`.

## Purpose

Test the local diagnostic observation that `numpy.linalg.solve(K,A)` can change float64 bits solely because OpenBLAS selects a different CPU microkernel, even when compact `A`, thread count, Python/NumPy lineage and mathematics are otherwise identical.

This experiment may not alter or rescue Exp073AQ, may not modify active Exp073BJ, and may not create Wm authority.

## Frozen input

Use only the immutable real DES-derived **provisional** Exp073BD Wm_S2 branch-B compact artifact from run `33342265114`, artifact name `exp073bd-wm-s2-B-70745b9eee87e3c196c4bb435a6770cf986ffe6b`.

Expected compact payload:

- key `A`;
- shape `<f8 [39,12288]`;
- canonical byte SHA256 `a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e`.

The payload remains Track-P and cannot be promoted to Track-A by this QA.

## Frozen computation

Reconstruct `K=AQ` with the same frozen Article-3 edges and the same ascending-ell fixed-order scalar accumulation used by the low-memory finalizer.

For each fresh hosted replica, launch separate child processes for four execution policies:

1. `default_t1`: normal OpenBLAS CPU dispatch, one thread;
2. `haswell_t1`: `OPENBLAS_CORETYPE=Haswell`, one thread;
3. `default_t2`: normal OpenBLAS CPU dispatch, two threads;
4. `haswell_t2`: `OPENBLAS_CORETYPE=Haswell`, two threads.

Each child computes exactly `W=np.linalg.solve(K,A)` and emits canonical `<f8 [39,12288]` SHA256 plus structural `max(abs(WQ-I))`. No rounding/tolerance modifies any array.

Four independent hosted replicas are required. Record CPU model, NumPy configuration and all four SHAs.

## Frozen QA interpretation

For each policy, exact cross-host reproducibility is descriptive only:

- `array_equal == True` across all complete replicas and one canonical SHA => `EXACT_CROSSHOST_EQUAL`;
- any complete mismatch => `EXACT_CROSSHOST_MISMATCH`;
- incomplete jobs => `INFRASTRUCTURE_INCOMPLETE`.

A particularly informative outcome is default-policy mismatch together with forced-Haswell equality across different CPU models. This would support, but not prove universally, CPU-dispatch causation for finalizer bit drift.

No outcome changes Article-3 scientific readiness, Exp073AQ classification, or Exp073BJ criteria.

## Firewalls

No support, covariance, whitening, nuisance, relation/null, G8 or physical-model information may be read. No tolerance, ULP acceptance, averaging, majority vote or preferred-replica rule exists.
