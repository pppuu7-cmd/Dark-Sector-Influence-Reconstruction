# DSIR current-process ledger

Updated: 2026-09-03

Repository, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. DSIR only; RTK/RQIR excluded.

## Active process
- experiment: Exp073CR Wm_S3 ll3-sharded resource v0.3, r3 affinity-CPU control repair
- workflow run/head: `33771269117` / `023fcfa28f0eb904656c76e55c55d821e50c8155`
- hosted authorize job: `100701802991` SUCCESS
- self-hosted job: `100701857748` IN_PROGRESS at last reconciliation
- live step: `Compute 64 frozen shards with durability-before-refill` IN_PROGRESS
- completed prerequisite steps: affinity CPU bind PASS; exact lineage PASS; bound Python compile PASS; source-order static audit PASS; NaMaster 2.7 PASS; exact hosted-seed restore PASS; exact helper compile/frozen geometry PASS
- checkpoint namespace/seed head: `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3` / `cb408d4edb2a73413db8d3181e9cb1680dc19276`
- seed fingerprint: `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`
- frozen resource architecture unchanged: exactly 8 outer workers, max 8 in flight, nested threads=1, 64 source-order ll3 shards over bands 29..38, durability-before-refill, exact reconstruction/reference equality, CPU>=0.90, swap increase=0
- r3 resource workflow commit: `d7bf00a5501367899472c861317fc24d83a6c4df`
- r3 hosted audit run/job: `33771208922` / `100701597029` SUCCESS; raw token `PASS_EXP073CR_V0_3_R3_AFFINITY_CPU_CONTROL_AUDIT`
- r3 activation commit: `023fcfa28f0eb904656c76e55c55d821e50c8155`
- home runner ownership: RESERVED EXCLUSIVELY for run `33771269117` / job `100701857748`; do not launch any competing home workload
- exact next action while running: do not duplicate; use only independent non-biasing work; on terminal immediately consume checkpoint/final receipt/artifact and classify against frozen gate
- exact next action on resource PASS: classify `+0/+0`, persist authority, then only preregister the scientifically permitted fresh-independent-PCL Wm_S3 A/B successor
- exact next action on resource FAIL: preserve frozen negative resource result `+0/+0`; no threshold/arithmetic rescue
- exact next action on infrastructure/software FAIL: preserve complete durable shards, diagnose first causal failure, smallest prospective repair + hosted audit, resume unfinished shards only

## Exact r2 control-plane cause now closed
- prior run/job `33771012683` / `100700992523` failed before seed/compute in distinct `Bind host CPU availability`.
- raw log under job-level `OMP_NUM_THREADS=1` printed `home_nproc=1`; the exact-home diagnostic without that job-level pin had measured 8 online logical CPUs.
- hosted r3 audit independently reproduced `omp_pinned_nproc=1`, proving GNU `nproc` was an invalid availability probe after nested OpenMP pinning.
- r3 repaired only the probe by using scheduler affinity (`os.sched_getaffinity`) while retaining nested pins, exact 8 outer workers, CPU threshold .90 and all numerical/resource criteria.
- classification of r2 attempt: INFRASTRUCTURE/CONTROL-PLANE FAILURE `+0/+0`; zero shards computed; seed unchanged.
- immutable note: `recovery/2026-09-03_exp073cr_v0_3_r2_nproc_omp_cause_r3_running.md`.

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
