# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

## Frozen scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain 107 rows = DES 53 + BOSS 54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Full107, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global65537, statistical/model validity and physical dark-sector inference remain closed. Never rerun historical science run `35033268924`, successor v0.1 `35174721773`, successor v0.2 target `35181812498`, failed v0.2 lanes, or any same-identity attempt.

Historical control V0.13 run `34773514342` remains terminal success, run #1 / attempt #1; decision job `103769308584` remains success; decision artifact `10322573705` remains bound to digest `sha256:b04db83d530c36e03f2b80ad33fb4be80747817bd08cb2b001d5c8c6375fd202`; frozen classification remains `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`.

## Terminal predecessor chain

Response-blind GRID896 dispatch diagnostic `35177449482` established `GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED`. Successor v0.2 target `35181812498`, exact head `1fd68a9814ac987300710c4e67d080c7455efa34`, run #1 / attempt #1, terminated `SENTINEL_INVALID` before numerical/scientific evaluation. Terminal-history `35183519508` closed provenance; its single artifact `10480539101` remains Actions digest `sha256:0d61e9f90f03d875e8a67d99a7882530f44e5d6bd875d900c33391033c5fb329`. Numerical/exact-target/scientific/model layers remain `NOT_EVALUATED`.

Terminal successor-sentinel-v0.2 implementation qualification remains blob `fddc6e08d0bdedcb468a18f749e862ae7c813e38`, verdict `INVALID_IMPLEMENTATION`, classification `SUCCESSOR_SENTINEL_V0_2_PER_LANE_NATIVE_GRID896_MATERIALIZATION_NOT_HOST_INVARIANT`.

