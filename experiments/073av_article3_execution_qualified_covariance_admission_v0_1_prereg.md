# Exp073AV — Article 3 execution-qualified covariance/whitening admission firewall v0.1

**Frozen:** 2026-08-30 while real Exp073AQ Wm_S1 controlled twins are still in progress, before any successor real Layer-A or Layer-B result, before any real covariance read, and before nuisance/relation/G8 access.

## Purpose

Exp073AV is a non-scientific provenance/release gate. It does not inspect or validate any real covariance. It freezes the authority chain that must exist before the already-frozen covariance/whitening contract `docs/ARTICLE3_COVARIANCE_WHITENING_FAILCLOSED_CONTRACT_V0_1.md` may read a real covariance.

The numerical covariance contract remains unchanged. Exp073AV only requires that covariance restriction be bound to the exact same execution-qualified candidate authority that obtained real Layer-A PASS and real Layer-B PASS.

Hosted synthetic PASS adds **0 scientific-readiness points**. Strict Article-3 readiness remains **52%**; G7/G8/G9 remain OPEN.

## Required upstream authority chain

A future covariance-admission receipt is valid only if all are true:

1. `authority_route = controlled_single_thread_exact_v1`.
2. Candidate manifest is a real hosted complete Exp073AS successor manifest with:
   - `candidate_manifest_complete=true`;
   - exactly 1410 pre-support rows;
   - Exp073U ordered-ID SHA `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
   - controlled Wm_S0 anchor `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`.
3. Layer A was admitted under Exp073AT and has real terminal status exactly `PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`.
4. Layer B was admitted under Exp073AU and has real terminal status exactly `PASS_PHYSICAL_SUPPORT_ARTICLE3`.
5. Layer-A and Layer-B receipts bind exactly the same candidate-manifest SHA.
6. Layer B binds exactly the Layer-A `S_op` SHA/order, without rebuilding or reordering it.
7. The final Layer-B retained-coordinate manifest has dimension `d >= 15`, inherits Exp073U order, and has a deterministic SHA256.
8. Exact-threshold numerical ambiguity counts are zero for both Layer A and Layer B.
9. No covariance, whitening, nuisance, quotient/relation/null or G8 information was used to obtain either support PASS.

Any upstream Layer-A/Layer-B FAIL, INVALID_FOR_SCIENCE, infrastructure-INCOMPLETE, unresolved threshold ambiguity, authority mismatch or provenance mismatch blocks covariance admission.

## Covariance contract inherited unchanged

After Exp073AV admission, the existing fail-closed covariance contract alone governs real numerical validation. Exp073AV does **not** modify:

- raw coordinate binding requirement;
- `C_S.shape == (d,d)`;
- finite entries and strictly positive diagonal;
- `rho_sym <= tau_sym(d)`, with `tau_sym(d)=1000*eps64*max(1,d)`;
- ordinary unrescued Cholesky only;
- `rho_chol <= tau_chol(d)`, with the same frozen formula;
- triangular-solve whitening, no explicit matrix inverse;
- `rho_white <= sqrt(eps64)`;
- prohibition on jitter, eigenvalue clipping, nearest-SPD repair, post-failure symmetrization, covariance-selected mode deletion or pseudowhitening.

## Anti-leakage firewall

Before covariance admission all must remain false:

- `covariance_numerical_contents_read`
- `whitening_performed`
- `nuisance_geometry_read`
- `nuisance_svd_performed`
- `quotient_geometry_read`
- `relation_null_read`
- `chi_square_read`
- `p_value_read`
- `G8_read`
- `scientific_pass_claimed`

Readiness remains exactly 52, `readiness_increment=0`, and G7/G8/G9 remain OPEN.

## Synthetic test matrix

At minimum:

1. valid same-authority Layer-A PASS + Layer-B PASS -> `AUTHORIZE_COVARIANCE_READ`;
2. Layer-A FAIL -> block;
3. Layer-A INVALID -> block;
4. Layer-A infrastructure incomplete -> block;
5. Layer-B FAIL -> block;
6. Layer-B INVALID -> block;
7. Layer-B infrastructure incomplete -> block;
8. candidate SHA mismatch between A/B -> block;
9. Layer-B `S_op` parent mismatch -> block;
10. final retained count 14 -> block;
11. final retained count 15 -> authorize;
12. wrong route -> block;
13. wrong Exp073AS join schema -> block;
14. wrong Exp073U order SHA -> block;
15. historical primary-P anchor -> block;
16. Layer-A threshold ambiguity nonzero -> block;
17. Layer-B threshold ambiguity nonzero -> block;
18. covariance already read -> block;
19. whitening already performed -> block;
20. nuisance/relation/G8 leakage -> block;
21. malformed hashes -> reject closed;
22. unknown keys -> reject closed;
23. readiness drift -> reject closed;
24. G7/G8/G9 drift -> reject closed;
25. deterministic authorization receipt hash invariant under dictionary insertion order -> pass.

## Required token

`PASS_EXP073AV_EXECUTION_QUALIFIED_COVARIANCE_ADMISSION_SYNTHETIC_V0_1`

This token is provenance/release QA only. It is not a covariance PASS, does not authorize nuisance geometry or G7, and gives +0 readiness.
