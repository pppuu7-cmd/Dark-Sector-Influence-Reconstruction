# DSIR disposition record — non-authoritative duplicate Exp073AW branch

Date: 2026-08-30

## Authority disposition

This file preserves the chronology of a parallel duplicate nuisance-rank branch that was created while another Exp073AW branch was already being completed concurrently. It is **NOT** the authoritative Exp073AW scientific/numerical contract.

Repository authority is the Exp073AW chain recorded in `docs/RECOVERY_LATEST.md` and `docs/RECOVERY_MANUAL_ADDENDUM_EXP073AW_2026-08-30.md`:

- prereg `bedb43f020fbbbb3af82671f1a801e6811b14a77`;
- validator `f6b69d173deafb401913083623246fa5dd2f65eb`;
- workflow `5f878cde775849df5223efb5671ea69e4665514b`;
- workflow freeze `2a6586c7264a2365fee7bf46a1b1cbc95962536f`;
- trigger/head `93df9575fa1ba9deb5c09d6eb39158e1a5a3e0bb`;
- hosted run `33332915782`, job `99314619888`, artifact `9738157877`;
- digest `sha256:ad9c924f582d07bcb5ac72791a70f762f2a7e9e36acddff117eeda770c0b6de2`;
- token `PASS_EXP073AW_NUISANCE_SVD_RANK_RESOLUTION_SYNTHETIC_V0_1`;
- 20/20 controls passed.

Its frozen rule (`tau_rank = eps64*max(d,m)*sigma_max` and the corresponding column-resolution rule) is the only live Exp073AW rule.

## Duplicate branch chronology retained for audit only

The competing branch began with prereg commit `4e256a57dc9d3bac15ecc3e24910e277268ba6c5` before the concurrent authoritative branch became visible in the live recovery pointer.

Its hosted chronology included:

- run `33332909901` / job `99314601956`: infrastructure-INCOMPLETE (`ModuleNotFoundError: numpy`);
- environment bootstrap repair `1697f17d1d571e0702453fb0c5f3bc350c3be4c2`;
- run `33332955814` / job `99314730335`: infrastructure-INCOMPLETE due to an incorrectly constructed toy cancellation control;
- toy-control repair `37d60a868579e22fffaf9c912555f650ea0598b5`;
- run `33332987461` / job `99314811367`: synthetic success, artifact `9738177681`, digest `sha256:e3f9bb0cd847021ea416a7576a805b7a06308add7ee25c770f8a6b1a805a7257`, 13/13 checks;
- later run `33332995634`: redundant synthetic success.

These results are **non-authoritative infrastructure/numerical QA only** and provide no scientific-readiness credit. They must not be used to replace or modify the authoritative Exp073AW threshold.

The duplicate prereg, validator, workflow and trigger were removed from the current live tree after the authority collision was detected. Their Git history is intentionally preserved for auditability.

## Scientific state

Strict Article-3 readiness remains **52%**. G7/G8/G9 remain OPEN. No real covariance, nuisance matrix, target quotient, relation/null statistic or G8 value was read by this duplicate branch.

Exp073AQ run `33327372191` remained active during this disposition; Wm_S2 was not launched.
