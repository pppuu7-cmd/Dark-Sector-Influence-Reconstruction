# Exp073R1 v0.5 — sequential whole-object transport/reconstruction preregistration

**Frozen:** 2026-08-28, before any v0.5 output.

## Purpose

This is an **infrastructure-only implementation replacement** for the already frozen Exp073R1 DES-Y1 weak-lensing mask reconstruction. It responds to repeated zero-byte failures of NCSA random HTTP Range requests, including the 40,239,104-byte small-range probe. It does not change the science question, selection, mapper, physical-support threshold, covariance policy, or any G7/G8/G9 rule.

## Immutable parent and input identities

- Exp073R0 parent run: `33103083736`, required status `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`.
- Number of parent rows: `136930995`.
- Source object: `y1_source_redshift_binning_v1.fits`.
  - expected bytes: `2738626560`;
  - authoritative SHA256: `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
  - table data start: byte `5760`;
  - row bytes: `20`;
  - `zbin_mcal`: big-endian int16 at row offset `10`.
- Metacal object: `mcal-y1a1-combined-riz-unblind-v4-matched.fits`.
  - expected bytes: `84075649920`;
  - authoritative SHA256: `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
  - table data start: byte `17280`;
  - row bytes: `614`;
  - `ra`: `>f8` row offset `566`;
  - `dec`: `>f8` row offset `574`;
  - `flags_select`: `>i4` row offset `594`.

The table geometry implies:

- source table bytes = `136930995*20 = 2738619900`; source tail = `900` bytes;
- metacal table bytes = `136930995*614 = 84075630930`; metacal tail = `1710` bytes.

## Frozen transport architecture

### Stage A — source sequential stream

1. Open one ordinary whole-object HTTP GET with `Accept-Encoding: identity`.
2. **Do not send a Range header.**
3. Require HTTP 200 and, if supplied, exact expected Content-Length.
4. Hash every byte in the same sequential stream.
5. Consume the exact FITS prefix, then all `136930995` rows in parent order, then the exact tail.
6. Extract only the two original bytes of `zbin_mcal` per row and write a row-aligned derived index with length exactly `2*NROWS` bytes. No numerical conversion, remapping, clipping or reordering is allowed in the derived index.
7. Require whole-object SHA256 to equal the authoritative source SHA above before Stage A is classified PASS.
8. Record the SHA256 of the derived zbin index and upload it as an immutable inter-stage artifact.

### Stage B — metacal sequential stream and mapper

1. Download the exact Stage-A zbin-index artifact and verify its recorded SHA256 and exact byte length.
2. Re-bind the Exp073R0 parent PASS artifact before reconstruction.
3. Open one ordinary whole-object metacal HTTP GET with `Accept-Encoding: identity` and **no Range header**.
4. Require HTTP 200 and, if supplied, exact expected Content-Length.
5. Hash every byte in that same stream while processing rows in exact parent order.
6. Sequential internal read blocks may be chosen for memory efficiency, but they are reads from the already-open whole-object response, not independent HTTP requests. The block size has no science semantics and must not alter row order.
7. Decode the frozen fields above and apply exactly:

   `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`

   for `t in {0,1,2,3}`.
8. Selected RA/DEC must be finite. Map selected rows with exactly:

   - `nside=4096`;
   - `ordering=RING`;
   - celestial coordinates `C`;
   - `healpy.ang2pix(..., lonlat=True)`.
9. Emit little-endian uint32 HEALPix pixel-index records in selected parent-row order and binary masks with the already frozen little-endian `np.packbits` convention.
10. Require whole metacal SHA256 to equal the authoritative metacal SHA above and exact total bytes before Exp073R1 v0.5 can PASS.
11. Reconstruct each mask independently from the emitted pixel-index record and require exact selected-count, unique-pixel count and mask-SHA repeatability.

## Hard failure semantics

The v0.5 route is PASS only if all frozen identity, parent, row-count, field, selection, mapper, byte-count and repeatability checks pass.

Any of the following is infrastructure/reproduction failure, not a science/support result:

- whole-object download failure or timeout;
- wrong byte count or SHA256;
- derived source-index SHA/length mismatch;
- parent Exp073R0 mismatch;
- row-count/order mismatch;
- nonfinite selected coordinates;
- out-of-domain HEALPix index;
- repeatability mismatch.

No support fraction may be calculated from a failed or incomplete reconstruction.

## Explicit anti-retuning / forbidden operations

- No HTTP Range requests.
- No alternate DES object without a separately frozen identity audit.
- No source/metacal row matching by a new identifier; the frozen parent-row alignment remains the contract.
- No changed redshift-bin selection, declination interval, flags rule, NSIDE, coordinate convention or HEALPix ordering.
- No post-hoc sky mask edits.
- No covariance read, whitening, nuisance SVD/rank, relation/null calculation or G8 read during this route.
- No change to the future physical-support threshold `f_invalid <= 0.05` or minimum retained dimension.

## Authorization after PASS

A true `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` from this sequential implementation only satisfies the existing Exp073R1 reproduction prerequisite. It does **not** itself PASS physical support or G7.

Only after an Exp073R1 PASS may the already frozen DES harmonic physical-support calculation be resumed. Covariance remains forbidden until the full common physical-support gate independently PASSes.

## Gate state at preregistration

- G7: OPEN
- G8: OPEN
- G9: OPEN
- physical support: not yet scored on this route
- covariance restriction: not authorized
