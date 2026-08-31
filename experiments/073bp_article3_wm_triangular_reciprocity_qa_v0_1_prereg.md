# Exp073BP — Article-3 Wm triangular-reciprocity general-coupling QA v0.1

**Project:** DSIR only.  
**Classification:** nonclassifying mathematical/source-equivalence and execution QA.  
**Scientific readiness increment:** `+0`.  
**Draft/data readiness increment:** `+0`.

## Purpose

Test whether the Wm general-coupling compact projection can be computed with approximately half of the expensive Wigner/cell evaluations by using the exact reciprocity of the Wm coupling core under `ll2 <-> ll3`, while preserving the frozen ascending-row accumulation order for every compact-A element.

This experiment is independent of and may not modify active Exp073BJ or Exp073BO.

## Mathematical basis

For Wm the frozen general-coupling call is

`get_general_coupling_matrix(pcl,0,2,0,2)`.

NaMaster v2.7 computes

`G[l2,l3] = (2*l3+1) * C[l2,l3]`,

where

`C[l2,l3] = sum_l1 pcl[l1]*(2*l1+1)/(4*pi) * W000(l1,l2,l3) * W02(l1,l2,l3)`.

The Wigner-3j permutation and simultaneous-m sign symmetries imply the exact mathematical identity

`C[l2,l3] = C[l3,l2]`

for this `(0,2,0,2)` channel. Hence mathematically

`G[l3,l2] = C[l2,l3]*(2*l2+1)`.

This experiment tests whether using a single numerical evaluation of `C[l2,l3]` for each unordered pair remains exactly compatible with the current stock compact projection at tractable scales.

## Operation-count motivation

For frozen full-scale `lmax=12287`, direct stock traversal contains exactly

`927,712,843,788`

accepted `l1` terms over ordered `(l2,l3)` pairs with `l2,l3>=2`.

Upper-triangle traversal including the diagonal contains

`463,913,044,996`

accepted terms. Therefore the mathematical core work is reduced to fraction

`0.5000610351601567`

before implementation overhead. This is an operation-count statement, not a frozen runtime guarantee.

## Frozen inputs and scales

Use exactly the same deterministic PCL construction and Article-3-truncated band edges as Exp073BO at:

- `lmax=95`;
- `lmax=255`;
- `lmax=511`.

PCL scalar definition:

`pcl[ell] = float(1 + (ell % 11)) / float((ell + 1)*(ell + 2))`.

## Frozen stock reference

Reuse the immutable Exp073BO stock-reference implementation commit `06f19e947a9a9ddb7b569856a50aca39b220c657` to compute full stock `G` and frozen-order compact `A_stock` in a fresh child process.

## Frozen triangular native algorithm

Use the exact runtime `drc3jj` symbol from PyMaster/NaMaster 2.7, as in Exp073BO. Do not independently implement Wigner-3j.

Initialize canonical `[nband,L]` float64 `A_tri` to zero.

For `l2=2..lmax` ascending and `l3=l2..lmax` ascending:

1. numerically evaluate the source core `C(l2,l3)` once using the same ascending `l1` loop and source expression;
2. let `b2=band(l2)` and add `C*(2*l3+1)` to `A_tri[b2,l3]`;
3. if `l3!=l2`, let `b3=band(l3)` and add `C*(2*l2+1)` to `A_tri[b3,l2]`.

After all unordered pairs, divide each band row exactly once by its integer width converted to float64.

### Accumulation-order property frozen before result

For a fixed compact element `A[b,j]`, contributions are indexed by source row `r` in band `b`.

- terms with `r<j` are generated when outer loop `l2=r`, in ascending `r`;
- `r=j` is generated on the diagonal;
- terms with `r>j` are generated during outer loop `l2=j`, with inner `l3=r` ascending.

Therefore all contributions to each `A[b,j]` are added in ascending source-row `r`, matching the frozen `compress_general` order. This is a prospective algorithmic invariant, not a result-dependent interpretation.

## Compilation and hosted replication

Compile with exactly:

`gcc -O2 -std=gnu11 -shared -fPIC ... -lm`.

Use four independent `ubuntu-24.04` replicas A-D with exact PyMaster/NaMaster 2.7 conda lineage and all known thread controls set to one.

Run stock and triangular native paths in separate child processes and record wall time and max RSS.

## Frozen result classes

### `BP_Q1_TRIANGULAR_RECIPROCITY_EXACT_PASS`

Requires for all three scales and all four replicas:

- `numpy.array_equal(A_stock,A_tri)`;
- canonical SHA equality within each replica;
- one cross-host SHA for `A_tri` at each scale.

### `BP_Q2_TRIANGULAR_RECIPROCITY_EXACT_FAIL`

Any complete exact mismatch within a replica or cross-host triangular mismatch. Numerical closeness cannot rescue this exact class.

For diagnosis only, report max/mean absolute difference and differing-entry count.

### `BP_Q3_INFRASTRUCTURE_INCOMPLETE`

Any missing scale/replica preventing the frozen exact comparison.

## Scientific firewalls

All outcomes are `+0/+0`. A Q1 result qualifies only the tractable-scale execution algorithm. It does not change Exp073AQ, does not change active Exp073BJ, and does not authorize a full-scale Track-A successor without a separate prospective preregistration. No support/covariance/whitening/nuisance/relation/null/G8 information is used.
