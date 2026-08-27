# Exp073R0 — DES Y1 raw-row decode + HEALPix mapper-equivalence audit v0.1

Date: 2026-08-27
Parent: Exp073Q2 PASS, Exp073P G7 OPEN

## Purpose

Validate the manual row decoder and pixelization on prospectively fixed row windows before any second full 84-GB traversal. This is an implementation-equivalence audit only; it does not score G7/G8/G9.

## Frozen exact inputs

- `y1_source_redshift_binning_v1.fits`: 2,738,626,560 bytes; SHA256 `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`.
- `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: 84,075,649,920 bytes; SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.
- row count in both files: 136,930,995 (Exp073Q2 PASS).
- source BINTABLE data offset 5,760 bytes, row size 20 bytes.
- metacal BINTABLE data offset 17,280 bytes, row size 614 bytes.
- source `zbin_mcal` row offset 10, FITS `I`.
- metacal `ra`, `dec`, `flags_select` row offsets 566, 574, 594 with FITS `D`, `D`, `J`.

## Frozen mapper semantics

Pinned implementation: `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`.

Pinned runnable DES/eBOSS test config freezes `nside=4096`, `coords='C'`. Both DES Y1 mappers use `_get_rotator('C')`, hence `rot=None` for the classifying configuration.

For the final DES weak-lensing mask of bin `t`, the exact surviving-row rule implied by the code is

`zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`.

The initial five-bin OR selection is automatically true for every row satisfying final `zbin_mcal == t`, so it does not alter final mask membership.

The exact point-to-pixel map is the pinned `get_map_from_points` rule

`hp.ang2pix(4096, ra, dec, lonlat=True)`

followed by unweighted `np.bincount`.

## Prospectively fixed sample windows

Use 16 windows of 8192 consecutive rows. Start rows are integer floor values from an evenly spaced grid spanning `[0, N-8192]`, with `N=136930995`. The starts are computed only from N before any sampled science values are read.

For each window, fetch matching source and metacal row byte ranges from the exact P2 URLs.

## Independent decode control

1. Concatenate all raw sampled source rows and all raw sampled metacal rows separately.
2. Decode required fields manually from fixed FITS row offsets using big-endian FITS scalar types.
3. Independently construct small valid FITS files by combining the exact original primary/table headers with the same raw sampled row bytes and patching only `NAXIS2` to the sampled row count.
4. Read those mini-FITS files with Astropy.
5. Require exact equality between manual and Astropy values for all required fields (floating values use bitwise-equivalent numeric values with NaN equality).
6. Require exact equality of final selection masks and HEALPix pixel indices.
7. Require that the union of sampled rows contains at least one final selected object in each source bin 0,1,2,3; otherwise classify implementation test incomplete rather than changing sampling after looking at data.

## Classification

PASS: `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`.

Deterministic mismatch: `FAIL_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`.

Network/package/infrastructure interruption: `INCOMPLETE_EXP073R0`.

No result changes G7/G8/G9. PASS only authorizes Exp073R1 full one-pass mask construction.
