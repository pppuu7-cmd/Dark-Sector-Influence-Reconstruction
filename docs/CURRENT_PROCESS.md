# DSIR current-process ledger

Updated: 2026-09-03

Repository, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. DSIR only; RTK/RQIR excluded.

## Active process
- experiment: Exp073CR Wm_S3 ll3-sharded resource v0.3, prospective r1 control repair
- workflow run/head: `33770577708` / `8eded6a41271e77750a0206ba2766fbbb7819dc3`
- authorize job: `100699474546` IN_PROGRESS at last reconciliation
- self-hosted job: not yet instantiated at last reconciliation; when created it exclusively owns DSIR-HOME-PC while queued/in_progress
- checkpoint namespace/head to restore: `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3` / `cb408d4edb2a73413db8d3181e9cb1680dc19276`
- seed fingerprint: `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`
- frozen resource architecture: exactly 8 outer workers, max 8 in flight, nested threads=1, 64 source-order ll3 shards over bands 29..38, durability-before-refill, CPU>=0.90, swap increase=0; arithmetic unchanged
- repaired workflow commit: `9eafc1c431f508d7a34800328b6718f146b346b5`
- r1 hosted audit: run/job `33770476672` / `100699131834` SUCCESS; raw token `PASS_EXP073CR_V0_3_R1_NPROC_CONTROL_AUDIT`
- repaired activation commit: `8eded6a41271e77750a0206ba2766fbbb7819dc3`
- exact next action while queued/running: do not duplicate; consume terminal result immediately; verify seed/fingerprint, all shard receipts, exact reconstruction, durability ordering, swap and CPU metric
- on resource PASS: classify +0/+0, persist authority, then only preregister scientifically permitted fresh-independent-PCL Wm_S3 A/B successor
- on resource FAIL: preserve frozen negative resource result +0/+0, no threshold rescue
- on infrastructure/software FAIL: diagnose first causal failure and resume only complete-checkpoint-safe unfinished work

## Preceding Exp073CR v0.3 attempt
- run/job `33770178685` / `100698177477`: infrastructure/control-plane FAILURE before seed restore/compute
- raw first cause: `test "$(nproc)" = "8"` failed in `Bind v0.3 runtime`; no Python/static audit or shard compute occurred
- repair changes host availability guard only to `nproc>=8`; actual compute remains exactly 8 outer workers; CPU threshold remains 0.90
- immutable note: `recovery/2026-09-03_exp073cr_v0_3_home_bind_failure_r1_repair.md`

## Latest completed resource result
- Exp073CQ v0.2 run/job `33752799918` / `100640079011`, terminal checkpoint `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`
- exact first-8 equality PASS; swap 0 KiB PASS; CPU `0.6638297425690942 < 0.90`
- status `FAIL_EXP073CQ_V0_2_WM_S3_CPU_TARGET`; RESOURCE/PERFORMANCE FAIL +0/+0, not scientific FAIL
- artifact `9897551836`, digest `sha256:0f10c863ee65f3d7c27177a324cafe2830e6b8b1096da054e35c638b26d6104c`

## Preserved authority
- Wm_S1 Track-A exact PASS and admitted Wm_S2 authority preserved.
- Wm_S3 angular scientific authority absent.
- frozen science boundaries unchanged.
- Article-3 readiness **Verified 52.0% | Draft/data 54.6%**.
