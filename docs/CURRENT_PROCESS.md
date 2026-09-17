# DSIR current-process ledger

Updated: 2026-09-17. Scope: **DSIR only**. Repository/Actions state, terminal artifacts and frozen authorities are authoritative; chat is not authority.

## Scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen under prereg blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain 107 rows = DES53+BOSS54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Full107, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global65537, statistical/model validity and physical dark-sector inference remain closed. Historical runs `35033268924`, `35174721773`, `35181812498` and failed v0.2 lanes remain consumed and non-rerunnable.

## Terminal v0.2 implementation state

Response-blind diagnostic `35177449482` established `GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED`. Successor v0.2 target `35181812498`, exact head `1fd68a9814ac987300710c4e67d080c7455efa34`, run #1 / attempt #1, terminal failure with `SENTINEL_INVALID` before numerical/scientific evaluation. Terminal-history `35183519508` succeeded and closed run provenance. Numerical/exact-target/scientific/model validity remains `NOT_EVALUATED`.

Terminal implementation qualification `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SUCCESSOR_SENTINEL_V0_2_TERMINAL_IMPLEMENTATION_QUALIFICATION_V0_1.json`, blob `fddc6e08d0bdedcb468a18f749e862ae7c813e38`, verdict `INVALID_IMPLEMENTATION`, opened only a prospective response-blind cross-host GRID896 producer-identity diagnostic design.

## Frozen cross-host GRID896 design

Exact design identities remain:
- prereg `docs/dsir4/prereg/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_1.md`, blob `903c80709439cb790bd41316029b218a77d5695b`;
- machine contract `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_CONTRACT_V0_1.json`, blob `6ba6e5a6c946a1091680f8f44821d323c9a463f3`;
- canonical source `docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_U64HEX_V0_1.txt`, blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- terminal preexecution confirmation blob `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`, verdict `CONFIRMED_SCOPED`.

Canonical source remains exactly 897 lowercase u64hex words, source SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`; canonical arithmetic-free producer yields exactly 7176 bytes with SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`; frozen one-bit corruption has SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

The frozen consumer operation is explicit: interpret the exact bytes as contiguous little-endian IEEE-754 binary64 with no arithmetic, immediately reserialize little-endian binary64, and require byte-for-byte identity and the same SHA256. Frozen PASS also requires complete receipts/artifacts and inner hashes binding run #1 / attempt #1.

## Implementation candidate V0.1 — terminal static audit INVALID_IMPLEMENTATION

Reviewed candidate identities:
- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_1.py`, blob `f5e482bfef050796687f4beeb4d3940543681392`;
- inert workflow `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-1.yml`, blob `78aa9d15be46bd2a5222e4618a88e56ed4e4e84c`;
- implementation manifest blob `c9bd923b0b7531307fe48dc5930c629745a89e37`.

Independent static audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_V0_1.md`, blob `21e9b62b53dccad3e09cb43f0b3a807bd6dbe4c2`, audit commit `c3fe18679eea52376fbd62e47433b4be1059de6e`.

Terminal qualification authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_QUALIFICATION_V0_1.json`, blob `d9f940f3ea7b41b8df76d102f71ead16342a7f23`, authority commit `8575ff64dd7bab88a1082d6b61d4e87002b096a8`, verdict `INVALID_IMPLEMENTATION`, classification `GRID896_DIAGNOSTIC_IMPLEMENTATION_DOES_NOT_REALIZE_FROZEN_CONSUMER_ROUNDTRIP_AND_ARTIFACT_PROVENANCE_CONTRACT`.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_V0_1.md`, blob `0abac9f574ae6065234d4acf00a148befdcd668d`, handoff commit `481120da74cf494f9c36a27fb72bdc097ee7dd3f`.

Two deterministic implementation defects are terminally recorded:

1. `consumer_roundtrip()` only slices raw bytes into 8-byte chunks and rejoins them; it does not perform the preregistered little-endian IEEE-754 binary64 decode + immediate little-endian reserialization. The reviewed implementation can therefore false-PASS a defect in the actual frozen consumer path.
2. Lane receipts/aggregate logic do not bind future Actions artifact ids/names/digests or inner receipt digests and do not enumerate/verify exact outer artifact metadata. The reviewed workflow can therefore emit PASS without satisfying the frozen complete artifact/inner-hash provenance predicate.

Surviving controls remain useful but insufficient for PASS: exact source/prereg/contract/preexecution bindings, canonical u64 little-endian producer, exact payload hash, frozen negative control, exactly 32 lanes `R01..R32`, no `workflow_dispatch`, run #1 / attempt #1 guards, active-workflow exact-copy guard, future authority/launch-marker guards, and strict no-CLASS/no-science boundary.

The failed executor/workflow blobs are historical and must not be rewritten. The active workflow path remains absent and the launch marker remains absent; no diagnostic run has been authorized or executed.

## Current authorization state

- frozen design: terminal `CONFIRMED_SCOPED`;
- implementation candidate V0.1: terminal `INVALID_IMPLEMENTATION`;
- corrected inert successor implementation authoring: **authorized next**;
- workflow promotion: **not authorized**;
- launch-marker creation: **not authorized**;
- diagnostic execution: **not authorized**;
- successor sentinel science: **not authorized**;
- full107/downstream science: **not authorized**.

## Funnel position

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED -> V0.5 GOVERNANCE CLOSED -> SUCCESSOR V0.1 CONSUMED -> GRID896 DISPATCH DIAGNOSTIC TERMINAL -> SUCCESSOR V0.2 SENTINEL_INVALID -> V0.2 INVALID_IMPLEMENTATION -> CROSS-HOST GRID896 DESIGN PREREGISTERED -> PREEXECUTION DESIGN CONFIRMED_SCOPED -> INERT IMPLEMENTATION V0.1 FROZEN -> STATIC AUDIT INVALID_IMPLEMENTATION -> CORRECTED INERT SUCCESSOR IMPLEMENTATION REQUIRED -> DIAGNOSTIC EXECUTION CLOSED -> SUCCESSOR SCIENCE CLOSED -> FULL107 CLOSED`.

Scientific effect remains `+0/+0`; interpretation ceiling remains infrastructure/provenance/static implementation. Numerical response reproducibility, exact-target/scientific criteria, covariance, statistical/model validity and physical dark-sector inference remain `NOT_EVALUATED`. No readiness/frontier increase is authorized.

## Exact next admissible action

`AUTHOR_PROSPECTIVE_CORRECTED_INERT_GRID896_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_ONLY`.

The successor must implement the exact frozen binary64 consumer decode/reserialize control, add terminally verifiable per-lane artifact id/name/digest plus inner receipt-digest provenance with exact count/uniqueness/digest checks, preserve all existing canonical/negative-control/32-lane/one-shot/no-science guards, remain inert outside `.github/workflows`, and then undergo a fresh independent static audit. Do not promote or execute during successor construction/review.
