# Erratum to DSIR response basis v0.1 — raw matter-power gauge dependence

Date: 2026-08-24

This erratum preserves the historical v0.1 specification while blocking one of its intended implementations.

## What remains valid

The following v0.1 elements remain valid and are not retracted:

- anchored relative expansion `r_E` with `z*=0.51`;
- fixed primordial normalization rule;
- AP identity bookkeeping;
- covariance/precision-metric amplitude quotient;
- non-double-counting of derived coordinates;
- frozen redshift and linear-scale support as a working domain.

## What failed

The intended perturbation response

`r_P(k,z)=ln[P_m(k,z)/P_m,ref(k,z)]`

was initially treated as a common coordinate provided each solver used a matched clustering-matter component definition.

A direct same-code gauge audit falsified that assumption for **raw solver `mPk`**. With identical LambdaCDM parameters in pinned `GDM_CLASS@4c87916...`, changing only `gauge=newtonian` to `gauge=synchronous` produced a maximum raw-`mPk` difference of approximately

`9.8434e-5`

inside `1e-3 <= k <= 1e-1 h/Mpc`.

This is substantially above the frozen solver zero-limit floors (`5e-6` for GDM-S1 and `2e-8` for IDE-S1). Therefore the difference cannot be treated as negligible compared with theory-regression accuracy.

## Consequence

**Do not populate a cross-family DSIR matrix with raw solver `mPk` when the contributing families use different gauges.**

Experiment 017 is not erased: it correctly tested the mathematical normalization/quotient properties of the specified coordinates. The empirical gauge audit adds a missing implementation constraint and reopens G2.

## Required successor

Response basis v0.1.1 must use either:

1. a common gauge-invariant/comoving matter-density response validated numerically across gauges and solver families; or
2. a different explicitly observable perturbation channel whose gauge safety is intrinsic.

The current candidate under test for pressureless matter is

`Delta_m = delta_m + 3 Hconf theta_m/k^2`,

with `Hconf=aH`, after independently inferring the sign and coefficient from Newtonian/synchronous transfer outputs of the pinned solver. This formula is not promoted into the common basis until its high-precision gauge audit and cross-solver compatibility tests pass.

See `docs/CONSERVATION_GAUGE_V0_1.md` and `docs/GATES.md` for the controlling gate rules.
