# DSIR authoritative recovery — latest

Updated: 2026-09-12. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-12_ARTICLE3_PARSER_CORRECTED_HIGHMEM_V136.md`, creation commit `10c2aeddacd43dc11a6aed2407fad8aa8fd13f7b`. V135 and all earlier recovery notes remain immutable history; V136 supersedes them for current-front recovery.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No 16385->32769 scientific execution is authorized or has occurred. `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## V136 closure
The former 32769 parser-under-capacity mechanism is no longer the active resource blocker. Parser capacity is now independently bound at `1048576` while point capacity remains `32769`.

Durable response-blind resource authority `docs/dsir4/authority/LAYERB_32769_PARSER_1MIB_STANDARD_HOSTED_MEMORY_EXHAUSTION_V0_1.json`, creation commit `74de2c9f49a676315fdab08cf948976f7d541bf2`, directly records standard-hosted memory exhaustion after the parser fix. Reference run `34649988416`, job `103429640299`, measured `MemTotal=16373452 kB`, `SwapTotal=3145724 kB`; last pre-kill Python RSS was `15663444 kB` with `MemAvailable=0`, `SwapFree=240 kB`. No numeric high-memory requirement is extrapolated from these data.

Current parser-corrected isolated source workflow is `.github/workflows/layerb-32769-isolated-highmem-resource-lifecycle-pilot-v0-3.yml`, creation commit `3e8eb465d1f2c59b5d709a901ca99f3adf871ca2`, Git blob `e55c0ab05c6b7eb0d622eadba25d7e20cdc4ce16`. Current independent consumer is `ci/layerb_32769_resource_lifecycle_independent_consumer_v0_3.py`, creation commit `738cc858359e3f0b792b1fba290e6f90e6798a3c`, Git blob `cb9e83377f7f7c0498f0b2bfc3b8b06c2683d9ab`.

Strengthened source+consumer static audit commit `1c87daaf339ff9dcf0dc40133e5252d9af341ea0`; run `34651919554` passed jobs `103435803834` and `103435832681`. Static artifact `10284595346`, ZIP SHA256 `7f52b57ae576d8d7bec537e137eb7983afb34e8a91e5bed52eb0e36e37288b05`; independent artifact `10283663788`, ZIP SHA256 `237bae6bdc4f63e47c39d718135316683b99942ee988ef5018166cfb9deef330`.

Durable static authority: `docs/dsir4/authority/LAYERB_32769_PARSER_CORRECTED_V03_STATIC_CONSUMER_AUDIT_V0_1.json`, creation commit `3ae5ffd46c4a8314a66eac7cb70a59919a95b428`.

These results are resource/support-only `+0/+0`; they do not create a real high-memory PASS or scientific authorization.

## Remaining blockers
1. Configure/attach a real isolated high-memory runner using `scripts/dsir4/configure_layerb_32769_highmem_runner_v0_1.sh`, with a unique runner name, `--no-default-labels`, exact custom label `dsir-32769-highmem`, and physical `MemTotal > 16373452 kB`.
2. Dispatch exactly one current V0.3 response-blind measured 32769 lifecycle pilot and obtain real registration/runtime evidence plus measured resource PASS.
3. Hosted independent consumer V0.3 and the unchanged candidate-packaging/materialization chain must produce a real candidate.
4. V133 exact-byte promotion review must PASS and exact reviewed bytes must be deliberately stored as durable resource authority.
5. Immediate one-live guard and current-run-only one-run authorization must PASS.
6. Only then the dormant canonical scientific 16385->32769 workflow may execute and be independently terminal-consumed.

Old superseded run `34550495778` / job `103112190909` remains queued on generic `[self-hosted, Linux, X64]` and must not receive runner ownership.

At V136 reconciliation, standard-hosted response-blind telemetry run `34649988416`, job `103429640191` (`beta_plus`), remains `in_progress`; consume it only after terminal state and never treat it as scientific authority.

## Readiness
Frozen repository/publication rubric remains **ARTICLE3_REPOSITORY_READINESS: 68%**.

Funnel-freeze/scientific frontier remains **67%**.

Operational roadmap tracking is **WORKING_PLAN_COMPLETION: 85%**. The increase is operational only: parser undercapacity is removed from the active blocker set and the parser-corrected V0.3 source/consumer path is statically closed. Scientific convergence remains open.

## Exact next action
Terminal-consume any newly terminal standard-hosted response-blind telemetry evidence. The actual current-front action remains attaching a qualifying isolated high-memory runner and dispatching exactly one V0.3 response-blind lifecycle pilot. Do not launch canonical 16385->32769 science before measured resource authority and live one-run authorization exist.
