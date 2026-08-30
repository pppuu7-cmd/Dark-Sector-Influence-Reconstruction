# DSIR RECOVERY MANUAL — live 2026-08-30 overlay

This is the active overlay to `docs/RECOVERY_MANUAL.md`. Read it with `docs/RECOVERY_LATEST.md`, `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`, and the newest recovery checkpoint.

## Active state

- Article-2 repository-for-writing readiness: **100%** for declared scope; not global G7/G8/G9 closure.
- Strict Article-3 scientific repository readiness: **52%**.
- G7/G8/G9 = OPEN.
- Layer A/B = OPEN.
- covariance/whitening = BLOCKED.
- reproducibility/provenance/governance/infrastructure QA adds **0 scientific-readiness points**.
- DSIR remains independent of RTK/RQIR.

## Frozen Article-3 boundaries

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid row fraction `<=0.05` inclusive;
- minimum final retained dimension `15`;
- DES classifying route `NSIDE=4096`;
- positive absolute operator/window envelopes only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance/whitening, nuisance SVD/rank, quotient/relation/null or G8 during support selection;
- exact-threshold ambiguity remains `numerically_unresolved`.

## Historical authority/negative record — preserve exactly

- Exp073X: `INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`.
- Exp073X2R primary P: hosted exact repeatability PASS / +0 readiness, canonical Wm_S0 SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.
- Exp073X2 Q: immutable `SCIENTIFIC_REPEATABILITY_FAIL` for exact operator repeatability, not dark-sector model physics.
- Exp073AH2: forensic class `WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE`; Q-A equals P exactly; Q-B SHA `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`; `472922/479232` differing entries; max absolute difference `2.0816681711721685e-17`; no frozen input/contract drift detected.
- Historical production route under Exp073AF remains `P PASS + Q SCIENTIFIC_REPEATABILITY_FAIL -> BLOCK_PRODUCTION`.

Do not erase or reclassify these records.

## Exp073AI original run — permanent infrastructure classification

Run `33310888983`, head `fdfb0eae9ea799b4a185a059a0d1b9dfca17b31d`:

- replica A job `99255607805`: success; artifact `9734480133`; digest `sha256:aa9f09e3dc8812341ad049ed39f5dea6da9249cf849417c60e825a7e48f93bc7`;
- replica B job `99255607640`: success; artifact `9734849638`; digest `sha256:f965b7cc120359d41246eccaa3d70a711485e75641252afe4d79813a061e5aee`;
- original aggregator job `99282603397`: failure before numerical comparison.

Root cause: workflow passed environment paths such as `external/a/data/derived/g7/exp073ai_env_a_v0_1.json`, but `actions/upload-artifact` had placed the files at artifact root after extraction. The comparator raised `FileNotFoundError` before reading either environment receipt or comparing the arrays.

Permanent original-run classification under the already-hosted-tested Exp073AK2 completion firewall:

`INCOMPLETE_INFRASTRUCTURE_AGGREGATOR_ENV_PATH_ERROR_BEFORE_REPEATABILITY_CLASSIFICATION`.

It is not repeatability FAIL.

## Exp073AM — prospective aggregator-only repair

Exp073AM was frozen after the path failure was diagnosed but before any repaired numerical comparison. It reused the immutable AI A/B artifacts and the unchanged comparator.

Frozen chain:

- prereg `3c18ea415f7fc5f4653cff5e241bdf0892140fde`;
- unchanged comparator `98e1518c34e30b0a7e59724ae60b7586f8c52f9c`;
- workflow `090d4f48f9eba0974c704a3dde410f99af9a64f0`;
- workflow freeze `8a85aaf768486bfce492a3a331a68e4382f6a130`;
- trigger/head `598e6e632f24ea54d43888fdc6d9d98b96d9ae3c`.

Hosted result:

- run `33321661835`;
- job `99284585530`;
- artifact `9735051043`;
- digest `sha256:167c82d36266efc3b7bd058f0cc307ec636b6c8efdb6b39b6e88f52d6edb3d66`;
- token `PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1`.

Exact repaired comparison:

- A SHA `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- B SHA `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- SHA identical = true;
- `numpy.array_equal(A,B)` = true;
- differing entries `0/479232`;
- differing bands `0/39`;
- max abs difference `0.0`;
- mean abs difference `0.0`;
- single-thread controls verified = true;
- frozen metadata identical = true.

