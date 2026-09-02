# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-02  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance/static/diagnostic QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-02_exp073ch_finalizer_environment_dispatch_historical_b_reproduced.md`
2. `preregistration/2026-09-02_exp073ch_finalizer_environment_dispatch_differential_v0_1.md`
3. `experiments/073ch_finalizer_environment_dispatch_differential_v0_1_binding.json`
4. `ci/exp073ch_finalizer_environment_dispatch_v0_1.py`
5. `.github/workflows/exp073ch-finalizer-environment-dispatch-differential-v0-1.yml`
6. `recovery/2026-09-02_exp073cf_continuation_successor_terminal_finalizer_exact_fail.md`
7. `recovery/2026-09-02_exp073cg_hosted_finalizer_cross_host_exact_stable_not_reproduced.md`
8. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Scientific authority — Exp073CF remains terminal FAIL at finalizer

Exp073CF continuation successor run `33601943300` reached complete A/B authority inputs; both A and B completed 39/39 bands on `DSIR-HOME-PC`.

The full-scale compact A/B comparator is an exact scoped PASS:
- comparator job `100260974130`;
- canonical shape `[39,12288]`;
- `array_equal=true`;
- compact canonical SHA A=B `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`;
- authority artifact `9848084775`, digest `sha256:29ac6e91f703734cfffcbffd1504fda9c861aa12dcb88822b83af50842983dd2`.

The frozen independent finalizers failed exact repeatability:
- final A W SHA `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`;
- final B W SHA `bed762740b625f932f016d0988be17500a2583daee08bee9a5da550de786193e`;
- final comparator job `100261645358`;
- token `SCIENTIFIC_REPEATABILITY_FAIL_EXP073CF_WM_S2_FINALIZER_EXACT_V0_1`;
- authority artifact `9848162380`, digest `sha256:f291447e109b2149958114baa30baf37edb6aa75efe9c2b41498d88fe4e193a1`.

This FAIL is permanent historical authority. No tolerance/ULP/rounding/averaging/smoothing/preferred-replica or environment rescue may reclassify it.

## Diagnostic authority — Exp073CG

Exp073CG run `33635554899` is terminal diagnostic/nonclassifying `+0/+0`. Four independent `ubuntu-24.04` workers were exact-stable and all produced K SHA `c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795` and W SHA equal to historical A `fc94c71...`. Status: `EXP073CG_DIAG_CROSS_HOST_EXACT_STABLE_NOT_REPRODUCED`. Authority artifact `9848673390`, digest `sha256:5470b57030b42c6e9da71f3a056e84ddca783d55ca90e61a36ded4ce7a87a641`.

## Current diagnostic result — Exp073CH isolates native BLAS dispatch

Exp073CH is a prospectively preregistered hosted-only diagnostic, `scientific_authority=false`, `+0/+0`.

Frozen provenance:
- preregistration commit `fe66db14ed621f2018ed64f43d11a0c713fee99d`;
- helper commit `79299e0e07f9993ef346a6d36a36dbd0bb789cac`;
- workflow commit `debf53af671ea51ab6c429c56a91b31836285b76`;
- binding commit `8450ee934af9bf4c43026d2a8f4fd7a290bea9d8`;
- trigger/head commit `063ab1ee804d0a4b4d36f843a5ae29e252f2db0d`;
- run `33645970816`.

Jobs:
- authorize `100300676816` success;
- R1 `100300734239` success;
- R2 `100300734241` success;
- R3 `100300734189` success;
- R4 `100300734176` success;
- aggregate comparator `100301228825` success.

Aggregate diagnostic authority artifact `9852842831`, digest `sha256:49528a12126cf0c9b83828f54d6b5543f82ee56dbbe0a477d8cd218cea766136`.

Terminal status: `EXP073CH_DIAG_HISTORICAL_B_SHA_REPRODUCED_BY_DISPATCH`.

All workers and regimes retained the exact K SHA `c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795`. Three fresh-process repeats per worker/regime were internally exact.

Native OpenBLAS dispatch separated by CPU/kernel:
- R1 AMD EPYC 7763, `Core: Zen` -> W SHA `fc94c71...` (historical A);
- R2 AMD EPYC 9V74, `Core: Zen` -> W SHA `fc94c71...`;
- R3 Intel Xeon Platinum 8573C, `Core: Cooperlake` -> W SHA `bed76274...` (**historical B exactly**);
- R4 AMD EPYC 9V74, `Core: Zen` -> W SHA `fc94c71...`.

Forced OpenBLAS core dispatch was cross-worker exact for each core and produced deterministic but core-dependent exact W hashes:
- `Nehalem` -> `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087`;
- `Sandybridge` -> `85195fade822de2218a21840835c7b950a90eb1493fd42568e33ff4f36ed2f6a`;
- `Haswell` -> `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`.

Therefore the historical A/B finalizer bit divergence is isolated to CPU-dependent/native OpenBLAS linear-solve kernel dispatch, with identical compact input and identical K. This diagnosis does not rewrite Exp073CF; it explains why its frozen exact-repeatability contract failed.

## Preserved scientific authority

- **Exp073BJ**: Wm_S1 Track-A exact PASS.
- **Exp073AQ**: permanent historical exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV** source-lineage PASS; **Exp073BW** streaming-equivalence PASS; **Exp073BZ** checkpoint/failover PASS.
- **Exp073CC/CD/CE**: synthetic/nonclassifying `+0/+0`.
- **Exp073CF attempt1/attempt2**: infrastructure incomplete `+0/+0`.
- **Exp073CF continuation successor**: compact exact scoped PASS; finalizer exact scientific repeatability FAIL.
- **Exp073CG/CH**: diagnostic/nonclassifying `+0/+0`.

## Frozen Article-3 order/boundaries

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order: `validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`. No G8 jump.

## Exact next gate

A **NEW prospectively versioned deterministic-finalizer experiment** is now permitted. It must be preregistered before execution, freeze one explicit BLAS dispatch contract instead of native CPU dispatch, use immutable compact authority inputs, run independent hosted workers/fresh processes, and demand exact equality with no tolerance. The dispatch choice must be justified prospectively by reproducibility/architecture rather than by choosing a preferred historical replica. Any PASS applies only to the new finalizer version and can never reclassify Exp073CF.

No self-hosted heavy computation is required for this gate.

- ✅ Exp073CF full-scale compact exact repeatability established.
- ❌ Exp073CF frozen finalizer exact repeatability permanently failed.
- ✅ Exp073CH reproduced historical B exactly and isolated native BLAS dispatch sensitivity.
- 🟡 New deterministic-finalizer contract not yet preregistered/executed.
- ❌ G7/G8 remain unauthorized.

**Home runner = FREE. Verified: 52.0% | Draft/data: 53.7% | readiness delta +0/+0.**
