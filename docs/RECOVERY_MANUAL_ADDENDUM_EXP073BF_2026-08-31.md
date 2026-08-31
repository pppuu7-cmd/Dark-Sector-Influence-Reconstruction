# DSIR Recovery Manual Addendum — Exp073BF Wm low-memory stock-equivalence QA

**Date:** 2026-08-31  
**Scope:** DSIR Article 3 / G7 pre-support angular route only. RTK/RQIR excluded.

## Why this addendum exists

At this checkpoint two heavy workflows are already active and must not be duplicated:

- Exp073BA clean Track-A Wm_S1 low-memory production run `33345968620`;
- Exp073BD Track-P provisional Wm_S2 twin run `33342265114`.

The BA implementation's existing small-scale self-test covers the spin-2 x spin-2 WW algebra but does not independently exercise the Wm spin-0 x spin-2 path used by BA. Exp073BF fills only that implementation-QA gap while the heavy runs continue.

## Frozen Exp073BF identity

- prereg commit: `99db0c8b7444ade7eb65df7626398a034bf16fda`;
- hosted workflow commit: `bbb4ecb14c01d2d7bafe37f0ae01377b2d81223b`;
- trigger/head commit: `47fab566ac115b83745fffdd60db8f937e043621`;
- hosted run: `33349183295`.

Frozen test: NaMaster 2.7, NSIDE=16, deterministic synthetic spin-0 and spin-2 masks, fixed edges `[0,4,8,16,24,32,48]`. It compares stock `NmtWorkspace` selected `TE <- TE` windows with the same general-coupling -> fixed-order compression -> fixed-order K -> solve route used by Exp073BA, and independently checks exact repeatability of two same-input `get_general_coupling_matrix(PCL,0,2,0,2)` calls.

QA acceptance was prospectively frozen at `max_abs(stock-reconstructed) < 1e-12` plus exact same-input G02 repeatability and finite/shape checks. This `1e-12` value is synthetic implementation QA only and must never be imported into scientific exact comparators.

## Terminal hosted result

Hosted run `33349183295` completed successfully on 2026-08-31 under Ubuntu 24.04 with the frozen single-thread controls and NaMaster/PyMaster 2.7.

Terminal token:

`PASS_EXP073BF_WM_STOCK_EQUIVALENCE_QA_V0_1`

Frozen-result facts:

- stock selected-window shape: `[6,48]`;
- reconstructed selected-window shape: `[6,48]`;
- all values finite: `true`;
- `max_abs(stock-reconstructed) = 8.326672684688674e-16`, below the prospectively frozen synthetic-QA threshold `1e-12`;
- two same-input `get_general_coupling_matrix(PCL,0,2,0,2)` calls were bitwise/exactly equal: `true`;
- stock SHA-256: `4699aea68c2e6c6bb0ff3d5938bb5bda18352e0287f093ea7b8c133af36ec35c`;
- reconstructed SHA-256: `fcd98c4bb21be5dda8dc1cf6d33971a5d4e33333ebaf0fb4e122e8d789c0fb3e`;
- authority artifact ID: `9743025349`;
- artifact digest: `sha256:b39c8449f1752c4f7cd985829620da82be4de86fde8f135206453c91baddf9b1`.

Classification remains **synthetic numerical/infrastructure QA only**. This is evidence that the low-memory Wm spin-0 x spin-2 algebra reproduces stock NaMaster at the frozen small-scale QA level and that repeated same-input G02 generation is exact within this hosted invocation. It is not a scientific Wm_S1 PASS and is not evidence that independent production runners will be bitwise identical.

## Authority/accounting firewall

Exp073BF can only classify implementation/numerical QA. It cannot:

- repair or reinterpret Exp073AQ;
- classify Exp073BA scientific outputs;
- authorize Wm_S2 Track A;
- authorize Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7 closure or G8;
- change frozen scientific thresholds;
- add scientific or draft/data readiness.

Thus after terminal Exp073BF:

`Verified: 52.0% | Draft/data: 53.7%`

Exp073AQ remains permanently:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

No tolerance/rounding/ULP/preferred-replica reinterpretation is permitted.

## Recovery order

1. Inspect Exp073BA run `33345968620`; at the latest check both compact replicas had passed exact AZ binding and remained inside `Compute low-memory compact Wm_S1 replica`. There was no BA artifact yet. Consume exact compact comparator/finalizer authority before any Track-A succession.
2. Inspect Exp073BD run `33342265114`; at the latest check both provisional branches remained inside `Compute independent Wm_S2 provisional branch`, with no artifacts yet. Preserve both branches and never choose a preferred branch.
3. Exp073BF is now terminal PASS for synthetic QA only; do not rerun it merely to seek a more favorable numerical difference.
4. Do not start another heavy Wm_S1/Wm_S2 control plane while BA/BD remain active.
5. Exp073AQ remains permanent exact-repeatability FAIL.
6. G7 order remains physical forward/power bridges -> support-validity mask -> Layer A/B -> covariance/whitening -> nuisance SVD -> quotient/relation/null -> G7 authorization -> fresh G8.