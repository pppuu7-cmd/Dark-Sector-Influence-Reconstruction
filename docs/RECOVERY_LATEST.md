# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

## Frozen scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain 107 rows = DES 53 + BOSS 54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Full107, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global65537, statistical/model validity and physical dark-sector inference remain closed. Never rerun historical science run `35033268924`, successor v0.1 `35174721773`, successor v0.2 target `35181812498`, failed v0.2 lanes, or any same-identity attempt.

Historical control V0.13 run `34773514342` remains terminal success, run #1 / attempt #1; decision job `103769308584` succeeded; decision artifact `10322573705` has digest `sha256:b04db83d530c36e03f2b80ad33fb4be80747817bd08cb2b001d5c8c6375fd202`. Existing frozen classification remains `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`; no new V0.13 authority is required.

## Terminal v0.2 implementation chain

Response-blind GRID896 diagnostic `35177449482` established `GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED`. Successor v0.2 target `35181812498`, exact head `1fd68a9814ac987300710c4e67d080c7455efa34`, run #1 / attempt #1, terminated with `SENTINEL_INVALID` before numerical/scientific evaluation. Terminal-history `35183519508` closed provenance. Numerical/exact-target/scientific/model layers remain `NOT_EVALUATED`.

Terminal v0.2 implementation qualification remains blob `fddc6e08d0bdedcb468a18f749e862ae7c813e38`, verdict `INVALID_IMPLEMENTATION`, classification `SUCCESSOR_SENTINEL_V0_2_PER_LANE_NATIVE_GRID896_MATERIALIZATION_NOT_HOST_INVARIANT`.

## Cross-host GRID896 producer-identity design — frozen

Frozen design identities:
- prereg blob `903c80709439cb790bd41316029b218a77d5695b`;
- contract blob `6ba6e5a6c946a1091680f8f44821d323c9a463f3`;
- canonical source blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- terminal preexecution confirmation blob `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`, verdict `CONFIRMED_SCOPED`.

Canonical source is 897 lowercase u64hex words, source SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`; fixed little-endian u64 binaryization is exactly 7176 bytes, SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`; one-bit negative control SHA256 is `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

Frozen consumer operation is explicit: decode the exact payload as contiguous little-endian IEEE-754 binary64 without arithmetic, immediately reserialize little-endian binary64, and require exact bytes/hash. PASS also requires complete per-lane runtime plus Actions artifact provenance with artifact id/name/digest and inner receipt digest.

## Historical implementation V0.1 — terminal INVALID_IMPLEMENTATION

Historical failed candidate remains immutable:
- executor blob `f5e482bfef050796687f4beeb4d3940543681392`;
- inert workflow blob `78aa9d15be46bd2a5222e4618a88e56ed4e4e84c`;
- implementation manifest blob `c9bd923b0b7531307fe48dc5930c629745a89e37`.

Independent static audit blob `21e9b62b53dccad3e09cb43f0b3a807bd6dbe4c2`; terminal qualification blob `d9f940f3ea7b41b8df76d102f71ead16342a7f23`, verdict `INVALID_IMPLEMENTATION`, classification `GRID896_DIAGNOSTIC_IMPLEMENTATION_DOES_NOT_REALIZE_FROZEN_CONSUMER_ROUNDTRIP_AND_ARTIFACT_PROVENANCE_CONTRACT`; Auditor handoff blob `0abac9f574ae6065234d4acf00a148befdcd668d`.

Defects were deterministic and pre-execution: V0.1 only sliced/rejoined raw 8-byte chunks rather than binary64 decode/reserialize, and its aggregate did not bind outer Actions artifact ids/names/digests plus inner receipt hashes.

## Corrected inert implementation successor V0.2 — CURRENT FRONTIER

The exactly authorized successor-authoring step has been completed without promotion or execution.

Frozen successor identities:
- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_2.py`, blob `69ead98fdaf605b961c7a85570a0cc5770af3750`, creation commit `b85b06818165129268be2a05e7a70f2d91f09383`;
- inert workflow candidate `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-2.yml`, blob `271646639792041eb88a1b5c31a3cd142d1778df`, creation commit `a617f66c656c43e8a19fd648d23a38c2a2a73b79`;
- non-authority successor implementation manifest `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_MANIFEST_V0_2.json`, blob `2d8b8aa8d91817e758edf5fabcdb79d3d53deeca`, commit `1267e880689f03c7a8949398d823eb9690ff8fb7`.

