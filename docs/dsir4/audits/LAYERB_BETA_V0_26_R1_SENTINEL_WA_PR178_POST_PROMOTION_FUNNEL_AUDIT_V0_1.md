# DSIR Funnel Audit — V0.26 R1 sentinel W/A PR178 post-promotion

Date: 2026-09-15

Reviewed object: exact PR178 merge `d605a941b412bb9625bf2fc6fedb0c7d9f8e8293`, which stages active-path W and authority-path A without final Q or L.

## Scope and authorization
The governing chain is prospective numerical/reproducibility only. V0.25 authorized a separately frozen successor rather than direct 107-row execution. Consolidated V0.26 R1 was frozen and independently qualified before sentinel implementation. PR171 implementation was independently qualified before promotion. PR173 froze the acyclic W/A/L package and was independently package-audited. The exact Q candidate was response-blind audited, independently funnel-qualified, and then promoted only at its inert candidate path. W/A pretrigger staging was then response-blind audited and independently funnel-qualified before PR178 promotion.

The W/A pretrigger terminal authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_WA_PRETRIGGER_FUNNEL_QUALIFICATION_V0_1.json` is blob `7c365449795d523d4ada39804c55c90e8c527a85`; its authority-bearing main merge `9a14b804c0743023c1225a53d55865612b3d0a97` predates PR178.

## Exact promotion identity
PR178 merge parents are exactly:

- first parent / authority-bearing main: `9a14b804c0743023c1225a53d55865612b3d0a97`;
- audited candidate parent: `15e7dbfb9c05744c026d5b03e5466267d802a2c7`.

Relative to its first parent PR178 adds exactly four files and no deletions:

- `.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml`;
- `.github/workflows/layerb-beta-v026-r1-sentinel-wa-pretrigger-static-audit-v0-1.yml`;
- `ci/layerb_beta_v026_r1_sentinel_wa_pretrigger_static_audit_v0_1.py`;
- `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json`.

Current exact blobs match the pretrigger authority:

- W `19907175f0f3417ddee2aba6916d961c6be02e26`;
- A `4ba40e59e6a9d48636d95d07efab575e56ae0966`;
- pretrigger auditor `2dbc76f15ee3510111db2bbe7da3cefb496d027b`;
- pretrigger workflow `f039472f7a94cda2ccf088f2e0e36b90ef08dc5d`.

Frozen executor and decision remain exact blobs `9affe7c7d4e02bbc728ba15e3cde893ec9876b38` and `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`. No implementation or threshold mutation occurred in PR178.

## Frozen preregistration/input identity
R1 machine contract remains blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`, binding the 107-row denominator, source-plan provenance, runtime stack, NumPy-1.26.4 GRID896 identity, parser byte convention, route-specific tolerances, strict scientific `<1e-3`, strict technical `<1e-5`, and requested-node `<=1e-12` boundary. PR178 does not modify the preregistration, contract, executor, decision, input plan, row denominator, sampling, tolerances, threshold rules, parameter ranges or interpretation ceiling.

Because this reviewed gate is launch-governance staging and no CLASS solve occurred, no substantive scientific-response values were inspected or used in this review.

## Pretrigger artifact provenance independently rechecked
Response-blind W/A pretrigger static run `35017254145`, run #1 / attempt #1, artifact `10415689546` was independently redownloaded. ZIP SHA256 reproduces `ac4d6b601e8f8b90cb0ae21bfbdc8f360949453784da51688a76318668076c72`; inner `wa_pretrigger_static_audit.json` is 1252 bytes, SHA256 `9f70c83f57f74805f073cbd0ef7b6bdf2fef0ac8028b01d503c6b54e7f46b681`.

Independent pretrigger funnel run `35017440323`, run #1 / attempt #1, artifact `10415119864` was independently redownloaded. ZIP SHA256 reproduces `e023a71379dee09ecf203b7a687c0da9b092b5ad2e39afc68dda39836752d8c0`; inner `wa_pretrigger_funnel_audit.json` is 1343 bytes, SHA256 `dfc6219a1d766f38957d20185f3e5473f7c33260abcfbf607f48053f7224e025`.

Both receipts are response-blind and record no CLASS invocation or scientific-response read.

## Post-promotion fail-closed controls
At exact PR178 promotion head `d605a941b412bb9625bf2fc6fedb0c7d9f8e8293`, an independent Actions query returns zero push workflow runs. Therefore staging W/A itself did not execute the sentinel.

Current active W is trigger-limited to `push` on `main` with path `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json`; it has no `workflow_dispatch`. Current final L path is absent. Current final Q authority path is absent. A binds exact W, requires a separate package qualification Q, deliberately does not bind L, and keeps full-107 authorization false.

A's internal `status=TERMINAL_LAUNCH_AUTHORITY` and `sentinel_science_execution_authorized=true` are frozen future launch content, not sufficient current execution permission in isolation: the active workflow itself requires both exact final Q and exact final L, and neither exists.

Hosted post-promotion response-blind run `35017910362`, run #1 / attempt #1 / push, job `104545919688`, completed success. Artifact `10417107515` was independently redownloaded: ZIP SHA256 `ce839f31ad5dfb164611df4cd49ee9b774c64cef7289e861944bb7e1c04e1c52`; inner `wa_post_promotion_audit.json` is 1179 bytes, SHA256 `034c546a75dfccc94dfb31596bea4d1967a33bccff219bffe1641e58f4a32ed2`. The receipt records L absent, final Q absent, exact-promotion push-run count zero, no sentinel workflow execution, no CLASS solve, no scientific-response read and no covariance read.

## Alternative explanations and counterexamples
Accidental activation by copying W to `.github/workflows` is refuted by the exact trigger path plus the observed zero-run exact promotion head. Manual activation is unavailable because `workflow_dispatch` is absent. A-alone activation is refuted by W's explicit requirements for Q and L and by the absence of both final objects. Candidate-Q storage cannot activate science because it remains under the inert candidate path. A merge-race/selected-success explanation is unsupported: the pretrigger static and funnel controls are both run #1 / attempt #1, and the post-promotion audit is run #1 / attempt #1; the exact promotion head itself has zero push runs.

The first three comment lines copied with W still describe it as “stored under docs” even though the exact frozen bytes now reside at the active workflow path. This is a documentary stale comment produced by the mandated byte-exact promotion, not executable behavior; changing it at this gate would mutate the frozen W identity. It is therefore noted but not treated as a scientific or provenance failure.

Interpolation, grid resolution, solver tolerance, execution order, numerical nondeterminism, covariance, nuisance, look-elsewhere/systematics and physical dark-sector explanations are not adjudicated by this gate because there is no substantive sentinel result yet. No claim about them is admitted.

## Interpretation ceiling
This review confirms only that exact PR178 W/A staging preserved the previously audited bytes and remains fail-closed before final Q/L. Green CI is not a scientific PASS. No numerical-response validity, statistical/model validity or physical dark-sector inference is established. Full 107-row replay and all downstream gates remain closed.

## Verdict
**CONFIRMED_SCOPED** — exact PR178 W/A promotion is confirmed only as fail-closed launch-governance staging. The next admissible operation is exact copy of the already-qualified Q candidate blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd` to the final Q authority path **without L**, followed by a separate final-Q post-promotion audit. Final L and sentinel execution remain forbidden until that later gate is terminal.
