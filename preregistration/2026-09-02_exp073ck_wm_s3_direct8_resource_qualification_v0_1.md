# Exp073CK — Wm_S3 direct-8 resource qualification v0.1

**Date:** 2026-09-02
**Classification:** prospective resource/numerical qualification; `+0/+0`
**Task:** `Wm_S3` (source-bin S3, not spin-3)

## Purpose

Prospectively supersede only the resource-schedule sentence in the 2026-09-02 Wm_S3 authority-gap audit that called for staged `4 -> 6 -> 8`. The user has explicitly selected a direct 8-thread qualification before execution. Historical Exp073AA/AF/X2 are immutable and remain blocked/non-authoritative.

## Frozen scientific arithmetic

- DES `NSIDE=4096`, RING/C.
- source-bin S3 is exactly Exp073R1 bin 3: selected rows `4,196,641`; pixel-record bytes `16,786,564`; pixel-record SHA256 `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; unique pixels `2,943,132`; occupancy SHA256 `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.
- lens public-file bytes `104,595,840`; SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.
- `ell=0..12287`, `L=12288`, 39 frozen bands.
- Wm coupling signature `(0,2,0,2)` and selected semantics `TE <- TE`.
- canonical little-endian `<f8`; no tolerance/ULP/rounding/averaging/smoothing rescue.
- no effective-ell/z/k or fiducial-P shortcut.

## Direct-8 qualification rule

1. Build a fresh real Wm_S3 mask PCL with the proven memory-stable ALM spill/reload construction, changing only source bin `2 -> 3` relative to the admitted Wm_S2 infrastructure helper.
2. Compile the frozen range streaming helper `ci/exp073ca_stream_general_coupling_range_v0_1.c` with the frozen strict FP flags.
3. On the real Wm_S3 PCL and full `L=12288`, compute frozen band index 20 (`ell 1098..1246`) once with a 1-thread canonical reference and once with 8 threads.
4. Require exact `np.array_equal` and identical canonical SHA256. A mismatch is a numerical/scientific exact-equivalence FAIL for this prospective resource plan; no tolerance rescue.
5. Record wall time, process peak RSS, `/proc/meminfo` swap before/after, and PCL-build `/usr/bin/time -v` telemetry. Qualification is resource-safe only if the 8-thread computation completes with finite output and does not increase swap usage during the exact-comparison process.
6. If all checks pass, freeze `8` as the Wm_S3 successor concurrency. The staged 4 and 6 runs are not required for this new version.
7. If infrastructure/network/runner failure occurs before comparison, classify `INFRASTRUCTURE_INCOMPLETE`, `+0/+0`; do not call it a scientific FAIL.

## Coordination

- Hosted fail-closed authorization must run before self-hosted scheduling.
- At authorization, no other DSIR run may be queued or in progress except the current run.
- At most one heavy DSIR job may own `DSIR-HOME-PC`.
- This qualification does not itself create Wm_S3 angular authority and changes Article-3 readiness by `+0/+0`.
- A full prospectively bound Wm_S3 A/B exact-repeatability successor may start only after `PASS_EXP073CK_WM_S3_DIRECT8_RESOURCE_QUALIFICATION_V0_1` is established.
