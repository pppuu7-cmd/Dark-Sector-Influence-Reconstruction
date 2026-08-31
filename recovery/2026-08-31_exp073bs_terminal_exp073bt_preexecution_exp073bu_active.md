# DSIR recovery — Exp073BS terminal, Exp073BT pre-execution incomplete, Exp073BU active

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

## Authority preserved

- Exp073BJ remains terminal Track-A exact authority PASS; final authority artifact `9758841785` remains authoritative.
- Exp073AQ remains the permanent hosted exact-repeatability scientific FAIL.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and cannot be preferred or used downstream.
- No result in this recovery note changes scientific or draft/data readiness; all source-linkage work below is `+0/+0`.

## Exp073BS — terminal setup-stage incomplete

Hosted run `33417511410`, job `99571616144`, is terminal `BS_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`; immutable artifact `9767580175`.

The BS full-history prospective-freeze step succeeded. The job then failed during environment installation before the inherited BR Wigner/`drc3jj` probe executed: system Python 3.12/PyPI could not install the requested `pymaster==2.7` lineage. Therefore BS supplies no Q1–Q4 source/linkage evidence and no evidence for or against `drc3jj` availability.

## Exp073BT — prospective environment successor, pre-execution workflow failure

Preregistration:

- `experiments/073bt_article3_namaster27_wigner_linkage_bj_environment_successor_v0_1_prereg.md`
- commit `07c17496597306ff410633264d1d050f833728b9`

Workflow creation:

- `.github/workflows/exp073bt-article3-namaster27-wigner-linkage-bj-environment-v0-1.yml`
- commit `16ecd4cb75a68a8878f539b301ae76d3f044b4e0`

Trigger/head:

- `experiments/073bt_hosted_trigger_v0_1.md`
- commit `5d145ce6093c7dac007277e6528b36de5504e353`

Hosted run `33419946707` terminated immediately with workflow-level failure and **zero jobs**. Thus no runner, environment installation, inherited diagnostic, or receipt existed. The cause was a YAML representation error in the single-line interpreter invocation. This is pre-execution infrastructure failure only and carries `+0/+0`.

## Exp073BU — YAML-only successor active

Preregistration:

- `experiments/073bu_article3_namaster27_wigner_linkage_yaml_successor_v0_1_prereg.md`
- commit `8dffb59a960d3871d20f1cca1f2442455d15b6fe`

Sole allowed BT->BU change: replace the invalid single-line YAML `run:` representation of the inherited diagnostic invocation by a valid block scalar. No package, runner, probe code, Q1–Q5 criterion, interpretation, firewall, or accounting changed.

Workflow:

- `.github/workflows/exp073bu-article3-namaster27-wigner-linkage-yaml-successor-v0-1.yml`
- creation commit `79e71ab9c0128488a5c07ff9f6c64071a0a69903`

Trigger/head:

- `experiments/073bu_hosted_trigger_v0_1.md`
- commit `557881b008aded44cb3895650c575ea289c47dce`

Hosted run:

- run `33420089328`
- job `99580060141`

At the recovery checkpoint the BU job was `in_progress`. Steps completed successfully:

1. hosted job setup;
2. full-history checkout;
3. Exp073BU prospective-freeze enforcement.

The job had entered `Install exact hosted-successful Exp073BJ NaMaster 2.7 lineage` using conda-forge `python=3.11 namaster=2.7 healpy astropy numpy` on `ubuntu-24.04`.

Do **not** start a duplicate BU run while `33420089328` is active.

## Frozen BU outcomes

Administrative BR-to-BU prefix translation only:

- `BU_Q1_EXTENSION_EXPORTS_DRC3JJ`
- `BU_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ`
- `BU_Q3_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND`
- `BU_Q4_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT`
- `BU_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`

Any Q1–Q4 result is source/linkage evidence only. Q5 is incomplete infrastructure evidence. Every outcome is authority-free and `+0/+0`.

## Exact next action

Consume terminal Exp073BU run `33420089328`, job `99580060141`, logs and immutable diagnostic receipt. Apply the preregistered Q1–Q5 branch exactly. Do not modify the inherited probe or use result-driven rescue. Only if the source/linkage prerequisite is genuinely resolved may the next separately preregistered source-equivalence/streaming successor be designed.

Required G7 order remains unchanged. Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7 and G8 remain unauthorized. **No G8 jump.**
