# DSIR recovery checkpoint — streaming band-projection equivalence audit while Exp073BJ computes

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Classification:** independent nonclassifying code-equivalence audit, `+0/+0`.

## Exp073BJ hosted state

Run `33379013167` remains active. Compact jobs A `99446854065` and B `99446854363` both remain after successful prospective freeze, exact NaMaster 2.7 setup, exact BI_Q1 authority binding, and exact Exp073AZ canonical PCL binding. Both are inside `Compute two-thread compact Wm_S1 replica`.

No duplicate heavy BJ run was started. No BJ compact artifact/comparator classification existed at this audit snapshot.

## New nonclassifying result

Frozen reference implementation commit `d77b7ba88801f6788f3d386e72b445c7859c7153` forms dense `G` and then performs a strictly increasing-ell left-to-right binary64 band accumulation in `compress_general`.

New audit:

`docs/ARTICLE3_STREAMING_BAND_PROJECTION_EQUIVALENCE_CONTRACT_2026-08-31.md`

commit `99ea22f8e1221cef1da49397d4e43789f467477c`.

It defines the exact prospective equivalence target for a future true row-streaming/native accumulator: per-row bitwise equality to dense `G`, identical increasing-ell accumulation order, no reassociation/tree/FMA/parallel reduction change, identical binary64 final division, exact compact `numpy.array_equal` against the frozen dense-reference path, and independent-process exact repeatability.

Algebraic `A=BG` equality alone is explicitly insufficient because floating-point reduction order matters.

If exact rows can genuinely be generated without allocating full `G`, retained storage can fall from `O(L^2)` to `O(39L+L)`; this does not prove runtime improvement and does not establish that NaMaster 2.7 internals expose such a row generator.

## Frozen boundaries preserved

- Active Exp073BJ workflow/code/classification unchanged.
- Complete exact compact mismatch remains the frozen scientific repeatability FAIL.
- Cancellation/timeout/incomplete before two valid comparator inputs remains infrastructure incomplete, no scientific classification.
- No tolerance/ULP/rounding/averaging/majority/preferred-replica rescue.
- Exp073AQ remains permanent historical exact-repeatability FAIL.
- Synthetic/infrastructure/provenance/code-equivalence/numerical QA gives `+0/+0`.
- Required G7 order and G8 firewall unchanged.

## Accounting

`Verified: 52.0% | Draft/data: 53.7%`.

## Exact next gate

Re-inspect Exp073BJ run `33379013167`. When both compact jobs become terminal, preserve the frozen exact compact comparator classification first. Only exact compact PASS may admit both finalizers and final exact authority. After classification, run the nonclassifying Wm_S1 structure diagnostic on any valid compact/final payload.
