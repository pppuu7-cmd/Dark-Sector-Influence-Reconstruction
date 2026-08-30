# DSIR recovery checkpoint — Exp073AL hosted PASS while Exp073AI remains active

**Date:** 2026-08-30

## Scientific accounting

- Strict Article-3 scientific repository readiness: **52%**.
- Article-2 repository-for-writing readiness: **100%** for declared scope; not G7/G8/G9 closure.
- G7/G8/G9 = OPEN.
- Layer A/B = OPEN.
- covariance/whitening = BLOCKED.
- Exp073AL is hosted synthetic governance/reproducibility QA and contributes **+0** scientific readiness.
- Historical Exp073X2 Q remains immutable `SCIENTIFIC_REPEATABILITY_FAIL`; Exp073AL cannot reclassify or rescue it.
- DSIR remains separate from RTK/RQIR.

## Pre-step audit

Before creating a new gate:

- `docs/RECOVERY_LATEST.md` was read;
- latest commits were inspected;
- Exp073AI run `33310888983` was inspected directly;
- jobs A `99255607805` and B `99255607640` were both still `in_progress` on `Compute exact single-thread replica`;
- no Exp073AI replica artifact existed at the beginning of this step;
- no duplicate Exp073AI and no Exp073AA production task was launched.

Thus the active heavy calculation was left untouched.

## Why Exp073AL was needed

Exp073AI's frozen preregistration correctly states that an internal AI PASS requires only exact equality of its own two single-thread replicas; historical-P agreement is explicitly not part of the AI PASS criterion.

That leaves a separate prospective question which had not yet been machine-frozen:

> If AI internally PASSes, is its exact canonical Wm_S0 authority also identical to the already hosted Exp073X2R primary-P authority?

Without a separate pre-output classifier, a future AI internal PASS could be over-interpreted post hoc as cross-route exact stability even if the new deterministic route produced a different exact canonical hash.

Exp073AL freezes this distinction before any AI output exists.

## Exp073AL frozen chain

- preregistration:
  `experiments/073al_article3_ai_vs_primary_exact_stability_classifier_v0_1_prereg.md`
  commit `cf3e4062f3068badc7e4453cb816de72168ffbc9`;
- implementation:
  `ci/exp073al_article3_ai_vs_primary_exact_stability_classifier_v0_1.py`
  commit `a0ee0c5f37533093931c0495b4edd5967ce5a00c`;
- hosted synthetic workflow:
  `.github/workflows/exp073al-article3-ai-vs-primary-exact-stability-classifier-v0-1.yml`
  commit `223951730f7193adc8690bf99538a8e2a313cb38`;
- workflow freeze:
  `experiments/073al_article3_ai_vs_primary_exact_stability_classifier_v0_1_workflow_freeze.md`
  commit `642263e96f545d8f3035af73adecf0af8449e7b8`;
- trigger/head:
  `ci/exp073al_article3_ai_vs_primary_exact_stability_classifier_v0_1.trigger`
  commit `2bd07bfdc850bc83897c6d67d9b13b583003aed9`.

All were committed while Exp073AI was still active and before any real AI artifact/final authority existed.

## Hosted synthetic result

- run `33319102300`;
- job `99277802521`;
- conclusion `success`;
- artifact `9734352248`;
- artifact digest `sha256:a9ed4f0be6ed4dd25924658697b76b5f0b016d0b7cdc09feafe3aa0441278aa1`;
- token `PASS_EXP073AL_AI_VS_PRIMARY_EXACT_STABILITY_CLASSIFIER_SYNTHETIC_V0_1`.

The hosted job passed prospective freeze enforcement, Python compilation, all 13 synthetic state tests, non-scientific accounting enforcement and artifact upload.

Classification of this result:

`HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

No real Exp073AI authority, angular array, AJ2 label, support, covariance, nuisance geometry or G8 quantity was read.

## Frozen historical-P authority

Primary Exp073X2R canonical Wm_S0 SHA remains:

`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

Exp073AL hard-fails if this historical authority identity drifts.

## Frozen future Exp073AL real classifications

A real future Exp073AL application can happen only after Exp073AK2 first supplies a valid completion class for Exp073AI.

### AI not validly classified

`NO_CROSS_ROUTE_STABILITY_CLASSIFICATION_AI_NOT_VALID`

No stability inference.

### Valid AI internal repeatability FAIL

`CROSS_ROUTE_STABILITY_BLOCKED_AI_INTERNAL_REPEATABILITY_FAIL`

No canonical AI hash accepted.

### Valid AI PASS and AI canonical SHA exactly equals primary P

`EXACT_CROSS_ROUTE_STABILITY_AI_EQUALS_PRIMARY_P`

This means exact authority stability across the two routes, but remains non-scientific and does not release production.

### Valid AI PASS but canonical SHA differs from primary P

`DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P`

This is a negative exact cross-route stability result. It does not retroactively convert AI's internal PASS into FAIL, but it blocks any claim that the exact operator authority is route-invariant.

## Firewall

Exp073AL may depend only on:

- immutable primary-P canonical SHA;
- Exp073AK2 completion class;
- verbatim valid Exp073AI final numerical token;
- AI canonical SHA only when AI has a valid internal PASS.

It may not use environment/AJ2 labels, angular values, support, fiducial P, covariance, whitening, nuisance geometry, quotient/relation/null or G8. It may not release Exp073AA production or change readiness.

## Current heavy-workflow state

At the latest inspection during this checkpoint, Exp073AI run `33310888983` remained active:

- A job `99255607805`: `Compute exact single-thread replica` in progress;
- B job `99255607640`: `Compute exact single-thread replica` in progress.

Do not launch another AI or Exp073AA production while AI remains active.

## Authorized next order

1. inspect Exp073AI terminal control-plane state and artifacts;
2. classify completion using Exp073AK2;
3. only if AK2 yields `VALID_HOSTED_EXP073AI_CLASSIFICATION`, preserve the final AI PASS/FAIL token verbatim;
4. independently apply AJ2 environment-provenance classification when complete environment receipts exist;
5. if AI validly PASSes, apply Exp073AL exact cross-route stability classification against primary P;
6. none of AI/AJ2/AK2/AL automatically authorizes production or changes readiness;
7. any future succession from the new route requires a separate prospective amendment after the real results are known.
