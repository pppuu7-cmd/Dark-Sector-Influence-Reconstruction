# DSIR recovery checkpoint — Exp073R1 active transport contingency

Date: 2026-08-27
Branch: `main`
Parent HEAD at audit start: `af0b3c40ac37a8847d3f7b5f2c38dda6f7f09da4`

## Active state

Exp073R1 workflow run `33108733415` (`Exp073R1 DES Y1 full one-pass weak-lensing mask v0.1`) remains `in_progress` in job `full-onepass-mask`, step `Execute frozen Exp073R1 one-pass construction`.

Completed successfully before the active heavy step:

1. checkout;
2. genuine Exp073R0 PASS binding;
3. frozen mapper runtime installation.

No duplicate heavy R1 run is authorized while run `33108733415` remains active.

## Frozen scientific contract remains unchanged

R1 is non-science infrastructure/provenance construction. It MUST NOT compute `f_invalid`, read covariance, read G8, or modify G7/G8/G9 state. The workflow asserts:

- status `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`;
- exact full row count `136930995` for both source and metacal inputs;
- source SHA256 `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`;
- metacal SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- all hard controls true;
- `science_gate_scored == false`;
- `f_invalid_computed == false`;
- `covariance_read == false`;
- `G8_read == false`;
- gate state remains `G7/G8/G9 = OPEN`.

## Infrastructure-risk audit

The current workflow has `timeout-minutes: 360`.

The frozen mapper uses `NROWS=136930995`, `CHUNK_ROWS=262144`, therefore a complete catalogue pass requires 523 row chunks. Each chunk performs two independent HTTP byte-range transports (source + metacal), in addition to prefix/suffix transports. The metacal input is 84,075,649,920 bytes. Consequently, wall-clock timeout or remote range-transport failure is a credible infrastructure failure mode even when the mapper/science contract is correct.

This risk is recorded **before** completion of R1 so that a future timeout is not misclassified as a scientific negative result.

## Pre-authorized contingency if and only if run 33108733415 fails for timeout/transport

A successor transport-only recovery experiment may be created only after confirming that the failure is infrastructure-level (GitHub timeout, curl/range transport, transient remote server failure, runner loss, disk/runtime failure) and not an R1 assertion failure.

Allowed changes in such a recovery:

- transport scheduling/chunk size/concurrency/cache strategy;
- runner timeout/resource envelope;
- resumable download or local sequential staging;
- logging/checkpoint frequency.

Forbidden changes:

- DES source/metacal URLs or expected file hashes;
- row count;
- FITS field offsets/types;
- source-bin/flags/declination selection;
- HEALPix `nside=4096`, RING, celestial lon/lat mapping;
- exact mask serialization semantics;
- R0 parent requirements;
- any downstream physical-support acceptance criterion;
- any covariance, nuisance, quotient/null, G8 or G9 access.

A transport-only recovery must reproduce the same input SHA256 values and the same final R1 mask/pixel-record semantics. It is an infrastructure retry, not a new scientific hypothesis.

## Next scientific action

If run `33108733415` completes with the exact frozen PASS classification, proceed to the preregistered physical support-validity stage (Exp073P lineage) only after binding the immutable R1 artifact and exact provenance. Do not open covariance/whitening before that support mask passes its frozen criteria.
