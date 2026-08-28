# Exp073R1 canonical range-identity recovery — 2026-08-28

## Why the previous v0.3 transport contract was blocked

The frozen scientific mapper itself was not the problem. The issue was input-byte provenance.

The successful whole-object checksum run `33081571259` is authoritative for the two large DES Y1 release objects used by the weak-lensing mask reconstruction. Its immutable artifacts bind:

- source bin file `y1_source_redshift_binning_v1.fits`: 2,738,626,560 bytes, SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`, artifact `9650284556`, artifact ZIP digest `sha256:0eb1fdc7bc2d9f5816e0a003418a41b540cd7281af1f5ceb24a37af82187f5d4`;
- metacalibration file `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: 84,075,649,920 bytes, SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`, artifact `9650627630`, artifact ZIP digest `sha256:5a80c70568a6ed114e4e32990c5399bc8109df10f4d2910abd73441edb122a2b`.

The source SHA had been transcribed incorrectly in later R1 files as `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`. That transcription is now explicitly rejected.

A second issue remained even after correcting that string: the old microshard code computed SHA256 for every consumed byte range, but those range hashes were not cryptographically linked to the previously whole-file-hashed object. A range `Content-Range` header and byte count prove position and length, not byte identity. SHA256 digests of independent ranges cannot be algebraically recombined into a whole-file SHA256.

For that reason PR #158 placed a fail-closed sentinel in the automatic v0.3 launcher before the then-running v0.2 parent could trigger it.

## Corrected cryptographic bridge

The replacement contract uses one canonical sequential stream of each entire release object. During that *same byte stream* it computes simultaneously:

1. the SHA256 of the entire object;
2. the SHA256 of the exact 32 contiguous table-row byte intervals later consumed by the R1 microshards;
3. prefix and FITS-tail SHA256 values for audit completeness.

For object bytes `B[0:N)`, table start `s`, row width `r`, total rows `R`, and microshard index `i=0,...,31`, define

`row_lo(i) = floor(R i / 32)` and `row_hi(i) = floor(R (i+1) / 32)`.

The canonical consumed interval is

`I_i = B[s + r row_lo(i) : s + r row_hi(i)]`.

The canonical manifest stores

`H_full = SHA256(B[0:N))`

and

`H_i = SHA256(I_i)`

for every `i`, with all `H_i` computed while the exact stream used for `H_full` is passing through the hasher. The stream is accepted only if `H_full` equals the authoritative whole-object SHA256 above and the exact byte count matches the frozen release size.

Each later transport microshard independently fetches its exact `I_i`, checks the exact HTTP `Content-Range` and byte count, computes `SHA256(I_i)` over the bytes actually decoded, and requires equality with the canonical `H_i`. Therefore the decoded shard bytes are cryptographically tied to a byte interval from a stream whose complete SHA256 is known and verified.

This removes the non-composability gap without requiring any fiducial spectrum, covariance, support result, effective ell, ad-hoc cutoff, or post-hoc scientific threshold.

## Frozen mapper and science boundary

The mapper remains:

- parent rows: exactly 136,930,995;
- source row bytes: 20, table data start 5,760;
- metacal row bytes: 614, table data start 17,280;
- selection: `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- HEALPix: `nside=4096`, RING, celestial coordinates, `lonlat=True`;
- four source bins `t=0,1,2,3`;
- output pixel-index records are little-endian uint32 in selected parent-row order;
- masks are reconstructed from those records and independently reconstructed a second time for repeatability.

The corrected transport/reproduction stage still sets:

- `science_gate_scored=false`;
- `f_invalid_computed=false`;
- `covariance_read=false`;
- `G8_read=false`;
- gate state `G7/G8/G9 = OPEN`.

A PASS from this stage is only `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`. It is not Exp073P physical-support PASS and cannot open covariance/whitening by itself.

## Implementation files

The corrected implementation is:

