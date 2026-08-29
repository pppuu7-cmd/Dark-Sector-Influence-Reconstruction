# Article 3 operator-support vs point-coordinate support — synthetic non-equivalence prereg v0.1

**Frozen:** 2026-08-29 before executing this synthetic demonstration.

## Purpose

Demonstrate with deterministic toy kernels that broad positive operator-support leakage and a scalar point-coordinate/common-response check are logically independent. No DES/BOSS artifact, covariance, nuisance quantity or scientific model result is read.

## Frozen constants

Use the already-frozen upper physical bound

`K_MAX = 0.06664762008318016 Mpc^-1`

and an in-range redshift `z=0.5`.

## Test A — scalar point can conceal unacceptable broad leakage

Use two positive support atoms:

- inside: `k=0.04`, weight `0.90`;
- outside: `k=0.10`, weight `0.10`.

Then

`operator_f_invalid = 0.10 > 0.05`

must FAIL the operator-support criterion.

Define only for the counterexample a naive scalar weighted-mean label

`k_scalar = sum(w_i k_i)/sum(w_i)`.

It equals `0.046`, which is inside the upper k bound. With a finite positive final-response vector, a point-coordinate classifier based only on this scalar label would PASS its geometric/envelope part.

The required conclusion is therefore:

`point-coordinate PASS does not imply broad operator-support PASS`.

This does not authorize weighted-mean scalarization in Article 3; it demonstrates why such scalarization cannot replace Layer A.

## Test B — exact operator threshold boundary

Use inside/outside weights `0.95/0.05` at the same k atoms. Require exact floating evaluation compatible with the frozen inclusive rule `operator_f_invalid <= 0.05`: this case must PASS the operator threshold.

## Test C — operator support does not imply common-response-envelope validity

Use an operator envelope with all positive weight inside the physical domain, so `operator_f_invalid=0`. Attach a hypothetical Layer-B component vector containing a zero component, e.g. `[1.0,0.0]`.

Under the already-frozen Layer-B rule, the zero component invalidates the common response envelope.

The required conclusion is therefore:

`broad operator-support PASS does not imply Layer-B common-response-envelope PASS`.

## Acceptance

Synthetic status is PASS only if all three conclusions hold exactly. The output must state:

- `scope=SYNTHETIC_ONLY_NO_REAL_SURVEY_DATA`;
- `scientific_credit=false`;
- G7/G8/G9 remain OPEN;
- no downstream authorization is granted.