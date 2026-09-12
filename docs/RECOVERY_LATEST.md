# DSIR authoritative recovery — latest

Updated: 2026-09-13. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the recovery source of truth. Older recovery notes remain immutable history and must not reopen superseded Layer-B work.

## Frozen scientific boundaries

Production `h=1e-4`; native `k_per_decade_for_pk=20`; strict response-stability tolerance `<1e-3`; exact target-k binding mismatch `<=1e-12`. Covariance restriction unauthorized; whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by the current diagnostic chain.

## Closed chain through V0.6

V0.5 run `34717972131`: `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`, effect `+0/+0`. Exactly 20/23 failing exact-target coordinates have five-h spread `>=1e-3`; controls remain stable.

V0.6 authority: `docs/dsir4/authority/LAYERB_BETA_FD_REPAIR_V0_6.json`, commit `4b62f4bf4057d34eff2b7cc1ceef98d63f8eafa7`. Classification `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`: Richardson repair recovered only 4/20 frozen h-unstable failures (`0.2`), median raw spread `0.003260200828240146` versus repaired local median `0.003198104008657432`. Exact-target mismatch max `1.2517848722592053e-16`; invariants PASS. Ordinary finite-difference truncation is not the dominant source.

## V0.7 — terminal partial solver-conditioning support

Authority: `docs/dsir4/authority/LAYERB_BETA_SOLVER_CONDITIONING_V0_7.json`, creation commit `b84dbcfd08046792866270d9b1dea7b2dfc6c955`.

Run `34719555760`, head `419e109429f77cb233a01b99e80c82d1c504e700`; all ten profile/domain jobs and decision job `103623179260` terminal success. Decision artifact `10306115925`, ZIP SHA256 `521fa3a3a42e68154afe5d310098e46519919678ba8a154dd16a7a16de74824f`.

Classification: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`. Attribution: `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`. Effect `+0/+0`.

Frozen parent-unstable subset: 20 coordinates, production median h-spread `0.004804415208560067`.

Tolerance-only results: `TOL10` (`3e-11`) recovers 11/20 (`0.55`), median `0.000810683437303502`, reduction `5.926x`; `TOL100` (`3e-12`) recovers 14/20 (`0.70`), median `0.0006864929897004239`, reduction `6.998x`.

Sampling-only results: `SAMP2` and `SAMP4` recover 0/20 and leave median essentially unchanged (`~0.004804`). Joint `TOL100+SAMP4` also recovers 14/20 with median `0.0006866054910050431`, showing no material added value from denser sampling. Tolerance axis monotonic; sampling axis not monotonic/material. All controls stable; exact target mismatch max `1.2517848722592053e-16`; joint interaction non-pathological.

Strong support was not awarded because preregistered recovery required `>=0.75` and observed best recovery was `0.70`. The threshold must not be changed post hoc.

Authorized successor: `PROSPECTIVELY_FROZEN_LOCALIZED_SOLVER_KNOB_ISOLATION_AUDIT` only.

## V0.8 — localized integration-tolerance isolation active

Contract: `docs/dsir4/contracts/LAYERB_BETA_TOLERANCE_KNOB_ISOLATION_V0_8.json`, creation commit `b329c72307771cc1768f156e4da25efaaf7dced2`.

Executor: `ci/layerb_beta_tol_isolation_v0_8.py`, creation commit `70ef8bbaebd0585ed9adafa3eb738c07e56d4661`, blob `2638690f17510033cca88494514dbc6cb208bb36`.

Workflow: `.github/workflows/layerb-beta-tolerance-isolation-v0-8.yml`, creation commit `10e33f74160d96e773557eb0a41e0089227d9f5e`.

Launch commit `00b365d08059f8eff81c8b1c963a13902f839aa0`; active run `34719854763`.

Tolerance ladder is frozen before V0.8 results: `PROD=3e-10`, `TOL3=1e-10`, retained V0.7 `TOL10=3e-11`, `TOL30=1e-11`, retained V0.7 `TOL100=3e-12`, `TOL300=1e-12`, `TOL1000=3e-13`. Sampling remains at production `0.00035` for all V0.8 calculations.

Efficiency rule: V0.7 `TOL10` and `TOL100` D/B artifacts are reused by exact artifact ID/SHA256 and are forbidden to recompute. V0.8 computes only four new tolerance values across D/B = eight new hosted science lanes.

A profile is prospectively defined as adequate only if controls remain `<1e-3`, at least 75% of the immutable 20-coordinate unstable subset recover `<1e-3`, and subset median h-spread is `<1e-3`. Candidate is the least-strict adequate tolerance whose entire tighter tested suffix remains adequate under frozen adjacent sanity bounds. No post-result retuning is allowed.

At the latest write, invariant-audit is terminal PASS. Five of eight new jobs have been picked up by hosted runners and three are queued; partial numerical outputs must not be inspected before the full decision barrier.

## Exact next order

1. Continue only V0.8 run `34719854763`; no duplicate tolerance sweep.
2. Wait for all eight new profile/domain jobs to become terminal; do not use partial numerical output to alter thresholds or ladder.
3. Decision must reuse exact V0.7 TOL10/TOL100 artifacts and exact V0.6 raw D/B artifacts, verify provenance, then apply the frozen V0.8 classifier.
4. Promote V0.8 authority only after terminal decision provenance is verified.
5. Launch only the classifier-authorized successor. A stable candidate can authorize only a stabilized-tolerance LOCAL common-grid validation; no outcome directly opens covariance, Wm_S3, global 65537 or a science gate.

## Publication/readiness locks

Last frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; diagnostic progress alone does not change them. Article-II real cross-family G5 ACT×unWISE closure remains a separate unresolved publication-readiness requirement; no ready repository executor/contract for that real-data gate was found in the current search, so no fabricated G5 run was launched.

## Automation / ownership

`DSIR Continuous Research` and `DSIR Auto-Research Guard` are disabled. Five other enabled research automations currently occupy the available task slots: QGR, MSQGR, KMQGB, RQIR-CG and ISQGR. Do not silently disable another project to free a DSIR slot without explicit user reprioritization.

V0.8 is GitHub-hosted diagnostic compute, not a new self-hosted `DSIR-HOME-PC` heavy-science run.
