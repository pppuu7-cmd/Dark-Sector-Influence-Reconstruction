# Exp073P split-provenance closure gap and join preregistration — 2026-08-28

## Result of this iteration

Classification: **provenance-architecture finding / prospective repair preregistered**. No physical-support quantity was evaluated.

A code audit of `ci/exp073p_des_public_input_checksum_preflight_v0_1.py` identified a deterministic closure gap. The preflight's local READY condition requires `all_checksum_bound=true` over all six DES Y1 objects, but the same implementation refuses to download/hash any object larger than 200 MiB. The frozen source-zbin object is 2.739 GB and the frozen metacal object is 84.076 GB, so at least those two records necessarily retain `checksum_bound=false` in this implementation. Consequently `READY_FOR_EXP073P_SUPPORT_IMPLEMENTATION` is not a reachable aggregate prerequisite state for the actual input set.

This does not invalidate the exact checksum/reproduction evidence already split across dedicated gates. It shows that those gates require an explicit aggregate join before physical support can execute.

## Fresh canonical Exp073R1 evidence bound during this audit

Canonical run `33160570463` now has **both** whole-object/range-manifest roots completed successfully.

### Source root

- job `98813812482`;
- status `PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M`;
- whole bytes `2,738,626,560`;
- SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- artifact `9681454384`;
- ZIP digest `sha256:58d74d7c6ae9a12150c8b0979e66e75d654e7dbfe83cfe9711e7c5ca836abebe`.

### Metacal root

- job `98813812443`;
- status `PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M`;
- whole bytes `84,075,649,920`;
- SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- 32 exact row ranges, all computed in the same accepted whole-object byte stream;
- artifact `9682053460`;
- ZIP digest `sha256:6a76731e11e13fd08e45647c647ad7bfc00a6548a26b884e351a5c6bb5362686`.

Both canonical-root results explicitly have `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, and `G8_read=false`. They are provenance/reproduction advances only.

## Live R1 state at the iteration checkpoint

Run `33160570463` remains active. Shard 0 job `98818838787` is executing the canonical-bound deterministic microshard; later shards remain queued because the workflow serializes the 32-way matrix. Therefore final R1 status `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` has **not** been reached and Exp073P support remains blocked.

No duplicate heavy run was launched.

## Repair frozen prospectively

The separate aggregate join must require, at minimum, immutable evidence for:

- exact Cosmotheka/public-input pinning;
- large DES source/metacal whole-object identity;
- remaining DES Y1 P2 checksum binding;
- S0 redMaGiC mask+n(z) reproduction;
- **final** R1 four-bin weak-lensing mask reproduction PASS;
- frozen BOSS Exp073J support operator/result;
- frozen Exp073P contract self-test.

Canonical R1 manifests alone cannot satisfy the final-R1 predicate.

The join is forbidden from reading or calculating support fractions, retained dimensions, covariance, nuisance SVD, relation/null controls, or held-out/G8 data. Only after this non-science prerequisite join passes may the already-preregistered physical-support executor be eligible to start.

## Frozen scientific state

Unchanged:

- common physical rectangle `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05`;
- minimum 15 retained full coordinates;
- positive absolute final-response envelope for support;
- signed Wm production response;
- all radial tails outside the frozen rectangle count invalid;
- no crop-before-normalization, effective ell, fiducial-P/model weighting, post-hoc cuts, covariance/SVD/relation/held-out leakage.

Covariance restriction/whitening remains CLOSED pending a genuine Exp073P physical-support PASS.
