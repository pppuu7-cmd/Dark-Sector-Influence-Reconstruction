# DSIR current-process ledger

Updated: 2026-09-13. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Active frontier — V0.12 production-h common-grid interpolation audit

Authoritative active run: `34749034836`, launch commit `0daf43908e276482eb3b02e45d9d93af02bc43f2`.

Parent authority: `docs/dsir4/authority/LAYERB_BETA_COMMON_GRID_DISCREPANCY_V0_11.json`, creation commit `2621e0ab74685e502e7cec53997c58f99e354085`. Parent classification: `PRODUCTION_H_COMMON_GRID_DISCREPANCY_SUPPORTED`; authorized successor: `PROSPECTIVELY_FROZEN_PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT`.

Prospectively frozen V0.12 contract: `docs/dsir4/contracts/LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_V0_12.json`, final pre-execution identity commit `d15999917dca48553840468ea4edbce6bd6f1b02`.

Executor: `ci/layerb_beta_production_h_common_grid_interpolation_v0_12.py`, final pre-execution commit `ad22203c29a448b3c0282649b72e491fc123b286`, blob `aedd509780786f1efc200710e572c0af848cd878`.

Workflow: `.github/workflows/layerb-beta-production-h-common-grid-interpolation-v0-12.yml`, creation commit `46574e6da1bc282f3480ac922a19ca4c67a623fe`.

V0.12 has five independent hosted grid lanes: `GRID512`, `GRID640`, `GRID768`, `GRID896`, `GRID1024`. Each lane evaluates the same three preregistered D-domain target coordinates at `h=2e-4` and production `h=1e-4`. For each h it performs both a pure common-grid run and a mixed run in which the same three exact target-k values are added to the output grid. This yields 30 frozen grid/h/target cells and eight CLASS constructions per grid lane.

The audit is causal rather than another grid search. It compares, inside the same pinned numerical environment: (1) pure common-grid cubic interpolation; (2) mixed-grid cubic interpolation using only the original common-grid stencil; and (3) the exact target value returned by the same mixed CLASS invocation. It then cross-checks against immutable V0.10/V0.11 common-grid artifacts and the independent V0.9 direct TOL300 artifacts.

All 30 pure-grid cells must replay their immutable parent common-grid responses within `1e-5`, 100x tighter than the scientific `1e-3` response threshold. The three frozen parent violation cells are:

- `GRID640`, `h=2e-4`, `[F,D,3fe43d70a3d70a3e,3f900ea7bc915d36]`, parent direct relative difference `0.003709335890188209`.
- `GRID768`, `h=1e-4`, `[F,D,3fdab851eb851eb8,3f890e66b051e28b]`, parent direct relative difference `0.004037659729341879`.
- `GRID896`, `h=1e-4`, `[F,D,3fe3d70a3d70a3d7,3f8fc70971921840]`, parent direct relative difference `0.0011351878950117023`.

The frozen classifier can support cubic-interpolation dominance only if all three violations reproduce, the mixed interpolation remains discrepant from the exact value in the same invocation by `>=1e-3`, the mixed exact value agrees with independent direct TOL300 within `1e-3`, and target insertion does not itself move the interpolated response by `>=1e-3`. A solver node-set class requires all three violations to satisfy the node-set condition. A mixed class requires every violation to be accounted for and at least one cell of each mechanism. Otherwise the result is unresolved/not-reproduced/inconclusive; thresholds may not be relaxed afterward.

Frozen boundaries remain: production `h=1e-4`; native kpd20; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; exact-node binding `<=1e-12`. No covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537, full 107-row Layer-B traversal or science gate is authorized.

At the latest ledger update GitHub has created run `34749034836`; it is queued for hosted-runner capacity. No V0.12 science output has been inspected.

## Closed parent — V0.11 common-grid discrepancy localization

Run `34748453026`, head `1a2825cdb91319f9da13a2b446f3cc0447d1690c`, decision job `103701429242`, decision artifact `10314413873`, ZIP SHA256 `21500360580263f9e9b81c362b8adbc4290880446f4014745c983c1022a38fee`.

Classification: `PRODUCTION_H_COMMON_GRID_DISCREPANCY_SUPPORTED`, effect `+0/+0`; invariant PASS, exact keysets, zero unsupported targets, max requested-node mismatch `1.6564666256119906e-16`.

Resolution summary versus independent direct TOL300: `GRID512` production-h max `0.0003587116277798966`; `GRID640` production-h max `0.0004402359888879361` but one `h=2e-4` violation `0.003709335890188209`; `GRID768` production-h max `0.004037659729341879`; `GRID896` production-h max `0.0011351878950117023`; `GRID1024` production-h max `0.00010217977189246786` but smallest-h max `0.010699084577323596`. GRID512/640/768/896 are adequate by the frozen recovery rule; GRID1024 alone is inadequate at 14/20.

Interpretation is intentionally limited: the discrepancy is sparse and resolution/coordinate-specific, not a uniform common-grid failure. Because real violations occur at or above production h, full common-grid promotion remains blocked until V0.12 identifies the numerical mechanism.

## Anti-duplication / exact next gate

Do not launch duplicate V0.12 lanes. Consume the decision only after all five lanes and invariant are terminal. Promote a durable V0.12 authority before any successor launch, and follow only the encoded `next_stage`.

## Recovery/readiness

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; this numerical diagnostic chain does not by itself raise either value. Article-II real G5 ACT×unWISE remains a separate unresolved publication gate.
