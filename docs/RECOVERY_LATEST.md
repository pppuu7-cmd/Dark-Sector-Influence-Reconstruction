# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

## Frozen scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain 107 rows = DES 53 + BOSS 54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Full107, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global65537, statistical/model validity and physical dark-sector inference remain closed. Never rerun historical science run `35033268924`, successor v0.1 `35174721773`, successor v0.2 target `35181812498`, failed v0.2 lanes, or any same-identity attempt.

Historical control V0.13 run `34773514342` remains terminal success, run #1 / attempt #1; frozen classification remains `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`.

## Terminal successor-sentinel v0.2 implementation chain

Response-blind GRID896 dispatch diagnostic `35177449482` established `GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED`. Successor v0.2 target `35181812498`, exact head `1fd68a9814ac987300710c4e67d080c7455efa34`, run #1 / attempt #1, terminated `SENTINEL_INVALID` before numerical/scientific evaluation. Terminal-history `35183519508` closed provenance. Numerical/exact-target/scientific/model layers remain `NOT_EVALUATED`.

Terminal v0.2 implementation qualification remains blob `fddc6e08d0bdedcb468a18f749e862ae7c813e38`, verdict `INVALID_IMPLEMENTATION`, classification `SUCCESSOR_SENTINEL_V0_2_PER_LANE_NATIVE_GRID896_MATERIALIZATION_NOT_HOST_INVARIANT`.

## Frozen cross-host GRID896 producer/content-addressing design

Frozen design identities:
- prereg blob `903c80709439cb790bd41316029b218a77d5695b`;
- contract blob `6ba6e5a6c946a1091680f8f44821d323c9a463f3`;
- canonical source blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- terminal preexecution confirmation blob `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`, verdict `CONFIRMED_SCOPED`.

Canonical source is 897 lowercase u64hex words, source SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`; fixed little-endian u64 binaryization is exactly 7176 bytes, SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`; one-bit negative control SHA256 is `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

Frozen consumer operation remains: decode exact payload as contiguous little-endian IEEE-754 binary64 without arithmetic, immediately reserialize little-endian binary64 and require exact bytes/hash. Frozen PASS also requires complete per-lane runtime plus Actions artifact provenance.

## Historical implementation V0.1 — terminal INVALID_IMPLEMENTATION

Historical failed candidate remains immutable:
- executor blob `f5e482bfef050796687f4beeb4d3940543681392`;
- inert workflow blob `78aa9d15be46bd2a5222e4618a88e56ed4e4e84c`;
- implementation manifest blob `c9bd923b0b7531307fe48dc5930c629745a89e37`.

Terminal qualification blob `d9f940f3ea7b41b8df76d102f71ead16342a7f23`, verdict `INVALID_IMPLEMENTATION`. Recorded defects: raw-byte slice/rejoin substituted for frozen binary64 decode/reserialize, and outer Actions artifact id/name/digest plus inner receipt digest were not terminally bound.

## Corrected inert implementation successor V0.2 — terminal INVALID_IMPLEMENTATION

Frozen V0.2 identities:
- executor blob `69ead98fdaf605b961c7a85570a0cc5770af3750`;
- inert workflow blob `271646639792041eb88a1b5c31a3cd142d1778df`;
- successor implementation manifest blob `2d8b8aa8d91817e758edf5fabcdb79d3d53deeca`.

Independent static audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_V0_2_STATIC_AUDIT_V0_1.md`, blob `7529240a3fd8053fb7e7e14d22b72e067ad50f75`, commit `15bf568aa04d239016a5506da723f47f02b13f4d`.

Terminal static-audit qualification: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_STATIC_AUDIT_QUALIFICATION_V0_2.json`, blob `effd843587442f1c7bb3e9d7ae1c7ae6a8afd618`, verdict `INVALID_IMPLEMENTATION`, classification `GRID896_DIAGNOSTIC_SUCCESSOR_V0_2_CLASSIFIER_PRECEDENCE_CAN_HIDE_ESTABLISHED_FAIL_OR_INVALID_PROVENANCE_BEHIND_INCOMPLETE_POPULATION_BLOCK`.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_CROSS_HOST_GRID896_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_V0_2_STATIC_AUDIT_V0_1.md`.

