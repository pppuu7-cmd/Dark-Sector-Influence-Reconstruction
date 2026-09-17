# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions state, frozen authorities, immutable artifacts and independent Critic closures are authoritative; chat is not authority.

## Frozen science boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen: 107 DES53+BOSS54 rows; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

Science remains `NOT_EVALUATED`. Full107 and all downstream science remain closed.

Never rerun consumed identities: V0.2 `35181812498`; V0.6 `35251121404`; V0.7 static qualification `35253515074`; V0.8 repair-primitive qualification `35264388526`; response-blind artifact transport qualification `35265458237`; response-blind corrected-repair-pair operational qualification `35266829413`; completed one-shot captures. New defect or prerequisite requires a new prospective identity.

## V0.6 / V0.7 / V0.8 terminal history

V0.6 run `35251121404` is terminal `INVALID_DIAGNOSTIC_PROVENANCE` after historical artifact retrieval observed HTTP 415. V0.7 run `35253515074` is terminal `INVALID_STATIC_QUALIFICATION` under the superseded final-LF hypothesis. V0.8 run `35264388526` is terminal `INFRASTRUCTURE_FAILURE_V0_8_QUALIFICATION_HTTP_AUTH` after local corrected-canonical checks reached network transport and HTTP 401.

These are historical infrastructure/provenance outcomes only: not numerical disagreement, host disagreement, scientific failure or dark-sector null. They are immutable and must not be rerun or repaired in place.

## Canonical source correction — definitive

Committed canonical V0.1 contains exactly one publication corruption: deleted ASCII `e` at zero-based byte offset `13182`, line 776 column 8 (1-based).

- correct token: `3f9c8a9eeea3c9c8`;
- malformed committed token: `3f9c8a9eea3c9c8`;
- historical V0.1 Git blob: `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- historical V0.1 SHA256: `f84d6fa7cf9e5b8014176fd480062b27aaf97947d4a5211c7fbb5c69f93634ba`;
- historical V0.1 byte length: `15248`;
- final LF is present.

Corrected canonical bytes are frozen as historical V0.1 plus one inserted ASCII `e` at offset 13182. Historical malformed V0.1 remains immutable evidence and must not be overwritten.

Corrected identity:

- byte length `15249`;
- SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`;
- Git blob `ded43b233a71a631809111514c9dd35d0419af2d`;
- 897 valid lowercase hex16 lines;
- payload length `7176`;
- payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`;
- frozen payload negative-control SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

Frozen specification: `docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_CANONICAL_V0_2_REPAIR_SPEC_V0_1.json`, Git blob `c3b3d2f5533d5c6c9c27b9922d58d0a32188be95`.

## Response-blind Actions artifact transport — terminal PASS

Functional transport identity executed exactly once: workflow `360818520`, run `35265458237`, run #1 / attempt #1, job `105351389294`, terminal success.

Classification:

`PASS_HISTORICAL_ACTIONS_ARTIFACT_TRANSPORT_PRIMITIVE_QUALIFIED`

Frozen transport target and live evidence:

- target artifact `10508904186`, name `grid896-v0-6-R01`;
- metadata API HTTP 200;
- archive API HTTP 302;
- redirect storage host `productionresultssa4.blob.core.windows.net`;
- redirected storage request rebuilt without repository Authorization;
- storage HTTP 200;
- outer ZIP SHA256 `b8897d2b5ff336be7f472bca740f1bc4b82e301b7b6ca0381127627a71050ffd`;
- sole member `R01.json`;
- member SHA256 `95516bd6920448c7bc36f4d85592f318a719d2ea3044388b31e2f7e1ef6deab3`;
- source run `35251121404`, attempt 1, head `c6526f940a559140eaa7928d97164524e462cecf`, lane `R01`;
- no CLASS, scientific response, covariance, scientific classifier or response-dependent decision.

Qualified transport implementation Git blob `0228fda053f6396708dabaf8e47984145e1b7b7a`. Terminal authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_ARTIFACT_TRANSPORT_QUALIFICATION_TERMINAL_V0_1.json`, Git blob `f5d2068ef33a6b00592951476030d84a25cb60a1`.

Transport is solved for this prerequisite chain. Do not create another transport experiment without a new defect.

## First corrected-repair-pair operational qualification — terminal INVALID_IMPLEMENTATION

A new response-blind functional identity was prospectively frozen to combine the exact canonical repair with the already-qualified transport primitive:

- qualification script blob `7fb1204a84ed6684d65e2ab12ebbf46e8c37f487`;
- workflow blob `1af3d4470c760b3f12d299b37b51cf1d5f48a543`;
- scoped authority blob `bc9bd0cf6f7871d2976abe03880b6e383bfc8969`;
- independent static Critic blob `277f7616c81bba33cf77872190b12fd058158547`, verdict `PASS_SCOPED`;
- marker launch commit `4e7b77d3c15c80657a88a59e017ef450b75413b1`.

One-shot execution:

- workflow ID `360827730`;
- run `35266829413`;
- run #1 / attempt #1;
- job `105355977563`;
- head `4e7b77d3c15c80657a88a59e017ef450b75413b1`;
- workflow conclusion `failure` because the terminal result classification was not PASS.

Immutable result artifact:

- artifact `10517147674`;
- name `layerb-beta-v026-r1-response-blind-corrected-repair-pair-operational-qualification-v0-1`;
- outer artifact digest `sha256:c455224b5b5da98b803da9ce16101c8e9536c8e1937b5beb771397e74119d46d`;
- `result.json` SHA256 `bf4d6814052cf729eab7f116ae60cd4fc79032a2c3164e344c8f3e92f3226804`.

