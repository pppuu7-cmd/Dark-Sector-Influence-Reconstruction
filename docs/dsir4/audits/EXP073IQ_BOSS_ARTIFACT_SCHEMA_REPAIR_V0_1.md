# Exp073IQ — BOSS artifact schema compatibility repair v0.1

Date: 2026-09-10. Scope: DSIR Article 3 Exp073IQ only.

Status: INFRASTRUCTURE / AUTHORITY-READER REPAIR FROZEN AFTER AN INVALID RUN AND BEFORE ANY CLASSIFYING Exp073IQ RESULT.

## Trigger

Run `34423116443`, job `102702614014`, reached the frozen Exp073IQ evaluator after all checkout, CAMB, DES-Y1, angular, Exp073IM and BOSS artifact transport steps passed. The evaluator terminated with

`INVALID_FOR_SCIENCE_ARTICLE3_OPERATOR_SUPPORT_V0_1 KeyError('entire_selection_inside_article3_domain')`.

No scientific PASS/FAIL was emitted. The invalid result artifact is `10131679990`, ZIP digest `sha256:2eb79423f4b9499225c3a9fea359dd8dc6d33b32685a0429c6b9799d610b0f0a`.

## Root cause

The Exp073IQ reader assumed that the downloaded immutable Exp073W artifact JSON exposes the compact publication-receipt field

`radial_support.entire_selection_inside_article3_domain`.

The immutable Exp073W artifact instead records the same already-frozen property as the execution control

`controls.z3_interval_subset_verified = true`

and separately records

`controls.effective_z_used = false`.

The committed immutable Exp073W publication receipt (`data/derived/g7/exp073w_article3_boss_lower_k_compatibility_v0_1_key_metrics.json`) records the equivalent compact form:

- `radial_support.selection = "0.5<z<0.75"`;
- `radial_support.entire_selection_inside_article3_domain = true`;
- `radial_support.effective_z_used = false`.

Both representations bind the same Exp073W run/job `33277001376 / 99165356858`, artifact `9721800577`, classification `PASS_EXP073W_BOSS_LOWER_K_COMPATIBILITY_V0_1`, candidate count `240`, and the same current retained-mask / `f_invalid` logical hashes consumed by Exp073IQ.

## Frozen repair

Change only the Exp073IQ artifact reader assertion from the publication-receipt field name to the exact immutable artifact fields:

- require `candidate_count == 240`;
- require `controls.z3_interval_subset_verified is true`;
- require `controls.effective_z_used is false`.

All other Exp073IQ code, hashes, arrays, scientific domain, 5% support threshold, coarse/fine tolerance `5e-4`, minimum retained count `15`, ordering rules and anti-leakage rules remain unchanged.

This repair does not inspect, use or alter a real Exp073IQ support fraction or retained count. It only makes the reader consume the schema actually present in the pre-existing immutable Exp073W artifact.

## Classification semantics

Run `34423116443` remains permanently `INVALID_FOR_SCIENCE_ARTICLE3_OPERATOR_SUPPORT_V0_1`. A new run after this reader-only repair is the next eligible classifying execution; it may PASS, FAIL, remain unresolved, or become invalid under the unchanged frozen scientific rules.
