# DSIR recovery checkpoint — Exp073R1 Attempt 3 terminal transport diagnosis + v0.4 small-range probe

Date: 2026-08-28
Branch: `main`
Scope: G7 / Exp073R1 DES Y1 full one-pass weak-lensing mask transport prerequisite

## Terminal state of Exp073R1 v0.2 sharded run

GitHub Actions run `33135622749` is completed with overall conclusion `failure`.

Latest-attempt job state:

- shard 0: **SUCCESS** (`job 98820219607`)
- shards 1–7: **FAILURE** in `Execute deterministic disjoint shard`
- merge: **SKIPPED** because the full disjoint shard universe was not available

This is **not a science-gate failure**. The workflow contract kept `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false`, and `gate_state={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}`.

## Exact failure diagnosis from decoded Actions logs

The failure is now directly identified rather than inferred.

For shard 1, the metacal range request eventually failed on:

- byte range `10992340164-11153296579`
- request size `160956416` bytes
- repeated `curl: (28) Operation timed out after 600000/600001 milliseconds with 0 bytes received`
- terminal exception: `RuntimeError: range transport exhausted`

For shard 7, the same failure mode occurred on:

- parent row start `119814620`
- byte range `73566193960-73727150375`
- request size `160956416` bytes
- five repeated 600 s zero-byte timeouts
- terminal exception: `RuntimeError: range transport exhausted`

By contrast, shard 0 ran the same frozen v0.2 mapper and source endpoints to completion and uploaded artifact `exp073r1s-shard-0`. Its final selected-row counters were `[201075, 211509, 207319, 99357]` for source bins 0–3 over its disjoint first eighth of the parent row universe. These partial counts remain explicitly NON-SCIENCE and must not be used to score G7.

### Interpretation

The terminal Attempt 3 state therefore demonstrates a **transport bottleneck / availability failure at the DES/NCSA range-serving layer**, not a failure of the mapper equations, row-to-HEALPix mapping, DES input identity, or dark-sector hypothesis.

## Audit of prepared v0.3 launcher

Prepared workflow:

`.github/workflows/exp073r1-desy1-low-concurrency-microshards-v0-3.yml`

It improves transport pressure by using:

- 32 deterministic disjoint microshards;
- `max-parallel: 1`;
- strict preflight binding to genuine Exp073R0 PASS and frozen DES checksum identities;
- exact shard coverage and merge/repeatability assertions.

However, the underlying mapper `ci/exp073r1_desy1_shard_v0_2.py` still has `CHUNK=262144` rows. For metacal row width 614 bytes this means each HTTP range request remains:

`262144 * 614 = 160956416 bytes` (~153.5 MiB).

Thus v0.3 changes concurrency/job granularity but does **not** reduce the individual range payload that was observed to time out with zero bytes. Launching the complete ~84 GB reconstruction before discriminating this factor would risk another long infrastructure-only failure.

## New targeted experiment: Exp073R1 transport small-range probe v0.4

Added:

- `ci/exp073r1_transport_probe_smallrange_v0_4.py`
- `.github/workflows/exp073r1-transport-smallrange-probe-v0-4.yml`
- one-shot push trigger `ci/exp073r1_transport_probe_v0_4.trigger`

Commits:

- probe script: `af739b41b8aaa39ae9da2e6334b7aad1957d5099`
- workflow: `f939b06597787c3af0e39b7f8cfa76283f5eac4b`
- trigger: `3bec88838e5e9e29e9435084eee0b3c8703b4822`

Launched Actions run:

- run id: `33170454493`
- workflow: `Exp073R1 transport small-range probe v0.4`
- event: `push`
- initial state at checkpoint: `queued`

### Probe contract

The probe targets the **exact 160956416-byte parent metacal range that failed in old shard 7**:

`73566193960-73727150375`

Instead of requesting it as one range, the probe requests four contiguous strict subranges of:

- `65536` rows each
- `40239104` bytes each

For each subrange it requires exact `Content-Range` and exact byte length. It then hashes the concatenated four subranges. The first subrange is fetched a second time and must reproduce the same SHA-256 exactly.

No weak-lensing mask, covariance, G8 input, `f_invalid`, or science score is computed.

## Decision rule after probe

1. **PASS**
   - conclude that smaller strict range payloads are transport-viable on the previously failing region;
   - prepare/launch full Exp073R1 transport v0.4 with `chunk_rows=65536`, low concurrency, exact coverage, and existing merge/repeatability guards;
   - G7 remains OPEN until the full parent row universe is reconstructed and the preregistered science gate is later scored.

2. **FAIL with repeated 0-byte timeouts even at 40239104 bytes**
   - do not launch the full transport reconstruction;
   - classify the DES/NCSA endpoint as currently unavailable/unsuitable for reliable range transport from Actions runners;
   - next infrastructure branch should be an independently identity-bound mirror/cache or another verified transport path, without changing science selection or mapper semantics.

3. **FAIL with nonzero bytes but bad Content-Range/length/repeat SHA**
   - treat as protocol/content-integrity failure;
   - do not merge or score science until the range-serving semantics are repaired and revalidated.

## Gate state preserved

- G7: OPEN
- G8: OPEN
- G9: OPEN

Nothing in Attempt 3 or the v0.4 transport probe is a negative dark-sector result. This checkpoint only resolves the infrastructure diagnosis and defines the next minimal discriminating experiment.
