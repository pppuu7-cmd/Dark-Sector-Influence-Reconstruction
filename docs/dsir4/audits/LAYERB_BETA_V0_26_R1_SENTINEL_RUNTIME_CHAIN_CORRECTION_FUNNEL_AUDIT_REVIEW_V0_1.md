# DSIR Funnel Auditor review — V0.26 R1 runtime-chain correction external funnel audit v0.2

Date: 2026-09-16. Scope: DSIR only.

## Reviewed result

Reviewed hosted independent response-blind governance-only funnel result: Actions run `35025283328`, workflow `dsir-v026-r1-sentinel-runtime-chain-correction-funnel-audit-v0-2`, exact audit head `5c34da32133f086d53c5af939e3e6e80147786d3`, reviewed correction head `d3b32cd341ce16b5494024dfa9785a2480173dc1`, base `78f96f2c60db385f88a391b7fd046dd312176019`.

Producer receipt verdict: `QUALIFIED`; classification: `SENTINEL_GOVERNANCE_ONLY_A_L_Q_RUNTIME_CHAIN_CORRECTION_QUALIFIED_FOR_AUTHORITY_FIRST_PROMOTION`; effect `+0/+0`.

This review does not inspect or infer any sentinel scientific response. It is limited to governance/provenance/code-contract compatibility before any final launch descriptor exists.

## Authorization and chronology

The terminal v0.2 runtime-chain blocker authority on main requires a governance-only corrected A/L/Q package and independent qualification before runtime replacement. The corrected package was frozen on the research head before the independent audit. The independent audit was a separate push workflow, run number 1 / attempt 1. No final L existed on the reviewed correction head and the captured exact-head sentinel-science run set was empty.

There is no threshold, target, tolerance, panel, row-denominator, solver, or scientific-object change in the correction diff. The exact changed-file set is six governance/audit files only: corrected A candidate, corrected L candidate, corrected Q candidate, correction contract, static-auditor source, static-audit workflow.

## Exact identities

Corrected candidate blobs independently rechecked against the audited head:

- A: `1c9945dd00b137f3e202efa14bf4112fffebf8af`;
- L: `fa7014435f0a5688def2124898ddd01d0c0183aa`;
- Q: `f7b97f47d9e771e3d3ea78875da5a45962160cd0`;
- frozen active W: `19907175f0f3417ddee2aba6916d961c6be02e26`;
- executor: `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`;
- decision: `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`;
- implementation contract: `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`;
- correction contract: `01af3648bd3dc640acf35c7b0b7c116334b61cfe`.

Independent source comparison confirms the correction is minimal: A is old A plus exactly the executor-compatible alias `promotion_authority_git_blob_sha1`; L changes only the bound A blob; Q adds exactly the six top-level bindings consumed by W and updates the nested A/L identities. W/executor/decision are unchanged.

## Completed static control

Hosted static audit run `35025081430`, job `104570053404`, run #1 / attempt #1, completed success. Artifact `10419525675`, Actions ZIP digest `sha256:82929104a6129f5f8f8bd465ef574b4ce55c172411415c19458de9bb8fe5fa0f`; frozen receipt SHA256 `b326cfc032a2e758d9565b4672d34f5f18ec61d8475ee5d23601e037bf3dab39`.

The independent funnel workflow hash-binds this artifact and receipt before executing its own checks.

## Independent funnel artifact provenance

Run `35025283328` completed success at 2026-09-15T21:32:48Z. Its only job, `104570712438`, completed success; every substantive step completed success. Actions reports exactly one artifact:

- artifact id `10419217250`;
- name `dsir-v026-r1-sentinel-runtime-chain-correction-funnel-audit-v0-2`;
- Actions ZIP digest `sha256:51fa034ee9b3ff4bafe2f030db1b619adabd5f8e69b3b88cbd626ed126e53592`.

The ZIP was independently downloaded and hashed; the downloaded ZIP SHA256 is exactly `51fa034ee9b3ff4bafe2f030db1b619adabd5f8e69b3b88cbd626ed126e53592`.

It contains exactly three files:

