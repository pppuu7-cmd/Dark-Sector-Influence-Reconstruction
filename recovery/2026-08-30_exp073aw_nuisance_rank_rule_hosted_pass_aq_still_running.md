# DSIR checkpoint — Exp073AW nuisance rank-resolution rule hosted PASS; Exp073AQ still active

**UTC chronology:** 2026-08-30.

## Heavy production state

Exp073AQ run `33327372191` remains the only active heavy production. Latest inspection after Exp073AW completion:

- Wm_S1 replica A job `99299799192`: `in_progress`;
- Wm_S1 replica B job `99299799338`: `in_progress`;
- no AQ comparator authority artifact yet.

No duplicate Wm_S1 and no Wm_S2 was launched.

## Newly closed methodological gap

The Article-3 signed nuisance-subspace contract required a prospectively frozen numerical-rank rule and final-representation nuisance resolvability threshold, but repository audit found no separate current rule. Exp073AW freezes that rule before any real nuisance singular value or target quotient is observed.

Frozen chain:

- prereg `bedb43f020fbbbb3af82671f1a801e6811b14a77`;
- validator `f6b69d173deafb401913083623246fa5dd2f65eb`;
- workflow `5f878cde775849df5223efb5671ea69e4665514b`;
- workflow freeze `2a6586c7264a2365fee7bf46a1b1cbc95962536f`;
- trigger/head `93df9575fa1ba9deb5c09d6eb39158e1a5a3e0bb`.

Hosted result:

- run `33332915782`;
- job `99314619888`;
- started `2026-08-30T20:10:50Z`;
- completed success by `2026-08-30T20:11:04Z`;
- artifact `9738157877`;
- digest `sha256:ad9c924f582d07bcb5ac72791a70f762f2a7e9e36acddff117eeda770c0b6de2`;
- token `PASS_EXP073AW_NUISANCE_SVD_RANK_RESOLUTION_SYNTHETIC_V0_1`;
- 20/20 synthetic controls passed.

Classification: `HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

## Frozen numerical rule

For whitened nuisance matrix `N_w` of shape `(d,m)`:

- `eps64 = numpy.finfo(float64).eps`;
- `tau_rank = eps64 * max(d,m) * sigma_max`;
- retain singular mode iff `sigma_i > tau_rank`;
- `sigma_i < tau_rank` is numerically unresolved;
- exact `sigma_i == tau_rank` is `NUMERICALLY_UNRESOLVED_NUISANCE_RANK_BOUNDARY` and blocks quotient/G7 rather than being rounded.

For individual nuisance columns:

- `epsilon_num = eps64 * max(d,m) * c_max`, where `c_max` is the largest nuisance-column norm;
- resolve a column only for `c_j > epsilon_num`;
- exact equality is a numerical boundary ambiguity and blocks normalized-angle use for that column.

All-zero nuisance matrix has rank 0 and remains an explicit resolved numerical state, not a dark-sector conclusion.

## Firewalls

Rank/resolution is fixed before target response, target overlap, quotient, relation/null, chi-square/p-value or G8. SVD is required; normal-equation inversion is forbidden. Duplicate/opposite/null directions remain explicit and cannot be post-hoc selected according to target survival.

## Scientific accounting

Exp073AW reads no real covariance/nuisance/target response and gives +0 readiness. Strict Article-3 readiness remains **52%**. G7/G8/G9 remain OPEN.

## Current order

`AQ Wm_S1 -> remaining controlled twins -> Exp073AR -> Exp073AS -> Exp073AT/Layer A -> Exp073AU/Layer B -> Exp073AV/covariance whitening -> Exp073AW nuisance rank/resolution -> signed nuisance projector/quotient -> G7 relation/null -> fresh G8`.
