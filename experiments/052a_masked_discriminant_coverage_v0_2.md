# Experiment 052A — masked discriminant coverage v0.2

## Purpose

After Exp051A made missing/near-null/solver-limited cells explicit and Exp050A completed C4's high-k time block, recompute the hard discriminant graph without constructing a zero-imputed common matrix.

This is deliberately a **coverage / exact hitting-set** calculation, not a response-rank calculation.

## Inputs

- `data/derived/comparison_readiness/block_aware_observability_atlas_v0_2.json`
- `data/derived/comparison_readiness/discriminant_edges_v0_1.json`

Only degeneracy edges whose separator was established by an existing frozen hard gate are eligible for the exact hitting-set calculation.

Old separator names map to current block-aware labels as follows:

- `small_scale_transfer -> M_highk`
- `metric_slip -> S_slip`
- `time_evolution_or_response_sign -> tau_or_full_kz`

## Frozen interpretation rules

1. `unknown`, `solver_limited`, and a missing domain are masked, never zero.
2. `near_null` remains observed but is never promoted to `hard_zero`.
3. A pair with no hard edge in `discriminant_edges_v0_1.json` is **unresolved by the hard edge catalogue**; it is not automatically called degenerate or distinguishable.
4. The exact minimum hitting set applies only to the hard-established edge catalogue.
5. C4 time-domain completion can strengthen its evidence mask, but it cannot create a new pairwise separator edge without a frozen pairwise comparison gate.

## Quantities

The experiment returns:

- normalized hard edges under current block names;
- the exact minimum hitting-set cardinality and all minimum hitting sets;
- pairwise jointly audited blocks and masked blocks for all atlas directions;
- number of atlas pairs currently represented by a hard degeneracy edge versus pairs still lacking pairwise hard-edge evidence.

## Scientific boundary

Even if the exact minimum remains three channel types, this is only a lower bound on separator **types needed by the current hard evidence graph**. It is not

- `N_micro`;
- `N_manifold`;
- `N_repr`;
- a universal `N_disc`;
- a survey-optimal observing program;
- a dark-sector no-hair theorem.

The result is intended to identify which new pairwise gates will add the most information next, especially now that C4 has a genuine high-k `(k,z)` block.
