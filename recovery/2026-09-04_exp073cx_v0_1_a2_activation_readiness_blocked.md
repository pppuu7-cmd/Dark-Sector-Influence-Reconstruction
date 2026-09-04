# DSIR immutable recovery — Exp073CX v0.1 A2 activation-readiness blocked

Date: 2026-09-04. Scope: DSIR only.

## Authoritative process
- Gate: Exp073CX v0.1 Wm_S3 activation-readiness audit, support-only `+0/+0`.
- Prereg commit/blob: `cacc4090a73ea281edfca0a9f41e02bf6d426623 / cfb4eac2ed0eaac400633438f5e3fd1520a71f7a`.
- Auditor commit/blob: `42c0269629e8a44f168b5223584262ef09b318a9 / 97d8168d7f052d09c0de8f9664a1407c264a745e`.
- Workflow commit: `a40c6512790fd403abd59e454e10659fb023c4f9`.
- Activation/head: `fc7268f3de8ed88d8e0acbf5146115123422c4ec`.
- Run/job: `33866284923 / 101001778900`.
- Artifact: `9934079080`.
- Independently downloaded artifact ZIP SHA256: `303f2b28d69ceff50eeafc4583f79a5dabee2ec6acc38d64b573072432b9c51e`.

## Raw frozen classification
`A2_IMPLEMENTATION_CONTRACT_FAIL`, accounting `+0/+0`.

Receipt checks:
- blob binding: PASS;
- checkpoint order: PASS;
- A/B namespace isolation: PASS;
- single-mask handoff: PASS;
- exact 8-core/nested-thread contract: PASS;
- forbidden historical numerical import check: PASS;
- unified production A/B driver present: FAIL;
- production exact-route composition check: FAIL;
- exact-comparator literal static check: FAIL.

The exact-comparator literal failure is non-authoritative as a scientific issue because the auditor searched one spelling while the Exp073BU prereg already freezes exact SHA256 plus `numpy.array_equal`; it is preserved historically and may be corrected only prospectively. The A2 classification remains valid independently because the unified production A/B driver is genuinely absent and the admitted Exp073CV production adapter consumes an already-persisted workspace rather than itself bridging a fresh workspace to stock `write_to()`.

## Interpretation
This is an implementation/readiness BLOCKING result `+0/+0`, **not** a Wm_S3 scientific arithmetic FAIL. It does not create Wm_S3 authority and does not activate Exp073BU. Historical results are unchanged.

The next permitted work is a prospective repository-bound source/interface audit for the exact fresh S3 and lens acquisition/reconstruction authority, followed by implementation and hosted audit of one unified production A/B driver. Home science remains forbidden until those gates and a subsequent fresh activation-readiness gate pass.

DSIR-HOME-PC remains FREE.
