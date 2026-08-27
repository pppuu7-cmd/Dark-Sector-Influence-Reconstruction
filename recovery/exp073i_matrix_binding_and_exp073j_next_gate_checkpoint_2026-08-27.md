# Recovery checkpoint — Exp073I finite-matrix PASS / Exp073J next gate — 2026-08-27

## Immutable state

Exp073H completed as `FAIL_FOURIER_MM_OPERATOR_SOURCE_BINDING_EXP073H`: H1/H2/H4-H8 PASS, H3 FAIL. Run `33039103109`, job `98408423778`, artifact `9633155256`. This is a source/operator scientific FAIL, not infrastructure and not a 5%-support rejection.

Exp073I then completed as `PASS_FINITE_TRUE_K_WINDOW_MATRIX_SOURCE_BINDING_EXP073I`: run `33039228551`, job `98408810891`, artifact `9633204048`, digest `sha256:de203dc675ecac48ee2dfa42b79302459810b8bc5fc03eac6c112f1f79b61248`.

Publication source: Beutler & McDonald (2021), arXiv:2106.06324 / JCAP 11 (2021) 031. Tooling semantics pinned to `fbeutler/pk_tools@707eb2a6a4691c34eae19d7f72047ca4892f528e`.

For BOSS DR12 z3 NGC and SGC, `W` is exactly `200 x 2000`; `M` is `2000 x 1200`. The page fixes `0<k<0.4 h/Mpc`, `Delta k_th=0.001 h/Mpc`, `Delta k_o=0.01 h/Mpc`. Finite `abs(W)` row sums are positive and finite, so operator-only positive support domination is mathematically available without fiducial P(k), covariance or a post-hoc cutoff.

## Frozen invariants

- physical rectangle: `z=[0.295,2.33]`, `k=[0.000704833374744468,0.06664762008318016] Mpc^-1`;
- maximum positive invalid fraction: `0.05`;
- minimum nominal retained dimension: `15`;
- signed Wm semantics preserved;
- no covariance numerical values, nuisance rank/SVD, relation/null or G8 outputs have been read.

## Next exact action

Use only `experiments/073j_kids_bnt_boss_finite_matrix_common_support_prereg_v0_1.md`. Reproduce the already-bound KiDS-BNT Wm/WW operators and Exp073I BOSS z3 finite matrices. Enumerate candidates before classification, build positive operator-only support weights, convert k to physical Mpc^-1, compute per-block invalid fractions against the unchanged rectangle, and classify Exp073J under the frozen 5% / retained-dimension >=15 rule.

Only an Exp073J PASS may authorize a separately frozen covariance restriction/whitening step. Do not run nuisance SVD, relation/null or G8 first.

G7 OPEN. G8 OPEN. G9 OPEN.
