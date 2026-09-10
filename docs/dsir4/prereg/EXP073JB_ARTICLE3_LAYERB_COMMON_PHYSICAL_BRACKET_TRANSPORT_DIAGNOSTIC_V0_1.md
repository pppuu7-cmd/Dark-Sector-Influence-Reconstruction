# Exp073JB — Article 3 Layer-B common-physical-bracket transport diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JA AND BEFORE ANY EXP073JB NUMERICAL OUTPUT.

## Bound authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: retained dimension 107, zero invalid rows, `f_B=0`, exact production-vs-dense maximum `0.9998247463807295 > 1e-3`; covariance restriction unauthorized. Exp073JA is validated support-only `HIGH_DENSITY_CANCELLATION_OBSERVED_PLUS_0_PLUS_0`, artifact ZIP SHA256 `5cec1bc0a6d3c05b37fab53c4ad5f76d7ea079bf81066eed7145a31bfa8a71ed`. JA shows a stable endpoint-value derivative nearly cancelled by a large model-dependent native-grid term, with alpha adjacent-density differences decreasing but beta remaining strongly resolution-sensitive.

## Purpose
Test whether the dominant resolution sensitivity is caused by model-dependent movement of the native CLASS k-bracket itself. This is a mechanism diagnostic only and cannot redefine the scientific gate.

## Frozen execution
Use exact pinned CLASS-IV source `ac627d54e9ce196a08878d1ba33999819925d19c`, audited public gauge-invariant `d_m` exposure patch, exact baseline/precision inputs, `h=1e-4`, and the same two historical probes:
- alpha-left: `z=0.7000000000000001`, `k=0.002502504647141259 Mpc^-1`;
- beta-symmetric: `z=0.9351`, `k=0.01860440444314368 Mpc^-1`.

Diagnostic ladder: `k_per_decade_for_pk in {80,160,320,640}`.
For every density compute the same four models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`.

For each probe/density:
1. Record the ordinary model-native fixed-target interpolation exactly as Exp073JA.
2. Take the reference `(0,0)` model's physical native bracket `[k_lo_ref,k_hi_ref]` around the target and its exact log-k target fraction.
3. For each perturbed model, evaluate `d_m` at `k_lo_ref` and `k_hi_ref` by the same log-k interpolation on that perturbed model's own native table; these are transported endpoint values at common physical coordinates.
4. Interpolate those transported endpoints to the target using the reference bracket fraction. This defines the common-physical-bracket counterfactual value.
5. Compute alpha-left and beta-symmetric finite-difference responses from both ordinary/native and common-physical-bracket values using exactly the original one-sided/symmetric formulas and `h=1e-4`.
6. Record signed native response, signed common-bracket response, and their difference `native_minus_common`, plus all transported endpoint provenance/brackets.
7. Record adjacent-density relative differences for both response sequences using `abs(a-b)/max(abs(a),abs(b))` for finite positive magnitudes.

No averaging, smoothing, extrapolation, tolerance adjustment, effective coordinate, fiducial-P substitution or scientific gate replacement is allowed.

## Science firewall
Exp073JB is support-only `+0/+0`. It MUST NOT alter `REL_TOL=1e-3`, historical Exp073IR kpd 10/20 arithmetic, source definitions, domains, interpolation rule, atomization, row membership, covariance firewall, or manuscript/model authority. The common-bracket construction is explicitly a counterfactual mechanism diagnostic and is not admissible as a replacement Layer-B estimator unless separately prospectively justified after this artifact is consumed.

## Frozen classifications
- `COMMON_BRACKET_TRANSPORT_OBSERVED_PLUS_0_PLUS_0`: complete valid records produced and decomposition finite.
- `INVALID_INFRA_PLUS_0_PLUS_0`: source/hash/build/interface/input/execution prevents valid observation.

No numerical pattern is pre-labelled scientific PASS/FAIL. The next step may only be selected after consuming the complete artifact.
