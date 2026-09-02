# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-02  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance/static/diagnostic QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `preregistration/2026-09-02_exp073ci_deterministic_fixed_dispatch_finalizer_v0_2.md`
2. `experiments/073ci_deterministic_fixed_dispatch_finalizer_v0_2_binding.json`
3. `ci/exp073ci_deterministic_fixed_dispatch_finalizer_v0_2.py`
4. `.github/workflows/exp073ci-deterministic-fixed-dispatch-finalizer-v0-2.yml`
5. `recovery/2026-09-02_exp073ch_finalizer_environment_dispatch_historical_b_reproduced.md`
6. `recovery/2026-09-02_exp073cf_continuation_successor_terminal_finalizer_exact_fail.md`
7. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Permanent scientific authority — Exp073CF

Exp073CF continuation successor run `33601943300` completed independent A/B full-scale Wm_S2 compact authority, 39/39 each.

Compact exact comparator job `100260974130` is a scoped PASS: canonical `<f8 [39,12288]` SHA A=B `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`; authority artifact `9848084775`, digest `sha256:29ac6e91f703734cfffcbffd1504fda9c861aa12dcb88822b83af50842983dd2`.

Frozen finalizer v0.1 exact repeatability is a permanent scientific FAIL: A W SHA `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`, B W SHA `bed762740b625f932f016d0988be17500a2583daee08bee9a5da550de786193e`; comparator job `100261645358`; token `SCIENTIFIC_REPEATABILITY_FAIL_EXP073CF_WM_S2_FINALIZER_EXACT_V0_1`; artifact `9848162380`, digest `sha256:f291447e109b2149958114baa30baf37edb6aa75efe9c2b41498d88fe4e193a1`. No tolerance/ULP/rounding/averaging/smoothing/preferred-replica/environment rescue may reclassify it.

## Diagnostic authority — Exp073CG / Exp073CH

Exp073CG run `33635554899`: four hosted workers exact-stable at K SHA `c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795`, W SHA historical-A `fc94c71...`; status `EXP073CG_DIAG_CROSS_HOST_EXACT_STABLE_NOT_REPRODUCED`; artifact `9848673390`, digest `sha256:5470b57030b42c6e9da71f3a056e84ddca783d55ca90e61a36ded4ce7a87a641`; diagnostic +0/+0.

Exp073CH run `33645970816` isolated native OpenBLAS solve dispatch and reproduced historical B exactly. Aggregate comparator job `100301228825`; artifact `9852842831`, digest `sha256:49528a12126cf0c9b83828f54d6b5543f82ee56dbbe0a477d8cd218cea766136`; status `EXP073CH_DIAG_HISTORICAL_B_SHA_REPRODUCED_BY_DISPATCH`; diagnostic +0/+0.

Exact dispatch evidence with identical compact input and identical K:
- native Zen (AMD R1/R2/R4) -> W `fc94c71...` historical A;
- native Cooperlake on R3, Intel Xeon Platinum 8573C -> W `bed76274...` historical B exactly;
- forced `Nehalem` -> W `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087` exactly across workers;
- forced `Sandybridge` -> W `85195fade822de2218a21840835c7b950a90eb1493fd42568e33ff4f36ed2f6a` exactly across workers;
- forced `Haswell` -> W `fc94c71...` exactly across workers.

Therefore historical Exp073CF A/B finalizer bit divergence is isolated to CPU-dependent/native OpenBLAS linear-solve kernel dispatch, not compact input or K construction.

## Current frontier — Exp073CI deterministic fixed-dispatch finalizer v0.2

Exp073CI is a NEW prospectively versioned exact-repeatability experiment. It cannot rewrite Exp073CF v0.1.

Frozen provenance:
- preregistration commit `1cf4ef96a44f26e7170d1ce6bd87c38dcc85cc7f`;
- helper commit `9f2f7870d912314e03f2f5725b07df12ace7fa92`;
- workflow commit `ca1af9bf17496e0f2bcb388356ea6a954844e2ef`;
- binding commit `835a916d5708d394cacc08c028cae1341e195868`;
- trigger/head commit `f8396c8e5e6b4a83340acf6ea0aaa262c9c71007`;
- run `33646799130`.

Prospective numerical contract:
- fixed `OPENBLAS_CORETYPE=Nehalem` selected as conservative fixed x86 dispatch, deliberately producing a new SHA distinct from both historical A and B rather than preferring either replica;
- exact expected K SHA `c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795`;
- exact expected v0.2 W SHA `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087`;
- immutable compact-A artifact `9841348367`, digest `sha256:d6703819745b22eadc9c6557c4d89d926ed9675c09bd41cb19e79d4050ef399b`;
- immutable compact-B artifact `9848067175`, digest `sha256:7e655144c07959f4ba7c6c6d82db0685b58e425958fa308e6b9e698ad6e30737`;
- 4 independent hosted `ubuntu-24.04` workers, 3 fresh-process solves per A/B artifact lane, exact-only comparator, no tolerance.

Current execution state:
- authorize job `100303472992`: PASS;
- R1 job `100303530655`: in progress;
- R2 job `100303530639`: in progress;
- R3 job `100303530782`: in progress;
- R4 job `100303530588`: in progress;
- compare job not yet eligible at this pointer update.

No self-hosted runner is used by Exp073CI. Unrelated legacy Exp073BT push checks may fail on repository writes; they have no Exp073CI scientific authority and do not alter this contract.

PASS token if every worker/lane/repeat matches exact frozen hashes: `PASS_EXP073CI_WM_S2_DETERMINISTIC_FIXED_NEHALEM_FINALIZER_EXACT_V0_2`. Otherwise valid complete exact mismatch is `SCIENTIFIC_REPEATABILITY_FAIL_EXP073CI_WM_S2_DETERMINISTIC_FIXED_NEHALEM_FINALIZER_EXACT_V0_2`; infrastructure failure before complete comparator inputs is nonclassifying.

## Preserved authority / boundaries

Exp073BJ Wm_S1 Track-A exact PASS; Exp073AQ permanent historical scientific FAIL; Exp073BD `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`; Exp073BV source-lineage PASS; Exp073BW streaming-equivalence PASS; Exp073BZ checkpoint/failover PASS; Exp073CC/CD/CE nonclassifying +0/+0; Exp073CF attempts1/2 infrastructure incomplete +0/+0; Exp073CF continuation compact scoped PASS + permanent finalizer v0.1 exact FAIL; Exp073CG/CH diagnostic +0/+0.

Frozen boundaries: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`.

Gate order remains `validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`. No G8 jump.

## Exact next gate

Consume Exp073CI run `33646799130` when terminal. Do not rerun or modify its frozen prereg/helper/workflow/binding/trigger while active. If all A/B lanes and all independent workers satisfy the prospective fixed-Nehalem exact comparator, record a NEW-version v0.2 exact repeatability PASS and then perform a frozen downstream semantic/criteria-binding audit before any readiness or G7 change. If valid exact mismatch occurs, record permanent v0.2 FAIL. If infrastructure fails before complete comparator inputs, classify infrastructure incomplete and repair prospectively only.

**Home runner = FREE. Verified 52.0% | Draft/data 53.7% | readiness delta +0/+0.**
