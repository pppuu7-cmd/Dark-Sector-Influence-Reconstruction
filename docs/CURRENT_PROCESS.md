# DSIR current-process ledger

Updated: 2026-09-03

Repository, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. DSIR only; RTK/RQIR excluded.

## Active process
- process: Exp073CR v0.3 r2 home bind diagnostic; infrastructure-only `+0/+0`, no numerical Wm_S3 compute and no checkpoint write
- workflow run/head: `33770780033` / `87ebc2bd850aba7beea6d6f84970ed9241a3e908`
- self-hosted job: `100700156146` IN_PROGRESS at last reconciliation on `DSIR-HOME-PC`
- diagnostic workflow commit: `a607cb2a548dfdb569445524b03639ddfa7b298b`
- purpose: measure/corroborate the first bind failure with distinct steps for host `nproc`/CPU topology, system Python, git lineage, py_compile, static audit, and exact read-only seed identity
- frozen seed namespace/head remains untouched: `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3` / `cb408d4edb2a73413db8d3181e9cb1680dc19276`
- seed fingerprint: `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`
- home runner ownership: RESERVED EXCLUSIVELY for diagnostic run `33770780033` / job `100700156146` while in_progress; do not launch any competing home workload
- exact next action on diagnostic terminal: consume raw log immediately; if `nproc<8`, freeze the current 8-worker CPU resource route as runner-capacity BLOCKED without oversubscription/threshold rescue; otherwise repair only the first distinct failed bind dependency, hosted-audit it, then resume from the same seed

## Exp073CR v0.3 repaired continuation just consumed
- run/head `33770577708` / `8eded6a41271e77750a0206ba2766fbbb7819dc3`
- authorize job `100699474546` SUCCESS
- home job `100699512748` FAILURE in the combined `Bind v0.3 runtime`; seed/helper/compute/final all skipped
- decoded log confirms repaired shell source includes `nproc>=8`, git lineage, py_compile and static audit but only exposes generic exit 1; exact failing subcommand is not evidenced, so no narrower cause is claimed
- classification: INFRASTRUCTURE/CONTROL-PLANE INCOMPLETE `+0/+0`; zero shards computed; seed unchanged
- immutable note: `recovery/2026-09-03_exp073cr_v0_3_r1_bind_failure_and_r2_diagnostic.md`

## Previous r1 control audit
- hosted audit run/job `33770476672` / `100699131834`: SUCCESS
- raw token `PASS_EXP073CR_V0_3_R1_NPROC_CONTROL_AUDIT`
- repaired workflow commit `9eafc1c431f508d7a34800328b6718f146b346b5` preserved exactly 8 outer workers, nested=1, 64 shard geometry/order, CPU>=0.90, swap=0; only changed machine guard from equality to availability form

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
