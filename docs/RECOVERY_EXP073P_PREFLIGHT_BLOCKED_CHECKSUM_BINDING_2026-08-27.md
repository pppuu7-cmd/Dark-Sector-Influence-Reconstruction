# DSIR recovery checkpoint — Exp073P preflight blocked on large-input checksum binding

**Date:** 2026-08-27

## Verified main parent

- Exp073O remains `PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`.
- Exp073P preregistration remains unchanged.
- Common physical rectangle remains `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`.
- Support threshold remains exactly `f_invalid <= 0.05`.
- Minimum retained full-coordinate dimension remains exactly `15`.
- Classifying DES harmonic route remains `nside=4096`.

## Preflight execution

Workflow run `33076320686`, job `98531327704`, artifact `9648001733` completed successfully. This was a provenance/input preflight only: no support fraction or retained dimension was evaluated.

The pinned `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463` source reproduced exactly, including all four frozen source paths and the exact DES filenames in `DESY1_eBOSS_P18CMBK.yml`.

All six DES release URLs were reachable and returned explicit byte counts. Four were downloaded and SHA256-bound:

- `DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits`: 31,383,360 bytes; SHA256 `4a0ed31a128c34aa0da17e1d826c76b5ac829ba1c2c2087b965977b89d43a177`.
- `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`: 104,595,840 bytes; SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.
- `y1_redshift_distributions_v1.fits`: 109,440 bytes; SHA256 `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`.
- `2pt_NG_mcal_1110.fits`: 6,600,960 bytes; SHA256 `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`.

Two required public objects are much larger and were intentionally not downloaded in this bounded preflight:

- `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: 84,075,649,920 bytes.
- `y1_source_redshift_binning_v1.fits`: 2,738,626,560 bytes.

The public server returned no ETag checksum for either object. A targeted public-web search did not locate an authoritative published MD5/SHA manifest for these exact two filenames in this iteration.

Therefore the preflight status is

`BLOCKED_PRE_SUPPORT_INPUT_CHECKSUM_BINDING_EXP073P_PREFLIGHT`.

This is **not** an Exp073P scientific FAIL and **not** an infrastructure failure. P2 is simply incomplete, so Exp073P support evaluation remains unauthorized.

## Next admissible work

1. Search for an authoritative immutable checksum manifest or byte-identical released derived product for the 84.1 GB Metacalibration catalogue and 2.74 GB source-bin catalogue.
2. Alternatively locate a publicly released exact Cosmotheka-compatible DES Y1 shear mask/workspace realization whose provenance is explicitly tied to those two release objects; do not substitute a different nside/operator silently.
3. Only after every actually consumed object is checksum-bound may the classifying NaMaster bandpower-window support calculation start.
4. Do not read covariance, nuisance SVD/rank, quotient/relation/null, G8 or article-selection information before Exp073P support PASS.

G7 OPEN. G8 OPEN. G9 OPEN. Covariance restriction/whitening CLOSED.
