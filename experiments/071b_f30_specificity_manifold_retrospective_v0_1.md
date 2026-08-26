# Exp071B — F30 specificity and pooled-manifold retrospective audit v0.1

**Date:** 2026-08-27  
**Status:** POST-UNBLINDING RETROSPECTIVE / DESCRIPTIVE ONLY.

Exp071A is already reserved on `main` for the G7 physical-provider eligibility ordering ledger. This audit is therefore Exp071B.

## Why this audit exists

F30 (Exp061A/061B) remains a genuine hard prospective PASS on withheld C9 IDM–baryon: the frozen training-only `(ell,q)` operator produced a simple microscopic-order path and every leave-one-redshift rebuild also passed. That prospective result is not reopened.

After unblinding C9, two extra questions became important:

1. How selective is the F30 no-self-intersection condition when the same five fixed C9 points are permuted through all `5! = 120` possible orders?
2. Does withheld C9 actually lie near the pooled C3+C5+C7+C8 *linear* centered-SVD training subspace, or did the two-coordinate F30 gate preserve topology without implying a common linear response manifold?

A third descriptive diagnostic reports centered-SVD spectra separately inside C3, C5, C7, C8 and C9.

## Immutable inputs

No Boltzmann solver is rerun. The audit consumes already-unblinded workflow artifacts only:

- C3 GDM run `32904158849`, digest `sha256:892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`;
- C5 f(R) run `32907619613`, digest `sha256:bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`;
- C7 IDM–DR run `32920776596`, digest `sha256:fa61a7ae5d53550fd9bf057a4354f8f343e74c18f93a4ce23d5ed964f6dc4c2a`;
- C8 IDM–photon run `32926084015`, digest `sha256:eb44e29725ace326e707d396158e7c4ed6fd4dccdd86d9ad18e67f42526750b1`;
- C9/F30 IDM–baryon run `32957427686`, digest `sha256:560f1fe127bfee1cd6fc14b91c455c11babf211a0854a37f6db30d6e5bbea6ed`.

Frozen response window: `k=[0.001,0.003,0.01,0.03,0.1] h/Mpc`, `z=[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`.

## A. F30 topology specificity

Use the exact standardized C9 coordinates already emitted by Exp061A. Enumerate all 120 orders. Apply the same F30 geometry: adjacent step norm `>1e-10`; no non-adjacent segment intersection with orientation/on-segment tolerance `1e-10`. Repeat every ordering in all seven already-emitted leave-one-z coordinate systems.

No post-hoc significance threshold is introduced: report the exact fractions.

## B. Pooled training-subspace transfer

Flatten and unit-normalize every 7×5 response. Fit a centered SVD using only the 20 C3+C5+C7+C8 training vectors. For each withheld C9 state `x`, let `c=x-mean_training` and report

`rho_d = ||c-Pi_d c||_2 / ||c||_2`, for `d=1,2,3,4`,

where `Pi_d` projects onto the first `d` training right-singular vectors. `rho_d` is descriptive, not an acceptance statistic.

## C. Family-local centered SVD

Center the five unit response vectors inside each family separately and report singular values plus explained/cumulative variance fractions. These numbers are explicitly window/grid dependent.

## Epistemic boundary

Exp071B cannot downgrade/upgrade F30, claim fundamental dimensionality, claim dark-specificity, certify C5, authorize the support mask, or close G7/G8/G9.

The next scientifically discriminating move is a **fresh prospective known-sector specificity control**. If ordinary parameters reproduce the same path/low-dimensional geometry, that geometry is a general response property rather than a dark-sector-specific law.
