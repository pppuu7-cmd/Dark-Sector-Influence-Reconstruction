# DSIR authoritative recovery — latest

Updated: 2026-09-12. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-12_ARTICLE3_CLEAN_RAM_REFERENCE_CONTROL_V139.md`, creation commit `48d684ce3ac0285fa9b1fcc1ca5444771664cd34`. V138 and all earlier recovery notes remain immutable history; V139 supersedes them for current-front recovery.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No 16385->32769 scientific execution is authorized or has occurred. `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`. No real durable resource authority, actual live-guard PASS or current-run authorization exists. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## V139 current result
V138's added-swap probes remain valid infrastructure/resource evidence only and are now explicitly interpreted narrowly: they rule out the tested standard-hosted +8/+12 GiB added-swap routes as successful resource routes, but cannot establish failure on a sufficiently large physical-RAM machine or an exact RAM minimum.

To remove that confound, V139 prospectively froze a clean-RAM reference-only control:
- contract `docs/dsir4/contracts/LAYERB_32769_CLEAN_RAM_REFERENCE_CONTROL_CONTRACT_V0_1.json`, blob `eec2eed8dc9af0b1bf0320ef310fe362e8172910`;
- dormant workflow `.github/workflows/layerb-32769-clean-ram-reference-control-v0-1.yml`, blob `59dcf6886512f5f6a1076c9196801477c0642347`;
- exactly one `reference` role;
- isolated `[dsir-32769-highmem]` runner with frozen `--no-default-labels` provenance;
- `MemTotal >= 62914560 kB` as a nominal-64-GiB-class control envelope, not an inferred minimum;
- `SwapTotal == 0` before compute;
- workflow does not mutate swap;
- same frozen canonical 32769 nodes, CLASS commit, point capacity `32769`, parser capacity `1048576`, and probe blob `f8776ae1e9e0c325f1a3f5f01b4388e1c93ef7e2`;
- no scientific transfer-value readout, no convergence metric, no scientific authority, no successor authorization.

Independent static/synthetic audit run `34663080404` passed three parallel lanes plus finalizer: jobs `103469460283`, `103469460241`, `103469460205`, final `103469483188`. Artifact `10287942224`, ZIP SHA256 `ff80beaa01c62fd5ae471255da38eca534f70e80f96366596804f2d7a1ae3161`; raw `summary.json` SHA256 `cdbbde5ea8d6ff6a534d8cd8fbd7ca0e0aa6795e3f75c54bba4868be894ff718`. The raw artifact was consumed and confirms `requires_real_runner=true`, `clean_reference_execution_authorized=false`, `scientific_execution_authorized=false`.

Durable authority: `docs/dsir4/authority/LAYERB_32769_CLEAN_RAM_REFERENCE_CONTROL_STATIC_AUDIT_V0_1.json`, creation commit `b30cde8957583258e8cfa0cd9daf908352ee838e`, blob `3ddf7095540129febcb0c5612f00970e32b214c2`.

## Retained parser-corrected downstream plane
V137 remains applicable below the real resource gate: V0.3 isolated source/independent consumer, candidate packaging/materialization V0.2, promotion V0.2, live guard/one-run authorizer V0.2, dormant scientific wrapper/workflow V0.2 and terminal consumer V0.2 remain prospectively prepared and independently audited. Frozen science and strict `<1e-3` classifier are unchanged.

## Exact remaining order
1. Attach/configure one real isolated runner with unique name, frozen configurator, `--no-default-labels`, exact label `dsir-32769-highmem`, `MemTotal >= 62914560 kB`, `SwapTotal == 0` before runner start.
2. Dispatch exactly one clean-RAM reference-only control and consume its artifact.
3. Only a clean-reference PASS permits a new prospective decision on the full four-role V0.3 resource lifecycle; it does not auto-authorize it.
4. Real four-role lifecycle PASS must traverse independent consumer V0.3 -> candidate packaging/materialization V0.2 -> promotion V0.2 -> exact durable resource authority.
5. Only then may live guard/current-run authorizer V0.2 permit exactly one canonical 16385->32769 scientific execution, followed by terminal consumer V0.2.

Old superseded run `34550495778` / job `103112190909` remains queued on generic `[self-hosted, Linux, X64]` and must not receive the dedicated runner.

## Readiness
Frozen repository/publication rubric: **ARTICLE3_REPOSITORY_READINESS: 68%**.

Funnel-freeze/scientific frontier: **67%**.

Operational roadmap: **WORKING_PLAN_COMPLETION: 89%**. Increase from V138 is operational only: the swap-confound concern has been converted into a frozen, independently audited clean-RAM reference control. Scientific convergence remains open.

## Exact next action
Do not run more standard-hosted swap experiments. Do not run the four-role lifecycle first. Attach a qualifying physical high-memory runner with swap disabled and execute exactly one clean-RAM `reference` control. Production science remains forbidden.

`DSIR Continuous Research` remains enabled hourly. Repository state and live Actions ownership are authoritative.
