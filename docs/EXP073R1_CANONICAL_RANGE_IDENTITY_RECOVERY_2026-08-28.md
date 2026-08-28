# Exp073R1 canonical range-identity recovery — 2026-08-28

## Why the previous v0.3 transport contract was blocked

The frozen scientific mapper itself was not the problem. The issue was input-byte provenance.

The successful whole-object checksum run `33081571259` is authoritative for the two large DES Y1 release objects used by the weak-lensing mask reconstruction. Its immutable artifacts bind:

- source bin file `y1_source_redshift_binning_v1.fits`: 2,738,626,560 bytes, SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`, artifact `9650284556`, artifact ZIP digest `sha256:0eb1fdc7bc2d9f5816e0a003418a41b540cd7281af1f5ceb24a37af82187f5d4`;
- metacalibration file `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: 84,075,649,920 bytes, SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`, artifact `9650627630`, artifact ZIP digest `sha256:5a80c70568a6ed114e4e32990c5399bc8109df10f4d2910abd73441edb122a2b`.

The source SHA had been transcribed incorrectly in later R1 files as `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`. That transcription is now explicitly rejected.

A second issue remained even after correcting that string: the old microshard code computed SHA256 for every consumed byte range, but those range hashes were not cryptographically linked to the previously whole-file-hashed object. A range `Content-Range` header and byte count prove position and length, not byte identity. SHA256 digests of independent ranges cannot be algebraically recombined into a whole-file SHA256.

For that reason PR #158 placed a fail-closed sentinel in the automatic v0.3 launcher before the still-running v0.2 parent could trigger it.

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

The prospective corrected implementation is:

- `ci/exp073r1_fullstream_range_manifest_v0_1.py` — same-stream full-object and exact 32-range SHA256 manifest;
- `ci/exp073r1_desy1_shard_v0_3.py` — range transport, frozen decoding/selection/HEALPix mapping, and exact equality to the canonical range digest;
- `ci/exp073r1_desy1_merge_v0_4.py` — complete 32-shard coverage, canonical digest equality, merged record verification, mask reconstruction and independent repeatability reconstruction;
- `.github/workflows/exp073r1-desy1-canonical-microshards-v0-4.yml` — authoritative prior checksum/R0 preflight, canonical streams, low-concurrency microshards, and merge.

The older v0.3 auto-launch remains blocked until the corrected implementation is independently reviewed and explicitly pinned. No automatic scientific support scoring is enabled by this document.