- `ci/exp073r1_fullstream_range_manifest_v0_1.py` — same-stream full-object and exact 32-range SHA256 manifest;
- `ci/exp073r1_desy1_shard_v0_3.py` — range transport, frozen decoding/selection/HEALPix mapping, and exact equality to the canonical range digest;
- `ci/exp073r1_desy1_merge_v0_4.py` — complete 32-shard coverage, canonical digest equality, merged record verification, mask reconstruction and independent repeatability reconstruction;
- `.github/workflows/exp073r1-desy1-canonical-microshards-v0-4.yml` — authoritative prior checksum/R0 preflight, canonical streams, low-concurrency microshards, and merge.

PR #159 merged the canonical byte-binding repair. PR #160 installed the duplicate-safe one-shot launcher that waited for the old v0.2 run to become terminal and then dispatched the canonical v0.4 implementation. No scientific acceptance criterion was changed by either PR.

## Runtime evidence added in this recovery iteration

### Old v0.2 is terminal but scientifically unclassified for support

Run `33135622749` is now `completed/failure`, head `70be4d35199d4132a2ca9da912689519e40bcc84`, attempt 2. The correct classification is reproduction/transport **INCOMPLETE**, not a physical-support FAIL.

Shard 0 (`98761777728`) reached `PASS_DESY1_R1_SHARD`; shard 1 (`98761778039`) is verified transport-incomplete after a read timeout; shard 2 (`98761777874`) is verified transport-incomplete after HTTP 502. The other failed shard jobs were not individually exception-audited in this recovery iteration. No `f_invalid` was produced anywhere in this run.

### Canonical v0.4 is the active authoritative R1 attempt

The authoritative run is `33160570463`:

- workflow `.github/workflows/exp073r1-desy1-canonical-microshards-v0-4.yml`;
- event `workflow_dispatch`;
- head SHA `e61c61a370cdc4cee5da2aa26cc677a6ad373c70`;
- attempt 1;
- status at this checkpoint: `in_progress`.

The source canonical-manifest job `98813812482` is a verified PASS. Its same-stream result is `PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M`, with exact byte count `2738626560`, exact whole SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`, 32 exact row ranges, and exact once-only coverage of all parent rows.

Its immutable artifact is:

- ID `9681454384`;
- `exp073r1-canonical-source-e61c61a370cdc4cee5da2aa26cc677a6ad373c70`;
- ZIP digest `sha256:58d74d7c6ae9a12150c8b0979e66e75d654e7dbfe83cfe9711e7c5ca836abebe`;
- size `3052` bytes.

The metacal canonical-manifest job `98813812443` is still in progress on the 84,075,649,920-byte whole-object stream. No metacal canonical-root PASS is claimed until its exact whole SHA and artifact contract finish successfully.

The prior internal/messaging association of another run ID with canonical v0.4 is superseded. Recovery must use **run `33160570463`** and exact head `e61c61a370cdc4cee5da2aa26cc677a6ad373c70`.

## Recovery decision tree from this point

1. Do not duplicate run `33160570463` while it is queued/running.
2. If the metacal canonical manifest is transport-incomplete, preserve that as infrastructure/reproduction INCOMPLETE; do not score support and do not change any scientific threshold.
3. If both canonical manifests pass, allow the frozen 32 microshards to run; each consumed source and metacal interval must match the canonical same-stream digest.
4. Only if all 32 shards pass exact byte identity, row-universe completeness, mapper controls, and deterministic merge may R1 be recorded as `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.
5. Even then, R1 is reproduction only. Exp073P remains the first stage permitted to calculate the frozen positive support leakage `f_invalid`.
6. Covariance restriction/whitening remains CLOSED until Exp073P itself passes physical support.

## Frozen Exp073P downstream criteria — unchanged

- physical redshift rectangle: `0.295 <= z <= 2.33`;
- physical wavenumber ceiling: `k <= 0.06664762008318016 Mpc^-1`;
- positive invalid-support threshold: `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension: `15`;
- no crop-before-normalization;
- no fiducial-P weighting;
- no effective-ell replacement;
- no ad-hoc k/ell cutoff;
- support envelope uses the positive absolute final response;
- signed Wm production response remains signed;
- covariance/SVD/relation/held-out data remain excluded from support selection.

Gate state remains G7/G8/G9 OPEN; covariance/whitening remains CLOSED pending Exp073P support PASS.
