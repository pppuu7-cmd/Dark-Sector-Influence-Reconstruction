# Exp073AK — Article 3 Exp073AI completion/authority classifier v0.1

**Frozen:** 2026-08-30 while Exp073AI run `33310888983` is still in progress, before either single-thread replica artifact exists and before any Exp073AI comparator result exists.

## Purpose

Exp073AK is a non-scientific completion/provenance gate. It freezes how the eventual hosted Exp073AI execution state is mapped to `PENDING`, a valid exact reproducibility classification, or an infrastructure-INCOMPLETE class. It exists so timeout/cancellation/artifact/comparator failures cannot be interpreted post hoc after the numerical outcome is known.

Exp073AK never reads angular array values and never changes the exact Exp073AI numerical PASS/FAIL criterion.

## Frozen Exp073AI identity

- run `33310888983`;
- head `fdfb0eae9ea799b4a185a059a0d1b9dfca17b31d`;
- replica jobs A `99255607805`, B `99255607640`;
- replica job timeout `240` minutes;
- aggregate job timeout `20` minutes;
- valid numerical tokens only:
  - `PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1`;
  - `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1`.

## Frozen input fields

The classifier may inspect only hosted control-plane/provenance facts:

- run state/conclusion;
- each frozen replica job state/conclusion;
- whether each replica artifact exists and contains its required environment receipt plus completed JSON+NPZ authority pair;
- aggregate job state/conclusion;
- whether final aggregate artifact exists;
- if final aggregate artifact exists, its declared status token only.

It may not inspect array values, per-element differences, support, covariance, nuisance geometry, relation/null, G8, or readiness optimization.

## Frozen decision order

1. If the run or any required job is still queued/in-progress and no terminal contradiction exists -> `PENDING_EXP073AI`.
2. If both replica jobs complete `success`, both complete replica artifacts exist, aggregate job completes `success`, final aggregate artifact exists, and its token is one of the two frozen valid numerical tokens -> `VALID_HOSTED_EXP073AI_CLASSIFICATION`, preserving that token verbatim.
3. If a replica job terminates non-success before producing a complete replica authority artifact -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_EXECUTION`.
4. If a replica job reports success but its required complete artifact is absent/incomplete -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_ARTIFACT`.
5. If both complete replica authorities exist but aggregate job terminates non-success before a valid frozen numerical token -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATOR_EXECUTION`.
6. If aggregate job reports success but final aggregate artifact/token is missing, malformed, or outside the frozen token set -> `INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATE_AUTHORITY`.
7. Run-level cancellation/timeout cannot by itself create scientific/repeatability FAIL; it maps to the most specific applicable infrastructure-INCOMPLETE branch above.
8. Unknown/conflicting control-plane states fail closed as `INVALID_CONTROL_PLANE_STATE_NO_SCIENCE_CLASSIFICATION`.

A numerical repeatability FAIL can therefore exist only if the frozen comparator actually reached a valid final hosted authority and emitted the frozen FAIL token.

## Scientific accounting/firewall

Every Exp073AK output must retain:

- Article-3 scientific readiness `52%`;
- readiness increment `0`;
- G7/G8/G9 `OPEN`;
- `science_gate_scored=false`;
- `production_release=false`;
- no reclassification of historical Q;
- no automatic Exp073AA release even if Exp073AI later PASSes.

## Required hosted synthetic QA token

`PASS_EXP073AK_AI_COMPLETION_AUTHORITY_CLASSIFIER_SYNTHETIC_V0_1`

This token means only that the completion classifier implements the prospective fail-closed state machine. It is not an Exp073AI result and contributes +0 scientific readiness.
