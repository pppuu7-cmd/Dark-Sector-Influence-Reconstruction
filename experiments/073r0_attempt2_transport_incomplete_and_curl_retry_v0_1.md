# Exp073R0 attempt-2 infrastructure record and transport-only retry v0.1

**Date:** 2026-08-27  
**Scientific status:** unchanged / not evaluated  
**Infrastructure classification:** `INCOMPLETE_EXP073R0`

## Verified attempt-2 provenance

- workflow run: `33092211100`;
- run attempt: `2`;
- job: `98606401508`;
- head SHA: `5ee34c3fc80ab1091b7e925d321d880dbadade3c`;
- workflow: `.github/workflows/exp073r0-desy1-raw-row-healpix-equivalence-v0-1.yml`;
- latest attempt artifact: `9659049157`;
- latest attempt artifact digest: `sha256:4bc23a613e4240a2de4ff21da090fdc05e81f407833b47093bbff49aa136f699`.

The 120-minute workflow timeout was not the causal scientific outcome. The frozen sampled audit again terminated in the byte-range transport layer while reading the 84,075,649,920-byte DES Y1 metacalibration FITS object. The observed exception was a Python/urllib read timeout after transport retries were exhausted.

Therefore this attempt is infrastructure-incomplete, not `FAIL_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`, and it does not authorize Exp073R1.

## Frozen contract preserved

No scientific or validation criterion is changed. In particular, preserve exactly:

- parent row count `136930995`;
- 16 prospectively frozen windows from the same `np.linspace` construction;
- `8192` rows per window;
- exact FITS row widths/offsets/types already frozen in Exp073R0;
- exact source fields and metacal `ra`, `dec`, `flags_select` decoding;
- `nside=4096`, `coords='C'`, `hp.ang2pix(..., lonlat=True)`;
- all four source bins must contain selected sampled rows;
- manual decoder must exactly reproduce Astropy fields and HEALPix indices;
- `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0` is still the only outcome that authorizes Exp073R1.

## Transport-only retry

The next retry replaces only the Python `urllib` byte-range transport backend by `curl` with transport retries. Every returned range is accepted only if both conditions hold:

1. the final `Content-Range` header exactly equals the frozen requested byte interval and exact known total object size;
2. the returned body length exactly equals the requested byte count.

No full-file substitution, alternate catalogue, changed sample location, changed decoder, changed HEALPix mapping, changed acceptance threshold, covariance read, nuisance read, relation/null read or G8 read is authorized.

## Gate state

- Exp073R0: `INCOMPLETE`, retry permitted on unchanged scientific contract;
- Exp073R1: preregistered but execution remains blocked until genuine R0 PASS;
- Exp073P physical-support audit: OPEN, no `f_invalid` scored by this retry;
- covariance/whitening: CLOSED;
- G7: OPEN;
- G8: OPEN;
- G9: OPEN.
