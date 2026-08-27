# Exp073S0 — exact DES Y1 redMaGiC mask + lens/source n(z) reproduction v0.1

Date: 2026-08-27
Parent: Exp073P2 checksum PASS, Exp073Q2 schema PASS
G7/G8/G9: OPEN.

## Purpose

Close the small-input part of Exp073P P3/P5 prerequisites while the large shear-mask row equivalence route is evaluated independently. This experiment reproduces only the exact density mask and released redshift kernels required later by the positive harmonic support mapping. It does not compute bandpower windows or any support fraction.

## Frozen inputs

- `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`, 104,595,840 bytes, SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.
- `2pt_NG_mcal_1110.fits`, 6,600,960 bytes, SHA256 `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`.
- `y1_redshift_distributions_v1.fits`, 109,440 bytes, SHA256 `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`.

Pinned code/config: `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`, `nside=4096`, `coords='C'`.

## Frozen redMaGiC mask semantics

Pinned `MapperDESY1gc._get_mask()`:

1. `hp.read_map(file_mask)`;
2. set `hp.UNSEEN` entries to zero;
3. rotate with `_get_rotator('C')`; under `coords='C'`, rotation is identity;
4. `hp.ud_grade(mask, nside_out=4096)`;
5. keep only `mask > 0.5`; set all other pixels to zero.

The pinned test configuration uses key `threshold`, while the mapper reads `mask_threshold`; therefore the mapper's own frozen default `0.5` is the operative threshold. The comparison is strict `>`.

S0 requires input NSIDE=4096 and exact equality between the pre- and post-`hp.ud_grade(...,4096)` arrays (with NaN equality if any) before thresholding. This explicitly verifies the same-resolution identity assumption instead of merely assuming it.

Record: input/output dtype, NPIX, number of UNSEEN pixels, number of positive retained pixels, sum/mean/min/max over retained mask, and SHA256 of canonical thresholded dense-array bytes plus a deterministic sparse `(pixel,value)` fingerprint.

## Frozen n(z) semantics

Lens redMaGiC `n(z)` follows pinned `MapperDESY1gc.get_nz()` exactly:

- open `2pt_NG_mcal_1110.fits`;
- use HDU index 7;
- record `Z_MID` and `BIN1`..`BIN5`.

Source weak-lensing `n(z)` follows pinned `MapperDESY1wl.get_nz()` exactly:

- read HDU 1 of `y1_redshift_distributions_v1.fits`;
- record `Z_MID` and `BIN1`..`BIN4`.

No interpolation, normalization, photo-z shift, fiducial cosmology or support cut is applied in S0. Arrays must be finite, equal-length within each file and have strictly increasing `Z_MID`.

## Classification

`PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0` iff all frozen input hashes, exact mask semantics and both released n(z) schemas pass.

Deterministic reproduction failure: `FAIL_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`.

Transport/package interruption: `INCOMPLETE_EXP073S0`.

A PASS closes only this small-input P3 prerequisite. G7/G8/G9 remain OPEN.