V0.2 successfully repairs the two V0.1 defects at source level: exact `struct` binary64 decode/immediate little-endian reserialization is implemented, and aggregate artifact provenance binds exact artifact ids/names/API digest/computed ZIP SHA256/inner receipt SHA256 plus run/head/job/code identities. Existing canonical hash, negative-control, 32-lane, run#1-attempt#1, no-workflow-dispatch, launch/authority and no-science controls survive.

A new deterministic classifier defect prevents execution readiness. `list_run_artifacts()` short-circuits to `PopulationIncomplete` whenever current-run artifact `total_count < 32`, before reading any present receipt or validating any present artifact provenance. This violates the frozen preregistered distinction:

1. `BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE` is allowed only when fewer than 32 receipts are available for infrastructure reasons **without an implementation-level FAIL predicate being established**. A present otherwise-valid lane can establish the frozen FAIL predicate while another lane artifact is missing; exact V0.2 still returns BLOCKED before observing the FAIL.
2. A present malformed or digest-mismatched artifact can coexist with a missing lane; exact V0.2 returns BLOCKED before the present evidence can establish `INVALID_DIAGNOSTIC_PROVENANCE`.

Therefore V0.2 exact blobs are historical failed objects and must not be modified, promoted, launch-marked or executed.

The active workflow path `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-2.yml` remains absent. Launch marker `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_2.launch.json` remains absent. No V0.2 diagnostic run is authorized or executed.

## Current authorization state

- frozen cross-host design: terminal `CONFIRMED_SCOPED`;
- implementation V0.1: terminal `INVALID_IMPLEMENTATION`;
- implementation successor V0.2: terminal static-audit `INVALID_IMPLEMENTATION`;
- prospective corrected inert implementation successor V0.3 authoring: **authorized next and only next stage**;
- workflow promotion: **not authorized**;
- launch-marker creation: **not authorized**;
- diagnostic execution: **not authorized**;
- successor sentinel science: **not authorized**;
- full107/downstream science: **not authorized**.

## Funnel position / interpretation ceiling

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED -> V0.5 GOVERNANCE CLOSED -> SUCCESSOR V0.1 CONSUMED -> GRID896 DISPATCH DIAGNOSTIC TERMINAL -> SUCCESSOR V0.2 SENTINEL_INVALID -> V0.2 INVALID_IMPLEMENTATION -> CROSS-HOST GRID896 DESIGN PREREGISTERED -> PREEXECUTION DESIGN CONFIRMED_SCOPED -> IMPLEMENTATION V0.1 STATIC-AUDIT INVALID -> CORRECTED INERT IMPLEMENTATION SUCCESSOR V0.2 FROZEN -> SUCCESSOR V0.2 STATIC-AUDIT INVALID_IMPLEMENTATION -> DIAGNOSTIC EXECUTION CLOSED -> SUCCESSOR SCIENCE CLOSED -> FULL107 CLOSED`.

Interpretation ceiling remains infrastructure/provenance/static implementation. Scientific effect remains `+0/+0`; numerical response reproducibility, exact-target/scientific criteria, covariance, statistical/model validity and physical dark-sector inference remain `NOT_EVALUATED`. No readiness/frontier percentage increase is authorized.

## Exact authorized next stage

`AUTHOR_PROSPECTIVE_CORRECTED_INERT_GRID896_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_V0_3_ONLY`.

Do not rewrite V0.2. A new successor must enumerate and validate all present artifacts before incomplete-population classification; preserve any established frozen implementation FAIL when another lane is missing; reject present malformed/duplicate/unexpected/digest-mismatched evidence as INVALID even when the population is also incomplete; and use `BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE` only when no FAIL or present INVALID predicate has been established. Preserve all surviving V0.2 controls. After freezing exact V0.3 blobs, run a new independent static audit before any promotion, launch marker, diagnostic execution or science gate.
