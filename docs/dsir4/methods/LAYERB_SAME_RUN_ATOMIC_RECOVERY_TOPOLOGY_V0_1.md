# Layer-B same-run atomic recovery topology v0.1

Date: 2026-09-11. Scope: DSIR Article III process/support only. Effect `+0/+0`.

This note is response-blind with respect to Exp073JR and any future recovered Exp073JL numerical output. It records the execution topology implied by the already-frozen Exp073IR traversal and by the independently verified Exp073JQ process result. It does not activate a new scientific gate.

## Fixed source traversal

The frozen Exp073IR common-response traversal has three numerical blocks:

1. DES: production/coarse response over the active subset of the fixed 2001 radial nodes, followed by dense/fine response over the same active z/target sets; coarse/fine responses are compared atomically by the unchanged `compare_response` formula.
2. BOSS GL64: production/coarse and dense/fine responses on the same frozen GL64 nodes and target set; responses are compared by the same unchanged formula and both contribute row finite/nonzero summaries.
3. BOSS GL128: fine/dense-only z-support control; no coarse/fine response difference is formed here. It contributes only the BOSS dense-z finite/positive row-status check against the production labels.

The frozen scientific decision remains the Exp073JL decision: same 2049/4097 guarded lattices, four finite-difference models, centered-cubic interpolation, `h=1e-4`, `REL_TOL=1e-3`, lookup ceiling `1e-12`, same 107-row parent, same invalid-row and retained-dimension criteria.

## Process constraint established by JO/JQ

Exp073JO v0.5 demonstrated that raw response operands produced in different hosted executions can differ in the last bits even with identical committed nodes and solver provenance. Exp073JQ then showed exact `fresh_A == after_history == fresh_B` for all four model roles when the executions were contained in one hosted job. Therefore future coarse/fine scientific comparison operands must not cross runner/process boundaries.

## Permitted chunk topology after an independently verified JR exact PASS

A future full recovery may use fixed, response-blind chunks, but every chunk that evaluates an Exp073JL coarse/fine comparison must complete both operands and the relative-component comparison locally inside one job before emitting an artifact.

For DES chunks, each job must receive an immutable contiguous range of the original `zdes` indices. It must reconstruct the original active masks/targets without alteration, compute the 2049-node and 4097-node responses under the same frozen arithmetic, and reduce locally to: maximum relative component difference, finite/nonzero-change boolean, per-row production/fine atom counts and finite/nonzero summaries, unsupported counters, lookup maximum, k-key provenance, and the exact chunk/index identity. Raw coarse/fine response arrays must not be consumed by a different job for the scientific comparison.

For BOSS GL64 chunks, each job must receive an immutable contiguous range of the original 64 GL nodes and perform the same local coarse/fine comparison and row-summary reduction.

For BOSS GL128 chunks, only the 4097-node response is required by the frozen parent algorithm. Jobs may emit only the finite/positive row-status receipts, support/lookup counters, and provenance required to reproduce `boss_dense_z_disagreement`; no cross-run raw response comparison is permitted or needed.

The final aggregate may combine only associative reductions of already-completed local scientific decisions: maximum of local relative maxima; OR of finite/nonzero-change flags; exact sums of atom/support counters; deterministic row-summary merges; exact conjunction of BOSS dense-z status; and provenance/identity checks. It may not reconstruct a coarse/fine response difference from raw arrays created on different runners.

## Anti-rescue boundary

Chunk boundaries are infrastructure only and must be frozen before the first full recovery output. They may not depend on observed response magnitude, argmax location, row validity, convergence behavior, or numerical result. No tolerance, grid density, interpolation, mask, domain, finite-difference rule, target ordering, quadrature, or scientific acceptance condition may change.

This topology note does not authorize a recovered Exp073JL execution by itself. Such execution is permitted only after the prerequisite Exp073JR exact-equivalence authority exists and a separate prospective full-run contract freezes the chunk partition and aggregate identities.