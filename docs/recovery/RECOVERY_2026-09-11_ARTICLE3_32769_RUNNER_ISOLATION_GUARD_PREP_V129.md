# DSIR recovery V129 — 32769 runner isolation and one-live guard preparation

Date: 2026-09-11. Scope: **DSIR only**. RTK/RQIR/KMQGB/KMDSB excluded.

## Scientific frontier
Unchanged. Canonical 8193->16385 remains independently classified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No 16385->32769 scientific response was executed or read in V129. Covariance restriction remains unauthorized and Wm_S3 remains closed.

## Existing closed prerequisites retained
- canonical response-blind 32769 bytes + independent consumer;
- CLASS capacity 32769 / parser 524288 / static scientific equivalence;
- terminal result schema + independent terminal consumer, including strict 0.001 boundary behavior.

`TERMINAL_SCHEMA_AND_INDEPENDENT_CONSUMER_FROZEN=TRUE` remains closed.

## Runner-isolation route — prepared and statically validated
The stale superseded generic self-hosted 16385 run `34550495778 / 103112190909` remains queued. Instead of attaching a new higher-memory runner to generic `[self-hosted, Linux, X64]` labels, V129 freezes a dedicated-label isolation route.

Isolation contract:
- `docs/dsir4/contracts/LAYERB_32769_HIGH_MEMORY_RUNNER_ISOLATION_CONTRACT_V0_1.json`;
- Git blob `d9d910d89889f6d3a27461a73c3dd72c2a9d2096`;
- required custom label `dsir-32769-highmem`;
- runner must be configured with no default labels;
- generic `self-hosted`, `Linux`, `X64` labels are forbidden for this isolated route;
- physical `MemTotal` must still be strictly greater than `16372440 kB`;
- no 32769 memory requirement is extrapolated.

Isolated dispatch-only workflow:
- `.github/workflows/layerb-32769-isolated-highmem-resource-lifecycle-pilot-v0-2.yml`;
- creation commit `5e2fc59b7ef83ae66f5900891c409f0962360d39`;
- Git blob `8ec0027d6fb45f3f12aa5f410de62093a7144924`;
- `runs-on: [dsir-32769-highmem]` only;
- no push or schedule trigger;
- queries stale job `103112190909` and fails closed if it is concurrently `in_progress`;
- binds exact canonical/build/isolation identities and the response-blind resource pilot;
- still reads no transfer values and computes no convergence metric/classification.

Static isolation audit:
- workflow run `34633703412`;
- job `103376415501` — SUCCESS;
- artifact `10277616865`;
- artifact ZIP SHA256 `48261fd0da92726eedf3987aa1888510716603222bf6f42ea12d685bec9173d2`;
- result SHA256 `22c9f5f191f3feae0e481f4c0e3f84ad33f03dae944a145507729ca21f00f363`;
- classification `LAYERB_32769_ISOLATED_RUNNER_CONTRACT_STATIC_AUDIT_PASS_PLUS_0_PLUS_0`.

Durable isolation authority:
`docs/dsir4/authority/LAYERB_32769_ISOLATED_RUNNER_CONTRACT_STATIC_AUDIT_V0_2.json`, creation commit `8f059f3960192f6d7b546be9402e41ffdd792328`.

This resolves the design-level ownership conflict but does not create or attach a physical runner. `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE` remains open until measured execution.

## One-live initial-run guard — implementation frozen, actual guard not yet PASS
Prospective guard contract:
- `docs/dsir4/contracts/LAYERB_32769_ONE_LIVE_GUARD_CONTRACT_V0_1.json`;
- Git blob `c88836865879e164d5f4599b5e586f148bc2d524`;
- future production workflow path frozen as `.github/workflows/layerb-16385-to-32769-canonical-scientific-v0-1.yml`;
- V0.1 is initial canonical run only: any other matching queued, in-progress or completed production run blocks it; retries require a separate prospective retry contract.

Guard implementation:
- `ci/layerb_32769_one_live_guard_v0_1.py`;
- Git blob `a1f2fa6b38ed95c1873be644b6377f481ffe8bff`.

Synthetic guard audit run `34633976800`:
- guard-synthetic-audit job `103377302152` — SUCCESS;
- independent-verifier job `103377345283` — SUCCESS;
- artifact `10277072929`;
- artifact ZIP SHA256 `57fbcfcdb05085e8135aff4136ab7727bd6ddc057f7efeca6078be8e3a82555f`;
- summary SHA256 `778c5433a326e2904c3ad38e7fdabae4c79546139a4e7ca8c2af91a26885d4b5`;
- current-run-only synthetic PASS receipt SHA256 `bde703b2e8c9477be074d7d3863648a616b98c5e10b63c0b3b2f07c4f59f5cbc`.

Synthetic behavior:
- current production run only -> PASS;
- other matching queued run -> FAIL;
- other matching in-progress run -> FAIL;
- any prior completed matching production run -> FAIL for initial-run V0.1;
- missing current run in API snapshot -> FAIL.

Durable synthetic authority:
`docs/dsir4/authority/LAYERB_32769_ONE_LIVE_GUARD_SYNTHETIC_AUDIT_V0_1.json`, creation commit `4933f03398ccfbc49b90d8255ba4e91c1d7a45dc`.

Important: `ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS=FALSE` remains open. Only the implementation is frozen. The actual PASS must be produced from live GitHub state inside the future first canonical production run.

## Remaining true blockers
1. A real isolated runner with label `dsir-32769-highmem`, configured without default labels, must exist and have physical `MemTotal > 16372440 kB`.
2. Exactly one response-blind 32769 lifecycle pilot must PASS on that runner and yield durable independent resource authority.
3. Immediately before/inside first production, the real one-live guard must PASS against live GitHub state.
4. Only then may the separate one-run authorization exist and scientific 16385->32769 execute.

No available repository/API capability in this research cycle can enumerate or reconfigure the user's self-hosted runner registration, so no physical-runner fact is invented.

## Readiness
Frozen publication rubric remains:
- `ARTICLE3_REPOSITORY_READINESS = 68%`;
- funnel-freeze readiness = `67%`.

Operational roadmap tracking advances to `WORKING_PLAN_COMPLETION = 76%`. This +1 reflects completed runner-isolation and anti-duplication implementation preparation, not measured resource PASS or actual one-live PASS. The frozen scientific/publication metrics remain unchanged.

## Exact next action
Use/attach a qualifying runner isolated under `dsir-32769-highmem` with no default labels, then dispatch exactly one V0.2 response-blind resource/lifecycle pilot. Until such a runner is available, continue only non-biasing dormant production/authorization preparation; never manufacture `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS` or `ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS`.
