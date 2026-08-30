# Exp073AW — Article 3 nuisance resolvability and SVD-rank rule v0.1

**Frozen:** 2026-08-30 while Exp073AQ Wm_S1 is still running, before any real successor covariance, whitening, nuisance matrix, target quotient, relation/null or G8 value exists.

## Purpose

The frozen signed-nuisance contract requires a prospectively defined numerical rank rule but does not specify one. Raw-column SVD rank is also vulnerable to arbitrary nuisance-parameter scaling. Exp073AW freezes a scale-invariant, fail-closed numerical rule before future scientific outputs can influence it.

This is architecture/numerics QA only. It reads no real covariance or nuisance output, claims no scientific PASS, gives +0 readiness, and keeps G7/G8/G9 OPEN.

## Upstream contracts retained unchanged

- `docs/ARTICLE3_SIGNED_NUISANCE_SUBSPACE_CONTRACT_V0_1.md`
- `docs/ARTICLE3_COVARIANCE_WHITENING_FAILCLOSED_CONTRACT_V0_1.md`
- Exp073AV successor covariance admission.

No support, covariance, nuisance-family or physics threshold is changed.

## Frozen arithmetic

Use float64 and `eps = numpy.finfo(float).eps`.

For each preregistered two-sided nuisance j after valid common whitening, define

`u_j = q_j_plus - q_j_minus`

and branch scale

`s_j = ||q_j_plus||_2 + ||q_j_minus||_2`.

Let observation dimension be `d >= 15` and freeze

`tau_res_j = 1000 * eps * max(1,d) * max(s_j, numpy.finfo(float).tiny)`.

A tangent is:

- `EXACT_NULL` iff `||u_j||_2 == 0`;
- `RESOLVED` iff `||u_j||_2 > 10 * tau_res_j`;
- `NUMERICALLY_UNRESOLVED` otherwise.

`NUMERICALLY_UNRESOLVED` is fail-closed for nuisance quotient execution. It may not be dropped, rounded to zero, or retained according to target overlap. `EXACT_NULL` is recorded but contributes no nuisance direction.

For each RESOLVED nuisance, form the central tangent `n_j = u_j/(2 delta_j)` and then the unit column

`v_j = n_j / ||n_j||_2`.

This unit-column normalization is mandatory before nuisance-rank SVD. It prevents arbitrary nuisance-parameter units or positive column rescaling from changing the numerical rank decision. Column sign remains irrelevant.

Let `V=[v_1,...,v_m]` and thin SVD `V = U Sigma W^T`. If `m=0`, nuisance rank is exactly 0. Otherwise define

`tau_rank = 1000 * eps * max(d,m) * sigma_max`.

For each singular value sigma_i:

- retained if `sigma_i > 10 * tau_rank`;
- discarded as numerical null if `sigma_i < tau_rank / 10`;
- otherwise the rank is `NUMERICALLY_UNRESOLVED_NUISANCE_RANK` and quotient/G7 execution is blocked.

This two-decade ambiguity firewall is frozen prospectively to prevent a near-threshold singular direction from being classified by rounding or downstream convenience.

## Required invariances

The resolved span/rank must be invariant under:

1. arbitrary positive rescaling of any nuisance parameter/column;
2. arbitrary sign flips;
3. nuisance-column permutation;
4. nonsingular well-conditioned basis changes that preserve the same exact span, when transformed columns remain numerically resolved;
5. simultaneous observation-coordinate orthogonal transformations in synthetic QA.

The rule must correctly identify exact duplicate/opposite columns, exact null columns, and clearly independent columns. Near-rank-threshold cases must return numerical-unresolved, never target-conditioned PASS/FAIL.

## Anti-leakage firewall

Forbidden inputs include target response, quotient residual, eta_N/theta_N, relation/null statistic, chi-square, p-value, G7/G8/G9, covariance repair choices, article claim metadata, or any ranking by target overlap.

## Required hosted token

`PASS_EXP073AW_NUISANCE_RANK_RULE_SYNTHETIC_V0_1`

Hosted PASS means only that the preregistered numerical semantics and invariances are implemented. It is not a nuisance scientific PASS and gives +0 scientific readiness.