# RECOVERY V136 — Article III parser-corrected high-memory resource front

Date: 2026-09-12. Scope: **DSIR Article III only**. V135 and all earlier recovery notes remain immutable history.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`.

No 16385->32769 scientific execution is authorized or has occurred. `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

Frozen scientific semantics remain unchanged: `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, the same physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup mismatch `<=1e-12`.

## New parser/resource result reconciled after V135
The old 32769 parser undercapacity mechanism was corrected by increasing `_ARGUMENT_LENGTH_MAX_` to `1048576`, while retaining point capacity `32769`. The corrected standard-hosted probes no longer support parser undercapacity as the dominant blocker.

Durable resource-only authority: `docs/dsir4/authority/LAYERB_32769_PARSER_1MIB_STANDARD_HOSTED_MEMORY_EXHAUSTION_V0_1.json`, creation commit `74de2c9f49a676315fdab08cf948976f7d541bf2`, classification `LAYERB_32769_PARSER_1MIB_STANDARD_HOSTED_MEMORY_EXHAUSTION_CONFIRMED_PLUS_0_PLUS_0`.

Reference live-memory run `34649988416`, job `103429640299`, on `ubuntu-24.04` measured `MemTotal=16373452 kB`, `SwapTotal=3145724 kB`; last pre-kill sample recorded Python RSS `15663444 kB`, `MemAvailable=0`, `SwapFree=240 kB`, followed by process/runner exhaustion. Separate requested subsets 20481 and 24577 also approached the same resident-memory ceiling, so these are not valid linear memory-scaling points. No numerical 32769 memory requirement is extrapolated.

This is a resource/performance result only (`+0/+0`): no transfer values, scientific responses, convergence metric, covariance gate or Wm_S3 state were created.

## Parser-corrected isolated high-memory V0.3 path
Current dispatch-only source workflow: `.github/workflows/layerb-32769-isolated-highmem-resource-lifecycle-pilot-v0-3.yml`, creation commit `3e8eb465d1f2c59b5d709a901ca99f3adf871ca2`, Git blob `e55c0ab05c6b7eb0d622eadba25d7e20cdc4ce16`.

It preserves the frozen response-blind four-role resource pilot, V135 registration/runtime binding, dedicated `[dsir-32769-highmem]` routing and stale generic-job guard, but updates the execution envelope to:
- parser capacity `1048576`;
- exhausted standard-hosted reference `MemTotal=16373452 kB`;
- physical candidate requirement `MemTotal > 16373452 kB`;
- preferred `33554432 kB` (32 GiB) as execution guidance only, not a scientific parameter and not proof that lower qualifying memory is insufficient.

Independent consumer V0.3: `ci/layerb_32769_resource_lifecycle_independent_consumer_v0_3.py`, creation commit `738cc858359e3f0b792b1fba290e6f90e6798a3c`, Git blob `cb9e83377f7f7c0498f0b2bfc3b8b06c2683d9ab`.

## Independent static closure
Original V0.3 workflow static audit run `34650733720` passed jobs `103432025767` and `103432068065` with source artifact `10282694355` (`sha256:9cc98539451a74121ebd806d295cbeda18c5ab8779a0a31c19b8d2c80b9ede8f`) and independent artifact `10283259037` (`sha256:e06cdc5628c24156918d6b967afd628f4bd1442208922b020b441f8eae8d26c5`).

The audit was then strengthened prospectively to bind the newly added V0.3 independent consumer as well. Audit commit `1c87daaf339ff9dcf0dc40133e5252d9af341ea0`; run `34651919554` passed static job `103435803834` and independent verifier `103435832681`. Static artifact `10284595346`, ZIP SHA256 `7f52b57ae576d8d7bec537e137eb7983afb34e8a91e5bed52eb0e36e37288b05`; independent artifact `10283663788`, ZIP SHA256 `237bae6bdc4f63e47c39d718135316683b99942ee988ef5018166cfb9deef330`.

Durable audit authority: `docs/dsir4/authority/LAYERB_32769_PARSER_CORRECTED_V03_STATIC_CONSUMER_AUDIT_V0_1.json`, creation commit `3ae5ffd46c4a8314a66eac7cb70a59919a95b428`.

These audits create no real high-memory PASS and no scientific authorization.

## Live Actions ownership at V136 creation
A non-scientific standard-hosted response-blind telemetry lane from run `34649988416`, job `103429640191` (`beta_plus`) remains `in_progress`; it is not a canonical scientific 32769 run and must not be interpreted as scientific authority before terminal consumption.

Old superseded self-hosted run `34550495778` / job `103112190909` remains queued on generic `[self-hosted, Linux, X64]`. It must not receive runner ownership. The dedicated future high-memory runner must use the V135 configurator with `--no-default-labels` and only `dsir-32769-highmem`.

## Remaining true blockers
1. Configure/attach a real isolated high-memory runner using `scripts/dsir4/configure_layerb_32769_highmem_runner_v0_1.sh`, with a unique runner name, no default labels, exact custom label `dsir-32769-highmem`, and physical `MemTotal > 16373452 kB`.
2. Dispatch exactly one current V0.3 response-blind measured 32769 lifecycle pilot and obtain real registration/runtime evidence plus resource PASS.
3. V0.3 hosted independent consumer and the existing candidate-packaging/materialization chain must produce a real candidate.
4. V133 exact-byte promotion review must PASS and the reviewed bytes must be deliberately stored as durable resource authority.
5. Immediate one-live guard and current-run-only one-run authorization must PASS.
6. Only then exactly one canonical scientific 16385->32769 run may execute, followed by independent terminal classification.

## Readiness
`ARTICLE3_REPOSITORY_READINESS: 68%`.

Funnel-freeze/scientific frontier: `67%`.

Operational roadmap tracking: `WORKING_PLAN_COMPLETION: 85%`. The increase is operational only: parser undercapacity is removed from the active blocker set and the parser-corrected V0.3 source/consumer path is statically closed. Scientific convergence remains open.

## Exact next action
Terminal-consume any newly terminal standard-hosted telemetry evidence, but do not create a scientific PASS from it. The actual frontier action remains: attach a qualifying isolated high-memory runner and dispatch exactly one V0.3 response-blind resource lifecycle pilot. Do not launch canonical 16385->32769 science before measured resource authority and live one-run authorization exist.
