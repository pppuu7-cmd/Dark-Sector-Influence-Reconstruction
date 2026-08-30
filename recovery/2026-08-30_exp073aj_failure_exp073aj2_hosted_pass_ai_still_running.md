# DSIR recovery checkpoint — Exp073AJ implementation failure, Exp073AJ2 hosted PASS, Exp073AI still running

**Date:** 2026-08-30

## Scientific accounting

- Strict Article-3 scientific repository readiness remains **52%**.
- G7/G8/G9 = OPEN.
- Layer A/B = OPEN.
- covariance/whitening = BLOCKED.
- Exp073AJ/AJ2 are provenance QA only and contribute **0** scientific-readiness points.
- Historical Q exact-repeatability FAIL remains immutable.
- Exp073AI remains a separate prospective reproducibility route and does not rescue/reclassify Q.

## Heavy-workflow audit

Exp073AI run `33310888983` was rechecked before new work.

- replica A job `99255607805`: `Compute exact single-thread replica` still IN PROGRESS;
- replica B job `99255607640`: `Compute exact single-thread replica` still IN PROGRESS.

No AI duplicate and no Exp073AA production task was launched.

## Exp073AJ v0.1 — negative implementation result

Prospectively frozen while Exp073AI was still running:

- prereg commit `361b86c7bb6215ea700e6a5c16578c059628987c`;
- implementation commit `4bea0c22c452916db0a6c20caef0782a1f3801f8`;
- workflow commit `bd8f98bac96d665db5c4cc44187610d83a792650`;
- workflow freeze `39b666b9c214c873dab01f53dd7df512ed35f226`;
- trigger/head `eb423aa97fbc03635328ee2fff4519c9929ea041`;
- hosted run `33313517040`, job `99262678309`.

The hosted run passed freeze enforcement but failed inside the synthetic matrix before any real AI receipt or numerical result was read. Exact error:

`TypeError: unhashable type: 'dict'`

Cause: the implementation attempted to use entire receipt dictionaries as dictionary keys while serializing resource SHA diagnostics.

Preserve classification exactly as:

`IMPLEMENTATION_FAILURE_UNHASHABLE_DICT_BEFORE_CLASSIFICATION_NOT_SCIENCE`.

This is not provenance evidence about AI, not scientific FAIL, not infrastructure evidence about the heavy workspace, and it changes no threshold/readiness/gate.

## Exp073AJ2 v0.2 — narrow prospective repair

AJ2 was frozen as a separate repair. It preserves the complete AJ classifier semantics and changes only resource diagnostic serialization to stable string keys `A` and `B`.

Frozen chain:

- prereg `33796a506ed375060a61c8ac22d7fdc1ee10bf5f`;
- implementation `d2ebf1769c2d0a86c8a0c3e2235e2da8ace074b5`;
- workflow `7a98eb2d763c8fa570f13dd22da839bde593b488`;
- workflow freeze `6e8733d656868eee615f4fcbe7dc631025312b15`;
- trigger/head `bcd287c8b648ab30568c7232d309dcffb4a7667f`.

Hosted authority:

- run `33313584914`;
- conclusion `success`;
- artifact `9732737233`;
- artifact digest `sha256:087ae5f1e01feac476317afcf4cfea3c8f4ee491c4edc0127b338c8ba7ffb49a`;
- token `PASS_EXP073AJ2_AI_ENVIRONMENT_PROVENANCE_CLASSIFIER_SYNTHETIC_V0_2`.

Classification:

`HOSTED_SYNTHETIC_PROVENANCE_QA_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

## Frozen future environment classification

After real Exp073AI receipts exist, AJ2 may classify only environment provenance, never the numerical operator result:

1. malformed identity/accounting/firewall -> invalid receipt;
2. thread-control mismatch -> `CONTROL_DRIFT`;
3. software/NumPy-build string mismatch -> `SOFTWARE_BUILD_DRIFT`;
4. controls/software equal and host fields equal -> `CONTROLLED_SOFTWARE_AND_HOST_MATCH`;
5. controls/software equal but host fields differ -> `CONTROLLED_SOFTWARE_MATCH_HOST_RUNTIME_DIVERGENCE`.

Volatile memory/filesystem/ulimit fields are hashed for provenance but cannot determine numerical reproducibility classification.

AJ2 cannot alter the frozen AI exact criterion, cannot introduce tolerance/ULP/rounding, cannot select a preferred replica, cannot release production, and cannot inspect support/covariance/nuisance/G8.

## Resume instruction

First inspect Exp073AI run `33310888983` and its artifacts. If AI remains active, do not duplicate it and do not launch the 13 Exp073AA tasks. If AI completes, preserve its exact hosted PASS/FAIL/infrastructure class first. Only after both real environment receipts exist may AJ2 be applied to those receipts, and even then the provenance label cannot reclassify the AI numerical outcome.
