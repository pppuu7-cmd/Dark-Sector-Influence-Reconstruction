# DSIR local compute benchmark — 2026-08-31

**Classification:** local/non-hosted infrastructure benchmark only. Not scientific authority. Not an angular authority. `+0` readiness.

## Environment

- 5 x Intel Xeon Platinum 8370C vCPU @ 2.80 GHz exposed to the local execution container.
- host-visible `free` reported ~5.9 GiB RAM and no swap.
- actual cgroup-v2 hard memory limit: exactly `4294967296` bytes = **4.0 GiB**.
- ~38 GiB free local disk at benchmark start.
- base Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0.
- base image initially lacked `healpy`, `pymaster`, and `astropy`.
- frozen DSIR single-thread environment variables were applied for the benchmarks where relevant.

## Exact R1 authority materialization

Downloaded immutable hosted Exp073R1 artifact `9720335366` into the local execution environment.

- compressed ZIP size: ~64 MiB;
- unpacked payload: ~203 MiB;
- includes exact `NSIDE=4096` source-bin pixel-index records and source occupancy bitpacks used by the Article-3 angular runner.

## Exact NSIDE=4096 source-count-map benchmark

Executed the exact `source_count_map` construction logic from `ci/exp073aa_article3_des_angular_task_runner_v0_1.py` for source bin S1 using the immutable R1 record:

- `NPIX = 201326592`;
- selected rows = `7851711`;
- unique occupied pixels = `4339193`;
- dense float64 map logical size = `1610612736` bytes;
- exact pixel-record SHA matched frozen authority;
- exact occupancy SHA matched frozen authority:
  `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1`.

Timing from the local benchmark process:

- record SHA: `0.338 s`;
- `np.add.at` source-map accumulation: `0.625 s`;
- count/unique checks: `0.587 s`;
- occupancy bitpack+SHA: `0.358 s`;
- Python-internal total: `1.910 s`;
- `/usr/bin/time` process wall clock: `3.39 s`.

This is a genuine exact Article-3 data-preparation computation, but it is not the expensive NaMaster coupling-matrix step and therefore cannot be used to infer angular scientific authority.

## Full-map memory stress

Two complete float64 HEALPix-sized arrays (`2 x 201326592` elements) were allocated and fully touched simultaneously.

- peak RSS: ~`3255840 KiB` (~3.1 GiB);
- first full-map fill: `6.52 s`;
- second full-map fill: `6.86 s`;
- full streaming `a += b`: `0.908 s`;
- effective three-stream bandwidth estimate: ~`5.32 GB/s`;
- checksum passed.

Therefore the local environment can physically hold and touch at least two complete NSIDE=4096 float64 maps without OOM, but only with limited headroom below the real 4 GiB cgroup ceiling.

## Single-thread transform benchmark

Executed SciPy `rfft2` on an `8192 x 8192` float64 array with `workers=1` and the DSIR single-thread environment controls.

- input size: `0.5 GiB`;
- output size: ~`0.5001 GiB` complex;
- transform time: `1.736 s`;
- whole-process wall clock including construction/cleanup: `7.89 s`;
- peak RSS: ~`1172152 KiB`.

This indicates strong local single-thread/memory-transform performance, but FFT2 is not a substitute for HEALPix spherical harmonic transforms or NaMaster coupling-matrix construction.

## Portable exact NaMaster 2.7 benchmark environment

A dedicated non-authoritative GitHub workflow was used only to package the exact dependency lineage so that the bottleneck could be attempted locally:

- workflow run `33337005305`;
- job `99325597211`;
- artifact `9739351741`;
- artifact digest `sha256:be3886f11b47c665e7494f6a7edb50d01df30c133565666b326dc482a88f0c79`;
- workflow commit `3e9925926571431ea9de2cf2ca917ee64865d46c`;
- environment Python `3.11.16`;
- `pymaster 2.7`;
- `healpy 1.20.0`;
- `numpy 2.4.6`;
- `astropy 8.0.1`.

The packed environment was materialized locally and `conda-unpack` completed successfully. This workflow is benchmark infrastructure only and is not an execution-authority qualification.

## Actual NaMaster NSIDE=4096 WW_S1_S1 attempt

Executed a local non-authoritative benchmark matching the key physical/angular bottleneck for task `WW_S1_S1`:

- same immutable R1 S1 source pixel record;
- `NSIDE=4096`;
- true ell range through `12287`;
- the same 39 frozen bandpower edges;
- spin-2 x spin-2 `NmtField` construction;
- `NmtWorkspace.compute_coupling_matrix(f,f,b)`;
- frozen DSIR single-thread environment variables;
- no radial kernel, physical support, covariance, nuisance, relation/null or G8 read.

Observed before the coupling call:

- exact source-count map: `2.185 s`;
- source occupancy authority matched exactly;
- spin-2 `NmtField` construction: `5.374 s`;
- RSS after field creation: ~`1883744 KiB` (~1.80 GiB).

The real NaMaster coupling started successfully but the process was killed by `SIGKILL` during `compute_coupling_matrix` after a total process wall time of about `24.02 s`.

Peak RSS reported by `/usr/bin/time`:

`3898528 KiB` (~3.72 GiB).

Immediately after termination, cgroup-v2 reported:

- `memory.max = 4294967296` bytes;
- `memory.peak = 4294967296` bytes;
- `memory.events: oom=1`;
- `memory.events: oom_kill=1`.

Therefore this was an unambiguous **local infrastructure OOM**, not a numerical/scientific failure and not evidence about the final WW window.

No selected bandpower window was produced and no local angular hash exists.

## Comparison point from GitHub hosted authority route

Historical Exp073X2 primary-P Wm_S0 exact replica computation on `ubuntu-24.04` required approximately `1 h 56 min 32 s` for each replica compute step.

Current Exp073AQ Wm_S1 replica B completed its exact compute step from `2026-08-30T18:13:24Z` to `2026-08-30T21:17:56Z`, approximately `3 h 04 min 32 s`, and uploaded a replica artifact successfully. Replica A remained in progress at the last benchmark-time inspection.

The local test therefore does **not** demonstrate that the full coupling would finish faster than GitHub, because the local process is terminated by the 4 GiB memory ceiling before the expensive transform can complete.

## Capability conclusion

The local execution environment is computationally fast for dense numeric and DSIR map-preparation work, but its **4 GiB cgroup hard limit is insufficient for the exact NSIDE=4096 NaMaster workspace**.

The limiting resource is memory, not preliminary CPU speed.

Consequences:

1. local chat-runtime computation is useful for smaller numerical experiments, operator construction, diagnostics, synthetic QA and medium/heavy array work;
2. it cannot currently replace the GitHub/self-hosted authority route for the exact Article-3 `NSIDE=4096` NaMaster coupling;
3. a higher-memory execution environment could plausibly be worth qualifying prospectively because the observed local CPU/memory-array performance is strong, but this benchmark alone does not establish cross-route exact reproducibility or a speed advantage for NaMaster;
4. no scientific thresholds or authority rules should be changed because of this benchmark.

## Scientific accounting

- Article-3 readiness remains `52%`.
- No scientific PASS is claimed.
- Local NaMaster termination is `LOCAL_INFRASTRUCTURE_OOM_BENCHMARK_ONLY`, not a project scientific FAIL.
- No local result is admitted to Exp073AR.
- Exp073AQ remains the authoritative Wm_S1 gate until its frozen comparator reaches a valid terminal state.
