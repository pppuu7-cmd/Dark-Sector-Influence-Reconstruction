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

QA acceptance is prospectively frozen at `max_abs(stock-reconstructed) < 1e-12` plus exact same-input G02 repeatability and finite/shape checks. This 1e-12 value is synthetic implementation QA only and must never be imported into scientific exact comparators.

## Authority/accounting firewall

Exp073BF can only classify implementation/numerical QA. It cannot:

- repair or reinterpret Exp073AQ;
- classify Exp073BA scientific outputs;
- authorize Wm_S2 Track A;
- authorize Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7 closure or G8;
- change frozen scientific thresholds;
- add scientific or draft/data readiness.

Thus throughout this addendum:

`Verified: 52.0% | Draft/data: 53.7%`

## Recovery order

1. Inspect Exp073BA run `33345968620`; if compact replicas complete, consume exact compact comparator/finalizer authority before any Track-A succession.
2. Inspect Exp073BD run `33342265114`; preserve both branches, never choose a preferred branch.
3. Inspect Exp073BF run `33349183295`; record PASS/FAIL strictly as synthetic numerical/infrastructure QA with `+0/+0`.
4. Do not start another heavy Wm_S1/Wm_S2 control plane while BA/BD remain active.
5. Exp073AQ remains permanent exact-repeatability FAIL.
6. G7 order remains physical forward/power bridges -> support-validity mask -> Layer A/B -> covariance/whitening -> nuisance SVD -> quotient/relation/null -> G7 authorization -> fresh G8.