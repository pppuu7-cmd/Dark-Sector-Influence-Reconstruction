# DSIR authoritative recovery — latest

Updated: 2026-09-13. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the recovery source of truth. Older recovery notes remain immutable history and must not reopen superseded Layer-B work.

## Frozen scientific boundaries

Production `h=1e-4`; native `k_per_decade_for_pk=20`; strict response-stability tolerance `<1e-3`; exact target-k binding mismatch `<=1e-12`; production `perturb_sampling_stepsize=0.00035`. Covariance restriction unauthorized; whitening/nuisance/relation-null unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this diagnostic chain.

## Closed chain through V0.7

V0.5 run `34717972131`: `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`, 20/23 failing exact-target coordinates h-unstable.

V0.6 authority `docs/dsir4/authority/LAYERB_BETA_FD_REPAIR_V0_6.json`, commit `4b62f4bf4057d34eff2b7cc1ceef98d63f8eafa7`: `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`; Richardson recovered 4/20. Ordinary finite-difference truncation is not the dominant source.

V0.7 authority `docs/dsir4/authority/LAYERB_BETA_SOLVER_CONDITIONING_V0_7.json`, commit `b84dbcfd08046792866270d9b1dea7b2dfc6c955`, run `34719555760`: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, attribution `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`. `TOL10=3e-11` recovered 11/20 with median `0.000810683437303502`; `TOL100=3e-12` recovered 14/20 with median `0.0006864929897004239`; sampling-only profiles recovered 0/20. Frozen strong threshold 75% was not met by the best 70% V0.7 recovery.

## V0.8 — terminal tolerance sweep, inconclusive because of one control instability

Authority: `docs/dsir4/authority/LAYERB_BETA_TOLERANCE_ISOLATION_V0_8.json`, creation commit `1ae1d93199b61f66a7b23f945d586b580e5bc3bd`.

Run `34719854763`, head `00b365d08059f8eff81c8b1c963a13902f839aa0`; decision job `103624105106`; decision artifact `10305343325`, ZIP SHA256 `0cfd690a123aa2891646eb89a29d873d3877ab0532fa45f7e174a657434f4c10`.

Classification: `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`, effect `+0/+0`. The tolerance trend is scientifically informative but cannot be promoted because the frozen all-controls invariant failed.

Key ladder: production `3e-10` recovered 0/20, median `0.004804415208560067`; `1e-10` recovered 10/20, median `0.0010349341119287158`; `3e-11` recovered 11/20, median `0.000810683437303502`; `1e-11` recovered 14/20, median `0.0006824582255432214` but control max `0.0012003119264226171 > 0.001`; `3e-12` recovered 14/20; `1e-12` recovered 16/20 (`0.8`), median `0.000510732305940965`, controls stable; `3e-13` recovered 16/20, median `0.0005100571566997025`, controls stable.

The observed `TOL300=1e-12` profile is therefore promising but explicitly **not authorized**. The only authorized successor is a prospectively frozen reproducibility/localization audit of the anomalous TOL30 control plus independent TOL300 replication.

## V0.9 — TOL30 resonance localization + TOL300 replication active

Parent authority: V0.8 commit `1ae1d93199b61f66a7b23f945d586b580e5bc3bd`.

Executor `ci/layerb_beta_tol30_resonance_v0_9.py`, creation commit `058c3cf0dde08325e4b768d1cc39e1f973e1769f`, blob `dcbdd3641b62b9399a1fc78dfbf3abd36d9b16e2`.

Prospectively frozen contract `docs/dsir4/contracts/LAYERB_BETA_TOL30_RESONANCE_AUDIT_V0_9.json`, creation commit `08fc52377b17285a3dda701b5c2829f8c8e49a9c`.

Workflow `.github/workflows/layerb-beta-tol30-resonance-v0-9.yml`, creation commit `fc6379a1a969d6446b0dadae137dbf6074a87b90`.

Launch commit `4004e876d0311654da2153ded992834ff83adf49`; active run `34740781222`.

V0.9 has 16 independent hosted science lanes, all started concurrently: control-only neighborhood profiles `2e-11`, `1.5e-11`, `1.2e-11`, exact `1e-11` replica R1, independent exact `1e-11` replica R2, `8e-12`, `6e-12`, each crossed with D/B, plus a full-coordinate independent `TOL300R=1e-12` D/B replication. The exact TOL30 replicas are separate jobs to test reproducibility rather than reusing the V0.8 result.

Frozen decision logic: local reproducible resonance requires both exact TOL30 replicas to violate `1e-3` on the identical nonempty control-coordinate set while every frozen neighboring tolerance is stable; TOL300R must independently satisfy recovery >=75%, median `<1e-3`, controls `<1e-3`, recovered count within 1 of parent TOL300 and median within 1.25x. Only that outcome may authorize a separately frozen stabilized-TOL300 **local** common-grid validation. Broad neighboring instability, nonreproducible TOL30, failed TOL300 replication or invariant failure each route to a diagnostic-only successor.

At the latest recovery write, all 16/16 science lanes are `in_progress`; invariant-audit has passed its scientific identity checks. Do not inspect partial profile numbers before the full barrier.

## Exact next order

1. Continue only V0.9 run `34740781222`; do not duplicate any of its 16 lanes.
2. Consume only terminal artifacts; do not retune neighborhood points or thresholds from partial output.
3. After all lanes close, apply only the frozen V0.9 decision job and independently verify artifact provenance.
4. Promote a durable V0.9 authority, then launch only the successor explicitly authorized by the V0.9 classifier.
5. Keep covariance, Wm_S3, global 65537 and science gate closed unless a later separately frozen authority opens them.

## Publication/readiness locks

Last frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; numerical diagnostic progress alone does not change them. Article-II real cross-family G5 ACT×unWISE closure remains a separate unresolved publication gate.

## Automation / ownership

At the latest automation check, QGR, MSQGR, KMQGB and RQIR-CG are enabled hourly; ISQGR is disabled, leaving one active-task slot available. `DSIR Continuous Research` may therefore be re-enabled without disabling another project. `DSIR Auto-Research Guard` remains disabled to avoid a duplicate DSIR control plane.

V0.9 is GitHub-hosted diagnostic compute, not a new self-hosted `DSIR-HOME-PC` heavy-science run.
