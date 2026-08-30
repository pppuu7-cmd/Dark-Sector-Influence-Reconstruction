# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-30.  
**Strict Article-3 scientific repository readiness:** **52%**.  
**Article-2 repository-for-writing readiness:** **100%** for declared scope; this is not G7/G8/G9 closure.

## Read first

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
4. `recovery/2026-08-30_exp073x2r_primary_repair_pass_q_still_running.md`

Repository/hosted authority outranks earlier chat wording. RTK/RQIR remain excluded from DSIR authority/readiness.

## Current headline state

- Exp073R1: real hosted DES source-mask reproduction **PASS / non-classifying authority**.
- Exp073U: immutable 1410-row observation skeleton **PASS / non-classifying**.
- Exp073V: broad-row support schema **PASS / non-classifying**.
- Exp073W: BOSS k-compatibility **PASS / non-classifying**; downstream `54/240` mask may not select pre-support candidates.
- Exp073Y: exact DES released n(z) inventory **PASS / non-classifying**.
- Exp073Z v0.1: **NUMERICAL IMPLEMENTATION FAILURE, NOT SCIENCE**.
- Exp073Z2: stable-direct DES radial authority **PASS / non-classifying**.
- Exp073AB: row-to-operator mapping **PASS / non-classifying**.
- Exp073AD: exact 5%-boundary QA **HOSTED SYNTHETIC PASS / +0 readiness**.
- Exp073X: `INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`; partial Wm_S0 reuse forbidden.
- Exp073X2 original P aggregate job `99242068393`: `INCOMPLETE_INFRASTRUCTURE_MISSING_NUMPY_BEFORE_REPEATABILITY_CLASSIFICATION`; not repeatability FAIL.
- Exp073X2R repaired primary P authority: **REAL HOSTED NONCLASSIFYING REPEATABILITY PASS / +0 readiness**, run `33305930375`, job `99242380374`, artifact `9730454167`, digest `sha256:f054b7fb30935f77fe7b187ba5130d23ebc99185c482e3682ae56b840ed5fea0`.
- canonical primary P `Wm_S0` selected-window SHA256: `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.
- Exp073X2 Q run `33301058260`: replica B completed/persisted; replica A still in progress at latest audit; Q authority pending.
- Exp073AE: pre-support real-join schema **HOSTED SYNTHETIC PASS / +0**.
- Exp073AF: X2->Exp073AA release control **HOSTED SYNTHETIC PASS / +0**.
- Exp073AG: exact ordered 14-window authority aggregator schema **HOSTED SYNTHETIC PASS / +0**.
- Exp073AA production remains **BLOCKED** by frozen Exp073AF rule `P PASS + Q PENDING -> BLOCK_PRODUCTION`.
- Layer A = OPEN; Layer B = OPEN; covariance/whitening = BLOCKED; G7/G8/G9 = OPEN.

## Primary P repair provenance

Primary run `33300997298` produced two successful immutable replicas:

- A job `99229007616`, artifact `9730411514`, digest `sha256:34530157cddf594c93728d5e092ab937d16a653665623f00513f4fd58df17555`;
- B job `99229007666`, artifact `9730409129`, digest `sha256:36358663fb1980ad75cb71f7ca7149d06d357cf7de8b29feca4273f4f88c89e5`.

Its original aggregator never reached comparison because the runner lacked NumPy. Exp073X2R was prospectively frozen before the repair path downloaded/read the replica numerical contents and allowed only `numpy==2.1.3` installation plus execution of the unchanged comparator at commit `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`.

Frozen repair chain:

- prereg `abe894465bacca43a758b8082923d1e0dbe54dfa`;
- workflow `bfcbebced87c1c982158d7e3783e0c82c6f501cc`;
- workflow freeze `bb564f48f710d7115eb35890b3a4cfd552d344c4`;
- trigger/head `f711f13bdeae2a0647ee9779dfe89d2025ba6c30`;
- hosted run `33305930375`, job `99242380374`;
- artifact `9730454167`, digest `sha256:f054b7fb30935f77fe7b187ba5130d23ebc99185c482e3682ae56b840ed5fea0`;
- comparator token `PASS_EXP073X2_DES_N4096_WM0_MASK_ONLY_REPEATABILITY_V0_1`;
- canonical Wm_S0 SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

The unchanged comparator established exact frozen-metadata equality, exact canonical SHA equality and `numpy.array_equal(A,B)==True`. This is an angular-operator repeatability authority only; support/covariance/G8 were not evaluated and readiness remains 52%.

## Frozen Article-3 boundaries

Never change post hoc:

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid observation-row fraction `<= 0.05` inclusive;
- final retained observation dimension `>=15`;
- DES classifying route `NSIDE=4096`;
- positive absolute operator/window envelope only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance, whitening, nuisance SVD/rank, quotient/relation/null or G8 during support selection;
- exact-threshold numerical ambiguity remains unresolved, never rounded to PASS/FAIL.

## X2 governance now

P is primary and now has valid hosted repeatability authority with canonical SHA `6ec29f6d...18d0f`. Q remains prospectively governed contingency/redundant run `33301058260`.

1. P remains canonical; Q cannot displace it.
2. If Q PASSes, Q canonical hash must equal P hash or production blocks.
3. If Q becomes infrastructure-INCOMPLETE, P may remain canonical and Exp073AF can release production.
4. If Q produces a scientific/repeatability disagreement, production blocks.
5. Exp073AF blocks while Q is PENDING.

No X2/X2R result alone raises readiness.

## Exact remaining 13 Exp073AA tasks after valid release

`Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

`Wm_S0` is canonical P X2 authority with SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

## Authorized next order

`resolve real Q outcome`

`-> apply frozen P/Q governance + Exp073AF`

`-> if released, execute exactly 13 Exp073AA tasks`

`-> build real exact ordered 14-window authority under Exp073AG`

`-> real strict pre-support join under Exp073AE with Exp073U + Exp073Z2 + Exp073AB + Exp073W`

`-> immutable complete 1410-row finite-operator candidate manifest`

`-> real Layer A`

`-> freeze S_op`

`-> real Layer B`

`-> only after Layer A/B PASS: covariance restriction + unrescued Cholesky whitening`

`-> representation/resolvability-controlled nuisance SVD/rank -> signed quotient/relation/null -> fresh withheld-family G8 after G7 relation freeze`.

While Q remains active, do not launch another X2 or any Exp073AA production task. No scientific-readiness increase is authorized before the real complete pre-support finite-operator candidate manifest exists.
