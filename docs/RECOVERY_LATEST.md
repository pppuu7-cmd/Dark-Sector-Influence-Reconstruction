# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-08-31  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable hosted artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical-QA work gives `+0/+0`. Track-P provisional work never becomes Track-A authority retroactively.

## Read first

1. `recovery/2026-08-31_exp073br_failure_capturing_linkage_active.md`
2. `recovery/2026-08-31_exp073bq_wigner_linkage_terminal_incomplete.md`
3. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
4. `recovery/2026-08-31_exp073bo_bp_hosted_incomplete_after_bj_authority.md`
5. `recovery/2026-08-31_local_numerical_structure_audit_bj_active.md`
6. `experiments/073bj_article3_wm_s1_two_thread_track_a_successor_v0_1_prereg.md`
7. `experiments/073bj_article3_two_thread_wm_s1_binding_v0_1.json`
8. `experiments/073br_article3_namaster27_wigner_linkage_failure_capturing_v0_1_prereg.md`
9. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`
10. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`

## Current authority state

**Exp073BJ is terminal Track-A exact authority PASS.** Hosted run `33379013167`, head `0fd096e38bf047b8106b80409bb0a2c8538c2c3e`. Compact A job `99446854065` and B job `99446854363` both passed prospective freeze, exact NaMaster 2.7 lineage, exact BI_Q1 binding and exact Exp073AZ PCL binding, then completed full-scale two-thread Wm_S1 compact computation. Frozen compact comparator emitted `PASS_EXP073BJ_WM_S1_COMPACT_EXACT_V0_1`; only then both finalizers ran. Frozen final comparator emitted `PASS_EXP073BJ_WM_S1_TWO_THREAD_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`. Final immutable authority artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`. No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue was used.

Post-classification NONCLASSIFYING Wm_S1 structure diagnostic remains: `sigma_max(K)=0.0348239490982196`, `sigma_min(K)=0.015870953261799613`, `cond_2(K)=2.19419391663377`, `max(abs(WQ-I))=1.5543122344752192e-15`, `||KW-A||_F/||A||_F=2.864435552712881e-16`. This is `+0/+0` and supports only the narrow conclusion that the 39x39 finalizer solve was not the historical multi-hour bottleneck.

Historical states remain unchanged: Exp073AQ permanent hosted exact-repeatability scientific FAIL; Exp073AZ predecessor authority PASS; Exp073BA infrastructure/execution incomplete with no scientific classification; Exp073BH `BH_D2_TIMEOUT_OR_EXTERNAL_CANCELLATION_EVIDENCED`; Exp073BD `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`; Exp073BI `BI_Q1_PARALLEL_EXACT_QA_PASS`, synthetic/infrastructure only.

## Native streaming/source-linkage state

Exp073BO run `33388775380` and Exp073BP run `33389213821` remain terminal infrastructure/QA incomplete: their comparator inputs were never validly produced. They are not scientific FAILs and must not be rerun unchanged.

Exp073BQ run `33411940994`, job `99553364178`, remains terminal `BQ_Q5_INFRASTRUCTURE_INCOMPLETE`. Prospective freeze and exact NaMaster 2.7 install passed, but the linkage inspection step failed before a JSON receipt artifact was produced. Therefore BQ supplies no direct evidence for or against runtime export of `drc3jj`; no root cause may be inferred from BQ alone.

### Exp073BR active failure-capturing successor

Exp073BR repairs only the BQ evidence-capture defect. It is prospectively frozen as NONCLASSIFYING infrastructure/source-linkage QA and gives `+0/+0` for every outcome.

Frozen provenance:

- preregistration commit `ec4b4eb977dc762b20add68190790e85796608fc`;
- failure-capturing harness commit `8a70892c9533206e4011eee041914ca89bae2290`;
- hosted workflow commit lineage `75bfa98bf81e69c468d96242660847b91248d654` -> trigger-path-only update `b73214bc9194b6dd11749b4bfbe128a7358b2b1c`;
- trigger receipt commit/head `aeaf68ed48da941d5b50f592d969b9382eb37fd8`.

Hosted run `33417344643`, job `99571067032`, was queued at the current checkpoint. Do not start another BR while it is active. The harness independently captures version/import, extension `ctypes`, `nm`, `readelf`, `ldd`, dependency symbol probes and bounded installed-text search, then guarantees a partial JSON receipt and `if: always()` artifact upload.

Frozen BR labels: `BR_Q1_EXTENSION_EXPORTS_DRC3JJ`, `BR_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ`, `BR_Q3_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND`, `BR_Q4_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT`, or `BR_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`. None is a scientific PASS/FAIL or source-equivalence authority.

## Frozen Article-3 boundaries

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity is `numerically_unresolved`; no covariance/whitening/nuisance/quotient/relation/null/G8 leakage into earlier support selection.

Required G7 order remains: `validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`. G8 may not be selected or exposed before actual G7 authorization.

## Exact next gate

Consume terminal Exp073BR run `33417344643` and its immutable failure-capturing JSON artifact. Preserve the frozen BR classification exactly. Only after direct hosted linkage evidence exists may a corrected streaming/source-equivalence successor be prospectively frozen; that future successor must still prove exact equivalence/repeatability before any Track-A use. Do not rerun BJ/BO/BP/BQ/BR unchanged. No G8 jump.

## Shorthand

- ✅ Exp073BJ Wm_S1 Track-A exact authority: PASS.
- ✅ Post-BJ Wm_S1 structure diagnostic: well conditioned, `+0/+0`.
- ✅ Exp073AZ predecessor PCL authority: PASS.
- ✅ Exp073BI synthetic parallel QA: PASS, `+0/+0`.
- ✅ Exp073BA/BH infrastructure state preserved; no scientific classification.
- ✅ Exp073BD P3 provisional incomplete; no downstream use.
- ✅ Exp073BQ terminal `BQ_Q5_INFRASTRUCTURE_INCOMPLETE`, `+0/+0`.
- 🟡 Exp073BR failure-capturing linkage diagnostic active, `+0/+0`.
- ❌ Exp073AQ permanent historical exact-repeatability scientific FAIL.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7, G8, G9 unauthorized; G8 jump forbidden.

**Verified: 52.0% | Draft/data: 53.7%**
