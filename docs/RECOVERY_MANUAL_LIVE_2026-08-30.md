# DSIR RECOVERY MANUAL — live 2026-08-30 overlay

This file is the active-state overlay to the stable historical `docs/RECOVERY_MANUAL.md`. Use the historical manual for derivations and long-lived methodology, then this overlay, `docs/RECOVERY_LATEST.md`, the DSIR cross-chat consolidation, and the newest recovery checkpoint.

## Active state

- Article-2 repository-for-writing readiness: **100%** for declared scope; this does not close global G7/G8/G9.
- Strict Article-3 scientific repository readiness: **52%**.
- G7/G8/G9 = OPEN.
- Layer A/B = OPEN.
- covariance/whitening = BLOCKED until real Layer A and real Layer B pass in frozen order.
- synthetic/infrastructure/governance QA adds **0 scientific-readiness points**.
- DSIR remains independent of RTK/RQIR.

## Frozen Article-3 boundaries

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid observation-row fraction `<=0.05` inclusive;
- minimum final retained observation dimension `15`;
- DES classifying route `NSIDE=4096`;
- positive absolute operator/window envelopes only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance/whitening, nuisance SVD/rank, quotient/relation/null or G8 during support selection;
- exact-threshold numerical ambiguity remains `numerically_unresolved`.

## Established Article-3 prerequisite chain

Retain all categories distinctly:

- Exp073R1 real hosted DES source-mask reproduction — PASS/non-classifying authority.
- Exp073U immutable 1410-row observation skeleton — PASS/non-classifying.
- Exp073V broad-row support schema — PASS/non-classifying.
- Exp073W BOSS k-compatibility — PASS/non-classifying; downstream `54/240` support mask cannot select pre-support rows.
- Exp073Y exact DES released n(z) inventory — PASS/non-classifying.
- Exp073Z v0.1 — numerical implementation failure, not science.
- Exp073Z2 stable-direct DES radial authority — PASS/non-classifying.
- Exp073AB row-to-operator mapping — PASS/non-classifying.
- Exp073AD exact 5%-boundary QA — hosted synthetic PASS/+0.
- Exp073X — `INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`; partial Wm_S0 reuse forbidden.

## X2 angular frontier

### Primary P — real hosted repeatability authority now established

Original run `33300997298`:

- replica A job `99229007616`: completed success;
- replica B job `99229007666`: completed success;
- A artifact `9730411514`, digest `sha256:34530157cddf594c93728d5e092ab937d16a653665623f00513f4fd58df17555`;
- B artifact `9730409129`, digest `sha256:36358663fb1980ad75cb71f7ca7149d06d357cf7de8b29feca4273f4f88c89e5`.

The original aggregate job `99242068393` failed before comparison with:

`ModuleNotFoundError: No module named 'numpy'`.

Freeze that event as:

`INCOMPLETE_INFRASTRUCTURE_MISSING_NUMPY_BEFORE_REPEATABILITY_CLASSIFICATION`.

It is not a repeatability/scientific FAIL.

### Exp073X2R — narrow aggregator-only repair

Prospectively frozen before the repair downloaded/read P replica numerical contents:

- prereg `abe894465bacca43a758b8082923d1e0dbe54dfa`;
- unchanged comparator last-modifying commit `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`;
- workflow `bfcbebced87c1c982158d7e3783e0c82c6f501cc`;
- workflow freeze `bb564f48f710d7115eb35890b3a4cfd552d344c4`;
- trigger/head `f711f13bdeae2a0647ee9779dfe89d2025ba6c30`;
- hosted run `33305930375`, job `99242380374`;
- artifact `9730454167`;
- digest `sha256:f054b7fb30935f77fe7b187ba5130d23ebc99185c482e3682ae56b840ed5fea0`.

Allowed repair: install `numpy==2.1.3` only for the unchanged lightweight comparator. No workspace recomputation, comparator change, tolerance, alternate artifacts or changed science/angular semantics.

Hosted comparator result:

`PASS_EXP073X2_DES_N4096_WM0_MASK_ONLY_REPEATABILITY_V0_1`

Canonical primary P selected `Wm_S0` TE-window SHA256:

