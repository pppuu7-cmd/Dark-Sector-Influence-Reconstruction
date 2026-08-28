# Exp073R1 v0.2 terminal classification + canonical v0.4 progress — 2026-08-28

## Scope

This record is an append-only research/recovery checkpoint. It records only facts independently verified from GitHub Actions and the repository in this iteration. Exp073R1 remains an input-reproduction stage: this record does **not** evaluate physical support, does not compute `f_invalid`, and does not open covariance/whitening or G8.

## Exp073R1 v0.2 — terminal reproduction classification

Workflow run `33135622749` is terminal:

- workflow: `.github/workflows/exp073r1-desy1-sharded-measurement-v0-2.yml`;
- head SHA: `70be4d35199d4132a2ca9da912689519e40bcc84`;
- run attempt: 2;
- status: `completed`;
- conclusion: `failure`.

The correct scientific classification is **reproduction/transport INCOMPLETE**, not physical-support FAIL. No `f_invalid` was scored.

### Verified shard evidence

Shard 0, job `98761777728`, completed its deterministic shard computation and emitted `PASS_DESY1_R1_SHARD`. It processed parent rows `[0,17116374)` and recorded:

- bin 0: selected rows `1,980,721`, unique pixels `13,024`;
- bin 1: selected rows `2,002,856`, unique pixels `13,449`;
- bin 2: selected rows `1,925,849`, unique pixels `13,142`;
- bin 3: selected rows `951,631`, unique pixels `11,959`;
- source consumed-range SHA256: `47ee44b1d2f90ac7978ce5d208c27bf34ae589431c4c07fea0404fe23330a51e`;
- metacal consumed-range SHA256: `ed67be2f25bd6b8772e82f3a993d03bbce74705af7331d842071cf19fd1f05cb`;
- `science_gate_scored=false`.

Shard 1, job `98761778039`, is independently verified as infrastructure/transport incomplete after a curl/read timeout while transporting its metacal byte range. Its exact status was `INCOMPLETE_DESY1_SHARDED_MASK_EXP073R1`; no support gate was scored.

Shard 2, job `98761777874`, is independently verified as infrastructure/transport incomplete after `HTTP Error 502: Bad Gateway` while transporting its metacal byte range. Its exact status was `INCOMPLETE_DESY1_SHARDED_MASK_EXP073R1`; no support gate was scored.

Jobs for shards 3–7 also failed at the deterministic transport/execution step in the terminal run. Their individual exception causes were not re-audited in this iteration, so no stronger per-shard cause is asserted here.

Consequence: the partial v0.2 shard evidence is useful for transport/reproduction diagnostics only. It cannot be combined into a physical-support result and cannot authorize Exp073P.

## Canonical byte-identity repair

PR #159 replaced the insufficient independent-range provenance contract with a same-stream whole-object/range-digest bridge. For bytes `B[0:N)`, table start `s`, row width `r`, row count `R`, and shard index `i=0,...,31`, define

`row_lo(i)=floor(R i/32)`, `row_hi(i)=floor(R(i+1)/32)`

and

`I_i = B[s+r row_lo(i) : s+r row_hi(i)]`.

A single sequential stream computes simultaneously

`H_full = SHA256(B[0:N))`

and

`H_i = SHA256(I_i)`

for all 32 intervals. The stream is accepted only when `H_full` equals the already-authoritative whole-object SHA256. Each later shard must independently recover its exact interval and satisfy `SHA256(I_i)==H_i`. This cryptographically binds decoded shard bytes to a verified whole release object without assuming any fiducial power spectrum or scientific support result.

The authoritative whole-object identities frozen in the current v0.4 workflow are:

- source `y1_source_redshift_binning_v1.fits`: `2,738,626,560` bytes, SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- metacal `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: `84,075,649,920` bytes, SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.

The previously transcribed source string `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd` is explicitly rejected.

## Canonical Exp073R1 v0.4 — live verified state

The canonical run is **run `33160570463`**, not any previously guessed/mis-associated run ID.

Verified binding:

- workflow: `.github/workflows/exp073r1-desy1-canonical-microshards-v0-4.yml`;
- workflow name: `Exp073R1 canonical whole-stream bound microshards v0.4`;
- event: `workflow_dispatch`;
- head branch: `main`;
- head SHA: `e61c61a370cdc4cee5da2aa26cc677a6ad373c70`;
- run attempt: 1;
- current status at this checkpoint: `in_progress`.

### Source canonical manifest — PASS

Job `98813812482` completed successfully. The same-stream root computation emitted

`PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M`

with:

- observed bytes: `2,738,626,560`;
- whole SHA256: `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- 32 exact contiguous row ranges;
- exact once-only table-row partition;
- range hashes computed in the same stream as the whole-object hash;
- `science_gate_scored=false`, `f_invalid_computed=false`, covariance/G8 unread.

Immutable source-root artifact:

- artifact ID `9681454384`;
- name `exp073r1-canonical-source-e61c61a370cdc4cee5da2aa26cc677a6ad373c70`;
- ZIP digest `sha256:58d74d7c6ae9a12150c8b0979e66e75d654e7dbfe83cfe9711e7c5ca836abebe`;
- size `3052` bytes;
- nonexpired at this checkpoint.

This is a real provenance/reproduction achievement, but **not** a physical-support PASS.

### Metacal canonical manifest — still running

Job `98813812443` is still executing `Stream whole release object once and derive exact 32-range SHA256 manifest`. The assertion and artifact-upload steps remain pending at this checkpoint. Therefore no metacal canonical-root PASS is claimed yet.

No duplicate heavy v0.4 run was started.

## Static v0.4 contract audit

The current main workflow was re-read in this iteration. It requires:

- genuine R0 PASS run `33103083736` and exact R0 workflow/head binding;
- authoritative prior whole-object checksum run `33081571259` and immutable artifacts;
- exact source/metacal byte counts and whole SHA256 values above;
- two same-stream canonical manifests, each with all 32 exact row ranges;
- every consumed shard range to match its canonical digest;
- all 32 shards before merge;
- exact 136,930,995-row universe and deterministic mask reconstruction;
- `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false` through R1.

Therefore the implementation remains fail-closed with respect to Exp073P: a partial transport success cannot be promoted into a support result.

## Frozen downstream boundary

Exp073P remains locked until a genuine full Exp073R1 reproduction PASS exists. After that, Exp073P must still independently apply the already-frozen physical-support contract:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- positive absolute final-response support envelope;
- `f_invalid <= 0.05`;
- at least 15 full retained coordinates;
- no crop-before-normalization;
- no fiducial-P weighting;
- no effective ell or ad-hoc k/ell cutoff;
- signed Wm production response remains signed;
- no covariance/SVD/relation/held-out information in support selection.

Only an Exp073P physical-support PASS can open covariance restriction/whitening.

## Gate state at this checkpoint

- G7: OPEN
- G8: OPEN
- G9: OPEN
- covariance/whitening: CLOSED pending Exp073P support PASS
