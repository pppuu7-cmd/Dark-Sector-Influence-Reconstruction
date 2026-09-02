# DSIR research note — nuisance quotient / Schur-complement duality v0.1

**Date:** 2026-09-03  
**Scope:** mathematical research only; nonclassifying `+0/+0`; no G7 authorization and no readiness change.  
**Downstream prohibition:** this note is not a preregistered scientific gate and must not be used to bypass the frozen Article-3 order.

## 1. Setup on the already-supported data subspace

Let the physical support-validity mask and covariance restriction already have been frozen and applied. Work only on the retained data coordinates. Let

- `C` be the restricted symmetric positive-definite covariance on that retained subspace;
- `S` be the supported signal-response/design matrix whose columns span the signal directions to be tested;
- `N` be the supported nuisance tangent matrix whose columns are nuisance directions.

Choose any whitening factor `W` satisfying

`W^T W = C^{-1}`.

A Cholesky implementation uses `C = L L^T` and `W = L^{-1}`. Define

`S_t = W S`,  `N_t = W N`.

The following theory is independent of the particular valid whitening factor.

## 2. Quotient-projector formulation

Let `Q` have orthonormal columns spanning `col(N_t)`. When `N_t` is rank deficient, `Q` is formed only from the numerically retained singular directions under a prospectively frozen rank/SVD rule; no arbitrary threshold is introduced here.

Define the orthogonal nuisance projector

`P_N = Q Q^T`

and quotient projector

`P_perp = I - P_N`.

The nuisance-quotiented signal Gram/Fisher matrix is

`G_q = S_t^T P_perp S_t`.

Immediate exact-theory properties:

1. `G_q` is symmetric positive semidefinite.
2. `G_0 - G_q = S_t^T P_N S_t` is positive semidefinite, where `G_0 = S_t^T S_t`.
3. Therefore `0 <= G_q <= G_0` in Loewner order.
4. A signal direction `v` is completely nuisance-degenerate iff `P_perp S_t v = 0`, equivalently `v^T G_q v = 0`.

## 3. Schur-complement / pseudoinverse formulation

For arbitrary-rank `N_t`, the orthogonal projector onto `col(N_t)` is

`P_N = N_t (N_t^T N_t)^+ N_t^T`,

where `+` is the Moore-Penrose pseudoinverse. Hence

`G_q = S_t^T S_t - S_t^T N_t (N_t^T N_t)^+ N_t^T S_t`.

Using `S_t=W S`, `N_t=W N`, and `W^T W=C^{-1}` gives

`G_q = S^T C^{-1} S
       - S^T C^{-1} N (N^T C^{-1} N)^+ N^T C^{-1} S`.

Thus the whitened quotient projector and the covariance-weighted Fisher Schur-complement marginalization are dual implementations of the same matrix on the supported data subspace.

For full-column-rank nuisance tangent `N`, the pseudoinverse reduces to an inverse and this is the usual Fisher Schur complement of the nuisance block.

## 4. Basis invariance of nuisance marginalization

Let nuisance coordinates be changed by any invertible matrix `R`, `N' = N R`. Then `col(W N') = col(W N)`, so the quotient projector is unchanged exactly:

`P_perp(N') = P_perp(N)`.

Consequently

`G_q(N') = G_q(N)`.

For rank-deficient or overcomplete nuisance parameterizations the stronger invariant object is the column space itself. Any two matrices whose whitened columns span the same nuisance subspace must produce the same exact projector and the same `G_q`, irrespective of the number or normalization of nuisance columns.

Prospective numerical QA should therefore compare the resulting projector/Gram object, not individual singular vectors (whose signs and bases inside degenerate singular subspaces are non-unique).

## 5. Whitening invariance

If `W_1^T W_1 = C^{-1}` and `W_2^T W_2 = C^{-1}`, then on the retained data space there exists an orthogonal map `O` such that `W_2 = O W_1` for square nonsingular whiteners. Hence

`S_t2 = O S_t1`,  `N_t2 = O N_t1`.

The nuisance projector transforms covariantly,

`P_perp,2 = O P_perp,1 O^T`,

and therefore

`S_t2^T P_perp,2 S_t2 = S_t1^T P_perp,1 S_t1`.

