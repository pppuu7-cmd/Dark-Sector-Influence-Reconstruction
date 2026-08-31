# Exp073BF -> Exp073BA implementation-coverage audit

**Date:** 2026-08-31  
**Scope:** DSIR Article-3 only; RTK/RQIR excluded.  
**Classification:** static implementation/provenance audit; non-scientific.  
**Scientific readiness increment:** `+0`.  
**Draft/data readiness increment:** `+0`.

## Question

What does the terminal hosted Exp073BF PASS actually validate about the still-running Exp073BA production route, and what remains unvalidated until BA hosted authority exists?

## Audited frozen objects

- Exp073BA production workflow: `.github/workflows/exp073ba-article3-low-memory-wm-s1-production-v0-1.yml`.
- Frozen production implementation: `ci/exp073az_article3_low_memory_general_coupling_v0_1.py`, enforced by BA at historical freeze commit `d77b7ba88801f6788f3d386e72b445c7859c7153`.
- Exp073BF preregistration commit: `99db0c8b7444ade7eb65df7626398a034bf16fda`.
- Exp073BF workflow commit: `bbb4ecb14c01d2d7bafe37f0ae01377b2d81223b`.
- Exp073BF hosted run: `33349183295`, terminal `PASS_EXP073BF_WM_STOCK_EQUIVALENCE_QA_V0_1`.

## Positive coverage

Static line-by-line algorithm comparison confirms that Exp073BF independently reimplemented the same Wm spin-0 x spin-2 low-memory algebra used by BA:

1. `pymaster.get_general_coupling_matrix(pcl,0,2,0,2)` for the Wm `TE <- TE` route;
2. fixed ascending band iteration;
3. fixed ascending ell summation into each compressed row;
4. division by exact integer band width during row compression;
5. construction of the binned coupling matrix by fixed ascending ell summation of `A[:,ell]`;
6. `numpy.linalg.solve(K,A)` for the selected Wm bandpower window;
7. NaMaster 2.7 lineage;
8. single-thread BLAS/OMP environment in hosted workflows.

Exp073BF therefore supplies an independent hosted check of Wm orientation and low-memory algebra against stock `NmtWorkspace` on a small synthetic geometry. Its frozen QA result (`max_abs(stock-reconstructed)=8.326672684688674e-16 < 1e-12`, same-input general coupling exact repeatability true) is consistent with the production algebra.

## Explicit non-coverage

Exp073BF does **not** validate or classify any of the following:

- full `NSIDE=4096`, `L=12288`, 39-band resource behavior;
- DES Y1 / R1 physical input maps;
- Exp073AZ immutable PCL provenance binding (that is separately covered by Exp073BE/BC);
- full-size general-coupling exact A/B repeatability across independent hosted runners;
- BA compact artifact serialization/deserialization exactness;
- BA compact exact comparator;
- BA finalizer exact A/B repeatability;
- physical support validity, Layer A, Layer B, covariance, whitening, nuisance SVD, quotient/relation/null, G7, G8, or G9.

In particular, the synthetic `1e-12` BF threshold is never transferable to BA. BA remains governed by frozen exact equality only; tolerance, rounding, ULP rescue, preferred replica selection and majority vote remain forbidden.

## Audit classification

`PASS_EXP073BF_TO_EXP073BA_IMPLEMENTATION_COVERAGE_AUDIT_2026_08_31`

This token means only that BF exercised an algorithmically matching independent small-scale Wm route and that its limits are explicitly recorded. It is not scientific authority and cannot modify Exp073AQ, which remains a permanent exact-repeatability FAIL under its historical implementation class.

## Operating consequence

No new heavy run is authorized by this audit. While Exp073BA run `33345968620` and Exp073BD run `33342265114` remain active, the correct control-plane action is to wait for their immutable hosted artifacts while performing only independent prerequisite/audit work. The next authority-changing gate remains Exp073BA terminal exact comparator/finalizer authority.