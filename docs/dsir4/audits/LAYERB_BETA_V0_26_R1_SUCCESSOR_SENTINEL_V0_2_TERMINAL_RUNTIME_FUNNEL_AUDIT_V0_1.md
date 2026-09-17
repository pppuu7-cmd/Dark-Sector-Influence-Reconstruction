# Layer-B beta V0.26 R1 successor sentinel v0.2 terminal runtime funnel audit v0.1

Date: 2026-09-17. Scope: DSIR only. This is an independent terminality/provenance/classifier audit of the already-consumed successor sentinel v0.2 execution. It does not open full 107-row science, change thresholds, inspect/select rows post hoc, or authorize a retry.

## Frozen inputs and source identities

- preregistration blob: `545e5be589e0f8029d23db2edb4e2faad116c3a0`
- R1 contract blob: `b510d8e97baf1c0b7b216c0605d83cdd029254e9`
- launch authority blob: `f5932ce87acc392220ca2fa71abbade8c5899723`
- design Critic blob: `f89dc41d46cbe5727bc16f216e21432cdc4a4a57`, verdict `PASS_SCOPED`
- executor blob: `1f727056491a6f4997298bb63dba26589fd3ddec`
- target workflow blob: `00bb68196c995079cad50da70be555d737d28ecb`
- terminal-history workflow blob: `9dc4962288471fbcd0803d22cabe1182bfac8ed3`
- decision blob: `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`
- launch marker blob: `69d827768bc852e8d5f62d2d27e137826dd82e25`
- target head: `1fd68a9814ac987300710c4e67d080c7455efa34`
- experiment id: `LAYERB_BETA_V0_26_R1_SUCCESSOR_SENTINEL_SCIENCE_V0_2`
- nonce: `DSIR-V026R1-SUCCESSOR-20260917-B1-4C92E7A1`

Frozen scientific/numerical criteria remain unchanged: 107 rows = DES 53 + BOSS 54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions.

## Target terminality and uniqueness

Target Actions run `35181812498`, workflow `360201395`, event `push`, exact head `1fd68a9814ac987300710c4e67d080c7455efa34`, run #1 / attempt #1 is terminal with overall conclusion `failure`. Independent Actions enumeration by exact head returned `total_count=1` and only run `35181812498`. No rerun is admissible.

Jobs endpoint reports 35 jobs: authorization, plan materialization, 32 matrix lanes, and decision. Authorization job `105075391316` and materialize-plan job `105075530174` completed success. Decision job `105080542988` completed success after the matrix terminated.

## Frozen decision classifier result

Decision job logs show `actions/download-artifact` found 11 artifacts existing before the decision upload and selected 10 matching lane artifacts. The frozen decision program requires `len(docs)==32`, exactly one of every replicate `R01` through `R32`, and no duplicate replicate. Therefore 10 lane documents deterministically set `invalid=True` before the numerical/reproducibility/exact-target criteria are evaluated.

The decision finalizer printed exactly:

`PASS_LAYERB_BETA_V0_26_R1_SENTINEL_DECISION_FINALIZER_PLUS_0_PLUS_0 SENTINEL_INVALID 0`

and then:

`SENTINEL_INVALID`

The trailing `0` is the frozen decision program's primitive metric count; because the object is invalid, no numerical/scientific metric gate is evaluated. The classifier is therefore an invalid execution/provenance endpoint, not a scientific or physical negative result.

Decision artifact:
- id `10480279579`
- name `layerb-beta-v026-r1-successor-decision-v0-2`
- ZIP SHA256 `8718c9ece145907aaa4f4d1b812a7245fd226aa22c6415042a3fa293bda068b6`

The frozen decision source encodes `full_replay_launch_authorized=false`, `full_107_row_execution_authorized=false` and, for every non-pass class, `next_admissible_action=DIAGNOSE_WITHIN_FROZEN_SENTINEL_CLASSIFICATION_ONLY`.

## Terminal-history closure

Frozen terminal-history run `35183519508`, workflow `360201396`, run #1 / attempt #1 completed success. Its single job `105080579651` completed success. Runtime logs show it checked out exact target head `1fd68a9814ac987300710c4e67d080c7455efa34` and bound:

- target run `35181812498`, run #1 / attempt #1, conclusion `failure`, updated `2026-09-17T04:51:48Z`;
- auditor run `35183519508`, run #1 / attempt #1;
- exact experiment id and nonce;
- exactly one target run in history;
- exactly one decision artifact with the frozen name;
- historical rerun authorization false;
- same-nonce second attempt authorization false;
- full107 authorization false.

Terminal-history classifier stdout is exactly:

`SENTINEL_INVALID INVALID NOT_EVALUATED NOT_EVALUATED NOT_EVALUATED`

corresponding to decision classification `SENTINEL_INVALID`, provenance validity `INVALID`, numerical validity `NOT_EVALUATED`, exact-target validity `NOT_EVALUATED`, and scientific criterion `NOT_EVALUATED`. Model/statistical interpretation is also frozen as `NOT_EVALUATED`.

Terminal-history artifact:
- id `10480539101`
- name `layerb-beta-v026-r1-successor-terminal-runtime-v0-2`
- ZIP SHA256 `0d61e9f90f03d875e8a67d99a7882530f44e5d6bd875d900c33391033c5fb329`
- contains `terminal_receipt.json`, `terminal_receipt.sha256`, and `decision/sentinel_decision.json` according to the terminal-history upload log.

## Provenance closure boundary

The terminal-history job itself computed and stored the downloaded decision ZIP SHA256 and the inner `sentinel_decision.json` SHA256 in `terminal_receipt.json`, and wrote `terminal_receipt.sha256`. The GitHub connector exposes the immutable artifact ids and ZIP digests but not the binary artifact payload. The inner decision SHA256 and terminal receipt SHA256 are not printed in job logs and therefore were not independently materialized during this audit.

Accordingly this audit does **not** create a separate terminal result authority. The next admissible step is limited to exact artifact-inner provenance materialization and verification from the already-existing immutable Actions artifacts. This does not authorize rerun, retry, criterion changes, or new science.

## Classification and effect

Audit classification: `TERMINAL_V0_2_SENTINEL_INVALID_INNER_ARTIFACT_PROVENANCE_MATERIALIZATION_PENDING`.

Frozen scientific classifier: `SENTINEL_INVALID`.

Scientific effect: `+0/+0`.

Interpretation ceiling: terminal execution/provenance/classifier state only. Numerical response, exact-target criterion, scientific criterion, statistical/model validity and physical dark-sector inference are `NOT_EVALUATED`.
