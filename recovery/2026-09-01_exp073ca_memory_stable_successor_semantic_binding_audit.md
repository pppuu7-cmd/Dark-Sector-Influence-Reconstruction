# Exp073CA memory-stable successor semantic-binding audit

**Date:** 2026-09-01  
**Scope:** repository-side prospective design/preregistration audit only; no workflow trigger; no scientific gate; Article-3 readiness delta `+0/+0`.

## Authority and coordination at audit start

Repository state and immutable GitHub Actions artifacts remain authoritative. Before this write, GitHub Actions reported exactly one queued DSIR run, Exp073CA attempt3 run `33448843621`, and zero `in_progress` DSIR runs. Replica A job `99673921219` remains terminal infrastructure failure during fresh Wm_S2 PCL; replica B job `99673921530` remains queued self-hosted and is not to be revived while the overnight lock is active.

Exp073CA attempt3 remains classified only as `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`. Compile, mandatory checkpoint preflight, checkpoint restore, heavy 39-band streaming, exact compact comparator and finalizer were not reached by replica A.

Preserved authority: Exp073BJ exact Track-A Wm_S1 PASS; Exp073AQ permanent historical exact-repeatability scientific FAIL; Exp073BD provisional/incomplete and forbidden downstream; Exp073BV source-lineage PASS; Exp073BW exact streaming-equivalence PASS; Exp073BZ checkpoint/failover PASS; Exp073CC corrected-lifetime exact-equivalence PASS; Exp073CD ALM spill/reload exact-equivalence PASS.

Home runner remains **OFFLINE/LOCKED**. No self-hosted run, rerun, trigger or WSL/computer change is authorized by this document.

## Frozen predecessor scientific contract

The future memory-stable successor must inherit the Exp073CA preregistration unchanged except for explicitly enumerated object-lifetime/storage engineering. In particular it must preserve:

- task `Wm_S2`, signature `(0,2,0,2)`, selected response `TE <- TE`;
- DES Y1 source-mask authorities and DES Y1 redMaGiC lens mask `104595840` bytes, SHA-256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- `NSIDE=4096`, RING, true ell `0..12287`, 39 frozen bands and the exact frozen edges;
- PyMaster/NaMaster v2.7 lineage and the same production `NmtField` constructor semantics;
- two fresh independent replicas A/B and no cross-replica scientific payload reuse;
- same compact streaming arithmetic, complete-band checkpoint boundary, chunk size at most 4 and exact checkpoint validation;
- same compiler flags and no fast-math/reassociation/FMA rescue;
- same exact compact and finalizer comparators (`np.array_equal` plus canonical SHA-256), with no tolerance/ULP/rounding/averaging/smoothing/majority/preferred-replica rescue;
- same finalizer arithmetic `W = numpy.linalg.solve(K,A)` with no pseudoinverse/regularization/jitter/clipping/smoothing/alternate-solver rescue;
- same thread policy: `OMP_NUM_THREADS=8`, BLAS-family threads 1, `OMP_DYNAMIC=FALSE`;
- same remote checkpoint authority beginning only after PCL construction;
- same authority tokens and readiness firewall.

## Semantic comparison: frozen production PCL vs permitted memory-only successor

Frozen production `ci/exp073az_article3_low_memory_general_coupling_v0_1.py::task_pcl` currently performs for Wm:

`a=lens_map -> b=source_map -> fa=NmtField(a,None,spin=0) -> fb=NmtField(b,None,spin=2) -> aa=fa.get_mask_alms() -> ab=fb.get_mask_alms() -> hp.alm2cl(aa,ab,lmax=fa.ainfo_mask.lmax)`.

A future successor is permitted to change only lifetime/storage ordering:

