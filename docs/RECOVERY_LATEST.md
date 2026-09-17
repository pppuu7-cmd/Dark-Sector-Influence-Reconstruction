# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

## Frozen scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain 107 rows = DES 53 + BOSS 54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Full107, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global65537, statistical/model validity and physical dark-sector inference remain closed. Never rerun historical science run `35033268924`, successor v0.1 `35174721773`, successor v0.2 target `35181812498`, failed v0.2 lanes, or any same-identity attempt.

## Terminal v0.2 implementation chain

Response-blind GRID896 diagnostic `35177449482` established `GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED`. Successor v0.2 target `35181812498`, exact head `1fd68a9814ac987300710c4e67d080c7455efa34`, run #1 / attempt #1, terminal failure; decision classification `SENTINEL_INVALID` before numerical/scientific evaluation. Terminal-history `35183519508`, run #1 / attempt #1, terminal success, closed provenance. Numerical/exact-target/scientific/model layers remain `NOT_EVALUATED`.

Terminal v0.2 implementation qualification remains blob `fddc6e08d0bdedcb468a18f749e862ae7c813e38`, verdict `INVALID_IMPLEMENTATION`, classification `SUCCESSOR_SENTINEL_V0_2_PER_LANE_NATIVE_GRID896_MATERIALIZATION_NOT_HOST_INVARIANT`.

## Cross-host GRID896 producer-identity design — frozen and terminally confirmed

Exact design identities:
- canonical source `docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_U64HEX_V0_1.txt`, blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- prereg `docs/dsir4/prereg/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_1.md`, blob `903c80709439cb790bd41316029b218a77d5695b`;
- contract `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_CONTRACT_V0_1.json`, blob `6ba6e5a6c946a1091680f8f44821d323c9a463f3`;
- terminal preexecution confirmation `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_PREEXECUTION_CONFIRMATION_V0_1.json`, blob `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`, verdict `CONFIRMED_SCOPED`.

Canonical source is exact pre-existing response-blind R1 identity data: 897 lowercase u64hex words, source SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`; canonical arithmetic-free producer is unsigned u64 parse + exactly eight little-endian bytes per word = 7176 bytes, SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`. Frozen negative control `corrupted[0] ^= 0x01` has SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800` and must be rejected.

Frozen consumer round-trip is not arbitrary byte identity: every lane must interpret the canonical bytes as contiguous little-endian IEEE-754 binary64 **without arithmetic**, immediately reserialize contiguous little-endian binary64, and require exact byte identity and the same SHA256. Frozen PASS also requires all lane receipts/artifacts and inner hashes to be present and bind run #1 / attempt #1.

## Inert implementation candidate V0.1 — terminal INVALID_IMPLEMENTATION

Reviewed implementation identities:
- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_1.py`, blob `f5e482bfef050796687f4beeb4d3940543681392`;
- inert workflow `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-1.yml`, blob `78aa9d15be46bd2a5222e4618a88e56ed4e4e84c`;
- non-authority implementation manifest blob `c9bd923b0b7531307fe48dc5930c629745a89e37`.

Independent static audit:
`docs/dsir4/audits/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_V0_1.md`, blob `21e9b62b53dccad3e09cb43f0b3a807bd6dbe4c2`, commit `c3fe18679eea52376fbd62e47433b4be1059de6e`.

Terminal implementation qualification:
`docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_QUALIFICATION_V0_1.json`, blob `d9f940f3ea7b41b8df76d102f71ead16342a7f23`, commit `8575ff64dd7bab88a1082d6b61d4e87002b096a8`, verdict `INVALID_IMPLEMENTATION`, classification `GRID896_DIAGNOSTIC_IMPLEMENTATION_DOES_NOT_REALIZE_FROZEN_CONSUMER_ROUNDTRIP_AND_ARTIFACT_PROVENANCE_CONTRACT`.

Auditor handoff:
`docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_V0_1.md`, blob `0abac9f574ae6065234d4acf00a148befdcd668d`, commit `481120da74cf494f9c36a27fb72bdc097ee7dd3f`.

