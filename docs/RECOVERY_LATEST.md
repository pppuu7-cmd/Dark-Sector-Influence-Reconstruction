# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_JO_STATIC_PASS_RESOURCE_PILOT_ACTIVE_V104.md`, creation commit `7756f29629c9dbbfc02417fbdd828d694cef369a`. Earlier notes remain immutable history.

## Recovered Exp073JL terminal result
Recovered canonical one-live Exp073JL v0.2 run/job `34544293038 / 103093458667`, head `417ec30eb0acd2896068f7ed3d5eeb3d47cedbbf`, is independently verified `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`.

Artifact `10178796851`; ZIP SHA256 `08e8b55c4c23374fc5e92e730e01c693a0aa2e8734d65bf3c38782a1bab16bab`; result SHA256 `b3798bbc83e6bbc070c02fba691813fe3de9d4fcc33de38a32c086b7e50c8478`. Frozen maximum 2049->4097 relative component difference is `0.012273497268380687`, `12.273497268380687 ×` strict `REL_TOL=1e-3`. Structural execution is clean: 107 retained rows, invalid 0, unsupported 0, lookup `1.6559173278185046e-16`, exact canonical/request-plan identities, 4040 transfer calls, 8 constructions/max one live/final zero, same-process operands.

Durable terminal authority: `docs/dsir4/authority/EXP073JL_ARTICLE3_RECOVERED_CANONICAL_ONE_LIVE_THIRD_REFINEMENT_NOT_CONVERGED_V0_2.json`, creation commit `b16c28f02a6449e36e4a7bc74f6080e32c8c9df5`, blob `aca79d6596f49ced9fe9d965059a2352447f13b4`.

Exp073JL remains support-only `+0/+0`; covariance restriction unauthorized and Wm_S3 unopened.

## Branch selection and JM preparation
JL NOT_CONVERGED activates **Exp073JM only**; Exp073JN is inactive. The pre-verdict sequential refinement ladder fixes JM at canonical requested 4097 -> 8193; no result-dependent density choice is allowed.

Canonical 4097 is the authoritative JL fine lattice, decoded SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`. Canonical 8193 was materialized response-blind before the JL verdict; 6/8 replicas reproduced the authoritative 4097 anchor and all six emitted byte-identical 8193 bytes. Fine decoded SHA256 `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`, text/u64hex SHA256 `90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6`.

Recovered JM helper `ci/exp073jm_article3_recovered_canonical_one_live_fourth_refinement_v0_2.py`, blob `4ba4868d751b95b97b2ac7f18701f5349e70c950`, preserves the original frozen JM classifier. Its no-science static audit run/job/artifact `34545274582 / 103096420233 / 10178767490` is independently verified 41/41 PASS, durable authority commit `1a1ccbd179fd6c8bd4a2cb3c589e57d21aad49a4`.

## Exp073JO resource-gate preparation
Prospectively frozen resource prereg `docs/dsir4/prereg/EXP073JO_ARTICLE3_JM_CANONICAL_8193_ONE_LIVE_RESOURCE_PILOT_V0_1.md` and helper `ci/exp073jo_article3_jm_canonical_8193_one_live_resource_pilot_v0_1.py` test only process/resource feasibility on the canonical 8193 lattice. They inherit the already-frozen JW A/B request set, use pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`, capacities 9216/262144, native kpd20, four sequential model roles and max one live. They deliberately do not execute the full 107-row JM traversal and define no coarse/fine JM convergence statistic.

No-CLASS/no-science Exp073JO static audit run/job/artifact `34545848379 / 103098154578 / 10178961999`, head `98fff1e68e552e6e96652e8ad1cbb2196c55956c`, is independently verified 42/42 `EXP073JO_RESOURCE_PILOT_STATIC_AUDIT_PASS_PLUS_0_PLUS_0`. ZIP SHA256 `eecb62871b31370b3820b2e0c971811df5f143eb229de4e7c83d821f1c493cfa`; result SHA256 `fd9e083114fe9979811a2d7f1dfddde4fcaf16b5ca2549eaec9bb1d81e381975`; no CLASS, no scientific response, no JM production. Durable static authority commit `a91e4c814c3b093740e512921446ee801913ff99`, blob `5ef079b37031cdd2b73982c45eb36ab705760355`.

## Current authoritative process
Immediately before launch, fresh Actions checks returned zero queued and zero in-progress runs. Exactly one Exp073JO canonical-8193 resource pilot was launched by workflow commit `a066756e65597959292ccf2762a50db97308b744`.

- workflow: `exp073jo-article3-jm-canonical-8193-one-live-resource-pilot-v0-1`;
- run/job: `34546569386 / 103100379621`;
- head: `a066756e65597959292ccf2762a50db97308b744`;
- GitHub-hosted Ubuntu 24.04;
- exact canonical 8193 lattice only;
- exact capacities 9216 / parser 262144;
- exactly four role-major CLASS constructions, max one live;
- fixed inherited JW A/B requests;
- no full 107-row JM production and no convergence classifier.

Latest V104 observation: authority/identity gate PASS and frozen stack installation in progress. Do not duplicate this run or use partial pilot response values for adaptation.

## Terminal transition
On terminal completion, independently verify the artifact ZIP/result/capacity receipt, exact canonical SHA, CLASS commit, one-replacement capacity provenance, role order, exactly 4 constructions, max-live=1, final-live=0, unsupported=0, lookup<=1e-12, finite operands/responses, same-process raw operands and explicit no-JM-production flags.

Only independently verified `CANONICAL_8193_ONE_LIVE_FOUR_BUILD_RESOURCE_PILOT_PASS_PLUS_0_PLUS_0` plus a fresh anti-duplication check may authorize exactly one full recovered Exp073JM 4097->8193 production convergence run under the unchanged original classifier. `CANONICAL_8193_RESOURCE_OR_INFRA_NOT_FEASIBLE_PLUS_0_PLUS_0` permits only minimal prospective process repair; no grid/tolerance/estimator rescue.

## Stable readiness telemetry
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** until a valid JM convergence rung is independently verified. Exp073JO itself is resource/process `+0/+0` and cannot change scientific readiness.
