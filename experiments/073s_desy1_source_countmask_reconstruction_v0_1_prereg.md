# Exp073S — DES-Y1 source count-mask reconstruction v0.1 — preregistration

**Frozen:** 2026-08-29, before Exp073S implementation and before any Exp073S output.

## Purpose

Demonstrate that the genuine Exp073R1 v0.8 authority artifact contains enough information to reconstruct the exact per-pixel DES-Y1 source count masks required by the pinned Cosmotheka mapper, without rereading the 84 GB Metacalibration object and without using the user's self-hosted computer.

This experiment is representation/provenance QA only. It does not evaluate physical support, covariance, nuisance geometry, G7, G8 or G9.

## Immutable R1 authority

Bind exactly:

- R1 workflow run: `33270843577`;
- R1 job: `99148916507`;
- R1 head: `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- R1 workflow: `.github/workflows/exp073r1-desy1-github-hosted-wholestream-retry-v0-8.yml`;
- R1 artifact ID: `9743987175`;
- R1 artifact name: `exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- GitHub artifact digest: `sha256:702151cb02abd291e96060887a0da3ce86b908d352997515d48897022b0387ba`;
- authoritative Metacal bytes: `84075649920`;
- authoritative Metacal SHA256: `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- R1 mapper PASS token: `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`;
- source bins: exactly `0,1,2,3`;
- selected-row counts observed by the now-terminal preregistered R1 run: bin0 `7705486`, bin1 `7851711`, bin2 `8238547`, bin3 `4196641`.

The downstream prerequisite authority join has also completed successfully as run `33271876425`; Exp073S does not substitute for that receipt and cannot authorize physical support by itself.

## Pinned mask semantics

The pinned Cosmotheka DES-Y1 weak-lensing mapper constructs its mask by applying `get_map_from_points(...)` to the selected source catalogue without weights. The helper maps catalogue positions to HEALPix pixels and returns `numpy.bincount(ipix, minlength=npix)`. Therefore the exact source mask semantics are the integer number of selected catalogue rows in each RING pixel, not merely binary occupancy.

Exp073R1 v0.8 contains, for every source bin, a little-endian uint32 pixel-index record with one HEALPix pixel index for each selected catalogue row. Consequently the exact count map is determined by the multiset of those pixel indices.

Freeze:

- `NSIDE = 4096`;
- `NPIX = 12*NSIDE^2 = 201326592`;
- ordering `RING`;
- each record element is one little-endian uint32 pixel index;
- exact count semantics: `count[p] = number of record entries equal to p`;
- no smoothing, apodization, thresholding, clipping or normalization.

## Four independent jobs

Run bins `0,1,2,3` as four independent GitHub-hosted matrix jobs. Each job downloads the same immutable R1 artifact but reads only its own bin record and corresponding frozen occupancy mask. Jobs do not consume outputs from other bins.

For each bin require all of the following:

1. R1 summary has the exact R1 PASS token, exact Metacal bytes/SHA, exact frozen mapper and no-science flags;
2. selected row count equals both the frozen R1 count above and the record byte length divided by four;
3. record-file SHA256 equals the SHA recorded by the R1 summary;
4. every pixel is `< 201326592`;
5. exact `unique(pixel, return_counts=True)` multiplicities are positive and their sum equals selected rows;
6. number of unique pixels equals `unique_selected_pixels` in the R1 mask summary;
7. reconstruct binary occupancy from the unique-pixel set using the same little-endian bit packing as R1 and require its SHA256 and byte length to equal the frozen R1 mask record and downloaded mask file;
8. compute a deterministic sparse count-map fingerprint by hashing the sorted sequence of `(pixel_uint32_le, count_uint32_le)` pairs; this fingerprint is a representation identifier only, not a science statistic;
9. record maximum pixel occupancy and elementary count diagnostics without using any physical-support or covariance information;
10. preserve `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false`, and `G7/G8/G9=OPEN`.

## PASS / failure taxonomy

Per-bin PASS token:

`PASS_EXP073S_DESY1_SOURCE_COUNTMASK_RECONSTRUCTION_V0_1`

A mismatch in R1 identity, record/hash/mask/count consistency or pixel domain is `INVALID_FOR_RECONSTRUCTION_EXP073S`, not evidence for or against dark-sector physics. GitHub transport/artifact unavailability is `INCOMPLETE_EXP073S`.

The four-bin package is complete only when all four prospectively identical per-bin jobs pass. No majority vote and no selection of successful bins is permitted.

## Downstream boundary

Exp073S PASS proves exact reconstructability of the pinned DES source count masks from the compact R1 artifact. It may be used as an input/provenance layer for future NaMaster Wm/WW workspace construction, but it does **not** itself establish physical operator support or authorize covariance.
