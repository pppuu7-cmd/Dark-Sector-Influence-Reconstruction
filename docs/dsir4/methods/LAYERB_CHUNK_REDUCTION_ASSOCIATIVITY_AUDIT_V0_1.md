# Layer-B chunk reduction associativity audit v0.1

Date: 2026-09-11. Scope: DSIR Article III support/process only. Effect `+0/+0`.

Purpose: prove, before any full recovered Exp073JL output is observed, that the scalar/row receipts proposed for a same-run chunked execution can be merged without changing the already-frozen Exp073IR/Exp073JL decision semantics. This note does not authorize a run.

## Frozen reductions in the parent algorithm

The original Exp073IR traversal reduces numerical atoms into the following state:

- convergence maximum: `max_relative_component_difference = max(previous, local_relative_max)`;
- finite/nonzero change: logical OR over any coarse/fine finite or positive-mask disagreement;
- per-row `atom_count`: integer sum over active atoms;
- per-row `finite_nonzero`: logical AND over all active response elements being finite and strictly positive;
- per-row `min_components[j]`: minimum over finite values for component `j`;
- production/fine row label: `(atom_count > 0) and finite_nonzero`;
- BOSS dense-z status: logical AND over all GL128 nodes of the required finite-and-positive condition for each retained row;
- unsupported target count: integer sum;
- requested-node coordinate mismatch: maximum;
- native transfer key set: set union.

## Associativity / deterministic merge proof

Each permitted receipt field has an order-independent associative merge:

1. maxima use `max`, which is associative and commutative for the finite nonnegative quantities admitted by the frozen execution;
2. failure/change flags use logical OR, which is associative and commutative;
3. counts use exact integer addition, which is associative for the bounded counts here;
4. row finite/nonzero status uses logical AND, which is associative and commutative;
5. per-component minima use `min` over finite values, associative and commutative; the existing `+inf` identity is preserved until final JSON conversion to `null` when no finite value exists;
6. BOSS dense-z validity uses logical AND;
7. k-key provenance uses set union.

Therefore a fixed partition of the original atom stream may merge these receipts in any deterministic chunk order and reproduce the same final decision function, provided that every coarse/fine response comparison itself is completed locally before reduction and no raw scientific operand is compared across runner/process boundaries.

## Non-associative / forbidden exports

The following must not be reconstructed across chunks or runners:

- a coarse/fine relative difference from raw responses produced in different execution contexts;
- finite-difference alpha or beta response columns assembled from model operands produced on different runners;
- interpolation from partial node tables;
- any result-dependent change in active masks, chunk boundaries, target ordering, quadrature nodes, grid density, tolerance or row selection.

Argmax telemetry, if recorded, is diagnostic only. If a global argmax identity is desired, the merge must use a prospectively fixed deterministic tie-break (for example lexicographic original atom ordinal) and must not affect the frozen maximum value or classification.

## Required aggregate invariants for a future full recovery

A future aggregate must fail closed unless all chunk identities form the exact frozen partition with no gaps or overlaps, every receipt has matching source/solver/grid/prereg fingerprints, and final structural totals reproduce the original traversal topology. Any missing/duplicate chunk or provenance mismatch is infrastructure-invalid, not numerical non-convergence.

Conclusion: receipt-level aggregation is mathematically compatible with the frozen parent decision; the process safety condition remains that scientific operands are formed and compared locally within one execution context.