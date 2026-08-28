# DSIR ray / line / nuisance-subspace equivalence geometry v0.1

**Date:** 2026-08-28

## Motivation

Exp071I/J/K compared an oriented positive K2 response with positive GDM response directions. Exp071L then showed that the physically allowed negative K2 displacement is almost antiparallel to K2(+) and overlaps both positive GDM directions. This exposes a general geometric distinction that must be explicit in DSIR:

- a one-sided physical deformation is naturally an **oriented ray**;
- an interior scalar nuisance with both signs allowed is naturally an **unoriented line**;
- several jointly allowed nuisances form a **nuisance subspace**.

A single oriented-vector angle is therefore not the correct specificity statistic for every parameter class.

## Metric-aware response space

Let `r` and `n` be response vectors in a declared observable block, and let `M` be a positive-definite comparison metric. In the current Exp071 series `M=I` (ordinary Euclidean metric). A future observational implementation may use a frozen whitened metric such as a valid covariance inverse after physical support and covariance gates are closed.

Define

`||x||_M = sqrt(x^T M x)`.

All equivalence objects below are block- and metric-conditioned.

## 1. Oriented-ray angle

For two physically oriented response rays,

`cos(theta_ray) = (r^T M n)/(||r||_M ||n||_M)`,

with

`theta_ray in [0, pi]`.

This retains sign/orientation information. It is appropriate only when reversing the parameter displacement is physically forbidden or represents a different physical hypothesis.

Exp071J used this object for positive K2 versus positive GDM and found

- `theta_ray(K2+, cs2+) = 166.4386944060 deg`;
- `theta_ray(K2+, cv2+) = 164.9270967302 deg`.

Those values are valid oriented-ray results.

## 2. Two-sided nuisance-line angle

If `n` is an interior nuisance tangent and both `+n` and `-n` are physically allowed, the relevant object is the line

`L(n) = {a n : a in R}`.

The angle from response `r` to this line is

`theta_line(r,n) = arccos(|r^T M n|/(||r||_M ||n||_M))`

or equivalently

`theta_line = min(theta_ray, pi-theta_ray)`.

Thus

`theta_line in [0, pi/2]`.

A near-180-degree oriented angle is **near the same nuisance line**, not strongly separated from it.

Applying this to the Exp071J positive-K2 angles gives immediately

- `theta_line(GDM cs2+, K2 line) = 13.5613055940 deg`;
- `theta_line(GDM cv2+, K2 line) = 15.0729032698 deg`.

Exp071L then independently realized the opposite K2 displacement with a fresh pinned CLASS run and measured

- `theta_ray(K2-, GDM cs2+) = 13.5502602743 deg`;
- `theta_ray(K2-, GDM cv2+) = 15.0708844313 deg`.

The differences from the ideal line-angle prediction are only

- `0.0110453197 deg` for cs2;
- `0.0020188384 deg` for cv2.

This agrees with the measured K2(+)/K2(-) mutual angle `179.9078020829 deg` and antisymmetry error `0.0029922493`.

Therefore Exp071L is not merely a special counterexample: it validates the line-geometry interpretation of the K2 nuisance to high accuracy on the tested finite step.

## 3. Multi-dimensional nuisance-subspace angle

Let the columns of matrix `N` span all allowed nuisance response directions in a declared block. The metric-orthogonal projector onto the nuisance span is

`P_N = N (N^T M N)^+ N^T M`,

where `+` denotes the Moore-Penrose pseudoinverse, required if nuisance directions are linearly dependent or nearly redundant.

For target response `r`, define

`r_perp = r - P_N r`.

The fraction of response surviving nuisance projection is

`eta_N(r) = ||r_perp||_M / ||r||_M`.

A corresponding subspace angle is

`theta_N(r) = asin(eta_N(r))`,

with `theta_N in [0, pi/2]`.

Interpretation:

- `theta_N -> 0`: target response lies inside or very near the nuisance span;
- large `theta_N`: a substantial component survives every allowed linear nuisance combination;
- only this subspace-aware quantity can support a claim of local linear specificity against several two-sided nuisance parameters.

## 4. Required ordering for observational use

The metric/subspace construction must obey the existing DSIR fail-closed ordering:

`physical support -> valid finite operator -> covariance/whitening -> full signed nuisance span -> nuisance projection -> relation/null test`.

Do **not** define `M=C^{-1}` or a nuisance projector before the relevant observational support and covariance objects have passed their own gates.

The Exp071 calculations are theory-space Euclidean controls only. They motivate the geometry but do not authorize an observational nuisance quotient.

## 5. Consequence for Article 2

The strongest defensible Article-2 claim is not “velocity separates K2 from GDM”. It is:

> Response equivalence is conditioned both on the observable channel and on the geometric class of the comparison object. The positive K2 response ray is nearly opposite the tested positive GDM rays in velocity-shape space and is robust to support ablations, but the physically two-sided K2 nuisance line lies only about 13.6-15.1 degrees from those GDM rays.

This turns the Exp071L negative result into a general DSIR methodological result.

## 6. Consequence for Article 3

Article 3 must build nuisance controls as signed spans/subspaces. A chosen positive nuisance orientation cannot be used as the object being quotiented.

Once an admissible observational metric `M` exists, the natural frozen statistic is the nuisance-orthogonal fraction `eta_N` (or equivalently `theta_N`) computed with the complete preregistered nuisance basis.

This provides a direct formal bridge from Article-2 response geometry to Article-3 covariance/nuisance closure.

## Provenance

- Exp071J positive-ray result: run `33182705074`.
- Exp071K support localization: run `33183729426`, artifact `9690784568`.
- Exp071L two-sided test: run `33184079909`, artifact `9690954372`.
- Exp071L terminal summary: `data/derived/exp071l_two_sided_k2_velocity_shape_nuisance_summary_v0_1.json`.
- Orientation boundary: `docs/ARTICLE2_EXP071I_J_K_L_ORIENTATION_BOUNDARY_2026-08-28.md`.

G7/G8/G9 remain OPEN.
