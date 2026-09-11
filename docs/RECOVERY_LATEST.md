# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_8193_EQUIVALENCE_PASS_16385_PATCHED_RESOURCE_ACTIVE_V111.md`, creation commit `ff18431ee6713294997c5b2701ad6abf503e7187`. Earlier recovery notes remain immutable history.

## Scientific frontier
Recovered Exp073JM canonical 4097->8193 remains independently verified `COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Source run/job `34548136827 / 103105092111`, source artifact `10181101449`, durable authority commit `24b55a087b3bc81c406978511e9ad47c90431a27`.

The maximum canonical 4097->8193 relative component difference is `0.01070806986822778`, or `10.70806986822778` times strict `1e-3`. Structural receipts remain clean: retained 107, invalid 0, unsupported 0, max lookup mismatch `1.6569708505745155e-16`, exact canonical/request-plan identities, eight constructions/max-one/final-zero and 4040 transfer calls. The only active scientific-support continuation is canonical 8193->16385. Covariance restriction unauthorized; Wm_S3 unopened.

## 8193 history-suppression equivalence is exact PASS
The prospectively frozen execution-only CLASS-IV patch that suppresses requested-k perturbation-history accumulation while retaining exact requested-node insertion and transfer computation has now passed two independent canonical-8193 exact-equivalence replicas.

Source workflow run `34551841749`, head `225c51fc0db4822703c24fb5743ad32b6214b4b8`:
- replica 1 job/artifact `103116205677 / 10181363100`, ZIP SHA256 `4d59f4f1add8bb2c730c6558291dd8340a57d884c6c3ab47716e5ae4a5062d5b`, equivalence SHA256 `538cc0e43368aaa3e6f8ca62d14299b9daa15823d0ec2afe3b56ff4c62d2cb58`;
- replica 2 job/artifact `103116205843 / 10181345079`, ZIP SHA256 `ac0f671684a8d0f7f4b9d6a60f93d1c844dc217a152dd1702b1104edfcfe4b23`, equivalence SHA256 `0e355186efb76a957dd247fa4cd71d7300f84bbec72fa1020ada1d85f24aa504`.

Both independently reproduce all eight raw Exp073JO operand SHA256 values and both pilot-response SHA256 values exactly. Their shared `result.json` SHA256 is `55f30427ddd867b30cd529ab6d954064d928dcf25b7fa35dfccd0012cb6092c9`; shared patch receipt SHA256 is `628d92c1b5bef05e776b6b510d3edc2b45513320310a1e616cef849ca7601f09`; canonical node identity is exact; unsupported=0; lookup mismatch=`1.6569708505745155e-16`; lifecycle is four sequential constructions/max-one-live/final-zero. Classification: `CLASSIV_K_OUTPUT_HISTORY_SUPPRESSION_8193_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0`.

Durable aggregate equivalence authority commit: `600c5567f8fe3f42901e7034372b8e3849050eb0`. This authorizes the patch for canonical-16385 resource testing only and creates no scientific authority.

## Current authoritative process: patched canonical-16385 resource gate
GitHub-native event-driven workflow `classiv-history-suppression-16385-resource-after-equivalence-v0-1` was prospectively added at commit `182d9dac9dabe8855e885749f4835a7ed589f5fe` and activated only after the source equivalence workflow completed.

Current run `34552645551`, head `182d9dac9dabe8855e885749f4835a7ed589f5fe`, is **IN_PROGRESS** with two independent hosted resource replicas:
- replica 1 job `103118559536`;
- replica 2 job `103118559274`.

Both have already independently verified both exact-equivalence source artifacts, passed frozen 16385 identities, installed the exact numerical/build stack, built pinned CLASS-IV with the prospectively frozen 18432/524288 capacity/parser values plus history suppression, and are now executing the patched canonical-16385 four-role resource pilot with telemetry.

Historical self-hosted unpatched 16385 run `34550495778` may remain queued awaiting Linux/X64; it is diagnostic only and cannot supersede hosted resource authority.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%.** Scientific Layer-B support remains unresolved; equivalence/resource work remains `+0/+0`.

## Exact next action
Terminal-consume both patched-16385 resource replicas and independently verify raw logs plus artifact/result/telemetry/patch hashes and provenance. Only replicated patched canonical-16385 resource PASS permits exactly one same-process/max-one-live full 8193->16385 scientific-support run under the unchanged frozen classifier. Resource/infrastructure failure remains `+0/+0` and must not weaken tolerance, h, grid/domain/mask/interpolation/estimator or provenance gates. Covariance restriction and Wm_S3 remain closed.
