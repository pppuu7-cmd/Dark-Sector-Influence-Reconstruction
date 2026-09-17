# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions state, frozen authorities and terminal artifacts are authoritative; chat is not authority.

## Frozen science boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen: 107 DES53+BOSS54 rows; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Science remains `NOT_EVALUATED`. Full107 and all downstream science remain closed.

Never rerun consumed identities: V0.2 `35181812498`; V0.6 `35251121404`; V0.7 static qualification `35253515074`; V0.8 repair-primitive qualification `35264388526`; response-blind artifact transport qualification `35265458237`; completed one-shot captures. New defect or new prerequisite requires a new prospective identity.

## V0.6 terminal history

Canonical V0.6 run `35251121404` is terminal `INVALID_DIAGNOSTIC_PROVENANCE`. Its aggregate artifact retrieval path observed `HTTP 415 Unsupported Media Type`. This historical failure is transport/provenance only, not numerical disagreement, host disagreement, scientific failure, or dark-sector null.

The historical V0.6 identity is immutable and must not be rerun.

## Canonical source correction — definitive

The old final-LF interpretation is superseded. Dedicated provenance evidence established that committed canonical V0.1 contains exactly one publication corruption: deleted ASCII `e` at zero-based byte offset `13182`, line 776 column 8 (1-based).

- correct token: `3f9c8a9eeea3c9c8`;
- malformed committed token: `3f9c8a9eea3c9c8`;
- historical V0.1 Git blob: `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- historical V0.1 SHA256: `f84d6fa7cf9e5b8014176fd480062b27aaf97947d4a5211c7fbb5c69f93634ba`;
- historical V0.1 byte length: `15248`;
- final LF is present.

Corrected canonical bytes are frozen as historical V0.1 plus one inserted ASCII `e` at offset 13182. The historical malformed object remains immutable evidence and must not be overwritten.

Corrected identity:

- byte length `15249`;
- SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`;
- Git blob `ded43b233a71a631809111514c9dd35d0419af2d`;
- 897 valid lowercase hex16 lines;
- payload length `7176`;
- payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`;
- negative-control SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

## V0.7 closure

V0.7 was built under the superseded final-LF hypothesis and is terminal `INVALID_STATIC_QUALIFICATION`. Run `35253515074` is consumed. No CLASS/science/covariance was touched. Do not repair or rerun V0.7.

## V0.8 repair-primitive qualification — terminal historical infrastructure failure

A scoped authority and independent static Critic authorized exactly one response-blind V0.8 repair-primitive qualification. Run `35264388526`, run #1 / attempt #1, reached the network phase after local corrected-canonical identity checks, then terminated with `HTTP 401` on artifact/network transport.

Frozen classification: `INFRASTRUCTURE_FAILURE_V0_8_QUALIFICATION_HTTP_AUTH`.

The V0.8 result is not canonical-repair falsification, not numerical reproducibility failure and not a scientific result. CLASS, scientific response and covariance were not touched. Effect remains `+0/+0`.

V0.8 is consumed and must not be rerun. Its historical terminal authority is `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_GRID896_V0_8_REPAIR_PRIMITIVE_QUALIFICATION_TERMINAL_V0_1.json`.

## Response-blind Actions artifact transport qualification — terminal PASS

A new functional identity, not an arbitrary V0.9, was prospectively frozen specifically for the HTTP auth/redirect defect class:

- script blob `0228fda053f6396708dabaf8e47984145e1b7b7a`;
- workflow blob `357154688bc95b0a937204224f014f900b6fe930`;
- scoped authority blob `b39df2b923f4aa282cbf829186ae24bab1750233`;
- independent static Critic blob `6a1cce0b83dee5f9cd552dd349609780487b7abc` with terminal `PASS_SCOPED`;
- marker-only launch commit `255bb40e2a8f75d80ee0547edb6a9c328be5f335`.

The authority permitted exactly one response-blind transport qualification run, run #1 / attempt #1, with interpretation ceiling `INFRASTRUCTURE_PROVENANCE_ONLY` and no CLASS, scientific response, covariance, scientific classifier, diagnostic producer, V0.8 promotion/execution, full107 or downstream science.

One-shot execution:

- workflow ID `360818520`;
- run `35265458237`;
- run #1 / attempt #1;
- job `105351389294`;
- head `255bb40e2a8f75d80ee0547edb6a9c328be5f335`;
- conclusion `success`.

Frozen qualification artifact:

- artifact `10516990564`;
- name `layerb-beta-v026-r1-response-blind-artifact-transport-qualification-v0-1`;
- outer artifact digest `sha256:1ce0b3a589f0c7e389805e3229bc5ceb3fe562b83d5f0c41abf36c3906180fd7`;
- `result.json` SHA256 `a1cebde64e494f24a7f1ddf1ebae7e7bd8a04c377fb4e1231d514c85717591b7`.

Terminal classification:

`PASS_HISTORICAL_ACTIONS_ARTIFACT_TRANSPORT_PRIMITIVE_QUALIFIED`

Exact live transport evidence:

- metadata API host `api.github.com` returned HTTP `200`;
- archive API returned HTTP `302`;
- redirect storage host was `productionresultssa4.blob.core.windows.net`;
- storage request was rebuilt without repository `Authorization`;
- storage request header names were exactly `accept`, `user-agent`;
- redirected storage returned HTTP `200`;
- historical target artifact ID `10508904186`;
- historical artifact name `grid896-v0-6-R01`;
- downloaded outer ZIP SHA256 exactly `b8897d2b5ff336be7f472bca740f1bc4b82e301b7b6ca0381127627a71050ffd`;
- ZIP sole member exactly `R01.json`;
- member SHA256 exactly `95516bd6920448c7bc36f4d85592f318a719d2ea3044388b31e2f7e1ef6deab3`;
- receipt provenance bound to source run `35251121404`, attempt 1, head `c6526f940a559140eaa7928d97164524e462cecf`, lane `R01`.

All defect-directed negative controls passed: wrong artifact ID rejected; wrong outer digest rejected; wrong member rejected; authorization leakage rejected; same-origin redirect rejected; malformed ZIP rejected.

Response blindness remained exact: `class_solver_invoked=false`, `scientific_response_read=false`, `covariance_read=false`, `scientific_classifier_invoked=false`, `response_dependent_decision=false`.

Terminal authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_ARTIFACT_TRANSPORT_QUALIFICATION_TERMINAL_V0_1.json`, Git blob `f5d2068ef33a6b00592951476030d84a25cb60a1`.

