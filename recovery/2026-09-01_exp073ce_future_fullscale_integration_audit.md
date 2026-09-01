# Exp073CE -> future full-scale Wm_S2 integration audit

Date: 2026-09-01
Classification: repository-side infrastructure/methodology audit only; `+0/+0`; no Article-3 readiness credit.

## Coordination state before write

Immediately before this recovery write, GitHub Actions reported zero `in_progress` DSIR workflow runs and exactly one queued DSIR run: Exp073CA attempt3 run `33448843621`. That queued run is the locked self-hosted frontier and was not touched, rerun, cancelled, revived, or otherwise caused to execute. The home runner remains OFFLINE/LOCKED.

## Authority and sources

This audit binds the prospectively frozen Exp073CE memory-stable package against the actual frozen Exp073CA production wiring and the current production PCL implementation.

Relevant fixed authority:

- Exp073CA attempt3 run `33448843621` remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`, not a scientific FAIL.
- Exp073CE hosted run `33523714876`, job `99909080713`, immutable artifact `9806792097`, digest `sha256:b8403d7997b2f1705f1163c9882be04558fd7272904de00f5a29e6d4cdefc857`, is terminal `CE_Q1_MEMORY_STABLE_EXACT_EQUIVALENCE_PASS`, synthetic/nonclassifying `+0/+0`.
- Exp073BJ Track-A Wm_S1 PASS, Exp073AQ permanent historical scientific FAIL, Exp073BD no-downstream, and Exp073BV/BW/BZ prerequisite authority remain unchanged.
- Article-3 readiness remains Verified 52.0%, Draft/data 53.7%.

## Production semantic binding

The frozen production Wm path in `ci/exp073az_article3_low_memory_general_coupling_v0_1.py` currently constructs:

```python
a=lens_map(...)
b=source_map(...)
fa=nmt.NmtField(a,None,spin=0)
fb=nmt.NmtField(b,None,spin=2)
aa=fa.get_mask_alms()
ab=fb.get_mask_alms()
pcl=hp.alm2cl(aa,ab,lmax=fa.ainfo_mask.lmax)
```

A future memory-stable successor is semantically admissible only if it changes object lifetime/local storage, not these scientific definitions. The integration contract is therefore:

1. Lens and source input authority, hashes, occupancy validation, NSIDE=4096, HEALPix ordering, Wm_S2 task identity and map arithmetic remain unchanged.
2. Lens field construction remains exactly `nmt.NmtField(a, None, spin=0)` and source field construction remains exactly `nmt.NmtField(b, None, spin=2)`. No explicit `lmax`, `lmax_mask`, purification, beam, templates, smoothing, alternate weights or equivalent-looking options may be introduced.
3. Before releasing the lens field, capture `pcl_lmax = int(fa.ainfo_mask.lmax)` and fail closed unless the production receipt is exactly `12287`. A literal replacement that bypasses the runtime receipt is forbidden.
4. The first mask ALM may be converted only to contiguous canonical `<c16>` storage for exact identity, spilled to local scratch using same-filesystem temp -> flush/fsync -> atomic `os.replace`, and verified by exact file size, shape, dtype and SHA-256 before the in-memory first ALM, lens field and lens map are released.
5. Only after that release and `gc.collect()` may the source map/field/second ALM be constructed.
6. The first ALM must be reopened read-only through mmap and revalidated byte-for-byte against the stored receipt before use.
7. Final arithmetic remains `hp.alm2cl(first_mask_alm, second_mask_alm, lmax=pcl_lmax)` with no tolerance/ULP/rounding/averaging/smoothing/majority/preferred-replica rescue.
8. Final PCL remains contiguous canonical `<f8>` shape `(12288,)`, finite, and enters the existing compact stage unchanged.

Exp073CE already tested the production-semantic lifetime/spill transformation at prospectively frozen small geometries and obtained exact PCL equality plus exact canonical SHA identity. This audit finds no additional scientific-semantic transformation needed for the future full-scale implementation.

## Checkpoint, comparator and finalizer isolation

The Exp073CA workflow places PCL construction before compilation, checkpoint preflight/restore, heavy 39-band compact streaming, compact replica comparison and finalization. Therefore the memory-stable change can remain confined to the PCL implementation boundary.

The future successor must leave unchanged:

- frozen compiler flags and compact streaming helpers;
- mandatory checkpoint-boundary exact preflight;
- durable remote checkpoint branches and checkpoint authority;
- 39-band compact arithmetic and checkpoint receipts;
- exact A/B compact comparator (`np.array_equal` plus canonical SHA identity; no rescue);
- finalizer arithmetic and downstream authority rules.

Local ALM spill scratch is disposable PCL-stage infrastructure state only. It must never be uploaded to, restored from, or interpreted as scientific checkpoint authority. Cleanup occurs in `finally` and may delete only the replica-specific local spill directory.

## Workflow-trigger isolation

The current Exp073CA attempt3 workflow is push-filtered only on `ci/exp073ca_attempt3_article3_wm_s2_checkpoint_streaming_track_a_v0_1.trigger`. Recovery/documentation commits therefore do not satisfy its trigger path. This audit does not modify that trigger and does not revive queued replica B.

## Thread and heartbeat binding: important infrastructure constraint

The frozen Exp073CA attempt3 workflow currently sets `OMP_NUM_THREADS='8'`, all listed BLAS-style thread pools to `1`, and the PCL/compact heartbeat reports `threads=8`. The Exp073CE preregistration explicitly requires the thread policy to remain unchanged.

Therefore a future scientific successor may NOT silently lower OMP threads as an ad-hoc memory rescue. If thread-count modification is ever desired, it requires a separate prospective infrastructure/methodology decision and exact-equivalence evidence before it can replace the frozen policy. For the currently bound successor, `threads=8` remains part of the preserved execution contract.

Heartbeat remains side-band infrastructure only, at <=60 s, with named stage, persisted completed/total when known, elapsed, ETA when estimable, threads, progress bar and `intra_unit_progress=unknown` when exact intra-unit fraction is unknowable. It must not read or mutate scientific arrays.

## Full-scale memory/infrastructure boundary

The exact semantic integration is now sufficiently specified, but full-scale memory safety is not proven. Current evidence remains:

- one full-scale `<c16>` mask ALM: 1,208,057,856 bytes (~1.12509 GiB);
- require >=2.5 GiB free local spill space per active replica;
- future constrained-host matrix concurrency must remain `max-parallel: 1`;
- the 6 GiB WSL cap is NOT certified safe because full-scale NaMaster/healpy SHT workspace and final mmap residency have not been measured under the production geometry/thread policy.

For the user's ~7.7 GB physical-RAM machine, tomorrow's repair should treat the software lifetime/spill change as the primary mitigation, not assume that raising the WSL cap is safe. The first unlocked full-scale attempt should retain fail-closed disk preflight, `/usr/bin/time -v`, the frozen thread policy, one replica at a time and <=60 s heartbeat. Any WSL/host tuning remains a separate user-controlled action and is not applied by this audit.

## Audit result

**PASS_INFRASTRUCTURE_SEMANTIC_INTEGRATION_SPECIFIED_EXP073CE_TO_FUTURE_FULLSCALE**, `+0/+0`.

No unresolved hosted-only scientific-semantic gap was found that justifies manufacturing another numerical run tonight. The remaining uncertainty is genuinely full-scale infrastructure behavior (SHT workspace/RSS and host stability), which cannot classify Wm_S2 without a fresh real-survey execution.

## Exact next permitted gate

While the home runner remains locked, the next permitted work is read-only/repository-side preparation of the fresh full-scale successor workflow/helper/binding **without triggering it**, including fail-closed local-spill preflight and preservation of the existing scientific/checkpoint/comparator/finalizer contract.

The next actual scientific frontier remains a **fresh full-scale Wm_S2 successor** only after the user explicitly re-enables the home runner. Do not rerun Exp073CA attempt3 and do not reuse stale queued replica B as scientific authority.