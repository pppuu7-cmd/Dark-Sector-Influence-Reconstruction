# DSIR checkpoint — Exp073BO/BP hosted incomplete after Exp073BJ authority

**Date:** 2026-08-31
**Scope:** DSIR Article-3 only. RTK/RQIR excluded.
**Accounting:** `Verified 52.0% | Draft/data 53.7%`; this checkpoint is `+0/+0`.

## Exp073BJ authority revalidation

Hosted run `33379013167` remains terminal Track-A exact authority PASS. Both compact replicas passed the frozen BI_Q1 and Exp073AZ PCL binding, the frozen compact comparator passed, both finalizers then passed, and the final exact comparator emitted `PASS_EXP073BJ_WM_S1_TWO_THREAD_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`. Final immutable authority artifact remains `9758841785` (`sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`).

Frozen BJ preregistration is commit `199fc3188808a30d0f364005f9b584a92a262acb`; immutable BI-to-AZ binding receipt is commit `cbe5f57f9ae04eb335ad9f9b6e4984bdd82247c0`, file `experiments/073bj_article3_two_thread_wm_s1_binding_v0_1.json`. No tolerance/ULP/rounding/averaging/majority/preferred-replica rescue is introduced.

## Exp073BO — terminal QA infrastructure incomplete

Prospective nonclassifying source-equivalence QA preregistration: commit `0b1be1ce0f17d0c8899a9be674f99eb0a2d89138`.
Hosted run: `33388775380`, head `1e36511108b18945e9145dbe69857cf2da5af3c9`, terminal `failure`.

All four replicas A-D:
- passed prospective-freeze enforcement;
- installed exact NaMaster 2.7 lineage;
- compiled the native projected kernel;
- failed in `Run stock and native scales`;
- therefore did not build replica receipts or upload artifacts.
The frozen cross-host comparator was skipped. No two/four complete comparator inputs exist.

Classification: `BO_Q3_INFRASTRUCTURE_INCOMPLETE` / harness-execution incomplete, **not** `BO_Q2...FAIL` and not a scientific FAIL. There is no exact stock-vs-native comparison result to classify.

Code audit identifies a concrete diagnostic target but not a proven cause: the native driver resolves `drc3jj` dynamically from `pymaster._nmtlib` using `ctypes.CDLL(...); getattr(cdll,'drc3jj')`. If the symbol is not exported in the packaged extension, the native stage raises before producing its output. Hosted metadata alone does not prove that this is the observed exception, so the root cause remains unresolved pending a narrow symbol/export diagnostic or captured log.

## Exp073BP — terminal QA infrastructure incomplete

Hosted run `33389213821`, head `33a28ca5d81caf23d5b1da77f219c5c4b523be7d`, terminal `failure`.
All four replicas passed freeze/install/compile and failed in `Run stock and triangular scales`; receipt/upload steps were skipped and the comparator was skipped. Therefore no complete exact reciprocity comparator exists. Classify as infrastructure/QA incomplete only; do not infer scientific or source-equivalence mismatch.

## Scientific firewalls

- Exp073AQ remains permanent historical `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.
- Exp073BJ PASS does not erase AQ.
- BO/BP are synthetic/source/infrastructure QA and contribute `+0 Verified / +0 Draft-data` regardless of eventual outcome.
- Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7 and G8 remain unauthorized.
- Required order remains: validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family.

## Exact next gate

Do not rerun BJ. Do not rerun BO/BP unchanged. Next useful nonclassifying gate is a prospectively frozen narrow native-symbol/source-linkage diagnostic that determines whether the packaged NaMaster 2.7 extension exposes/can safely call the exact Wigner `drc3jj` implementation (or identifies the exact source-level callable/link target) **without** changing any scientific Article-3 acceptance rule. Only after that diagnostic may a corrected streaming/source-equivalence QA successor be preregistered. In parallel, physical forward/power-input bridge ordering remains the scientific G7 path; no G8 access is allowed.