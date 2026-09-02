# Exp073CG hosted finalizer determinism diagnostic — terminal exact-stable, prior FAIL not reproduced

**Date:** 2026-09-02  
**Scope:** DSIR Article 3 / Wm_S2 finalizer diagnostic only.  
**Run:** `33635554899`  
**Head SHA:** `6b6f85ee611c8fd0b8cde455ab349dd9fcd38b0c`  
**Classification:** `EXP073CG_DIAG_CROSS_HOST_EXACT_STABLE_NOT_REPRODUCED`  
**Scientific authority:** `false` (diagnostic/nonclassifying)  
**Readiness delta:** `+0/+0`

Exp073CG was launched only after the frozen Exp073CF terminal result. It used one immutable hash-bound compact Wm_S2 input and four independent GitHub-hosted Ubuntu 24.04 workers (R1–R4), with one-thread numerical runtime controls and repeated same-process plus fresh-process finalizer executions. No self-hosted/home runner was used.

## Terminal exact result

All four workers completed successfully. Aggregate comparator job `100265859912` found:

- `k_cross_exact=true`;
- identical K SHA on R1/R2/R3/R4: `c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795`;
- `within_worker_exact=true`;
- `w_cross_exact=true`;
- exact W SHA on R1/R2/R3/R4: `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`;
- pairwise differing count against R1: `0 / 479232` for R2, R3, R4;
- `max_abs=0.0`, `max_rel=0.0` for all cross-worker comparisons;
- `no_tolerance_used=true`.

Aggregate authority artifact: `9848673390`, digest `sha256:5470b57030b42c6e9da71f3a056e84ddca783d55ca90e61a36ded4ce7a87a641`.

The exact W SHA equals the historical Exp073CF finalizer-A SHA, while the Exp073CF finalizer-B SHA remains different. Therefore the previously observed A/B finalizer mismatch was **not reproduced** under this pinned hosted diagnostic environment. This narrows the likely locus to environment/runtime differences or another factor specific to the original independent finalizer executions, but does not prove a unique cause.

## Scientific consequence

Exp073CF remains permanently classified:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073CF_WM_S2_FINALIZER_EXACT_V0_1`

Exp073CG cannot retroactively rescue or reclassify that result. The diagnostic only establishes that, for the immutable compact input under the prospectively pinned Exp073CG environment, K construction and `np.linalg.solve` are exactly stable within and across four hosted workers.

Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**. No G7 authorization and no G8 jump.

## Next permitted research step

Do not rerun full-scale compact A/B: exact compact repeatability is already established.

The next useful step is a prospectively preregistered **environment-differential finalizer audit** comparing the exact original Exp073CF finalizer environments (package versions, BLAS/LAPACK vendor/kernel dispatch, CPU family/region/runtime metadata) against the pinned Exp073CG environment. If the original B environment can be reconstructed sufficiently, reproduce only the cheap finalizer on the immutable compact input. Any successor deterministic finalizer must be a new version with a prospective contract; it may establish new-version repeatability but may not rewrite Exp073CF.

### Status

- ✅ Full-scale Wm_S2 compact A/B exact PASS preserved.
- ❌ Exp073CF frozen finalizer exact repeatability FAIL preserved.
- ✅ Exp073CG four-host diagnostic: K exact and W exact across R1–R4.
- 🟡 Original Exp073CF B-only divergence source remains unresolved.
- ❌ No G7/G8 authorization.

**Verified 52.0% | Draft/data 53.7% | readiness delta +0/+0.**
