# Exp073CL — Wm_S3 hosted-mask eight-band direct-8 resource qualification v0.1

**Date:** 2026-09-02  
**Classification:** prospective infrastructure/resource qualification, `+0/+0`  
**Task:** `Wm_S3` (source tomographic bin S3; not spin-3)

## Motivation

Exp073CK v0.1 ended before any scientific/numerical comparison because the DES public server delivered the exact lens mask at only tens of KiB/s, repeatedly truncated HTTP responses, and the manually started home runner was stopped. Its one-band direct-8 benchmark also could not qualify 8-core utilization because the frozen C helper parallelizes across bands.

This successor changes only transport/resource qualification. It does not alter the frozen Wm scientific arithmetic, historical Exp073AA/AF authority, or Article-3 readiness.

## Frozen scientific/resource contract

- DES `NSIDE=4096`, RING/C.
- `ell=0..12287`, `L=12288`.
- 39 canonical frozen bands and exact frozen band edges.
- Wm selected component `TE <- TE`.
- source tomographic bin **S3** (`source_bin=3`).
- coupling signature **(0,2,0,2)**.
- canonical little-endian `<f8` arrays.
- no effective-ell/z/k or fiducial-P shortcut.
- exact equality only; no tolerance/ULP/rounding/smoothing/averaging rescue.

## Transport change

The exact DES Y1 lens mask is downloaded and SHA/size verified on a GitHub-hosted `ubuntu-24.04` staging job, then uploaded as an Actions artifact. The self-hosted home job MUST obtain the mask only from that staged GitHub artifact and independently verify:

- bytes = `104595840`;
- SHA256 = `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

Hosted download must use HTTP/1.1 plus finite connect/max/low-speed timeouts and retries. A hosted download failure is infrastructure incomplete, not a scientific FAIL.

## Eight-band direct-8 benchmark

Use exactly frozen bands **0..7** (`ib_lo=0`, `ib_hi=8`). These bands have nearly balanced widths and permit the existing OpenMP `omp for` architecture to expose eight independent work units simultaneously.

On one fresh real full-L Wm_S3 PCL:

1. compute the full 8-row range with `nthreads=1` as canonical reference;
2. compute the exact same range with `nthreads=8` as target;
3. require `np.array_equal(reference,target)` and identical canonical SHA256;
4. require all values finite;
5. require no increase in used swap during the 8-thread target;
6. record process CPU seconds and target wall seconds. Define `effective_cpu_cores = process_cpu_seconds / wall_seconds` and `cpu_fraction_of_8 = effective_cpu_cores / 8`.

The requested CPU-utilization qualification requires `cpu_fraction_of_8 >= 0.90` for the target interval. If exact equality passes but CPU fraction is below 0.90, classify the resource architecture as **CPU_TARGET_NOT_MET**, not as a scientific Wm failure. No post-hoc lowering of the 0.90 threshold is allowed for this version.

## Decision tree

- hosted mask staging/network failure -> `INFRASTRUCTURE_INCOMPLETE_EXP073CL_MASK_STAGE`, `+0/+0`;
- self-hosted setup/PCL failure before comparator -> infrastructure incomplete unless an explicit frozen arithmetic assertion fails;
- exact 1-vs-8 mismatch -> `FAIL_EXP073CL_WM_S3_EIGHTBAND_DIRECT8_EXACT_EQUIVALENCE_V0_1`, resource/numerical FAIL, `+0/+0` readiness;
- exact equality + safe swap but CPU fraction <0.90 -> `FAIL_EXP073CL_WM_S3_DIRECT8_CPU_TARGET_V0_1`, performance/resource FAIL, `+0/+0` readiness;
- exact equality + safe swap + CPU fraction >=0.90 -> `PASS_EXP073CL_WM_S3_EIGHTBAND_DIRECT8_RESOURCE_V0_1`, resource PASS, `+0/+0` readiness.

Only the PASS outcome may authorize `threads=8, chunk_bands=8` for a NEW prospectively preregistered full Wm_S3 A/B successor. It does not itself create Wm_S3 angular scientific authority.

At most one heavy DSIR self-hosted job may own `DSIR-HOME-PC` at a time.
