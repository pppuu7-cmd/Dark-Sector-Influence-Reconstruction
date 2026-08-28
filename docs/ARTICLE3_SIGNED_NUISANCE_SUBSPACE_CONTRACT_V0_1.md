# DSIR Article 3 — signed nuisance-subspace implementation contract v0.1

**Date:** 2026-08-28  
**Status:** architecture-only freeze before Article-3 physical-support/covariance authorization.  
**No G7 statistic is evaluated here.**

## Purpose

Exp071L and Exp071N showed that a selected positive nuisance ray is not the correct object when an interior known-sector parameter can move with either sign. Article 3 must therefore remove the **complete local nuisance span** only after the observational support and covariance gates are valid.

This document freezes the algebra and ordering needed for that future step. It does not select support, inspect covariance eigenmodes, choose data-dependent rank thresholds, or evaluate a relation/null statistic.

## Mandatory gate order

The implementation order is

`true reproduction -> physical support -> finite observation operator -> covariance restriction -> whitening -> signed nuisance construction -> nuisance SVD/projector -> quotient response -> G7 relation/null test`.

Forbidden before upstream gates pass:

- constructing `C^{-1}` or `C^{-1/2}`;
- trimming covariance modes to improve a later G7 statistic;
- selecting nuisance directions by their overlap with the target response;
- choosing SVD rank from a desired residual;
- evaluating G7/G8/G9.

## 1. Support-restricted observation vectors

Let `S` be the already-frozen retained coordinate set produced by the physical-support gate. For any model/parameter point let

`x_S in R^d`

be the finite-operator observation response restricted **only after** the support decision is terminal.

The same ordered coordinate map `S` must be used for:

- target response;
- every nuisance plus/minus realization;
- covariance rows/columns;
- all robustness calculations.

A coordinate may not be removed later because it makes a nuisance projection inconvenient.

## 2. Covariance whitening

Let the valid restricted covariance be

`C_S = L L^T`

for an accepted factorization. For a Cholesky-valid positive-definite covariance define the whitened vector

`w = L^{-1} x_S`.

Then

`||w||_2^2 = x_S^T C_S^{-1} x_S`.

If Cholesky fails, Article 3 must stop at its covariance gate unless a prospectively frozen PSD/pseudowhitening policy already exists. No eigenvalue clipping or diagonal jitter may be introduced after seeing the target/nuisance geometry.

## 3. Two-sided nuisance construction

For each interior nuisance parameter `p_j`, use prospectively fixed finite steps `+delta_j` and `-delta_j` around the same reference point whenever both directions are physically admissible.

Define signed finite responses before tangent compression:

`d_j^+ = x_S(p_j+delta_j) - x_S(ref)`

`d_j^- = x_S(p_j-delta_j) - x_S(ref)`.

Whiten them with the **same** `L`:

`q_j^+ = L^{-1} d_j^+`

`q_j^- = L^{-1} d_j^-`.

A central local tangent is

`n_j = (q_j^+ - q_j^-)/(2 delta_j)`.

The sign of a column is geometrically irrelevant to its span, but both physical signs are required when available to validate that the local-line approximation is meaningful rather than assuming it from one selected ray.

## 4. Linearity / antisymmetry diagnostic

For every two-sided nuisance report

`epsilon_anti,j = ||q_j^+ + q_j^-||_2 / ((||q_j^+||_2 + ||q_j^-||_2)/2)`.

Also report the plus/minus mutual angle and step-size stability where preregistered realizations exist.

These diagnostics do **not** permit post-hoc deletion of a nuisance direction. A failed local-linearity diagnostic must trigger the prospectively declared nonlinear-nuisance handling rule or an explicit `INVALID_FOR_NUISANCE_LINEARIZATION` state; it cannot be repaired by retaining only the sign that gives a favorable G7 residual.

## 5. Nuisance matrix

Collect all resolved local nuisance tangents as columns

`N_w = [n_1, n_2, ..., n_m] in R^(d x m)`.

Every column must correspond to a preregistered nuisance family and immutable parameter step lineage. A nuisance direction that is null or unresolved in the final observation representation must be recorded explicitly; Exp071M shows why nullity in an **intermediate** representation is not sufficient to discard a nuisance globally.

No nuisance may be added/removed after inspecting the target projection merely because it changes the final residual.

## 6. Numerically stable SVD projector

