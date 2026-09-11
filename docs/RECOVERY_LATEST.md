# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_JL_NOT_CONVERGED_JM_RESOURCE_PILOT_NEXT_V103.md`, creation commit `13eac01bb565e8171724151b047127e268ff9c37`. Earlier notes remain immutable history.

## Recovered Exp073JL terminal result
Recovered canonical one-live Exp073JL v0.2 retry run/job `34544293038 / 103093458667`, head `417ec30eb0acd2896068f7ed3d5eeb3d47cedbbf`, is independently verified `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`.

Artifact `10178796851`; ZIP SHA256 `08e8b55c4c23374fc5e92e730e01c693a0aa2e8734d65bf3c38782a1bab16bab`; result SHA256 `b3798bbc83e6bbc070c02fba691813fe3de9d4fcc33de38a32c086b7e50c8478`; capacity receipt SHA256 `e1af249ccdfd393b9b0f1020ffa1b70d953fa457ca2212aa3ab29be01f74b66a`.

Frozen maximum coarse-vs-fine relative component difference is `0.012273497268380687`, `12.273497268380687 ×` the strict `1e-3` threshold. This is valid NOT_CONVERGED science-support rather than infrastructure failure: 107 retained rows; invalid rows 0; unsupported 0; lookup `1.6559173278185046e-16`; finite/nonzero and row labels unchanged; BOSS dense-z disagreement false; exact canonical grid and request-plan hashes; 4040 transfer calls; exactly 8 solver constructions/max one live/final live zero; same-process raw operands; parent identity preserved.

Durable terminal authority: `docs/dsir4/authority/EXP073JL_ARTICLE3_RECOVERED_CANONICAL_ONE_LIVE_THIRD_REFINEMENT_NOT_CONVERGED_V0_2.json`, creation commit `b16c28f02a6449e36e4a7bc74f6080e32c8c9df5`, blob `aca79d6596f49ced9fe9d965059a2352447f13b4`.

Exp073JL remains support-only `+0/+0`; covariance restriction unauthorized and Wm_S3 unopened.

## Branch selection
The prospectively frozen branch rule now selects **Exp073JM** only. Exp073JN is not activated and must not run for this JL outcome. The pre-verdict deterministic refinement ladder fixes JM at base 4096 -> 8192, requested canonical 4097 -> 8193; no result-dependent density choice is allowed.

## JM preparation complete except resource pilot
Canonical 4097 is the existing authoritative Exp073JT/JL fine lattice. Canonical 8193 was materialized response-blind before the JL verdict: 6/8 replicas matched the authoritative 4097 anchor and all six emitted byte-identical 8193 bytes. Committed 8193 decoded SHA `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`, text/u64hex SHA `90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6`, materialization commit `944619861bd2630431d8693615919820067cd1f0`.

Recovered JM helper `ci/exp073jm_article3_recovered_canonical_one_live_fourth_refinement_v0_2.py`, commit `0acfa1f00516a055795335c372845f51961ad797`, blob `4ba4868d751b95b97b2ac7f18701f5349e70c950`, preserves the original JM scientific contract while consuming canonical 4097/8193 and using the recovered exact eight-build/max-one-live architecture.

No-science JM static audit run/job `34545274582 / 103096420233` is independently verified 41/41 PASS; artifact `10178767490`, ZIP SHA `01c26c1a5586b964f395d3f1ab589bcfd100c518a653f136d9782428b39791d8`, result SHA `d265f98ff74b30917ced73e7ca2523fef19e28306c0e21bfed6f32e2faaf0eef`, durable authority creation commit `1a1ccbd179fd6c8bd4a2cb3c589e57d21aad49a4`.

## Current authoritative process
Full JM production is not yet authorized. Next mandatory gate is the canonical-8193 resource-only pilot required by the pre-verdict recovered JM alignment. It must mirror the already-validated JW fixed pilot requests, use exact canonical 8193, CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`, capacities 9216/262144, native kpd20, exactly four sequential roles/max one live, finite pilot responses, unsupported=0 and lookup<=1e-12. It must not execute the full 107-row JM convergence calculation.

Only an independently verified resource-pilot PASS plus a fresh anti-duplication check may authorize exactly one recovered JM 4097->8193 production run.

## Stable readiness telemetry
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%**. Valid JL NOT_CONVERGED moves the process branch but does not close Layer-B science.

## Exact next action
Prospectively freeze the JM 8193 resource-only pilot against the existing JW request set; implement/static-audit it without changing science; perform fresh zero queued/in-progress heavy-DSIR check; launch exactly one resource pilot. No JN execution and no tolerance/grid/estimator rescue.