Frozen result:

`INVALID_IMPLEMENTATION`

with error stage `negative_control` and message:

`repair negative control did not reject: wrong insert offset`.

### Localized causal defect

The negative control used the same inserted ASCII `e` at offset `13183` rather than frozen offset `13182`. The malformed token contains a contiguous identical-byte `ee` run, while the corrected token contains `eee`. Insertion of the same `e` at an adjacent position inside that run can produce byte-identical corrected serialization. Therefore output identity alone cannot distinguish that operation-parameter change.

This is classified narrowly as:

`NEGATIVE_CONTROL_EQUIVALENT_OUTPUT_ALIASING`

The defect is in the negative-control design, not in the frozen repair hypothesis and not in transport.

Because code order performs exact historical-source, exact frozen repair, corrected SHA/Git-blob/grammar and payload checks before the negative controls, reaching this negative-control error establishes that the main frozen repair/payload path reached that stage successfully. It does **not** make the pair qualification PASS because the required control suite was invalid.

The failure occurs before all network calls. Therefore the qualified transport primitive was not runtime-tested or falsified in this consumed identity; artifact provenance was not evaluated here.

Response blindness stayed exact: CLASS false; scientific response false; covariance false; scientific classifier false; response-dependent decision false; producer lane count 0.

Terminal authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_REPAIR_PAIR_OPERATIONAL_QUALIFICATION_TERMINAL_V0_1.json`, Git blob `c851c8c93c1228ae268808dd0ef707fe190a02ae`.

Independent runtime Critic: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_REPAIR_PAIR_OPERATIONAL_QUALIFICATION_RUNTIME_CRITIC_V0_1.json`, verdict `PASS_TERMINAL_CLOSURE`, classification `INVALID_IMPLEMENTATION_NEGATIVE_CONTROL_ALIASING_CONFIRMED`.

Run `35266829413` is consumed and must not be rerun.

## Minimal successor defect hypothesis

A new prospective successor may be authored only for this localized defect:

`REPAIR_OPERATION_PARAMETERS_MUST_BE_VALIDATED_INDEPENDENTLY_OF_RESULTING_BYTE_IDENTITY_BECAUSE_IDENTICAL_BYTE_INSERTION_WITHIN_AN_IDENTICAL_BYTE_RUN_CAN_ALIAS_TO_THE_SAME_SERIALIZATION`.

Minimal repair:

1. add a pure exact-operation validator requiring offset exactly `13182` and inserted byte exactly ASCII `e`;
2. validate those operation parameters before reconstruction;
3. wrong-offset and wrong-byte negative controls must target that operation validator, not infer operation identity only from resulting bytes;
4. keep historical V0.1 identity, resulting corrected-byte identity, payload identity, frozen payload negative control, qualified transport implementation, artifact target, provenance rules and response-blind boundaries unchanged;
5. no producer lanes, CLASS, scientific response, covariance or science.

The consumed identity must remain immutable.

## Prospective population evidence

Historical V0.22 run `34875798025` had 32/32 eligible = `10 NATIVE_AVX512_ACTIVE + 22 NATIVE_AVX512_INACTIVE`. V0.2 later retained exactly 10 ACTIVE lanes while others died after fingerprinting at native GRID896 materialization. This remains response-blind motivating evidence only. Population recovery is `NOT_ESTABLISHED`.

## Current authorization state

- V0.6/V0.7/V0.8: terminal historical, rerun false.
- corrected canonical identity/specification: frozen.
- artifact transport: terminal PASS, rerun false.
- first corrected-repair-pair operational qualification run `35266829413`: terminal `INVALID_IMPLEMENTATION`, rerun false, runtime Critic closed.
- exact-operation-bound corrected-repair-pair successor: authoring authorized; execution requires a new prospective scoped authority and independent static Critic.
- corrected producer / cross-host population gate: **closed**.
- numerical reproducibility gate: **closed**.
- minimal scientific response: **closed**.
- full107/downstream science: **closed**.

## Recalculated dependency DAG

`corrected canonical identity` = frozen

`artifact transport` = terminal PASS

`corrected repair pair operational usability` = current highest prerequisite; first implementation consumed INVALID, minimal exact-operation-bound successor next

→ `corrected producer / cross-host population validity`

→ `numerical reproducibility prerequisite`

→ `minimal scientific response`

→ later scientific/statistical funnel only if upstream gates pass.

## Exact next stage

`AUTHOR_ONE_NEW_RESPONSE_BLIND_CORRECTED_REPAIR_PAIR_OPERATIONAL_QUALIFICATION_SUCCESSOR_WITH_EXACT_REPAIR_OPERATION_PARAMETER_BINDING;_VALIDATE_OFFSET_13182_AND_ASCII_E_BEFORE_RECONSTRUCTION;_MAKE_WRONG_OFFSET_AND_WRONG_BYTE_CONTROLS_TARGET_THE_OPERATION_VALIDATOR;_KEEP_ALL_FROZEN_OUTPUT_IDENTITIES_QUALIFIED_TRANSPORT_ARTIFACT_PROVENANCE_AND_RESPONSE_BLIND_CRITERIA_UNCHANGED;_INDEPENDENT_STATIC_CRITIC_BEFORE_ONE_SHOT_EXECUTION`.

Only a terminal PASS of that successor may open design/static qualification of the corrected producer / cross-host population gate.

Scientific effect remains `+0/+0`; science remains `NOT_EVALUATED`.