Frozen cross-host GRID896 design remains: prereg `903c80709439cb790bd41316029b218a77d5695b`; contract `6ba6e5a6c946a1091680f8f44821d323c9a463f3`; canonical source `24fa61685ab45e42e3ab0d453f5cb223c247ced6`; terminal preexecution confirmation `5f1a7dcaeb39dd093586eefb4f869cc0791ae715` (`CONFIRMED_SCOPED`). Canonical source is 897 lowercase u64hex words, source SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`; fixed little-endian payload is exactly 7176 bytes SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`; frozen one-bit negative control SHA256 is `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

Historical implementation V0.1 remains terminal `INVALID_IMPLEMENTATION`, authority blob `d9f940f3ea7b41b8df76d102f71ead16342a7f23`. Historical implementation V0.2 remains terminal `INVALID_IMPLEMENTATION`, authority blob `effd843587442f1c7bb3e9d7ae1c7ae6a8afd618`. Historical implementation V0.3 remains terminal `INVALID_IMPLEMENTATION`, authority blob `b20311d02c8fc0353e04c138b8ad4f121f4de0a2`. Historical implementation V0.4 remains terminal `INVALID_IMPLEMENTATION`, authority blob `f5d15887f88e6d9753e475d9c69572265babb2d6`, classification `GRID896_DIAGNOSTIC_SUCCESSOR_V0_4_DUPLICATE_RERUN_INVALID_CLASSIFIER_UNREACHABLE`.

## Implementation successor V0.5 — prospectively frozen inert candidate

V0.4 closed the V0.3 first-parent launch-chronology defect but had one terminal workflow-reachability defect: both matrix and decision jobs were gated by `run_number == 1 && run_attempt == 1`, so a rerun/duplicate invalid execution skipped the decision job before the frozen aggregate one-shot guard could durably emit `INVALID_DIAGNOSTIC_PROVENANCE`.

V0.5 prospectively corrects only that defect while preserving the frozen scientific/design contract and all surviving V0.4 controls.

Exact frozen V0.5 identities:
- executor `scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_5.py`, blob `224a4b8472c6aa0081627894d31cf967a2f2fc78`, creation commit `7cfb9ffdc600183795622242f5d67a80e539ea98`;
- inert workflow `docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-5.yml`, blob `f2134d3f80ead145aaae1c1203eac0626cf914f7`, creation commit `9fd9f9e2f16e52770a08babcb57eec58ebeff237`;
- implementation manifest `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_MANIFEST_V0_5.json`, blob `a19883ec25942664c89afe40b89ef5afa8cc8bf1`, creation commit `f57fc3ce537c7a4cf9f605cdc558cf8884c0f0dc`.

V0.5 lane execution remains one-shot gated to matching push/main + run #1 / attempt #1. The decision job now uses `always()` with matching push/main but deliberately omits the run-number/run-attempt job-level gate, while still `needs: grid896`. Therefore on attempt >1 or run number >1 the lane matrix is skipped but the decision job remains reachable; the unchanged aggregate one-shot guard writes `INVALID_DIAGNOSTIC_PROVENANCE`, the workflow uploads `grid896-cross-host-decision-v0-5`, and the final step reflects the frozen classifier without converting it to PASS.

V0.5 also preserves V0.4 `HEAD==GITHUB_SHA`, single-parent launch, exact authority/workflow unchanged in `HEAD^`, marker absence in `HEAD^`, marker-only first-parent diff, binary64 decode/immediate reserialize, canonical/hash/negative-control guards, exact 32-lane topology, artifact ZIP/API digest and inner-receipt bindings, present-evidence classifier precedence, and strict no-CLASS/no-science boundary.

At freeze, active V0.5 workflow `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-5.yml` is absent and launch marker `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_5.launch.json` is absent. No V0.5 diagnostic execution is authorized.

## Current authorization state

- frozen cross-host design: terminal `CONFIRMED_SCOPED`;
- implementation V0.1: terminal `INVALID_IMPLEMENTATION`;
- implementation V0.2: terminal `INVALID_IMPLEMENTATION`;
- implementation V0.3: terminal `INVALID_IMPLEMENTATION`;
- implementation V0.4: terminal `INVALID_IMPLEMENTATION`;
- implementation V0.5: `INERT_SUCCESSOR_IMPLEMENTATION_CANDIDATE_FROZEN_AWAITING_INDEPENDENT_STATIC_AUDIT`;
- exact historical failed V0.1–V0.4 blobs must not be rewritten;
- exact V0.5 blobs must not be changed during their audit;
- authorized next stage: **independent static audit of exact V0.5 executor/workflow/manifest only**;
- workflow promotion: **not authorized**;
- terminal implementation execution authority: **not authorized**;
- launch-marker creation: **not authorized**;
- diagnostic execution: **not authorized**;
- successor sentinel science: **not authorized**;
- full107/downstream science: **not authorized**.

## Funnel position / interpretation ceiling

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED -> V0.5 GOVERNANCE CLOSED -> SUCCESSOR V0.1 CONSUMED -> GRID896 DISPATCH DIAGNOSTIC TERMINAL -> SUCCESSOR V0.2 SENTINEL_INVALID -> V0.2 INVALID_IMPLEMENTATION -> CROSS-HOST GRID896 DESIGN PREREGISTERED -> PREEXECUTION DESIGN CONFIRMED_SCOPED -> IMPLEMENTATION V0.1 STATIC-AUDIT INVALID -> IMPLEMENTATION V0.2 STATIC-AUDIT INVALID -> IMPLEMENTATION V0.3 STATIC-AUDIT INVALID -> IMPLEMENTATION V0.4 STATIC-AUDIT INVALID -> IMPLEMENTATION V0.5 INERT CANDIDATE FROZEN -> INDEPENDENT STATIC AUDIT REQUIRED -> DIAGNOSTIC EXECUTION CLOSED -> SUCCESSOR SCIENCE CLOSED -> FULL107 CLOSED`.

Interpretation ceiling remains infrastructure/provenance/static implementation. Scientific effect remains `+0/+0`; numerical response reproducibility, exact-target/scientific criteria, covariance, statistical/model validity and physical dark-sector inference remain `NOT_EVALUATED`. No readiness/frontier percentage increase is authorized.

## Exact authorized next stage

`INDEPENDENT_STATIC_AUDIT_OF_EXACT_GRID896_DIAGNOSTIC_IMPLEMENTATION_SUCCESSOR_V0_5_ONLY`.

The audit must verify exact blobs `224a4b8472c6aa0081627894d31cf967a2f2fc78`, `f2134d3f80ead145aaae1c1203eac0626cf914f7`, and `a19883ec25942664c89afe40b89ef5afa8cc8bf1`; specifically prove that run #1/attempt #2, run number >1/attempt #1, and run number >1/attempt >1 skip all lanes but still run the decision and durably upload `INVALID_DIAGNOSTIC_PROVENANCE`, while only run #1/attempt #1 may execute lanes. Re-check all surviving V0.4 chronology/binary64/hash/artifact/classifier/no-science controls. Do not promote, create an authority/marker, execute diagnostic, rerun consumed identities, or open successor/full107/downstream science.
