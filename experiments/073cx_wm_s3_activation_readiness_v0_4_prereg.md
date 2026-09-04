# Exp073CX v0.4 — data-bound final hosted activation-readiness audit

Status: prospectively frozen hosted support/integration gate, accounting `+0/+0`; no Wm_S3 science or Exp073BU activation occurs here.

Historical CX v0.1 A2, CX v0.2 A4 and CX v0.3 A2 remain immutable. v0.4 repairs only the v0.3 verifier's prose-phrase coupling for the frozen angular edges. All production arithmetic, source blobs, prerequisite authorities, anti-import firewall, checkpoint/comparator rules and science thresholds are unchanged.

Exact source bindings remain: BU prereg blob `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`; CW helper `f61b4e42ace7e2ab7220c0df0b38d8663136896c`; CV adapter `dafe86086a470c852106f0d4ecccbda1d389e397`; production A/B driver `5c8d5d3463e455389a1ca3df2639bf06a3b7b603`; CZ Z1 recovery `140b65be4901af3893a75f770ab20a9eed9f2f14`.

Immutable ancestor authorities remain exact: CW H1 commit `a763a83275c4105903b0dbee272a9ca72fc61ca0`; CV I1 commit `df49dcb50d5ccffb7b29d030ed8f1f99cbf4cdd6`; CZ Z1 commit `d0f70ac07707af960d2accd708ea1064fc05f523`, with the exact paths/tokens frozen by CX v0.3.

## Correct edge verifier
The exact edge authority is the numeric sequence `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`, length 40 defining 39 bands and ell `0..12287`. The auditor must verify this exact sequence in the exact production driver and verify the BU science prereg binds canonical `<f8 [39,12288]` / exact equality semantics. It must not score based on prose variants such as `39 bands` versus `39-band`.

All other v0.3 checks are frozen unchanged: direct anti-import firewall, exact A/B namespaces, six checkpoint stages, fail-closed identity, same-field PCL/workspace handoff, stock `write_to()`, no production `get_coupling_matrix()` materialization, exact mmap adapter, `TE<-TE`, SHA256 plus `numpy.array_equal`, no tolerance rescue, 8 outer workers and nested thread pins, immutable H1/I1/Z1 authorities, and hosted non-science flags.

Classifications remain `A1_EXP073BU_ACTIVATION_READINESS_PASS`, `A2_IMPLEMENTATION_CONTRACT_FAIL`, `A3_CHECKPOINT_FAILCLOSED_FAIL`, `A4_HISTORICAL_IMPORT_FAIL`, `A5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`. Only A1 permits a fresh live Actions noncompetition check before an explicit science activation.