Instead of forming the normal equations directly, compute a thin SVD

`N_w = U Sigma V^T`.

Let `U_r` contain the columns associated with the prospectively defined numerical rank rule. Then the Euclidean projector in whitened space is

`P_N = U_r U_r^T`.

This is algebraically equivalent to

`N_w (N_w^T N_w)^+ N_w^T`

for the same retained numerical column space, while avoiding an unnecessary squaring of the condition number in `N_w^T N_w`.

The rank decision must be independent of the target response. The implementation must persist:

- all singular values;
- numerical-rank rule and threshold;
- retained rank `r`;
- condition diagnostics;
- orthogonality error `||U_r^T U_r-I||`;
- projector idempotence error `||P_N^2-P_N||`.

A numerical-rank rule may be preregistered from machine precision/dimensions or from an external covariance/numerics contract, but may not be tuned to maximize target survival.

## 7. Quotient response

Let the whitened target response be

`y = L^{-1} r_S`.

The nuisance-orthogonal component is

`y_perp = (I-P_N) y`.

Freeze the primary geometry diagnostics

`eta_N = ||y_perp||_2 / ||y||_2`

and

`theta_N = asin(eta_N)`.

Equivalent consistency checks:

- `||U_r^T y_perp||` must be numerically zero;
- `||y||^2 ~= ||P_N y||^2 + ||y_perp||^2`;
- changing the basis inside the same nuisance span must not change `eta_N` beyond tolerance.

## 8. Basis-invariance test

As a required software unit test, replace the nuisance basis by

`N'_w = N_w A`

for one or more nonsingular synthetic matrices `A`. The projector and quotient diagnostics must remain invariant within frozen numerical tolerance:

`P(N'_w) ~= P(N_w)`

`eta_{N'} ~= eta_N`.

This guards against accidentally interpreting individual nuisance columns rather than the subspace they span.

## 9. Sign-invariance test

Independently flip arbitrary nuisance-column signs with a diagonal matrix `D` whose entries are `+1/-1`:

`N'_w = N_w D`.

The projector and `eta_N` must be unchanged to numerical tolerance. This is the subspace counterpart of the Exp071L ray-versus-line correction.

## 10. Near-collinearity stress test

Before scientific use, unit-test the implementation on synthetic nuisance matrices containing:

- exactly duplicate columns;
- exactly opposite columns;
- nearly collinear columns;
- one null column;
- nuisance rank close to observation dimension.

The SVD implementation must remain finite and return the expected subspace dimension under the frozen rank rule. Direct inversion of `N_w^T N_w` is forbidden.

## 11. Representation-resolvability rule

For each nuisance column record the pre-normalization whitened norm. A normalized angle or direction is defined only when

`||n_j|| > epsilon_num`

under the frozen numerical-resolution rule.

If a nuisance is unresolved in the **final support-restricted whitened observation representation**, it may be marked unresolved there. This must not be inferred from transfer-only theory representations; Exp071M/Exp071N demonstrate that a missing primordial or operator contribution can restore an apparently null nuisance.

## 12. G7 firewall

This contract authorizes no G7 evaluation by itself. G7 may be computed only after all of the following are terminal and immutable:

1. Exp073R1 true reproduction PASS;
2. physical-support PASS with frozen retained coordinates;
3. covariance restriction/factorization PASS;
4. complete nuisance-family/step provenance bound;
5. nuisance SVD rank rule frozen before target quotient inspection;
6. signed-linearity diagnostics evaluated according to their preregistered rule.

G8 must remain a fresh post-G7 falsification layer.

## Article-2 provenance bridge

This contract is motivated by, but does not reuse as observational evidence:

- Exp071L: fresh K2(-) validates that a two-sided nuisance is a line rather than a selected positive ray;
- Exp071M: a nuisance can be null in an incomplete/intermediate representation;
- Exp071N: restoring the missing physical response can resolve that nuisance while preserving overlap.

## Current gate state

- `G7 = OPEN`
- `G8 = OPEN`
- `G9 = OPEN`
- covariance/whitening = NOT AUTHORIZED
- nuisance quotient = ARCHITECTURE FROZEN, EXECUTION NOT AUTHORIZED

## Contract verdict

`ARTICLE3_SIGNED_NUISANCE_SUBSPACE_ARCHITECTURE_FROZEN_V0_1`
