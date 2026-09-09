# DSIR-4 radial authority DES-Y1 supersession audit v0.1

Date: 2026-09-09. Scope: DSIR only.

Status: SUPPORT / PROVENANCE CORRECTION. This file supersedes the use of DES-Y3 as the active C2 radial-authority candidate. It does not delete historical audits, does not score `G_RADIAL_SUPPORT`, and does not create scientific model authority.

## 1. Correct source-side authority

The frozen C2 angular source labels `S0..S3` are DES Y1 Metacalibration source bins with `zbin_mcal=[0,1,2,3]`, not DES Y3 bins.

Pinned observation code:

`Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`

`cosmotheka/mappers/mapper_DESY1wl.py` explicitly:

- defines `zbin = 0/1/2/3`;
- filters the Metacalibration catalogue using `cat['zbin_mcal'] == self.zbin`;
- binds `file_nz = y1_redshift_distributions_v1.fits`;
- reads radial source data from HDU 1 as `Z_MID` and `BIN{self.zbin+1}`.

Therefore the source radial mapping is code-level and exact in ordinal convention:

- `S0 / zbin_mcal=0 -> BIN1`;
- `S1 / zbin_mcal=1 -> BIN2`;
- `S2 / zbin_mcal=2 -> BIN3`;
- `S3 / zbin_mcal=3 -> BIN4`.

The DES-Y3 file `2pt_NG_final_2ptunblind_02_24_21_wnz_covupdate.v2.fits` remains useful only as a methodological analogue and must not be used as C2 radial authority.

## 2. Wm physical identity recovered

The historical Exp073O public real-data replacement froze the Wm observation operator to the Cosmotheka DES Y1 galaxy-density x galaxy-shear route.

Its exact public input set includes:

- `DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits`;
- `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`;
- `mcal-y1a1-combined-riz-unblind-v4-matched.fits`;
- `y1_source_redshift_binning_v1.fits`;
- `y1_redshift_distributions_v1.fits`;
- `2pt_NG_mcal_1110.fits`.

Pinned `mapper_DESY1gc.py` defines the lens bins

`[0.15,0.30), [0.30,0.45), [0.45,0.60), [0.60,0.75), [0.75,0.90)`

and reads lens radial distributions from `2pt_NG_mcal_1110.fits` HDU 7 using `Z_MID` and `BIN{zbin+1}`.

The Wm observable is therefore a signed density x shear cross-observable. It must not be reinterpreted as an unspecified matter-side radial kernel merely from the symbolic label `Wm`.

## 3. WW physical identity recovered

The same pinned DES-Y1 observation stack uses the source `n(z)` from `y1_redshift_distributions_v1.fits` for the shear source bins.

The pinned CosmoSIS DES-Y1 configuration at

`cosmosis-developers/cosmosis-standard-library@9e3dd611fc20bf39489d43bf4afeb503d26b4e79`

loads source/lens number densities from the DES-Y1 2pt file and prospectively identifies:

- `position-shear = lens-source`;
- `shear-shear = source-source`.

The generic pinned projection implementation supplies the usual weak-lensing source kernels for the shear-shear LOS projection. Direct raw `n_i(z)n_j(z)` multiplication is not an admissible replacement for the derived lensing kernels.

## 4. Historical Exp073P radial/support methodology

Exp073P was preregistered on 2026-08-27 before any support fraction was evaluated. It froze:

- the same Cosmotheka DES-Y1 Wm/WW operator family;
- exact DES-Y1 source/lens radial products;
- bandpower response-envelope propagation into `(k,z)`;
- Limber support bookkeeping `k=(ell+1/2)/chi(z)`;
- physical `k` in `Mpc^-1`;
- no fiducial `P(k)`, covariance, nuisance, relation/null or later-gate weighting;
- fixed support rectangle and fixed threshold.

This historical contract materially constrains the correct implementation of the new decomposed `G_RADIAL_SUPPORT` stage.

## 5. Immutable radial payload identities recovered from Exp073P

The historical Exp073P checksum preflight already acquired exact full-file SHA256 for the two compact radial products required by a minimal current C2 radial executor:

- `y1_redshift_distributions_v1.fits`
  - bytes: `109440`
  - SHA256: `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`
  - relevant source schema from pinned mapper: HDU 1, `Z_MID`, `BIN1..BIN4`;
- `2pt_NG_mcal_1110.fits`
  - bytes: `6600960`
  - SHA256: `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`
  - relevant lens schema from pinned mapper: HDU 7, `Z_MID`, `BIN1..BIN5`.

These hashes were acquired before support scoring under the historical provenance-only Exp073P preflight. They may be reused as immutable identities only if the new C2 radial executor consumes those exact public objects byte-for-byte.

The much larger Metacalibration and source-bin catalogues are not automatically required as runtime inputs to the new radial executor if the already-admitted angular authority and the code-level ordinal bridge are treated as upstream authority rather than recomputed inside `G_RADIAL_SUPPORT`.

## 6. Non-aliasing with later Article-3 physical-support statistic

Repository chronology later froze a distinct Article-3 coordinate-level physical-support statistic. The two must not be conflated:

- legacy Exp073P `operator_f_invalid` = positive response-envelope weight outside the frozen physical rectangle divided by total positive response-envelope weight;
- later Article-3 `f_invalid` = count fraction of geometrically eligible final coordinates whose frozen common response envelope is invalid.

They have different denominators. A PASS of one cannot be copied into the other.

The current route is therefore:

`angular authority -> ordered join -> G_RADIAL_SUPPORT -> Article-3-style G_PHYSICAL_SUPPORT -> covariance/whitening -> nuisance quotient -> relation/null -> final observational validation`.

## 7. What is now resolved for G_RADIAL_SUPPORT

Resolved at authority level:

1. current survey generation: DES Y1, not DES Y3;
2. exact source labels: `zbin_mcal=0..3`;
3. exact source ordinal bridge: `0..3 -> BIN1..BIN4`;
4. source radial product identity: `y1_redshift_distributions_v1.fits`;
5. Wm field identity: DES-Y1 galaxy-density x galaxy-shear;
6. Wm lens-bin redshift definition and lens radial source path;
7. WW field identity: DES-Y1 source shear x source shear;
8. historical physical mapping convention `k=(ell+1/2)/chi(z)` and no-downstream-leakage rule;
9. exact bytes/SHA256 and relevant FITS-column binding for the two compact radial payloads needed by a minimal current executor.

Still to freeze prospectively before `G_RADIAL_SUPPORT` can be scored:

1. exact normalization and photo-z shift convention used at the radial stage;
2. one explicit current C2 radial executor interface consuming the admitted 14-slot ordered join and producing pre-physical-support coordinates without using covariance/nuisance/relation information;
3. exact coordinate/ordinal schema passed to the already-frozen later physical-support gate;
4. synthetic fail-closed tests for bin permutation, unit mixing, zero/non-finite kernels, forbidden interpolation/effective coordinates and downstream leakage.

For project tracking only, the radial-prerequisite task is now `9/(9+4)=69.2%` resolved by checklist item count. This percentage is not a scientific gate state.

## 8. Scientific state

Unchanged:

- `G_DOMAIN_MAPPING=PASS`;
- `G_ANGULAR_AUTHORITY=PASS`;
- `G_ORDERED_JOIN=PASS`;
- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`;
- `scientific_model_authority_created=false`;
- `overall_status=NOT_YET_TESTABLE`.

The blocker is no longer survey/source identity or compact radial-payload identity. It is now the prospective freeze and execution of the exact DES-Y1 radial interface, normalization convention and coordinate handoff.
