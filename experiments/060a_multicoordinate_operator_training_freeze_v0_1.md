# Experiment 060A — exact multicoordinate operator training freeze v0.1

Date: 2026-08-26
Status: TRAINING-ONLY FREEZE; C9 RESPONSE FORBIDDEN

## Purpose

Exp058A preregistered a two-coordinate response path after the structural C8 failure of the scalar half-transition law. Exp059A then froze C9 as IDM-baryon scattering and passed a source-only contamination guard. This experiment now fixes the exact numerical construction of `(ell,q)`, its leave-one-redshift recomputation and its geometric path gate before any C9 matter-power response exists.

## Immutable training set

Use only already-unblinded response products:

- C3 GDM run `32904158849`;
- C5 designer-f(R) run `32907619613`;
- C7 IDM-DR run `32920776596`;
- C8 IDM-photon run `32926084015`.

Each contributes five 7x5 response matrices on the standard DSIR grid, for 20 training vectors total. C9 is not training data.

## Frozen response block

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}` and `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

For any model response `R(z,k)=ln(P_model/P_ref)`, require a finite non-zero response norm.

## Localization coordinate ell

Define

`q_k = sum_z R(z,k)^2 / sum_{z,k} R(z,k)^2`

and

`ell = sum_k q_k ln(k/[h/Mpc])`.

Thus `exp(ell)` is the raw-response-power geometric scale centroid. Unlike F27, Exp060A does not impose a slope law on `ell`; it is one axis of a 2D path.

## Shape/orientation coordinate q

Flatten each response matrix in redshift-major order and normalize to unit L2 norm. On the 20 training unit vectors only, subtract their mean and perform deterministic SVD. The second right singular vector is the shape mode `v2`. Fix its otherwise arbitrary sign by requiring the first component with magnitude greater than `1e-12` to be positive.

For any model,

`q = < unit(R) - mean_training_unit_response, v2 >`.

No C9 vector can enter the mean, SVD, sign choice or mode construction.

## Training-only standardization

For the 20 training models compute `(ell,q)` and freeze the positive affine coordinates

`x=(ell-mean_train ell)/sd_train ell`,

`y=(q-mean_train q)/sd_train q`,

with sample standard deviation `ddof=1`. This standardization only conditions the numerical geometry; positive affine axis scaling preserves segment intersections and nonzero adjacency.

## Frozen prospective path gate

For the ordered five C9 source points from Exp059A, later compute `(x_i,y_i)` without any reordering.

PASS requires:

1. every response and coordinate is finite and valid;
2. every adjacent Euclidean step has norm strictly greater than `1e-10`;
3. no pair of non-adjacent polyline segments intersects, including collinear/touching cases, using orientation and on-segment tolerance `1e-10` in standardized coordinates;
4. every leave-one-redshift recomputation has the same PASS/FAIL outcome as the full seven-redshift result.

For leave-one-redshift, the dropped redshift is removed from both training and future C9 matrices, then the training-only mean, PC2, sign and standardization are rebuilt from the remaining six redshifts. No C9 information enters rebuilding.

## Anti-retuning boundary

After first C9 response output, do not rotate modes, flip signs, change `ell`, change centering/scaling, alter tolerances, delete source points, modify k/z nodes, or replace the path topology rule. Any FAIL is permanent scientific evidence for v0.1.

## Gate state

F27 HARD FAIL; F28 retrospective only; F29 HARD PROSPECTIVE FAIL; G7 OPEN; G8 OPEN; G9 OPEN.

## Next step

Run Exp060A training-only freeze and merge it only if all immutable inputs are recovered and the operator record is generated with no C9 response contamination. Only then may a separate experiment generate the first C9 `P(k,z)` and apply this exact gate.
