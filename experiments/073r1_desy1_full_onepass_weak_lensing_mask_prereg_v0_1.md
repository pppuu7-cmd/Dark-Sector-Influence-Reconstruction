# Exp073R1 — DES Y1 full one-pass weak-lensing mask construction v0.1

Date frozen: 2026-08-27
Parent: Exp073Q2 PASS; Exp073R0 pending. This preregistration is frozen before any Exp073R0 result and before any Exp073R1 full-catalogue output.

## Purpose

Construct the exact DES Y1 weak-lensing HEALPix masks needed by the already-frozen Exp073P route by streaming the two checksum-bound public catalogues exactly once, using only the row decoder and mapper semantics already frozen in Exp073R0. Exp073R1 is an input-reproduction/construction experiment only. It must not compute physical-support leakage, covariance, nuisance rank/SVD, relation/null statistics, or G8 quantities.

Execution is authorized only if Exp073R0 classifies `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`. If R0 is FAIL or INCOMPLETE, this preregistration remains frozen but Exp073R1 must not execute.

## Immutable input binding

Use exactly:

- `y1_source_redshift_binning_v1.fits`: size 2,738,626,560 bytes; SHA256 `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`;
- `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: size 84,075,649,920 bytes; SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- row count in both: 136,930,995;
- source BINTABLE data offset 5,760 bytes, row size 20 bytes;
- metacal BINTABLE data offset 17,280 bytes, row size 614 bytes;
- source `zbin_mcal` row offset 10, FITS `I`;
- metacal `ra`, `dec`, `flags_select` row offsets 566, 574, 594 with FITS `D`, `D`, `J`.

Pinned mapper source: `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`.

## Frozen mapper and selection semantics

Use exactly `nside=4096`, `coords='C'`, hence no coordinate rotation for the classifying route.

For each source bin `t in {0,1,2,3}`, retain exactly rows satisfying

`zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`.

Map each retained row with

`hp.ang2pix(4096, ra, dec, lonlat=True)`

and accumulate an unweighted count map using integer pixel counts. The binary weak-lensing mask for each bin is `count > 0`.

No smoothing, apodization, interpolation, reweighting, star-density correction, survey-systematics weighting, or post-hoc pixel pruning is allowed in Exp073R1.

## Frozen one-pass algorithm

1. Stream the source and metacal table rows in synchronized contiguous chunks using the exact row count and exact binary row layouts above.
2. Decode only the required fields with big-endian FITS scalar semantics.
3. For each chunk, require the source and metacal chunk row counts to match exactly.
4. Apply the four frozen bin selections before pixelization.
5. Increment four `nside=4096` integer count maps.
6. Never materialize the full 84-GB catalogue on runner disk as an intermediate scientific requirement; streaming/local temporary transport is allowed, but the scientific output is only the four masks and diagnostics.
7. Preserve exact cumulative counters: rows read, selected rows per bin, finite/nonfinite RA/DEC counts, out-of-range pixel count, and unique retained pixels per bin.
8. After the final row, require total rows read to equal exactly 136,930,995 for both tables.

## Hard controls

R1. Parent authorization: Exp073R0 must be `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0` with frozen R0 semantics unchanged.

R2. Byte/row completeness: exact expected row count is consumed in both streams; no short read, duplicated chunk, skipped chunk or reordered row window is allowed.

R3. Decoder contract: field offsets/types are exactly those frozen above; no Astropy-derived alternate column interpretation may silently replace them after R0.

R4. Mapper contract: `hp.ang2pix(4096, ra, dec, lonlat=True)` only, no rotation and no alternate ordering convention.

R5. Selection contract: only the exact final selection expression above is allowed.

R6. Deterministic repeatability: a second execution on the same bytes and software versions must reproduce selected-row counts, unique-pixel counts and mask SHA256 values exactly. If a full second 84-GB traversal is operationally disproportionate, repeatability may be established by exact deterministic re-hashing/reconstruction from a preserved row-selection/pixel-index record only if that record itself was emitted during the first pass without changing the scientific algorithm; otherwise repeatability remains unverified and R1 cannot PASS.

R7. Output provenance: for each of the four masks record `nside`, ordering, selected-row count, unique-pixel count, FITS/NumPy serialization convention, file size and SHA256.

R8. No science leakage: no `f_invalid`, k-support fraction, covariance, whitening, nuisance SVD/rank, quotient/relation/null, article-selection or G8 output may be read or computed.

## Classification

PASS only if R1–R8 all pass:

`PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.

Any deterministic mismatch in row completeness, decoding, selection, pixelization or repeatability is

`FAIL_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.

Network/storage/package/runner interruption before complete deterministic evaluation is

`INCOMPLETE_EXP073R1`.

A PASS only closes the weak-lensing-mask input prerequisite for Exp073P. It does not authorize changing the already-frozen Exp073P rectangle or thresholds.

## Downstream rule

Only after Exp073R1 PASS and all other already-frozen Exp073P prerequisites are independently PASS may the Exp073P physical-support leakage computation execute under its unchanged criteria:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- positive invalid-support fraction `<= 0.05`;
- at least 15 retained full observation coordinates;
- classifying DES mask resolution `nside=4096`.

Covariance/whitening remains closed until Exp073P itself passes. G7 OPEN. G8 OPEN. G9 OPEN.
