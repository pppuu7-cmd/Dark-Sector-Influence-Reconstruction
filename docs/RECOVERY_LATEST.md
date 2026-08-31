# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-08-31  
**Article-3 scientific authority readiness:** **52.0%**  
**Article-3 draft/data readiness:** **53.714285714285715%** (display **53.7%**)  
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state and immutable hosted artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical-QA work gives `+0` scientific readiness. Track-P provisional work never becomes Track-A authority retroactively.

## Read first

1. `recovery/2026-08-31_local_numerical_structure_audit_bj_active.md`
2. `recovery/2026-08-31_exp073bj_binding_provenance_audit_compute_active.md`
3. `recovery/2026-08-31_exp073bi_q1_exp073bj_track_a_active.md`
4. `experiments/073bj_article3_wm_s1_two_thread_track_a_successor_v0_1_prereg.md`
5. `experiments/073bj_article3_two_thread_wm_s1_binding_v0_1.json`
6. `experiments/073bi_article3_wm_s1_parallel_execution_successor_v0_1_prereg.md`
7. `recovery/2026-08-31_exp073bh_d2_timeout_class_evidenced.md`
8. `recovery/2026-08-31_exp073ba_cancelled_execution_incomplete_bd_p3.md`
9. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`
10. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`

## Current authority state

- Exp073AQ remains permanent hosted exact-repeatability scientific FAIL. Numerical closeness never rescues it.
- Exp073AZ exact mask-PCL predecessor authority remains PASS only as predecessor authority.
- Exp073BC/BE provenance route and Exp073BF algorithm QA are closed, all `+0` scientific readiness.
- Exp073BA run `33345968620` remains terminal infrastructure/execution incomplete with no scientific classification.
- Exp073BH run `33370998182` remains `BH_D2_TIMEOUT_OR_EXTERNAL_CANCELLATION_EVIDENCED`: both BA compact jobs reached the frozen 360-minute execution boundary. This is not scientific PASS/FAIL and is not stronger causal evidence for OOM/manual cancellation/runner loss.
- Exp073BD `33342265114` remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, `+0/+0`; no branch salvage.
- Exp073BI run `33375467713` is terminal **`BI_Q1_PARALLEL_EXACT_QA_PASS`**. Artifact `9751718353`, digest `sha256:c857b24fdcc0a49b749fbfd538451a8e53bf98f4da9abd92cefce3c4a9df2752`; independent two-thread QA outputs were exactly equal with identical SHA `5e00c7377d50a71d88c98a324d53ef403617022c8dadd4a390eebbe7be4612ba`. BI is synthetic/infrastructure only, `+0/+0`.
- Exp073BJ is the prospectively frozen full-scale two-thread Track-A Wm_S1 successor. Hosted run **`33379013167`** is active from trigger/head `0fd096e38bf047b8106b80409bb0a2c8538c2c3e`. Compact jobs A `99446854065` and B `99446854363` have both passed prospective freeze, exact NaMaster lineage, exact BI Q1 binding and exact Exp073AZ canonical PCL binding; both are now in `Compute two-thread compact Wm_S1 replica`. No BJ artifacts exist yet, so no compact classification exists.
- Local numerical structure audit is frozen separately as nonclassifying `+0/+0`; it may not alter any BJ decision rule.

## Exp073BJ immutable route and provenance audit

Preregistration `199fc3188808a30d0f364005f9b584a92a262acb`; BJ comparator adapter `66f9727acf7fc94294b6031eaeb34283e1a78058`; inherited exact BA comparator `a0b5bd8065c590e20c648215b8d993452fb7339c`; inherited heavy implementation `d77b7ba88801f6788f3d386e72b445c7859c7153`; workflow `416b4d4717989f9c228c47614d1e9e48f9bc93e4`; binding receipt `cbe5f57f9ae04eb335ad9f9b6e4984bdd82247c0`; trigger/head `0fd096e38bf047b8106b80409bb0a2c8538c2c3e`.

Independent static audit while BJ computes found a narrow harness/provenance-enforcement omission: the workflow checks many binding JSON values but does not explicitly assert the binding receipt's own last-change commit SHA and does not explicitly assert the JSON field `bj_workflow_commit`. For this already-triggered immutable run, external Git history closes the provenance link without modifying the workflow: at run head `0fd096e...`, the binding receipt's last-change commit is exactly `cbe5f57...`, whose parent is workflow commit `416b4d47...`; the workflow file's last-change commit at the same run head is exactly `416b4d47...`; and the binding JSON records that same workflow commit. This audit is `+0/+0`, changes no scientific criterion, and must not be used as post-hoc rescue. Future successor workflow revisions should add those explicit assertions prospectively.

