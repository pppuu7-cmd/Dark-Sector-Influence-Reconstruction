# DSIR recovery checkpoint — local NaMaster benchmark, AQ replica B complete / A active

**Date:** 2026-08-31  
**Classification:** infrastructure benchmark + authoritative AQ status update. No scientific gate change. `+0` readiness.

## Local compute benchmark

A direct test was performed in the model execution container to determine whether the local runtime could replace multi-hour GitHub-hosted `NSIDE=4096` angular calculations.

Durable benchmark record:

`docs/LOCAL_COMPUTE_BENCHMARK_2026-08-31.md`

latest result commit:

`90c77f92e273a526803a2a1f20e2efeffbe87ef4`.

### Exact R1 data preparation

Immutable Exp073R1 artifact `9720335366` was downloaded locally.

Exact S1 source-count-map construction on `NPIX=201326592` reproduced the frozen occupancy SHA

`fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1`.

Process wall time was `3.39 s`.

### Memory/transform tests

- two fully touched float64 NSIDE=4096 maps fit simultaneously at ~3.1 GiB RSS;
- single-thread SciPy `rfft2` on 8192x8192 float64 completed in `1.736 s`;
- these showed strong local CPU/memory-array speed but did not test the NaMaster coupling bottleneck.

### Exact NaMaster 2.7 environment export

Non-authoritative dependency-only workflow:

- workflow commit `3e9925926571431ea9de2cf2ca917ee64865d46c`;
- run `33337005305`;
- job `99325597211`;
- artifact `9739351741`;
- digest `sha256:be3886f11b47c665e7494f6a7edb50d01df30c133565666b326dc482a88f0c79`;
- pymaster `2.7`, healpy `1.20.0`, Python `3.11.16`.

This workflow exists only to make a local benchmark possible; it is not an Article-3 execution authority.

### Actual local NSIDE=4096 NaMaster result

A real non-authoritative `WW_S1_S1` `NmtWorkspace.compute_coupling_matrix` was started with:

- exact R1 S1 source record;
- NSIDE=4096;
- 39 frozen bandpower edges;
- spin-2 x spin-2 field;
- frozen single-thread environment controls;
- no support/covariance/nuisance/G7/G8 reads.

Before coupling:

- source map `2.185 s`;
- spin-2 field creation `5.374 s`;
- RSS after field ~1.80 GiB.

During coupling the process was terminated by `SIGKILL` after total wall time ~24 s.

Cgroup evidence:

- `memory.max = 4294967296` bytes (4 GiB);
- `memory.peak = 4294967296`;
- `oom=1`;
- `oom_kill=1`;
- `/usr/bin/time` max RSS before kill `3898528 KiB`.

Classification:

`LOCAL_INFRASTRUCTURE_OOM_BENCHMARK_ONLY`.

This is not a numerical/scientific FAIL and produced no angular window/hash. The local chat-runtime cannot currently replace the hosted exact NSIDE=4096 NaMaster route because its 4 GiB cgroup memory ceiling is too small.

## Exp073AQ authoritative status during checkpoint

Run:

`33327372191`.

Replica B job `99299799338` completed successfully:

- exact compute started `2026-08-30T18:13:24Z`;
- exact compute completed `2026-08-30T21:17:56Z`;
- compute duration ~`3 h 04 min 32 s`;
- replica artifact `9739045909`;
- artifact digest `sha256:4069f4deb3c608f6fb2c1fa686181746901befbe945cc07374c7d32346778e2f`.

The B replica numerical/window contents were **not read** while A remains active; only job status/timing/provenance were inspected.

Replica A job `99299799192` remained IN_PROGRESS in the exact compute step at the latest checkpoint inspection.

Therefore:

- no AQ comparator authority exists yet;
- Wm_S1 is not admitted yet;
- do not launch Wm_S2;
- readiness remains 52%.

If A completes, allow the frozen aggregator/comparator to classify exact twin equality. If A times out/fails before comparator, apply Exp073AY infrastructure-INCOMPLETE rules; do not reuse partial A output and do not call it repeatability FAIL.

## Scientific state

Unchanged:

- Article-3 readiness = `52%`;
- Layer A OPEN;
- Layer B OPEN;
- covariance/whitening BLOCKED;
- G7/G8/G9 OPEN.
