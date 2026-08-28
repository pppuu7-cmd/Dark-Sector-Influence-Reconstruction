# DSIR recovery checkpoint — Exp073P after Exp073S0

**Original checkpoint date:** 2026-08-27  
**Latest verified runtime update:** 2026-08-28, canonical Exp073R1 v0.4 run `33160570463`

This document is the primary recovery entry point for resuming the Exp073P branch in another chat/session. Newer facts below supersede older intermediate states; scientific thresholds remain frozen.

## 1. Current validated prerequisites

### Exp073P2 / Exp073Q2 / Exp073S0

- Exp073P2 checksum identity binding is recorded as `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`.
- Exp073Q2 large-FITS schema/row-layout audit: PASS.
- Exp073S0 exact DES Y1 redMaGiC mask + released lens/source n(z) reproduction: `PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`.
  - run `33086762750`, job `98568401949`, artifact `9652504743`;
  - artifact digest `sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e`;
  - exact same-NSIDE `hp.ud_grade(...,4096)` identity passed;
  - redMaGiC retained pixels `6536725`;
  - lens/source n(z) each contain 400 rows and reproduce the frozen schemas.

### Exp073R0 — genuine reproduction/equivalence PASS

- run `33103083736`, job `98625663930`;
- exact workflow/head binding to `94b05d307295d5e9263646983ece9514f9fa2e88`;
- final status `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`;
- sampled rows `131072` across all four bins;
- manual big-endian field decoding exactly matched Astropy;
- independently selected rows and `hp.ang2pix` indices matched exactly;
- `science_gate_scored=false`;
- immutable artifact `9661445512`, ZIP digest `sha256:bfa97a88218cda6e6e6c58d915e8e5b21500fa677a484205691f2f01662ed4d0`.

R0 is a reproduction/numerical-equivalence PASS only. It is not physical-support PASS.

## 2. Exp073R1 transport history and authoritative object identities

### v0.2 terminal result

Run `33135622749`, head `70be4d35199d4132a2ca9da912689519e40bcc84`, reached terminal failure with only shard 0 successful. The correct classification is **reproduction/transport INCOMPLETE**, not physical-support FAIL. No `f_invalid` was scored.

Preserved shard-0 evidence from that old route:

- artifact `9681429458`, name `exp073r1s-shard-0`;
- size `1,627,743` bytes;
- ZIP digest `sha256:1daa27ba0b8b1194cfddaf43c65fa1e592057d202b48f93ac5e9a74cd8101d62`.

It is diagnostic/reproduction evidence only and is not reusable as final R1 PASS.

### Correct whole-object identities

Authoritative large-object identity must remain exactly:

