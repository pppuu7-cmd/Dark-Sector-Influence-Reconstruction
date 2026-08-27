# Exp073P2 — remaining DES Y1 release checksum binding v0.1

Date: 2026-08-27
Parent: Exp073P P2
Science gates: G7/G8/G9 OPEN.

## Purpose

Complete checksum binding for the smaller DES Y1 release objects prospectively frozen by Exp073P before any physical support fractions are evaluated.

Already bound and not repeated:

- `y1_source_redshift_binning_v1.fits` — 2,738,626,560 bytes — SHA256 `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`.
- `mcal-y1a1-combined-riz-unblind-v4-matched.fits` — 84,075,649,920 bytes — SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.

## Frozen remaining release filenames

1. `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`
   - official directory: `https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redmagic/`
   - index-advertised size before hashing: 104,595,840 bytes.

2. `DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits`
   - same official directory
   - index-advertised size before hashing: 31,383,360 bytes.

3. `2pt_NG_mcal_1110.fits`
   - official directory: `https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/chains/`
   - index-advertised size before hashing: 6,600,960 bytes.

4. `y1_redshift_distributions_v1.fits`
   - frozen filename from the pinned Cosmotheka DES Y1 weak-lensing mapper configuration;
   - prospectively search only the official DES Y1 `redshift_bins/` directory first. If absent, do not substitute a similarly named file; record `MISSING_FROZEN_RELEASE_OBJECT_EXP073P2` and leave P2 incomplete pending a separately documented immutable source.

## Binding rule

For every found object:

- stream the complete byte sequence from the official DES server;
- record requested URL, final URL, HTTP status, Content-Length, observed byte count, Last-Modified/ETag when exposed, and full SHA256;
- for the three index-sized objects require observed bytes exactly equal the prospectively recorded index size;
- do not evaluate masks, redshift kernels, bandpowers, support fractions, covariance or any science gate.

`PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2` requires all four frozen objects to be found and fully hashed. Otherwise P2 remains incomplete; no scientific FAIL is authorized.
