# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-01_exp073cd_production_spill_integration_audit.md`
2. `recovery/2026-09-01_exp073cd_q1_spill_reload_exact_equivalence_pass.md`
3. `recovery/2026-09-01_exp073cc_fullscale_memory_budget_audit.md`
4. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
5. `recovery/2026-09-01_exp073cb_helper_rss_semantics_audit.md`
6. `recovery/2026-09-01_exp073ca_attempt3_infra_incomplete_exp073cb_hosted_memory_qa_active.md`
7. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
8. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
9. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
10. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
11. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current overnight frontier

- Home runner is **OFFLINE/LOCKED** until the user explicitly re-enables it.
- Exp073CA attempt3 run `33448843621`: replica A job `99673921219` terminal infrastructure failure during fresh Wm_S2 PCL; replica B job `99673921530` remains queued self-hosted and must not be revived overnight.
- Frozen Exp073CA classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`.
- Compile, checkpoint preflight/restore, heavy 39-band streaming, exact compact comparator and finalizer did not run in replica A.
- Latest coordination check before the production-audit pointer sync: zero `in_progress` DSIR runs; Exp073CA attempt3 is the sole queued run.

## Exp073CD terminal spill/reload QA

Hosted run `33495127089`, job `99815424166`, immutable artifact `9795414546`, digest `sha256:9c88bb95c796e4a0220856f93574e14aa1873dbcd00b714c2e37693edfa5c069`.

Frozen classification: **`CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS`**. For every frozen `NSIDE={64,128,256}` case, canonical `<c16>` first-mask ALM saved/reloaded SHA-256 was exactly identical, and final PCL passed `np.array_equal` plus canonical `<f8` SHA equality against the corrected-sequential oracle. No tolerance/ULP/rounding/averaging/smoothing/majority/preferred-replica rescue.

RSS remained essentially unchanged at these small/medium hosted geometries; this is diagnostic only and must not be extrapolated into full DES memory safety. Exp073CD is `+0/+0` and closes no real-survey/scientific gate.

## Production spill/reload integration audit

Repository-side audit `recovery/2026-09-01_exp073cd_production_spill_integration_audit.md` binds the future memory-only Wm sequence to `ci/exp073az_article3_low_memory_general_coupling_v0_1.py::task_pcl` without changing scientific arithmetic.

Required future sequence is: lens map -> lens `NmtField` -> delete caller lens map -> first mask ALM -> delete lens field -> canonical `<c16>` SHA -> same-filesystem atomic `.npy` spill/verify -> delete in-memory first ALM -> source map -> source `NmtField` -> delete caller source map -> second mask ALM -> delete source field -> reopen first ALM read-only mmap with exact shape/dtype/SHA verification -> unchanged `hp.alm2cl` -> canonical contiguous `<f8>` PCL.

At DES `NSIDE=4096`, `lmax=12287`, one first-mask complex128 ALM has `75,503,616` values = `1,208,057,856` payload bytes ≈ **1.12509 GiB**. Future preflight should require at least **2.5 GiB free local spill space per active replica**. Spill scratch is local infrastructure state, not Git/checkpoint/scientific authority.

The memory benefit is specifically removal of the retained first ALM from the **second SHT phase**. Final `hp.alm2cl` will traverse the mmap and may residentize file-backed pages, so full-scale RSS safety under the 6 GiB WSL cap remains unproven. `/usr/bin/time -v` RSS remains infrastructure diagnostics only.

Atomicity/failure semantics are frozen for future preregistration planning: unique temp file -> flush/fsync -> atomic rename -> exact shape/dtype/canonical SHA verification; partial temp files are disposable; stale spills may never be reused without exact task/replica/input-lineage/SHA binding; spill state must remain separate from the existing post-PCL remote 39-band checkpoint namespace.

Future heavy heartbeat remains <=60 s and must name stages such as `lens_mask_build`, `lens_field_sht`, `alm_spill_verify`, `source_mask_build`, `source_field_sht`, `alm_reload_verify`, `alm2cl`, `pcl_persist`; when transform fractional progress is unknowable use `intra_unit_progress=unknown`. Heartbeat must never touch scientific arithmetic.

## Exp073CC and full-scale memory budget

Exp073CC run `33475627726`, job `99754170638`, immutable artifact `9788075152`, digest `sha256:08b0e29e93e9eddaabe7f23de618a7a68b152b2115eb0e1727d7f3d0af8de5d9` remains **`CC_Q1_EXACT_EQUIVALENCE_PASS`**.

For DES `NSIDE=4096`, one float64 map is 1.500 GiB and one complex128 mask ALM is about 1.12509 GiB. Current simultaneous lifetime is about **8.25018 GiB** persistent payload before SHT workspace/process overhead. Corrected sequential lifetime lowers worst deterministic persistent baseline to about **4.12509 GiB**. The CD-supported spill design gives a prospective deterministic second-SHT baseline near **2.62509 GiB plus SHT workspace/process overhead**. This remains an engineering estimate, not proof that the current 6 GiB WSL cap is safe.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: terminal Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV**: `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`, artifact `9768866582`.
- **Exp073BW**: `BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS`, artifact `9774112002`.
- **Exp073BZ**: remote checkpoint/failover exact-byte PASS, artifact `9776592370`.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

While home runner remains locked, do not touch or revive Exp073CA replica B. The next permitted work is a **prospective successor design audit/preregistration** binding the production spill/reload lifetime changes to the frozen Exp073CA scientific contract and checking for any hidden semantic change to inputs, `NmtField` arguments, `lmax`, `hp.alm2cl`, PCL canonicalization, compact streaming, exact comparator, checkpoint authority or thread policy. If no unresolved semantic delta remains, prepare—but do not trigger—the future self-hosted successor.

Only after the user explicitly re-enables the home runner may a separately prospectively frozen Exp073CA infrastructure successor use the Exp073CC/Exp073CD-supported memory-lifetime repairs.

- ✅ Exp073CD = `CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS`; immutable artifact `9795414546`.
- ✅ Exp073CC = `CC_Q1_EXACT_EQUIVALENCE_PASS`; immutable artifact `9788075152`.
- ✅ Production spill/reload insertion/atomicity/checkpoint audit recorded; `+0/+0`.
- ✅ Exp073BJ exact Track-A Wm_S1 authority PASS preserved.
- ✅ Exp073BV/BW/BZ prerequisite authority preserved.
- 🟡 Exp073CA remains infrastructure incomplete; self-hosted replica B queued but locked out.
- ❌ Exp073AQ permanent historical scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Verified: 52.0% | Draft/data: 53.7%**
