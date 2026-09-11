# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_32769_DORMANT_RESOURCE_AUTHORIZATION_CHAIN_V130.md`, creation commit `29598a0c0998faeb6fa214adf6f7e76d58eb00b2`. V129 and all earlier recovery notes remain immutable history; V130 supersedes them for current-front recovery.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No 16385->32769 scientific execution is authorized. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Closed 32769 prerequisites and dormant machinery
Durably closed and independently checked:
- canonical response-blind 32769 bytes + independent static consumer;
- CLASS point capacity 32769 on pinned commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- parser/build parity 524288 and static scientific equivalence;
- terminal result schema + independent terminal consumer;
- isolated runner route using dedicated label `dsir-32769-highmem`, no default labels, physical `MemTotal > 16372440 kB` required;
- one-live guard implementation + independent synthetic audit;
- independent measured-resource consumer + synthetic regression audit;
- GitHub-native isolated-pilot -> hosted-consumer completion-event chain;
- measured-resource authority materializer + independent synthetic fail-closed audit;
- first-run one-run authorizer + independent synthetic fail-closed audit.

`TERMINAL_SCHEMA_AND_INDEPENDENT_CONSUMER_FROZEN=TRUE`.

## Newly reconciled V130 authorities
Resource consumer authority: `docs/dsir4/authority/LAYERB_32769_RESOURCE_CONSUMER_SYNTHETIC_AUDIT_V0_1.json`, creation commit `84246c4038f599246346ebe908583587295a51d5`; source run/artifact `34634540227 / 10276978722`, ZIP SHA256 `f21252c1f36927ce88ba12c9ad0dd61d1f35168f70e71b51633d231882f10c74`.

Resource event-chain authority: `docs/dsir4/authority/LAYERB_32769_RESOURCE_EVENT_CHAIN_STATIC_AUDIT_V0_1.json`, creation commit `bac1dfd064e338ac119a2bdc754a15a3f799ccf0`; source run/artifact `34635474683 / 10278660102`, ZIP SHA256 `0698491a857a780b3f4ce389767d2d86d3d863921ff9d22f950270d6e9251aa4`.

One-run authorizer synthetic authority: `docs/dsir4/authority/LAYERB_16385_TO_32769_ONE_RUN_AUTHORIZER_SYNTHETIC_AUDIT_V0_1.json`, creation commit `ea810aa8363b7543ba88476e0cc860d409db8875`; run `34635692929`, jobs `103382890526 / 103382929964`, artifact `10278610547`, ZIP SHA256 `b5666dd53718ecd479ace0f3da418ca4f3796c8fb95f4228b84ac6cbcf6804da`, summary SHA256 `c5cb633160de4dd3ade91bd068ea6f59fec06e26db11e895033c554add50693c`. Independent rehash reproduced these values. `actual_one_run_authorization_exists=false` and `scientific_execution_authorized=false` remain explicit.

Measured-resource authority materializer synthetic authority: `docs/dsir4/authority/LAYERB_32769_RESOURCE_AUTHORITY_MATERIALIZER_SYNTHETIC_AUDIT_V0_1.json`, creation commit `1fc8b84e8b3f0b9e2de6a32e3fc4a0e0c97a88ef`; run `34636032375`, jobs `103384017602 / 103384081084`, artifact `10279000641`, ZIP SHA256 `1bbbd2b11131b71d665baeaf501c9643105242c821c984624cb09995139c057e`, summary SHA256 `31288a256a0f8906023b49c37df281e95c12a2293a0052258602b622669d245c`. Independent rehash reproduced these values. Explicit synthetic source/independent/provenance marks and source-SHA mismatch fail closed. `actual_resource_authority_exists=false` and `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE` remain explicit.

## Remaining true blockers
1. Real isolated runner `dsir-32769-highmem`, no default labels, physical `MemTotal > 16372440 kB`.
2. Exactly one measured response-blind V0.2 32769 lifecycle pilot PASS on that runner.
3. Hosted independent consumer + materializer must create durable real measured-resource authority.
4. Actual immediate one-live PASS against live first-production state.
5. Real one-run authorization binding resource + guard authorities to exactly one production run.
6. Only then one canonical scientific 16385->32769 run + independent terminal consumption.

No available repository/API capability in this cycle can enumerate or reconfigure the user's physical self-hosted runner registration, so no physical-runner fact is invented.

## Live ownership
Current reconciliation: useful in-progress lanes = `0`. Exactly one stale superseded self-hosted run remains queued: `34550495778 / 103112190909`; it must not receive home-runner ownership.

## Readiness
Frozen repository/publication rubric remains **ARTICLE3_REPOSITORY_READINESS: 68%** and funnel-freeze readiness **67%**.

Operational roadmap tracking is **WORKING_PLAN_COMPLETION: 78%**. Dormant resource-consumption/materialization/authorization machinery is closed prospectively; measured high-memory execution and real live authorization remain open.

## Exact next action
Attach/use a qualifying runner under dedicated label `dsir-32769-highmem` with no default labels and dispatch exactly one response-blind V0.2 lifecycle pilot. Until then, only non-biasing dormant production wiring/static auditing is permitted; scientific 16385->32769 remains forbidden.
