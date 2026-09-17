# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions state, frozen authorities and terminal artifacts are authoritative; chat is not authority.

## Frozen scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen under prereg blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain 107 rows = DES53+BOSS54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Full107, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global65537, statistical/model validity and physical dark-sector inference remain closed. Never rerun historical/same-identity runs including `35033268924`, `35174721773`, `35181812498`, failed v0.2 lanes, and V0.6 run `35251121404`.

## Terminal predecessor chain

V0.13 remains terminal `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`. Response-blind GRID896 dispatch diagnostic `35177449482` established `GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED`. Successor v0.2 `35181812498` terminated `SENTINEL_INVALID` before science with 10 eligible lanes, all `NATIVE_AVX512_ACTIVE`, and zero inactive. Numerical/scientific/model layers remained `NOT_EVALUATED`.

Frozen cross-host GRID896 design: prereg `903c80709439cb790bd41316029b218a77d5695b`; contract `6ba6e5a6c946a1091680f8f44821d323c9a463f3`; canonical Git blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`; preexecution confirmation `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`; packed payload 7176 bytes SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`; negative-control SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

Implementations V0.1–V0.5 remain terminal `INVALID_IMPLEMENTATION`.

## V0.6 execution history — closed

V0.6 exact executor blob `eae9eee7ae6a1424bcac67279663a2c8ddd3ebf9`; active workflow blob `832f0491421619579c2a1d77ba9ca339cb4898ac`. Read-only registry capture `35247378034` bound workflow ID `360576929`, exact canonical path and state `active`; registry result blob `033c9df4fde1feecd6cd1a75e1feb9abb9dc3013`, confirmation blob `6c92403f487a4fe487a942e426930134c7c0b949`.

V0.6 one-shot execution authority blob `eb27b62d809ac26611ba6b79bc1100b3dd1d9f0b` and independent confirmation blob `9171ce6e562846040ce8f0e9c4776edbd4b37bd0` authorized exactly one infrastructure-only run #1 / attempt #1, 32 lanes. Marker-only commit `c6526f940a559140eaa7928d97164524e462cecf` launched run `35251121404`. That identity is consumed and MUST NOT be rerun.

Run `35251121404` produced 32 lane artifacts and terminal decision artifact `10510805424`. Decision outer SHA256 `fe664cd5ef1c5adf959d40f7c179550074b380ccd0c3805dc361661bf97bc574`; inner `decision.json` SHA256 `e57bcb39736bf80dac16900cb124ec66429e00bc1e20c31df0b05ea5f2a86325`. Frozen classification is **`INVALID_DIAGNOSTIC_PROVENANCE`** with `HTTPError: HTTP Error 415: Unsupported Media Type`. The decision had 32 artifacts, no missing lanes and zero accepted `artifact_provenance` because retrieval failed before receipt validation. This is not diagnostic FAIL or PASS.

Durable terminal result blob: `6a75796df2b88c426549a9cd047169bbf9115599` at `docs/dsir4/results/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_6_TERMINAL_RESULT_V0_1.json`.

Dual-root-cause audit blob: `43045a929e5cfb87aaa32c3158fc8839ede88df5` at `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_GRID896_V0_6_TERMINAL_DUAL_ROOT_CAUSE_AUDIT_V0_1.md`.

Independent terminal confirmation blob: `bdabd5bd085a8507af999fd535701ce6adb10688` at `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_GRID896_V0_6_TERMINAL_INVALID_CONFIRMATION_V0_1.json`; verdict `CONFIRMED_SCOPED`.

## Confirmed defect A — canonical source serialization identity

The pre-existing semantic lines hash `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4` corresponds to 897 lines normalized with exactly one final LF. The committed canonical Git object contains the same 897 words but no final LF:

