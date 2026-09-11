# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_JM_NOT_CONVERGED_16385_MEMORY_REPAIR_ACTIVE_V110.md`, creation commit `d0e80b22d0a2057bcf6f95c9bbf154825c105867`. Earlier recovery notes remain immutable history.

## Scientific frontier
Recovered Exp073JM canonical 4097->8193 is now independently verified `COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Source run/job `34548136827 / 103105092111`, source artifact `10181101449`, ZIP SHA256 `e80799bc087746029940206a6fed143cd327a49d1123f28ca7bb0d343a0e9588`, result SHA256 `1084dcfc451d2aad5b3cb6f96589753f6a7418e72cb1f5dfbb0f2868c199927a`.

The maximum canonical 4097->8193 relative component difference is `0.01070806986822778`, or `10.70806986822778` times the strict `1e-3` threshold. Structural receipts are clean: retained 107, invalid 0, unsupported 0, max lookup mismatch `1.6569708505745155e-16`, exact canonical/request-plan identities, 8 constructions/max-one/final-zero and 4040 transfer calls.

The pre-result event-driven consumer run/job `34551879267 / 103116317825` independently revalidated the artifact and selected only `NOT_CONVERGED_8193_TO_16385`. Consumer artifact `10181107144`, ZIP SHA256 `0682d03c97b4f053767a8b63d44be973fb58b6deecc1c270901014c8dce9f912`, validation SHA256 `c4eb7b0d75ce5ef3e47ae44eb6a54115e86ec4d3543e0ddcad03d97ee160e792`. Durable JM authority commit `24b55a087b3bc81c406978511e9ad47c90431a27`.

Therefore the fresh-closure CONVERGED branch is closed for this result; the only active scientific-support continuation is the already prospectively frozen canonical 8193->16385 rung.

Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, domain/masks/107-row accounting and lookup ceiling remain unchanged. Covariance restriction unauthorized; Wm_S3 unopened.

## 16385 resource boundary and active repair
Canonical 16385 is fixed at decoded SHA256 `3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975`, text/u64hex SHA256 `7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69`.

Four independent hosted telemetry roles establish real memory exhaustion under the unmodified CLASS k-output-history architecture: Python RSS reaches ~15.4–15.7 GB while MemAvailable/swap collapse, followed by process kill. Durable resource authority commit `9a2a580c078e89bcf9dca058069e756406c82a92`. This is resource `+0/+0`, not science.

Pinned CLASS-IV source audit identifies unnecessary per-k perturbation-history accumulation behind `k_output_values`. Root-cause audit commit `a8ecf4b7070068ff7efed788e9d69a253ce4ff21`. Prospectively frozen minimal execution-only patch suppresses only the history callback while preserving exact requested k-node insertion and transfer computation. Patch script commit `ca42f22cd8190454a8c3bd4b354bbc761a48ea74`, blob `e20687e933d665973c3be40598180587701fa8e0`.

The patch is not authorized for 16385 yet. Two independent canonical-8193 exact-equivalence replicas run under workflow `classiv-k-output-history-suppression-8193-equivalence-v0-1`, run `34551841749`, head `225c51fc0db4822703c24fb5743ad32b6214b4b8`, jobs `103116205677` and `103116205843`. Both must reproduce all 8 raw operand SHA256 and both pilot-response SHA256 values from the independently verified Exp073JO baseline. Memory savings alone cannot pass the gate.

Self-hosted unpatched 16385 run `34550495778` remains queued awaiting a Linux/X64 repository runner and does not supersede the established hosted OOM result.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%.** JM is a valid new NOT_CONVERGED result and selects the next rung, but numerical Layer-B support remains unresolved. Resource/process work remains `+0/+0`.

## Exact next action
Terminal-consume both 8193 history-suppression equivalence replicas. Only two exact PASS results permit patched canonical-16385 resource pilots. Only patched 16385 resource PASS permits the activated full 8193->16385 scientific-support run. No tolerance/grid/domain/mask/interpolation/estimator rescue; covariance restriction and Wm_S3 remain closed.
