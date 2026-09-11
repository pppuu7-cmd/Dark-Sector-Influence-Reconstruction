# DSIR current-process ledger

Updated: 2026-09-11. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged.

No 16385->32769 scientific execution is authorized. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Closed prerequisites
The following 32769 prerequisites are now durable and independently checked:
- response-blind canonical 32769 bytes + static consumer;
- CLASS point capacity `32769` on pinned commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- parser capacity/parity `524288`;
- static scientific-equivalence audit: only the capacity constant differs from the validated 18432 tree;
- prospective terminal result schema + independent terminal consumer.

`TERMINAL_SCHEMA_AND_INDEPENDENT_CONSUMER_FROZEN=TRUE`.

## Resource/lifecycle gate — implementation ready, measured PASS still open
The exhausted hosted 16385 topology is frozen at `MemTotal=16372440 kB`, `SwapTotal=3145724 kB`, terminal `MemAvailable=0`, `SwapFree=0`. No 32769 memory requirement is extrapolated.

A response-blind 32769 lifecycle engine is frozen at `ci/layerb_32769_response_blind_resource_lifecycle_pilot_v0_1.py`, Git blob `11c7d9a1f95d7c1c394dd520f1c4340a4ce397b4`. It constructs four roles sequentially, requires `max_live_instances=1` and final live zero, reads no transfer values, computes no scientific response and no convergence metric/classification.

### Isolated runner routing — V129 prepared
Stale superseded generic self-hosted run `34550495778 / 103112190909` remains queued. To prevent a future higher-memory runner from being captured by that generic `[self-hosted, Linux, X64]` job, V129 freezes a dedicated-label route:
- isolation contract `docs/dsir4/contracts/LAYERB_32769_HIGH_MEMORY_RUNNER_ISOLATION_CONTRACT_V0_1.json`, Git blob `d9d910d89889f6d3a27461a73c3dd72c2a9d2096`;
- required custom label `dsir-32769-highmem`;
- runner configuration requires no default labels;
- isolated dispatch-only workflow `.github/workflows/layerb-32769-isolated-highmem-resource-lifecycle-pilot-v0-2.yml`, Git blob `8ec0027d6fb45f3f12aa5f410de62093a7144924`;
- workflow `runs-on` contains only `dsir-32769-highmem`;
- it fails closed if stale job `103112190909` is concurrently `in_progress`;
- it still requires physical `MemTotal > 16372440 kB`.

Static isolation audit run `34633703412`, job `103376415501`, SUCCESS. Artifact `10277616865`, ZIP SHA256 `48261fd0da92726eedf3987aa1888510716603222bf6f42ea12d685bec9173d2`, result SHA256 `22c9f5f191f3feae0e481f4c0e3f84ad33f03dae944a145507729ca21f00f363`. Durable authority `docs/dsir4/authority/LAYERB_32769_ISOLATED_RUNNER_CONTRACT_STATIC_AUDIT_V0_2.json`, creation commit `8f059f3960192f6d7b546be9402e41ffdd792328`.

`HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE` until an actual isolated higher-memory runner executes the measured pilot successfully.

## One-live anti-duplication guard — implementation frozen, actual PASS open
Prospective initial-run contract `docs/dsir4/contracts/LAYERB_32769_ONE_LIVE_GUARD_CONTRACT_V0_1.json`, Git blob `c88836865879e164d5f4599b5e586f148bc2d524`, freezes future production workflow path `.github/workflows/layerb-16385-to-32769-canonical-scientific-v0-1.yml`. V0.1 is first-run only: any other matching queued, in-progress or completed production run blocks it; retries require a separate future retry contract.

Guard implementation `ci/layerb_32769_one_live_guard_v0_1.py`, Git blob `a1f2fa6b38ed95c1873be644b6377f481ffe8bff`.

Synthetic audit run `34633976800`: job `103377302152` SUCCESS, independent verifier `103377345283` SUCCESS. Artifact `10277072929`, ZIP SHA256 `57fbcfcdb05085e8135aff4136ab7727bd6ddc057f7efeca6078be8e3a82555f`, summary SHA256 `778c5433a326e2904c3ad38e7fdabae4c79546139a4e7ca8c2af91a26885d4b5`.

Synthetic behavior is fail-closed: current-run-only passes; any second queued/in-progress matching run, any prior completed matching production run, or a snapshot missing the current run fails. Durable synthetic authority `docs/dsir4/authority/LAYERB_32769_ONE_LIVE_GUARD_SYNTHETIC_AUDIT_V0_1.json`, creation commit `4933f03398ccfbc49b90d8255ba4e91c1d7a45dc`.

Important: `ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS=FALSE`. Only implementation readiness is closed; actual PASS must be created from live GitHub state in the future first production run.

## Remaining true blockers
1. A real runner isolated under `dsir-32769-highmem`, with no default labels and physical `MemTotal > 16372440 kB`.
2. Measured response-blind 32769 lifecycle PASS and durable independent resource authority.
3. Actual immediate one-live PASS against live production state.
4. Separate one-run authorization binding the real resource + guard authorities.
5. Only then: one canonical scientific 16385->32769 run and independent terminal consumption.

No available repository/API capability in this research cycle can enumerate or reconfigure the user's self-hosted runner registration, so physical-runner facts are not invented.

### Exact next action
Attach/use a qualifying isolated `dsir-32769-highmem` runner and dispatch exactly one V0.2 response-blind lifecycle pilot. Until such a runner exists, only non-biasing dormant production/authorization preparation is permitted. Do not manufacture resource/one-live PASS values and do not execute scientific convergence.

## Automation / ownership
`DSIR Continuous Research` remains enabled hourly. No duplicate heavy science lane is authorized.

## Recovery authority
Newest immutable note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_32769_RUNNER_ISOLATION_GUARD_PREP_V129.md`, creation commit `84cce92ed48986e7ae0bc4d30885fa52400b08b0`.

## Readiness
Frozen publication rubric remains **ARTICLE3_REPOSITORY_READINESS: 68%** and funnel-freeze readiness **67%** because the scientific convergence gate is unchanged.

Operational roadmap tracking: **WORKING_PLAN_COMPLETION: 76%**. The additional point reflects completed isolated-runner routing and one-live guard implementation preparation; measured resource PASS and actual one-live PASS remain open.
