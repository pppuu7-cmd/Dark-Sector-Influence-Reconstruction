# Exp073AA — Article 3 DES exact angular task runner v0.1

**Frozen:** 2026-08-30 while Exp073X run `33277263287` is still in progress and before any production 13-task angular output or DES Layer-A support fraction is available.

## Purpose

Exp073AA is the generic one-task production executor for the exact `nside=4096` DES Y1 NaMaster angular operators frozen in `docs/ARTICLE3_DES_ANGULAR_14_TASK_MANIFEST_2026-08-30.md` and the prospective pilot-reuse amendment `docs/ARTICLE3_DES_ANGULAR_EXP073X_PILOT_REUSE_AMENDMENT_2026-08-30.md`.

It computes one finite angular window only. It cannot compute radial factors, physical k, `f_invalid`, retained rows, covariance, nuisance geometry, relation/null statistics or G8.

## Required upstream condition

The production workflow using this executor must not be triggered unless Exp073X run `33277263287` has completed with its frozen PASS token and immutable artifact. Under the already-frozen reuse rule, Exp073X supplies `Wm_S0`; Exp073AA production computes the remaining 13 task identities.

## Exact software and binning

- NaMaster/PyMaster 2.7 lineage only.
- `nside=4096`, `NPIX=201326592`, RING, coordinates C.
- true-ell axis `0..12287`.
- band edges exactly `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`.
- exactly 39 bandpowers.

## Source-mask authority

Bind exact hosted R1:

- run `33270843577`, job `99148916507`, head `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- summary SHA256 `100458e046088b24cba671db1852112676e487331d5c1f5c5cb55f8a9e011df4`;
- R1 PASS token `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.

Reconstruct every requested source mask from its exact little-endian uint32 pixel-index sequence by adding `1.0` to a dense float64 HEALPix count map at every selected row. Before NaMaster, verify pixel-record bytes/SHA, total count, unique occupied pixels and bitpacked occupancy SHA for the requested bin exactly as frozen in the 14-task manifest.

This reproduces pinned Cosmotheka `MapperDESY1wl._get_mask()`, which is an unweighted object-count map, not a binary mask.

## Lens-mask authority

For Wm only, bind `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`, bytes `104595840`, SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

Read RING field 0 as float64, map UNSEEN to zero, retain original mask weights only where `mask>0.5`, set all other pixels to zero. This reproduces pinned `MapperDESY1gc._get_mask()` at native `nside=4096`, C/RING geometry.

WW tasks must not read the lens mask.

## Allowed task identities

The generic executor recognizes the complete frozen set:

- Wm: `Wm_S0`, `Wm_S1`, `Wm_S2`, `Wm_S3`;
- WW: `WW_S0_S0`, `WW_S0_S1`, `WW_S0_S2`, `WW_S0_S3`, `WW_S1_S1`, `WW_S1_S2`, `WW_S1_S3`, `WW_S2_S2`, `WW_S2_S3`, `WW_S3_S3`.

The production matrix after Exp073X PASS runs the 13 identities excluding `Wm_S0`.

## NaMaster component rule

For Wm construct `NmtField(lens_mask,None,spin=0)` and `NmtField(source_count,None,spin=2)`. Require full window shape `[2,39,2,12288]` and select only

`window = wins[0,:,0,:]` = output TE from physical input TE.

For WW construct two spin-2 source-mask fields. For auto-pairs the same field may be used on both sides. Require full window shape `[4,39,4,12288]` and select only

`window = wins[0,:,0,:]` = output EE from physical input EE.

The selected canonical window must have shape `[39,12288]`, finite values and finite strictly positive per-band absolute-response normalizations.

No effective ell or band center represents this window.

## Output authority

Serialize/hash the selected little-endian float64 `[39,12288]` logical window. Record exact task identity, source-mask authorities, optional lens-mask authority, PyMaster version, band edges, ell axis, full workspace shape and selected component semantics. NPZ metadata is transport-only.

## Firewall

Hard-fail if the executor or its output implies any of:

- radial kernel read;
- physical k computation;
- support fraction;
- retained/rejected row;
- fiducial P weighting;
- covariance/whitening;
- nuisance SVD/rank;
- relation/null/G8 output.

## Required PASS token

`PASS_EXP073AA_DES_ANGULAR_TASK_V0_1`

A task PASS is non-classifying. Strict Article-3 readiness remains **52%** until all 14 angular task authorities, radial authority and BOSS broad operator have been joined into a single immutable pre-support finite-operator candidate manifest.
