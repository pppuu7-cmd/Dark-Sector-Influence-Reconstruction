# Exp073P — large DES input streaming checksum binding — prospective method freeze v0.1

**Date frozen:** 2026-08-27  
**Status:** FROZEN BEFORE ANY LARGE-OBJECT SHA256 OUTPUT IS READ

## Purpose

Exp073P support evaluation remains blocked by P2 until every actually consumed DES Y1 release object is checksum-bound. The bounded preflight already SHA256-bound four of six required public objects. Two exact frozen release objects remain:

- `mcal-y1a1-combined-riz-unblind-v4-matched.fits`, expected byte count `84075649920`;
- `y1_source_redshift_binning_v1.fits`, expected byte count `2738626560`.

The official DES directory indexes expose these exact filenames and byte counts but no authoritative MD5/SHA manifest or ETag checksum was found in the completed preflight. This method therefore acquires SHA256 directly from the complete public byte stream without storing the complete object on runner disk.

## Frozen URLs

- `https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/shear_catalogs/mcal-y1a1-combined-riz-unblind-v4-matched.fits`
- `https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redshift_bins/y1_source_redshift_binning_v1.fits`

No alternate object or transformed catalogue may be substituted by this experiment.

## Frozen acquisition semantics

For each object independently:

1. issue an HTTPS GET to the exact frozen URL;
2. follow redirects, while recording the final URL;
3. require HTTP success;
4. stream every response byte exactly once through SHA256 without writing the full object to disk;
5. count streamed bytes independently;
6. require counted bytes to equal the frozen expected byte count;
7. if a response `Content-Length` is supplied, require it to equal the frozen expected byte count;
8. record SHA256, observed byte count, headers relevant to provenance, UTC completion time and exact URL.

Retries may restart an object from byte zero, but a checksum record is accepted only from one uninterrupted successful full-object response whose final byte count matches exactly. Partial/range checksums, multipart ETags, inferred hashes, decompressed/re-encoded content, or hashes of selected FITS columns are forbidden.

## Classification boundary

This is provenance acquisition only, not a physical-support experiment.

A file record is `PASS_FULL_OBJECT_STREAMING_SHA256_BINDING` only if the complete byte stream is read and exact byte-count checks pass. Network interruption, timeout or server failure is `INCOMPLETE_STREAMING_SHA256_BINDING` and is not a scientific FAIL.

Only when both large objects have PASS records may Exp073P P2 be considered complete together with the four preflight-bound objects. This method does not itself authorize support evaluation unless all six exact consumed release objects are checksum-bound.

## Frozen scientific boundaries preserved

No support fraction, retained dimension, covariance, whitening, nuisance SVD/rank, relation/null quantity or G8 information may be evaluated or read here. Exp073P remains bound to:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension `15`;
- classifying `nside=4096`.

G7 OPEN. G8 OPEN. G9 OPEN. Covariance restriction/whitening CLOSED.
