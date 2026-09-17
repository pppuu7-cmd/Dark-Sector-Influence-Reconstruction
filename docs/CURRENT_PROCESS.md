# DSIR current-process ledger

Updated: 2026-09-17. Scope: **DSIR only**. Repository/Actions state, terminal artifacts and frozen authorities are authoritative; chat is not authority.

## Scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen under prereg blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain 107 rows = DES53+BOSS54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Full107, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global65537, statistical/model validity and physical dark-sector inference remain closed. Historical/same-identity runs must not be rerun, including `35033268924`, `35174721773`, `35181812498`, failed v0.2 lanes, and V0.6 run `35251121404`.

## Terminal predecessor chain

Historical V0.13 control remains terminal `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`. Response-blind GRID896 dispatch diagnostic `35177449482` established `GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED`. Successor sentinel v0.2 `35181812498` terminated `SENTINEL_INVALID` before numerical/scientific evaluation: only 10 eligible lanes, all `NATIVE_AVX512_ACTIVE`, zero inactive. Numerical/exact-target/scientific/model layers remained `NOT_EVALUATED`.

The frozen cross-host GRID896 design remains bound by prereg `903c80709439cb790bd41316029b218a77d5695b`, contract `6ba6e5a6c946a1091680f8f44821d323c9a463f3`, canonical Git blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`, and preexecution confirmation `5f1a7dcaeb39dd093586eefb4f869cc0791ae715`. Semantic canonical content remains 897 lowercase u64hex words; packed payload remains 7176 bytes SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`; one-bit negative-control SHA256 remains `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

Implementations V0.1–V0.5 remain terminal `INVALID_IMPLEMENTATION`, immutable.

## V0.6 registry binding and one-shot execution — consumed

Exact V0.6 executor blob `eae9eee7ae6a1424bcac67279663a2c8ddd3ebf9` and active workflow blob `832f0491421619579c2a1d77ba9ca339cb4898ac` were promoted byte-exactly. Read-only registry capture `35247378034` durably bound workflow ID `360576929`, exact canonical workflow path and registry state `active`, with zero prior target history. Registry-capture result blob is `033c9df4fde1feecd6cd1a75e1feb9abb9dc3013`; independent registry confirmation blob is `6c92403f487a4fe487a942e426930134c7c0b949`.

A separate V0.6 execution authority was then frozen and independently confirmed:
- execution authority blob `eb27b62d809ac26611ba6b79bc1100b3dd1d9f0b`;
- authority confirmation blob `9171ce6e562846040ce8f0e9c4776edbd4b37bd0`;
- exactly one run #1 / attempt #1, 32 lanes, infrastructure/provenance only;
- CLASS/science/full107/downstream remained false.

Marker-only commit `c6526f940a559140eaa7928d97164524e462cecf` launched canonical V0.6 run `35251121404`, workflow ID `360576929`, run #1 / attempt #1. The launch identity was correct and is now historical. No rerun is authorized.

## V0.6 terminal result — INVALID_DIAGNOSTIC_PROVENANCE

V0.6 produced all 32 lane artifacts and a terminal decision artifact. Decision job `105307265996`; decision artifact `10510805424`; outer SHA256 `fe664cd5ef1c5adf959d40f7c179550074b380ccd0c3805dc361661bf97bc574`; sole `decision.json` SHA256 `e57bcb39736bf80dac16900cb124ec66429e00bc1e20c31df0b05ea5f2a86325`.

Frozen decision classification is **`INVALID_DIAGNOSTIC_PROVENANCE`**, not PASS, FAIL, or BLOCKED. The aggregate error is `HTTPError: HTTP Error 415: Unsupported Media Type`. The decision saw 32 lane artifacts and no missing lane IDs but accepted no lane artifact provenance because retrieval failed before validation. No CLASS/scientific response/covariance was read.

Durable terminal result: `docs/dsir4/results/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_6_TERMINAL_RESULT_V0_1.json`, blob `6a75796df2b88c426549a9cd047169bbf9115599`.

Independent root-cause audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_GRID896_V0_6_TERMINAL_DUAL_ROOT_CAUSE_AUDIT_V0_1.md`, blob `43045a929e5cfb87aaa32c3158fc8839ede88df5`.

