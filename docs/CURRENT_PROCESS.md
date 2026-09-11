# DSIR current-process ledger

Updated: 2026-09-12. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`.

Frozen science remains unchanged: `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, the same physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup mismatch `<=1e-12`.

No 16385->32769 scientific execution is authorized or has occurred. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Parser-corrected 32769 resource front
The old parser-under-capacity mechanism is no longer the active blocker. Durable resource-only authority `docs/dsir4/authority/LAYERB_32769_PARSER_1MIB_STANDARD_HOSTED_MEMORY_EXHAUSTION_V0_1.json`, creation commit `74de2c9f49a676315fdab08cf948976f7d541bf2`, records parser capacity `1048576` and directly observed exhaustion of standard hosted memory.

Reference run `34649988416`, job `103429640299`, measured `MemTotal=16373452 kB`, `SwapTotal=3145724 kB`; the last pre-kill sample recorded Python RSS `15663444 kB`, `MemAvailable=0`, `SwapFree=240 kB`. Requested-node subsets 20481 and 24577 approached the same resident-memory ceiling and therefore are not used for linear memory extrapolation.

This remains `+0/+0` resource/performance evidence only. No scientific transfer values, responses, convergence metric or scientific authority were created.

## Parser-corrected isolated high-memory V0.3 path
Current source workflow: `.github/workflows/layerb-32769-isolated-highmem-resource-lifecycle-pilot-v0-3.yml`, creation commit `3e8eb465d1f2c59b5d709a901ca99f3adf871ca2`, Git blob `e55c0ab05c6b7eb0d622eadba25d7e20cdc4ce16`.

It is dispatch-only and routes only on `[dsir-32769-highmem]`. It preserves the frozen response-blind four-role resource core and V135 runner-registration/stale-job guards, while requiring parser capacity `1048576`, point capacity `32769`, physical candidate `MemTotal > 16373452 kB`; `33554432 kB` (32 GiB) is preferred execution guidance only, not a scientific parameter and not proof that a lower qualifying runner is insufficient.

Independent consumer V0.3: `ci/layerb_32769_resource_lifecycle_independent_consumer_v0_3.py`, creation commit `738cc858359e3f0b792b1fba290e6f90e6798a3c`, Git blob `cb9e83377f7f7c0498f0b2bfc3b8b06c2683d9ab`.

Strengthened source+consumer static audit commit `1c87daaf339ff9dcf0dc40133e5252d9af341ea0`; run `34651919554` passed jobs `103435803834` and `103435832681`. Static artifact `10284595346`, ZIP SHA256 `7f52b57ae576d8d7bec537e137eb7983afb34e8a91e5bed52eb0e36e37288b05`; independent artifact `10283663788`, ZIP SHA256 `237bae6bdc4f63e47c39d718135316683b99942ee988ef5018166cfb9deef330`.

Durable audit authority: `docs/dsir4/authority/LAYERB_32769_PARSER_CORRECTED_V03_STATIC_CONSUMER_AUDIT_V0_1.json`, creation commit `3ae5ffd46c4a8314a66eac7cb70a59919a95b428`.

`HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`: the static closure creates no real high-memory PASS and no scientific authorization.

## Retained prospective chain
V135 runner configurator remains frozen: `scripts/dsir4/configure_layerb_32769_highmem_runner_v0_1.sh`, Git blob `7489deb49b86245cf399d8020b9ac4fdfcac9278`, SHA256 `2cd02d1a7ac58ea3945a435272f03ea1abe2d7e3410191b5a17a9c62e0a297ce`. A qualifying runner must have a unique name, `--no-default-labels`, and exactly `dsir-32769-highmem`.

The real fail-closed chain is:
`frozen runner configuration -> registration/runtime evidence -> V0.3 isolated resource pilot -> hosted independent consumer V0.3 -> API-backed provenance packager -> hardened materializer -> read-only candidate artifact -> exact-byte promotion review -> deliberate durable authority copy -> immediate live guard -> current-run-only one-run authorization -> exactly one scientific run -> independent terminal consumer`.

Dormant scientific engine/workflow remains unchanged and unauthorized. No 32769 scientific production run has been launched.

## Live Actions ownership
At V136 reconciliation, standard-hosted response-blind telemetry run `34649988416`, job `103429640191` (`beta_plus`), remains `in_progress`. It is resource-only and cannot create scientific authority; consume it only after terminal status.

Old superseded self-hosted run `34550495778` / job `103112190909` remains queued on generic `[self-hosted, Linux, X64]`; it must not receive runner ownership. A future dedicated high-memory runner therefore must have no default labels.

## Remaining true blockers
1. Configure/attach a real isolated high-memory runner using the frozen configurator, with unique name, no default labels, exact custom label `dsir-32769-highmem`, and physical `MemTotal > 16373452 kB`.
2. Dispatch exactly one V0.3 response-blind measured 32769 lifecycle pilot and obtain real registration/runtime evidence plus resource PASS.
3. Hosted independent consumer V0.3 and existing candidate-packaging/materialization chain must PASS and produce a real candidate.
4. The candidate must pass V133 exact-byte promotion review, then exact reviewed bytes must be deliberately copied to durable resource authority.
5. Immediate one-live guard and current-run-only one-run authorization must PASS.
6. Only then exactly one canonical scientific 16385->32769 run may execute, followed by independent terminal classification.

## Recovery authority
Newest immutable note: `docs/recovery/RECOVERY_2026-09-12_ARTICLE3_PARSER_CORRECTED_HIGHMEM_V136.md`, creation commit `10c2aeddacd43dc11a6aed2407fad8aa8fd13f7b`.

## Readiness
`ARTICLE3_REPOSITORY_READINESS: 68%`.

Funnel-freeze/scientific frontier: `67%`.

Operational roadmap tracking: `WORKING_PLAN_COMPLETION: 85%`. This is an operational increase only: parser undercapacity is removed from the active blocker set and the parser-corrected V0.3 source/consumer path is statically closed. Scientific convergence remains open.

## Exact next action
Terminal-consume any newly terminal standard-hosted response-blind telemetry evidence. The actual frontier action remains attaching a qualifying isolated high-memory runner and dispatching exactly one V0.3 response-blind resource lifecycle pilot. Do not launch canonical 16385->32769 science before measured resource authority and live one-run authorization exist.

## Automation / ownership
No duplicate DSIR control plane is authorized. Repository state and live Actions ownership govern all future launches.
