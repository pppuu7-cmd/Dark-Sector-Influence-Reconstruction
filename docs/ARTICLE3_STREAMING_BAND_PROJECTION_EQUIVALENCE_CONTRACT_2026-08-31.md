# Article-3 nonclassifying audit — streaming band-projection equivalence contract

**Date:** 2026-08-31  
**Scope:** DSIR Article-3 Wm/WW general-coupling execution engineering only.  
**Classification:** nonclassifying numerical/code-equivalence audit, `+0 Verified / +0 Draft-data`.

## Motivation

The frozen low-memory implementation at commit `d77b7ba88801f6788f3d386e72b445c7859c7153` computes a dense general-coupling matrix `G` and then compresses it with `compress_general`. For `L=12288`, one scalar dense `<f8 [12288,12288]` object is exactly 1.125 GiB, while the retained compact `<f8 [39,12288]` object is only about 3.66 MiB. The prior public-API audit established that post-return Python chunking cannot avoid dense materialization.

This note freezes the *equivalence target* that any future source-level streaming/native accumulator would have to satisfy. It does not authorize changing Exp073BJ or any frozen scientific criterion.

## Existing exact operation

For band `b` with frozen integer edges `[lo_b, hi_b)`, the current code is literally

`acc = zeros(L)`

`for ell in range(lo_b, hi_b): acc += G[ell]`

`A[b] = acc / float(hi_b-lo_b)`.

Thus, componentwise,

`A[b,j] = (((0 + G[lo_b,j]) + G[lo_b+1,j]) + ... + G[hi_b-1,j]) / n_b`,

with Python/NumPy left-to-right row order fixed by increasing `ell`.

## Streaming equivalence contract

A future row-streaming/native implementation can be considered a candidate exact replacement only if all of the following are demonstrated prospectively on the pinned NaMaster lineage:

1. For every `ell`, the emitted row is bitwise identical to the corresponding dense `G[ell,:]` row produced by the frozen reference path for identical PCL/spins.
2. Rows are accumulated in the same strictly increasing `ell` order within every frozen band.
3. The accumulator dtype is binary64 and no reassociation, tree reduction, fused alternative, extended-precision retention, or parallel reduction changes the operation order.
4. The final division by `float(hi-lo)` is performed at the same point and dtype as the frozen Python reference.
5. The resulting complete compact array satisfies exact `numpy.array_equal` against the frozen dense-reference compact array in independent processes. No tolerance/ULP/rounding criterion is admissible for Track-A equivalence.
6. Independent-process repeatability of the streaming candidate itself must also be exact before any classifying successor may use it.

The algebraic identity `A = B G`, where `B` is the fixed 39-row boxcar averaging operator, is not by itself sufficient for bitwise equivalence because floating-point summation is non-associative.

## Memory consequence if row generation is genuinely streamable

If the native general-coupling implementation can emit one exact row at a time without first allocating the full dense `G`, retained Python-side storage falls from `O(L^2)` to `O(39 L + L)`: the compact `A` plus one row/accumulator. At `L=12288`, this is only a few MiB rather than 1.125 GiB for `G` alone.

This is a storage upper-bound argument only. It does **not** prove runtime improvement: if row generation repeats expensive global work, evaluates all matrix elements with the same total cost, or cannot reuse required Wigner/kernel state efficiently, wall time may remain comparable or worsen.

## Scientific boundary

This audit does not change Exp073BJ run `33379013167`, its exact comparator, finalizers, or classification. A complete BJ mismatch remains the prospectively frozen scientific repeatability FAIL; incomplete execution before two valid comparator inputs remains infrastructure incomplete with no scientific classification. Exp073AQ remains permanent historical FAIL.

Any future source-level streaming implementation must be preregistered as a new execution successor and pass exact code-equivalence/repeatability qualification before classifying use. Synthetic/code-equivalence QA remains `+0/+0`.

## Current conclusion

The mathematically correct future optimization target is not merely "chunk the dense matrix" but **generate each reference-equivalent general-coupling row and immediately fold it into the frozen left-to-right band accumulator before the next row**, while preserving exact per-row values and accumulation order. Whether NaMaster 2.7 internals expose a practical row generator remains an unresolved source-level implementation question.
