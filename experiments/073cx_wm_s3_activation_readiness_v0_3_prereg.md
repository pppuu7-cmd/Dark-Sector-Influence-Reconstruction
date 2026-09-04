# Exp073CX v0.3 — authority-bound Wm_S3 activation-readiness audit

Status: prospectively frozen hosted support/integration gate. Accounting `+0/+0`. This gate cannot create Wm_S3 scientific authority or activate Exp073BU.

## Immutable history
CX v0.1 remains `A2_IMPLEMENTATION_CONTRACT_FAIL`. CZ v0.1 remains `Z2_IMPLEMENTATION_CONTRACT_FAIL` from its verifier-scope defect. CZ v0.2 is authoritative `Z1_UNIFIED_PRODUCTION_AB_DRIVER_INTEGRATION_PASS`. CX v0.2 remains immutable `A4_HISTORICAL_IMPORT_FAIL`; its first causal defect was auditor literal coupling, not observed numerical import. v0.3 is a prospective auditor repair only; production arithmetic and science criteria remain unchanged.

## Exact current-source bindings
The auditor must bind exactly:
- Exp073BU prereg blob `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`;
- Exp073CW helper blob `f61b4e42ace7e2ab7220c0df0b38d8663136896c`;
- Exp073CV adapter blob `dafe86086a470c852106f0d4ecccbda1d389e397`;
- unified production A/B driver blob `5c8d5d3463e455389a1ca3df2639bf06a3b7b603`;
- CZ v0.2 recovery blob `140b65be4901af3893a75f770ab20a9eed9f2f14`.

## Immutable prerequisite authorities
The auditor must fetch/verify these exact ancestor commits and their exact recovery paths:
- CW H1 authority: commit `a763a83275c4105903b0dbee272a9ca72fc61ca0`, path `recovery/2026-09-04_exp073cw_v0_1_h1_single_mask_integrated_driver_pass.md`, containing `H1_SINGLE_MASK_INTEGRATED_DRIVER_PASS`, run/job `33860891989 / 100984835847`, artifact `9932088071`, and `historical_wm_s3_numerical_import=false`.
- CV I1 authority: commit `df49dcb50d5ccffb7b29d030ed8f1f99cbf4cdd6`, path `recovery/2026-09-04_exp073cv_v0_3_i1_exact_production_integration_pass.md`, containing `I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS`, run/job/head `33847132443 / 100941396500 / 77cc6ba35aac41d2f6af12c7b865787db2bb3e44`, artifact `9926971841`, and `historical_wm_s3_numerical_import=false`.
- CZ Z1 authority: commit `d0f70ac07707af960d2accd708ea1064fc05f523`, path `recovery/2026-09-04_exp073cz_v0_2_z1_scoped_driver_integration_pass.md`, containing `Z1_UNIFIED_PRODUCTION_AB_DRIVER_INTEGRATION_PASS`, run/job/head `33871304159 / 101017678531 / b7cc90467006718a115b4dba40962cc8275f1c69`, artifact `9935990587` and raw receipt SHA256 `03938c3b2f2759a60be1f4d5bfdd6eb23018e9507e0a6688ba20364e02eaa5b1`.

Each authority commit must be an ancestor of the audited source head. Hosted checkout therefore uses full history.

## Frozen anti-import firewall
`no_historical_import` is true only if the exact production driver explicitly sets `historical_wm_s3_numerical_import` false and `other_replica_output_read` false, and the driver contains no references to historical Wm_S3 numerical-route identifiers `exp073cr`, `exp073cq`, or `exp073cm` (case-insensitive). It MUST NOT depend on whether those literal names are restated in this preregistration.

## Other readiness checks
Unchanged from the frozen science contract: exact 39-band edges ending at 12288; A/B namespaces `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`; six ordered durable stages; fail-closed source-head/contract/namespace/payload identity; same fresh field pair for PCL/workspace; stock `write_to()` and no production `get_coupling_matrix()` materialization; admitted exact mmap route and `TE<-TE`; final whole selected-TE SHA256 equality AND `numpy.array_equal`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue; `OUTER_COMPUTE_WORKERS=8` with nested OMP/OpenBLAS/MKL/NumExpr threads pinned to 1. Hosted audit executes no DES-scale science and keeps `science_gate_scored=false`, `wm_s3_authority_created=false`, `exp073bu_activated=false`.

## Frozen classification
- `A1_EXP073BU_ACTIVATION_READINESS_PASS`: all exact source, immutable-authority, anti-import, checkpoint, production and comparator checks pass.
- `A2_IMPLEMENTATION_CONTRACT_FAIL`: production/composition contract inconsistent.
- `A3_CHECKPOINT_FAILCLOSED_FAIL`: checkpoint/isolation/comparator fail-closed contract insufficient.
- `A4_HISTORICAL_IMPORT_FAIL`: direct anti-import firewall fails.
- `A5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: source/blob/ancestor/authority/audit infrastructure failure.

Only A1 permits a subsequent fresh live Actions noncompetition check and explicit activation step. A1 itself is not Wm_S3 science.
