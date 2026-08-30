# DSIR recovery checkpoint — Exp073X2R primary repaired repeatability PASS, Q still running

**Date:** 2026-08-30  
**Project:** Dark-Sector Influence Reconstruction (DSIR)

## Scientific-accounting headline

- Strict Article-3 scientific repository readiness: **52%**.
- Exp073X2R contributes **0 readiness points**.
- G7/G8/G9 = OPEN.
- Layer A/B = OPEN.
- covariance/whitening = BLOCKED.
- DSIR remains independent of RTK/RQIR.

## 1. Fresh audit of the previous primary X2 state

Primary Exp073X2 run `33300997298` changed materially since the previous recovery pointer:

- replica A job `99229007616`: **completed success**;
- replica B job `99229007666`: **completed success**;
- replica A artifact `9730411514`, digest `sha256:34530157cddf594c93728d5e092ab937d16a653665623f00513f4fd58df17555`;
- replica B artifact `9730409129`, digest `sha256:36358663fb1980ad75cb71f7ca7149d06d357cf7de8b29feca4273f4f88c89e5`;
- aggregate job `99242068393`: **failed before classification**.

Exact aggregate failure from hosted logs:

`ModuleNotFoundError: No module named 'numpy'`.

The failure happened while importing the unchanged comparator, before either replica was loaded and before frozen metadata, canonical hashes or `numpy.array_equal` were compared.

Therefore the original aggregate failure is classified as:

`INCOMPLETE_INFRASTRUCTURE_MISSING_NUMPY_BEFORE_REPEATABILITY_CLASSIFICATION`.

It is neither repeatability/scientific FAIL nor PASS.

## 2. Prospectively frozen aggregator-only repair — Exp073X2R

Because both expensive P replicas were already immutable hosted artifacts and the aggregate failure was a missing runtime dependency before comparison, a narrow infrastructure repair was frozen **before the repair path downloaded/read replica numerical contents**.

Frozen chain:

- prereg `experiments/073x2r_article3_p_aggregator_numpy_infra_repair_v0_1_prereg.md`
  - commit `abe894465bacca43a758b8082923d1e0dbe54dfa`;
- unchanged comparator `ci/exp073x2_compare_replicas_v0_1.py`
  - last-modifying commit `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`;
- repair workflow `.github/workflows/exp073x2r-article3-p-aggregator-numpy-infra-repair-v0-1.yml`
  - commit `bfcbebced87c1c982158d7e3783e0c82c6f501cc`;
- workflow freeze `experiments/073x2r_article3_p_aggregator_numpy_infra_repair_v0_1_workflow_freeze.md`
  - commit `bb564f48f710d7115eb35890b3a4cfd552d344c4`;
- trigger/head `ci/exp073x2r_article3_p_aggregator_numpy_infra_repair_v0_1.trigger`
  - commit `f711f13bdeae2a0647ee9779dfe89d2025ba6c30`.

Allowed change was only installation of `numpy==2.1.3` for the lightweight comparator. No workspace recomputation, comparator modification, tolerance, alternate artifacts or changed scientific/angular contract was allowed.

## 3. Hosted repaired primary authority

Exp073X2R hosted run:

- run `33305930375`;
- job `99242380374`;
- result: **success**;
- artifact `9730454167`;
- artifact digest `sha256:f054b7fb30935f77fe7b187ba5130d23ebc99185c482e3682ae56b840ed5fea0`.

The hosted workflow verified exact immutable P artifact IDs/names/digests/run/head bindings, installed only the missing NumPy runtime, downloaded the exact two P replica artifacts, and executed the unchanged frozen comparator exactly once.

Comparator result:

`PASS_EXP073X2_DES_N4096_WM0_MASK_ONLY_REPEATABILITY_V0_1`

Canonical selected Wm_S0 TE window SHA256:

`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`

The unchanged comparator established:

- exact frozen metadata equality;
- canonical SHA equality;
- `numpy.array_equal(A,B) == True`;
- selected window shape `[39,12288]`;
- Article-3 readiness remains `52`;
- G7/G8/G9 remain OPEN;
- physical support/covariance/G8 remain unread/unscored.

Classification:

`REAL_HOSTED_NONCLASSIFYING_EXACT_WM_S0_REPEATABILITY_AUTHORITY_PASS_PLUS_0_READINESS`.

This is a real hosted angular-operator repeatability authority, but it is **not** a scientific model/gate PASS.

## 4. P/Q governance after the repair

Under the already-frozen authority rule, primary Chain P is now a valid repeatability PASS with canonical Wm_S0 hash:

`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

However Exp073AA production is still blocked by Exp073AF because Chain Q has not resolved.

Latest Q state at this checkpoint:

- run `33301058260`;
- replica B job `99229177540`: **completed success**;
- replica B artifact `9730346824`, digest `sha256:a969aa3d04b2d2278d16e84e14ec2fbc046fc79c5bd1c63615e01c783592ce95`;
- replica A job `99229177604`: **still in progress** inside exact workspace computation;
- Q aggregate/final authority: not yet available.

Therefore the frozen Exp073AF rule `P PASS + Q PENDING -> BLOCK_PRODUCTION` applies.

No Exp073AA production task was launched.

## 5. Frozen scientific boundaries unchanged

Never change post hoc:

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid observation-row fraction `<=0.05` inclusive;
- minimum final retained observation dimension `15`;
- DES classifying route `NSIDE=4096`;
- positive absolute operator/window envelope only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance/whitening, nuisance SVD/rank, quotient/relation/null or G8 during support selection;
- exact-threshold numerical ambiguity remains unresolved.

## 6. Authorized next order

1. inspect Q run `33301058260` until its immutable outcome is available;
2. apply the already-frozen P/Q governance and Exp073AF release control;
3. if Q PASSes, require Q canonical Wm_S0 SHA to equal P canonical SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f` before production;
4. if Q becomes infrastructure-INCOMPLETE, P remains canonical and Exp073AF may release the exact remaining 13 tasks;
5. if Q produces a scientific/repeatability disagreement, production remains blocked;
6. after valid release, execute exactly the frozen 13 Exp073AA tasks;
7. aggregate canonical P Wm_S0 + 13 under Exp073AG;
8. perform the real strict pre-support join under Exp073AE;
9. freeze the complete immutable 1410-row finite-operator candidate manifest;
10. only then run real Layer A.

Strict Article-3 scientific repository readiness remains **52%** until the real complete pre-support finite-operator candidate manifest exists.
