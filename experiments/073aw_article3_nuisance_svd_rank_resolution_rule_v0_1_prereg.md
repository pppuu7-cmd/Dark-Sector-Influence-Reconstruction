# Exp073AW — Article 3 nuisance SVD numerical-rank and representation-resolution rule v0.1

**Frozen:** 2026-08-30 while Exp073AQ Wm_S1 is still running, before any real successor covariance read, before any real nuisance singular value is computed, and before any target quotient/relation/G8 statistic exists.

## Purpose

The frozen signed nuisance-subspace contract requires a target-independent numerical-rank rule and a final-representation nuisance resolvability threshold, but no separate current Article-3 rule was found in repository authority. Exp073AW closes that numerical-method gap prospectively.

Exp073AW is numerical architecture QA only. It does not read real covariance, nuisance vectors, target responses, relation/null outputs or G8. Hosted PASS adds **0 scientific-readiness points**; strict Article-3 readiness remains **52%**.

## Frozen SVD input

After a real covariance/whitening PASS, let the whitened signed nuisance matrix be

`N_w in R^(d x m)`

with inherited final observation order, `d >= 15`, and prospectively fixed nuisance-family/step provenance. All entries must be finite. SVD is thin SVD with singular values `sigma_1 >= ... >= sigma_p >= 0`, `p=min(d,m)`.

No target response may be read before rank is frozen for that nuisance matrix.

## Frozen numerical-rank rule

Let

- `eps64 = numpy.finfo(numpy.float64).eps`;
- `sigma_max = sigma_1` when `p>0`, else `0`;
- `tau_rank = eps64 * max(d,m) * sigma_max`.

If `sigma_max == 0`, numerical rank is exactly `0` and all nuisance columns are numerically null in the final whitened representation.

Otherwise:

- retain singular mode `i` iff `sigma_i > tau_rank`;
- discard it as numerically unresolved iff `sigma_i < tau_rank`;
- if canonical float64 `sigma_i == tau_rank` exactly, the rank classification is `NUMERICALLY_UNRESOLVED_NUISANCE_RANK_BOUNDARY` and downstream quotient/G7 is blocked. No rounding to PASS/FAIL is permitted.

This is the standard machine-precision/dimension-scaled SVD rank criterion and is frozen before observing real singular values.

## Frozen individual-column resolvability rule

For nuisance tangent columns `n_j`, compute canonical float64 norms `c_j = ||n_j||_2` and `c_max=max_j c_j`.

- if `c_max == 0`, every nuisance column is numerically unresolved in the final representation;
- otherwise set `epsilon_num = eps64 * max(d,m) * c_max`;
- a nuisance direction is resolved iff `c_j > epsilon_num`;
- `c_j < epsilon_num` is numerically unresolved;
- exact equality `c_j == epsilon_num` is `NUMERICALLY_UNRESOLVED_NUISANCE_COLUMN_BOUNDARY` and blocks any normalized angle for that column.

Unresolved nuisance directions remain explicit provenance records; they are never silently deleted because their removal benefits the target residual.

## Rank must be target independent

Forbidden before rank and column-resolvability receipts are immutable:

- target response or target norm;
- target-nuisance overlap;
- quotient residual `eta_N`/`theta_N`;
- relation/null residual;
- chi-square/p-value;
- G7/G8/G9 output.

The rank threshold may not be tuned after any such read.

## Numerical implementation requirements

- use SVD, not inversion of `N_w^T N_w`;
- persist all canonical singular values, `tau_rank`, retained rank, `epsilon_num`, column norms and boundary-ambiguity counts;
- persist orthogonality and projector-idempotence diagnostics after rank is resolved;
- exact duplicate/opposite columns must not spuriously increase rank;
- global positive rescaling of the entire nuisance matrix must leave numerical rank unchanged;
- arbitrary sign flips of columns must leave rank/projector unchanged;
- row-coordinate permutation applied consistently must leave singular values/rank unchanged;
- a well-conditioned nonsingular nuisance-basis transformation on test matrices far from the numerical boundary must preserve the represented subspace/projector.

## Scientific/authority classification

Rank or column boundary equality is numerical ambiguity, not scientific evidence. Nonfinite input is `INVALID_FOR_SCIENCE_NUISANCE_NUMERICS`. A resolved rank receipt is still only a prerequisite; it does not by itself authorize G7.

## Anti-leakage firewall

Synthetic QA must assert false for:

- `real_covariance_read`
- `real_nuisance_read`
- `target_response_read`
- `target_overlap_read`
- `quotient_read`
- `relation_null_read`
- `chi_square_read`
- `p_value_read`
- `G8_read`
- `scientific_pass_claimed`

Readiness remains 52, increment 0, G7/G8/G9 OPEN.

## Required hosted synthetic controls

At minimum test:

1. full-rank matrix -> expected rank;
2. exact duplicate column -> rank reduction;
3. exact opposite column -> rank reduction;
4. exact zero column -> unresolved column without rank inflation;
5. all-zero matrix -> rank 0;
6. global positive rescaling -> same rank;
7. column sign flips -> same singular values/rank;
8. consistent row permutation -> same singular values/rank;
9. near-collinear but clearly above threshold -> retained rank;
10. constructed singular value clearly below threshold -> dropped;
11. exact synthetic rank-boundary equality through direct classifier -> numerically unresolved;
12. exact synthetic column-boundary equality through direct classifier -> numerically unresolved;
13. nonfinite matrix -> invalid;
14. `d<15` -> reject stage input;
15. target-read firewall activation -> reject;
16. covariance-read synthetic activation -> reject;
17. quotient/G8 leakage -> reject;
18. readiness drift -> reject;
19. gate-state drift -> reject;
20. deterministic receipt hash invariant to dictionary insertion order -> pass.

## Required token

`PASS_EXP073AW_NUISANCE_SVD_RANK_RESOLUTION_SYNTHETIC_V0_1`

This token means only that the target-independent numerical rank/resolution rule is frozen and software-tested. It is not nuisance scientific PASS, not G7, and gives +0 readiness.
