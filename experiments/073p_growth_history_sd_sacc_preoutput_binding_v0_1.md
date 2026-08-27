# Exp073P — growth-history SD SACC pre-output binding v0.1

**Date frozen:** 2026-08-27  
**Status:** FROZEN BEFORE DOWNLOADING OR READING THE SD SACC PAYLOAD

## Purpose

Exp073P remains blocked before support evaluation because the raw DES Y1
Metacalibration catalogue and source-bin catalogue have not yet been
checksum-bound.  The primary analysis paper supplies a narrower public route:
footnote 7 of arXiv:2105.12108 points to the public growth-history repository
"together with the data products", and that repository publishes an SD SACC
download.

This binding tests whether that released SACC object can provide a
checksum-bound, finite DES Y1 operator product without consuming the 84.1 GB
Metacalibration catalogue or the 2.74 GB source-bin catalogue.  It is a
provenance/operator-availability step only, not a physical-support evaluation.

## Prospectively frozen source

- paper: `arXiv:2105.12108`;
- canonical source repository:
  `Cosmotheka/growth-history@6accbf70e55e8a55e7a61289c85d8665bfb1e310`;
- source tree: `06ca903788fbb2c0791ac7c80e276ce6a78230fd`;
- README Git blob: `056306bfca9d6425073d965fa6a718e34f843c9e`;
- exact README-labelled product: `SD SACC link`;
- requested download URL:
  `https://entangled.physics.ox.ac.uk/index.php/s/cF1x6j4biWXjDy3/download`.

The following exact source paths are bound at the same commit:

- `README.md`;
- `xCell/input/desy1_ebossqso_p18cmbk.yml`;
- `xCell/xcell/mappers/mapper_DESY1gc.py`;
- `xCell/xcell/mappers/mapper_DESY1wl.py`;
- `xCell/xcell/cls/cl.py`;
- `xCell/xcell/cls/to_sacc.py`.

## Frozen binding procedure

1. Reproduce the exact source commit and confirm that its README contains both
   `arXiv:2105.12108` and the exact requested SD SACC URL.
2. Follow redirects from only that prospectively frozen URL.
3. Record the effective URL, HTTP status, byte count, selected public response
   headers and SHA256 of the downloaded bytes.
4. Open the object lazily as FITS and inventory only HDU headers, dimensions and
   column names.  Do not access any HDU data payload in this step.
5. In particular, do not read a covariance table or matrix even if one is
   present in the container.
6. Do not compute a bandpower-window value, support fraction or retained
   dimension.

If source identity, transport, byte accounting or the FITS container cannot be
verified, record

`INCOMPLETE_EXP073P_GROWTH_HISTORY_SD_SACC_BINDING`.

If all binding controls pass, record

`BOUND_GROWTH_HISTORY_SD_SACC_CHECKSUM_FOR_OPERATOR_AUDIT_EXP073P`.

Neither status is an Exp073P scientific classification.  A successful binding
authorizes only a subsequent, separately recorded audit of non-covariance DES
tracer, n(z) and bandpower-window payloads after the observed SACC SHA256 has
been committed.

## Preserved scientific boundary

- common rectangle: `0.295 <= z <= 2.33`,
  `k <= 0.06664762008318016 Mpc^-1`;
- future threshold: `f_invalid <= 0.05`;
- future minimum retained full-coordinate dimension: `15`;
- classifying route remains `nside=4096`;
- covariance/whitening, nuisance rank/SVD, quotient/relation/null and G8 remain
  closed;
- Exp073P remains unclassified and support evaluation remains unauthorized.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
