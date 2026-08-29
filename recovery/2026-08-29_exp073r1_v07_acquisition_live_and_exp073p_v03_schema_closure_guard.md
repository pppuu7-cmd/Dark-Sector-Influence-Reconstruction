# DSIR checkpoint — Exp073R1 v0.7 live acquisition + Exp073P v0.3 schema-closure guard

Date: 2026-08-29
Branch: `main`

## Canonical Exp073R1 v0.7 state

Authoritative workflow run remains:

- run id: `33240490287`
- run attempt: `2`
- job id: `99080934021`
- job name: `transport-stabilized-replay`

At this checkpoint the job is `in_progress`.

Completed successfully before acquisition:

1. checkout;
2. frozen-contract / syntax firewall;
3. local capacity gate;
4. pinned mapper runtime + provenance capture;
5. immutable Stage-A / Exp073R0 rebinding;
6. parent artifact downloads;
7. downloaded-parent internal-contract rebinding.

Current active step is:

`Acquire authoritative object by full-from-zero no-Range retries`

The loopback endpoint, unchanged frozen mapper, genuine Exp073R1 PASS assertion and artifact publication have **not** yet run. Therefore the correct scientific status remains:

- `reproduction=INCOMPLETE`
- `scientific_FAIL=false`
- `G7=OPEN`
- no downstream physical-support execution is authorized.

No duplicate heavy run was launched.

## Independent Exp073P v0.3 reproducibility control added

Added prospective fail-closed evidence-schema closure guard:

- `ci/exp073p_v03_evidence_schema_closure_guard_v0_1.py`
- guard commit: `640764456d5d9ecb452772ef95ccd1897f507243`
- workflow: `.github/workflows/ci-exp073p-v03-evidence-schema-closure-v0-1.yml`
- workflow commit: `b5bffe99086ec7137355de8cef5a71c9f2786716`

Purpose: supplement the existing strict-JSON parser ambiguity guard with a separate proof that authority-bearing JSON can be treated as a **closed schema**, rejecting semantic drift through extra, aliased, case-shifted, padded, Unicode-confusable, wrongly nested, or wrong-typed keys.

This is a prospective synthetic validation control only. It does not modify the frozen Exp073P v0.3 prerequisite join, frozen acceptance criteria, Exp073R1 evaluator, or physical-support mask definition.

Synthetic negative cases include:

- unknown root/summary/authority/catalog/acquisition/runtime keys;
- camelCase alias of `run_attempt`;
- case-shifted and whitespace-padded status key;
- Unicode-confusable key;
- authority field moved to the wrong nesting level;
- root/object shape substitutions;
- exact JSON type confusions (`bool` as integer, float as exact byte count, integer as boolean flag).

Hosted CI:

- run: `33267947264`
- job: `99141254295`
- conclusion: `success`
- all steps passed, including explicit assertions:
  - `support_executor_authorized=false`
  - `gate_state=G7:OPEN,G8:OPEN,G9:OPEN`
  - `frozen_acceptance_criteria_changed=false`

Classification: reproducibility/validation PASS only; **not** a scientific G7 PASS.

## Frozen downstream order

Still enforced without exception:

`genuine Exp073R1 PASS -> real attempt-aware Exp073P v0.3 prerequisite join -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`
