# Research log — 2026-09-08 — GA active guard + C2 HB implementation anchors

Scope: DSIR only. RTK/RQIR excluded.

## GitHub Actions guard

Fresh Actions inspection found exactly one `in_progress` workflow and zero queued workflows.

- Exp073GA / `WW_S3_S3` recovery run: `34197207582`
- head SHA: `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`
- hosted audit job: `101967492875` — `SUCCESS`
- home-science job: `101967543808` — `IN_PROGRESS`
- active step: frozen `WW_S3_S3` A/B gate with durable checkpoints
- queued workflows: `0`

No new terminal failure is present. The active heavy computation was therefore not cancelled, rerun or duplicated. In-progress output is not treated as scientific evidence and was not numerically interpreted.

The previous Exp073GA post-compute pruner failure remains classified `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, not scientific FAIL. The existing recovery continues from the durable Replica-A authority boundary rather than intentionally repeating that completed expensive replica.

## Scientific status preserved

- `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`
- `WW_S3_S3 = NOT_YET_ADMITTED / ACTIVE_HEAVY_GATE`
- new scientific FAIL in this guard iteration: `0`

A candidate GA PASS, if produced, still requires separate frozen Exp073GB provenance admission before `ww_s3_s3_authority_created=true` can exist.

## Independent allowed DSIR4 advancement

Because no new GA infrastructure error was detected and GA retains exclusive ownership of home-heavy work, only the independent hosted/static C2 preparation branch was advanced.

Pinned upstream source inspection resolved the exact implementation anchors needed before the frozen Exp073HB build/static audit:

- NDF15 accepted terminal state is `ynew`; final-step logic reaches exact `tnew=tfinal`; the direct output branch uses `ynew` only when `tnew==t_vec[next]`, while the alternate branch uses forbidden `interp_from_dif`.
- Native total-matter construction assigns current-gauge `ppw->delta_m=delta_rho_m/rho_m` and `ppw->theta_m=rho_plus_p_theta_m/rho_plus_p_m` before downstream transfer/source transformation.

These anchors are frozen in:

`docs/dsir4/mappings/C2_DIAGNOSTIC_EXACT_ENDPOINT_IMPLEMENTATION_ANCHORS_V0_1.md`

Creation commit: `e662adfc836126cf9e6e8e7f53d5e56dc890ae7a`

Blob: `197debe1cf0dad10809974e1309513e260092296`

This is implementation support only: `SUPPORT_PLUS_0_PLUS_0`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

No cosmological run, runtime record, 28-packet/1792-byte payload, mapping, prediction or authority was created. Real C2 runtime remains `BLOCKED_BY_HEAVY_RUN_EXCLUSIVITY` while Exp073GA is active.

## Next permitted actions

1. Primary chain: terminal-consume run `34197207582`; if it yields a valid GA candidate, execute the already frozen separate GB provenance admission. If it fails technically, recover only from the last valid durable artifact/checkpoint and do not classify the infrastructure failure as scientific FAIL.
2. Independent C2: implement the deterministic default-off diagnostic patch and hosted Exp073HB build/static audit against prereg blob `fc5f08889f84e628cb789070abd9179a74ef7e04`. HB itself must execute no cosmological model and create zero runtime payload records.
