# DSIR Funnel Auditor — GRID896 diagnostic implementation successor V0.2 static audit

Date: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

Reviewed `main`: `c5273e9b37568c7bdc7d8730531761e95c611cb8`.

Reviewed exact frozen successor objects:

- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_2.py`, blob `69ead98fdaf605b961c7a85570a0cc5770af3750`;
- inert workflow `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-2.yml`, blob `271646639792041eb88a1b5c31a3cd142d1778df`;
- successor implementation manifest blob `2d8b8aa8d91817e758edf5fabcdb79d3d53deeca`;
- frozen preregistration blob `903c80709439cb790bd41316029b218a77d5695b`;
- frozen machine contract blob `6ba6e5a6c946a1091680f8f44821d323c9a463f3`;
- canonical source blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- terminal preexecution confirmation blob `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`;
- terminal predecessor implementation qualification blob `d9f940f3ea7b41b8df76d102f71ead16342a7f23`.

The active workflow path and V0.2 launch-marker path are absent on reviewed main, so no diagnostic execution is authorized or reviewed here.

## Authorization and chronology

The terminal predecessor authority permits only prospective corrected inert successor construction followed by an independent static audit. The V0.2 executor/workflow/manifest were created after that authority and before this audit. No scientific threshold, V0.26 R1 denominator, tolerance, sampling rule, PASS/FAIL science criterion or interpretation ceiling was changed.

The current gate is therefore source/provenance/static implementation only. No Actions outcome for this candidate exists and no partial substantive value is used.

## Controls that survive review

The exact V0.2 source prospectively fixes both defects recorded against historical implementation V0.1:

1. `consumer_roundtrip()` now performs explicit little-endian IEEE-754 binary64 decoding with `struct.iter_unpack("<d", payload)` followed immediately by `struct.pack("<d", value)` without arithmetic. The frozen canonical GRID896 words are finite positive binary64 values, so this exact path realizes the frozen decode/reserialize operation for the canonical object. Exact 7176-byte identity and SHA256 remain required.
2. The aggregate queries current-run Actions artifacts, requires expected lane artifact names/ids, downloads immutable ZIPs, compares GitHub `sha256:` digest to independently computed ZIP SHA256, requires one exact `Rxx.json` member, computes inner receipt SHA256 and records per-lane artifact id/name/API digest/ZIP SHA256/inner receipt SHA256 in the terminal decision.
3. Artifact run/head and receipt run/run-number/run-attempt/job/event/ref/source/contract/executor/workflow identities are checked.
4. The exact 32-lane `R01..R32` topology, `ubuntu-24.04`, run-number-1/attempt-1 guards, absence of `workflow_dispatch`, active-workflow exact-copy guard, future authority/launch-marker guards, canonical source/hash controls, fixed one-bit negative control and strict no-CLASS/no-science boundary are preserved.

These surviving controls do not rescue the candidate because the frozen terminal classifier is not faithfully implemented.

## Deterministic counterexample — valid FAIL is converted to BLOCKED

The frozen preregistration defines `BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE` only when fewer than 32 lane receipts are available for infrastructure reasons **without an implementation-level FAIL predicate being established**. `FAIL_SHARED_GRID896_CONTENT_ADDRESSING_CROSS_HOST` requires at least one otherwise-valid completed lane with correct source and audited implementation to produce a wrong canonical length/hash, a non-identical binary64 round-trip, or acceptance of the frozen corruption.

Exact V0.2 code violates that precedence. `list_run_artifacts()` executes before any available lane receipt is read. If the Actions artifact API reports `total_count < 32`, it immediately raises `PopulationIncomplete`. The outer `aggregate_command()` catches that exception and writes `BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE` without inspecting any artifact that is present.

Concrete frozen-scope witness:

- R01 is an otherwise-valid completed exact lane and produces a genuine frozen FAIL predicate, for example `roundtrip_byte_identical=false` with correct canonical source/code identities, and successfully uploads its artifact;
- R02..R31 upload otherwise-valid artifacts;
- R32 artifact is unavailable because of hosted infrastructure/upload failure;
- the current-run artifact API therefore returns 31 artifacts.

The preregistered result is not the hosted-infrastructure BLOCKED case, because an implementation-level FAIL predicate has already been established by R01. Exact V0.2 nevertheless returns `BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE` before it can observe R01. This is a deterministic classifier mismatch, not a numerical or scientific ambiguity.

## Secondary counterexample — malformed provenance can also be laundered into BLOCKED

The same early `total_count < 32` short-circuit occurs before per-artifact name/id/digest/ZIP/member/inner-receipt validation. Therefore a state containing fewer than 32 total artifacts **and** one present malformed or digest-mismatched artifact is classified `BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE` before the malformed evidence can trigger `INVALID_DIAGNOSTIC_PROVENANCE`.

This conflicts with the successor manifest's prospective mapping that duplicate/extra/malformed/digest-mismatched evidence is INVALID. Missing population alone may be BLOCKED; missing population cannot erase an already-present provenance invalidity.

## Why this is implementation-invalid rather than a qualification of the frozen design

No threshold, hypothesis, object, PASS/FAIL/BLOCKED criterion or interpretation ceiling needs to change. The defect is in the ordering of source-level classifier operations relative to already-frozen criteria. Rewriting the reviewed V0.2 blobs would violate historical preservation; a corrected implementation must therefore be a new prospective successor.

A minimally faithful successor classifier must enumerate and validate all available artifacts before applying the incomplete-population BLOCKED classification. At minimum it must ensure that:

1. any malformed/duplicate/unexpected/digest-mismatched present evidence is `INVALID_DIAGNOSTIC_PROVENANCE`;
2. any otherwise-valid present lane that establishes the frozen implementation FAIL predicate is not erased by a simultaneously missing infrastructure lane;
3. `BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE` is used only when the population is incomplete and no implementation-level FAIL predicate or present invalid-provenance predicate has been established;
4. all surviving V0.2 binary64, artifact-hash, one-shot, 32-lane, launch/authority and no-science guards remain unchanged.

Because exact precedence involving any additional simultaneous `BLOCKED_MISSING_OR_UNBOUND_CANONICAL_OBJECT` state should not be invented retrospectively by implementation code, a successor should preserve the existing frozen text and fail closed rather than add a new scientific or diagnostic criterion.

## Interpretation ceiling

This audit is infrastructure/provenance/static implementation only. No diagnostic execution, CLASS solve, numerical response, interpolation/grid/resolution/tolerance science test, covariance, statistical/model inference, nuisance removal or physical dark-sector inference was performed. Scientific effect remains `+0/+0`; no readiness/frontier increase is authorized.

## Verdict

**INVALID_IMPLEMENTATION**

Classification: `GRID896_DIAGNOSTIC_SUCCESSOR_V0_2_CLASSIFIER_PRECEDENCE_CAN_HIDE_ESTABLISHED_FAIL_OR_INVALID_PROVENANCE_BEHIND_INCOMPLETE_POPULATION_BLOCK`.

The exact V0.2 executor/workflow/manifest remain historical frozen failed objects and must not be promoted, launch-marked or executed. The next admissible gate is prospective construction of a new inert implementation successor that corrects classifier precedence while preserving all already-surviving controls, followed by a fresh independent static audit of the exact new blobs.