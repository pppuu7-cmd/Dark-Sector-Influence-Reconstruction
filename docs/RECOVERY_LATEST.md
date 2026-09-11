# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_32769_TERMINAL_CONTRACT_CLOSED_V128.md`, creation commit `e8b55c733103f060609baef18c03b83124949664`. V127 and all earlier recovery notes remain immutable history; V128 supersedes them for current-front recovery.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No 16385->32769 scientific execution is authorized. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Closed 32769 prerequisites
The following are now closed and durable:
- canonical response-blind 32769 bytes + static consumer;
- CLASS point capacity `32769` on pinned CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- parser/build parity at `524288`;
- static scientific-equivalence audit (only capacity constant changes versus validated 18432 tree);
- prospective terminal result schema + independent terminal consumer.

CLASS/build authority: `docs/dsir4/authority/LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_V0_1.json`, Git blob `ec773d9f5cbed652c52c52b5a4fae74efd5ecd0d`.

Terminal contract: `docs/dsir4/contracts/LAYERB_16385_TO_32769_TERMINAL_RESULT_CONTRACT_V0_1.json`, Git blob `c2f4ff4bb6d3555f78d80503ac5bc73c15ebc4d5`. Terminal consumer: `ci/layerb_16385_to_32769_terminal_consumer_v0_1.py`, Git blob `1ce035030e275effa0a323881cb7e13f54395a10`.

Synthetic terminal audit run `34633253098` passed both job `103374944658` and independent verifier `103374993793`. Artifact `10276822455`, ZIP SHA256 `50a0603c85bce78ef361917a6d6bbcac7f0280492c321cedec704de063352e76`, summary SHA256 `ea7b47da886a493e6dbed445d062dcbf53071780cacba6e0e6e0f786f9ba4e4b`. It prospectively proves unchanged strict semantics: `0.000999` can be CONVERGED, exact `0.001` must be NOT_CONVERGED, and a forced CONVERGED label at `0.001` is rejected with `strict_classifier`.

Durable terminal authority: `docs/dsir4/authority/LAYERB_16385_TO_32769_TERMINAL_CONTRACT_V0_1.json`, creation commit `add05df55267ab0e4bbc01de104c501fe427d197`.

Therefore `TERMINAL_SCHEMA_AND_INDEPENDENT_CONSUMER_FROZEN=TRUE`.

## Resource/lifecycle front
The exact exhausted hosted 16385 topology is frozen at `MemTotal=16372440 kB`, `SwapTotal=3145724 kB`, terminal `MemAvailable=0`, `SwapFree=0`; no 32769 memory requirement is extrapolated. Topology authority: `docs/dsir4/authority/LAYERB_CANONICAL_16385_GITHUB_HOSTED_TOPOLOGY_ENVELOPE_V0_1.json`, Git blob `ea97e50650a85d70356d8529673396090980130a`.

A response-blind 32769 high-memory lifecycle pilot is frozen but not dispatched as scientific work. Static audit run `34632908128`, job `103373820112`, passed; artifact `10277300894`, ZIP SHA256 `511e0800f7edeafacb2bf91d28c07305b8dad04e84249bcf311a76ad328d0963`, result SHA256 `c4015bc359ffac0cde1b69a3c5979c16e282bbd6cf1f852860f92c9dd2c929cf`. Durable static authority `docs/dsir4/authority/LAYERB_32769_RESOURCE_CONTRACT_STATIC_AUDIT_V0_1.json`, creation commit `9fb6e7997a28668fbe2deec89a574486eee2e1e6`.

`HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE` until a real measured response-blind 32769 lifecycle pilot succeeds on a candidate with `MemTotal > 16372440 kB`, max one live solver and final live zero.

## Remaining blockers
- `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`;
- `ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS=FALSE` (must be generated immediately before future production dispatch).

Stale superseded generic self-hosted 16385 run `34550495778 / 103112190909` remains queued and must not receive home-runner or future high-memory runner ownership. This is an operational runner-isolation problem, not a scientific route change.

`32769_EXECUTION_AUTHORIZED=FALSE` until the measured resource gate and immediate one-live gate close, followed by a separate one-run authorization.

## Readiness
Frozen repository/publication rubric remains **ARTICLE3_REPOSITORY_READINESS: 68%** and funnel-freeze readiness **67%**.

Operational roadmap tracking is now **WORKING_PLAN_COMPLETION: 75%**. This working-plan number does not rewrite the frozen publication-readiness percentage.

## Exact next action
Resolve runner isolation/cancellation for stale run `34550495778`, then execute exactly one response-blind 32769 resource/lifecycle pilot on a qualifying higher-memory topology. Prepare the one-live anti-duplication guard/dormant production bindings in parallel, but do not mark them PASS before the immediate pre-dispatch check. Do not execute scientific 16385->32769 convergence yet.
