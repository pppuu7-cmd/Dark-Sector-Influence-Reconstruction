# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-01_exp073cf_disabled_fullscale_successor_package_prepared.md`
2. `preregistration/2026-09-01_exp073cf_fullscale_memory_stable_wm_s2_successor_v0_1.md`
3. `recovery/2026-09-01_exp073ce_future_fullscale_integration_audit.md`
4. `recovery/2026-09-01_exp073ce_terminal.md`
5. `preregistration/2026-09-01_exp073ce_memory_stable_wm_s2_successor_package_v0_1.md`
6. `recovery/2026-09-01_exp073ca_memory_stable_successor_semantic_binding_audit.md`
7. `recovery/2026-09-01_exp073cd_production_spill_integration_audit.md`
8. `recovery/2026-09-01_exp073cd_q1_spill_reload_exact_equivalence_pass.md`
9. `recovery/2026-09-01_exp073cc_fullscale_memory_budget_audit.md`
10. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
11. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
12. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
13. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
14. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
15. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current overnight frontier

- Home runner is **OFFLINE/LOCKED** until the user explicitly re-enables it.
- Exp073CA attempt3 run `33448843621`: replica A job `99673921219` terminal infrastructure failure during fresh Wm_S2 PCL; replica B job `99673921530` remains queued self-hosted and must not be revived overnight.
- Exp073CA classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`, not scientific FAIL.
- Latest coordination check immediately before this sync found exactly one queued DSIR run (Exp073CA attempt3) and zero `in_progress` DSIR runs.

## Exp073CF disabled successor preparation

Exp073CF is now prospectively prepared but deliberately **non-executable** overnight. No file was created under `.github/workflows`, no Exp073CF trigger exists, and no self-hosted run was started.

Frozen preparation lineage:

- preregistration `e0c92ebaba576a5aa5dfd06d1d972bfa3b025d36`;
- corrected memory-stable PCL helper `5423976c09d5ee338d1a7894ce143faf1bb88225`;
- disabled main workflow specification `d0a52ef4669c177732935bff28be7282208c4fcb`;
- disabled exact comparator/finalizer authority tail `9654ca78514495da5c788ca0418ffe3eca9f2ad8`;
- preparation binding `f8da5f35d2ead65b9db24ee19649846243a7f606`;
- recovery record `3c0b8cfcfe8cafc393165f60df134c76d5d77616`.

A memory regression was caught before binding: the first helper draft would have hashed the reloaded mmap through `np.ascontiguousarray(...).tobytes()`, potentially materializing another ~1.12509 GiB copy. The bound helper instead hashes the canonical in-memory ALM through a buffer view and verifies temp/final/reloaded spill files with streaming 8 MiB SHA-256 reads. It therefore does not intentionally create a full-size verification copy.

The helper preserves production semantics: exact lens/source authority, `nmt.NmtField(a,None,spin=0)`, `nmt.NmtField(b,None,spin=2)`, runtime `pcl_lmax=int(fa.ainfo_mask.lmax)` with full-scale fail-closed receipt `12287`, exact canonical `<c16>` spill, same-filesystem temp -> flush/fsync -> atomic `os.replace`, read-only mmap reload, unchanged `hp.alm2cl(...,lmax=pcl_lmax)`, and canonical finite `<f8 [12288]>` PCL.

The disabled workflow specs preserve `OMP_NUM_THREADS=8`, BLAS-style pools=1, `max-parallel: 1`, <=60 s heartbeat, compiler flags, checkpoint preflight/authority, heavy 39-band compact streaming, exact A/B compact comparator and exact finalizer comparator. Local spill is disposable infrastructure state and never checkpoint authority.

Full-scale memory safety is still unproven. Require >=2.5 GiB free local spill space. The current 6 GiB WSL cap is **not certified safe** because full-scale SHT workspace and final mmap residency remain unknown.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: terminal Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV**: source-lineage PASS, artifact `9768866582`.
- **Exp073BW**: exact streaming-equivalence PASS, artifact `9774112002`.
- **Exp073BZ**: remote checkpoint/failover exact-byte PASS, artifact `9776592370`.
- **Exp073CC/CD/CE**: synthetic/nonclassifying exact-equivalence PASS evidence only, all `+0/+0`.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

While home runner remains locked, the next permitted work is a **repository-side static audit of the disabled Exp073CF package**. Audit activation-time binding completeness, compatibility of status/output tokens with the frozen Exp073CA streaming driver, cleanup/failure paths, and search for any remaining hidden full-size memory copies. No `.github/workflows` activation, trigger creation, rerun, or self-hosted execution is permitted.

After the user explicitly re-enables the home runner, the next actual scientific frontier is a **fresh full-scale Exp073CF Wm_S2 successor**, but only after a new prospective activation binding pins the actual activated workflow/trigger and an infrastructure preflight passes. Do not rerun or reuse stale Exp073CA replica B as scientific authority.

- ✅ Exp073CF disabled package prepared; `+0/+0`; no run created.
- ✅ Exp073CE/CC/CD methodology evidence preserved.
- ✅ Exp073BJ and Exp073BV/BW/BZ authority preserved.
- 🟡 Exp073CA remains infrastructure incomplete; self-hosted replica B queued but locked out.
- ❌ Exp073AQ permanent scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Home runner = OFFLINE/LOCKED. Verified: 52.0% | Draft/data: 53.7%**
