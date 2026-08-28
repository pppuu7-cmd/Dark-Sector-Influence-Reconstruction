# DSIR recovery checkpoint — Exp073P after Exp073S0

**Original checkpoint date:** 2026-08-27  
**Latest verified runtime update:** 2026-08-28 GitHub Actions state

This document is the primary recovery entry point for resuming the Exp073P branch in another chat/session. Newer facts below supersede older intermediate states; scientific thresholds remain frozen.

## 1. Current validated prerequisites

### Exp073P2 / Exp073Q2 / Exp073S0

- Exp073P2 checksum identity binding: `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`.
- Exp073Q2 large-FITS schema/row-layout audit: PASS.
- Exp073S0 exact DES Y1 redMaGiC mask + released lens/source n(z) reproduction: `PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`.
  - run `33086762750`, job `98568401949`, artifact `9652504743`;
  - artifact digest `sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e`;
  - exact same-NSIDE `hp.ud_grade(...,4096)` identity passed;
  - redMaGiC retained pixels `6536725`;
  - lens/source n(z) each contain 400 rows and reproduce the frozen schemas.

### Exp073R0 — genuine reproduction/equivalence PASS

Earlier R0 attempts were infrastructure-incomplete, but the hardened run is now resolved:

- run `33103083736`, job `98625663930`;
- exact workflow/head binding to `94b05d307295d5e9263646983ece9514f9fa2e88`;
- final status `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`;
- sampled rows `131072` across all four bins;
- manual big-endian field decoding exactly matched Astropy;
- independently selected rows and `hp.ang2pix` indices matched exactly;
- `science_gate_scored=false`;
- immutable artifact `9661445512`, ZIP digest `sha256:bfa97a88218cda6e6e6c58d915e8e5b21500fa677a484205691f2f01662ed4d0`.

R0 is a reproduction/numerical-equivalence PASS only. It is not physical-support PASS.

## 2. Exp073R1 transport history and current authoritative implementation

### v0.2 terminal result

Run `33135622749`, head `70be4d35199d4132a2ca9da912689519e40bcc84`, attempt 2 is now `completed/failure`.

The correct classification is **reproduction/transport INCOMPLETE**, not physical-support FAIL. No `f_invalid` was scored.

Verified evidence:

- shard 0 job `98761777728` completed deterministic mapping and emitted `PASS_DESY1_R1_SHARD`;
- shard 1 job `98761778039` is transport-incomplete after read timeout;
- shard 2 job `98761777874` is transport-incomplete after HTTP 502;
- shards 3–7 failed their execution step, but their individual exception causes were not re-audited in the latest recovery iteration and therefore are not overclassified here.

Shard 0 selected-row/unique-pixel counts were:

- bin 0: `1,980,721 / 13,024`;
- bin 1: `2,002,856 / 13,449`;
- bin 2: `1,925,849 / 13,142`;
- bin 3: `951,631 / 11,959`.

These partial numbers are diagnostic only and cannot be used as support evidence.

### Correct whole-object identities

The authoritative prior full-object checksum run is `33081571259`. Current canonical R1 must bind exactly:

