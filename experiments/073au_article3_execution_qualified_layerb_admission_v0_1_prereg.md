# Exp073AU — Article 3 execution-qualified Layer-B admission firewall v0.1

**Frozen:** 2026-08-30 after hosted Exp073AT synthetic PASS, while real Exp073AQ Wm_S1 controlled twins are still in progress, before any AQ comparator authority exists, before any real execution-qualified 14-window aggregate, before any real Exp073AS candidate manifest, before any real Layer-A score, and before covariance inspection.

## Purpose

Exp073AU is a non-scientific provenance/release gate between the future real Layer-A result and the already-frozen broad-row Layer-B semantics in `docs/ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md` and Exp073V.

The Layer-B mathematics is not changed. Exp073AU only prevents a future Layer-B execution from consuming a Layer-A result from the historical authority route, an incomplete candidate manifest, a different candidate manifest, an altered/reordered `S_op`, an unresolved exact-threshold comparison, or any state that has already read covariance/nuisance/G8 information.

Hosted synthetic PASS adds **0 scientific-readiness points**. Strict Article-3 readiness remains **52%**.

## Required upstream chain

A future Layer-B input is admissible only when all upstream identities are bound in one immutable receipt:

1. authority route `controlled_single_thread_exact_v1` authorized by Exp073AO/AP;
2. future real 14-window aggregate validated under Exp073AR;
3. future real complete 1410-row pre-support candidate manifest validated under Exp073AS;
4. candidate-to-Layer-A admission validated under Exp073AT;
5. real Layer-A result on that exact candidate manifest.

Historical primary-P, `canonical_exp073x2`, old `exp073aa`, historical Exp073AE join, single-replica successor inputs, tolerance/ULP/rounding, majority vote or preferred-replica rescue are not admissible.

## Frozen Layer-A receipt contract

The Layer-A receipt presented to Exp073AU must declare exactly:

- `authority_route = controlled_single_thread_exact_v1`;
- `candidate_join_schema = exp073as_execution_qualified_presupport_join_v0_1`;
- `layera_admission_schema = exp073at_execution_qualified_layera_admission_v0_1`;
- `layera_status = PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`;
- `candidate_manifest_complete = true`;
- `candidate_row_count = 1410`;
- block counts `Wm=780`, `WW=390`, `BOSS=240`;
- Exp073U ordered-ID SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
- controlled Wm_S0 anchor SHA256 `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- immutable 64-hex candidate manifest SHA256;
- immutable 64-hex Layer-A result SHA256;
- `S_op` retained row count at least `15` and at most `1410`;
- `S_op` ordered-ID SHA256 as 64 lowercase hex;
- `S_op_inherited_exp073u_order = true`;
- `operator_f_invalid_threshold = 0.05`;
- `operator_f_invalid_threshold_inclusive = true`;
- exact domain bounds `z_min=0.295`, `z_max=2.33`, `k_max_Mpc^-1=0.06664762008318016`;
- `threshold_numerical_ambiguity_count = 0`.

The last condition is bookkeeping, not a new threshold: the already-frozen rule says exact-threshold numerical ambiguity remains `numerically_unresolved` and may never be rounded into PASS/FAIL. Therefore a receipt claiming Layer-A PASS while retaining unresolved threshold comparisons is inadmissible for Layer B.

## Frozen `S_op` inheritance

Layer B may receive only the exact Layer-A retained row set `S_op`.

It may not:

- rerun Layer A with changed numerical settings;
- add back rejected rows;
- remove rows based on response amplitude;
- reorder retained rows;
- recenter or scalarize broad support;
- use covariance, whitening, nuisance alignment, relation/null information or G8 to modify `S_op`.

The inherited order must be the restriction of Exp073U order to the retained IDs.

## Layer-B semantics retained unchanged

For each `i in S_op`, Layer B evaluates the already-frozen common-response validity on the active in-domain support atoms. A row is valid only when the active in-domain set is non-empty and every required final-response component is finite and strictly positive on every active in-domain atom.

The frozen scientific Layer-B acceptance remains:

- invalid observation-row fraction `<= 0.05` inclusive;
- at least `15` common-response-valid observation rows after removal;
- no response component silently removed;
- no effective `(z,k)` or effective-ell shortcut.

Exp073AU does not evaluate these quantities.

## Anti-leakage firewall

The admission receipt must assert all of the following exactly false:

- `covariance_read`;
- `inverse_covariance_read`;
- `whitening_performed`;
- `nuisance_geometry_read`;
- `nuisance_svd_performed`;
- `relation_null_read`;
- `chi_square_read`;
- `p_value_read`;
- `G8_read`;
- `scientific_pass_claimed_by_admission_gate`.

It must also preserve:

- `fiducial_P_weighting_used=false`;
- `effective_ell_override=false`;
- `effective_z_override=false`;
- `effective_k_override=false`;
- `signed_Wm=true`;
- `selection_reads=[]`.

## Scientific accounting

Exp073AU is provenance/release QA only:

- readiness increment `0`;
- Article-3 scientific readiness remains `52%` at synthetic-gate time;
- Layer B remains OPEN until a real Layer-B hosted authority exists;
- covariance/whitening remain BLOCKED until real Layer-A PASS and real Layer-B PASS exist on the same inherited authority chain;
- G7/G8/G9 remain OPEN;
- no dark-sector model scientific PASS is claimed.

## Frozen synthetic test matrix

At minimum:

1. exact valid synthetic successor Layer-A PASS receipt -> admit Layer B;
2. Layer-A FAIL -> reject;
3. Layer-A INVALID_FOR_SCIENCE -> reject;
4. historical authority route -> reject;
5. old Exp073AE join schema -> reject;
6. wrong Exp073AT admission schema -> reject;
7. incomplete candidate manifest -> reject;
8. candidate row-count drift -> reject;
9. block-count drift -> reject;
10. Exp073U order authority drift -> reject;
11. Wm_S0 anchor drift -> reject;
12. malformed candidate manifest SHA -> reject;
13. malformed Layer-A result SHA -> reject;
14. `S_op` count below 15 -> reject;
15. `S_op` count above 1410 -> reject;
16. malformed `S_op` ordered-ID SHA -> reject;
17. `S_op_inherited_exp073u_order=false` -> reject;
18. Layer-A threshold drift -> reject;
19. domain-bound drift -> reject;
20. unresolved threshold ambiguity count >0 -> reject;
21. covariance/whitening leakage -> reject;
22. nuisance/relation/G8 leakage -> reject;
23. effective-coordinate/fiducial-P/selection leakage -> reject;
24. unknown top-level or nested field -> reject;
25. readiness/gate-state drift -> reject;
26. deterministic admission metadata SHA invariant under dictionary insertion order -> pass.

## Required hosted synthetic QA token

`PASS_EXP073AU_EXECUTION_QUALIFIED_LAYERB_ADMISSION_SYNTHETIC_V0_1`

This token means only that the future Layer-A -> Layer-B boundary is fail-closed. It is not Layer-A PASS, not Layer-B PASS, not covariance authorization, and gives +0 readiness.