1. Build the same `a = lens_map(...)` from the same bound file bytes.
2. Build `fa = nmt.NmtField(a, None, spin=0)` with no additional constructor argument unless a separately frozen audit proves it byte-equivalent.
3. **Before deleting `fa`, capture `pcl_lmax = int(fa.ainfo_mask.lmax)` and fail closed unless `pcl_lmax == 12287`.** This is required because the frozen production call derives the final `hp.alm2cl` lmax from `fa.ainfo_mask.lmax`; silently replacing that derivation by an assumed constant would be an unnecessary hidden semantic delta.
4. Delete caller `a`; obtain first mask ALM from the same `fa.get_mask_alms()` call.
5. Canonicalize only for spill identity as contiguous `<c16>`; record exact shape/dtype/SHA. Exp073CD supports exact save/reload semantics at frozen hosted geometries, but this remains infrastructure evidence, not real-survey gate closure.
6. Atomically spill/verify the first ALM and release `fa` and the in-memory first ALM before source-mask construction.
7. Build the same `b = source_map(...)` from the same R1 authority and construct `fb = nmt.NmtField(b, None, spin=2)` with unchanged defaults.
8. Obtain `ab = fb.get_mask_alms()` with no scientific transformation, then release `fb`.
9. Reopen the first ALM read-only, require exact shape/dtype/SHA identity, and call the unchanged operation `hp.alm2cl(aa_reload, ab, lmax=pcl_lmax)`.
10. Canonicalize final PCL exactly as the frozen production helper already does: contiguous `<f8>`, shape `(12288,)`, all finite.

No mask values, map construction, spin, `NmtField` defaults, SHT definition, ALM values, `alm2cl` algorithm, lmax, output dtype/order or downstream arithmetic may change.

## Hidden-delta audit findings

### 1. `lmax` derivation is a real semantic guardrail

The current production code passes `lmax=fa.ainfo_mask.lmax`, not a literal constant. Therefore a memory repair that deletes `fa` before `alm2cl` must first capture that exact runtime integer and assert it equals the frozen expected value `12287`. This preserves both the dynamic production derivation and the frozen geometry. Using a literal without this receipt is not preferred.

### 2. `NmtField` constructor defaults must remain defaults

The memory repair must not opportunistically add `lmax`, `lmax_mask`, purification, beam, templates or other `NmtField` arguments. Even an argument believed numerically equivalent would widen the scientific delta. The successor should construct the fields with the same positional/keyword semantics as the current production path and only alter when objects are released.

### 3. First-ALM canonicalization is storage identity, not a new numerical operation

The spill representation may be canonical contiguous `<c16>` solely to define exact serialization/SHA identity. Exp073CD established exact PCL equality for this spill/reload operation on frozen hosted geometries. The successor preregistration must still require exact preflight equivalence and may never use approximate equality to justify the storage conversion.

### 4. mmap must be read-only and scientifically inert

The reloaded first ALM is an immutable input to the same `hp.alm2cl`. The mmap path may change paging/RSS but may not change element order, dtype, shape or bytes. Exact SHA verification immediately before `alm2cl` is mandatory.

### 5. PCL scratch must not become checkpoint authority

ALM spill files remain local disposable infrastructure scratch. They are outside the existing remote complete-band checkpoint namespace. A PCL-stage restart recomputes PCL unless a future preregistration separately binds a spill to exact run/replica/input lineage and receipt; no such reuse is authorized here.

### 6. Compact streaming and finalizer need no scientific modification

The memory failure occurred before compile/preflight/heavy compact work. The Exp073BW/BZ-supported compact/checkpoint path can remain byte-for-byte frozen. A successor should therefore modify the PCL implementation/workflow wiring only as required for the memory-lifetime repair, leaving range helper, checkpoint driver, checkpoint utilities, compiler flags, comparator and finalizer lineages frozen.

### 7. Heartbeat remains side-band only

The <=60 s heartbeat may report named PCL stages (`lens_mask_build`, `lens_field_sht`, `alm_spill_verify`, `source_mask_build`, `source_field_sht`, `alm_reload_verify`, `alm2cl`, `pcl_persist`), elapsed time, threads, durable completed/total where meaningful, ETA when estimable, and `intra_unit_progress=unknown` when an SHT fraction is unavailable. It must not inspect/mutate mask or ALM arrays or alter scheduling/arithmetic.

