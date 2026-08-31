# Exp073BT — Article-3 NaMaster-2.7 Wigner linkage BJ-environment successor v0.1 — preregistration

**Project:** DSIR only. **Classification:** NONCLASSIFYING infrastructure/source-linkage diagnostic. **Accounting:** `+0/+0` for every outcome.

Frozen prospectively on 2026-08-31 after Exp073BS run `33417511410` terminal `BS_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE` and before any BT result.

## Preserved state

- Exp073BJ terminal Track-A exact authority PASS remains unchanged.
- Exp073AQ permanent hosted exact-repeatability scientific FAIL remains unchanged.
- Exp073BS remains a terminal infrastructure/source-linkage incomplete result. Its full-history freeze passed, but the hosted job failed during environment installation before the inherited Wigner/`drc3jj` diagnostic executed; therefore BS supplies no evidence for or against any Q1–Q4 linkage branch.
- Exp073BS preregistration commit is `284bca8a32cd390781ab7349fc2bcd14f94461ca`.
- The exact inherited failure-capturing linkage diagnostic implementation remains `ci/exp073br_namaster27_wigner_linkage_failure_capturing_v0_1.py` at implementation commit `8a70892c9533206e4011eee041914ca89bae2290`.

## Sole allowed execution/environment change relative to Exp073BS

Replace the unsuccessful system-Python/PyPI installation route with the already hosted-successful Exp073BJ NaMaster-2.7 lineage:

```bash
conda create -y -p "${RUNNER_TEMP}/nmt27" -c conda-forge python=3.11 namaster=2.7 healpy astropy numpy
echo "NMT_PY=${RUNNER_TEMP}/nmt27/bin/python" >> "${GITHUB_ENV}"
```

The hosted runner is pinned to `ubuntu-24.04`, matching the successful Exp073BJ execution lineage. The resulting `NMT_PY` interpreter must be used both to verify `pymaster` version 2.7.x and to execute the inherited diagnostic. These are execution-environment changes only; they do not alter the probe logic, evidentiary branches, Article-3 interpretation, or scientific accounting.

## Frozen probe and outcome interpretation

The exact inherited BR diagnostic is reused unchanged. Its internal `BR_` status prefix is translated administratively to `BT_` without changing the underlying evidentiary branch.

Frozen terminal labels:

- `BT_Q1_EXTENSION_EXPORTS_DRC3JJ`
- `BT_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ`
- `BT_Q3_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND`
- `BT_Q4_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT`
- `BT_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`

Interpretation is frozen as follows:

1. Q1: the loaded `pymaster._nmtlib` extension dynamically exposes `drc3jj`.
2. Q2: the extension does not expose it, but at least one linked runtime dependency does.
3. Q3: neither extension nor linked dependency dynamically exposes it, while the completed installed-text search finds a `drc3jj` reference.
4. Q4: the essential extension/ldd/text-search probes complete and neither dynamic export nor installed-source/text reference is found.
5. Q5: any essential diagnostic remains incomplete, including environment/setup failure or failure to obtain a complete extension+ldd+installed-text-search basis.

A Q1–Q4 result is **source/linkage evidence only**. It is not Wm_S2 authority, WW authority, Layer-A/B authorization, covariance/whitening authorization, G7 authorization, or evidence for new physics.

## Firewalls

- No modification of the inherited diagnostic implementation after this preregistration is allowed for BT.
- No tolerance, ULP, rounding, averaging, majority-vote, preferred-replica or result-driven rescue.
- No use of Exp073BD provisional Wm_S2 branch as downstream authority.
- No covariance/whitening/nuisance/quotient/relation/null/G8 reads or claims from this diagnostic.
- No G8 jump.
- Every BT outcome carries `scientific_readiness_increment=0` and `draft_data_readiness_increment=0`.

**Readiness remains:** `Verified 52.0% | Draft/data 53.7%`.
