# Experiment 047B — scale-time interaction leave-one-node stability v0.1

**Date:** 2026-08-25  
**Status:** protocol frozen before first target output  
**Parent result:** Exp046.  
**Scope:** common C1/C2/C3/C5 frozen low-k structure atlas; C4 remains outside this domain.

## Question

Are the new interaction statistics

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2}
\]

and

\[
\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}
\]

robust to the exact choice of the seven frozen redshift nodes and five frozen k nodes, or are they dominated by one particular sample point?

This is a deterministic grid-sensitivity stress test, not an independent new-data confirmation.

## Frozen perturbations

Starting from the full `7 x 5` response matrix, generate exactly 12 reduced grids:

- five `leave-one-k-out` variants;
- seven `leave-one-z-out` variants.

No node is chosen after looking at the result and no reweighting is introduced.

For every reduced grid, recompute the orthogonal decomposition from scratch:

\[
R=\mu+T+\tau+I.
\]

## Quantities reported

For every direction:

- full-grid `chi_I`;
- min/max `chi_I` over the 12 reduced grids;
- max absolute drift;
- max multiplicative drift for directions with full `chi_I>=1e-6`;
- whether the Exp046 near-null IDE directions ever cross the pre-existing morphology floor `1e-6`.

For key pairs:

- GDM cs2/cv2;
- GDM cs2/f(R);
- GDM cv2/f(R);
- IDE-alpha/f(R);
- IDE-alpha/beta;

report full, min and max `eta_I` and maximum absolute drift.

Also report whether the **descriptive mechanism-tier ordering**

`IDE near-null < smooth-w < both GDM < designer f(R)`

is preserved in every reduced grid. This ordering is not a hard pass criterion because it was first noticed in Exp045A/046 and therefore is not an independent pre-registered discovery threshold.

## Hard controls

Only algebraic/operator controls can fail the workflow:

1. decomposition relative reconstruction error `<=1e-12`;
2. normalized core/interaction orthogonality `<=1e-12`;
3. pairwise Pythagorean residual `<=1e-12`;
4. finite outputs and nonzero pair distances where `eta_I` is evaluated.

No scientific stability threshold is frozen on the target drifts. This prevents turning the already observed central values into a post-hoc pass gate.

## Interpretation boundary

A stable result would support `chi_I`/`eta_I` as grid-robust response descriptors on the current low-k atlas. It would not establish survey detectability, universal mechanism classes, intrinsic dimension, a new physical law or discovery. A failure of tier ordering or large drift is scientifically useful and must be preserved.
