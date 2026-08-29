# Exp073R1 v0.8 — GitHub-hosted rate-qualified whole-stream retry — preregistration

**Frozen:** 2026-08-29, before implementation and before any v0.8 execution output.

## Purpose

Recover the already-frozen Exp073R1 DES-Y1 weak-lensing mask reproduction without relying on the user's self-hosted computer. This is an infrastructure/transport replacement only. It does not change the mapper, selection, input identity, row universe, HEALPix semantics, support thresholds, or any Article-3 scientific gate.

## Parent evidence frozen before v0.8

- authoritative metacal object bytes: `84075649920`;
- authoritative metacal SHA256: `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- authoritative source whole-object SHA256: `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- source-index artifact: run `33175886694`, artifact `exp073r1-v05-source-index-2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c`, source-index SHA256 `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`;
- Exp073R0 PASS: run `33103083736`, head `94b05d307295d5e9263646983ece9514f9fa2e88`;
- frozen mapper implementation: `ci/exp073r1_sequential_wholestream_v0_5.py`, Git blob SHA1 `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`.

The successful GitHub-hosted provenance run `33081571259` previously streamed the complete 84.1 GB metacal object and obtained the authoritative SHA256. Its metacal stream completed from approximately 14:19:18 to 14:28:27 UTC on 2026-08-27. Therefore a hosted complete stream is known to be feasible on a sufficiently good transport route.

## Frozen mapper semantics — unchanged

The v0.8 execution must call the frozen v0.5 `metacal_map` implementation without modifying its science/mapping code. Preserve exactly:

- parent rows `136930995`;
- metacal data start `17280`, row bytes `614`, tail `1710`;
- source-index row order and exact bytes from the frozen Stage-A artifact;
- selection `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- four source bins `0,1,2,3`;
- HEALPix `nside=4096`, RING, coords `C`, `lonlat=True`;
- little-endian uint32 selected-pixel records in parent-row order;
- independent repeat mask reconstruction;
- `out_of_range_pixel_count=0`;
- `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false`, gates G7/G8/G9 OPEN.

## Transport-only change

Every remote metacal request must be an ordinary whole-object HTTP GET with:

- no `Range` header;
- `Accept-Encoding: identity`;
- expected HTTP status 200;
- no `Content-Range` response header;
- exact `Content-Length` when supplied.

Every candidate connection starts at byte 0. No resume, continuation, partial-object stitching, or byte-range transport is allowed.

### Rate qualification

Before committing a connection to the expensive mapper pass, the transport wrapper may read and buffer an initial prefix from that same whole-object response and evaluate only transport throughput. This is permitted because throughput is independent of any science payload or later gate result.

Freeze defaults:

- qualification prefix: `67108864` bytes (64 MiB);
- minimum active network-read throughput: `8 MiB/s`;
- socket/read timeout: `45 s`;
- maximum candidate connections per mapper attempt: `8`;
- maximum full mapper attempts after a connection qualifies: `3`;
- each rejected or failed connection is closed and never resumed.

The 8 MiB/s threshold is an execution-feasibility threshold only. It is not a data-quality or physics criterion and earns no scientific credit. A faster or slower accepted transport may not alter any selected row or mapper output.

The qualifying prefix must be replayed byte-for-byte to the frozen v0.5 mapper before subsequent network bytes, so the mapper still observes the exact original object beginning at byte 0.

During subsequent reads, the wrapper may fail closed if sustained active network-read throughput falls below the same frozen minimum. Any such event is an infrastructure/transport failure and forces a clean restart from byte 0.

## Retry integrity

Each full mapper attempt writes only into an attempt-specific temporary directory. On transport EOF, timeout, connection reset, or frozen throughput failure:

1. close the response;
2. discard the entire attempt directory;
3. retain only transport provenance;
4. start a new whole-object GET from byte 0 if attempts remain.

No partial pixel record, mask, hash state, source selection state, or row counter may be reused across attempts.

Non-transport exceptions from the frozen mapper are fail-closed and must not be converted into retries.

## Genuine PASS

A genuine v0.8 reproduction PASS requires all of the following in one successful mapper attempt:

- the unchanged frozen v0.5 mapper reaches `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`;
- observed metacal bytes equal `84075649920`;
- metacal SHA256 equals the authoritative hash above;
- source whole/index identity remains exactly bound;
- rows read source index and metacal both equal `136930995`;
- selection and mapper dictionaries equal the frozen values;
- selected rows are nonzero in all four bins;
- out-of-range pixels equal zero;
- record/mask repeatability assertions all pass;
- Exp073R0 parent checks all pass;
- transport provenance proves zero Range requests, all candidate connections started at byte 0, and the successful network stream consumed the complete object;
- no science gate/support/covariance/G8 information is read or scored.

A transport exhaustion, GitHub-hosted timeout, runner interruption, or inability to find a sufficiently fast route is `INCOMPLETE/INVALID FOR EXECUTION`, not a scientific FAIL.

## Downstream boundary

A v0.8 PASS is only an exact DES-Y1 reproduction authority candidate. It does not itself close G7, does not compute Article-3 physical support, and does not authorize covariance. A separate prospectively frozen prerequisite/authority receipt must bind the exact v0.8 implementation and run before the later Article-3 real support executor may proceed.

The self-hosted v0.7 attempt-3 route remains preserved as infrastructure history but is no longer the operationally preferred route while the user's home internet-dependent runner is unavailable.