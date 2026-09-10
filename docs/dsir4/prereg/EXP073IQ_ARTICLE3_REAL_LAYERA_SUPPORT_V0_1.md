# Exp073IQ — Article 3 real Layer-A broad physical-support execution v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 only.

Status: **PROSPECTIVELY FROZEN AFTER EXP073IM RADIAL PASS AND BEFORE ANY EXP073IQ REAL LAYER-A SUPPORT FRACTION IS EVALUATED.**

## Purpose

Execute the already-frozen Article-3 broad finite-operator Layer-A criterion on the complete inherited 1410-observation-row authority:

- 1170 DES Y1 Wm/WW rows using the exact factorized NaMaster-window x radial-kernel representation;
- 240 BOSS DR12 z3 rows using the already-frozen Exp073W finite `C=W@M` broad true-k representation.

This execution does not read or score Layer B common-response values, covariance, whitening, nuisance/SVD, relation/null statistics, G8, model ranking or article-selection information.

## Frozen parents

Bind:

- Exp073U full order SHA256: `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
- Exp073IM valid radial-support run/job: `34419165956 / 102690618922`;
- Exp073IM result artifact: `10130241439`;
- Exp073IM artifact digest: `sha256:3325bab0faa821c5ca3b13b4cd64d3d58c323e56a6f3e44952be84bfbc477156`;
- Exp073IM status: `PASS_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_2`;
- DES angular/radial authority manifest: `docs/dsir4/authority/EXP073IM_C2_REAL_INPUT_MANIFEST_V0_4.json` plus the prospectively frozen Wm_S3 transport override v0.2;
- Exp073W BOSS compatibility authority: run/job `33277001376 / 99165356858`, artifact `9721800577`, status `PASS_EXP073W_BOSS_LOWER_K_COMPATIBILITY_V0_1`.

The BOSS z3 selection is already frozen as `0.5<z<0.75`, entirely inside the Article-3 redshift domain; no effective-z is used.

## Frozen Layer-A science rule

Use exactly the previously frozen documents:

- `docs/ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md` for broad-row Layer-A semantics;
- `docs/ARTICLE3_DES_FACTORIZED_FINITE_OPERATOR_AMENDMENT_2026-08-30.md`;
- `docs/ARTICLE3_LAYERA_FACTORIZED_DES_SUPPORT_EVALUATOR_2026-08-30.md`;
- `docs/ARTICLE3_LAYERA_EXACT_5PCT_MASS_COMPARISON_AMENDMENT_2026-08-30.md`.

Physical domain remains exactly:

- `0.295 <= z <= 2.33`;
- `k > 0`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `k(ell,z)=(ell+0.5)/chi(z)` for DES support bookkeeping.

For every DES row, positive total mass `D` and valid in-domain mass `N` are evaluated with the exact factorized broad operator. Retain only when **both** frozen inequalities are true:

- `D - N <= 0.05 * D`;
- `N >= 0.95 * D`.

If the two checks disagree, classify that row `NUMERICALLY_UNRESOLVED_AT_5PCT_BOUNDARY`; Exp073IQ itself is then numerically unresolved and may not emit scientific PASS/FAIL until a separately preregistered higher-precision resolution.

No epsilon expands the scientific 5% boundary.

## Prospectively frozen coarse/fine convergence control

The 2026-08-30 finite-operator amendment requires a coarse/fine support-fraction and retained-label convergence test before the first classifying real Layer-A output but did not assign a numerical tolerance. Freeze it now, before Exp073IQ evaluates any real support fraction:

1. reconstruct both Exp073Z2 radial representations from the exact frozen DES-Y1 payloads, frozen CAMB commit and frozen Exp073Z2 algorithm:
   - coarse base step `0.005`;
   - fine base step `0.0025`;
   - released `Z_MID` nodes and exact Article-3 z boundaries included identically;
2. verify the freshly reconstructed **fine** logical arrays against the already-admitted Exp073Z2 hashes before scoring;
3. evaluate every DES Layer-A row independently on coarse and fine radial representations with the same exact angular bytes;
4. require retained/rejected labels to be identical for all 1170 DES rows;
5. require `max_q |f_invalid_coarse(q)-f_invalid_fine(q)| <= 5e-4`;
6. require every row's distance from the 5% threshold to exceed its own coarse/fine absolute change unless both coarse and fine classifications agree exactly through the dual mass inequalities. The categorical identical-label rule remains mandatory in all cases.

The `5e-4` numerical convergence tolerance is chosen prospectively to match the already-frozen Exp073Z2 radial normalization convergence ceiling. It is a numerical-stability control, not a relaxation of the scientific `0.05` threshold.

## BOSS composition

For the 240 BOSS rows consume the exact current-rule Exp073W support arrays. Do not recompute an effective k or z. Require:

- exact 240 inherited ordinals `1170..1409`;
- exact current retained mask logical SHA256 `249f4d6facd52e640ba170898a91191a6c918a58ab5cb04870687bf5a8c9ac32`;
- exact current `f_invalid` logical SHA256 `4e561cac60c76af3ccc4a858cd7510a7e0c7196e1f71aaba261e3b97715bfff7`;
- retained count `54`;
- no effective-z use.

## Full-order and Layer-A classification

Compose DES then BOSS in inherited ordinal order. Require exactly 1410 unique coordinate IDs and ordinals and reproduce the frozen full-order SHA256.

`PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1` is emitted only if:

- all authority/hash/order/anti-leakage checks pass;
- DES coarse/fine controls pass;
- no 5% boundary row is numerically unresolved;
- BOSS current-rule authority is exact;
- the combined Layer-A retained set contains at least 15 observation rows.

A valid run with fewer than 15 retained rows is `FAIL_ARTICLE3_OPERATOR_SUPPORT_V0_1`.

Authority/schema/hash mismatch, forbidden downstream access, failed fine-authority reconstruction, or execution failure is `INVALID_FOR_SCIENCE_ARTICLE3_OPERATOR_SUPPORT_V0_1`, never a scientific FAIL.

## Required output

Record at minimum:

- all input run/job/artifact/logical-array authorities;
- 1410 candidate IDs/order digest;
- per-row `D`, `N`, `f_invalid`, dual inequality outcomes and retained flag;
- DES coarse/fine maximum absolute support-fraction delta and changed-label count;
- DES/BOSS/combined retained counts and ordered retained-ID SHA256;
- all anti-leakage assertions;
- one frozen Layer-A classification.

No threshold, family selection, physical domain, carrier-selection rule or convergence criterion may be changed after a real Exp073IQ support output is inspected.
