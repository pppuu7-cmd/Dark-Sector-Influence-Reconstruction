# Exp073Q — DES Y1 mapper-equivalent mask geometry / FITS row-layout freeze v0.1

Date: 2026-08-27
Parent: Exp073P exact common physical-support gate
Status at preregistration: P2 provenance identity COMPLETE; P3/P4 and G7/G8/G9 OPEN.

## Purpose

Remove the remaining implementation ambiguity before a second expensive traversal of the public DES Y1 shear inputs. This experiment does **not** score G7/G8/G9. It freezes the exact row-layout and the minimal mapper-equivalent geometry projection needed to reproduce `MapperDESY1wl._get_mask()` from the pinned public inputs.

## Frozen parents / identities

- DSIR repository parent state: `372997bf1240a224c2a915fd0d1a5ae50476ba7a`.
- Cosmotheka implementation: `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`.
- DES Y1 source-bin object: `y1_source_redshift_binning_v1.fits`, exact size 2,738,626,560 bytes, SHA256 `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`.
- DES Y1 Metacalibration object: `mcal-y1a1-combined-riz-unblind-v4-matched.fits`, exact size 84,075,649,920 bytes, SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.

These two large-object hashes were obtained by the Exp073P streaming full-object binding workflow. They are identity/provenance results only.

## Exact pinned mapper facts

For a target source bin `t`, the pinned `MapperDESY1wl`:

1. row-wise `hstack`s Metacalibration columns with source-bin columns;
2. makes an initial permissive selection requiring `t` to occur in at least one of `zbin_mcal`, `zbin_mcal_1p`, `zbin_mcal_1m`, `zbin_mcal_2p`, `zbin_mcal_2m`;
3. imposes `-90 < dec < -35` and `flags_select == 0`;
4. computes shear-response quantities;
5. then keeps `zbin_mcal == t` for the final catalogue;
6. `_get_mask()` calls `get_map_from_points(self.cat_data, ...)` **without a weight argument**, then normalizes occupied-pixel counts as `npix*N/(4*pi)`.

Therefore, conditional on successful execution of the pinned mapper on the exact public files, final mask **geometry and counts** are determined by the row-aligned tuple

`(ra, dec, flags_select, zbin_mcal)`

with final row rule

`zbin_mcal == t AND -90 < dec < -35 AND flags_select == 0`,

followed by exactly the same coordinate rotation and HEALPix `ang2pix` projection.

This reduction is valid only for the **mask geometry/count map**. It MUST NOT be reused for the shear signal maps or response calibration, where the sheared-bin and ellipticity/response columns remain physical inputs.

## Important equivalence caveat

The reference mapper computes response quantities before its final `zbin_mcal == t` cut. A reduced streaming mask builder is therefore claimed to be **mathematically mask-equivalent conditional on normal reference-mapper completion**, not bytecode- or failure-mode-equivalent for malformed inputs. The exact public objects are already byte-bound; Exp073Q additionally freezes their table schemas/row alignment before a reduced implementation is permitted.

## Frozen schema audit

Using HTTP byte ranges only (no second full-object download in this subexperiment):

1. parse FITS headers at 2880-byte boundaries;
2. identify the relevant BINTABLE HDU in each object;
3. record `NAXIS1`, `NAXIS2`, `TFIELDS`, all `TTYPEi`/`TFORMi` pairs needed by the projection;
4. compute fixed-row byte offsets for required columns where the FITS `TFORM` is fixed-width;
5. require equal source-bin and Metacalibration `NAXIS2` values, because the pinned mapper joins by row position;
6. require the source table to contain at least `zbin_mcal` (and report the four sheared-bin columns for provenance);
7. require the Metacalibration table to contain at least `ra`, `dec`, `flags_select` (and report calibration columns if present);
8. fail-stop on missing columns, unsupported variable-length layout for a required geometry column, unequal row counts, malformed FITS headers, or ambiguous multiple candidate tables.

No G7/G8/G9 status is changed by a schema PASS.

## Coordinate / resolution invariant

Pinned tracer configuration fixes DES Y1 weak-lensing `nside=4096`, and the global sphere configuration is required by `Data.get_mapper()` to supply a matching `coords`. The historical pinned input YAML used for provenance does not by itself provide enough evidence here to silently invent a `sphere.coords` value. Therefore the exact normalized coordinate setting is an explicit pre-P3 invariant: resolve it from a pinned runnable/normalized Cosmotheka configuration or an equivalent immutable upstream artifact before any harmonic support score is accepted.

If coordinate provenance remains unresolved, Exp073Q may still PASS its FITS schema/row-layout audit, but P3 remains blocked and G7 remains OPEN.

## PASS / FAIL

`SCHEMA_ROW_LAYOUT_PASS_EXP073Q` iff:

- both target BINTABLEs are uniquely identified;
- all required geometry columns exist with fixed-width row offsets;
- the two tables have exactly equal `NAXIS2`;
- row layout can be traversed deterministically without heuristic field discovery.

Else: `FAIL_EXP073Q_SCHEMA_OR_ROW_ALIGNMENT` and stop before another 84-GB traversal.

## Next step if PASS

Exp073R will implement the one-pass mapper-equivalent streaming DES Y1 source-bin mask construction at NSIDE=4096, with chunked/sparse accumulation so a standard GitHub runner does not need four dense 201,326,592-pixel float64 masks simultaneously. Exact coordinate provenance must be resolved before Exp073R can certify the final masks/workspaces for P3.