So `G_q` is whitening-invariant in exact arithmetic. A prospective implementation audit can compare Cholesky whitening to a symmetric-eigendecomposition whitening, but such a comparison must use a preregistered numerical acceptance rule rather than post-hoc tolerance.

## 6. Rank/SVD handling — prospective requirements

The scientific result depends on the nuisance subspace rank. Therefore rank handling must be frozen before downstream use.

Recommended prospective contract:

1. Form `N_t = W N` only after frozen support restriction and covariance validation.
2. Compute an SVD `N_t = U Sigma V^T` with a fixed library/environment contract.
3. Store the full ordered singular spectrum canonically.
4. Do not choose a rank threshold from downstream desired behavior.
5. Predeclare the singular-value decision rule and the exact-threshold ambiguity policy.
6. If a singular value lies in a preregistered ambiguity interval around the decision boundary, classify the rank decision `numerically_unresolved` rather than forcing inclusion/exclusion.
7. Require the retained nuisance rank and retained signal dimension to satisfy the already frozen downstream dimensional constraints before quotient use.

A rank decision should be stable under nuisance-column rescaling only if the rank rule itself is scale-aware. A dimensionless rule based on `sigma_i / sigma_max` is basis-normalization sensitive under general non-orthogonal column rescaling, so it is not automatically nuisance-coordinate invariant. A preferable scientific construction is to freeze physically meaningful nuisance parameter units/priors before building `N`, or to define rank from an invariant metric on nuisance parameter space if such a metric is part of the physical model.

This issue must be resolved prospectively; no threshold is selected in this note.

## 7. Generalized surviving-signal spectrum

Define

`G_0 = S_t^T S_t`,  `G_q = S_t^T P_perp S_t`.

On the supported signal subspace where `G_0` is positive definite, consider

`G_q v = lambda G_0 v`.

From `0 <= G_q <= G_0`, every exact generalized eigenvalue obeys

`0 <= lambda <= 1`.

Interpretation:

- `lambda = 1`: the corresponding signal combination is orthogonal to the nuisance tangent subspace and survives nuisance quotient completely;
- `lambda = 0`: the signal combination lies entirely inside the nuisance tangent span and is completely removed;
- `0 < lambda < 1`: partial overlap with nuisance directions.

If `G_0` is singular, first restrict to `range(G_0)` using a prospectively frozen signal-rank rule; do not feed null signal directions to a generalized eigensolver and then interpret arbitrary infinite/undefined eigenvalues.

An equivalent stable exact-theory formulation is to choose `R_0` with `R_0^T R_0 = G_0` on the retained signal range and diagonalize

`H = R_0^{-T} G_q R_0^{-1}`.

Then `H` is symmetric PSD with spectrum in `[0,1]`.

## 8. Invariance/consistency checks required before scientific use

A future preregistered QA gate should require all of the following on a synthetic matrix family with known ranks and degeneracies, followed by the actual supported matrices only after all upstream gates pass:

- quotient-vs-Schur equality under the frozen numerical criterion;
- symmetry of `G_q` under the same criterion;
- PSD diagnostics for `G_q` and `G_0-G_q`;
- nuisance-basis invariance under predetermined invertible nuisance transformations;
- orthogonal whitening invariance under predetermined alternate whitening constructions;
- invariance of generalized eigenvalues under invertible signal-basis changes;
- exact handling of duplicated nuisance columns and exactly dependent nuisance columns;
- explicit `numerically_unresolved` behavior at preregistered rank-boundary stress cases;
- no arbitrary clipping of generalized eigenvalues into `[0,1]`; excursions must remain visible as numerical diagnostics.

## 9. Relation to DSIR gate order

This note only develops the mathematics for the already-frozen later sequence

`covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control`.

It does **not** establish that the physical forward/power-input bridge, support-validity mask, Layer A/B prerequisites, covariance, nuisance tangent, or G7 authorization are complete. It must not be used to jump to G8.

## 10. Current research conclusion

The projector and Schur-complement routes are not competing scientific definitions; they are exact-theory dual implementations of the same nuisance quotient, provided they use the same supported data space, covariance metric, and nuisance tangent span. This duality is useful as a future implementation cross-check. The scientifically delicate unresolved component is not the algebra but the prospective, invariant treatment of numerical nuisance rank and any threshold ambiguity.
