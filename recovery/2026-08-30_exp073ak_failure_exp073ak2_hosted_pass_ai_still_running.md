# DSIR recovery checkpoint — Exp073AK v0.1 implementation failure, Exp073AK2 hosted PASS, Exp073AI still running

**Date:** 2026-08-30

## Accounting

- Strict Article-3 scientific repository readiness: **52%**.
- G7/G8/G9: **OPEN**.
- Layer A/B: **OPEN**.
- covariance/whitening: **BLOCKED**.
- Exp073AK/AK2 are governance/synthetic QA only and contribute **+0** scientific readiness.
- Historical Exp073X2 Q `SCIENTIFIC_REPEATABILITY_FAIL` remains immutable and is not reclassified.
- DSIR remains separate from RTK/RQIR.

## Heavy-work audit

Before this gate, latest commits, Actions, artifacts and `docs/RECOVERY_LATEST.md` were checked.

Real Exp073AI remains the active heavy route:

- run `33310888983`;
- head `fdfb0eae9ea799b4a185a059a0d1b9dfca17b31d`;
- replica A job `99255607805`;
- replica B job `99255607640`;
- both still in `Compute exact single-thread replica` at latest inspection;
- run status `in_progress`;
- replica artifacts at latest artifact inspection: `0`.

No duplicate Exp073AI and no Exp073AA production tasks were launched.

The Exp073AI workflow itself prospectively freezes replica timeout `240` minutes and aggregate timeout `20` minutes. Its prereg already states that failure before valid comparison is infrastructure-INCOMPLETE rather than repeatability FAIL. Exp073AK was added only to make this control-plane distinction executable/fail-closed before the AI numerical outcome exists.

## Exp073AK v0.1

Prospective chain:

- prereg `ffb20ffcea7b0acd9687a34bc38c506b0750a5f6`;
- implementation `597f64387ef164944cce2296f66d8f82b10a0cdb`;
- workflow `72e5f6ffa0f4899f9c9e5f163d5c7d1e4901ce0d`;
- workflow freeze `449e0bf34bf4883e8804efbdbe2145702e21ec6d`;
- trigger/head `717285a4d64ced4ae6120ece3a8a4622d267054f`;
- hosted run `33316169150`, job `99269912588`.

The run passed prospective-freeze enforcement, then failed inside the synthetic matrix before any real AI receipt was read. Root cause: several self-test `check(...)` calls omitted their fixture argument.

Permanent classification:

`IMPLEMENTATION_FAILURE_SYNTHETIC_HARNESS_MISSING_FIXTURE_ARGUMENT_BEFORE_CLASSIFICATION_NOT_SCIENCE`.

This is not an Exp073AI result and not a scientific result.

## Exp073AK2 v0.2 narrow repair

Allowed repair was limited to supplying the intended fixture to the synthetic `check(name, fixture, expected, ...)` call sites. The completion state machine, AI valid-token vocabulary, run/job identities, firewall and accounting were kept unchanged.

Frozen chain:

- prereg `61b725cc3e98acb6374b9165acbbb77deba10284`;
- implementation `6ca671ad6145ae5b78977958999ec5bdae380fbb`;
- workflow `14f5c3ebafe663479b454c7944d95cb9277207cf`;
- workflow freeze `d82ed284e80d2157f55418b205bb7b00f7fa87c2`;
- trigger/head `8f2d7a2d5b909c475dcd1940f82d9332129462ce`;
- hosted run `33316242357`;
- job `99270113118` completed `success`;
- artifact `9733523834`;
- artifact digest `sha256:f08e772acab3a0c08269fa637d8dc8fe6a4839a73630e04048d86680e8ab94bb`;
- token `PASS_EXP073AK2_AI_COMPLETION_AUTHORITY_CLASSIFIER_SYNTHETIC_V0_2`.

Classification:

`HOSTED_SYNTHETIC_COMPLETION_CLASSIFIER_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

## Frozen completion semantics now hosted-tested

Exp073AK2 distinguishes:

- live queued/in-progress state -> `PENDING_EXP073AI`;
- both complete replica authorities + successful aggregate + final artifact with one of the two frozen AI tokens -> `VALID_HOSTED_EXP073AI_CLASSIFICATION`, preserving that token verbatim;
- replica non-success before complete authority -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_EXECUTION`;
- replica success but missing/incomplete artifact -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_ARTIFACT`;
- both replica authorities present but aggregator non-success before valid token -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATOR_EXECUTION`;
- aggregate success but missing/malformed final authority/token -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATE_AUTHORITY`;
- unknown/conflicting state -> `INVALID_CONTROL_PLANE_STATE_NO_SCIENCE_CLASSIFICATION`.

A scientific/repeatability FAIL for Exp073AI may therefore be recorded only if the frozen comparator actually reaches a valid final hosted authority and emits `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1`. Timeout, cancellation, missing artifacts or aggregator failure can never be silently promoted to that class.

Exp073AK2 reads no angular values, support, covariance, nuisance geometry or G8; it cannot release Exp073AA production.

## Resume instruction

1. Inspect Exp073AI run `33310888983`, both replica jobs and artifacts.
2. Do not launch another AI while it is active.
3. When AI becomes terminal, classify completion under Exp073AK2 before interpreting numerical repeatability.
4. Only a valid hosted AI final token is a valid AI PASS/FAIL authority.
5. After both environment receipts exist, AJ2 may add its independent provenance label but may not reclassify the AI numerical result.
6. Even AI PASS remains +0 readiness and does not automatically release Exp073AA; a future succession amendment must be separately prospective.
