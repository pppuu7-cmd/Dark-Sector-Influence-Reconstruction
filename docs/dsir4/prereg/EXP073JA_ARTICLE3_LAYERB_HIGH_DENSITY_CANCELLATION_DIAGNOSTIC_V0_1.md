# Exp073JA — Article 3 Layer-B high-density cancellation diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073IZ AND BEFORE ANY EXP073JA NUMERICAL OUTPUT.

## Bound authority

Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: retained dimension 107, zero invalid rows, `f_B=0`, exact production-vs-dense maximum `0.9998247463807295 > 1e-3`, covariance restriction unauthorized.

Exp073IZ run/job `34452935477 / 102792610244`, artifact `10142351750`, is validated support-only `NATIVE_GRID_MECHANISM_OBSERVED_PLUS_0_PLUS_0`. Its artifact shows non-monotone response behavior over `k_per_decade_for_pk={10,20,40,80}`. Exact algebraic decomposition of the validated artifact shows that from kpd 20 through 80 the endpoint-value derivative term is comparatively stable while a large model-dependent native-grid interpolation-fraction term nearly cancels it and remains resolution-sensitive. This motivates a higher-density cancellation diagnostic; it does not alter the scientific gate.

## Purpose

Determine whether the model-dependent native-k interpolation cancellation approaches a stable fixed-physical-k response when the numerical transfer grid is made substantially denser, or remains non-convergent/oscillatory at the two prospectively frozen historical probes.

## Frozen execution

Use the exact pinned CLASS-IV source `ac627d54e9ce196a08878d1ba33999819925d19c`, exact audited public gauge-invariant `d_m` exposure patch, exact baseline/precision inputs, and exactly the Exp073IR fixed-physical-k log-k interpolation and response arithmetic.

The two frozen probes remain:
- alpha-left: `z=0.7000000000000001`, `k=0.002502504647141259 Mpc^-1`;
- beta-symmetric: `z=0.9351`, `k=0.01860440444314368 Mpc^-1`.

The prospectively frozen diagnostic grid-density ladder is

`k_per_decade_for_pk ∈ {80, 160, 320, 640}`.

For each density compute the same four models used by Exp073IR:
`(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`.

For every model/density/probe record the native physical-k array size/range, bracketing native k values, bracket `d_m` values, exact log-k interpolation fraction and interpolated `d_m`.

Compute exactly:
- alpha-left response `abs((d_m(-h,0)-d_m(0,0))/(-h))`;
- beta-symmetric response `abs((d_m(0,+h)-d_m(0,-h))/(2h))`;
with `h=1e-4`.

Also record signed cancellation decomposition:
- alpha endpoint-value term: evaluate the alpha-perturbed bracket endpoints using the reference model's interpolation fraction, subtract the reference interpolated value, divide by `-h`;
- alpha grid-fraction term: actual alpha-perturbed interpolated value minus that common-fraction value, divide by `-h`;
- beta endpoint-value term: evaluate beta-plus bracket endpoints using beta-minus interpolation fraction, subtract beta-minus interpolated value, divide by `2h`;
- beta grid-fraction term: actual beta-plus interpolated value minus that common-fraction value, divide by `2h`.

The two signed terms MUST sum to the signed total response to binary64 arithmetic as produced by the implementation. Record adjacent-density relative differences `80→160`, `160→320`, `320→640` with the unchanged metric `abs(a-b)/max(abs(a),abs(b))` for finite positive response magnitudes.

## Science firewall

Exp073JA is support-only `+0/+0`. It MUST NOT:
- redefine Exp073IR, alter `REL_TOL=1e-3`, `h=1e-4`, physical parameters/domains, source definitions, interpolation rule, atomization or row membership;
- use kpd 160/320/640 as retrospective replacements for Exp073IR production/dense settings;
- average, smooth, round, extrapolate or tolerance-rescue the result;
- read covariance, whitening, nuisance, relation-null or manuscript-selection information;
- authorize covariance restriction, Layer-B PASS, model authority or manuscript claims.

## Frozen classifications

- `HIGH_DENSITY_CANCELLATION_OBSERVED_PLUS_0_PLUS_0`: complete valid requested records and exact decomposition are produced.
- `INVALID_INFRA_PLUS_0_PLUS_0`: source/hash/build/interface/input/execution prevents valid observation.

No numerical pattern is pre-labelled scientific PASS/FAIL. After a valid artifact is consumed, the next step may prospectively define a new numerical-resolution architecture only if the high-density sequence supplies a defensible convergence mechanism. The original Exp073IR result remains historical and unchanged.
