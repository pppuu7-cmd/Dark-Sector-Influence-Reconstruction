# Recovery checkpoint — Article-3 dual readiness accounting frozen — 2026-08-31

## User-directed accounting change

The user requested two separate completion percentages so that strict scientific verification can remain conservative while provisional calculations produced on available compute can show practical manuscript/repository progress.

This checkpoint implements that request without changing any frozen Track-A scientific gate.

## Frozen values at checkpoint

- `SCIENTIFIC_AUTHORITY_READINESS = 52.0%`
- `DRAFT_DATA_READINESS = 53.714285714285715%` (display `53.7%`)

Dashboard shorthand:

`Verified: 52.0% | Draft/data: 53.7%`

## Why draft/data is 53.7%

A prospectively frozen operational denominator allocates the uncompleted 48 points across the declared downstream Article-3 production path. The 14-window angular data stage is worth 12 points, or `12/14 = 0.8571428571428571` points per complete usable angular object.

Currently usable angular objects for this metric:

1. Wm_S0 — complete controlled exact object from Exp073AM.
2. Wm_S1 — complete AQ A/B pair; exact AQ repeatability FAIL is preserved, while both complete branches are eligible only for provisional downstream sensitivity propagation under Exp073BB.

Thus `52 + 2*(12/14) = 53.714285714285715`.

No credit is currently awarded for later Layer-A/B/covariance/nuisance/G7/G8/G9 stages.

## Authority separation

This accounting does NOT:

- turn AQ into PASS;
- change strict 52%;
- relax exact comparator rules;
- admit provisional data into AR/AS/AT Track-A authority;
- permit preferred-replica selection;
- allow manuscript-final claims without later exact recomputation.

## Durable files

Created:

- `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`
  - creation commit `72e229c5ed9dcaf77e4155ff1a02be2b33c9c754`;
- `docs/RECOVERY_MANUAL_ADDENDUM_DUAL_READINESS_2026-08-31.md`
  - creation commit `421326b00d81f06190ab733c1f44f868ae142c56`.

Next recovery pointer update must list both percentages and link these files.

## Future reporting rule

After every substantive Article-3 computational/data step, report:

`Verified: XX.X% | Draft/data: YY.Y%`

Update `Draft/data` only from the frozen accounting document. Preserve exact history if it rises or falls. Track P remains non-authoritative and all its manuscript dependencies remain in the exact-recompute ledger.
