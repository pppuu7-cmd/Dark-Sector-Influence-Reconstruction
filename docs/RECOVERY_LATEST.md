# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-08-31  
**Article-3 scientific authority readiness:** **52.0%**  
**Article-3 draft/data readiness:** **53.714285714285715%** (display **53.7%**)  
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state and immutable hosted artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical-QA work gives `+0` scientific readiness. Track-P provisional work never becomes Track-A authority retroactively.

## Read first

1. `experiments/073bq_article3_namaster27_wigner_linkage_diagnostic_v0_1_prereg.md`
2. `recovery/2026-08-31_exp073bo_bp_hosted_incomplete_after_bj_authority.md`
3. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
4. `recovery/2026-08-31_local_numerical_structure_audit_bj_active.md`
5. `experiments/073bj_article3_wm_s1_two_thread_track_a_successor_v0_1_prereg.md`
6. `experiments/073bj_article3_two_thread_wm_s1_binding_v0_1.json`
7. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`
8. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`

## Current authority state

- **Exp073BJ is terminal Track-A exact authority PASS.** Hosted run `33379013167`, head `0fd096e38bf047b8106b80409bb0a2c8538c2c3e`.
- Compact A job `99446854065` and B job `99446854363` both passed prospective freeze, exact NaMaster 2.7 lineage, exact BI_Q1 binding and exact Exp073AZ PCL binding, then completed the full-scale two-thread Wm_S1 compact computation.
- Compact artifacts: A `9758771199` digest `sha256:550ea185c462f807fa0e9eb718aac5b4cf08498cb65508aabc02112274928891`; B `9757788069` digest `sha256:8b696ada051a3f5ff42bb8e30e83b81bd241467e8de087d14b41be75474785bd`.
- Frozen compact comparator job `99495776269` emitted `PASS_EXP073BJ_WM_S1_COMPACT_EXACT_V0_1`; compact authority artifact `9758781028`, digest `sha256:5019b9da9d55f4cfa9304f20576fb791193952c205a763fa0657f528cc70f7af`.
- Only after compact exact PASS, finalizers A `99495858598` and B `99495858554` ran and succeeded.
- Final artifacts: A `9758830321`, digest `sha256:46c48302550f2e35b33bd06af1df6267fd1704b0906516d56cc92f585e3abcfd`; B `9758826333`, digest `sha256:e6eee1e0500d70dd3b5c756fee87be4bb40491aef2edc0255cabb9ed376f7f65`.
- Frozen final comparator job `99496306351` emitted `PASS_EXP073BJ_WM_S1_TWO_THREAD_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`. Final immutable authority artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- Frozen BJ preregistration commit `199fc3188808a30d0f364005f9b584a92a262acb`; frozen BI-to-AZ binding receipt commit `cbe5f57f9ae04eb335ad9f9b6e4984bdd82247c0`.
- No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue was used.

Historical states remain preserved:
- Exp073AQ remains permanent hosted exact-repeatability scientific FAIL. BJ does not erase or reinterpret it.
- Exp073AZ remains exact mask-PCL predecessor authority PASS.
- Exp073BA remains terminal infrastructure/execution incomplete with no scientific classification.
- Exp073BH remains `BH_D2_TIMEOUT_OR_EXTERNAL_CANCELLATION_EVIDENCED`, `+0/+0`.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, `+0/+0`.
- Exp073BI remains terminal `BI_Q1_PARALLEL_EXACT_QA_PASS`, synthetic/infrastructure only, `+0/+0`.

## Post-classification Wm_S1 numerical structure diagnostic — NONCLASSIFYING

Only after preserving the frozen BJ PASS classification, the immutable compact/final payloads were reproduced through the logic of `ci/article3_window_structure_diagnostic_v0_1.py`.

Authoritative Wm_S1 results:
- `sigma_max(K)=0.0348239490982196`;
- `sigma_min(K)=0.015870953261799613`;
- `cond_2(K)=2.19419391663377`;
- `max(abs(WQ-I))=1.5543122344752192e-15`;
- `||WQ-I||_F=3.291139766893894e-15`;
- max off-diagonal `abs(WQ-I)=5.659535340374333e-17`;
- `||KW-A||_F/||A||_F=2.864435552712881e-16`;
- `max(abs(KW-A))/max(abs(A))=8.951217569802171e-16`.

Canonical array-byte hashes:
- compact `A`: `dd640da962f64ebedd8418c1eb3d27a2dca28f0daf345aab8bc445e3a23e497a`;
- final `window`: `1a2be04c40ef434a05edb9d9cb878b718ba906949fe0736ab5ad9e90c90266e3`.