`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

The unchanged comparator established exact frozen-metadata equality, exact canonical SHA equality and `numpy.array_equal(A,B)==True` for `<f8 [39,12288]`.

Classification:

`REAL_HOSTED_NONCLASSIFYING_EXACT_WM_S0_REPEATABILITY_AUTHORITY_PASS_PLUS_0_READINESS`.

This is a real hosted angular authority PASS, not a scientific model/gate PASS. Support/covariance/nuisance/G8 remain unread; readiness stays 52%.

### Q contingency/redundant chain

- run `33301058260`;
- head `730ae4951ab8cd8e1dd2c392e991c3120345678a`;
- replica B job `99229177540`: completed success;
- B artifact `9730346824`, digest `sha256:a969aa3d04b2d2278d16e84e14ec2fbc046fc79c5bd1c63615e01c783592ce95`;
- replica A job `99229177604`: still in progress at latest audit;
- Q final authority: pending.

Binding governance now:

1. P is canonical and cannot be displaced.
2. If Q PASSes, Q canonical selected-window SHA must equal P SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`; disagreement blocks production.
3. If Q becomes infrastructure-INCOMPLETE, P may remain canonical and Exp073AF can release production.
4. If Q produces scientific/repeatability disagreement, production blocks.
5. Exp073AF blocks while Q remains PENDING.

No X2/X2R result alone raises readiness.

## Exp073AE — future real pre-support join firewall

Hosted synthetic PASS:

- run `33301598268`, job `99230706936`;
- artifact `9729115927`;
- digest `sha256:57a16aa9d95b13278f7abb2497edb9f1c8d5a6714612b35c43c5cc214e632117`;
- token `PASS_EXP073AE_ARTICLE3_PRESUPPORT_AUTHORITY_JOIN_SCHEMA_SYNTHETIC_V0_1`.

Classification: synthetic/governance QA only, +0 readiness.

Future real join must bind exact 14-window angular authority to Exp073U + Exp073Z2 + Exp073AB + Exp073W without support/covariance/nuisance/G8 leakage.

## Exp073AF — X2 -> Exp073AA release control

Hosted synthetic PASS:

- run `33302029344`, job `99231856970`;
- artifact `9729246776`;
- digest `sha256:adae6a7c4688674f41e32a0865971b1e92b5fac452371684376c07f5463b77a2`;
- token `PASS_EXP073AF_X2_TO_EXP073AA_RELEASE_CONTROL_SYNTHETIC_V0_1`.

Classification: synthetic/governance QA only, +0 readiness.

While Q is pending, Exp073AF blocks production even though P now PASSes.

If valid release occurs, exactly these 13 tasks may run:

`Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

`Wm_S0` is supplied only by canonical primary P with SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

## Exp073AG — exact 14-window authority aggregator schema

Prospectively frozen before remaining Exp073AA production release.

- prereg `2af44c322e03ce40882891a64c12e39b1e0a3564`;
- implementation `d49c8f43aa3ae3c6547864278fb9380720e61475`;
- workflow `61dded0fbd0cea8cc5218d6c46d570a873084c4d`;
- workflow freeze `80c381ccc2e16091a44649d475966244ca9cfe71`;
- trigger/head `1583760a13072628b307c216857dedc06748b19b`;
- hosted run `33303419856`, job `99235598024`;
- artifact `9729669260`;
- digest `sha256:71929dbc9eb77d59fbe5ad790d6c9cecfb236cefb457ab9a1dbd2e67d4a549c1`;
- token `PASS_EXP073AG_EXACT_14WINDOW_AUTHORITY_AGGREGATOR_SCHEMA_SYNTHETIC_V0_1`.

Classification: hosted synthetic PASS/+0 readiness.

The future real authority must contain exactly in order:

`Wm_S0, Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

## Authorized order from here

1. inspect Q run `33301058260` until its immutable outcome resolves;
2. apply frozen P/Q governance and Exp073AF release control;
3. if Q PASSes, require exact SHA equality with P canonical `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`;
4. if valid release occurs, execute exactly 13 remaining Exp073AA tasks;
5. build the real exact ordered 14-window authority under Exp073AG;
6. execute the real strict pre-support join under Exp073AE with Exp073U + Exp073Z2 + Exp073AB + Exp073W;
7. freeze the complete immutable 1410-row finite-operator candidate manifest;
8. only then execute real Layer A;
9. freeze `S_op` in inherited Exp073U order;
10. execute real Layer B;
11. only after both support layers PASS may covariance restriction and unrescued Cholesky whitening begin;
12. then nuisance representation/resolvability, signed SVD/rank, quotient/relation/null and fresh withheld-family G8 after G7 relation freeze.

No later-stage information may choose an earlier authority, threshold, representation, row set or support set. No scientific-readiness increase is authorized before the real complete pre-support finite-operator candidate manifest exists.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/RECOVERY_LATEST.md`
4. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
5. `recovery/2026-08-30_exp073x2r_primary_repair_pass_q_still_running.md`
6. `experiments/073x2r_article3_p_aggregator_numpy_infra_repair_v0_1_prereg.md`
7. `experiments/073af_article3_x2_to_exp073aa_release_control_v0_1_prereg.md`
8. `experiments/073ag_article3_exact_14window_authority_aggregator_schema_v0_1_prereg.md`
9. `experiments/073ae_article3_presupport_authority_join_schema_v0_1_prereg.md`.