Independent terminal confirmation: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_GRID896_V0_6_TERMINAL_INVALID_CONFIRMATION_V0_1.json`, blob `bdabd5bd085a8507af999fd535701ce6adb10688`, verdict `CONFIRMED_SCOPED`, classification `V0_6_TERMINAL_INVALID_DIAGNOSTIC_PROVENANCE_WITH_DUAL_INFRASTRUCTURE_ROOT_CAUSE_CONFIRMED`.

### Root cause A — raw vs normalized canonical-source serialization

The static identity probe froze `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4` for the normalized 897-line serialization with one final LF. The committed canonical Git object contains the same 897 words but no final LF:
- raw repository file: 15248 bytes, SHA256 `e9b5a3093223f13291993ea4339398cc5274c0047540740dd73978529c2689a0`;
- normalized semantic serialization + final LF: 15249 bytes, SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`.

V0.6 applies the normalized hash directly to raw `read_bytes()` and also requires a raw final LF. Independent R01/R03/R17 receipts on different hosted runners therefore all terminate `BLOCKED_MISSING_OR_UNBOUND_CANONICAL_OBJECT` with `canonical source SHA256 mismatch` before payload reconstruction. This is a confirmed one-byte serialization-binding defect, not evidence of host disagreement.

### Root cause B — aggregate artifact-download transport

V0.6 aggregate calls `/actions/artifacts/{artifact_id}/zip` with `Accept: application/octet-stream`; the observed result is HTTP 415. Current GitHub Actions artifact-download documentation describes the successful endpoint as a 302 redirect and recommends `Accept: application/vnd.github+json`. The defect is therefore localized to the artifact-download request/media-type compatibility path. The precise repair must be prospectively qualified; no post-hoc reclassification of V0.6 is permitted.

These defects are independent: fixing only source parsing leaves the aggregate transport invalid; fixing only artifact transport leaves every checked lane blocked at source binding.

## Prospective hosted-population evidence

Historical V0.22 terminal cross-host run `34875798025` had all 32 lanes eligible with `10 NATIVE_AVX512_ACTIVE + 22 NATIVE_AVX512_INACTIVE` and satisfied its frozen population power gate. V0.2 later retained exactly 10 eligible ACTIVE lanes while the other lanes failed after fingerprinting at native GRID896 materialization. This is response-blind evidence that a future exact-byte producer repair can plausibly restore the previously censored INACTIVE class. It is not a scientific result and does not authorize a successor sentinel.

## Current authorization state

- V0.6: **terminal historical `INVALID_DIAGNOSTIC_PROVENANCE`; rerun forbidden**;
- V0.6 diagnostic PASS/FAIL: **not established**;
- dual V0.6 infrastructure root cause: **independently confirmed scoped**;
- V0.7 new implementation identity design/static qualification: **authorized**;
- V0.7 promotion/execution: **not authorized**;
- successor sentinel science: **not authorized**;
- full107/downstream science: **not authorized**.

## Funnel position

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED -> V0.5 GOVERNANCE CLOSED -> SUCCESSOR V0.1 CONSUMED -> GRID896 DISPATCH DIAGNOSTIC TERMINAL -> SUCCESSOR V0.2 SENTINEL_INVALID -> CROSS-HOST GRID896 DESIGN CONFIRMED_SCOPED -> V0.1-V0.5 INVALID -> V0.6 STATIC CONFIRMED -> V0.6 REGISTRY BOUND -> V0.6 ONE-SHOT AUTHORITY CONFIRMED -> V0.6 RUN 35251121404 CONSUMED -> INVALID_DIAGNOSTIC_PROVENANCE -> RAW/NORMALIZED SOURCE-BINDING DEFECT CONFIRMED + ARTIFACT-TRANSPORT DEFECT LOCALIZED -> V0.7 DESIGN/STATIC-QUALIFICATION GATE OPEN -> V0.7 EXECUTION CLOSED -> SUCCESSOR SCIENCE CLOSED -> FULL107 CLOSED`.

Scientific effect remains `+0/+0`. Numerical reproducibility, exact-target/scientific criteria, covariance, statistical/model validity and physical dark-sector inference remain `NOT_EVALUATED`.

## Exact next admissible action

`DESIGN_AND_STATICALLY_QUALIFY_NEW_V0_7_IDENTITY_WITH_ONLY_CANONICAL_SOURCE_SERIALIZATION_BINDING_AND_ACTIONS_ARTIFACT_DOWNLOAD_TRANSPORT_REPAIRED`.

V0.7 must preserve the V0.6 32-lane population, canonical Git blob, 897 semantic tokens, 7176-byte payload SHA, negative control, consumer roundtrip and classifier semantics. It must split raw-file identity (`e9b5a309...`, 15248 bytes) from normalized-line identity (`e4f8d717...`, 15249 bytes) and prospectively qualify the repaired Actions artifact-download transport. No V0.7 launch authority may be created until exact new executor/workflow/manifest bytes pass response-blind static qualification and an independent Critic.
