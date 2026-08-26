# Exp067E — precision-aware CAMB ↔ CLASS convention gate v0.1

Date: 2026-08-26
Status: PREREGISTERED BEFORE FIRST Exp067E CALCULATION

## Purpose

Exp067B is permanently HARD FAIL and is not rerun or rescued. Exp067C/067D localized and causally identified its CAMB rank-one coherence failure as a float32-first transfer-product precision floor in pinned CAMB. Exp067E is a new convention/reference gate whose acceptance criteria are frozen before execution and explicitly separate physical cross-solver agreement from the known implementation precision floor.

## Immutable lineage

- CAMB pin: `fa3f097343fbbe427cc04b4f5f0041c22c6ec764`.
- CLASS pin: `e85808324f51fc694d12e3ed7439552a3c3f9540`.
- Cosmology, physical k nodes, redshift nodes, units, Weyl definition, CLASS construction, sign checks, 3% logarithmic cross-solver thresholds and missing-k^2 negative control are inherited unchanged from Exp067B.
- Exp067B state must remain `HARD_FAIL_UNCHANGED`.

## Precision-aware CAMB control

The official CAMB power arrays are still used for all physical CAMB↔CLASS comparisons. They are not replaced by reconstructed spectra.

For the rank-one numerical control only, read the same CAMB result object's raw float32 transfer values `delta_nonu` and `Weyl`, align the exact internal redshift indices as in Exp067D, promote those stored values to float64 before multiplication, and form

`mm64 = tm64*tm64`, `wm64 = tw64*tm64`, `ww64 = tw64*tw64`.

Require

`max_abs(wm64^2/(ww64*mm64)-1) <= 1e-12`

on every native CAMB node in `0.005<=k<=0.2 Mpc^-1` and at `z={0,0.5,1,2}`.

This tests algebraic rank-one consistency of the stored transfer fields without the separately diagnosed float32 multiplication rounding. It does not recover information lost in storage and does not modify official CAMB powers.

## Physical cross-solver criteria

On the same 20 physical cells as Exp067B (`k={0.005,0.02,0.05,0.10,0.20} Mpc^-1`, `z={0,0.5,1,2}`), retain unchanged:

- finite positive auto-powers;
- finite nonzero cross-powers;
- CAMB/CLASS cross-power sign agreement at every cell;
- `D_mm <= 0.03`;
- `D_WW <= 0.03`;
- `D_Wm <= 0.03`;
- CLASS internal Weyl identity tolerance `1e-10`;
- CLASS rank-one coherence `max|rho^2-1| <= 5e-8`;
- missing-k^2 negative control median log-error `>=5`.

The official CAMB coherence statistic from Exp067B must also be recomputed and recorded, and must remain `>5e-8`; this is a lineage/causal sanity check, not an Exp067E failure condition.

## Hard outcome

PASS iff all source/provenance contracts, physical cross-solver checks, CLASS controls, missing-k^2 negative control and the new promoted-transfer CAMB coherence control pass.

PASS status: `PASS_PRECISION_AWARE_CAMB_CLASS_CONVENTION_GATE_V0_1`.

FAIL status: `FAIL_PRECISION_AWARE_CAMB_CLASS_CONVENTION_GATE_V0_1`.

No solver pin, cosmology, node, unit, definition, sign convention, interpolation rule or threshold may be changed after the first Exp067E output. Infrastructure repairs are allowed only when they do not alter this scientific contract.

## Gate semantics

A PASS would validate the solver convention needed to advance toward G7 while preserving Exp067B as a genuine negative result. Exp067E itself does not close G7/G8/G9 and uses no fresh withheld dark-sector family. Regardless of outcome: `G7 OPEN`, `G8 OPEN`, `G9 OPEN`.
