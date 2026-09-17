# DSIR Funnel Auditor — cross-host GRID896 diagnostic implementation static audit V0.1

Date: 2026-09-17. Scope: DSIR only. GitHub repository/Actions are the sole durable scientific source of truth.

Reviewed main: `6a2ed1b7a8ee012f74fd4f163c5199669553d434`.

Reviewed exact inert implementation candidate:
- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_1.py`, blob `f5e482bfef050796687f4beeb4d3940543681392`;
- inert workflow `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-1.yml`, blob `78aa9d15be46bd2a5222e4618a88e56ed4e4e84c`;
- implementation manifest blob `c9bd923b0b7531307fe48dc5930c629745a89e37`.

Governing frozen design:
- preregistration blob `903c80709439cb790bd41316029b218a77d5695b`;
- machine contract blob `6ba6e5a6c946a1091680f8f44821d323c9a463f3`;
- canonical source blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- terminal pre-execution confirmation blob `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`.

No diagnostic execution was performed. The active workflow path and one-shot launch-marker path are absent on current main, and recent Actions state contains no run of this inert candidate.

## Authorization and chronology

The terminal pre-execution authority authorizes executor/workflow construction followed by one independent static pre-launch audit only. Promotion, launch-marker creation and execution are explicitly closed. The exact candidate was constructed after that authority and remains inert outside `.github/workflows`; no result exists to tune against.

No V0.26 R1 science threshold, denominator, sampling rule, solver object, response object, covariance object or downstream inference object is changed by the candidate.

## Controls that survive review

The executor binds the exact preregistration, contract, canonical source and terminal pre-execution authority blobs. Canonical production is response-blind and arithmetic-free: 897 lowercase u64hex words are parsed as unsigned integers and emitted as exactly 8 little-endian bytes each. It checks the frozen source SHA256, exact 7176-byte payload SHA256, and the frozen one-bit negative-control digest. It imports no NumPy or CLASS and contains no scientific-response read.

The inert workflow fixes exactly 32 `ubuntu-24.04` lanes `R01..R32`, `fail-fast:false`, run-number 1 / attempt 1 guards, no `workflow_dispatch`, and a separate aggregate decision job. Missing lane population can reach the frozen infrastructure BLOCKED classifier because classification and decision upload use `always()` semantics.

The runtime candidate also requires a future terminal implementation authority, exact byte identity between promoted active workflow and the audited inert workflow candidate, and a separately bound launch marker before lane work can proceed.

## Deterministic counterexample 1 — frozen consumer-roundtrip contract is not implemented

The frozen preregistration requires every lane to perform this exact operation: interpret the canonical bytes as contiguous little-endian IEEE-754 binary64 values **without arithmetic**, immediately reserialize them as contiguous little-endian binary64, and require byte-for-byte identity plus the same SHA256. The machine contract freezes the same consumer-roundtrip semantics.

The reviewed executor does not perform that operation. Its `consumer_roundtrip(payload)` only slices the payload into 8-byte byte strings and concatenates those same byte strings. No IEEE-754 binary64 interpretation or binary64 serialization is exercised.

Therefore a consumer-side endian/serialization implementation defect that would be exposed by the preregistered binary64 decode/re-encode path is structurally invisible to this candidate. The current round-trip is an identity framing operation and cannot test the frozen consumer hypothesis. This is not a threshold choice and cannot be repaired by interpreting a future result differently; the exact executor fails the preregistered operation identity before execution.

The non-authority implementation manifest explicitly records the substituted operation as `byte-only 8-byte framing and re-concatenation; no float conversion or arithmetic`, confirming that this is a deliberate implementation change relative to the frozen preregistration/contract rather than an ambiguous reading.

## Deterministic counterexample 2 — required artifact/inner-hash provenance is absent

The frozen preregistration requires each lane receipt/provenance chain to include artifact hashes and requires PASS only when all receipts/artifacts and inner hashes are present and bind run #1 / attempt #1. The terminal pre-execution authority correspondingly requires `RECORD_COMPLETE_PER_LANE_RUNTIME_AND_ARTIFACT_PROVENANCE`.

The reviewed lane receipt contains run/job/runtime identities and source/output hashes but no Actions artifact id, artifact digest/ZIP SHA256, or independently checkable inner receipt hash. The workflow uploads each lane JSON with `actions/upload-artifact@v4`, but the aggregate decision merely downloads files with pattern `grid896-*` and parses `R*.json`; it never enumerates Actions artifact metadata, verifies exact artifact count/names/ids, verifies GitHub artifact digests, or binds outer artifact digests into the decision.

Consequently two executions with identical parsed lane JSON content but different or incomplete outer artifact provenance are indistinguishable to the frozen aggregate classifier. A PASS decision could therefore be emitted without satisfying the preregistered artifact/inner-hash provenance predicate.

This is an implementation/provenance defect, not a scientific result and not a numerical artifact.

## Classifier consequence

Because the exact candidate substitutes a different consumer-roundtrip operation and omits a mandatory artifact-provenance predicate, a future green workflow cannot be interpreted as the prospectively frozen `PASS_SHARED_GRID896_CONTENT_ADDRESSING_CROSS_HOST`. The implementation identity does not realize the frozen gate.

The correct response is not to rewrite the preregistration, reinterpret PASS, or patch these exact blobs after seeing a result. Preserve executor blob `f5e482bf...` and workflow blob `78aa9d15...` as the reviewed failed candidate and create a prospectively frozen successor implementation candidate under the same frozen scientific/no-science boundary.

## Required successor implementation controls

A successor implementation candidate must, before any execution authority is considered:

1. implement the exact frozen consumer operation using an explicit little-endian IEEE-754 binary64 decode followed immediately by little-endian binary64 reserialization, with no arithmetic, and require exact byte identity and canonical SHA256;
2. keep canonical producer arithmetic-free (`u64hex -> unsigned integer -> fixed 8-byte little-endian packing`) and preserve all frozen source/payload/negative-control hashes;
3. add a prospective artifact-provenance scheme that can terminally bind every lane artifact to exact run/job/lane identity, exact artifact id/name/digest, and exact inner receipt digest, and require the aggregate/terminal validator to reject missing, duplicate, extra or digest-mismatched lane evidence;
4. preserve exactly 32 lanes `R01..R32`, no replacement/selection, run #1 / attempt #1, no workflow dispatch, exact audited workflow promotion, future terminal implementation authority and one-shot launch-marker guards;
5. remain response-blind with no CLASS/scientific-response/covariance/whitening/nuisance/relation-null/`Wm_S3`/global65537 access;
6. undergo a fresh independent static audit before promotion or launch.

## Interpretation ceiling

This review is infrastructure/provenance/static implementation only. No CLASS solve, Layer-B response, interpolation/resolution/tolerance comparison, covariance, nuisance, statistical/model inference or physical dark-sector inference was executed or evaluated. Scientific effect remains `+0/+0`; no readiness/frontier increase is authorized.

## Review result

Verdict: **INVALID_IMPLEMENTATION**.

Classification: `GRID896_DIAGNOSTIC_IMPLEMENTATION_DOES_NOT_REALIZE_FROZEN_CONSUMER_ROUNDTRIP_AND_ARTIFACT_PROVENANCE_CONTRACT`.

Authorized next stage: prospectively author a corrected inert successor executor/workflow implementation candidate only, preserving the historical failed candidate and frozen design. No workflow promotion, launch marker, diagnostic execution, successor sentinel science, full107 or downstream science is authorized by this audit.
