# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_32769_RUNNER_ISOLATION_GUARD_PREP_V129.md`, creation commit `84cce92ed48986e7ae0bc4d30885fa52400b08b0`. V128 and all earlier recovery notes remain immutable history; V129 supersedes them for current-front recovery.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No 16385->32769 scientific execution is authorized. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Closed 32769 prerequisites
Durably closed:
- canonical response-blind 32769 bytes + independent static consumer;
- CLASS point capacity 32769 on pinned commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- parser/build parity 524288;
- static scientific equivalence;
- prospective terminal schema + independent terminal consumer.

`TERMINAL_SCHEMA_AND_INDEPENDENT_CONSUMER_FROZEN=TRUE`.

## High-memory resource route — isolated preparation complete, measured PASS open
Hosted 16385 exhaustion envelope remains `MemTotal=16372440 kB`; no 32769 requirement is extrapolated.

Dedicated isolation contract: `docs/dsir4/contracts/LAYERB_32769_HIGH_MEMORY_RUNNER_ISOLATION_CONTRACT_V0_1.json`, Git blob `d9d910d89889f6d3a27461a73c3dd72c2a9d2096`. It requires a runner configured without default labels and with custom label `dsir-32769-highmem`, so the stale generic self-hosted job `34550495778 / 103112190909` cannot match that isolated route.

Isolated dispatch-only pilot workflow: `.github/workflows/layerb-32769-isolated-highmem-resource-lifecycle-pilot-v0-2.yml`, Git blob `8ec0027d6fb45f3f12aa5f410de62093a7144924`, `runs-on: [dsir-32769-highmem]` only. It still requires physical `MemTotal > 16372440 kB`, fails closed if stale job `103112190909` is concurrently in progress, reads no transfer values and computes no convergence metric/classification.

Static isolation audit run `34633703412`, job `103376415501`, PASS; artifact `10277616865`, ZIP SHA256 `48261fd0da92726eedf3987aa1888510716603222bf6f42ea12d685bec9173d2`, result SHA256 `22c9f5f191f3feae0e481f4c0e3f84ad33f03dae944a145507729ca21f00f363`. Durable authority: `docs/dsir4/authority/LAYERB_32769_ISOLATED_RUNNER_CONTRACT_STATIC_AUDIT_V0_2.json`, creation commit `8f059f3960192f6d7b546be9402e41ffdd792328`.

`HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE` until the real measured pilot succeeds on a qualifying isolated runner.

## One-live guard — implementation frozen, actual PASS open
Guard contract: `docs/dsir4/contracts/LAYERB_32769_ONE_LIVE_GUARD_CONTRACT_V0_1.json`, Git blob `c88836865879e164d5f4599b5e586f148bc2d524`. Guard implementation: `ci/layerb_32769_one_live_guard_v0_1.py`, Git blob `a1f2fa6b38ed95c1873be644b6377f481ffe8bff`.

Synthetic audit run `34633976800` passed job `103377302152` and independent verifier `103377345283`. Artifact `10277072929`, ZIP SHA256 `57fbcfcdb05085e8135aff4136ab7727bd6ddc057f7efeca6078be8e3a82555f`, summary SHA256 `778c5433a326e2904c3ad38e7fdabae4c79546139a4e7ca8c2af91a26885d4b5`. It proves current-run-only PASS and fail-closed rejection of a second queued/in-progress run, any prior completed matching production run, or a snapshot missing the current run.

Durable synthetic authority: `docs/dsir4/authority/LAYERB_32769_ONE_LIVE_GUARD_SYNTHETIC_AUDIT_V0_1.json`, creation commit `4933f03398ccfbc49b90d8255ba4e91c1d7a45dc`.

`ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS=FALSE` until the guard executes against real live GitHub state in the future first canonical production run.

## Remaining true blockers
1. Real isolated runner `dsir-32769-highmem`, no default labels, physical `MemTotal > 16372440 kB`.
2. Measured response-blind 32769 lifecycle PASS and durable resource authority.
3. Immediate actual one-live PASS.
4. Separate one-run authorization binding real resource + guard authorities.
5. Only then one canonical scientific 16385->32769 run + independent terminal consumption.

No available repository/API capability in this cycle can enumerate or reconfigure the user's self-hosted runner registration, so no physical-runner fact is invented.

## Readiness
Frozen repository/publication rubric remains **ARTICLE3_REPOSITORY_READINESS: 68%** and funnel-freeze readiness **67%**.

Operational roadmap tracking is **WORKING_PLAN_COMPLETION: 76%**. The extra preparation is real, but measured resource PASS and actual one-live PASS are not counted as closed.

## Exact next action
Attach/use a qualifying runner under dedicated label `dsir-32769-highmem` with no default labels and dispatch exactly one response-blind V0.2 lifecycle pilot. Until then, only non-biasing dormant production/authorization preparation is permitted; scientific 16385->32769 remains forbidden.
