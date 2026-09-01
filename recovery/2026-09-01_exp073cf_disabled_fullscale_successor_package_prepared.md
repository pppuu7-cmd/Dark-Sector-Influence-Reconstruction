# Exp073CF disabled full-scale memory-stable Wm_S2 successor package prepared

Date: 2026-09-01
Classification: repository-side infrastructure/methodology preparation only; `+0/+0`; no Article-3 readiness credit.

## Coordination state

Before every repository write in this preparation sequence, GitHub Actions was rechecked. The state remained zero `in_progress` DSIR runs and exactly one queued DSIR run: Exp073CA attempt3 run `33448843621`. The queued self-hosted replica B was not touched, rerun, cancelled, revived or otherwise caused to execute. Home runner remains OFFLINE/LOCKED.

## Package lineage

- preregistration commit: `e0c92ebaba576a5aa5dfd06d1d972bfa3b025d36`;
- first helper draft: `5c349386981776d2c878c3c0d75f31fc42b51ec8`;
- corrected no-large-copy helper commit: `5423976c09d5ee338d1a7894ce143faf1bb88225`;
- disabled main workflow specification: `d0a52ef4669c177732935bff28be7282208c4fcb`;
- disabled comparator/finalizer authority-tail specification: `9654ca78514495da5c788ca0418ffe3eca9f2ad8`;
- preparation binding commit: `f8da5f35d2ead65b9db24ee19649846243a7f606`.

No file was created under `.github/workflows`, no Exp073CF trigger file was created, and no self-hosted workflow/run was activated.

## Important memory finding fixed before binding

The first helper draft used `np.ascontiguousarray(mm, dtype='<c16').tobytes()` to compute the reloaded mmap SHA. At full scale this could materialize an avoidable ~1.12509 GiB transient copy, defeating the purpose of the memory-stable design. This was caught before the package binding and corrected.

The frozen helper now:

- hashes the in-memory canonical first ALM via a buffer view (`memoryview(...).cast('B')`) without a `tobytes()` copy;
- verifies temp/final/reloaded spill identity by streaming SHA-256 directly from the spill file in 8 MiB chunks;
- opens the first ALM read-only with `np.memmap` and does not materialize a separate full-array copy solely for verification;
- preserves the unchanged scientific call `hp.alm2cl(mm, second_alm, lmax=pcl_lmax)`.

This is an infrastructure memory correction only and does not alter scientific arithmetic.

## Frozen implementation content

The helper preserves production-semantic constructors `nmt.NmtField(a, None, spin=0)` and `nmt.NmtField(b, None, spin=2)`, captures runtime `pcl_lmax=int(fa.ainfo_mask.lmax)` and fails closed unless it is `12287`, requires at least 2.5 GiB free local spill space, performs same-filesystem temp -> flush/fsync -> atomic `os.replace`, exact file-size/SHA verification, lens-side release + `gc.collect()`, source-side construction, read-only mmap reload, repeat SHA/shape/dtype checks, unchanged `hp.alm2cl`, and canonical finite `<f8 [12288]>` output.

The disabled workflow specification preserves OMP threads=8, BLAS-style pools=1, `max-parallel: 1`, <=60 s heartbeat, frozen compiler flags, mandatory checkpoint preflight, fresh Exp073CF checkpoint namespaces, and the existing streaming helper lineage. The companion disabled authority tail preserves exact compact/final comparator semantics with no tolerance/ULP/rounding/majority/preferred-replica rescue.

## Overnight safety boundary

The package is deliberately non-executable. It is outside `.github/workflows`; the future isolated trigger path does not exist. Activation is forbidden until the user explicitly re-enables the home runner.

After explicit re-enable, the required order is:

1. inspect all queued/in_progress DSIR runs and resolve the stale Exp073CA queued state without using it as scientific authority;
2. audit the disabled Exp073CF specifications against current repository state;
3. create a separate prospective activation binding pinning the actual activated workflow commit and new trigger binding;
4. only then create/touch the isolated Exp073CF trigger and run fresh replicas one at a time;
5. retain fail-closed spill-space preflight, `/usr/bin/time -v`, frozen thread policy and heartbeat.

The current 6 GiB WSL cap remains uncertified because full-scale SHT workspace and mmap residency are still empirically unknown.

## Preserved authority and readiness

Exp073BJ PASS, Exp073AQ permanent scientific FAIL, Exp073BD no-downstream, Exp073BV/BW/BZ PASS, Exp073CC/CD/CE nonclassifying exact-equivalence PASSes, and Exp073CA infrastructure-incomplete status all remain unchanged.

Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**.

## Exact next permitted gate

While home runner remains locked, the next permitted work is a **repository-side static audit of the disabled Exp073CF package**, focusing on activation-time binding completeness, output/status-token compatibility with the frozen Exp073CA streaming driver, cleanup/failure behavior and ensuring no hidden memory copies remain. No self-hosted activation or trigger is permitted.
