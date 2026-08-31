# Exp073BF — Article-3 Wm low-memory small-scale stock-equivalence QA v0.1

**Project:** DSIR only; RTK/RQIR excluded.  
**Classification:** independent numerical/infrastructure validation prerequisite; non-classifying for Article-3 science.  
**Scientific readiness increment:** `+0`.  
**Draft/data readiness increment:** `+0`.

## Purpose

While Exp073BA heavy Wm_S1 Track-A production is running, validate the algebra and orientation of the frozen Wm low-memory route against stock NaMaster on a deliberately small synthetic geometry. This test must not read Exp073AQ numerical outputs, Exp073BA live outputs, downstream support/covariance/nuisance/relation/G8 data, or any scientific acceptance threshold beyond the already-frozen route definition.

## Frozen test

Use NaMaster 2.7, `NSIDE=16`, `L=48`, deterministic analytic masks, fixed band edges `[0,4,8,16,24,32,48]`, spin-0 field crossed with spin-2 field.

1. Compute stock `NmtWorkspace.compute_coupling_matrix(f0,f2,b)` and extract selected `TE <- TE` bandpower windows.
2. Independently compute the mask PCL from `f0.get_mask_alms()` and `f2.get_mask_alms()`.
3. Build `G02 = pymaster.get_general_coupling_matrix(PCL,0,2,0,2)`.
4. Apply the same fixed-order band-row compression and fixed-order binned-coupling construction used by the frozen Exp073BA implementation.
5. Solve `W = solve(K,A)` and compare the selected low-memory window to stock.
6. Repeat the same-input general-coupling call twice and test exact repeatability.

## Frozen QA acceptance

PASS requires all of:

- stock and reconstructed selected windows have identical shape;
- every entry finite;
- `max_abs(stock-reconstructed) < 1e-12`;
- two same-input `G02` calls satisfy `numpy.array_equal == True`;
- no forbidden downstream reads;
- NaMaster lineage is 2.7.x.

This `1e-12` criterion is a synthetic algebra/implementation QA criterion only. It is **not** a scientific tolerance and cannot be used to rescue or reinterpret Exp073AQ/Exp073BA exact scientific comparators.

Failure is `INFRASTRUCTURE_NUMERICAL_QA_FAIL_EXP073BF_WM_STOCK_EQUIVALENCE_V0_1`, never a scientific FAIL. PASS token is `PASS_EXP073BF_WM_STOCK_EQUIVALENCE_QA_V0_1`.

## Firewall

Forbidden reads/uses: Exp073AQ window arrays as targets, Exp073BA live replica outputs, physical support mask, Layer A/B decisions, covariance, whitening, nuisance SVD, quotient/relation/null, chi-square, p-values, G8/G9. No readiness change is permitted.