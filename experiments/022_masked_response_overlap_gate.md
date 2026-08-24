# Experiment 022 — validity-masked response overlap gate

Date: 2026-08-24
Status: METHOD GATE

## Problem

The six DSIR control families do not necessarily have validated predictions for every response channel, redshift, or scale. Filling an undefined response with zero or a catalog mean would create artificial geometry in response space and can generate spurious low rank or false relations.

## Frozen representation

Store a response matrix `X[model,feature]` together with an explicit boolean validity mask `M` of identical shape. Production storage uses `NaN` wherever `M=False`.

No zero, mean, nearest-neighbour, or model-class imputation is permitted before a missing-data method has passed an independent synthetic and null-calibrated gate.

## Common-subspace rule

For a selected model set `S`, the admissible feature block is

\[
J_S=\{j:\;M_{ij}=1\;\forall i\in S\}.
\]

Only

\[
X_{S,J_S}
\]

may enter an ordinary global covariance whitening/SVD calculation.

Pairwise or family-subset comparisons may have larger intersections, but such local blocks must not be concatenated and interpreted as one global rank without a separately validated masked-factor method.

## Overlap graph

Define

\[
N_{ij}=\sum_a M_{ia}M_{ja}.
\]

An edge exists when `N_ij >= n_min`. Disconnected components are observationally incomparable islands for the chosen channel definition and cannot support a single global manifold/rank claim.

Connectivity is necessary but not sufficient: even an overlap-connected catalog may lack one feature block common to all models.

## Regression requirements

1. global common-subspace extraction uses only the exact validity intersection;
2. pair subsets can expose larger local overlaps without changing the global block;
3. finite values in cells marked invalid are rejected as forbidden imputation;
4. disconnected overlap islands are detected explicitly.

Implementation: `src/dsir/response_matrix.py`.
Tests: `tests/test_response_matrix.py`.

## Scientific consequence

The first six-family matrix will report both:

- the common production block used for global `R_model(pi)`;
- the larger local/discriminant blocks, with explicit masks and overlap graph.

No absent model/channel value is interpreted as a physical zero.
