# DSIR current-process ledger

Updated: 2026-09-03

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoint branches are authoritative. DSIR only; RTK/RQIR excluded.

## Active process
- experiment: Exp073CR Wm_S3 ll3-sharded resource v0.3
- workflow run: `33770178685`
- workflow/head: `.github/workflows/exp073cr-v0-3-wm-s3-ll3-sharded-resource.yml` / `3404eccc347d5f44f1cdc1514078d411fce1682b`
- authorize job: `100698111100` SUCCESS
- self-hosted job: `100698177477` QUEUED at last live reconciliation
- checkpoint namespace: `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3`
- exact hosted seed head: `cb408d4edb2a73413db8d3181e9cb1680dc19276`
- seed contract fingerprint: `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`
- source parent terminal checkpoint: Exp073CQ v0.2 `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`
- resource geometry: frozen bands `29..38` represented as 64 source-order ll3 shards; exactly 8 outer workers; nested threads=1; max 8 in flight; durability-before-refill mandatory
- frozen CPU gate: `cpu_fraction >= 0.90`; positive swap increase forbidden
- candidate SHA256: `d48e46197b48a6fcdf7d3eb3b0817973a2eadb25bbb617e7b8060c8c17209462`
- heavy-first queue SHA256: `3ba315d9bc24883ef746d92e785e0a040f9b13e751f59dda9a93e825a6390db4`
- prereg commit: `fb10a589ee5ac03f478160c9cfd28484169e48ca`
- driver commit: `365fd7a8527b2dafe4785f95fa104276788c11d1`
- self-hosted workflow commit: `85993d73565c3fc4d1389cc942bc69073b89d89e`
- hosted seed audit workflow commit: `5f5a7a060b17e11b0f53453d6ca6898cda00d2fd`
- binding commit: `0e0d13a6f7736eb56689d57c3557410007ec48d2`
- activation commit: `3404eccc347d5f44f1cdc1514078d411fce1682b`
- hosted audit authority: run `33768977707`, job `100694004982`, tokens `PASS_EXP073CR_V0_3_SOURCE_ORDER_STATIC_AUDIT`, `PASS_EXP073CR_HOSTED_AUTHORITATIVE_LL3_BITWISE_REGRESSION_V0_1`, `PASS_EXP073CR_V0_3_HOSTED_SEED_STATIC_BITWISE_AUDIT`, artifact `9898817387`, digest `sha256:6d0435cfb99e4c05c49a5e61f8944d85a786820e3bf2f0913135b263bb0c734d`
- home runner ownership: RESERVED EXCLUSIVELY for run `33770178685` / job `100698177477` while queued or in_progress; DO NOT launch a competing home job
- exact next action while QUEUED/RUNNING: do not duplicate; consume terminal result immediately; validate exact seed restore, all shard receipts, durability ordering, complete-band reconstruction equality, swap and frozen CPU gate
- exact next action on resource PASS: classify `+0/+0`, commit final provenance/recovery, then preregister only the scientifically permitted fresh-independent-PCL Wm_S3 A/B successor
- exact next action on resource/numerical FAIL: preserve as frozen negative resource result `+0/+0`; do not weaken threshold or arithmetic
- exact next action on infrastructure/software/checkpoint FAIL: preserve all complete durable shards, diagnose first causal failure, prospective smallest repair + hosted audit, resume unfinished shards only

## Most recently consumed authoritative process — Exp073CQ v0.2
- run/job: `33752799918` / `100640079011`; head `011852feb6d40152f4b33bde732b00520cd28f79`
- terminal checkpoint: `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2` / `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`
- final receipt: complete `<f8 [39,12288]`; exact first-8 array/SHA equality PASS; swap increase `0 KiB` PASS
- measured CPU fraction: `0.6638297425690942`; frozen minimum `0.90`
- terminal token/status: `FAIL_EXP073CQ_V0_2_WM_S3_CPU_TARGET`
- classification: **RESOURCE/PERFORMANCE FAIL `+0/+0`**, not Wm_S3 scientific arithmetic FAIL
- artifact `9897551836`, digest `sha256:0f10c863ee65f3d7c27177a324cafe2830e6b8b1096da054e35c638b26d6104c`

## Recovery correction
- `recovery/2026-09-03_exp073cr_v0_3_driver_lineage_correction.md` is authoritative for the v0.3 driver SHA. The correct bound driver commit is `365fd7a8527b2dafe4785f95fa104276788c11d1`.

## Preserved authority
- Wm_S1 Track-A exact PASS remains preserved.
- admitted Wm_S2 authority remains preserved.
- Exp073CM and Exp073CN remain historical resource/performance FAIL `+0/+0`.
- Wm_S3 angular scientific authority remains absent.
- frozen science boundaries remain unchanged.
- Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
