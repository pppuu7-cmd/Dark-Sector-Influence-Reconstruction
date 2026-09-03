# DSIR current-process ledger

Updated: 2026-09-03

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. DSIR only; RTK/RQIR excluded.

## Active process
- experiment/process: Exp073CR v0.3 r1 prospective control repair audit
- hosted audit run/job: `33770476672` / `100699131834`
- audit head: `3c3086489195bdc610ec026772a148fec5b15625`
- state at last reconciliation: QUEUED
- expected token: `PASS_EXP073CR_V0_3_R1_NPROC_CONTROL_AUDIT`
- repaired home-workflow commit: `9eafc1c431f508d7a34800328b6718f146b346b5`
- audit-workflow commit: `6fc6db1d0e074d02ce6e58e7ed58977e76a18b75`
- frozen seed namespace/head: `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3` / `cb408d4edb2a73413db8d3181e9cb1680dc19276`
- seed fingerprint: `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`
- frozen resource architecture remains: exactly 8 outer workers, max 8 in flight, nested threads=1, 64 source-order ll3 shards over bands 29..38, durability-before-refill, CPU>=0.90, swap increase=0
- home runner ownership: FREE; repaired home relaunch is BLOCKED until hosted r1 audit PASS
- exact next action on hosted audit PASS: verify raw token, update activation with the PASS provenance, recheck `0 queued/0 in_progress` competing home runs, launch exactly one repaired home continuation
- exact next action on hosted audit FAIL: diagnose first failing audit assertion; prospective smallest repair; no home launch

## Newly consumed Exp073CR v0.3 home attempt
- run/head: `33770178685` / `3404eccc347d5f44f1cdc1514078d411fce1682b`
- authorize job `100698111100`: SUCCESS
- home job `100698177477`: FAILURE in `Bind v0.3 runtime` before seed restore or compute
- first causal raw-log failure: `test "$(nproc)" = "8"` exited 1 before Python/static-audit output
- secondary fallout: `CR_ROOT` unbound in always-run artifact-preparation path; not first cause
- classification: **INFRASTRUCTURE/CONTROL-PLANE FAILURE `+0/+0`**; no shard computed, no resource/science classification
- repair: machine guard prospectively changed to `nproc>=8`; actual outer worker count remains exactly 8; nested threads=1; frozen CPU threshold remains 0.90; numerical arithmetic unchanged
- immutable note: `recovery/2026-09-03_exp073cr_v0_3_home_bind_failure_r1_repair.md`

## Most recently completed resource gate — Exp073CQ v0.2
- run/job/head: `33752799918` / `100640079011` / `011852feb6d40152f4b33bde732b00520cd28f79`
- terminal checkpoint: `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2` / `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`
- exact first-8 array/SHA equality PASS; swap increase `0 KiB` PASS
- CPU fraction `0.6638297425690942 < 0.90`
- status `FAIL_EXP073CQ_V0_2_WM_S3_CPU_TARGET`
- classification: RESOURCE/PERFORMANCE FAIL `+0/+0`, not scientific FAIL
- artifact `9897551836`, digest `sha256:0f10c863ee65f3d7c27177a324cafe2830e6b8b1096da054e35c638b26d6104c`

## Preserved authority
- Wm_S1 Track-A exact PASS and admitted Wm_S2 authority remain preserved.
- Wm_S3 angular scientific authority remains absent.
- frozen science boundaries remain unchanged.
- Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
