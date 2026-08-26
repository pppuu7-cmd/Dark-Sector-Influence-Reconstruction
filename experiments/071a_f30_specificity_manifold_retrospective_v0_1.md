# Exp071A — F30 specificity and pooled-manifold retrospective audit v0.1

**Date:** 2026-08-27  
**Status:** retrospective/descriptive only; C9/F30 was already unblinded before this audit.

## Motivation

F30 (Exp061A/061B) remains a genuine hard prospective PASS on withheld C9 IDM–baryon: the frozen training-only `(ell,q)` operator produced a non-self-intersecting microscopic-order path and all seven leave-one-redshift rebuilds also passed.  That result is not reopened here.

Two questions were *not* preregistered before the C9 response was seen and therefore must be answered only retrospectively:

1. **Topology specificity:** how many of the other `5!` orderings of the same five fixed C9 points would also satisfy the no-self-intersection gate?
2. **Global manifold transfer:** although pooled C3+C5+C7+C8 training responses are strongly compressed by their first few centered-SVD modes, does withheld C9 actually remain close to that same linear training subspace?

A third descriptive calculation reports within-family centered-SVD spectra for C3, C5, C7, C8 and C9 on the same frozen 7-redshift × 5-k response window.

## Immutable inputs

No solver is rerun.  Only already-unblinded immutable workflow artifacts are consumed:

- C3 GDM: run `32904158849`, artifact digest `sha256:892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`;
- C5 f(R): run `32907619613`, digest `sha256:bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`;
- C7 IDM–DR: run `32920776596`, digest `sha256:fa61a7ae5d53550fd9bf057a4354f8f343e74c18f93a4ce23d5ed964f6dc4c2a`;
- C8 IDM–photon: run `32926084015`, digest `sha256:eb44e29725ace326e707d396158e7c4ed6fd4dccdd86d9ad18e67f42526750b1`;
- C9/F30 IDM–baryon: run `32957427686`, digest `sha256:560f1fe127bfee1cd6fc14b91c455c11babf211a0854a37f6db30d6e5bbea6ed`.

The response window remains exactly

- `k = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`,
- `z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`.

## Calculation A — all-order topology specificity

Use the exact standardized C9 coordinates already emitted by Exp061A.  Enumerate all 120 permutations.  For each permutation apply the exact F30 geometric rule: every adjacent step norm must exceed `1e-10`, and no non-adjacent polyline segments may intersect using the frozen orientation/on-segment tolerance `1e-10`.

Repeat the same ordering in every one of the seven already-emitted leave-one-z standardized coordinate systems.  Report the full-sample and all-LOO robust pass fractions.  No post-hoc significance threshold is introduced.

## Calculation B — pooled training-subspace transfer

For every 7×5 response matrix `R`, flatten and unit-normalize it.  Fit a centered SVD to only the 20 C3+C5+C7+C8 training vectors, exactly matching the response normalization used in the multicoordinate program.  Report the training variance fractions.

For each withheld C9 unit response `x`, define `c=x-mean_training`.  For training subspace dimension `d=1,2,3,4`, report

`rho_d = ||c - Pi_d c||_2 / ||c||_2`,

where `Pi_d` is projection onto the first `d` training centered-SVD right-singular vectors.  This is a descriptive distance, not a preregistered acceptance statistic.

## Calculation C — family-local dimensionality

For each five-point family independently, center its five unit response vectors and report the singular values plus explained/cumulative variance fractions.  These values are window- and grid-dependent descriptive diagnostics.

## Interpretation boundary

Exp071A **cannot**:

- downgrade or upgrade F30;
- claim a discovery or a fundamental dimensionality of the dark sector;
- claim that any trajectory geometry is specific to dark physics;
- certify C5 or authorize the G7 support mask;
- close G7, G8 or G9.

The scientifically useful next test must be prospective and use **known-sector control families whose responses have not yet been generated for this question**.  If ordinary-physics parameter families reproduce the same trajectory geometry, the geometry is a generic smooth-response property rather than a dark-sector-specific law.
