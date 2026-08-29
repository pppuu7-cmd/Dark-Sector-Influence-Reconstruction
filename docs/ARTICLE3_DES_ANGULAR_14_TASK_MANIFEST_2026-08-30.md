# Article 3 — DES Y1 exact angular-operator 14-task manifest

**Frozen:** 2026-08-30 before any production 14-task angular run and before any DES Layer-A support fraction is evaluated.

## Purpose

This document freezes the complete set of unique `nside=4096` NaMaster angular workspaces required by the current DES Y1 Wm+WW Article-3 route. It is an operator/provenance manifest only. It contains no physical-k conversion, `f_invalid`, support mask, covariance, nuisance or G8 output.

Exp073X is the exact Wm source-bin-0 performance/repeatability pilot. Production execution is authorized only after Exp073X itself finishes with its frozen PASS token; production does not need to repeat every workspace twice because pilot repeatability is a separate QA purpose.

## Pinned software/operator semantics

- `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`.
- `cosmotheka/mappers/mapper_DESY1wl.py` logical source previously bound with SHA256 `f44ce29a6f73ea5d315bbd17f38fc72f22521cb923fdec972fa1e093f818e9df`.
- `cosmotheka/mappers/mapper_DESY1gc.py` logical source previously bound with SHA256 `c4b5e114b47b5a8b7ff0f5e7007e9f9fae6e2b9274532be5f9fc946966784dc7`.
- NaMaster/PyMaster 2.7 lineage.
- classifying-resolution route `nside=4096`, HEALPix RING, coordinates C.
- finite band edges exactly
  `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`.
- 39 finite bandpowers and full true-ell axis `ell=0..12287`.

## Exact mask semantics

### DES source/shear mask

Pinned Cosmotheka `MapperDESY1wl._get_mask()` is the unweighted `get_map_from_points` occupancy-count map of the selected source catalog, not a binary mask and not a shear-signal map. Therefore production reconstructs the dense float64 count map exactly from the R1 little-endian uint32 pixel-index records. It does not re-read the 84-GB metacal signal catalog.

Hosted R1 authority:

- run `33270843577`;
- job `99148916507`;
- head `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- artifact `9720335366`;
- artifact digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- summary logical file SHA256 `100458e046088b24cba671db1852112676e487331d5c1f5c5cb55f8a9e011df4`;
- upstream metacal bytes `84075649920`, SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.

Exact source-bin records:

| source bin | selected rows | pixel-record bytes | pixel-record SHA256 | unique occupied pixels | occupancy SHA256 |
|---|---:|---:|---|---:|---|
| S0 | 7,705,486 | 30,821,944 | `5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15` | 4,305,774 | `b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32` |
| S1 | 7,851,711 | 31,406,844 | `752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241` | 4,339,193 | `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1` |
| S2 | 8,238,547 | 32,954,188 | `259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f` | 4,401,919 | `9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d` |
| S3 | 4,196,641 | 16,786,564 | `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec` | 2,943,132 | `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094` |

For each source bin production must reconstruct the count map from the pixel sequence, verify exact total count, unique-pixel count and binary-occupancy SHA before NaMaster is invoked.

### DES lens/density mask

Pinned `MapperDESY1gc._get_mask()` reads the public redMaGiC mask, maps UNSEEN to zero and sets pixels not strictly above `mask_threshold=0.5` to zero. At the already-native `nside=4096` and C/RING convention this is the production lens mask used for every Wm lens-redshift bin; the angular mask itself is independent of lens z-bin.

Public mask:

- `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`;
- bytes `104595840`;
- SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- keep original positive weights where `mask>0.5`; set all other pixels to zero.

## Frozen component extraction

Exp073T already verified NaMaster 2.7 component ordering:

- spin0 x spin2: `[TE, TB]`;
- spin2 x spin2: `[EE, EB, BE, BB]`.

For Wm, use only decoupled output TE from underlying physical TE:

`W_Wm[b,ell] = get_bandpower_windows()[0,b,0,ell]`.

For WW, the physical route is E-only, so use only decoupled output EE from underlying physical EE:

`W_WW[b,ell] = get_bandpower_windows()[0,b,0,ell]`.

The full NaMaster workspace is still computed; selecting the physical input/output component does not replace the mode-coupling calculation or assume an effective ell.

The positive support envelope later uses `abs(W[b,ell])`; the measured Wm observable remains signed.

## Exactly 14 unique production tasks

### Wm — four unique spin0 x spin2 workspaces

1. `Wm_S0`: lens mask x S0 count mask.
2. `Wm_S1`: lens mask x S1 count mask.
3. `Wm_S2`: lens mask x S2 count mask.
4. `Wm_S3`: lens mask x S3 count mask.

The same angular workspace is reused across all five DES lens redshift kernels for a fixed source bin because the angular lens mask is the same public mask for all lens bins. Thus 20 Wm radial kernels require only four angular workspaces, not twenty.

### WW — ten unique unordered spin2 x spin2 workspaces

5. `WW_S0_S0`.
6. `WW_S0_S1`.
7. `WW_S0_S2`.
8. `WW_S0_S3`.
9. `WW_S1_S1`.
10. `WW_S1_S2`.
11. `WW_S1_S3`.
12. `WW_S2_S2`.
13. `WW_S2_S3`.
14. `WW_S3_S3`.

No ordered duplicate `(j,i)` is computed when `j>i` because the Article-3 WW observation/radial inventory is frozen on unordered source pairs `i<=j`.

## Production output authority

Each task must output one canonical little-endian float64 `[39,12288]` selected physical angular-window array and its SHA256, plus input-mask logical hashes and exact task identity. Container/NPZ metadata is not authoritative.

The join step must require all 14 distinct task identities exactly once and hash their ordered manifest before any radial multiplication or support scoring.

## Performance rule

Exp073X deliberately computes the Wm_S0 workspace twice to establish exact deterministic repeatability. Production computes every one of the 14 unique workspaces once. This is a pre-frozen performance optimization, not an outcome-dependent change to the operator.

The production workflow may parallelize tasks across independent hosted runners. Parallel scheduling is implementation-only and cannot change task identity, input hashes, NaMaster version, binning, selected component or canonical output bytes.

## Firewall and readiness

Until the ordered 14-window authority is joined with the separately frozen DES radial authority and BOSS broad-operator authority into one immutable candidate manifest:

- physical support is not scored;
- `f_invalid` is forbidden;
- row retention is forbidden;
- covariance/whitening is forbidden;
- nuisance SVD/rank is forbidden;
- quotient/relation/null and G8 are forbidden;
- G7/G8/G9 remain OPEN;
- strict Article-3 scientific readiness remains **52%**.
