# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_32769_RUNNER_REGISTRATION_PROVENANCE_V135.md`, creation commit `e9a1ea249573d527e3d8cc6b757645aec9b981a4`. V134 and all earlier recovery notes remain immutable history; V135 supersedes them for current-front recovery.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No 16385->32769 scientific execution is authorized or has occurred. `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## V135 closure
V135 found and closed a real provenance gap: the prior resource lane required a future `dsir-32769-highmem` runner configured with `--no-default-labels`, but did not independently bind that configuration to the actual executing Actions job.

Frozen configurator `scripts/dsir4/configure_layerb_32769_highmem_runner_v0_1.sh`, Git blob `7489deb49b86245cf399d8020b9ac4fdfcac9278`, SHA256 `2cd02d1a7ac58ea3945a435272f03ea1abe2d7e3410191b5a17a9c62e0a297ce`, now performs the exact dedicated-label/no-default-label configuration and emits a sanitized non-secret registration receipt.

Current source resource workflow `.github/workflows/layerb-32769-isolated-highmem-resource-lifecycle-pilot-v0-2.yml` is now Git blob `3297a556299daf75e4c7ff15f8e56586e45ebdf0`. Its scientific/resource core identities remain unchanged, but it now binds the receipt to the live job's `runner_id`, `runner_name` and exact dedicated routing labels, then hashes registration/runtime evidence into `result.json`.

Registration-aware independent consumer `ci/layerb_32769_resource_lifecycle_independent_consumer_v0_2.py`, Git blob `e08f15394ba3b16222b62d061a621e24f3a857ec`, revalidates those bindings together with all earlier canonical/capacity/memory/lifecycle/response-blind checks. The event-chain workflow remains name/path-compatible with the existing V132 candidate packager; current workflow blob `a68148e6826cda223368f8a624014a873cd1dc44`.

Audit run `34645311690` passed synthetic consumer job `103414563351`, static source-workflow job `103414563197`, and independent verifier `103414777148`. Synthetic artifact `10281202698`, ZIP SHA256 `8206c140aefba57a892ab4adb366bf315b8477c911fc78f4850c2b7b163b4fa0`; static artifact `10281867381`, ZIP SHA256 `7e7cf6b1ffc31c8ed23bde5aae891f1572c63ec17d20eab03e55446de2bc2d6b`.

The valid registration-bound fixture passed. `no_default_labels=false`, wrong configurator hash, generic-label insertion, runner-id mismatch and routing-label substitution were independently rejected. Scientific/resource core blobs were confirmed unchanged.

Durable authority: `docs/dsir4/authority/LAYERB_32769_RUNNER_REGISTRATION_PROVENANCE_AUDIT_V0_1.json`, creation commit `6c6d9e82db30a5dadc5295b7e615822730df1a49`.

## Remaining blockers
1. Configure/attach a real qualifying runner using the V135 frozen configurator, with a unique new runner name and physical `MemTotal > 16372440 kB`.
2. Dispatch exactly one current V0.2 response-blind 32769 lifecycle pilot and obtain real V135 registration/runtime evidence plus measured resource PASS.
3. Hosted independent consumer V0.2 and the unchanged candidate-packaging/materialization chain must produce a real candidate.
4. V133 exact-byte promotion review must PASS and the exact reviewed candidate bytes must be deliberately stored as durable resource authority.
5. Immediate one-live guard and current-run-only one-run authorization must PASS.
6. Only then the dormant canonical scientific 16385->32769 workflow may execute and be independently terminal-consumed.

Old superseded run `34550495778` / job `103112190909` remains queued on generic `[self-hosted, Linux, X64]`. The new runner must therefore have no default labels. The V135 source workflow fails closed if the stale job is observed `in_progress`.

## Automation state
`DSIR Continuous Research` is currently **disabled**. It was not re-enabled in V135.

## Readiness
Frozen repository/publication rubric remains **ARTICLE3_REPOSITORY_READINESS: 68%**.

Funnel-freeze/scientific frontier remains **67%**.

Operational roadmap tracking is **WORKING_PLAN_COMPLETION: 84%**. V135 closes runner-registration provenance prospectively; measured resource execution and scientific convergence remain open.

## Exact next action
Configure the high-memory runner using `scripts/dsir4/configure_layerb_32769_highmem_runner_v0_1.sh`, start it, then dispatch exactly one current V0.2 response-blind lifecycle pilot. Do not launch canonical 16385->32769 science before measured resource authority and live one-run authorization exist.
