# Exp073ID — C2 tangent response monotone scale-stability admission v0.1

Status: PROSPECTIVELY FROZEN AFTER Exp073IC RAW-LOG CANDIDATE PASS AND **BEFORE INSPECTING IC SCALE-RELATION VALUES**.

## Input authority ceiling
Exp073IC run `34249380208`, job `102139612475`, head `f3475f5d409a50c31fb1eda3870837542797e091` emitted exact token `PASS_EXP073IC_C2_TANGENT_FINITE_DIFFERENCE_RESPONSE_CANDIDATE_V0_1`, response JSONL SHA256 `e97ef98a5b137081df5937454f02576d30e726266e9c50733bf399a9be2b1907`, and classification `TANGENT_RESPONSE_CANDIDATE_PLUS_0_PLUS_0`. At preregistration time the response artifact numerical rows have not been inspected for inter-scale behavior.

## Purpose
Prospectively test only whether the already-frozen finite-difference responses exhibit monotone stabilization as step size decreases. This is a numerical response-admission gate, not a fit, extrapolation or physical-model authority gate.

The frozen IC scales are `h1=1e-4`, `h2=1e-3`, `h3=1e-2`, with alpha one-sided negative response and beta symmetric response. The h1 pair remains the frozen base-step candidate.

## Exact no-tolerance stability rule
For each exact request ID independently and for each direction `x in {alpha,beta}`, decode the three IC response fields exactly as binary64:

- `D1 = D_x(h1)`
- `D2 = D_x(h2)`
- `D3 = D_x(h3)`

Require all finite. Execute exactly:

1. `e_small = abs(D1 - D2)`
2. `e_large = abs(D2 - D3)`
3. PASS-node iff `e_small <= e_large` using the exact binary64 comparison, with no tolerance.

Thus the response change from `1e-3` to `1e-4` must not exceed the change from `1e-2` to `1e-3`. If `e_large == 0.0`, PASS requires `e_small == 0.0`. No ratio, epsilon, rounding, smoothing, averaging, sign rescue, coordinate dropping or post-hoc scale substitution is allowed.

Global PASS requires all `28*2 = 56` node-direction checks PASS. The rule is intentionally weaker than enforcing the ideal asymptotic error-order ratios (alpha O(h), beta O(h^2)); it tests only contraction toward the frozen base scale and therefore does not inject an arbitrary numerical threshold.

## Scientific meaning and boundaries
A global PASS admits the h=`1e-4` finite-difference pair as a **numerically scale-stable tangent response** for the frozen 28 coordinates. It does not prove the physical model, does not create a prediction, and does not test `G_DOMAIN_MAPPING`.

A global FAIL is a negative numerical/scientific response-stability result under the prospectively frozen three-scale design. It must not be repaired by choosing h=`1e-3`/`1e-2`, removing coordinates, relaxing the exact comparison, adding tolerance, smoothing or extrapolation. The next scientific branch after FAIL must be chosen without rewriting this historical result.

PASS token: `PASS_EXP073ID_C2_TANGENT_RESPONSE_MONOTONE_SCALE_STABILITY_ADMISSION_V0_1`.

On PASS only:
- `classification=TANGENT_RESPONSE_NUMERICALLY_ADMITTED_PLUS_0_PLUS_0`
- `response_candidate_created=true`
- `tangent_response_ready=true`
- `admitted_base_step=1e-4`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

On global stability failure:
- `classification=SCIENTIFIC_NUMERICAL_STABILITY_FAIL`
- `tangent_response_ready=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`.