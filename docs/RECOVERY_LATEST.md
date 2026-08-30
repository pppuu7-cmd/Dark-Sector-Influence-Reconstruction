# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-30.  
**Strict Article-3 scientific repository readiness:** **52%**.  
**Article-2 repository-for-writing readiness:** **100%** for declared scope; not G7/G8/G9 closure.

## Read first

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
4. `recovery/2026-08-30_exp073aq_controlled_twin_wm_s1_launched.md`

Repository/hosted authority outranks chat wording. RTK/RQIR remain excluded from DSIR authority/readiness.

## Current authority state

- Historical primary P exact Wm_S0 SHA: `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`; historical-route authority only.
- Historical Q remains immutable `SCIENTIFIC_REPEATABILITY_FAIL`; this is computational repeatability, not dark-sector model physics.
- Exp073AM controlled single-thread exact repeatability PASS: run `33321661835`, artifact `9735051043`, canonical SHA `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`, exact A/B equality, +0 readiness.
- Exp073AN: `DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P`; run `33321762778`, +0 readiness.
- Exp073AO defines execution-qualified authority class `controlled_single_thread_exact_v1`; no tolerance/ULP/rounding contract is authorized.
- Exp073AP real hosted decision: `AUTHORIZE_EXECUTION_QUALIFIED_EXACT_SUCCESSOR_ROUTE`; run `33324664267`, artifact `9735869454`, +0 readiness.

## Successor exact contract

Controlled Wm_S0 anchor:

`8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`.

Every remaining angular task requires two independent hosted replicas under exact controls:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

Admission requires exact canonical SHA equality and `numpy.array_equal == True`. No tolerance, rounding, majority vote, preferred-replica selection or closeness-to-P rescue.

Remaining task order:

`Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

## Exp073AQ — first real controlled production gate

A duplicate audit found no active heavy workflow and no remaining-task production after Exp073AP. The first unexecuted task `Wm_S1` was therefore prospectively frozen and launched as two independent hosted replicas.

Frozen chain:

- prereg `2794ed0a48e8e7f8019584461296661d1a83ae08`;
- unchanged Exp073AA physical/angular runner `45ed8d8d1e90cdaf314e0384b6f3cdfef369925b`;
- superseding pre-freeze comparator `8772ff5550351d53dfa47aeb05cd83bd6f673750`;
- workflow `42b6241dc90a253cc4d4e8f8dbf72a6a71b46c18`;
- workflow freeze `a60c7a2020843e2ea800e361e54cb13ac6c39ac4`;
- trigger/head `fe89b6c64ee0cee5dbc40080973ec2af2ae683e0`.

Hosted run `33327372191` started `2026-08-30T18:12:00Z`.

Current jobs at latest inspection:

- replica A `99299799192`: IN PROGRESS;
- replica B `99299799338`: IN PROGRESS.

No final authority artifact exists yet.

The earlier comparator commit `64ae1eae3fc8902c0ec4368c2b7209be4fcbc67e` had a pre-freeze JSON-selection harness error and is not authority. It was superseded before trigger/output; exact criterion was unchanged.

Valid final classifications after both complete replicas reach the comparator are only:

- `PASS_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`, or
- `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Any failure before comparator classification remains infrastructure-INCOMPLETE.

A PASS admits only Wm_S1 into the future 14-window authority and adds **0 readiness**.

## Frozen Article-3 science boundaries

Unchanged:

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid row fraction `<=0.05` inclusive;
- final retained dimension `>=15`;
- genuine DES Y1, `NSIDE=4096`, PyMaster 2.7, true ell `0..12287`, 39 bandpowers;
- Wm `TE<-TE`, WW `EE<-EE`, canonical `<f8 [39,12288]`;
- positive absolute operator/window envelope only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no support/covariance/whitening/nuisance/quotient/relation/null/G8 leakage during angular construction;
- exact-threshold ambiguity remains unresolved.

## Current authorized order

`resolve Exp073AQ Wm_S1`

`-> if exact PASS, freeze/run Wm_S2 as its own controlled twin gate`

`-> continue remaining tasks only via independent exact twin admission`

`-> Exp073AM Wm_S0 + 13 admitted tasks -> ordered 14-window authority`

`-> real strict pre-support join under Exp073AE`

`-> immutable complete 1410-row finite-operator candidate manifest`

`-> real Layer A -> Layer B -> covariance/whitening -> nuisance/quotient/relation/null -> fresh G8`.

Strict Article-3 readiness remains **52%** until the real complete pre-support finite-operator candidate manifest exists.
