# DSIR current-process ledger

Updated: 2026-09-13. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Active frontier — V0.8 integration-tolerance knob isolation

Authoritative active run: `34719854763`, launch commit `00b365d08059f8eff81c8b1c963a13902f839aa0`.

Prospectively frozen contract: `docs/dsir4/contracts/LAYERB_BETA_TOLERANCE_KNOB_ISOLATION_V0_8.json`, creation commit `b329c72307771cc1768f156e4da25efaaf7dced2`.

V0.8 follows the terminal V0.7 result that upstream response-solver conditioning is partially supported and specifically sensitive to `tol_perturb_integration`, not to `perturb_sampling_stepsize`.

Frozen tolerance ladder: production `3e-10`, new `TOL3=1e-10`, retained `TOL10=3e-11`, new `TOL30=1e-11`, retained `TOL100=3e-12`, new `TOL300=1e-12`, new `TOL1000=3e-13`. Sampling remains production `0.00035`; production `h=1e-4`, five-h ladder and strict `<1e-3` response threshold remain unchanged.

Only TOL3/TOL30/TOL300/TOL1000 are newly computed, crossed with domains D/B for eight hosted jobs. Existing V0.7 TOL10/TOL100 D/B artifacts are reused by exact IDs/SHA256 and are forbidden to recompute.

Frozen adequacy rule: controls `<1e-3`, recovery of at least 75% of the immutable 20-coordinate h-unstable parent subset, and subset median h-spread `<1e-3`. Candidate is the least-strict adequate profile whose entire tighter tested suffix stays adequate under frozen adjacent sanity checks. No post-result retuning.

At the latest ledger update, V0.8 invariant-audit is terminal PASS; five new jobs are running and three queued. Do not inspect partial science outputs. Continue only run `34719854763` until the full decision barrier.

## Closed parent — V0.7 partial upstream solver-conditioning support

Authority: `docs/dsir4/authority/LAYERB_BETA_SOLVER_CONDITIONING_V0_7.json`, commit `b84dbcfd08046792866270d9b1dea7b2dfc6c955`.

Run `34719555760`, decision job `103623179260`, decision artifact `10306115925`, ZIP SHA256 `521fa3a3a42e68154afe5d310098e46519919678ba8a154dd16a7a16de74824f`.

Classification `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`; attribution `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`; effect `+0/+0`.

Production parent-unstable median h-spread `0.004804415208560067`. `TOL10=3e-11`: 11/20 recovered, median `0.000810683437303502`, `5.926x` reduction. `TOL100=3e-12`: 14/20 recovered, median `0.0006864929897004239`, `6.998x` reduction. `SAMP2/SAMP4`: 0/20 recovered, essentially no median improvement. Joint `TOL100+SAMP4`: 14/20, median `0.0006866054910050431`, so sampling adds no material benefit. All controls stable, keysets exact, exact-target mismatch max `1.2517848722592053e-16`.

Strong support was not awarded because frozen strong recovery threshold was 75% and best observed recovery was 70%; this threshold must not be altered post hoc.

## Closed parent — V0.6 FD repair not supported

Authority `docs/dsir4/authority/LAYERB_BETA_FD_REPAIR_V0_6.json`, commit `4b62f4bf4057d34eff2b7cc1ceef98d63f8eafa7`. Classification `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`: 4/20 recovered, `0.2`; ordinary centered finite-difference truncation is not the dominant source.

## Frozen safety / anti-duplication

No covariance, whitening/nuisance/relation-null, `Wm_S3`, global 65537 or science gate is authorized. Current V0.8 jobs are GitHub-hosted diagnostics, not a self-hosted `DSIR-HOME-PC` heavy run.

If V0.8 has an infrastructure failure, repair only the smallest technical defect and reuse immutable successful artifacts. Do not alter tolerance ladder, adequacy threshold, h ladder, target coordinates, sampling step or decision logic.

## Recovery/readiness

`docs/RECOVERY_LATEST.md` advanced to V0.7 terminal + V0.8 active in commit `99b4049357483963780561f20524ffc60b1279c2`.

Last frozen readiness values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`. Article-II real G5 ACT×unWISE remains a separate unresolved publication gate.

## Automation

`DSIR Continuous Research` and `DSIR Auto-Research Guard` remain disabled. Five active automation slots are currently occupied by QGR, MSQGR, KMQGB, RQIR-CG and ISQGR. Do not disable those projects silently.
