# Exp073CD-supported production spill/reload integration audit

**Date:** 2026-09-01  
**Scope:** repository-side hosted/read-only methodology and infrastructure audit; no scientific gate; Article-3 readiness delta `+0/+0`.

## Authority and coordination

Repository state and immutable Actions artifacts remain authoritative. Exp073CA attempt3 run `33448843621` remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`; replica A job `99673921219` is terminal infrastructure failure and replica B job `99673921530` remains queued self-hosted. Home runner remains **OFFLINE/LOCKED** and was not touched. At the pre-write coordination check there was exactly one queued DSIR run (Exp073CA attempt3) and zero `in_progress` DSIR runs.

Preserved authority: Exp073BJ exact Track-A Wm_S1 PASS; Exp073AQ permanent historical exact-repeatability scientific FAIL; Exp073BD provisional/incomplete and forbidden downstream; Exp073BV/BW/BZ PASS; Exp073CC `CC_Q1_EXACT_EQUIVALENCE_PASS`; Exp073CD `CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS`.

## Production insertion points

Current production PCL path is `ci/exp073az_article3_low_memory_general_coupling_v0_1.py::task_pcl`. For `Wm` it currently executes, in order:

`a=lens_map -> b=source_map -> fa=NmtField(a) -> fb=NmtField(b) -> aa=fa.get_mask_alms() -> ab=fb.get_mask_alms() -> hp.alm2cl(aa,ab)`.

A future prospectively frozen memory-stable successor may change **object lifetime and storage only**, not scientific arithmetic, task parsing, mask construction, NaMaster/healpy versions, spins, `lmax`, dtype/order/indexing, final `hp.alm2cl`, PCL canonicalization, comparator, thresholds, or thread policy.

Required Wm sequence for that successor:

1. `a = lens_map(...)`.
2. `fa = nmt.NmtField(a,None,spin=0)` using the same production defaults as the frozen path.
3. `del a; gc.collect()`.
4. `aa = np.ascontiguousarray(fa.get_mask_alms(), dtype='<c16')`.
5. `del fa; gc.collect()`.
6. Compute and record canonical `<c16>` shape, dtype and SHA-256 of `aa`.
7. Persist `aa` to a run/replica-unique local temporary file on the same filesystem as the intended final spill file; use `np.save(..., allow_pickle=False)` so serialization semantics remain those already exact-tested by Exp073CD.
8. Flush and `fsync` the temporary file, atomically `os.replace(tmp, final)`, then `fsync` the containing directory where supported.
9. Reopen the final file with `np.load(..., mmap_mode='r', allow_pickle=False)` and require exact shape, dtype string and canonical `<c16>` SHA equality to the in-memory pre-spill receipt. If any identity check fails, classify infrastructure incomplete/failure according to the future preregistration; never continue to science.
10. Close the verification mmap, `del aa; gc.collect()` **before constructing the source mask or second NmtField**. This is the memory-critical boundary.
11. `b = source_map(...)`; `fb = nmt.NmtField(b,None,spin=2)` with unchanged production semantics.
12. `del b; gc.collect()`.
13. `ab = fb.get_mask_alms()`; then `del fb; gc.collect()` so the second-SHT field/mask can be released before final cross-spectrum.
14. Reopen the first ALM read-only with `np.load(final, mmap_mode='r', allow_pickle=False)` and re-require exact shape/dtype/SHA identity.
15. Execute the unchanged scientific operation `pcl = hp.alm2cl(aa_reload, ab, lmax=<same production lmax>)`.
16. Canonicalize the PCL exactly as production already does: contiguous `<f8>`, shape `(12288,)`, all finite. No tolerance/ULP/rounding/averaging/smoothing/majority/preferred-replica rescue.
17. Close/delete mmap and spill file only after the PCL has been durably written and its receipt finalized.

## Full-scale storage budget

For DES `NSIDE=4096`, `lmax=12287`, a triangular complex128 ALM contains `12288*12289/2 = 75,503,616` values, or `1,208,057,856` payload bytes = about **1.12509 GiB** before the small `.npy` header.

A future runner preflight should therefore require at least **2.5 GiB free local space per active replica** in the spill filesystem. This is deliberately conservative: it covers one ~1.125 GiB final spill plus a same-filesystem temporary/verification margin and metadata. The future workflow remains matrix `max-parallel: 1` unless separately preregistered, so two replicas must not simultaneously consume this budget on the home machine.

Spill paths must be run/replica unique under a runner-temp directory, never repository paths and never checkpoint branches. Spill bytes are infrastructure scratch, not scientific authority artifacts.

## Memory interpretation boundary

Exp073CD proved exact serialization/reload equivalence at frozen hosted geometries; it did **not** prove full-scale RSS safety. The spill design chiefly removes the retained first ALM from the **second SHT phase**, where workspace pressure is expected to be largest. It does not guarantee low RSS during the final `hp.alm2cl`: the read-only mmap must be traversed and may become resident as file-backed pages. Therefore a future full-scale successor must measure `/usr/bin/time -v Maximum resident set size` around the PCL stage and preserve it as infrastructure diagnostics, not as a scientific acceptance threshold.

The current deterministic second-SHT baseline estimate remains approximately **2.62509 GiB plus SHT workspace/process overhead** under the spill design. This is an engineering budget, not proof that the present 6 GiB WSL cap is sufficient.

## Atomicity, failure and cleanup semantics

- Never overwrite an existing spill file in place. Write a unique temp file, `fsync`, atomic rename, then verify.
- A spill is valid only after exact canonical `<c16>` shape/dtype/SHA verification. File existence alone is not validity.
- On process restart, a leftover spill may be reused only if a future preregistration binds it to the exact task, replica, source commit/input lineage, expected shape/dtype and SHA receipt. Otherwise delete/recompute; never infer authority from filename.
- A partial temp file is always disposable infrastructure state.
- Spill scratch must not be pushed to Git, uploaded as scientific authority, or used to replace the existing remote band-checkpoint design.
- Existing remote checkpoint semantics begin after PCL construction in Exp073CA; therefore ALM spill state should remain local PCL-stage scratch. A failed PCL stage should restart PCL deterministically rather than promoting the spill into the 39-band scientific checkpoint namespace.
- Cleanup must be `try/finally`-style where practical: close mmap handles first, then unlink temp/final scratch after successful PCL persistence; on failure preserve only small JSON/log diagnostics, not multi-GiB spill payloads.

## Heartbeat contract for a future heavy successor

The <=60 s heartbeat rule remains mandatory and must not touch scientific arithmetic. PCL heartbeat stages should be named at least:

`lens_mask_build`, `lens_field_sht`, `alm_spill_verify`, `source_mask_build`, `source_field_sht`, `alm_reload_verify`, `alm2cl`, `pcl_persist`.

Every heartbeat must report stage, elapsed, threads, progress bar, persisted completed/total when meaningful, ETA when estimable, and `intra_unit_progress=unknown` when the current NaMaster/healpy transform exposes no trustworthy fractional progress. Heartbeat state must not alter mask arrays, ALMs, PCL arrays or numerical scheduling.

## Result of this audit

The production insertion/deletion points, spill size, atomicity, exact verification, mmap boundary, cleanup and checkpoint separation are now concretely specified. No hosted computation was required and no workflow was triggered.

**Classification:** methodology/infrastructure audit only, `+0/+0`.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**, unchanged.  
**Home runner:** **OFFLINE/LOCKED**.

## Exact next permitted gate

While the home runner remains locked, the next scientifically permitted work is a **prospective successor design audit/pre-registration** that binds the above production-lifetime changes to the frozen Exp073CA scientific contract and proves there are no hidden changes to inputs, `NmtField` parameters, `lmax`, `hp.alm2cl`, PCL output canonicalization, compact streaming, comparator, checkpoint authority or thread policy. If that audit finds no unresolved semantic delta, prepare—but do not trigger—the future self-hosted successor. Full-scale execution remains forbidden until the user explicitly re-enables the home runner.
