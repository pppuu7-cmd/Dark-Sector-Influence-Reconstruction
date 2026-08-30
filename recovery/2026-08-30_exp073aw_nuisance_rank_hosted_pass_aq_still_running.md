# DSIR checkpoint — Exp073AW hosted nuisance-rank PASS, AQ still running

Date: 2026-08-30

## Scientific state

Strict Article-3 readiness remains **52%**. This checkpoint adds **0** scientific-readiness credit. G7/G8/G9 remain OPEN. No real covariance, nuisance matrix, target quotient, relation/null statistic or G8 value was read.

## Heavy authority state

Exp073AQ run `33327372191` remains active at this checkpoint:

- Wm_S1 replica A job `99299799192`: exact controlled computation IN PROGRESS;
- Wm_S1 replica B job `99299799338`: exact controlled computation IN PROGRESS;
- no AQ comparator artifact/classification yet.

Therefore Wm_S2 was not launched.

## Exp073AW purpose

The existing signed nuisance-subspace contract required a prospectively defined numerical SVD-rank/resolvability rule but did not specify one. Exp073AW freezes the missing rule before any downstream target/covariance/nuisance outcome can influence it.

Frozen semantics:

- two-sided branch difference `u_j=q_j+ - q_j-`;
- scale-free branch-aware resolvability threshold `tau_res_j = 1000*eps64*max(1,d)*max(||q_j+||+||q_j-||, tiny)`;
- exact null only for exactly zero branch difference;
- resolved only above `10*tau_res_j`; otherwise numerical-unresolved and fail-closed;
- every resolved tangent is normalized to unit L2 norm before SVD, preventing arbitrary nuisance-parameter scaling from changing span rank;
- `tau_rank = 1000*eps64*max(d,m)*sigma_max` on the normalized-column matrix;
- singular values above `10*tau_rank` are retained, below `tau_rank/10` are numerical null, and the intermediate band is `NUMERICALLY_UNRESOLVED_NUISANCE_RANK`, blocking quotient/G7 execution;
- target overlap is forbidden from rank/resolvability decisions.

## Hosted chronology

Prereg commit: `4e256a57dc9d3bac15ecc3e24910e277268ba6c5`.

Initial validator commit: `1abfbdf88973c992d254dbfc4445b2e21ba42928`.

Initial workflow commit: `ad2bdab20ecbeff844c45c66cf91f812af256ecf`.

Run `33332909901` / job `99314601956`: infrastructure-INCOMPLETE because hosted image lacked NumPy (`ModuleNotFoundError`). No scientific classification.

Environment bootstrap repair commit: `1697f17d1d571e0702453fb0c5f3bc350c3be4c2`. This changed only dependency installation, not frozen numerical semantics.

Run `33332955814` / job `99314730335`: infrastructure-INCOMPLETE because one toy cancellation control was incorrectly constructed; the frozen rule itself was unchanged. No scientific classification.

Synthetic-control repair commit: `37d60a868579e22fffaf9c912555f650ea0598b5`. Only the toy near-cancellation case changed; preregistered formulas did not.

First hosted PASS authority:

- run `33332987461`;
- job `99314811367`;
- head `37d60a868579e22fffaf9c912555f650ea0598b5`;
- artifact `9738177681`;
- digest `sha256:e3f9bb0cd847021ea416a7576a805b7a06308add7ee25c770f8a6b1a805a7257`;
- NumPy `2.5.2`;
- 13/13 checks passed;
- token `PASS_EXP073AW_NUISANCE_RANK_RULE_SYNTHETIC_V0_1`.

Fail-closed pipe repair commit `5f98825e36d4d7e75a405c9318bad41052ab4aa8` followed immediately so future Python assertion failures cannot be masked by `tee`. Its run `33332995634` also succeeded, but it is redundant infrastructure confirmation and is not used as extra scientific authority or readiness credit.

## Classification

`HOSTED_SYNTHETIC_PASS_EXP073AW_NUISANCE_RANK_RULE_V0_1`

This is numerical-method QA only. It is not a nuisance scientific PASS and does not authorize target quotient/G7 by itself.
