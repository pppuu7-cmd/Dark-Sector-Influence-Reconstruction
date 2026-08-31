# DSIR recovery checkpoint — Exp073BQ terminal infrastructure incomplete

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Classification:** `BQ_Q5_INFRASTRUCTURE_INCOMPLETE`, NONCLASSIFYING, `+0/+0`.

## Preserved scientific authority

Exp073BJ remains terminal Track-A exact authority PASS. Exp073AQ remains permanent historical scientific exact-repeatability FAIL. No acceptance criterion, threshold, authority state or G7/G8 boundary is altered.

## Exp073BQ provenance

- preregistration commit `7c6b15e99ec0691e1e2b3064b2668ef574d8d73f`;
- diagnostic implementation commit `c46123466aad96449a94893b199b686afadcfda9`;
- hosted workflow commit `03485b7d5c3886d9a39d38e08c3d1d591b2deaa0`;
- trigger commit `c4f4a8c1fd262acaf582426ee3c1dbd009fbc608`;
- hosted run `33411940994`;
- job `99553364178`.

## Terminal evidence

Hosted job metadata records:

- checkout: success;
- prospective freeze enforcement: success;
- exact NaMaster 2.7 installation: success;
- `Inspect runtime Wigner linkage`: failure;
- artifact upload: skipped.

No valid JSON diagnostic receipt or immutable artifact was produced. Therefore frozen classes Q1–Q4 cannot be selected. The only admissible outcome is `BQ_Q5_INFRASTRUCTURE_INCOMPLETE`.

This outcome does **not** prove that `_nmtlib` does or does not export `drc3jj`; it does not establish a linked dependency target; it does not establish upstream/source absence; and it is not a source-equivalence or scientific FAIL. Root cause remains unresolved because the failing inspection step did not preserve its partial probes.

## Methodological negative result

BQ exposed a harness-design deficiency: the inspection script writes its receipt only after all probes complete. A probe-level exception can therefore destroy the very evidence needed to classify linkage. This is an infrastructure/harness defect, not a scientific defect.

A successor must be prospectively frozen and failure-capturing: each probe must be individually guarded, partial results must be serialized in `finally`/equivalent logic, artifact upload must use `if: always()`, and the final classification must distinguish probe failure from genuine symbol absence. It must remain `+0/+0` and may not modify BJ/AQ or Article-3 scientific criteria.

## Accounting

`Verified: 52.0% | Draft/data: 53.7%`.

Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7, G8 and G9 remain unauthorized. No G8 jump.

## Exact next gate

Prospectively freeze a failure-capturing NaMaster-2.7 linkage harness successor. Do not rerun BQ unchanged. Only after direct hosted evidence identifies a valid callable/source-link target may a corrected streaming/source-equivalence successor be frozen.
