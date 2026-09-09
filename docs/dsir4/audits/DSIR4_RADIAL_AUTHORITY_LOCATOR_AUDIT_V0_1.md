# DSIR-4 radial-authority locator audit v0.1

Date: 2026-09-09. Scope: DSIR only.

Status: EVIDENCE-LOCATOR ADVANCE ONLY. This document does **not** pass `G_RADIAL_SUPPORT`, does not reserve a new experiment label, and does not authorize numerical radial multiplication.

## Upstream frozen prerequisite
`docs/dsir4/contracts/DSIR4_RADIAL_SUPPORT_INPUT_REQUIREMENTS_V0_1.md` requires, for S0..S3, an immutable source-radial payload with exact bin identity, coordinates/edges, units, normalization/weighting, provenance, exact combination operator, and fail-closed coordinate rules. Wm additionally requires its actual matter-side radial/line-of-sight factor.

## New external evidence located
A concrete DES Y3 fiducial TwoPoint data file is repeatedly referenced by DES Y3 analysis code as:

`des-y3/2pt_NG_final_2ptunblind_02_24_21_wnz_covupdate.v2.fits`

Evidence trail located on 2026-09-09:

1. DES collaboration analysis repository `des-science/y3-3x2pt-ppd-postunblinding` uses this exact file as the fiducial `DATAFILE` in its post-unblinding PPD scripts.
2. A public DES-Y3 loader implementation opens the same exact filename and reads extension `nz_source` with coordinate column `Z_MID` and four source-distribution columns `BIN1`, `BIN2`, `BIN3`, `BIN4`.
3. That loader constructs four weak-lensing tracers from those four distributions after explicit numerical normalization of each `BINi` over `Z_MID`.
4. DES Y3 redshift-calibration literature independently states that the weak-lensing source sample is divided into four tomographic bins and that fiducial source redshift distributions are generated from SOMPZ combined with clustering-redshift information (with the final cosmology treatment using fiducial n(z) distributions plus redshift-shift nuisance parameters).

## What this resolves
The previous blocker statement "no external radial source candidate has been located" is no longer accurate.

There is now a high-confidence candidate for the S0..S3 radial source authority: the `nz_source` extension of the exact fiducial DES Y3 TwoPoint FITS above, with the natural structural mapping candidate

- S0 -> `BIN1`
- S1 -> `BIN2`
- S2 -> `BIN3`
- S3 -> `BIN4`

and redshift coordinate candidate `Z_MID`.

This mapping is **not yet admitted**. It remains a candidate until exact identity with the frozen `zbin_mcal=[0,1,2,3]` labels is proven from authoritative DES metadata/code rather than inferred from ordinal coincidence.

## Remaining fail-closed blockers before a scientific radial gate
The following must still be bound before `G_RADIAL_SUPPORT` can become testable:

1. **Exact bin identity:** authoritative proof that the frozen metacal source labels 0..3 correspond exactly and in order to `nz_source/BIN1..BIN4` in this file.
2. **Full coordinate contract:** inspect the FITS extension schema, including any `Z_LOW`, `Z_MID`, `Z_HIGH` or equivalent fields, units and edge convention. `Z_MID` alone is insufficient if the observation model uses bin edges or widths.
3. **Normalization/weighting convention:** bind whether the stored `BINi` vectors are already normalized and which shear/source weights are encoded. Do not silently renormalize merely because a downstream loader does so.
4. **Immutable payload:** acquire the exact FITS bytes (or an authoritative immutable mirror), record file SHA256, FITS extension/header identity, row count, dtype and per-extension digest or equivalent reproducible identity.
5. **WW radial operator:** prospectively bind the exact two-source kernel construction used by the actual observable convention; no ad-hoc product of source n(z) vectors is authorized.
6. **Wm radial/LOS operator:** bind the actual matter-side kernel for the Wm convention. The existing angular authority `TE<-TE` does not by itself specify the radial matter/lensing factor.
7. **Coordinate compatibility:** define an exact fail-closed rule joining the radial support to the frozen C2 prediction-domain coordinates without interpolation, extrapolation, smoothing, rounding, effective-z/effective-k, or fiducial-P substitution.

## Scientific classification after this audit
- `G_DOMAIN_MAPPING=PASS`
- `G_ANGULAR_AUTHORITY=PASS`
- `G_ORDERED_JOIN=PASS`
- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`
- `scientific_model_authority_created=false`
- `overall_status=NOT_YET_TESTABLE`

The blocker has narrowed from "radial payload/operator unknown" to "candidate source payload located; exact source-bin binding + payload digest/schema + WW/Wm radial operators remain unresolved".

## Exact next permitted action
Acquire/inspect the exact fiducial DES Y3 FITS payload and authoritative DES metadata/code that connects metacal tomographic labels to `nz_source/BIN1..BIN4`. In parallel, locate the actual DES/observation-model equations or implementation that turns those source distributions into the radial weak-lensing kernels used for WW and the matter-side Wm observable. Freeze those identities and equations prospectively before preregistering any numerical `G_RADIAL_SUPPORT` experiment.