- `runtime_chain_correction_funnel_audit.json`: 1607 bytes, SHA256 `7edd0cdaa06a43c7c42518993891c63c071c3feda2c187ff9b60f767b1a1b9d6`;
- `runtime_chain_correction_funnel_audit.sha256`: 114 bytes, SHA256 `8278dd9988e2820c40d6a025594e3389e5aae8db19ce1bfb7a70701fd827e524`;
- `science_runs.json`: 36 bytes, SHA256 `a2790a384d7d281e7395679000c35d27768d89dbd7052f725b8f4688beb59915`.

`science_runs.json` is exactly an empty workflow-run set: `total_count=0`. No sentinel-science execution occurred at the correction head.

## Independent code audit

The independent auditor is blob `1ee95009fef7b259deaa93b4594a67f37d20dbf3`. It independently reconstructs the candidate diff from base/head rather than trusting the static receipt for the semantic deltas. It checks exact A/L/Q and unchanged W/executor/decision blobs, verifies no final L, recomputes minimal A/L/Q semantic deltas, checks the frozen W and executor consumer contracts, retains the decision full-replay firewall, verifies the immutable static receipt identity, and rejects any sentinel-science workflow run at the correction head.

The workflow pins the correction head and static artifact identities, verifies its own auditor blob, downloads and hash-checks the static artifact, captures exact-head science runs before emitting its receipt, and persists the resulting receipt.

## Counterexample / alternative-explanation search

The prior observed failures were concrete schema-consumer mismatches, not scientific-response failures: old Q lacked six top-level keys consumed by W; old A lacked the executor alias consumed by `require_launch_authority()`. The corrected objects repair exactly those consumer interfaces while preserving the same semantic identities and scientific object.

I attempted to find a broader hidden runtime change, a different A/L/Q semantic change, a final-L early trigger, a science run at the candidate head, a decision-firewall relaxation, or a provenance mismatch. None is supported by the exact diff, source, run/job state, or independently downloaded artifact.

One important interpretation constraint remains: the corrected Q still contains historical package-evidence fields from the original package. That is acceptable only because this new independent correction receipt is not being smuggled into Q retroactively; it must be persisted as a separate qualification authority before corrected A/Q are promoted. The reviewed receipt itself explicitly requires `PERSIST_QUALIFICATION_AUTHORITY_THEN_PROMOTE_EXACT_CORRECTION_PACKAGE_WITHOUT_FINAL_L`. Therefore confirmation here does not authorize direct creation of L.

## Reproducibility / numerical scope

No CLASS solver was invoked, no scientific response was read, and no covariance was read. Consequently this review cannot test interpolation, grid resolution, tolerance dependence, execution order, numerical nondeterminism, cross-host response reproducibility, nuisance structure, covariance structure, look-elsewhere effects, or physical/systematic explanations. Those questions remain outside this governance-only gate.

## Interpretation ceiling

A green governance workflow is not a scientific PASS. This result establishes only that the exact corrected governance package is internally compatible with the already-frozen runtime consumers and may proceed to authority-first promotion. It does not establish sentinel numerical validity, full 107-row validity, statistical/model validity, nuisance removal, or physical dark-sector inference.

## Verdict

`CONFIRMED_SCOPED`.

Confirmed scope: the exact corrected A/L/Q package at `d3b32cd341ce16b5494024dfa9785a2480173dc1` is independently qualified for **authority-first, no-L promotion sequencing only**. The producer receipt verdict `QUALIFIED` survives this audit in that exact governance-only scope.

The historical runtime-chain `BLOCKED` authority is not erased. It remains the reason old final A/Q cannot be used to launch. The correction result only opens the next governance gate.

## Authorized next stage

Persist a separate terminal qualification authority on main binding this run/job/artifact/receipt and exact corrected A/L/Q identities. Only after that authority is on main may corrected A and corrected Q replace the old final A/Q **without final L**. Then perform a separate response-blind post-replacement fail-closed audit. Final L remains forbidden until a later terminal authority explicitly authorizes its one-time creation.

Full 107-row execution, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed. Readiness remains 68%, scientific frontier 67%, effect `+0/+0`.
