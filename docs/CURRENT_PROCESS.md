# DSIR current-process ledger

Updated: 2026-09-03

Repository, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. DSIR only; RTK/RQIR excluded.

## Active process
- experiment: Exp073CR Wm_S3 ll3-sharded resource v0.3, r2 split-bind continuation
- workflow run/head: `33771012683` / `1e4345286d8816ff3d850d3a39b8aff0645948df`
- hosted authorize job: `100700943092` QUEUED at last reconciliation
- self-hosted job: not yet instantiated at last reconciliation; once instantiated it exclusively owns DSIR-HOME-PC while queued/in_progress
- checkpoint namespace/head to restore: `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3` / `cb408d4edb2a73413db8d3181e9cb1680dc19276`
- seed fingerprint: `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`
- frozen resource architecture unchanged: exactly 8 outer workers, max 8 in flight, nested threads=1, 64 source-order ll3 shards over bands 29..38, durability-before-refill, exact reconstruction/reference equality, CPU>=0.90, swap increase=0
- r2 exact-home diagnostic run/job `33770780033` / `100700156146`: SUCCESS; raw token `PASS_EXP073CR_V0_3_R2_HOME_BIND_DIAGNOSTIC`; measured `nproc=8`, online CPUs=8, Python 3.14.4, bound lineage/py_compile/static audit/exact seed identity all PASS
- r2 split-bind hosted audit run/job `33770942410` / `100700703465`: SUCCESS; raw token `PASS_EXP073CR_V0_3_R2_SPLIT_BIND_CONTROL_AUDIT`
- split-bind workflow commit: `3f78577a12d5c6943f713c1451948ce00b8acc26`
- activation commit: `1e4345286d8816ff3d850d3a39b8aff0645948df`
- exact next action while queued/running: do not duplicate; consume terminal state immediately; verify bind steps, exact seed restore, all shard receipts, durability-before-refill, complete-band exact reconstruction/reference equality, swap and frozen CPU metric
- on resource PASS: classify `+0/+0`, persist final provenance, then only preregister scientifically permitted fresh-independent-PCL Wm_S3 A/B successor
- on resource FAIL: preserve frozen negative resource result `+0/+0`, no threshold/arithmetic rescue
- on infrastructure/software FAIL: preserve complete durable shards, identify first distinct failing step, smallest prospective repair + hosted audit, resume unfinished work only

## Preceding r1 continuation
- run/head `33770577708` / `8eded6a41271e77750a0206ba2766fbbb7819dc3`; authorize `100699474546` SUCCESS; home `100699512748` FAILURE in combined bind before seed/compute
- classification: INFRASTRUCTURE/CONTROL-PLANE INCOMPLETE `+0/+0`; no shard computed
- individual r2 diagnostic proved CPU/Python/lineage/compile/static/seed controls independently healthy on exact runner, so split-bind is a control-plane isolation repair only
- immutable notes: `recovery/2026-09-03_exp073cr_v0_3_r1_bind_failure_and_r2_diagnostic.md` and `recovery/2026-09-03_exp073cr_v0_3_r2_diagnostic_pass_split_bind_launch.md`

## Latest completed resource result
- Exp073CQ v0.2 run/job `33752799918` / `100640079011`, terminal checkpoint `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`
- exact first-8 equality PASS; swap 0 KiB PASS; CPU `0.6638297425690942 < 0.90`
- status `FAIL_EXP073CQ_V0_2_WM_S3_CPU_TARGET`; RESOURCE/PERFORMANCE FAIL `+0/+0`, not scientific FAIL
- artifact `9897551836`, digest `sha256:0f10c863ee65f3d7c27177a324cafe2830e6b8b1096da054e35c638b26d6104c`

## Preserved authority
- Wm_S1 Track-A exact PASS and admitted Wm_S2 authority preserved.
- Wm_S3 angular scientific authority absent.
- frozen science boundaries unchanged.
- Article-3 readiness **Verified 52.0% | Draft/data 54.6%**.
