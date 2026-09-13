# DSIR authoritative recovery — latest

Updated: 2026-09-13. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, terminal GitHub Actions artifacts and this file are the source of truth. Older recovery notes are immutable history and must not reopen superseded Layer-B work.

## Frozen scientific boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; native `k_per_decade_for_pk=20`; response threshold `<1e-3`; exact/requested-node mismatch `<=1e-12`; production `perturb_sampling_stepsize=0.00035`; stabilized `tol_perturb_integration=1e-12`. Covariance/whitening/nuisance/relation-null remain unopened; `Wm_S3` unopened; global 65537 unauthorized; no science gate opened by this chain.

## Closed chain through V0.10

V0.5: `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`.

V0.6: `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`; Richardson recovered only 4/20.

V0.7: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, attribution `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`; sampling-only tightening had no material recovery.

V0.8: `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`; TOL300/TOL1000 reached 16/20 but TOL30=`1e-11` produced one unstable control.

V0.9 authority `docs/dsir4/authority/LAYERB_BETA_TOL30_RESONANCE_V0_9.json`, run `34740781222`: `REPRODUCIBLE_LOCAL_TOL30_CONTROL_RESONANCE_WITH_REPLICATED_TOL300`. Independent TOL300R=`1e-12` reproduces 16/20 recovery, median `0.000510732305940965`, control max `5.0840057663462765e-05`.

V0.10 authority `docs/dsir4/authority/LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_V0_10.json`, run `34741342346`: `STABILIZED_TOL300_LOCAL_COMMON_GRID_NOT_VALIDATED`. GRID512 recovers 16/20; GRID1024 14/20. Maximum GRID512-vs-GRID1024 response discrepancy is `0.0108331289703319` at `h=2.5e-5`, while GRID1024-vs-direct at production h is only `0.00010217977189246786`. This authorized only discrepancy localization.

## V0.11 — terminal common-grid discrepancy localization

Authority: `docs/dsir4/authority/LAYERB_BETA_COMMON_GRID_DISCREPANCY_V0_11.json`, creation commit `2621e0ab74685e502e7cec53997c58f99e354085`.

Run `34748453026`, head `1a2825cdb91319f9da13a2b446f3cc0447d1690c`; decision job `103701429242`; decision artifact `10314413873`, ZIP SHA256 `21500360580263f9e9b81c362b8adbc4290880446f4014745c983c1022a38fee`.

Classification: `PRODUCTION_H_COMMON_GRID_DISCREPANCY_SUPPORTED`, effect `+0/+0`. All keysets exact, unsupported targets zero, max requested-node mismatch `1.6564666256119906e-16`, invariant PASS.

Resolution path versus independent direct TOL300:

- `GRID512`: adequate, 16/20 recovered, production-h max response difference `0.0003587116277798966`.
- `GRID640`: adequate, 15/20; production-h max `0.0004402359888879361`, but one `h=2e-4` violation `0.003709335890188209` at `[F,D,3fe43d70a3d70a3e,3f900ea7bc915d36]`.
- `GRID768`: adequate, 15/20; production-h violation `0.004037659729341879` at `[F,D,3fdab851eb851eb8,3f890e66b051e28b]`.
- `GRID896`: adequate, 15/20; production-h violation `0.0011351878950117023` at `[F,D,3fe3d70a3d70a3d7,3f8fc70971921840]`.
- `GRID1024`: inadequate, 14/20; production-h max only `0.00010217977189246786`, but smallest-h max `0.010699084577323596`.

The discrepancy is sparse and resolution/coordinate-specific, not a uniform common-grid failure. Because violations occur at or above production h, V0.11 authorizes only `PROSPECTIVELY_FROZEN_PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT` and explicitly does not authorize full Layer-B promotion.

## V0.12 — active production-h common-grid interpolation audit

Executor: `ci/layerb_beta_production_h_common_grid_interpolation_v0_12.py`, final pre-execution commit `ad22203c29a448b3c0282649b72e491fc123b286`, blob `aedd509780786f1efc200710e572c0af848cd878`.

Prospectively frozen contract: `docs/dsir4/contracts/LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_V0_12.json`, final pre-execution identity commit `d15999917dca48553840468ea4edbce6bd6f1b02`.

Workflow: `.github/workflows/layerb-beta-production-h-common-grid-interpolation-v0-12.yml`, creation commit `46574e6da1bc282f3480ac922a19ca4c67a623fe`.

Launch commit `0daf43908e276482eb3b02e45d9d93af02bc43f2`; active run `34749034836`.

V0.12 computes five independent hosted lanes: `GRID512`, `GRID640`, `GRID768`, `GRID896`, `GRID1024`. Each lane tests the same three frozen D-domain coordinates at `h=2e-4` and `h=1e-4`. Every lane performs a pure common-grid invocation and a mixed invocation that adds all three exact target-k values while retaining the original common-grid nodes. The mixed invocation therefore permits an apples-to-apples comparison between cubic interpolation over the original stencil and the exact target returned by the same solver invocation.

There are 30 preregistered grid/h/target cells. Every pure-grid cell must replay the immutable V0.10/V0.11 parent response within `1e-5`. The three parent violation cells are fixed before execution and may not be changed. The classifier distinguishes: cubic interpolation mechanism supported; k-output node-set solver dependence supported; mixed mechanism; parent violations not reproduced; unresolved target-stencil geometry; or invariant failure.

No full 107-row Layer-B traversal, covariance, Wm_S3, global 65537 or science gate is authorized by V0.12.

At the latest write GitHub has created run `34749034836`; it is queued for hosted-runner capacity. Do not inspect partial science results or launch duplicate lanes.

## Exact next order

1. Continue only V0.12 run `34749034836`.
2. Let invariant and all five grid lanes finish; do not use partial numeric output to alter the frozen classifier.
3. Consume the single decision artifact and verify immutable parent artifact provenance.
4. Write a durable V0.12 authority.
5. Launch only the successor encoded by the terminal V0.12 decision.
6. Keep covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537, full 107-row traversal and science gate closed unless a later prospectively frozen authority explicitly opens them.

## Publication/readiness locks

Frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; diagnostic progress alone does not change them. Article-II real cross-family G5 ACT×unWISE remains a separate unresolved publication gate.

## Automation / ownership

Repository/Actions state wins over any stale automation prompt. DSIR scheduled automation must not be assumed enabled unless a later explicit task-state check confirms it. Avoid a duplicate DSIR control plane while this chat is actively advancing V0.12.

V0.12 is GitHub-hosted diagnostic compute, not a self-hosted `DSIR-HOME-PC` heavy-science run.
