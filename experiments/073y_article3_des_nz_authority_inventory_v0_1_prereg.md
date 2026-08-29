# Exp073Y — Article 3 DES Y1 redshift-distribution authority inventory v0.1

**Frozen:** 2026-08-30, before Exp073Y output and before any current DES line-of-sight support fraction.

## Purpose

Exp073Y is an input-structure/provenance inventory only. It binds the exact public DES Y1 source/lens redshift-distribution arrays needed by the Article-3 broad finite operator before any quadrature, CAMB distance calculation, `(ell,z)->k` mapping or support classification is chosen from their numerical output.

It must not compute `chi(z)`, `H(z)`, lensing efficiencies `g(z)`, Wm/WW projection kernels, `k`, `f_invalid`, retained coordinates, covariance, nuisance geometry, relation/null statistics or G8.

## Frozen public files

### Source n(z)

`y1_redshift_distributions_v1.fits`

- bytes `109440`;
- SHA256 `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`;
- public URL `https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redshift_bins/y1_redshift_distributions_v1.fits`;
- pinned Cosmotheka semantics: HDU 1, redshift column `Z_MID`, source columns `BIN1..BIN4`.

### Lens n(z)

`2pt_NG_mcal_1110.fits`

- bytes `6600960`;
- SHA256 `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`;
- public URL `https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/chains/2pt_NG_mcal_1110.fits`;
- pinned Cosmotheka semantics: HDU 7, redshift column `Z_MID`, lens columns `BIN1..BIN5`.

## Required inventory

For each table, record without any physical-domain crop:

1. exact HDU/table row count;
2. exact column names and FITS dtypes;
3. canonical little-endian float64 SHA256 of `Z_MID` and every required BIN column;
4. whether all required arrays are finite;
5. whether `Z_MID` is strictly increasing;
6. `z_min`, `z_max`, minimum/maximum adjacent spacing;
7. for each BIN column: minimum, maximum, number of negative values, number of positive values, first/last index with non-zero value, and the corresponding raw `Z_MID` endpoints;
8. whole-table canonical logical-array SHA256 in fixed order `[Z_MID,BIN1,...]`;
9. raw trapezoidal integral of each released BIN column over its released `Z_MID` grid **only as an input diagnostic**, with no renormalized array emitted yet.

No clipping, interpolation, shift, normalization, rebinning or support crop is allowed in Exp073Y.

## Structural controls

Fail closed unless:

- exact byte counts and SHA256 match;
- required HDUs and columns exist exactly;
- all required arrays are finite;
- both `Z_MID` arrays are strictly increasing;
- every required source/lens BIN has a finite strictly positive raw trapezoidal integral;
- every required BIN has at least one positive entry.

Negative released BIN samples, if any, are recorded rather than silently modified. Their eventual treatment must be prospectively frozen in the later quadrature/kernel contract before support scoring.

## Large-file boundary

The 2.738-GB `y1_source_redshift_binning_v1.fits` remains upstream provenance for source-bin membership and was already consumed by the exact Exp073R1 mask reproduction. Exp073Y does not claim that file never mattered. It tests only the narrower statement that the radial `n(z)` arrays used by pinned `MapperDESY1wl.get_nz` come from the byte-bound `y1_redshift_distributions_v1.fits`, while the source angular count masks are inherited from the exact R1 authority.

## Required positive token

`PASS_EXP073Y_DES_NZ_AUTHORITY_INVENTORY_V0_1`

## Scientific accounting

Even on PASS:

- physical support evaluated: false;
- Layer A classified: false;
- retained coordinates evaluated: false;
- covariance authorized: false;
- strict Article-3 readiness: **52%**;
- G7/G8/G9: OPEN.

PASS authorizes a separately frozen deterministic line-of-sight quadrature and CAMB-background kernel producer using the already-frozen `ARTICLE3_DES_BACKGROUND_GEOMETRY_INHERITANCE_2026-08-30.md` contract.
