# Exp073Z — Article 3 DES radial-kernel authority QA v0.1

**Frozen:** 2026-08-30, after Exp073Y raw-input PASS and before any current DES physical-k/support fraction is evaluated.

## Purpose

Exp073Z constructs and content-binds the **radial-only** DES Y1 Wm/WW support factors under the already-frozen Article-3 background geometry. It is deliberately independent of the NaMaster angular windows and therefore cannot classify Layer A.

It must not compute physical `k`, multiply by an angular bandpower window, evaluate `f_invalid`, or retain/reject an observation row.

## Input authorities

Bind exactly the Exp073Y byte/logical-array authorities:

- common released `Z_MID`: 400 rows, `0.0051..3.9951`, nominal spacing `0.01`, SHA256 `b93b65adb24b98fd76a41486a1352978459af2836f533d0adadd0ca390dca89b`;
- source file SHA256 `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`, HDU 1, `BIN1..BIN4`;
- lens file SHA256 `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`, HDU 7, `BIN1..BIN5`;
- all 9 released BIN arrays are finite and non-negative;
- source raw trapezoid integrals are approximately unity and lens integrals are unity to floating precision.

Use no source-bin photo-z membership file here. The exact 2.738-GB source-binning object remains upstream provenance of the R1 source count masks, while the radial `n(z)` values themselves are exactly the byte-bound source distribution file above.

## Frozen background geometry

Inherit `docs/ARTICLE3_DES_BACKGROUND_GEOMETRY_INHERITANCE_2026-08-30.md` exactly:

- `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- `H0=67.0`;
- `ombh2=0.0224`;
- `omch2=0.1200`;
- `mnu=0.0`;
- `nnu=3.046`;
- `TCMB=2.7255 K`;
- `YHe=0.24`;
- `tau=0.0`;
- `w=-1.0`, `wa=0.0`;
- `chi(z)` in Mpc and `H(z)` from the pinned CAMB background.

Exp073Z does not use the old KiDS positive lower-k cutoff because it does not calculate k at all.

## Frozen raw-distribution treatment

For each of the 4 source and 5 lens released BIN arrays:

1. use the 400 released `Z_MID` values exactly;
2. compute its normalization constant by ordinary trapezoidal integration on those 400 released midpoint nodes;
3. divide by that constant before any later crop or interpolation;
4. do not smooth, shift, clip or re-bin the distribution;
5. no negative-value policy is needed for this release because Exp073Y established zero negative samples; any negative sample in the bound input is an authority mismatch.

Outside the released midpoint domain, direct `n(z)` interpolation is zero.

## Source lensing efficiency

For normalized source bin `i`, define tail integrals directly on the released source `Z_MID` grid:

`T0_i(z) = integral_z^infinity n_i(z_s) dz_s`

`T1_i(z) = integral_z^infinity n_i(z_s)/chi(z_s) dz_s`.

The deterministic numerical representation uses cumulative trapezoids on the released source grid and piecewise-linear interpolation of the resulting tail functions. For evaluation redshifts below the first released midpoint, use the complete tail values; above the last released midpoint use zero.

Then

`g_i(z) = T0_i(z) - chi(z) * T1_i(z)`.

This gives the correct finite low-z limit without ever dividing an evaluation-grid zero-distance cell by `chi(0)`.

Require all `g_i` values to be finite. Tiny negative roundoff values with magnitude `<=1e-12` may be set to zero **only as a numerical roundoff canonicalization**; any value below `-1e-12` is invalid.

## Frozen radial support factors

For every evaluation grid point:

### Wm

For 5 lens bins `a` and 4 source bins `i`:

`B_Wm[a,i](z) = abs(n_lens,a(z) * g_i(z) / chi(z))`.

At exactly `z=0`, where the lens interpolation is zero and `chi=0`, define the continuous bookkeeping value `B_Wm=0` rather than evaluating `0/0`.

This gives exactly 20 distinct Wm radial kernels.

### WW

For the 10 unordered source pairs `i<=j`:

`B_WW[i,j](z) = abs((c/H(z)) * g_i(z) * g_j(z))`, with `c=299792.458 km/s`.

This gives exactly 10 distinct WW radial kernels.

These are positive support-domination factors only. No matter power spectrum, GR Poisson closure, nonlinear boost, bias amplitude or covariance is used.

## Frozen evaluation grids and convergence

Both grids cover `z=0` through `z=4.0` inclusive and are formed by the sorted unique union of:

- a uniform grid from 0 to 4.0;
- all 400 released `Z_MID` nodes;
- the exact Article-3 domain boundaries `0.295` and `2.33`.

Coarse uniform spacing: `0.005`.

Fine uniform spacing: `0.0025`.

The domain-boundary nodes are inserted only to make the later physical-support integration exact at the frozen z cuts; **Exp073Z itself performs no support crop**.

For every one of the 20 Wm and 10 WW kernels compute the full `z=0..4` positive normalization by trapezoidal integration. Require:

- finite and strictly positive coarse/fine normalizations;
- relative coarse/fine normalization difference `<=5e-4` for every kernel.

Failure is numerical incompleteness, not a physical support FAIL.

## Canonical authority arrays

Serialize/hash canonical little-endian float64 logical arrays for:

- fine `z`;
- fine `chi_Mpc`;
- fine `H_km_s_Mpc`;
- normalized source `n(z)` on released nodes `[4,400]`;
- normalized lens `n(z)` on released nodes `[5,400]`;
- fine source efficiencies `[4,nz_fine]`;
- fine Wm radial factors `[20,nz_fine]` in order lens-major then source-major;
- fine WW radial factors `[10,nz_fine]` in order `(0,0),(0,1),...,(3,3)`;
- coarse/fine normalization vectors and their convergence deltas.

NPZ transport metadata is not authoritative; logical-array SHA256 values are.

## Required controls

1. exact public file byte/SHA authority;
2. exact Exp073Y Z/BIN logical-array hashes;
3. pinned CAMB git HEAD exact;
4. background parameter echo exact;
5. no input negative n(z);
6. full released-node normalization before interpolation;
7. finite monotonic non-decreasing `chi(z)` with `chi(0)=0`;
8. finite positive `H(z)`;
9. finite source efficiencies with only <=1e-12 negative roundoff canonicalized;
10. 20 Wm + 10 WW radial kernels exactly;
11. all radial normalizations positive and coarse/fine converged to <=5e-4;
12. no k, angular window, support fraction or retained coordinate is computed;
13. no covariance/nuisance/relation/null/G8 read.

## Required positive token

`PASS_EXP073Z_DES_RADIAL_KERNEL_AUTHORITY_V0_1`

## Scientific accounting

PASS closes the radial-kernel implementation/provenance prerequisite but is not Layer A.

- strict Article-3 readiness: **52%**;
- full real finite-operator candidate manifest: OPEN;
- Layer A: OPEN;
- Layer B: OPEN;
- covariance: BLOCKED;
- G7/G8/G9: OPEN.

The next readiness checkpoint remains approximately **55–57%** only after all 14 exact DES angular workspaces, these radial kernels and the already-bound BOSS broad operator are assembled into one immutable pre-support finite-operator candidate manifest.
