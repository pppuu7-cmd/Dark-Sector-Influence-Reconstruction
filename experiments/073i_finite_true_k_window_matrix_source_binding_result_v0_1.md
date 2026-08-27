# Exp073I — finite true-k clustering-window matrix source binding — result v0.1

**Date:** 2026-08-27  
**Classification:** `PASS_FINITE_TRUE_K_WINDOW_MATRIX_SOURCE_BINDING_EXP073I`

The publication-linked Beutler & McDonald (2021) BOSS DR12 z3 products satisfy frozen I1-I8. The workflow completed successfully: run `33039228551`, job `98408810891`, artifact `9633204048`, digest `sha256:de203dc675ecac48ee2dfa42b79302459810b8bc5fc03eac6c112f1f79b61248`.

For both NGC and SGC z3, the released survey window is an explicit finite `200 x 2000` matrix and the wide-angle matrix is `2000 x 1200`. The publication defines a finite theory grid `0<k<0.4 h/Mpc` with `Delta k_th=0.001 h/Mpc` and observed grid `Delta k_o=0.01 h/Mpc`. Every absolute window-row sum is finite and positive, so a later non-negative support envelope can be defined without a fiducial `P(k)`, covariance weighting or post-hoc k cutoff.

Pinned semantics source: `fbeutler/pk_tools@707eb2a6a4691c34eae19d7f72047ca4892f528e`.

This PASS is only an operator/source-binding PASS. No common KiDS-BNT+BOSS support fraction was computed, and no covariance, nuisance SVD, relation/null or G8 information was read. The unchanged physical rectangle and 5% threshold must be tested prospectively next.

G7 OPEN. G8 OPEN. G9 OPEN.
