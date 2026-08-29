# Article 3 — exact 5% Layer-A mass-comparison amendment

**Frozen:** 2026-08-30 after synthetic Exp073AC/AC2 exposed a floating-point boundary pathology and before any real DES angular authority or Layer-A support result exists.

## Triggering numerical finding

Exp073AC v0.1 first failed before execution because NumPy was absent. Exp073AC2 repaired only the environment and then reached the synthetic controls.

The exact-threshold synthetic case had positive operator total `D=20` and valid mass `N=19`. Mathematically

`f_invalid=(D-N)/D=1/20=0.05`

and must PASS because the scientific rule is inclusive `f_invalid<=0.05`.

However the diagnostic expression

`1 - N/D`

produced binary64 value `0.050000000000000044`, causing a false rejection when directly compared to binary64 `0.05`.

This is subtractive floating-point cancellation in a diagnostic ratio. It is not evidence for changing the 5% scientific threshold.

## Frozen classification rule

For each row compute positive total operator mass `D>0` and valid mass `N`, with deterministic high-quality summation (`math.fsum` for finite term collections where applicable).

Define the two algebraically equivalent inclusive checks:

1. invalid-mass form: `D - N <= 0.05 * D`;
2. valid-mass form: `N >= 0.95 * D`.

The row is scientifically retained **only if both checks are True**.

The row is scientifically rejected **only if both checks are False**.

If the two mathematically equivalent checks disagree in floating-point arithmetic, the row is `NUMERICALLY_UNRESOLVED_AT_5PCT_BOUNDARY`; Layer A cannot be classified until a prospectively specified higher-precision/reproduction step resolves it. No epsilon is added to the scientific threshold and no ambiguous row is silently retained.

## Diagnostic f_invalid

For reporting, prefer

`f_invalid = (D-N)/D`

over `1-N/D`, because it avoids the exact pathology found by Exp073AC2.

Store both positive masses `D` and `N` and the diagnostic ratio. The scientific retained flag is determined by the dual mass inequalities above, not by a tolerance-expanded ratio comparison.

## Roundoff guards

Before classification require:

- `D` finite and strictly positive;
- `N` finite;
- `N >= 0` up to representation construction (negative valid mass is a numerical failure);
- `N <= D` in the mathematical operator.

If floating arithmetic produces a material violation of `0<=N<=D`, classify numerical/reproduction failure. Tiny endpoint effects must not be used to alter a retained/rejected classification; an ambiguity at the 5% boundary is unresolved, not threshold-relaxed.

## Scientific equivalence

For exact arithmetic,

`D-N <= 0.05D`

is exactly equivalent to

`N >= 0.95D`

and to

`f_invalid <= 0.05`.

Thus this amendment changes only a numerically unstable implementation of the already-frozen inclusive rule. It does not change the domain, threshold, operator weights, mapping, or any observed output.

## Status

- no real Exp073X/AA angular-window value was used to define this amendment;
- no real DES Layer-A result exists yet;
- readiness remains **52%**;
- G7/G8/G9 remain OPEN;
- covariance remains BLOCKED.