### Defect 1 — consumer operation identity mismatch

The reviewed `consumer_roundtrip()` merely slices raw bytes into 8-byte chunks and concatenates the same chunks. It never performs the prospectively frozen little-endian IEEE-754 binary64 decode and immediate little-endian binary64 reserialization. A real consumer endian/serialization defect can therefore exist while this implementation trivially returns byte-identical output. The implementation cannot earn the frozen PASS.

### Defect 2 — artifact/inner-hash provenance predicate missing

Lane receipts/workflow do not record or terminally bind Actions artifact id/name/digest or inner receipt digest. Aggregate logic parses downloaded `R*.json` files but does not enumerate exact artifact metadata, require exact artifact count/names/ids, verify GitHub artifact digests, or bind outer/inner digests into the decision. A PASS decision could therefore occur without the frozen complete artifact/inner-hash provenance predicate.

Both are pre-execution deterministic implementation defects. No scientific or partial numerical output was used.

Surviving controls remain: exact prereg/contract/canonical/preexecution bindings; arithmetic-free canonical producer; source/payload hashes; fixed negative control; exactly 32 lanes `R01..R32`; no `workflow_dispatch`; run #1 / attempt #1 guards; active-workflow exact-copy guard; future authority and one-shot launch-marker guards; no NumPy/CLASS/scientific-response access. These do not rescue the failed frozen PASS identity.

The reviewed executor/workflow blobs are historical failed candidates and must not be silently modified. The active workflow path `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-1.yml` remains absent and the launch marker remains absent. No diagnostic run was authorized or executed.

## Current authorization state

- cross-host diagnostic design: terminal `CONFIRMED_SCOPED`;
- implementation candidate V0.1: terminal `INVALID_IMPLEMENTATION`;
- corrected inert successor implementation authoring: **authorized and now the only next stage**;
- workflow promotion: **not authorized**;
- launch-marker creation: **not authorized**;
- diagnostic execution: **not authorized**;
- successor sentinel science: **not authorized**;
- full107/downstream science: **not authorized**.

## Funnel position / interpretation ceiling

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED -> V0.5 GOVERNANCE CLOSED -> SUCCESSOR V0.1 CONSUMED -> GRID896 DISPATCH DIAGNOSTIC TERMINAL -> SUCCESSOR V0.2 SENTINEL_INVALID -> V0.2 INVALID_IMPLEMENTATION -> CROSS-HOST GRID896 DESIGN PREREGISTERED -> PREEXECUTION DESIGN CONFIRMED_SCOPED -> INERT IMPLEMENTATION V0.1 FROZEN -> STATIC AUDIT INVALID_IMPLEMENTATION -> CORRECTED INERT SUCCESSOR IMPLEMENTATION REQUIRED -> DIAGNOSTIC EXECUTION CLOSED -> SUCCESSOR SCIENCE CLOSED -> FULL107 CLOSED`.

Interpretation ceiling remains infrastructure/provenance/static implementation. Scientific effect remains `+0/+0`; numerical response reproducibility, exact-target/scientific criteria, covariance, statistical/model validity and physical dark-sector inference remain `NOT_EVALUATED`. No readiness/frontier percentage increase is authorized.

## Exact authorized next stage

`AUTHOR_PROSPECTIVE_CORRECTED_INERT_GRID896_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_ONLY`.

The successor must preserve the frozen design and historical failed candidate while implementing the exact binary64 decode/immediate reserialize consumer control and a terminally verifiable per-lane artifact provenance scheme with exact artifact id/name/digest plus inner receipt digest and exact count/uniqueness/digest rejection rules. Preserve all existing canonical source/payload/negative-control, 32-lane, one-shot and no-science controls. Keep the successor inert outside `.github/workflows`; after freezing its exact identities, perform a fresh independent static audit. Only a later terminal authority may consider promotion/launch. Do not run the diagnostic or any science gate now.
