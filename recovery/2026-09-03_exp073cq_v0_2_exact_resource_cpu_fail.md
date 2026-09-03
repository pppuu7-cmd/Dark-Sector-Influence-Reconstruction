# Exp073CQ v0.2 — exact resource CPU-target FAIL

Date: 2026-09-03
Scope: DSIR / Wm_S3 resource qualification only. Scientific credit: +0/+0.

## Terminal authority

- GitHub Actions run: `33752799918`
- hosted authorization job: `100640020607` — SUCCESS
- self-hosted job: `100640079011` on `DSIR-HOME-PC` — terminal FAILURE only because the prospectively frozen final classifier returned the resource-fail exit code
- launch/source head: `011852feb6d40152f4b33bde732b00520cd28f79`
- successor checkpoint namespace: `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2`
- successor seed head: `4f528424a2d2b3e32aeb4a68d73265ef9de8bd4e`
- terminal durable checkpoint head: `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`
- contract fingerprint: `87b58bf120510bec50b21851d7ff21269689db6dcdd906cb3a14102e4a4f5f97`
- authority artifact: `9897551836`
- artifact archive digest: `sha256:0f10c863ee65f3d7c27177a324cafe2830e6b8b1096da054e35c638b26d6104c`

## What completed

Hosted-seeded exact restore succeeded. NaMaster 2.7 environment and frozen helper completed successfully. Imported bands `0..28` remained read-only. Numerical allowlist was exactly bands `29..38`, and every one of those ten bands completed and was durably checkpointed before final classification.

Durable new-band heads in completion order:

- band 29: `c4ad1e538e7040d89bc9dd34bfa7499d7b72541c`
- band 30: `f2b091e92b1da80aaca7c60b4e6e37b03a041d2e`
- band 31: `ad9d79d0b32a6a097669966c8b94b7424521c34e`
- band 32: `313a791afce05ec8056799073b6d3bb6d6be11fa`
- band 33: `dad93ef50e1d0b1a31e50041514e749aa2c94d9a`
- band 34: `51c95828fe9776960c727b73f443c25220c5c686`
- band 35: `5cf0b941e54db91a9aa8472896cde9a0fedb792b`
- band 36: `0ebdb61c8b1503ca4c8a50c4ec7d923e717a5e44`
- band 37: `6405b69d247b408aad80b99792d1a15c6c4a66e4`
- band 38: `8f5124d2d0319047f50cc73db915bbab61540408`
- telemetry: `928b6c099b6af16d502889ab9e46900b3864ff36`
- frozen final: `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`

## Frozen terminal measurements

- `array_equal_reference_0_7 = true`
- `sha_equal_reference_0_7 = true`
- first-8 SHA256 = reference SHA256 = `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`
- canonical dtype `<f8`
- target shape `[39,12288]`
- `swap_increase_kib = 0`
- numerical active wall time for new bands 29..38: `7452.963947676 s`
- sum worker numerical CPU: `39579.9931101 s`
- effective compute cores: `5.310637940552754`
- CPU fraction of 8: `0.6638297425690942`
- frozen requirement: `>=0.90`
- terminal token: `FAIL_EXP073CQ_V0_2_WM_S3_CPU_TARGET`

## Classification

**RESOURCE/PERFORMANCE FAIL, +0/+0.**

This is NOT a Wm_S3 scientific arithmetic failure. Exact control passed, finite/canonical output was retained, all required numerical bands completed, and swap safety passed. The only failed frozen criterion was CPU utilization: `0.6638297425690942 < 0.90`.

No tolerance, rounding, smoothing, averaging, thread-count change, or post-hoc threshold rescue is permitted. Exp073CQ v0.2 remains a preserved negative resource result.

## Consequence / next gate

Complete-band outer scheduling is still too coarse for the heterogeneous cost of bands 29..38. The next permitted resource successor may split only the independent output `ll3` domain while preserving, for each fixed `ll3`, the exact frozen `ll2` ordering, both Wigner recurrences, ascending `l1` accumulation, multiplication and `acc += xi` recurrence. Reassembly must be placement/concatenation only, never an arithmetic reduction.

A research-only Exp073CR preflight already supplied independent exactness evidence: hosted run `33754644074`, job `100646005106`, artifact `9892971697`, digest `sha256:766184eb42ef696e3c493d55ebb78cbc6c4fab83baf7c0d17bbdb7b3cf104a72`; bands 0, 7 and 15 matched immutable complete-band references bit-for-bit under two distinct ll3 partitions. This evidence is +0/+0 and does not itself authorize home execution.

The authoritative successor must be prospectively preregistered, use a fresh dedicated checkpoint namespace, exactly 8 persistent outer workers, nested numerical threads=1, frozen shard boundaries/order, durable complete-shard checkpoints, exact restore/provenance, exact complete-band reconstruction against the preserved Exp073CQ complete-band payloads, zero positive swap increase, and the unchanged CPU fraction threshold `>=0.90`. Hosted seed/static/bitwise audit must PASS before self-hosted execution.