Prospective source-level corrections now frozen for independent audit:
1. `consumer_roundtrip()` uses explicit `struct.iter_unpack("<d", payload)` followed by immediate `struct.pack("<d", value)` with no arithmetic; exact payload byte identity and SHA remain required.
2. Aggregate no longer trusts an extracted receipt directory. It queries current-run Actions artifacts, requires exactly 32 unique expected lane artifact names/ids, downloads each immutable artifact ZIP, requires GitHub `sha256:` digest to equal computed ZIP SHA256, requires exactly one expected `Rxx.json` member, computes its inner SHA256, parses that exact bytestring, and records per-lane artifact id/name/API digest/ZIP SHA256/inner receipt SHA256 in the terminal decision.
3. Aggregate verifies artifact run/head binding and receipt run/run-attempt/job/event/ref/source/contract/executor/workflow bindings; missing population maps to `BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE`; duplicate/extra/malformed/digest-mismatched evidence maps to `INVALID_DIAGNOSTIC_PROVENANCE`.
4. Existing source/hash/negative-control/32-lane/run#1-attempt#1/no-replacement/no-science controls are preserved.

The active workflow path `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-2.yml` is absent. Launch marker `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_2.launch.json` is absent. Therefore no diagnostic run can have been authorized by this successor construction step.

## Current authorization state

- frozen cross-host design: terminal `CONFIRMED_SCOPED`;
- historical implementation V0.1: terminal `INVALID_IMPLEMENTATION`;
- corrected inert implementation successor V0.2: **frozen, not yet independently audited**;
- independent static audit of exact V0.2 executor/workflow blobs: **authorized next and only next stage**;
- workflow promotion: **not authorized**;
- launch-marker creation: **not authorized**;
- diagnostic execution: **not authorized**;
- successor sentinel science: **not authorized**;
- full107/downstream science: **not authorized**.

## Funnel position / interpretation ceiling

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED -> V0.5 GOVERNANCE CLOSED -> SUCCESSOR V0.1 CONSUMED -> GRID896 DISPATCH DIAGNOSTIC TERMINAL -> SUCCESSOR V0.2 SENTINEL_INVALID -> V0.2 INVALID_IMPLEMENTATION -> CROSS-HOST GRID896 DESIGN PREREGISTERED -> PREEXECUTION DESIGN CONFIRMED_SCOPED -> IMPLEMENTATION V0.1 STATIC-AUDIT INVALID -> CORRECTED INERT IMPLEMENTATION SUCCESSOR V0.2 FROZEN -> INDEPENDENT STATIC AUDIT REQUIRED -> DIAGNOSTIC EXECUTION CLOSED -> SUCCESSOR SCIENCE CLOSED -> FULL107 CLOSED`.

Interpretation ceiling remains infrastructure/provenance/static implementation. Scientific effect remains `+0/+0`; numerical response reproducibility, exact-target/scientific criteria, covariance, statistical/model validity and physical dark-sector inference remain `NOT_EVALUATED`. No readiness/frontier percentage increase is authorized.

## Exact authorized next stage

`INDEPENDENT_STATIC_AUDIT_OF_EXACT_GRID896_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_V0_2_ONLY`.

Audit only executor blob `69ead98fdaf605b961c7a85570a0cc5770af3750`, inert workflow blob `271646639792041eb88a1b5c31a3cd142d1778df`, manifest blob `2d8b8aa8d91817e758edf5fabcdb79d3d53deeca`, and their frozen parents. Verify exact binary64 consumer semantics; exact Actions artifact count/name/id/digest and ZIP/inner receipt hash binding; run/head/job provenance; PASS/FAIL/BLOCKED/INVALID logic; 32-lane topology; one-shot guards; no `workflow_dispatch`; active-copy/authority/launch guards; and strict no-science boundary. Do not modify the exact successor during that audit, do not promote, do not create a launch marker, and do not execute any diagnostic or science gate.
