# Exp073CH — hosted finalizer environment/dispatch differential v0.1

Date: 2026-09-02
Class: DIAGNOSTIC_NONCLASSIFYING_PLUS0_PLUS0

## Immutable authority preserved

Exp073CF Wm_S2 compact exact scoped PASS remains valid and limited to the compact arrays. Exp073CF finalizer exact scientific FAIL remains permanent historical authority and cannot be rescued or reclassified by this diagnostic.

Historical finalizer exact outputs:
- A W SHA256: `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`
- B W SHA256: `bed762740b625f932f016d0988be17500a2583daee08bee9a5da550de786193e`

Immutable numerical input:
- source run: `33601943300`
- compact-A artifact: `9841348367`
- artifact digest: `sha256:d6703819745b22eadc9c6557c4d89d926ed9675c09bd41cb19e79d4050ef399b`
- canonical compact `<f8 [39,12288]` SHA256: `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`

Frozen production finalizer source is imported rather than reimplemented: `ci/exp073az_article3_low_memory_general_coupling_v0_1.py`, authority path-history commit `d77b7ba88801f6788f3d386e72b445c7859c7153`.

## Motivation / prior evidence

Exp073CG run `33635554899` found exact stability across four independent `ubuntu-24.04` workers: K SHA `c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795`, W SHA equal to historical A (`fc94c71...`) on every worker. Historical Exp073CF A and B logs show the same visible Python/NumPy/SciPy/OpenBLAS/NaMaster versions/builds and runner image generation, yet B differed. Exp073CG also produced historical-A output on a worker in `westus3`, so region `westus3` alone is not sufficient to reproduce the B divergence.

The remaining prospectively testable hypothesis is hidden runtime dependence, especially CPU model/ISA and OpenBLAS kernel dispatch. Historical jobs did not capture enough CPU/kernel metadata to reconstruct B exactly.

## Frozen diagnostic contract

Hosted-only `ubuntu-24.04`. No self-hosted runner.

Pinned numerical package targets:
- Python 3.11.16
- NumPy 2.4.6
- SciPy 1.17.1
- NaMaster/pymaster 2.7
- libopenblas 0.3.34 pthreads

Each worker must fail closed on compact shape/SHA and capture before interpretation:
- `lscpu`
- `/proc/cpuinfo` vendor/model/flags
- `uname` / OS release
- `np.__config__.show()` and `np.show_runtime()`
- conda explicit package listing
- relevant BLAS/OpenMP environment
- `OPENBLAS_VERBOSE=2` stderr/stdout evidence where emitted

The exact same finalizer arithmetic is executed in fresh processes under predeclared OpenBLAS dispatch regimes. Regimes are diagnostic only:
1. `native` (no `OPENBLAS_CORETYPE` override; historical visible contract)
2. `Nehalem`
3. `Sandybridge`
4. `Haswell`

A forced regime that is unsupported or exits nonzero is recorded as `unsupported_or_failed_regime`; it is not converted into a scientific result. No fallback from a failed forced regime to native is allowed.

For every successful regime record exact K and W SHA256 and exact equality. Descriptive numerical differences may be recorded but cannot be used for rescue/tolerance classification.

## Preregistered diagnostic decision tree

All outcomes are `+0/+0`, `scientific_authority=false`, and preserve the historical Exp073CF FAIL.

1. If any successful controlled regime produces exact historical B W SHA `bed762740...`, status `EXP073CH_DIAG_HISTORICAL_B_SHA_REPRODUCED_BY_DISPATCH` and report the exact runtime/dispatch provenance.
2. Else if a single regime gives different exact K/W outputs across independent workers or fresh-process repeats, status `EXP073CH_DIAG_WITHIN_REGIME_NONDETERMINISM`.
3. Else if at least two successful regimes are internally exact but have different W SHA values, status `EXP073CH_DIAG_DISPATCH_SENSITIVE_B_NOT_REPRODUCED`.
4. Else if all successful regimes are exact and equal to historical A W SHA `fc94c71...`, status `EXP073CH_DIAG_ENVIRONMENT_DISPATCH_EXACT_STABLE_NOT_REPRODUCED`.
5. Otherwise status `EXP073CH_DIAG_OTHER_EXACT_DIFFERENTIAL`, with exact hashes only and no post-hoc scientific interpretation.

The K construction SHA is also compared. Any K divergence is reported explicitly and cannot be silently attributed to the solve.

## Forbidden interpretations/actions

- No tolerance, ULP, rounding, smoothing, averaging, majority vote, or preferred-replica rescue.
- No modification or rerun of Exp073CF.
- No readiness increment.
- No full-scale compact recomputation.
- No deterministic-successor scientific claim from this diagnostic alone.
- A future deterministic finalizer, if justified, must be a NEW prospectively versioned experiment/contract.
