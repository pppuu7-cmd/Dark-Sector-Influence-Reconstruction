# DSIR current-process ledger

Updated: 2026-09-17. Scope: **DSIR only**. Repository/Actions state, terminal artifacts and frozen authorities are authoritative; chat is not authority.

## Scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen under prereg blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain 107 rows = DES53+BOSS54; alpha `3e-10`; beta `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Full107, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global65537, statistical/model validity and physical dark-sector inference remain closed. Historical runs `35033268924`, `35174721773`, `35181812498` and failed v0.2 lanes remain consumed and non-rerunnable.

## Terminal v0.2 implementation state

Response-blind diagnostic `35177449482` established `GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED`; exact frozen GRID896 SHA256 is `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`.

Successor v0.2 target `35181812498`, exact head `1fd68a9814ac987300710c4e67d080c7455efa34`, run #1 / attempt #1, is terminal failure. Decision job `105080542988` froze `SENTINEL_INVALID` before numerical/scientific evaluation. Terminal-history `35183519508` succeeded and closed run provenance. Numerical/exact-target/scientific/model validity remains `NOT_EVALUATED`.

Terminal implementation authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SUCCESSOR_SENTINEL_V0_2_TERMINAL_IMPLEMENTATION_QUALIFICATION_V0_1.json`, blob `fddc6e08d0bdedcb468a18f749e862ae7c813e38`, verdict `INVALID_IMPLEMENTATION`, classification `SUCCESSOR_SENTINEL_V0_2_PER_LANE_NATIVE_GRID896_MATERIALIZATION_NOT_HOST_INVARIANT`. Counterexample: `R01` failed exact GRID896 materialization before CLASS while other hosted lanes passed. That authority opened only a prospective response-blind producer-identity diagnostic design.

## Cross-host GRID896 diagnostic design — preregistered and independently confirmed

Exact frozen design identities:

- canonical source `docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_U64HEX_V0_1.txt`, Git blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- prereg `docs/dsir4/prereg/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_1.md`, blob `903c80709439cb790bd41316029b218a77d5695b`;
- contract `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_CONTRACT_V0_1.json`, blob `6ba6e5a6c946a1091680f8f44821d323c9a463f3`.

Canonical source provenance: response-blind static-identity run `34954905127`, workflow `358611729`, exact head `5dc6150191638f48442671395ce4da9e676579b4`, run #2 / attempt #1, job `104334496210`, artifact `10390997654`, Actions ZIP SHA256 `5cd19512bef3d9795957fb8105361e4006123ae59794bc94e2e5ded5722436ff`, inner identity SHA256 `3a9d8375119068063ddcb4ac37d8f3da92444261b0fad356a228ccaedf6292d7`, inner receipt SHA256 `5c6187a03db04888c4e3bd4f6f98befc1d67ae45a0c362fdbb320fe5dcf70f32`.

Canonical producer is arithmetic-free: exactly 897 lowercase u64hex words -> unsigned u64 parse -> exactly eight bytes little-endian per word -> 7176 bytes -> SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`. Source SHA256 is `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`. Frozen negative control `corrupted[0] ^= 0x01` has SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800` and must be rejected.

Independent pre-execution audit `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_PREEXECUTION_AUDIT_V0_1.md`, blob `391848495af22c6c282f91ed70ba64ffdcdf39e8`, found no deterministic source-level counterexample in the frozen design.

Terminal pre-execution authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_PREEXECUTION_CONFIRMATION_V0_1.json`, blob `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`, verdict `CONFIRMED_SCOPED`, classification `CROSS_HOST_GRID896_CONTENT_ADDRESSED_DIAGNOSTIC_DESIGN_PREEXECUTION_CONFIRMED_SCOPED`. It authorized executor/workflow construction only and required a separate independent static pre-launch audit before execution.

## Inert implementation candidate — current gate input

Construction is now complete without launching the diagnostic.

Exact executor candidate:

- `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_1.py`;
- Git blob `f5e482bfef050796687f4beeb4d3940543681392`.

