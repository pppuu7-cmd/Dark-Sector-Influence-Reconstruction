# DSIR recovery V131 — dormant 16385→32769 engine and production workflow

Date: 2026-09-11. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Scientific frontier — unchanged
Canonical 8193→16385 remains independently classified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` against frozen strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, interpolation/domain/masks/107-row accounting, invalid-fraction, retained-dimension, unsupported-target and lookup guards remain unchanged.

No 16385→32769 scientific execution has occurred in V131. No measured 32769 resource PASS exists. No actual live anti-duplication PASS or one-run authorization exists. Covariance restriction remains unauthorized and Wm_S3 remains closed.

## V130 inherited authority
V131 is layered on authoritative V130 (`docs/recovery/RECOVERY_2026-09-11_ARTICLE3_32769_DORMANT_RESOURCE_AUTHORIZATION_CHAIN_V130.md`, creation commit `29598a0c0998faeb6fa214adf6f7e76d58eb00b2`). V130 already prospectively closed canonical 32769 support, CLASS capacity/parser/static equivalence, terminal schema/consumer, isolated high-memory routing, resource independent consumer, resource event-chain, measured-resource materializer implementation, one-live guard implementation and one-run authorizer implementation.

During the V131 work the hourly DSIR automation advanced the repository from V129 to V130. This was reconciled as an operational versioning event, not a scientific deviation: the automation state was compatible with the same frozen route and did not launch scientific 32769. V131 therefore extends rather than overwrites V130.

## Dormant canonical 16385→32769 scientific engine — statically closed
New dormant engine:
- `ci/layerb_16385_to_32769_canonical_one_live_refinement_v0_1.py`;
- creation commit `819ae844afdc479c01dec0603f211bdc12380d95`;
- Git blob `5ae2068d65dd45e0813c75fb795e55aa1bda1d5e`.

The engine is derived from previously validated `ci/post_jm_next_support_canonical_one_live_refinement_v0_1.py`, Git blob `10492520b4a0eb8992e9ccb101a4ccd26127be82`. It adds fail-closed runtime bindings to the measured resource authority, immediate live anti-duplication guard and current-run-only one-run authorization. The scientific request/evaluate/replay/classify core is unchanged except for the prospectively frozen support-rung identities:
- coarse support count `8193 → 16385`;
- fine support count `16385 → 32769`.

Static-equivalence workflow run `34636344054` completed successfully:
- source job `103385069742` — SUCCESS;
- independent verifier `103385131485` — SUCCESS;
- artifact `10278416811`;
- artifact ZIP SHA256 `b3a0d233877971aa849c0bf2e84fed7b11d6f8a39e2e65ecf9944dc584bfc747`;
- result JSON SHA256 `e3847b130d768af05bc90a221fa7df33e6d6f74942ba666ae156e416586d3dd3`;
- classification `LAYERB_16385_TO_32769_DORMANT_ENGINE_STATIC_EQUIVALENCE_PASS_PLUS_0_PLUS_0`.

The audit proved that after normalizing only the two support-count changes, the scientific core is identical to the previous validated engine. `h=1e-4`, strict `REL_TOL=1e-3`, native kpd20, request-plan hashes, request scalar counts, parent 107-row accounting, validity guards and classifier are unchanged. No CLASS solver/scientific response was invoked by the audit.

Durable authority:
`docs/dsir4/authority/LAYERB_16385_TO_32769_DORMANT_ENGINE_STATIC_EQUIVALENCE_V0_1.json`, creation commit `de31e58ce0f2131b6e8731dd38abcd095b119785`.

## Dormant first canonical production workflow — statically closed
Production workflow:
- `.github/workflows/layerb-16385-to-32769-canonical-scientific-v0-1.yml`;
- creation commit `652f5e41f4d8cac45755414662c51a98f3cf8e9a`;
- Git blob `765abe3f6ec0c47392328678fffd5417f2ae4b43`.

Safety/ordering properties frozen before any production run:
- trigger is **only** `workflow_dispatch`; no push/schedule/workflow_run/pull_request trigger;
- canonical-science job routes only to `[dsir-32769-highmem]`;
- durable measured resource authority `docs/dsir4/authority/LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_V0_1.json` is mandatory and currently absent, so production fails closed;
- live anti-duplication guard for the current GitHub run is generated before one-run authorization;
- one-run authorization for the same current run is generated before CLASS build/science;
- authorization permits exactly one canonical run;
- production CLASS build matches the frozen 32769/524288 envelope and does **not** introduce the earlier history-suppression patch;
- canonical supports are exactly frozen 16385 coarse and 32769 fine files;
- the raw scientific result is uploaded and then consumed by a separate hosted `ubuntu-24.04` terminal-consumer job using the prospectively frozen independent terminal consumer.

Production static-audit workflow run `34636665246` completed successfully:
- source job `103386110141` — SUCCESS;
- independent verifier `103386152908` — SUCCESS;
- artifact `10278872102`;
- artifact ZIP SHA256 `85100ccea27bdde8c2e46cef24f280dcaf4970e3b722aea7689f56d1ee546af2`;
- result JSON SHA256 `ccc26cf8d9712fb0c3148707e919159917171d17dc2a2c2d677a64183a856635`;
- classification `LAYERB_16385_TO_32769_PRODUCTION_WORKFLOW_STATIC_AUDIT_PASS_PLUS_0_PLUS_0`.

Durable authority:
`docs/dsir4/authority/LAYERB_16385_TO_32769_PRODUCTION_WORKFLOW_STATIC_AUDIT_V0_1.json`, creation commit `f5021db2b8be593c222704c771b4b6b4ab1e3136`.

A repository Actions reconciliation after workflow creation found no production-workflow run. Therefore the creation/static audit did not trigger scientific execution.

## Technical deviations repaired before live science
Two implementation-level deviations were discovered and repaired before any live high-memory/scientific execution:
1. resource independent consumer initially assumed a different telemetry delimiter and wrong four-role order; final frozen role order is `reference`, `alpha_minus`, `beta_plus`, `beta_minus`, and the corrected consumer passed independent synthetic regression;
2. measured-resource materializer initially lacked an explicit rejection of inputs marked `synthetic_fixture/synthetic_only`; the hardened materializer now rejects synthetic-marked source/consumer/provenance and source-SHA mismatch, with independent synthetic regression PASS.

Neither repair changed any frozen scientific arithmetic, tolerance, finite-difference step, canonical grid, request plan, mask, estimator, accounting or classifier.

## Remaining true blockers
1. A real isolated runner registered for `dsir-32769-highmem`, configured without default labels, with physical `MemTotal > 16372440 kB`.
2. Exactly one measured response-blind V0.2 32769 resource/lifecycle pilot PASS on that runner.
3. Hosted independent consumer and hardened materializer must create the durable **real** resource authority.
4. The immediate live anti-duplication guard must PASS inside the first canonical production run.
5. The one-run authorizer must bind the real resource authority and live guard to that exact current run.
6. Only then may the already-frozen dormant production workflow execute one scientific 16385→32769 refinement and the separate terminal consumer classify it under strict `<1e-3` semantics.

The currently available GitHub connector does not expose runner-administration/enumeration, so no physical runner presence/configuration is inferred or invented.

## Readiness
Frozen publication metrics remain unchanged:
- `ARTICLE3_REPOSITORY_READINESS = 68%`;
- funnel-freeze readiness = `67%`.

Operational roadmap tracking advances from V130 `78%` to **`WORKING_PLAN_COMPLETION = 80%`**. The increment reflects prospectively closed dormant scientific-engine equivalence and dormant production orchestration, not scientific convergence or measured resource closure.

## Exact next permitted action
Attach/use a qualifying isolated `dsir-32769-highmem` runner and dispatch exactly one response-blind V0.2 resource/lifecycle pilot. Until a real measured resource authority exists, do not dispatch the canonical scientific production workflow and do not manufacture live guard/one-run authorization PASS values.
