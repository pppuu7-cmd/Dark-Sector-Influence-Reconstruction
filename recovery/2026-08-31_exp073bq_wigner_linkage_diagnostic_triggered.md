# DSIR recovery checkpoint — Exp073BQ Wigner linkage diagnostic triggered

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Classification:** nonclassifying infrastructure/source-linkage gate, `+0/+0`.

## Preserved authority state

Exp073BJ run `33379013167` is terminal success and remains Track-A exact authority PASS. Compact jobs `99446854065` and `99446854363` completed after prospective freeze, exact BI_Q1 authority binding and exact Exp073AZ PCL binding; compact exact comparator passed, both finalizers were admitted only after that PASS, and final exact comparator passed. Exp073AQ remains permanent historical scientific exact-repeatability FAIL.

## BO/BP negative result preserved

Exp073BO run `33388775380` and Exp073BP run `33389213821` are infrastructure/QA incomplete. Their execution failed before valid comparator inputs existed. They are not scientific FAILs and must not be rerun unchanged.

The concrete BO code path requests `drc3jj` by dynamically opening packaged `pymaster._nmtlib` with `ctypes`. Prior hosted metadata did not record the underlying exception, so non-export of `drc3jj` was only a hypothesis.

## New prospective gate — Exp073BQ

Frozen preregistration: `experiments/073bq_article3_namaster27_wigner_linkage_diagnostic_v0_1_prereg.md`, commit `7c6b15e99ec0691e1e2b3064b2668ef574d8d73f`.

Diagnostic: `ci/exp073bq_namaster27_wigner_linkage_diagnostic_v0_1.py`, commit `c46123466aad96449a94893b199b686afadcfda9`.

Hosted workflow: `.github/workflows/exp073bq-namaster27-wigner-linkage-diagnostic-v0-1.yml`, commit `03485b7d5c3886d9a39d38e08c3d1d591b2deaa0`.

Trigger: `ci/exp073bq_namaster27_wigner_linkage_diagnostic_v0_1.trigger`, commit `c4f4a8c1fd262acaf582426ee3c1dbd009fbc608`.

BQ directly inspects exact NaMaster 2.7 `_nmtlib`, its `ldd` dependency closure, `nm -D`/`readelf -Ws` dynamic symbols, direct `ctypes` lookup of `drc3jj`, and bounded installed textual source/header/build references. Frozen outcomes distinguish extension export, linked-dependency export, runtime-symbol absence with installed source reference, runtime/source-reference absence, and infrastructure incomplete.

BQ cannot alter BJ/AQ classification or Article-3 scientific criteria. No tolerance, ULP, rounding, averaging, majority vote or preferred-replica concept is involved. It is `+0 Verified / +0 Draft-data` under every outcome.

## Accounting and boundaries

`Verified: 52.0% | Draft/data: 53.7%`.

Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7, G8 and G9 remain unauthorized. Required G7 order is unchanged and no G8 jump is permitted.

## Exact next gate

Consume the terminal hosted Exp073BQ classification when available. Only a directly evidenced callable/link target can justify prospectively freezing a corrected streaming/source-equivalence successor. If the packaged runtime route is unsupported, perform source-level NaMaster-2.7 linkage design before any successor. Do not rerun BJ/BO/BP unchanged.
