# Exp073BS — Article-3 NaMaster-2.7 Wigner linkage full-history successor v0.1 — preregistration

**Project:** DSIR only. **Classification:** NONCLASSIFYING infrastructure/source-linkage diagnostic. **Accounting:** `+0/+0` for every outcome.

Frozen prospectively on 2026-08-31 after Exp073BR run `33417344643` terminal `BR_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE` and before any BS result.

## Preserved state

- Exp073BJ terminal Track-A exact authority PASS remains unchanged.
- Exp073AQ permanent exact-repeatability scientific FAIL remains unchanged.
- BR artifact `9767517801`, ZIP digest `sha256:2268a3ef4544aae6b4e7bbf0701f5719d127080b3c3da8bd273afb32b7274263`, proves the fallback receipt/upload path works but contains no NaMaster linkage evidence because freeze enforcement failed before install/probes.

## Sole allowed change relative to BR

Use `actions/checkout@v4` with `fetch-depth: 0` before SHA-history freeze assertions. BR used the default shallow `fetch-depth: 1` while invoking `git log -1 -- <path>`, so the hosted history assertions were not execution-safe.

All linkage probes, receipt schema, frozen Q1–Q5 interpretation, Article-3 firewalls and readiness accounting are inherited unchanged from Exp073BR. The exact BR diagnostic implementation commit `8a70892c9533206e4011eee041914ca89bae2290` is reused unchanged.

## Frozen labels

- `BS_Q1_EXTENSION_EXPORTS_DRC3JJ`
- `BS_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ`
- `BS_Q3_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND`
- `BS_Q4_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT`
- `BS_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`

The reused BR script emits BR labels internally; the BS hosted workflow must translate the receipt status prefix `BR_` to `BS_` without changing the evidentiary branch, then save the BS authority-free receipt. This prefix translation is administrative only and cannot change probe evidence.

No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue. No G8 jump.

**Readiness remains:** `Verified 52.0% | Draft/data 53.7%`.
