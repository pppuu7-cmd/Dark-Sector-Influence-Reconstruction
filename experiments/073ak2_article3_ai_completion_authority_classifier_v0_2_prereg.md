# Exp073AK2 — Article 3 AI completion authority classifier v0.2 narrow repair

**Frozen:** 2026-08-30 after Exp073AK v0.1 hosted run `33316169150` failed inside its synthetic test matrix, while real Exp073AI run `33310888983` remains in progress and before any real AI artifact/token is read by this classifier.

## Historical v0.1 classification

Exp073AK v0.1 is permanently retained as:

`IMPLEMENTATION_FAILURE_SYNTHETIC_HARNESS_MISSING_FIXTURE_ARGUMENT_BEFORE_CLASSIFICATION_NOT_SCIENCE`.

The prospective freeze step passed. The failure occurred in the synthetic matrix because several test-harness `check(...)` calls omitted the fixture argument. No real Exp073AI receipt, artifact, numerical window or status token was read; therefore no Exp073AI or scientific classification follows from v0.1.

## Allowed repair

Exp073AK2 may change only the synthetic self-test call sites so every `check(name, fixture, expected_class, ...)` call receives its intended fixture.

The v0.1 classifier state machine, valid Exp073AI token vocabulary, frozen run/job identities, firewall, readiness accounting and production prohibition must remain semantically identical.

## Required hosted token

`PASS_EXP073AK2_AI_COMPLETION_AUTHORITY_CLASSIFIER_SYNTHETIC_V0_2`

A PASS is synthetic/governance QA only, +0 scientific readiness, and is not an Exp073AI result.
