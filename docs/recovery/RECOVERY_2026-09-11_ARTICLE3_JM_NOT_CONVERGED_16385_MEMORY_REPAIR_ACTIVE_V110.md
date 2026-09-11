# DSIR Article III recovery — JM NOT_CONVERGED, canonical 16385 memory repair active V110

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR into this state.

## New independently verified scientific-support result
Recovered Exp073JM canonical 4097->8193 completed successfully and is independently verified:
- workflow run/job `34548136827 / 103105092111`;
- head `ab9e29234781c94b80280aa0d7b16245a3e31804`;
- source artifact `10181101449`;
- source artifact ZIP SHA256 `e80799bc087746029940206a6fed143cd327a49d1123f28ca7bb0d343a0e9588`;
- result JSON SHA256 `1084dcfc451d2aad5b3cb6f96589753f6a7418e72cb1f5dfbb0f2868c199927a`;
- capacity receipt SHA256 `cd6870264060afd2f3605473288323c978f88c0a6c340d748e8a3083effbc173`.

Terminal classification is `COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0` with max coarse/fine relative component difference `0.01070806986822778`, still `10.70806986822778` times the strict `1e-3` threshold. All structural receipts are clean: 107 retained rows, invalid-row count/fraction `0 / 0.0`, unsupported targets 0, max requested-node mismatch `1.6569708505745155e-16`, exact canonical 4097/8193 identities, exact frozen request-plan identities, exactly eight CLASS constructions/max-one-live/final-live-zero, no cross-process raw operand combination and 4040 transfer calls.

The reduction from the independently verified JL maximum `0.012273497268380687` to JM is only a factor `1.1461913696321435`.

## Independent pre-result validation
The pre-result terminal validator had already been frozen and statically verified before JM completed. Its event-driven consumer run/job `34551879267 / 103116317825` independently downloaded the exact source artifact, reverified the GitHub artifact digest and classified the branch as `NOT_CONVERGED_8193_TO_16385`.

Consumer artifact `10181107144`, ZIP SHA256 `0682d03c97b4f053767a8b63d44be973fb58b6deecc1c270901014c8dce9f912`; validation JSON SHA256 `c4eb7b0d75ce5ef3e47ae44eb6a54115e86ec4d3543e0ddcad03d97ee160e792`; source receipt SHA256 `52f973247856628396ad9a2baa6ef5bef22b8a7cae1d84a2276a79b9d838806e`.

Durable JM authority: `docs/dsir4/authority/EXP073JM_ARTICLE3_RECOVERED_CANONICAL_ONE_LIVE_FOURTH_REFINEMENT_NOT_CONVERGED_V0_2.json`, creation commit `24b55a087b3bc81c406978511e9ad47c90431a27`.

Therefore the CONVERGED fresh-closure branch is closed for this JM result and the prospectively frozen canonical 8193->16385 support rung is now the only active scientific-support continuation.

## Canonical 16385 resource boundary is established
Canonical 16385 remains fixed at decoded SHA256 `3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975`, text/u64hex SHA256 `7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69`.

Four independent hosted telemetry roles reproduce memory exhaustion under the unmodified k-output-history architecture. Python RSS reaches approximately 15.4–15.7 GB while MemAvailable and swap collapse; each process is killed. Durable resource authority: `docs/dsir4/authority/LAYERB_CANONICAL_16385_GITHUB_HOSTED_MEMORY_EXHAUSTION_V0_1.json`, creation commit `9a2a580c078e89bcf9dca058069e756406c82a92`.

This is a resource/performance failure `+0/+0`, not a scientific CONVERGED/NOT_CONVERGED result.

## Source-level memory root cause and prospectively frozen repair
Pinned CLASS-IV source audit shows that `k_output_values` both (a) inserts requested canonical k nodes into the perturbation solver grid and (b) assigns `perturb_print_variables`, which accumulates full per-k perturbation histories in `scalar_perturbations_data` and related arrays. DSIR requires (a) but does not consume (b) when reading transfer functions through `get_transfer`.

Root-cause audit: `docs/dsir4/audits/LAYERB_CANONICAL_16385_CLASSIV_K_OUTPUT_HISTORY_MEMORY_ROOT_CAUSE_V0_1.md`, commit `a8ecf4b7070068ff7efed788e9d69a253ce4ff21`.

Prospectively frozen minimal execution-only patch changes only the active history callback assignment from `perhaps_print_variables = perturb_print_variables;` to `perhaps_print_variables = NULL;`, while retaining all requested k nodes, CLASS integration, source/transfer generation and DSIR arithmetic. Patch script `scripts/dsir4/classiv_k_output_history_suppression_patch_v0_1.py`, commit `ca42f22cd8190454a8c3bd4b354bbc761a48ea74`, blob `e20687e933d665973c3be40598180587701fa8e0`.

## Current authoritative resource-equivalence process
The patch is **not authorized for 16385 yet**. Two independent canonical-8193 equivalence replicas are active in workflow run `34551841749`, head `225c51fc0db4822703c24fb5743ad32b6214b4b8`, jobs `103116205677` and `103116205843`.

Both must reproduce exactly the previously verified Exp073JO baseline: all eight raw A/B operand SHA256 values plus both A/B pilot-response SHA256 values, canonical-node identity, zero unsupported targets, lookup<=1e-12 and four sequential constructions/max-one-live. Memory reduction alone is insufficient. Any bit mismatch rejects the patch.

## Parallelization boundary
Independent response-blind/static/resource/provenance jobs may run concurrently. The activated scientific 8193->16385 support calculation must not be launched until memory repair is independently proven numerically equivalent and resource-feasible. Its eight finite-difference role lifetimes must remain in the prospectively frozen same-process/max-one-live architecture; do not split scientific operands across independent jobs.

A self-hosted unpatched 16385 pilot remains queued as historical diagnostic only and does not override the established hosted-memory failure.

## Stable readiness telemetry
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%.** JM supplies a valid new NOT_CONVERGED support result and activates the next rung, but Layer-B numerical support is still unresolved. Resource/process repair does not increase scientific readiness.

## Exact next action
1. Terminal-consume both 8193 history-suppression equivalence replicas and independently verify all numerical SHA receipts.
2. Only if both are exact PASS, freeze/launch replicated patched canonical-16385 resource pilots with telemetry.
3. Only after patched 16385 resource PASS may the full activated 8193->16385 scientific-support rung launch under the unchanged frozen classifier.
4. No tolerance/grid/domain/mask/interpolation/estimator rescue. Covariance restriction and Wm_S3 remain closed.
