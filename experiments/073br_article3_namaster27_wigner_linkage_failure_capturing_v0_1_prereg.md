# Exp073BR — Article-3 NaMaster-2.7 Wigner linkage failure-capturing diagnostic v0.1 — preregistration

**Project:** Dark-Sector Influence Reconstruction (DSIR) only; RTK/RQIR excluded.  
**Frozen prospectively:** 2026-08-31 after Exp073BQ terminal `BQ_Q5_INFRASTRUCTURE_INCOMPLETE` and before any Exp073BR hosted result.  
**Classification:** NONCLASSIFYING infrastructure/source-linkage diagnostic.  
**Accounting:** `+0 Verified / +0 Draft-data` for every possible outcome.

## Immutable predecessor state

- Exp073BJ run `33379013167` remains terminal Track-A exact authority PASS; BR may not alter or reinterpret it.
- Exp073AQ remains permanently `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.
- Exp073BQ run `33411940994`, job `99553364178`, remains `BQ_Q5_INFRASTRUCTURE_INCOMPLETE`: its diagnostic step failed before a receipt artifact existed, so BQ provides no direct evidence for or against runtime export of `drc3jj`.
- BO/BP remain infrastructure/QA incomplete and are not rerun unchanged.

## Sole purpose

Obtain direct hosted evidence about how NaMaster 2.7 exposes or references the Wigner `drc3jj` implementation while guaranteeing a durable partial JSON receipt even if any individual probe fails.

This diagnostic is not a scientific gate, does not validate a streaming kernel, and cannot authorize a Track-A replacement implementation by itself.

## Frozen probes

The harness must attempt, independently and with exception capture:

1. installed `pymaster` version;
2. import and resolved path of `pymaster._nmtlib`;
3. direct `ctypes.CDLL(extension)` lookup of `drc3jj`;
4. `nm -D` and `readelf -Ws` on the extension;
5. `ldd` dependency enumeration;
6. for each resolvable linked dependency, independent `ctypes` lookup plus `nm -D` and `readelf -Ws`;
7. bounded installed-text search for `drc3jj` in plausible package/prefix source/header/build metadata.

Every probe records success/failure/error independently. No failed probe may abort receipt creation.

## Frozen durability requirements

- JSON receipt path: `data/derived/g7/exp073br_wigner_linkage_failure_capturing_result_v0_1.json`.
- Receipt must be written in a `finally`-equivalent path even if version/import/linkage probes fail.
- Workflow artifact upload must use `if: always()` and must not depend on the diagnostic process exit status.
- Diagnostic process should normally exit zero after recording probe failures; unexpected top-level exceptions must still produce the partial receipt before exit.

## Frozen outcome labels

The receipt must assign exactly one nonclassifying status:

- `BR_Q1_EXTENSION_EXPORTS_DRC3JJ`: extension import/path known and direct dynamic lookup finds nonzero `drc3jj`.
- `BR_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ`: extension does not provide it directly, but at least one linked dependency does.
- `BR_Q3_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND`: no direct/linked dynamic export found, but bounded installed-text search finds at least one `drc3jj` reference.
- `BR_Q4_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT`: required runtime probes completed sufficiently to establish no direct/linked export and no installed-text reference was found.
- `BR_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`: evidence is insufficient to distinguish Q1–Q4 (for example extension import/path unresolved, `ldd` unavailable, or other essential probe coverage missing).

These are infrastructure/source-linkage diagnostic labels only, never scientific PASS/FAIL.

## Interpretation firewall

- A Q1/Q2 result proves only a callable dynamic symbol target exists in that hosted environment; it does not prove exact equivalence of any future streaming implementation.
- Q3 proves only that an installed textual reference exists; it does not prove the reference is callable or ABI-compatible.
- Q4 is limited to the frozen hosted environment and bounded search scope; it is not a general claim about all NaMaster source distributions.
- Q5 requires a later prospectively frozen diagnostic if more evidence is needed; no root cause may be guessed.
- No tolerance, ULP, rounding, averaging, majority vote, preferred-replica rescue, or post-hoc scientific criterion is introduced.

## Article-3/G7 firewall

All existing frozen Article-3 boundaries remain unchanged. Required G7 order remains:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

BR cannot authorize Layer A/B, covariance/whitening, nuisance geometry, quotient/relation/null, G7 or G8.

**Readiness remains:** `Verified 52.0% | Draft/data 53.7%`.