- source `y1_source_redshift_binning_v1.fits`: `2,738,626,560` bytes, SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- metacal `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: `84,075,649,920` bytes, SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.

The previously transcribed source hash `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd` is wrong and must never be restored into the scientific chain.

### Why independent range hashes were insufficient

An HTTP `Content-Range`, byte count, and SHA256 of an independently downloaded interval establish the interval's transport integrity, but do not by themselves prove that the interval belongs to the same whole object whose SHA256 was previously certified. Ordinary SHA256 range hashes cannot be algebraically recombined into the whole-file SHA256.

PR #159 repaired this provenance gap. For release bytes `B[0:N)`, table start `s`, row width `r`, total rows `R`, and microshard `i=0,...,31`, define

`row_lo(i)=floor(R i/32)`, `row_hi(i)=floor(R(i+1)/32)`,

`I_i=B[s+r row_lo(i):s+r row_hi(i)]`.

One canonical sequential stream computes simultaneously

`H_full=SHA256(B[0:N))`

and every

`H_i=SHA256(I_i)`.

The stream is accepted only if `H_full` equals the authoritative whole-object hash. Later decoding of microshard `i` is accepted only if the bytes actually consumed reproduce canonical `H_i`. This creates the missing cryptographic bridge from each decoded range to the trusted whole release object.

## 3. Canonical Exp073R1 v0.4 — current live state

The authoritative active run is:

- run `33160570463`;
- workflow `.github/workflows/exp073r1-desy1-canonical-microshards-v0-4.yml`;
- workflow name `Exp073R1 canonical whole-stream bound microshards v0.4`;
- event `workflow_dispatch`;
- head `e61c61a370cdc4cee5da2aa26cc677a6ad373c70`;
- attempt 1;
- status at this checkpoint: `in_progress`.

Any prior internal/messaging association of another run ID with canonical v0.4 is superseded by this exact binding.

### Source canonical root: verified PASS

Job `98813812482` emitted `PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M` and verified:

- exact `2,738,626,560` bytes;
- exact whole SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- 32 exact contiguous row intervals covering every table row exactly once;
- interval hashes were computed in the same byte stream as the accepted whole-object SHA256;
- no science/support/covariance/G8 quantity was read or scored.

Immutable artifact:

- ID `9681454384`;
- name `exp073r1-canonical-source-e61c61a370cdc4cee5da2aa26cc677a6ad373c70`;
- ZIP digest `sha256:58d74d7c6ae9a12150c8b0979e66e75d654e7dbfe83cfe9711e7c5ca836abebe`;
- size `3052` bytes.

This is a genuine provenance/reproduction advance, **not** a physical-support PASS.

### Metacal canonical root: unresolved at this checkpoint

Job `98813812443` is still executing `Stream whole release object once and derive exact 32-range SHA256 manifest` for the 84,075,649,920-byte metacal release object. Its contract assertion and artifact upload remain pending. Do not claim metacal root PASS unless this job later completes successfully with the exact frozen SHA256.

No duplicate canonical v0.4 run should be launched while this run is active.

## 4. Frozen Exp073R1 mapper contract

R1 remains an input-reproduction stage with:

- parent rows exactly `136930995`;
- source table start `5760`, row width `20` bytes;
- metacal table start `17280`, row width `614` bytes;
- selection `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- bins `t=0,1,2,3`;
- HEALPix `nside=4096`, RING, celestial coordinates, `lonlat=True`;
- unweighted selected-pixel count construction;
- selected pixel-index records preserved in parent-row order;
- deterministic independent reconstruction for repeatability;
- all 32 canonical-bound shards required before merge;
- `science_gate_scored=false`;
- `f_invalid_computed=false`;
- `covariance_read=false`;
- `G8_read=false`.

A genuine R1 PASS may only be `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`; it cannot itself open covariance.

## 5. Frozen Exp073P scientific acceptance criteria — unchanged

Do not modify post hoc:

- common physical redshift support: `0.295 <= z <= 2.33`;
- common physical wavenumber ceiling: `k <= 0.06664762008318016 Mpc^-1`;
- positive invalid-support threshold: `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension: `15`;
- classifying DES map resolution: `nside=4096`;
- support selection uses the positive absolute final-response envelope;
- signed Wm production response remains signed;
- all radial tails outside the redshift rectangle count invalid;
- no crop-before-normalization;
- no fiducial-P weighting;
- no effective ell;
- no ad-hoc k/ell cutoff;
- no covariance/SVD/relation/held-out information may influence support selection.

Frozen BOSS Exp073J result remains `54/240` retained (`27/120` cap; `9/40` in each P0/P2/P4 block). This does not by itself determine the combined DES+BOSS Exp073P result.

## 6. Next admissible actions

1. Resolve canonical v0.4 run `33160570463` without launching a duplicate.
2. If the metacal whole-stream manifest is infrastructure/transport incomplete, preserve that classification; harden only transport mechanics prospectively and do not score `f_invalid`.
3. If both canonical manifests pass, allow the already-frozen 32 canonical-bound microshards to execute.
4. Only if all 32 ranges bind exactly, the full row universe is complete, and deterministic merge/reconstruction passes may R1 be classified reproduction PASS.
5. Only after genuine R1 PASS may the already-frozen Exp073P physical-support calculation execute.
6. Only Exp073P support PASS can open covariance restriction/whitening. G8 relation/null and G9 held-out remain downstream and must not leak into support selection.

## 7. Gate state

- G7: OPEN
- G8: OPEN
- G9: OPEN
- covariance/whitening: CLOSED pending Exp073P support PASS
