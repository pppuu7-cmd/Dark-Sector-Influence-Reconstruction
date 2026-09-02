# Exp073CG — hosted finalizer cross-host determinism diagnostic v0.1

**Preregistered:** 2026-09-02  
**Scope:** DSIR Article 3 / Wm_S2 numerical determinism diagnosis only.  
**Classification class:** diagnostic / nonclassifying / `+0/+0`.

## Motivation and immutable predecessor

Exp073CF continuation successor run `33601943300` established:

- full-scale independent A/B compact arrays are bit-for-bit identical, canonical `<f8 [39,12288]>`, SHA `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`;
- compact exact status `PASS_EXP073CF_WM_S2_COMPACT_EXACT_V0_1`;
- frozen finalizer output arrays are not bit-for-bit identical;
- terminal finalizer status `SCIENTIFIC_REPEATABILITY_FAIL_EXP073CF_WM_S2_FINALIZER_EXACT_V0_1`.

Exp073CG may diagnose the reason for that FAIL. It may **not** rescind, weaken, reinterpret, tolerance-rescue, or retroactively convert the Exp073CF classification.

Immutable diagnostic input is the Exp073CF compact-A artifact from run `33601943300`:

- artifact ID `9841348367`;
- artifact digest `sha256:d6703819745b22eadc9c6557c4d89d926ed9675c09bd41cb19e79d4050ef399b`;
- required compact A content SHA `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`;
- required shape `[39,12288]`, finite canonical float64.

The compact-B artifact is not required because Exp073CF already proved A and B content-identical before finalization.

## Frozen finalizer semantics

The production source authority remains `ci/exp073az_article3_low_memory_general_coupling_v0_1.py`, path-history scientific source commit `d77b7ba88801f6788f3d386e72b445c7859c7153`.

For Wm:

1. load `A` as float64;
2. construct `K=k_from_a(A)` with the frozen increasing-band/increasing-ell accumulation order;
3. compute `W=np.linalg.solve(K,A)`;
4. canonicalize output to contiguous little-endian float64.

Exp073CG must reproduce those semantics exactly. It must not replace the solver, reorder arithmetic, symmetrize, regularize, round, quantize, average, or apply tolerances.

## Hosted worker design

Run four independent `ubuntu-24.04` GitHub-hosted workers `R1..R4`. No self-hosted runner is permitted.

Each worker must:

- download the exact immutable Exp073CF compact artifact;
- fail closed on compact shape, finiteness and canonical content SHA;
- use Python 3.11 / NaMaster 2.7 and an explicitly recorded NumPy/OpenBLAS-family environment;
- set `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`, `BLIS_NUM_THREADS=1`, `OMP_DYNAMIC=FALSE` for the diagnostic solve;
- record CPU model and architecture, `lscpu`, NumPy version/configuration/runtime, BLAS/LAPACK/OpenBLAS information and relevant environment variables;
- construct canonical `K` and record its exact SHA;
- execute the same `np.linalg.solve(K,A)` at least three times in the same Python process and compare exact content SHA / `np.array_equal`;
- execute at least three additional solves in fresh child Python processes on the same hosted worker and compare exact content SHA;
- save one canonical final window for cross-worker exact comparison.

All hashes are SHA-256 over canonical contiguous little-endian array bytes.

## Preregistered diagnostic decision tree

The aggregate job compares all worker records and arrays exactly.

1. **If K SHA differs across workers:** classify diagnostic result `EXP073CG_DIAG_K_CONSTRUCTION_NONDETERMINISM`.
2. **If any same-process or same-worker fresh-process solve differs exactly:** classify `EXP073CG_DIAG_WITHIN_WORKER_SOLVE_NONDETERMINISM`.
3. **If K is exact across workers and each worker is internally exact-stable, but final W differs across workers:** classify `EXP073CG_DIAG_CROSS_HOST_SOLVE_NONDETERMINISM_REPRODUCED`.
4. **If K and W are exact across all workers/repeats:** classify `EXP073CG_DIAG_CROSS_HOST_EXACT_STABLE_NOT_REPRODUCED` and investigate environment drift between Exp073CF and Exp073CG rather than declaring the issue solved.

If multiple failure modes occur, report all observed predicates and use the earliest applicable branch above as the headline diagnostic token.

## Descriptive metrics

When two W arrays differ, the aggregate may report max/mean/median absolute difference, relative difference and ULP distribution **only as descriptive diagnostics**. No such metric is an acceptance threshold and none can rescue Exp073CF.

## Scientific/accounting consequences

Every Exp073CG outcome is `+0/+0`. Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**.

A successful isolation of a cross-host numerical cause permits only a later **prospectively versioned deterministic-finalizer experiment**. That later version must be preregistered before execution and cannot rewrite Exp073CF history.

No G7 authorization and no G8 transition are permitted from Exp073CG alone.
