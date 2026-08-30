# DSIR local compute benchmark — 2026-08-31

**Classification:** local/non-hosted infrastructure benchmark only. Not scientific authority. Not an angular authority. `+0` readiness.

## Environment

- 5 x Intel Xeon Platinum 8370C vCPU @ 2.80 GHz exposed to the local execution container.
- ~5.9 GiB RAM, no swap.
- ~38 GiB free local disk at benchmark start.
- Python 3.13.5.
- NumPy 2.3.5, SciPy 1.17.0.
- No local `healpy`, `pymaster`, or `astropy` initially available.
- Frozen DSIR single-thread environment variables were applied for the benchmarks where relevant.

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

Therefore the local environment can physically hold and touch at least two complete NSIDE=4096 float64 maps without OOM. This does not prove that NaMaster workspace internals fit within the ~5.9 GiB memory limit.

## Single-thread transform benchmark

Executed SciPy `rfft2` on an `8192 x 8192` float64 array with `workers=1` and the DSIR single-thread environment controls.

- input size: `0.5 GiB`;
- output size: ~`0.5001 GiB` complex;
- transform time: `1.736 s`;
- whole-process wall clock including construction/cleanup: `7.89 s`;
- peak RSS: ~`1172152 KiB`.

This indicates strong local single-thread/memory-transform performance, but FFT2 is not a substitute for HEALPix spherical harmonic transforms or NaMaster coupling-matrix construction.

## Comparison point from GitHub hosted authority route

Historical Exp073X2 primary-P Wm_S0 exact replica computation on `ubuntu-24.04` required approximately `1 h 56 min 32 s` for each replica compute step.

Current Exp073AQ Wm_S1 replica B completed its exact compute step from `2026-08-30T18:13:24Z` to `2026-08-30T21:17:56Z`, approximately `3 h 04 min 32 s`, and uploaded a replica artifact successfully. Replica A remained in progress when this benchmark record was written.

## Limitation blocking a true local NaMaster timing

The local execution image does not contain NaMaster/PyMaster 2.7, Healpy, GSL development headers, or an outbound package-install network path. Therefore the actual `NmtWorkspace.compute_coupling_matrix` bottleneck has not yet been timed locally.

A portable NaMaster 2.7 environment export may be used only for a **non-authoritative local benchmark** unless a separately preregistered execution-authority succession is later qualified. Any local benchmark result remains `+0` readiness and cannot replace the hosted exact-twin route.

## Scientific accounting

- Article-3 readiness remains `52%`.
- No scientific PASS is claimed.
- No local result is admitted to Exp073AR.
- Exp073AQ remains the authoritative active Wm_S1 gate until its frozen comparator reaches a valid terminal state.
