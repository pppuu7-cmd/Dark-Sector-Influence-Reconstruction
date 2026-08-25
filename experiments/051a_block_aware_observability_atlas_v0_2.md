# Experiment 051A — block-aware observability atlas v0.2

## Goal

Convert the qualitative BuyanovGPT table into a machine-readable evidence mask after Exp050A filled the C4 high-k time domain.

This experiment is deliberately **not** a rank estimator. It records what has actually been validated in each response block and preserves missing/blocked channels explicitly.

## Frozen state vocabulary

Each `(direction, block)` cell has exactly one state:

- `active` — validated nonzero response;
- `hard_zero` — exact/stored-precision null under a hard audit;
- `near_null` — measured tiny response, explicitly not zero;
- `degenerate` — active but nearly collinear with a named direction in this block;
- `unknown` — not validated;
- `solver_limited` — desired observable blocked by the current solver/bridge contract.

The validator enforces:

`unknown != zero`, `solver_limited != zero`, `near_null != hard_zero`.

## Blocks

- `B_AP`: background/AP geometry;
- `G_lowk`: low-k full structure;
- `tau_lowk`: low-k temporal response;
- `I_kz`: irreducible scale-time interaction on the family-specific validated domain;
- `S_slip`: metric slip;
- `M_highk`: high-k transfer/free-streaming;
- `C_dv`: density-velocity scalar representability.

Different k-domains remain masked. In particular the C4 high-k time atlas is not concatenated to the C1/C2/C3/C5 low-k matrix by zeros.

## Evidence incorporated

The initial v0.2 mask encodes established findings through F24, including:

- C3/C5 background/AP hard nulls;
- C3 pressure/viscosity low-k and temporal degeneracy plus slip separator;
- C5 nonzero density-velocity representability defect;
- C3 velocity solver limitation;
- C4 low-k near-blindness and hard high-k transfer activity;
- C4 high-k `I(k,z)` near-null at `chi_I ~ 2e-10`, not exact zero;
- low-k interaction hierarchy for C1/C2/C3/C5.

## Output interpretation

A PASS means the evidence-mask semantics are internally consistent and no missing cell has been silently converted to a numeric zero. It does **not** establish:

- an intrinsic response rank;
- a number of fundamental dark-sector degrees of freedom;
- a universal no-hair basis;
- survey distinguishability;
- G7/G8 closure.

The next use of this artifact is to recompute pairwise discriminant coverage and rank **bounds** under explicit masks rather than a zero-imputed common matrix.
