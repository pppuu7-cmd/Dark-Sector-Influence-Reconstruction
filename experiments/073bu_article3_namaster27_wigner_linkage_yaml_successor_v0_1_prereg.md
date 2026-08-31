# Exp073BU — Article-3 NaMaster-2.7 Wigner linkage YAML-only successor v0.1 — preregistration

**Project:** DSIR only. **Classification:** NONCLASSIFYING infrastructure/source-linkage diagnostic. **Accounting:** `+0/+0` for every outcome.

Frozen prospectively on 2026-08-31 after Exp073BT hosted run `33419946707` terminated with workflow-level failure and **zero jobs**, before any BU result.

## Preserved state

- Exp073BJ terminal Track-A exact authority PASS remains unchanged.
- Exp073AQ permanent hosted exact-repeatability scientific FAIL remains unchanged.
- Exp073BS remains `BS_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`: setup failed before its inherited linkage probe.
- Exp073BT preregistration commit `07c17496597306ff410633264d1d050f833728b9` remains immutable.
- Exp073BT workflow creation commit `16ecd4cb75a68a8878f539b301ae76d3f044b4e0` remains an execution-harness failure: run `33419946707` produced no job and therefore no diagnostic evidence.
- The inherited diagnostic remains exactly `ci/exp073br_namaster27_wigner_linkage_failure_capturing_v0_1.py` at implementation commit `8a70892c9533206e4011eee041914ca89bae2290`.
- The BJ environment lineage remains exactly conda-forge `python=3.11 namaster=2.7 healpy astropy numpy` on `ubuntu-24.04`.

## Sole allowed change relative to Exp073BT

Correct only the YAML representation of the inherited-diagnostic invocation. The invalid single-line form

```yaml
run: "${NMT_PY}" ci/exp073br_namaster27_wigner_linkage_failure_capturing_v0_1.py
```

is replaced by a valid block scalar:

```yaml
run: |
  "${NMT_PY}" ci/exp073br_namaster27_wigner_linkage_failure_capturing_v0_1.py
```

No environment package, runner, diagnostic code, Q1–Q5 criterion, receipt interpretation, Article-3 firewall, or readiness accounting may change.

## Frozen labels and interpretation

Administrative BR-to-BU prefix translation only:

- `BU_Q1_EXTENSION_EXPORTS_DRC3JJ`
- `BU_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ`
- `BU_Q3_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND`
- `BU_Q4_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT`
- `BU_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`

Q1–Q4 retain exactly the definitions frozen in Exp073BT. Q5 covers any incomplete essential basis. Any BU outcome is source/linkage infrastructure evidence only and cannot itself authorize Wm_S2, WW, Layer A/B, covariance/whitening, G7, or G8.

## Firewalls

- No modification of inherited diagnostic code.
- No tolerance, ULP, rounding, averaging, majority vote, preferred-replica, or result-driven rescue.
- Exp073BD provisional Wm_S2 remains forbidden as downstream authority.
- No downstream covariance/whitening/nuisance/quotient/relation/null/G8 read or claim.
- No G8 jump.
- `scientific_readiness_increment=0`; `draft_data_readiness_increment=0` for every result.

**Readiness remains:** `Verified 52.0% | Draft/data 53.7%`.
