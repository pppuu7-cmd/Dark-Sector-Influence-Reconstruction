# DSIR recovery — Exp073BR Q5 terminal; Exp073BS full-history successor active

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Accounting:** `Verified 52.0% | Draft/data 53.7%`; all BR/BS outcomes are `+0/+0`.

## Exp073BR terminal

Hosted run `33417344643`, job `99571067032`, is terminal failure. The exact frozen classification is:

`BR_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`

Direct hosted logs show checkout used default `fetch-depth: 1`; `Enforce Exp073BR prospective freeze` then exited code 1 before NaMaster installation or linkage probes. The workflow fallback path executed successfully and uploaded immutable artifact `9767517801`, ZIP digest `sha256:2268a3ef4544aae6b4e7bbf0701f5719d127080b3c3da8bd273afb32b7274263`. The fallback receipt preserves Exp073AQ FAIL, Exp073BJ PASS, no scientific authority, and `+0/+0` accounting.

The narrow harness diagnosis is that BR's history-based SHA enforcement was not execution-safe under a depth-1 checkout. Because the logs do not identify which of the sequential assertions was the first false expression, no stronger claim is made. BR produced no evidence for or against `drc3jj` linkage.

## Exp073BS prospective successor

BS changes only the execution prerequisite needed by the same frozen linkage diagnostic: checkout now uses `fetch-depth: 0` before `git log` history assertions. The BR probe implementation is reused unchanged.

Provenance:

- BS preregistration commit `284bca8a32cd390781ab7349fc2bcd14f94461ca`;
- inherited BR harness commit `8a70892c9533206e4011eee041914ca89bae2290`;
- BS workflow commit `27a10caa405ca2e99eb5d565979efb642b423b71`;
- BS trigger/head commit `8a3b23736cffebfd2e3696f7c1d6e9b36a3e761b`;
- hosted run `33417511410`, job `99571616144`.

At this checkpoint BS is in progress in full-history checkout. No duplicate BR/BS run is permitted while it is active.

Frozen BS outcomes are `BS_Q1_EXTENSION_EXPORTS_DRC3JJ`, `BS_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ`, `BS_Q3_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND`, `BS_Q4_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT`, or `BS_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`. All are nonclassifying infrastructure/source-linkage labels.

## Permanent scientific state

Exp073BJ remains terminal Track-A exact authority PASS. Exp073AQ remains permanent historical exact-repeatability scientific FAIL. No tolerance/ULP/rounding/averaging/majority/preferred-replica rescue exists. Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7 and G8 remain unauthorized.

## Exact next gate

Consume terminal Exp073BS run `33417511410`, its immutable JSON artifact and hosted probe evidence. Only after direct linkage evidence exists may a corrected streaming/source-equivalence successor be prospectively frozen, and such a successor must still prove exact equivalence/repeatability before any Track-A use.
