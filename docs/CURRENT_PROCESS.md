# DSIR current-process ledger

Updated: 2026-09-17. Scope: **DSIR only**. Repository/Actions state, terminal artifacts and frozen authorities are authoritative; chat is not authority.

## Frozen scientific boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen: 107 rows = DES53+BOSS54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions. Full107, covariance, whitening, nuisance, relation-null, `Wm_S3`, global65537, statistical/model validity and physical dark-sector inference remain closed.

Never rerun consumed identities, including `35033268924`, `35174721773`, `35181812498`, V0.6 `35251121404`, V0.7 static qualification `35253515074`, or completed one-shot provenance captures.

## Predecessor evidence

Response-blind GRID896 dispatch diagnostic `35177449482` established `GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED`. Successor sentinel v0.2 `35181812498` terminated `SENTINEL_INVALID` before science: 10 eligible lanes, all `NATIVE_AVX512_ACTIVE`, zero inactive. Historical V0.22 cross-host run `34875798025` had 32/32 eligible with `10 ACTIVE + 22 INACTIVE`, so restoration of the censored INACTIVE population remains a response-blind prospective hypothesis, not a scientific result.

## V0.6 — terminal historical INVALID

V0.6 registry ID `360576929` / exact path / state `active` was prospectively bound. One-shot run `35251121404`, run #1 / attempt #1, produced all 32 lane artifacts and decision artifact `10510805424`. Frozen terminal classification is **`INVALID_DIAGNOSTIC_PROVENANCE`**, not PASS or FAIL. Decision artifact outer SHA256 `fe664cd5ef1c5adf959d40f7c179550074b380ccd0c3805dc361661bf97bc574`; inner decision SHA256 `e57bcb39736bf80dac16900cb124ec66429e00bc1e20c31df0b05ea5f2a86325`. Aggregate observed `HTTP 415 Unsupported Media Type` while retrieving lane ZIPs. V0.6 is closed; no rerun.

The previously merged V0.6 dual-root-cause audit blob `43045a929e5cfb87aaa32c3158fc8839ede88df5` remains historical. Its aggregate HTTP-415 observation remains valid. Its source-side claim that canonical V0.1 lacked a final LF is **superseded** by stronger byte-level evidence below.

## Canonical V0.1 definitive byte identity — single hex deletion

One-shot byte capture run `35253892736`, run #1 / attempt #1, completed success. Artifact `10511577132`: outer SHA256 `55268b6f8302b269583e6546d61a8504c82bc644ed04d8ddb87765fd6122cf24`; inner result SHA256 `2d6d5d5cd5fc0cefc5f9ab53b64379a4a1e722638188d5734f3e6c051ccca9c7`.

Hosted Ubuntu measurements prove working-tree bytes = `git show` bytes = exact Git blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`; `git hash-object` agrees. No checkout transformation was observed. Actual committed V0.1 metrics:
- 15248 bytes;
- SHA256 `f84d6fa7cf9e5b8014176fd480062b27aaf97947d4a5211c7fbb5c69f93634ba`;
- final LF present;
- 897 LF / 897 split lines;
- at least one line is not 16 lowercase hex characters.

Exact comparison with the pre-v0.2 origin artifact from run `34954905127`, artifact `10390997654`, proves a **single ASCII `e` deletion**:
- zero-based byte offset `13182`;
- line 776, column 8 (1-based);
- correct origin token `3f9c8a9eeea3c9c8`;
- committed malformed V0.1 token `3f9c8a9eea3c9c8`.

Deleting only that byte from the pre-existing origin serialization reproduces exactly V0.1 SHA256 `f84d6fa7...` and Git blob `24fa6168...`. The intact pre-existing origin serialization is 15249 bytes, 897 valid hex16 lines, SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`, Git blob `ded43b233a71a631809111514c9dd35d0419af2d`, and packs to the unchanged 7176-byte payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`.

Therefore V0.6's source guard correctly rejected a malformed published canonical object. The source-side failure is a canonical publication defect, not missing LF, checkout normalization, or host disagreement.

## V0.7 — terminal invalid static qualification

First V0.7 thin-successor package attempted to repair a now-superseded final-LF hypothesis. Static qualification run `35253515074`, run #1 / attempt #1, is terminal `INVALID_STATIC_QUALIFICATION` with `FileNotFoundError: canonical raw SHA256 mismatch`; artifact `10512311250`, outer SHA256 `736b412c171afe1e04b30b5735fcd7a728c032f4f142e08b535a8bb964e91c9a`, inner SHA256 `260bf466611d9b5f7666246bcfb27601a94a6e99b1409a384c057241b548a072`. V0.7 is closed; no rerun or mutation.

## Corrected canonical V0.2 specification

The immutable V0.1 object is retained as historical evidence. A corrected V0.2 **repair specification** reconstructs the origin object from V0.1 by inserting exactly one `e` at byte offset 13182 and then requires:
- 15249 bytes;
- SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`;
- Git blob `ded43b233a71a631809111514c9dd35d0419af2d`;
- 897 lowercase hex16 lines;
- payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`;
- frozen one-bit negative-control SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

The V0.6 aggregate HTTP-415 transport defect remains separately open for successor qualification.

## Current authorization state

- V0.6: terminal `INVALID_DIAGNOSTIC_PROVENANCE`, rerun forbidden.
- V0.7 static qualification: terminal `INVALID_STATIC_QUALIFICATION`, rerun forbidden.
- canonical V0.1 single-hex deletion: independently confirmed; prior final-LF interpretation superseded.
- corrected canonical V0.2 reconstruction specification: frozen.
- V0.8 design and response-blind static qualification: **authorized**.
- V0.8 promotion/execution: **not authorized**.
- successor sentinel science: **not authorized**.
- full107/downstream science: **not authorized**.

## Funnel

`... -> V0.6 RUN 35251121404 -> INVALID_DIAGNOSTIC_PROVENANCE -> BYTE CAPTURE -> CANONICAL V0.1 SINGLE-HEX DELETION CONFIRMED -> PRIOR FINAL-LF CLAIM SUPERSEDED -> V0.7 STATIC QUALIFICATION INVALID/CLOSED -> CORRECTED V0.2 REPAIR SPEC FROZEN -> V0.8 DESIGN/STATIC-QUALIFICATION OPEN -> V0.8 EXECUTION CLOSED -> SUCCESSOR SCIENCE CLOSED -> FULL107 CLOSED`.

Scientific effect remains `+0/+0`; all numerical/scientific/model claims remain `NOT_EVALUATED`.

## Exact next admissible action

`DESIGN_NEW_V0_8_IDENTITY_FROM_IMMUTABLE_V0_6_BASE_PLUS_EXACT_CANONICAL_V0_2_RECONSTRUCTION_AND_ARTIFACT_DOWNLOAD_TRANSPORT_REPAIR;_RUN_ONE_RESPONSE_BLIND_STATIC_QUALIFICATION;_NO_PROMOTION_OR_DIAGNOSTIC_EXECUTION_BEFORE_INDEPENDENT_PASS_SCOPED`.
