# DSIR recovery — Exp073CJ mixed-authority 14-window schema hosted PASS

**Date:** 2026-09-02  
**Classification:** hosted synthetic/governance PASS, non-scientific `+0/+0`.

## Purpose

After Wm_S2 v0.2 Track-A admission, the frozen Exp073AG v0.1 14-window aggregator schema was found to require `authority_class=exp073aa` for every non-Wm_S0 task. That would fail closed on the legitimate new Wm_S2 authority, whose accepted class is `exp073ci_v0_2`.

Exp073CJ v0.2 prospectively repairs only this provenance-class mismatch. It does not alter task order, numerical arrays, selected-component semantics, support rules, covariance, nuisance geometry, G7/G8/G9, or scientific readiness.

## Frozen chain

- preregistration: `preregistration/2026-09-02_exp073cj_14window_mixed_authority_aggregator_schema_v0_2.md`, commit `50509dfd654508e3c1d3edb51b64374f1e5b205e`;
- validator: `ci/exp073cj_article3_exact_14window_mixed_authority_schema_v0_2.py`, commit `b2bd80750c89a707727a49bd8032d2af7d53c6cb`;
- workflow: `.github/workflows/exp073cj-article3-exact-14window-mixed-authority-schema-v0-2.yml`, commit `10d8996edf88012a894867f6d57a742b3edd22e4`;
- binding: `experiments/073cj_article3_exact_14window_mixed_authority_schema_v0_2_binding.json`, commit `35c601751c738019feceddf81228b25add473088`;
- trigger/head: `efde40d160687fa39545fdbce816126c760b818b`.

## Hosted result

- run `33658754903`;
- job `100343790886`;
- conclusion `success`;
- artifact `9857796176`;
- artifact digest `sha256:1833e9e2a15bbd5938f1f786c10fa1d9822a040a763654299fc964506960af49`;
- PASS token `PASS_EXP073CJ_EXACT_14WINDOW_MIXED_AUTHORITY_SCHEMA_SYNTHETIC_V0_2`.

All prospective binding checks passed. The 20-case synthetic matrix passed. Non-scientific accounting enforcement passed.

## Frozen authority map v0.2

Exact ordered task list remains:

`Wm_S0, Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

Authority classes are now prospectively:

- `Wm_S0 -> canonical_exp073x2` only;
- `Wm_S2 -> exp073ci_v0_2` only;
- all other 12 tasks -> `exp073aa` only.

Wm_S2 v0.2 is bound to Exp073CI run `33646799130`, comparator job `100304043991`, artifact `9853165664`, digest `sha256:fcfccb6768948ffe34d28e9ed32da64d3b1d071704028fe6f312c1ab8b440f57`, selected W SHA `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087`.

Exp073CF v0.1 finalizer FAIL remains permanent and is not an accepted `exp073ci_v0_2` authority.

## Accounting / coordination

Exp073CJ itself is synthetic/governance `+0/+0`. Current Article-3 ledger remains:

`Verified 52.0% | Draft/data 54.6%` (exact Draft/data `54.57142857142857%`).

After completion, repository-wide DSIR Actions inspection found `0` queued and `0` in-progress runs. DSIR-HOME-PC remains FREE.

A separate legacy push-trigger workflow emitted a terminal failure on an intermediate governance commit with no jobs; it created no scientific authority, no artifact used here, and did not occupy the home runner.

## Exact next gate

The frozen task order shows the next missing angular task after admitted Wm_S0/Wm_S1/Wm_S2 is `Wm_S3`. Before any heavy Wm_S3 execution, inspect existing Exp073AA/Wm_S3 production history to ensure it has no valid complete authority already; then prospectively freeze a non-duplicative Wm_S3 successor only if actually missing. For any NEW self-hosted heavy workflow, apply the authorized staged `4 -> 6 -> 8` exact-equivalence plus RSS/swap safety preflight before freezing wider concurrency. No historical workflow may be altered.