- source `y1_source_redshift_binning_v1.fits`: `2,738,626,560` bytes, SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- metacal `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: `84,075,649,920` bytes, SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.

The previously transcribed source hash `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd` is wrong and must never be restored into the scientific chain.

### Why canonical range manifests are required

An independently downloaded HTTP range plus its own SHA256 establishes that range's transport integrity, but ordinary SHA256 range hashes cannot be algebraically recombined into a trusted whole-file SHA256. Canonical v0.4 therefore streams the entire release object once and computes the whole-file SHA256 and all exact row-range SHA256 values in that same byte stream.

For release bytes `B[0:N)`, table start `s`, row width `r`, total rows `R`, and shard `i=0,...,31`:

`row_lo(i)=floor(R i/32)`, `row_hi(i)=floor(R(i+1)/32)`,

`I_i=B[s+r row_lo(i):s+r row_hi(i)]`.

The stream accepts the range manifest only if `SHA256(B[0:N))` equals the frozen whole-object digest. A decoding shard is accepted only if the exact bytes it consumes reproduce the corresponding canonical `SHA256(I_i)`.

## 3. Canonical Exp073R1 v0.4 — authoritative live branch

Authoritative run:

- run `33160570463`;
- workflow `.github/workflows/exp073r1-desy1-canonical-microshards-v0-4.yml`;
- name `Exp073R1 canonical whole-stream bound microshards v0.4`;
- event `workflow_dispatch`;
- head `e61c61a370cdc4cee5da2aa26cc677a6ad373c70`;
- attempt 1.

### Source canonical root — PASS

Job `98813812482` emitted `PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M` and verified:

- `2,738,626,560` bytes;
- whole SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- 32 exact contiguous row intervals covering every table row exactly once;
- interval hashes computed in the same byte stream as the accepted whole-object SHA256;
- `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false`.

Immutable artifact:

- ID `9681454384`;
- name `exp073r1-canonical-source-e61c61a370cdc4cee5da2aa26cc677a6ad373c70`;
- ZIP digest `sha256:58d74d7c6ae9a12150c8b0979e66e75d654e7dbfe83cfe9711e7c5ca836abebe`;
- size `3052` bytes.

### Metacal canonical root — PASS

Job `98813812443` emitted the same provenance status and verified:

- `84,075,649,920` bytes;
- whole SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- 32 exact contiguous row intervals covering every table row exactly once;
- canonical range hashes computed in the same accepted whole-object stream;
- prefix `17280` bytes and FITS tail `1710` bytes;
- `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false`.

Immutable artifact:

- ID `9682053460`;
- name `exp073r1-canonical-metacal-e61c61a370cdc4cee5da2aa26cc677a6ad373c70`;
- ZIP digest `sha256:6a76731e11e13fd08e45647c647ad7bfc00a6548a26b884e351a5c6bb5362686`;
- size `3129` bytes.

Both canonical roots are genuine provenance/reproduction advances, **not** final R1 PASS and not physical-support PASS.

### Live microshard checkpoint

At the latest verified checkpoint, shard 0 job `98818838787` is executing `Execute canonical-bound deterministic microshard`; later shards are queued by the serial `max-parallel=1` matrix. Final R1 PASS has not yet been reached. No duplicate canonical v0.4 run should be launched while this run is active.

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

A genuine final R1 PASS may only be `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`; canonical manifests or partial shard success cannot substitute for it.

## 5. Newly identified Exp073P split-provenance closure gap

Audit of `ci/exp073p_des_public_input_checksum_preflight_v0_1.py` found an architectural inconsistency in the **authorization plumbing**, not in the frozen physics contract.

The preflight uses `MAX_DOWNLOAD_BYTES = 200 * 1024 * 1024` and sets its local `support_evaluation_authorized` only when all six DES public objects have `checksum_bound=true` in that same run. Yet the source object is `2,738,626,560` bytes and metacal is `84,075,649,920` bytes. For any object above the cap the code never enters the download/hash branch, so `checksum_bound` remains false.

Therefore `READY_FOR_EXP073P_SUPPORT_IMPLEMENTATION` in this old all-in-one preflight is structurally unreachable for the actual frozen six-object set. This is **not** a support FAIL and does not invalidate separately certified inputs. It means a separate immutable aggregate prerequisite join is required.

Prospective join semantics are frozen in `docs/METHOD_EXP073P_SPLIT_PROVENANCE_JOIN_V0_1.md` and guarded by `ci/exp073p_split_provenance_join_contract_selftest_v0_1.py`.

The future aggregate join must require all of:

1. exact Cosmotheka/public-input provenance, pin `7bde066626f66cd7bbe79cc46224d2342840e463`;
2. exact source/metacal whole-object identities;
3. P2 remaining DES Y1 checksum binding;
4. S0 redMaGiC mask+n(z) reproduction PASS;
5. **final** R1 four-bin weak-lensing mask reproduction PASS;
6. frozen BOSS Exp073J support operator/result;
7. frozen Exp073P support-contract self-test.

The join itself must keep all of `support_fraction_evaluated`, `f_invalid_computed`, `retained_dimension_evaluated`, `covariance_read`, `nuisance_svd_read`, `relation_null_read`, `heldout_read`, and `G8_read` false. It is a provenance authorization boundary only.

## 6. Frozen Exp073P scientific acceptance criteria — unchanged

Do not modify post hoc:

- common physical redshift support: `0.295 <= z <= 2.33`;
- common physical wavenumber ceiling: `k <= 0.06664762008318016 Mpc^-1`;
- positive invalid-support threshold: `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension: `15`;
- classifying DES map resolution: `nside=4096`;
- exact Limber map `k=(ell+1/2)/chi(z)` under the pinned background;
- support selection uses the positive absolute final-response envelope;
- signed Wm production response remains signed;
- all radial tails outside the redshift rectangle count invalid;
- no crop-before-normalization;
- no fiducial-P/model weighting;
- no effective ell;
- no ad-hoc k/ell cutoff;
- no covariance/SVD/relation/held-out information may influence support selection.

Frozen BOSS Exp073J result remains `54/240` retained (`27/120` cap; `9/40` in each P0/P2/P4 block). This does not by itself determine the combined DES+BOSS Exp073P result.

## 7. Next admissible actions

1. Let canonical v0.4 run `33160570463` progress without duplication.
2. Classify any shard transport/runtime failure as reproduction INCOMPLETE unless an exactness violation is demonstrated; never convert infrastructure failure into `f_invalid`.
3. Require all 32 canonical ranges and deterministic merge/reconstruction before final R1 PASS.
4. After final R1 PASS, construct/run the preregistered non-science aggregate prerequisite join; do not use the legacy preflight READY flag as the aggregate gate.
5. Only after aggregate prerequisite PASS may the already-frozen Exp073P physical-support calculation execute.
6. Only Exp073P support PASS can open covariance restriction/whitening. Nuisance SVD, quotient/relation/null, fresh G8, and held-out work remain downstream in the frozen order.

## 8. Gate state

- G7: OPEN
- G8: OPEN
- G9: OPEN
- Exp073P physical support: BLOCKED pending final R1 PASS and aggregate prerequisite join
- covariance/whitening: CLOSED pending Exp073P support PASS
