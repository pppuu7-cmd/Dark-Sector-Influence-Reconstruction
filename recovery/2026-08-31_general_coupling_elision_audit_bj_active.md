# DSIR recovery — 2026-08-31 — general-coupling elision audit; Exp073BJ active

**Scope:** DSIR Article-3 only. RTK/RQIR excluded.  
**Readiness:** `Verified 52.0% | Draft/data 53.7%`.  
**Audit effect:** `+0/+0`.

## Hosted authority snapshot

Exp073BJ run `33379013167` remains active. Jobs `99446854065` and `99446854363` both passed prospective freeze enforcement, exact NaMaster 2.7 lineage, immutable BI/AZ authority download, and exact BI_Q1 plus Exp073AZ canonical-PCL binding. Both remain in `Compute two-thread compact Wm_S1 replica`.

At this checkpoint no BJ compact artifacts and no frozen exact comparator output exist. Therefore no BJ scientific classification exists. Do not start a duplicate heavy BJ run and do not alter the active workflow.

## New independent result

`docs/ARTICLE3_GENERAL_COUPLING_ELISION_AUDIT_2026-08-31.md` records a nonclassifying public-API/structure audit of ways to avoid the dense full-scale general-coupling materialization.

For `nl=12288`, one scalar dense float64 `nl x nl` matrix is `150,994,944` doubles = `1,207,959,552` bytes = `1.125 GiB` before overhead. The retained `[39,12288]` compact projected payload is only about `3.66 MiB`, roughly 315x smaller by storage.

The audit rejects two superficially attractive routes:

- chunking/slicing *after* documented `get_general_coupling_matrix` cannot remove the original dense construction, because the public API has already materialized the full returned matrix;
- documented `NmtWorkspace.couple_cell` applies coupling through an already constructed workspace and is not a documented block/row construction iterator.

No documented public block/row streaming interface for `get_general_coupling_matrix` was found. A direct band-projected/native accumulator is therefore only a future hypothesis. It must receive prospective source-level provenance and exact code-equivalence/repeatability qualification before any classifying full-scale successor. Merely reducing retained storage does not prove runtime reduction if the native implementation still evaluates all coupling elements.

This result is consistent with the existing local numerical-structure audit: provisional real-DES Wm_S2 has `cond_2(K)=2.1928888836909883`, so the small 39x39 finalizer solve is not the observed multi-hour bottleneck.

## Frozen classifications preserved

- Exp073AQ remains permanent historical exact-repeatability scientific FAIL.
- Exp073BA remains infrastructure execution incomplete, no scientific classification.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`.
- Exp073BI remains synthetic/infrastructure `BI_Q1_PARALLEL_EXACT_QA_PASS`, `+0/+0`.
- Exp073BJ exact scientific decision rules remain untouched: two complete valid compact inputs are required; exact mismatch is scientific repeatability FAIL; cancellation/timeout/incomplete before two valid comparator inputs is infrastructure execution incomplete with no scientific classification; only exact compact PASS may admit both finalizers and final exact authority.
- No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue.
- Synthetic/infrastructure/provenance/numerical-structure work gives `+0` scientific readiness.
- Article-3 anti-leakage firewall and required G7 order remain unchanged. G8 remains forbidden before actual G7 authorization.

## Provenance from this iteration

- general-coupling elision audit commit: `fe251ac43870efa79e578af9f07d5ba7bff78d55`;
- hosted BJ run: `33379013167`;
- BJ compact jobs: A `99446854065`, B `99446854363`.

## Exact next gate

Re-inspect Exp073BJ jobs and artifacts. When both compact jobs become terminal, preserve and consume the frozen exact compact comparator classification before any supplementary diagnostic. Only exact compact PASS permits both finalizers. After BJ classification is durably preserved and a valid compact/final Wm_S1 payload exists, run/reproduce `ci/article3_window_structure_diagnostic_v0_1.py` as strictly nonclassifying `+0/+0` and report `cond_2(K)`, singular values, `WQ-I`, and `KW-A` residuals.
