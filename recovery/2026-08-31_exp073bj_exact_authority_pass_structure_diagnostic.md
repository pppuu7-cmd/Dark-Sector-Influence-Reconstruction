# DSIR recovery checkpoint — Exp073BJ exact authority PASS + nonclassifying Wm_S1 structure diagnostic

**Date:** 2026-08-31  
**Scope:** DSIR only. RTK/RQIR excluded.  
**Classification:** Track-A exact authority PASS, followed only afterwards by a nonclassifying numerical-structure diagnostic.

## Frozen Exp073BJ outcome

Hosted run `33379013167`, trigger/head `0fd096e38bf047b8106b80409bb0a2c8538c2c3e`.

Compact jobs:
- A `99446854065` — completed success.
- B `99446854363` — completed success.

Both jobs passed prospective freeze, exact NaMaster 2.7 lineage, exact BI_Q1 execution binding and exact Exp073AZ PCL binding before full-scale two-thread compact computation. Both full-scale compact computations completed and uploaded immutable artifacts.

Compact artifacts:
- A artifact `9758771199`, archive digest `sha256:550ea185c462f807fa0e9eb718aac5b4cf08498cb65508aabc02112274928891`.
- B artifact `9757788069`, archive digest `sha256:8b696ada051a3f5ff42bb8e30e83b81bd241467e8de087d14b41be75474785bd`.

Frozen exact comparator job `99495776269` consumed both artifacts and emitted, in order:

`PASS_EXP073BA_WM_S1_COMPACT_EXACT_V0_1`

`PASS_EXP073BJ_WM_S1_COMPACT_EXACT_V0_1`

Therefore the prospectively frozen exact compact gate PASSED. No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rule was used.

Compact authority artifact:
- artifact `9758781028`;
- digest `sha256:5019b9da9d55f4cfa9304f20576fb791193952c205a763fa0657f528cc70f7af`.

Only after this frozen exact compact PASS, both finalizers were admitted:
- finalizer A job `99495858598` — success;
- finalizer B job `99495858554` — success.

Final artifacts:
- A artifact `9758830321`, digest `sha256:46c48302550f2e35b33bd06af1df6267fd1704b0906516d56cc92f585e3abcfd`;
- B artifact `9758826333`, digest `sha256:e6eee1e0500d70dd3b5c756fee87be4bb40491aef2edc0255cabb9ed376f7f65`.

Frozen final exact comparator job `99496306351` completed success and emitted:

`PASS_EXP073BA_WM_S1_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`

`PASS_EXP073BJ_WM_S1_TWO_THREAD_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`

Final immutable authority artifact:
- artifact `9758841785`;
- digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.

This is the first successful full-scale two-thread Track-A Wm_S1 exact authority successor after BA's execution-boundary incompletion. Exp073AQ remains permanently preserved as the historical exact-repeatability scientific FAIL and is not overwritten or reinterpreted.

## Nonclassifying Wm_S1 numerical-structure diagnostic

Only after preserving the frozen BJ compact and final PASS classifications, the immutable BJ compact/final authority payloads were reproduced through `ci/article3_window_structure_diagnostic_v0_1.py` logic. This diagnostic is explicitly `+0/+0` and cannot alter BJ criteria or authority.

Canonical payload hashes:
- compact A-array bytes SHA256 `dd640da962f64ebedd8418c1eb3d27a2dca28f0daf345aab8bc445e3a23e497a`;
- final window bytes SHA256 `1a2be04c40ef434a05edb9d9cb878b718ba906949fe0736ab5ad9e90c90266e3`.

Results for frozen Wm_S1:
- `sigma_max(K) = 0.0348239490982196`;
- `sigma_min(K) = 0.015870953261799613`;
- `cond_2(K) = 2.19419391663377`;
- `max(abs(WQ-I)) = 1.5543122344752192e-15`;
- `||WQ-I||_F = 3.291139766893894e-15`;
- max off-diagonal `abs(WQ-I) = 5.659535340374333e-17`;
- `||KW-A||_F / ||A||_F = 2.864435552712881e-16`;
- `max(abs(KW-A))/max(abs(A)) = 8.951217569802171e-16`;
- minimum window row L1 norm `1.008682540869702`;
- maximum window row L1 norm `1.2288526222627798`.

Scientific interpretation is deliberately narrow: like provisional BD Wm_S2 (`cond_2(K)=2.1928888836909883`), authoritative Wm_S1 has a very well-conditioned 39x39 finalizer. This strengthens the execution diagnosis that the historical multi-hour bottleneck was the dense general-coupling construction rather than the small final `solve(K,A)`. It is not a new acceptance criterion and adds no scientific-readiness credit.

## Accounting

The dual-readiness ledger remains:

`Verified: 52.0% | Draft/data: 53.7%`

Reason: the frozen accounting document explicitly gives individual angular tasks `+0` to Scientific Authority Readiness unless separately authorized, and Wm_S1 was already counted once in Draft/data as a manuscript-usable provisional branch pair. Track-A supersession changes its authority label but does not double-count draft/data points.

## Boundaries preserved

- Exp073AQ permanent historical exact-repeatability FAIL remains unchanged.
- Synthetic/infrastructure/provenance/numerical QA remains `+0/+0`.
- No post-hoc tolerance or rescue rule exists.
- Layer A/B, covariance restriction/whitening, nuisance tangent SVD, quotient/relation/null control and G7 remain to be completed in their frozen order.
- G8 remains forbidden before actual G7 authorization.

## Exact next gate

With Wm_S1 Track-A authority now closed, advance only to the next prospectively frozen Article-3 angular/prerequisite object consistent with the existing G7 order and ledgers. Do not re-run Exp073BJ and do not jump to G8. Before any new heavy angular successor, inspect the frozen task inventory and choose the next missing physical forward/power-input bridge or angular operator without duplicating an already-authoritative/provisional object.