## Prospective successor freeze requirements

A future self-hosted Exp073CA infrastructure successor must be a new attempt/successor, not a rerun or mutation of attempt3. Before any trigger, repository history should freeze in separate commits:

1. a successor preregistration stating that the scientific contract is unchanged and enumerating the lifetime/storage-only delta;
2. a new PCL helper or narrowly scoped successor helper containing the sequential/spill implementation, including dynamic `pcl_lmax` capture and fail-closed assertion;
3. a nonclassifying exact-equivalence selftest/hosted QA binding original/corrected-sequential/spill paths at tractable geometry with `np.array_equal` + canonical SHA only;
4. workflow wiring with the same raw inputs, NaMaster 2.7 provisioning, thread policy, compact/checkpoint helpers, exact comparators and finalizer;
5. a binding JSON containing all predecessor scientific lineages plus Exp073CC/Exp073CD immutable run/artifact/digest provenance and the exact new helper/workflow commits;
6. a separate trigger commit only after the user explicitly removes the home-runner lock.

The successor must not consume provisional Exp073BD output, old incomplete CA PCL scratch, or any self-hosted leftover spill lacking the future exact binding receipt.

## Tomorrow home-runner memory-stability plan — design only, do not apply overnight

Given approximately 7.7 GiB physical host RAM, current WSL `memory=6GB`, `processors=10`, `swap=8GB`, and the observed attempt3 infrastructure termination under severe memory pressure:

- Do **not** treat 6 GiB as proven safe even with spill; full-scale SHT workspace remains unmeasured.
- First preserve the software memory repair because it reduces deterministic resident payload independently of WSL tuning.
- Before a future full-scale trigger, verify at least 2.5 GiB free local spill filesystem space per active replica and keep matrix `max-parallel: 1`.
- Keep the scientific thread policy at 8 because it is frozen; do not change thread count merely to rescue memory without a new prospective contract. If infrastructure testing later shows thread-dependent workspace is decisive, preregister that as a separate infrastructure successor and retain exact-output requirements.
- At the user's return, inspect Windows host available RAM and WSL configuration before choosing any cap change. With only ~7.7 GiB physical RAM, setting WSL near total physical RAM can starve Windows and should not be assumed safe. Any cap/swap adjustment must be deliberate and external to scientific acceptance.
- Future PCL execution should retain `/usr/bin/time -v` Maximum resident set size and heartbeat diagnostics. RSS is infrastructure evidence only, never a scientific threshold.
- If the memory-stable successor still terminates before a complete PCL, classify infrastructure incomplete `+0/+0`; do not reduce scientific criteria or reinterpret a partial result.

## Audit conclusion

No unresolved scientific-semantic delta is required by the proposed memory repair **provided all guardrails above are frozen prospectively**, especially runtime capture/assertion of `fa.ainfo_mask.lmax`, unchanged `NmtField` constructor semantics, exact ALM spill identity, unchanged `hp.alm2cl`, and an untouched compact/checkpoint/finalizer path.

This audit authorizes preparation of a future successor preregistration/helper/workflow while the home runner is locked, but **does not authorize triggering any self-hosted job**.

**Classification:** methodology/infrastructure design audit only, `+0/+0`.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**, unchanged.  
**Home runner:** **OFFLINE/LOCKED**.

## Exact next permitted gate

While the home runner remains locked, the next permitted work is to prepare a **prospectively frozen, hosted-testable memory-stable successor implementation package** (new preregistration + narrowly scoped PCL helper + hosted exact-equivalence/selftest + workflow/binding skeleton) without creating or triggering any `[self-hosted, Linux, X64]` run. The package must remain untriggered for full-scale Wm_S2 until the user explicitly re-enables the home runner.
