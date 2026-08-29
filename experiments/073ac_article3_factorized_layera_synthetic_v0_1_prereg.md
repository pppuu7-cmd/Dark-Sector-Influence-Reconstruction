# Exp073AC — Article 3 factorized Layer-A evaluator synthetic QA v0.1

**Frozen:** 2026-08-30 before the complete DES angular authority and before any real Layer-A support fraction.

Purpose: test the numerical semantics frozen in `docs/ARTICLE3_LAYERA_FACTORIZED_DES_SUPPORT_EVALUATOR_2026-08-30.md` without reading any real Exp073X/AA angular window or scoring a science gate.

The synthetic evaluator must use:

- discrete integer-ell sum of `abs(W_ell)` with no extra ell measure;
- piecewise-linear radial functions/integrals;
- monotone piecewise-linear inverse chi;
- exact split at z and k boundaries;
- `f_invalid = 1-valid/total`;
- inclusive `f_invalid<=0.05`.

Frozen controls:

1. all support inside domain gives zero invalid fraction;
2. exact `f_invalid=0.05` passes;
3. value above `0.05` fails;
4. positive angular rescaling leaves result unchanged;
5. positive radial rescaling leaves result unchanged;
6. a broad-window case with >5% invalid high-ell support rejects even though its weighted-mean/effective ell would lie inside;
7. a case with 4% invalid high-ell support remains 4%; inserting `(2ell+1)` would change the answer and is therefore explicitly not the frozen operator;
8. k boundary falling inside a coarse radial line segment is integrated at the exact split, not nearest node;
9. k equality at the lower valid-z boundary is inclusive;
10. ell=0 still has positive `k=(ell+0.5)/chi` and no artificial positive k_min is applied;
11. zero angular/radial normalization is invalid-for-science, not a scientific support FAIL;
12. negative radial support input is rejected as a representation failure;
13. direct explicit summation over ell of exact radial valid integrals equals the factorized evaluator result;
14. no covariance, nuisance, relation/null or G8 information is present.

Required token:
`PASS_EXP073AC_FACTORIZED_LAYERA_SYNTHETIC_V0_1`

This test is architecture/numerical QA only. `science_gate_scored=false`, `scientific_readiness_credit=false`, readiness remains **52%**, G7/G8/G9 OPEN.
