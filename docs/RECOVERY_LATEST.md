# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-01_exp073ca_memory_stable_successor_semantic_binding_audit.md`
2. `recovery/2026-09-01_exp073cd_production_spill_integration_audit.md`
3. `recovery/2026-09-01_exp073cd_q1_spill_reload_exact_equivalence_pass.md`
4. `recovery/2026-09-01_exp073cc_fullscale_memory_budget_audit.md`
5. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
6. `recovery/2026-09-01_exp073cb_helper_rss_semantics_audit.md`
7. `recovery/2026-09-01_exp073ca_attempt3_infra_incomplete_exp073cb_hosted_memory_qa_active.md`
8. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
9. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
10. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
11. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
12. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current overnight frontier

- Home runner is **OFFLINE/LOCKED** until the user explicitly re-enables it.
- Exp073CA attempt3 run `33448843621`: replica A job `99673921219` terminal infrastructure failure during fresh Wm_S2 PCL; replica B job `99673921530` remains queued self-hosted and must not be revived overnight.
- Frozen Exp073CA classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`, not scientific FAIL.
- Compile, checkpoint preflight/restore, heavy 39-band streaming, exact compact comparator and finalizer did not run in replica A.
- Latest coordination checks around the successor semantic audit found exactly one queued DSIR run (Exp073CA attempt3) and zero `in_progress` DSIR runs.

## Memory-stable successor semantic-binding audit

Repository audit `recovery/2026-09-01_exp073ca_memory_stable_successor_semantic_binding_audit.md` compared the proposed sequential/spill PCL lifetime repair against the frozen Exp073CA scientific contract. No unresolved scientific-semantic delta is required if the repair is prospectively frozen with the documented guardrails.

The most important newly explicit guardrail is `lmax`: frozen production calls `hp.alm2cl(..., lmax=fa.ainfo_mask.lmax)`. A future repair that deletes the lens `NmtField` before final `alm2cl` must first capture `pcl_lmax=int(fa.ainfo_mask.lmax)` and fail closed unless it equals `12287`; silently replacing this dynamic derivation by an assumed literal is not preferred.

Future fields must retain the exact production constructor semantics `nmt.NmtField(a,None,spin=0)` and `nmt.NmtField(b,None,spin=2)` with no opportunistic `lmax`, `lmax_mask`, purification, beam or template changes. The first ALM may be canonicalized to contiguous `<c16>` only for exact spill identity, then SHA/shape/dtype verified; mmap reload must be read-only and byte-identical before the unchanged `hp.alm2cl` call. PCL remains contiguous `<f8 [12288]`, finite, with unchanged downstream compact/checkpoint/finalizer arithmetic.

The audit explicitly freezes the firewall that local ALM spill state is disposable PCL-stage infrastructure scratch and cannot become remote scientific checkpoint authority. Compact streaming, checkpoint helpers, compiler flags, exact comparator and finalizer require no scientific modification.

## Exp073CD / Exp073CC memory evidence

Exp073CD hosted run `33495127089`, job `99815424166`, immutable artifact `9795414546`, digest `sha256:9c88bb95c796e4a0220856f93574e14aa1873dbcd00b714c2e37693edfa5c069` is terminal **`CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS`**. For frozen `NSIDE={64,128,256}`, first-mask canonical `<c16>` ALM save/reload SHA was exactly identical and final PCL passed `np.array_equal` plus canonical `<f8` SHA against corrected sequential. No tolerance rescue. `+0/+0`.

Exp073CC hosted run `33475627726`, job `99754170638`, artifact `9788075152`, digest `sha256:08b0e29e93e9eddaabe7f23de618a7a68b152b2115eb0e1727d7f3d0af8de5d9` remains **`CC_Q1_EXACT_EQUIVALENCE_PASS`**.

At DES `NSIDE=4096`, one float64 map is 1.500 GiB and one complex128 mask ALM is about 1.12509 GiB. Current simultaneous lifetime is about **8.25018 GiB** persistent payload before SHT workspace/process overhead. Corrected sequential lifetime lowers worst deterministic persistent baseline to about **4.12509 GiB**. The CD-supported spill design gives a prospective deterministic second-SHT baseline near **2.62509 GiB plus SHT workspace/process overhead**. This remains an engineering estimate, not proof that the current 6 GiB WSL cap is safe.

A future preflight should require at least **2.5 GiB free local spill space per active replica**, same-filesystem temp -> flush/fsync -> atomic rename -> exact verification, with matrix `max-parallel: 1`. Final `alm2cl` may residentize mmap pages, so full-scale RSS remains unproven.

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

While the home runner remains locked, do not touch or revive Exp073CA replica B. The next permitted work is to prepare a **prospectively frozen, hosted-testable memory-stable successor implementation package**: new infrastructure-successor preregistration, narrowly scoped PCL helper implementing sequential/spill lifetime with dynamic `pcl_lmax` capture/assertion, hosted exact-equivalence selftest/QA, and workflow/binding skeleton. The package may be prepared and frozen in Git but must not create or trigger any `[self-hosted, Linux, X64]` run.

Only after the user explicitly re-enables the home runner may a separate trigger commit launch the full-scale successor. No rerun of attempt3 and no reuse of its stale queued replica B.

- ✅ Exp073CD = `CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS`; immutable artifact `9795414546`.
- ✅ Exp073CC = `CC_Q1_EXACT_EQUIVALENCE_PASS`; immutable artifact `9788075152`.
- ✅ Production spill insertion/atomicity/checkpoint audit recorded; `+0/+0`.
- ✅ Successor semantic-binding audit recorded; dynamic `fa.ainfo_mask.lmax` guardrail identified; `+0/+0`.
- ✅ Exp073BJ exact Track-A Wm_S1 authority PASS preserved.
- ✅ Exp073BV/BW/BZ prerequisite authority preserved.
- 🟡 Exp073CA remains infrastructure incomplete; self-hosted replica B queued but locked out.
- ❌ Exp073AQ permanent historical scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Verified: 52.0% | Draft/data: 53.7%**