- raw file = 15248 bytes, SHA256 `e9b5a3093223f13291993ea4339398cc5274c0047540740dd73978529c2689a0`;
- normalized semantic lines + LF = 15249 bytes, SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`.

V0.6 compares the normalized hash directly with raw file bytes and requires raw final LF. Independent R01/R03/R17 receipts, on different hosted runners, all report `BLOCKED_MISSING_OR_UNBOUND_CANONICAL_OBJECT` / `canonical source SHA256 mismatch` before payload reconstruction. Therefore this is a common one-byte serialization-binding defect, not host-specific evidence.

## Localized defect B — Actions artifact-download transport

V0.6 aggregate enumerated all 32 lane artifacts, then requested `/actions/artifacts/{artifact_id}/zip` using `Accept: application/octet-stream` and observed HTTP 415. Current GitHub Actions artifact-download documentation describes a 302 redirect and recommends `Accept: application/vnd.github+json`. Treat this as a localized request/media-type compatibility defect. V0.7 must prospectively qualify the repaired request path; do not post-hoc alter V0.6 classification.

The two defects are independent. Repairing only one is insufficient.

## Prospective population evidence

Historical V0.22 terminal cross-host run `34875798025` had all 32 lanes eligible with `10 NATIVE_AVX512_ACTIVE + 22 NATIVE_AVX512_INACTIVE`, satisfying its frozen population-power gate. V0.2 later retained exactly the 10 ACTIVE lanes while other lanes failed after fingerprinting at native GRID896 materialization. This response-blind history supports the hypothesis that a content-addressed producer can restore the censored INACTIVE population. It does not authorize science.

## Current authorization state

- V0.6: terminal historical **`INVALID_DIAGNOSTIC_PROVENANCE`**, rerun forbidden;
- V0.6 diagnostic PASS/FAIL: not established;
- V0.6 dual infrastructure root cause: independently confirmed scoped;
- V0.7 design/static qualification: authorized;
- V0.7 promotion/execution: not authorized;
- successor sentinel science: not authorized;
- full107/downstream science: not authorized.

## Funnel

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED -> V0.5 GOVERNANCE CLOSED -> SUCCESSOR V0.1 CONSUMED -> GRID896 DISPATCH DIAGNOSTIC TERMINAL -> SUCCESSOR V0.2 SENTINEL_INVALID -> CROSS-HOST DESIGN CONFIRMED_SCOPED -> V0.1-V0.5 INVALID -> V0.6 STATIC CONFIRMED -> REGISTRY BOUND -> ONE-SHOT AUTHORITY CONFIRMED -> V0.6 RUN 35251121404 CONSUMED -> INVALID_DIAGNOSTIC_PROVENANCE -> SOURCE SERIALIZATION DEFECT CONFIRMED + ARTIFACT TRANSPORT DEFECT LOCALIZED -> V0.7 DESIGN/STATIC QUALIFICATION OPEN -> V0.7 EXECUTION CLOSED -> SUCCESSOR SCIENCE CLOSED -> FULL107 CLOSED`.

Scientific effect remains `+0/+0`; numerical response reproducibility, exact-target/scientific criteria, covariance, statistical/model validity and physical dark-sector inference remain `NOT_EVALUATED`.

## Exact next admissible stage

`DESIGN_AND_STATICALLY_QUALIFY_NEW_V0_7_IDENTITY_WITH_ONLY_CANONICAL_SOURCE_SERIALIZATION_BINDING_AND_ACTIONS_ARTIFACT_DOWNLOAD_TRANSPORT_REPAIRED`.

Required V0.7 invariants:
1. Preserve canonical Git blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`.
2. Bind raw file separately: 15248 bytes, SHA256 `e9b5a3093223f13291993ea4339398cc5274c0047540740dd73978529c2689a0`.
3. Parse exactly 897 lowercase 16-hex tokens independent of final-LF presence, then reproduce normalized-line SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`.
4. Preserve packed 7176-byte payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d` and negative-control SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.
5. Repair and response-blind qualify artifact ZIP retrieval while preserving GitHub artifact digest verification.
6. Preserve 32 lanes, run/job/head bindings, consumer roundtrip, classifier semantics and zero-science scope.
7. No V0.7 promotion or execution authority before exact new executor/workflow/manifest pass static qualification and independent Critic.
