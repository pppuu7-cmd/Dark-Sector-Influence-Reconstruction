# Exp073GP — C2 IDE recorder ABI static audit v0.1

Status: PROSPECTIVELY FROZEN after validated Exp073GO support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Exp073GO established that the pinned baseline and exact GM-instrumented `perturbations.c` translation units both compile. GP freezes the next narrower support question before any cosmological prediction is generated: can the admitted observation-only hook hand its eight source values to a deterministic recorder ABI whose serialization schema is explicit, finite-checking, append-only, and external to solver state?

This is not a numerical prediction gate and cannot create C2 model authority.

## Frozen recorder schema

One record contains exactly eight IEEE-754 binary64 values, in this order:

`tau, k, a, H, delta_m, theta_m, rho_idm_iv, rho_iv`.

The hosted audit must prove:

1. the record struct contains exactly eight `double` fields in the frozen order;
2. the serializer writes exactly eight binary64 values per accepted record with no arithmetic transformation;
3. all eight values must be finite or the record is rejected fail-closed;
4. the recorder may mutate only its own external stream/counter state and may not write CLASS background/perturbation state;
5. a deterministic round-trip fixture reproduces the exact input bytes field-by-field;
6. no cosmological solver run, self-hosted computation, C2 prediction generation, interpolation, smoothing, averaging, tolerance rescue, or scientific gate is allowed.

## Classification

Exact PASS token: `PASS_EXP073GP_C2_IDE_RECORDER_ABI_STATIC_AUDIT_V0_1`.

PASS classification is only `SUPPORT_PLUS_0_PLUS_0`, with `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any compiler, schema, finiteness, serialization, or round-trip failure is implementation/infrastructure `+0/+0`, never a scientific model FAIL. A PASS may authorize a separately prospectively frozen hosted integration/runtime extraction contract, but does not itself authorize scientific interpretation.
