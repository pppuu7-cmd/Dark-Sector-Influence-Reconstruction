# DSIR checkpoint — Exp073P v0.3 strict JSON evidence ambiguity guard PASS

Date: 2026-08-29

## Live authority state

- Canonical Exp073R1 v0.7 run: `33240490287`.
- Canonical rerun attempt: `2`.
- Canonical self-hosted job: `99080934021`.
- At this checkpoint the run/job remain `queued`.
- Therefore Exp073R1 reproduction remains **INCOMPLETE**; there is no scientific FAIL and no downstream G7 authorization.
- No duplicate heavy R1 run was launched in this iteration.

## Independent validation gap addressed

The frozen Exp073P v0.3 production route consumes JSON evidence with CPython's standard JSON parser. CPython's default decoder accepts duplicate object keys (last key wins) and non-standard non-finite constants such as `NaN` and `Infinity`. These parser semantics can create authority/evidence ambiguity even when higher-level field checks are fail-closed.

A separate prospective validation control was added at `ci/exp073p_v03_json_evidence_ambiguity_guard_v0_1.py`. It does **not** modify the frozen Exp073P v0.3 evaluator, production workflow, preregistration, acceptance criteria, or scientific classification. It is intended for strict validation of future real JSON receipts before downstream scientific use.

The guard enforces:

- strict UTF-8 decoding;
- duplicate-key rejection at every object depth;
- rejection of `NaN`, `Infinity`, and `-Infinity`;
- recursive rejection of any non-finite float;
- exactly one JSON value with no trailing second document;
- JSON object as the required top-level evidence type.

Synthetic negative cases: duplicate top-level key, duplicate nested key, NaN, +Infinity, -Infinity, invalid UTF-8, trailing JSON document, and top-level array.

## Hosted receipt

Workflow: `.github/workflows/exp073p-v03-json-evidence-ambiguity-guard-v0-1.yml`

Hosted Actions run `33265437688`, job `99134562144`: **PASS**.

The guard explicitly emits:

- `frozen_acceptance_criteria_changed=false`
- `scientific_classification=None`
- `support_executor_authorized=false`
- `gate_state=G7:OPEN,G8:OPEN,G9:OPEN`

## Scientific ordering

No support-validity, covariance, whitening, nuisance SVD/rank, quotient/relation/null, held-out, G8, or G9 quantity was evaluated. Required ordering remains:

`genuine Exp073R1 PASS -> real Exp073P v0.3 prerequisite join -> strict receipt validation / physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.

This checkpoint records a reproducibility/authority validation improvement only; it is not a scientific result and cannot be used to convert an incomplete R1 reproduction into PASS or FAIL.