Exact inert workflow candidate:

- `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-1.yml`;
- Git blob `78aa9d15be46bd2a5222e4618a88e56ed4e4e84c`;
- remains outside `.github/workflows` and therefore is not executable in its current location.

Non-authority implementation manifest:
`docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_CANDIDATE_V0_1.json`.

The executor is response-blind and stdlib-only. It accesses no CLASS/scientific response; binds the frozen prereg, contract, canonical object and preexecution authority; reconstructs GRID896 by u64hex -> exact 8-byte little-endian packing only; performs a byte-only 8-byte round-trip; checks exact payload SHA256 and the fixed one-bit negative-control digest; distinguishes missing/unbound canonical object from invalid provenance; freezes lane IDs `R01..R32`; records hosted runtime/job provenance; and emits only infrastructure/provenance classifications.

The inert workflow freezes exactly 32 `ubuntu-24.04` lanes, `fail-fast:false`, no lane replacement, no `workflow_dispatch`, and run #1 / attempt #1 guards. Lane steps preserve receipts even on a frozen non-PASS; the decision step aggregates exactly 32 unique receipts, emits `BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE` for incomplete hosted population, uploads a frozen decision artifact, and never authorizes successor/full107/downstream science.

Runtime code additionally requires any later promoted `.github/workflows/...` file to be byte-identical to the audited candidate, a future terminal implementation authority, and a separately bound one-shot launch marker. The active workflow and launch marker are currently absent.

No independent static implementation audit has yet been performed on these exact code/workflow blobs. Therefore no promotion or launch authority exists.

## Current authorization state

- executor construction: complete;
- inert workflow-candidate construction: complete;
- independent static pre-launch audit: **authorized and required next**;
- workflow promotion: **not authorized**;
- launch-marker creation: **not authorized**;
- diagnostic execution/launch: **not authorized**;
- successor sentinel science: **not authorized**;
- full107/downstream science: **not authorized**.

## Funnel position

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED -> V0.5 GOVERNANCE CLOSED -> SUCCESSOR V0.1 CONSUMED -> GRID896 DISPATCH DIAGNOSTIC TERMINAL -> SUCCESSOR V0.2 EXECUTED / SENTINEL_INVALID -> V0.2 INVALID_IMPLEMENTATION -> CROSS-HOST GRID896 PRODUCER-IDENTITY DIAGNOSTIC V0.1 PREREGISTERED DESIGN -> PREEXECUTION DESIGN CONFIRMED_SCOPED -> INERT EXECUTOR/WORKFLOW IMPLEMENTATION CANDIDATE FROZEN -> INDEPENDENT STATIC PRELAUNCH AUDIT REQUIRED -> DIAGNOSTIC EXECUTION CLOSED -> SUCCESSOR SCIENCE CLOSED -> FULL107 CLOSED`.

Scientific effect stays `+0/+0`; interpretation ceiling is infrastructure/provenance/static implementation only. Numerical response reproducibility, exact-target/scientific criteria, covariance, statistical/model validity and physical dark-sector inference remain `NOT_EVALUATED`. No readiness/frontier increase.

## Exact next admissible action

`INDEPENDENT_STATIC_AUDIT_OF_EXACT_GRID896_DIAGNOSTIC_IMPLEMENTATION_CANDIDATE_ONLY`.

The audit must independently verify executor blob `f5e482bfef050796687f4beeb4d3940543681392`, workflow candidate blob `78aa9d15be46bd2a5222e4618a88e56ed4e4e84c`, all frozen source/authority bindings, exact byte reconstruction and controls, classifier semantics, topology/provenance, 32-lane/no-replacement semantics, one-shot protections, active-workflow exact-copy guard, launch-marker guard and strict no-science boundary. Do not promote the workflow, create the launch marker, execute the diagnostic or open successor science during that audit. If a source-level defect is found, preserve this candidate and require a prospectively corrected candidate rather than mutating the audited bytes post hoc.
