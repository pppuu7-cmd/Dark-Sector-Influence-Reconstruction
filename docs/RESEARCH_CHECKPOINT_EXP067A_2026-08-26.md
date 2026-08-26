# DSIR recovery checkpoint — Exp067A (2026-08-26)

## Frozen question

Can the exact released ACT DR6 × unWISE Blue/Green selected `Clgg+Clkg` covariance be bound to the already frozen 26-coordinate observable ordering and whitened by an unmodified direct Cholesky factor, with no covariance repair or post-output retuning?

The scientific contract was committed on `main` before the first execution in `experiments/067a_act_unwise_observational_covariance_whitening_v0_1.md`.

## Hard result

Push workflow run `32994782105`, job `98261038810`, execution commit `2b02556bcac07c475d160736241c8e8b8ed0d1fc` returned

`PASS_ACT_UNWISE_OBSERVATIONAL_COVARIANCE_WHITENING_V0_1`.

All preregistered subtests passed:

- A1 provenance/order: exact 26-coordinate order `[Blue gg(6), Blue kg(7), Green gg(6), Green kg(7)]` reproduced;
- A2 raw selected covariance: shape `26×26`, finite, strictly positive diagonal, symmetry ratio exactly `0` against frozen `1e-12` threshold;
- A3 direct `numpy.linalg.cholesky`: PASS; reconstruction relative infinity residual `7.799310879558051e-17 <= 5e-12`;
- diagnostic eigenvalue range: `lambda_min=1.2742353176342933e-17`, `lambda_max=3.980349119528573e-15`;
- A4 solve-built `W=L^{-1}`: `||W Sigma W^T-I||_inf = 1.0425503003180775e-15 <= 5e-10`;
- A5 deterministic seed-`20260893` whiten/unwhiten round-trip: relative infinity error `3.1871930361769926e-16 <= 5e-12`.

No symmetrisation, Hartlap rescaling, jitter, shrinkage, eigenvalue clipping, diagonal loading, pseudoinverse, nearest-PSD projection, scale-cut change or coordinate reorder was used.

Frozen operator hashes:

- selected covariance float64 bytes: `df7e285c40009e0ba20cc5d920342e1066ceff69d277fdf3233ac63463ffddb9`;
- Cholesky `L`: `6a30b1792d8b3f29ae66102dadb285f394f6aa4c30cba29dc3c3234a1897f109`;
- whitener `W`: `b32e59a98b6910427ac5026bc3f882ea8b0934b65de9abe44c599e1c7ec66822`.

These hashes are the binding targets for any later G7 observational residual statistic using this covariance convention.

## Scientific meaning

The covariance/whitening prerequisite identified by the literal G7/G8 closure audit is now satisfied for the pinned ACT×unWISE 26-coordinate block. This is an observational-operator PASS only. It is not itself a nontrivial cross-channel relation and therefore does not close G7.

A future G7 candidate must still:

1. use at least two independently meaningful response/observable blocks;
2. quotient exact identities and declared measurement-degeneracy directions;
3. use the frozen observational kernel and this bound whitening convention where applicable;
4. freeze one mathematical relation and acceptance statistic from training/control information only;
5. pass a nontrivial null/permutation or covariance-coordinate control;
6. freeze all of the above before choosing a fresh withheld family for G8.

## Convention issue discovered immediately after Exp067A

The next law search must not begin until the physical solver convention of the ACT projector's three independent spectra is audited. CAMB documentation defines its power-spectrum variable `Weyl` as `k^2*(phi+psi)/2`, not simply `(phi+psi)/2`. Its raw matter-transfer-table interface then applies an additional `1/k^2` normalization to transfer columns. Therefore a CLASS `phi/psi` table cannot be inserted into the ACT `Pk_interpolator` contract by name or by a naive transfer-column comparison.

This convention correction is to be recorded separately and validated on a fixed LambdaCDM reference before any CLASS dark-sector family is projected through ACT×unWISE.

Top-level state remains **G7 OPEN, G8 OPEN, G9 OPEN**.