This is a real hosted **non-classifying exact reproducibility PASS** for the controlled single-thread route. No tolerance, rounding, ULP allowance or majority voting was introduced. It adds +0 readiness and does not release production.

## Exp073AL/Exp073AN — real cross-route stability result

Exp073AL had already been prospectively frozen and hosted-tested before any real AI output existed. Its branch logic was therefore pre-result:

- valid AI PASS + SHA equal to primary P -> `EXACT_CROSS_ROUTE_STABILITY_AI_EQUALS_PRIMARY_P`;
- valid AI PASS + different SHA -> `DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P`.

Historical primary-P SHA:

`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

Controlled single-thread AI/AM SHA:

`8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`.

Exp073AN real binding used the unchanged Exp073AL classifier:

- binding note `9e0f586107e0b458d2e7f1a4a9378af2b7ed5257`;
- input binding `0cd75c9566b37c0042d73e6a021c473ace896933`;
- classifier `a0ee0c5f37533093931c0495b4edd5967ce5a00c`;
- workflow `d1d3c33b242cd13d681616871820a093c3a526d6`;
- freeze `591f7cc80fad513246b6344693722e66768b87a3`;
- trigger/head `c6e385d6e4051b6cf5d3f57d1074d12e63bf53fe`;
- hosted run `33321762778`, job `99284850109`;
- artifact `9735076794`;
- digest `sha256:c93e50f2ac6b8f932d8dd9e2cc94b4a2304398549eb1ae033d195b989e8c780b`.

Real hosted classification:

`DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P`.

Interpretation: the frozen single-thread execution route is internally bitwise deterministic across the two independent hosted replicas, but it converges to an exact authority different from the historical primary-P authority. Therefore bitwise operator authority is execution-route-sensitive.

This is a numerical/reproducibility governance result, not dark-sector model physics. Production remains false and readiness remains 52%.

## Exp073AJ2 and Exp073AK2 remain applicable firewalls

- AJ2 may independently classify environment provenance from complete receipts but may not alter numerical PASS/FAIL, select a preferred replica, introduce tolerance or release production.
- AK2 guarantees infrastructure failures/cancellations/path errors cannot be promoted to repeatability FAIL; only a valid completed comparator authority may carry the frozen AI numerical PASS/FAIL token.

Neither adds readiness.

## What is established vs not established

Established:

1. historical Q exact repeatability failed;
2. original AI aggregate failed only because of environment-receipt path binding;
3. repaired controlled single-thread AI route is bitwise reproducible across two independent hosted runners;
4. its exact SHA is `8ac59fc0...9220`;
5. historical primary-P exact SHA is `6ec29f6d...18d0f`;
6. the two exact authorities differ, so exact workspace authority is execution-route-sensitive.

Not established:

- no tolerance-based numerical/physical equivalence criterion;
- no new canonical production authority;
- no supersession of primary P or historical Q;
- no Exp073AA production release;
- no Layer-A support result;
- no covariance/nuisance/G8 result;
- no scientific dark-sector model PASS.

## Current authorized route

Do **not** launch another AI and do **not** launch the remaining 13 Exp073AA tasks.

The next admissible gate must be a **new prospectively frozen authority-succession decision protocol**, defined before any further angular production. It must decide whether production authority requires exact bitwise agreement across execution routes or whether a separately justified numerical-equivalence contract can be scientifically admitted. It must preserve historical P/Q/AI/AM/AN results exactly and cannot retroactively change any FAIL/INCOMPLETE classification.

Until a valid succession authority exists and a real complete pre-support operator manifest is produced, strict Article-3 readiness remains **52%**.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/RECOVERY_LATEST.md`
4. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
5. `recovery/2026-08-30_exp073am_pass_exp073an_real_cross_route_shift.md`
6. `experiments/073am_article3_ai_aggregator_path_repair_v0_1_prereg.md`
7. `experiments/073an_article3_real_exp073al_binding_v0_1.md`
8. `experiments/073al_article3_ai_vs_primary_exact_stability_classifier_v0_1_prereg.md`
9. `experiments/073ak2_article3_ai_completion_authority_classifier_v0_2_prereg.md`
10. `experiments/073aj2_article3_ai_environment_provenance_classifier_v0_2_prereg.md`
11. `experiments/073ah2_article3_q_repeatability_forensic_binding_v0_2_prereg.md`
12. `experiments/073af_article3_x2_to_exp073aa_release_control_v0_1_prereg.md`.
