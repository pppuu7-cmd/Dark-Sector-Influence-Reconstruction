# Exp073AD — Article 3 exact 5% mass-threshold factorized Layer-A synthetic QA v0.1

**Frozen:** 2026-08-30 after Exp073AC2 exposed a false binary64 rejection of an exact 5% case, and before any real DES angular authority or Layer-A support result.

This experiment validates the numerical amendment `docs/ARTICLE3_LAYERA_EXACT_5PCT_MASS_COMPARISON_AMENDMENT_2026-08-30.md` without reading real angular/radial data.

The scientific threshold remains exactly and inclusively 5%.

The evaluator must classify from dual mass inequalities:

- `D-N <= 0.05D`;
- `N >= 0.95D`.

Both true -> retained; both false -> rejected; disagreement -> numerically unresolved. The diagnostic ratio is `(D-N)/D`, not `1-N/D`.

Use `math.fsum` for finite positive term collections. The synthetic evaluator is standard-library-only so its execution does not depend on NumPy availability.

Frozen controls preserve the original Exp073AC intent and add direct boundary-stability checks:

1. all support valid -> zero invalid;
2. exact `D=20,N=19` -> diagnostic exactly 0.05 and retained by both mass forms;
3. above 5% -> both mass forms reject;
4. positive angular scaling invariance;
5. positive radial scaling invariance;
6. effective-ell counterexample rejects 6% broad high-ell leakage;
7. 4% high-ell leakage remains 4%, proving no `(2ell+1)` weighting;
8. k boundary inside a radial segment is split exactly;
9. equality at k_max boundary is inclusive;
10. ell=0 has positive k and no artificial positive k_min;
11. zero normalization rejected as numerical/reproduction failure;
12. negative radial representation rejected;
13. explicit per-ell contraction equals factorized contraction;
14. a deliberately constructed floating comparison disagreement must be labelled unresolved rather than threshold-relaxed;
15. no real-data/downstream information is read.

Required token:
`PASS_EXP073AD_FACTORIZED_LAYERA_MASS_THRESHOLD_SYNTHETIC_V0_1`

No scientific readiness credit; readiness remains **52%**.