This is `+0/+0` and cannot alter BJ acceptance. Together with provisional BD Wm_S2 `cond_2(K)=2.1928888836909883`, it supports the narrow execution conclusion that the 39x39 finalizer solve is well-conditioned and was not the historical multi-hour bottleneck; the expensive stage remains the dense general-coupling construction.

## Native streaming QA audit after BJ

Exp073BO prospective native band-projected source-equivalence QA run `33388775380` is terminal `failure`. All four replicas passed frozen prereg enforcement, exact NaMaster 2.7 install and native-kernel compilation, then failed in `Run stock and native scales`; no replica receipt/artifact exists and the cross-host exact comparator was skipped. Therefore the only admissible class is infrastructure/harness incomplete (`BO_Q3`), not exact-equivalence FAIL and not a scientific FAIL.

Exp073BP triangular-reciprocity QA run `33389213821` is likewise terminal `failure`: all four replicas passed freeze/install/compile, failed in `Run stock and triangular scales`, produced no valid comparator inputs, and its comparator was skipped. It is infrastructure/QA incomplete only.

Code audit isolated the concrete BO hypothesis: `ci/exp073bo_native_band_projected_general_coupling_qa_v0_1.py` dynamically loads packaged `pymaster._nmtlib` and requests `drc3jj` via `ctypes`. Hosted BO metadata did not expose the exception, so this hypothesis was not promoted to fact.

## Exp073BQ — prospectively frozen linkage diagnostic

A new narrow nonclassifying gate is frozen to resolve that hypothesis directly under exact NaMaster 2.7:

- preregistration commit `7c6b15e99ec0691e1e2b3064b2668ef574d8d73f`;
- diagnostic implementation commit `c46123466aad96449a94893b199b686afadcfda9`;
- hosted workflow commit `03485b7d5c3886d9a39d38e08c3d1d591b2deaa0`;
- trigger commit `c4f4a8c1fd262acaf582426ee3c1dbd009fbc608`.

Frozen outcomes distinguish: direct `_nmtlib` export; direct linked-dependency export; no runtime export but installed textual source/header reference; or no runtime export/source reference in the packaged environment. Installation/inspection failure remains infrastructure incomplete. Exp073BQ is `+0/+0` under every outcome and cannot alter BJ/AQ or any G7/G8 authorization.

## Dual-readiness accounting

`Verified: 52.0% | Draft/data: 53.7%`

No percentage change is applied here. The frozen accounting explicitly gives individual angular tasks `+0` to scientific authority readiness unless separately authorized. Wm_S1 was already counted once in Draft/data through its complete provisional branch pair; Track-A supersession changes authority status but does not double-count the angular object.

## Frozen scientific boundaries

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity is `numerically_unresolved`; no covariance/whitening/nuisance/quotient/relation/null/G8 leakage into earlier support selection.

## Required G7 order

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

G8 may not be selected or exposed before actual G7 authorization.

## Exact next operating gate

Do not rerun Exp073BJ, BO or BP unchanged. Consume the terminal hosted Exp073BQ result when available and preserve its frozen linkage classification. If BQ identifies a callable exact runtime/source target, only then prospectively freeze a corrected source-equivalence streaming successor. If it shows the packaged runtime strategy is unsupported, perform source-level NaMaster-2.7 linkage design before any successor. All such work remains `+0/+0`. The scientific G7 path remains validated physical forward/power-input bridges first; no G8 jump.

## Current shorthand

- ✅ Exp073BJ Wm_S1 Track-A exact authority: PASS.
- ✅ post-BJ Wm_S1 structure diagnostic: well-conditioned `cond_2(K)=2.19419`, `+0/+0`.
- ✅ Exp073AZ predecessor PCL authority: PASS.
- ✅ Exp073BI: `BI_Q1_PARALLEL_EXACT_QA_PASS`, `+0/+0`.
- ✅ Exp073BA/BH infrastructure diagnosis: preserved, no scientific classification.
- ✅ Exp073BD: P3 provisional incomplete, no downstream use.
- 🟡 Exp073BQ: frozen Wigner linkage diagnostic triggered; terminal hosted classification pending.
- 🟡 Native streaming architecture: BO/BP hosted QA incomplete; BQ is the direct linkage root-cause gate.
- ❌ Exp073AQ: permanent historical exact-repeatability scientific FAIL.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7, G8, G9: not authorized; G8 jump forbidden.

`Verified: 52.0% | Draft/data: 53.7%`