The only intended execution change from BA is the prospectively validated BI two-thread policy (`OMP/OpenBLAS/MKL/NUMEXPR/BLIS=2`, `OMP_DYNAMIC=FALSE`); historical `VECLIB_MAXIMUM_THREADS=1` and compact timeout `360` min remain unchanged. Scientific math, AZ PCL authority, NSIDE/ell/bands/component/shapes and exact comparator criteria remain unchanged.

No tolerance/ULP/rounding/averaging/majority vote/preferred-replica rescue exists. Failure before two complete valid comparator inputs is infrastructure incomplete with no scientific classification. A complete exact mismatch is scientific repeatability FAIL. A scientific PASS can exist only after exact compact PASS, two finalizers, exact final PASS and immutable hosted final authority token `PASS_EXP073BJ_WM_S1_TWO_THREAD_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`.

## Local numerical structure audit — nonclassifying

Local compute established the exact-arithmetic identity `K=AQ`, `W=solve(K,A) => WQ=I_39`. The reusable diagnostic is `ci/article3_window_structure_diagnostic_v0_1.py` at commit `6163c15cb7390d27864a682e405506e14fbf0425`; it defines no PASS/FAIL threshold.

Historical Exp073AQ Wm_S1 A/B windows both give `max(abs(WQ-I)) = 6.816769371198461e-14`, while the maximum difference between their two residual matrices is only `5.551115123125783e-16`. AQ remains permanent scientific FAIL; this merely argues against a gross band-normalization/finalizer-structure error.

Real DES-derived provisional Exp073BD Wm_S2 branch-B artifact `9746250767` gives `cond_2(K)=2.1928888836909883`, `sigma_min(K)=0.01669516419847395`, `max(abs(WQ-I))=9.992007221626409e-16`, and `||KW-A||/||A||=3.2380349152387473e-16`. This provisional task has a very well-conditioned 39x39 finalizer, supporting the diagnosis that the multi-hour execution bottleneck is the full general-coupling construction rather than the final `solve(K,A)`. Wm_S1 conditioning remains unknown until BJ yields a valid compact artifact.

Full audit: `docs/ARTICLE3_LOCAL_NUMERICAL_STRUCTURE_AUDIT_2026-08-31.md`. Recovery checkpoint: `recovery/2026-08-31_local_numerical_structure_audit_bj_active.md`. All results are `+0/+0` and cannot alter frozen BJ criteria.

## Frozen scientific boundaries

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity is `numerically_unresolved`; no covariance/whitening/nuisance/quotient/relation/null/G8 leakage into earlier support selection.

## Required G7 order

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

G8 may not be selected/exposed before actual G7 authorization.

## Exact next operating gate

Do not start a duplicate Exp073BJ run. Re-inspect jobs `99446854065` and `99446854363`. When both compact jobs are terminal, consume immutable compact A/B artifacts and the frozen exact comparator output. Only an exact compact PASS may admit the two finalizers. Consume final authority strictly under the frozen BJ decision classes. After preserving BJ classification, run the nonclassifying structural diagnostic on any valid compact/final payload. If BJ remains heavy/in-progress, continue only independent prerequisite/provenance/code-equivalence/recovery audits.

## Current shorthand

- ✅ Exp073AZ predecessor PCL authority: PASS.
- ✅ Exp073BC/BE provenance route: closed, `+0`.
- ✅ Exp073BF algorithm QA: PASS, synthetic/infrastructure only, `+0`.
- ✅ Exp073BA: execution incomplete, no scientific classification.
- ✅ Exp073BH: D2 execution-boundary evidence, `+0/+0`.
- ✅ Exp073BD: P3 provisional incomplete, no downstream use.
- ✅ Exp073BI: `BI_Q1_PARALLEL_EXACT_QA_PASS`, `+0/+0`.
- ✅ Exp073BJ binding-provenance audit: run-head Git history closes two missing explicit workflow assertions for this immutable run; `+0/+0`.
- ✅ local numerical structure audit: WQ identity frozen; provisional Wm_S2 `cond_2(K)=2.19`; `+0/+0`.
- 🟡 Exp073BJ run `33379013167`: full-scale two-thread Track-A compact A/B active after exact BI/AZ binding PASS.
- ❌ Exp073AQ: permanent exact-repeatability scientific FAIL.
- ❌ Layer A/B, covariance/whitening, G7, G8, G9: not authorized; G8 jump forbidden.

`Verified: 52.0% | Draft/data: 53.7%`