This PASS qualifies only the historical Actions artifact transport primitive. It does **not** retroactively turn V0.8 into PASS, does not qualify the corrected canonical repair pair operationally, does not establish cross-host numerical reproducibility and does not evaluate science.

## Prospective population evidence

Historical V0.22 run `34875798025` had 32/32 eligible = `10 NATIVE_AVX512_ACTIVE + 22 NATIVE_AVX512_INACTIVE`. V0.2 later retained exactly 10 ACTIVE lanes while others died after fingerprinting at native GRID896 materialization. This remains response-blind motivating evidence that an exact corrected content-addressed producer may restore the censored INACTIVE class. It is not science and is not population-recovery evidence yet.

## Current authorization state

- V0.6: terminal historical `INVALID_DIAGNOSTIC_PROVENANCE`, rerun false.
- V0.7: terminal historical `INVALID_STATIC_QUALIFICATION`, rerun false.
- corrected canonical identity/specification: frozen.
- V0.8 repair-primitive qualification: terminal historical `INFRASTRUCTURE_FAILURE_V0_8_QUALIFICATION_HTTP_AUTH`, rerun false.
- response-blind Actions artifact transport primitive: terminal `PASS_HISTORICAL_ACTIONS_ARTIFACT_TRANSPORT_PRIMITIVE_QUALIFIED`, rerun false.
- corrected canonical repair pair operational qualification: **not yet terminally qualified**.
- one new response-blind corrected-repair-pair qualification successor may be authored; execution requires its own prospective scoped authority and independent static Critic.
- V0.8 diagnostic promotion/execution: **closed**.
- cross-host numerical validity gate: **closed pending corrected repair-pair qualification**.
- successor sentinel science: **closed**.
- full107/downstream science: **closed**.

## Recalculated dependency DAG

`corrected canonical identity` = frozen

`artifact transport` = terminal PASS

`corrected repair pair operational usability` = current highest prerequisite

→ `corrected producer / cross-host population validity`

→ `numerical reproducibility prerequisite`

→ `minimal scientific response`

→ later scientific/statistical funnel only if upstream gates pass.

## Exact next stage

`AUTHOR_ONE_NEW_RESPONSE_BLIND_CORRECTED_REPAIR_PAIR_OPERATIONAL_QUALIFICATION_SUCCESSOR_USING_THE_VALIDATED_TRANSPORT_PRIMITIVE;_FREEZE_HISTORICAL_V0_1_PLUS_EXACT_ONE_BYTE_E_RECONSTRUCTION_AND_CORRECTED_SHA256_GIT_BLOB_PAYLOAD_IDENTITIES;_RETRIEVE_THE_FROZEN_HISTORICAL_SOURCE_ARTIFACT_USING_THE_ALREADY_QUALIFIED_METADATA_REDIRECT_STORAGE_TRANSPORT;_VERIFY_IMPLEMENTATION_AND_PROVENANCE_ONLY;_NO_CLASS_NO_SCIENTIFIC_RESPONSE_NO_COVARIANCE_NO_SCIENTIFIC_CLASSIFIER;_INDEPENDENT_STATIC_CRITIC_BEFORE_ONE_SHOT_EXECUTION`.

The purpose of that successor is narrow: prove that the **corrected canonical reconstruction + exact payload identity + now-qualified artifact transport** work together in one prospective response-blind identity. It must not run a 32-lane producer or science. Only a terminal PASS there can open design/static qualification of the corrected producer/cross-host numerical gate.

Scientific effect remains `+0/+0`; science remains `NOT_EVALUATED`.
