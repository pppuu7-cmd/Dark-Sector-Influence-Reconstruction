# DSIR recovery manual addendum — Exp073AW nuisance SVD rank/resolution rule

Read with the base recovery manual, current live overlay, Exp073AV addendum, and `docs/RECOVERY_LATEST.md`.

## Scientific state unchanged

- strict Article-3 readiness: **52%**;
- G7/G8/G9: OPEN;
- no real covariance/nuisance/target quotient was read by Exp073AW;
- hosted synthetic/numerical QA adds +0 readiness;
- RTK/RQIR remain excluded.

## Exp073AW immutable authority

- prereg `bedb43f020fbbbb3af82671f1a801e6811b14a77`;
- validator `f6b69d173deafb401913083623246fa5dd2f65eb`;
- workflow `5f878cde775849df5223efb5671ea69e4665514b`;
- workflow freeze `2a6586c7264a2365fee7bf46a1b1cbc95962536f`;
- trigger/head `93df9575fa1ba9deb5c09d6eb39158e1a5a3e0bb`;
- hosted run `33332915782`, job `99314619888`;
- artifact `9738157877`;
- digest `sha256:ad9c924f582d07bcb5ac72791a70f762f2a7e9e36acddff117eeda770c0b6de2`;
- token `PASS_EXP073AW_NUISANCE_SVD_RANK_RESOLUTION_SYNTHETIC_V0_1`;
- 20/20 controls passed;
- classification `HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

## Numerical-rank rule

For real future whitened nuisance matrix `N_w` shape `(d,m)` after valid covariance PASS:

`tau_rank = eps64 * max(d,m) * sigma_max`.

Retain `sigma_i` iff `sigma_i > tau_rank`. Values below are numerically unresolved. Exact canonical float64 equality to the threshold is **numerically unresolved boundary ambiguity** and blocks downstream quotient/G7 until prospectively resolved; never round equality to retained/dropped.

If `sigma_max==0`, rank is 0 and all nuisance directions are numerically null in the final whitened representation. This is a numerical representation state, not evidence about dark-sector physics.

## Individual nuisance-column resolution

Let `c_j=||n_j||_2` and `c_max=max c_j`. For nonzero `c_max`:

`epsilon_num = eps64 * max(d,m) * c_max`.

A normalized nuisance direction exists only for `c_j > epsilon_num`; below threshold it is unresolved; exact equality is numerical ambiguity. Unresolved nuisance provenance remains explicit and may not be silently dropped because target residual improves.

## Required ordering

Rank/resolution must be computed only after Exp073AV-admitted real covariance/whitening PASS, but **before reading target response/overlap or quotient**. Use SVD directly; do not infer rank from `N_w^T N_w` inversion. Persist singular values, thresholds, rank, column norms, ambiguity counts, orthogonality and projector-idempotence diagnostics.

## Current blocker

Exp073AQ Wm_S1 hosted twins remain active. Do not start Wm_S2 until AQ obtains a valid terminal comparator authority and exact PASS.
