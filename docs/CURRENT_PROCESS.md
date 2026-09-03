# DSIR current-process ledger

Updated: 2026-09-03

Repository/immutable Actions/checkpoints are authoritative.

## Active process
- experiment: Exp073CQ Wm_S3 hosted-seeded missing29-38 resource v0.2
- workflow run: `33752799918`
- workflow/head: `.github/workflows/exp073cq-v0-2-hosted-seeded-missing29-38-resource.yml` / `011852feb6d40152f4b33bde732b00520cd28f79`
- authorize job: `100640020607` SUCCESS
- self-hosted job: `100640079011` QUEUED
- checkpoint namespace: `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2`
- exact hosted seed head: `4f528424a2d2b3e32aeb4a68d73265ef9de8bd4e`
- seed contract fingerprint: `87b58bf120510bec50b21851d7ff21269689db6dcdd906cb3a14102e4a4f5f97`
- durable seed state: exact imported/read-only bands `0..28`; compute allowlist exactly `29..38`; no new numerical band yet claimed
- expected gate/token: `PASS_EXP073CQ_V0_2_WM_S3_MISSING29_38_8WORKER_HOSTED_SEEDED_RESOURCE`
- prereg commit: `71800bedbf8c23d7aee4538a0230bdac4bd5c6f3`
- driver commit: `0bf7ea195bccbb8e6458f1269640c279668d4a1f`
- home workflow commit: `31c57d7b3565aea7c6ff3edbdf978f51f652abcb`
- binding commit: `f25cdc25c9e2d4a0f6d1ec673922cda9ca3019fc`
- activation commit: `fabb0c601edcb117d7734ba1828da762b585c2db`
- launch commit: `011852feb6d40152f4b33bde732b00520cd28f79`
- hosted seed authority: run `33752529085`, job `100639147404`, token `PASS_EXP073CQ_V0_2_HOSTED_PARENT_IMPORT_SEED`, artifact `9892102247`, digest `sha256:8af123e1102f17feae01050c456983e8547306c9f59b4a72f64ccb917b55a2ae`
- hosted post-seed audit authority: run `33752695840`, job `100639693792`, token `PASS_EXP073CQ_V0_2_HOSTED_SEED_STATIC_AUDIT`, artifact `9892171765`, digest `sha256:8e9acc8142bf5bc1a441259d6884d2dc54cda8a5690a64cdef81525479c7d68b`
- home runner ownership: RESERVED EXCLUSIVELY for run `33752799918` / job `100640079011` while queued or in_progress; DO NOT launch a competing home job
- exact next action while QUEUED/RUNNING: do not duplicate; consume terminal job immediately; validate seed restoration, all new per-band checkpoints, exact first-8, swap and CPU gate
- exact next action on PASS: consume artifact/checkpoint/final receipt and keep resource gate `+0/+0`; only then preregister fresh-independent-PCL Wm_S3 A/B scientific successor
- exact next action on numerical/resource FAIL: preserve frozen negative result `+0/+0`; no tolerance rescue
- exact next action on infrastructure/software/checkpoint failure: preserve all exact-valid durable units, diagnose first causal failure, repair prospectively, hosted-audit again, resume only unfinished units

## Most recently consumed process
- experiment: Exp073CQ v0.1
- workflow run/job: `33742582807` / `100607697336`
- terminal state: FAILURE at `Exact import of immutable Exp073CP band0-28 authority`; helper/29..38/final/artifact not run
- successor v0.1 namespace remained absent; no CQ v0.1 durable unit exists
- decoded job log remains `BlobNotFound`, so no narrower cause is inferred
- classification: `INFRASTRUCTURE_OR_SOFTWARE_INCOMPLETE_AT_PARENT_IMPORT`, `+0/+0`, not scientific/resource FAIL
- clean hosted reproducer run/job `33752333426` / `100638517360` PASSed exact parent restore/import with token `PASS_EXP073CQ_HOSTED_PARENT_IMPORT_REPRODUCER_V0_1`, localizing the v0.1 failure to home environment/transport unless later logs prove otherwise

## Preserved authority
- immutable Exp073CP parent checkpoint `025629d9bb7b113bd0548ff6a32c6ee5812ae245`, contract fingerprint `32d15a39f1bcdcee0f9b9f88ebc8fd8f82eb850bb71eca4b51d95eb40f111efc`, complete bands `0..28`.
- Exp073CN remains exact-equal/swap-safe but CPU-utilization resource FAIL `+0/+0`, CPU fraction `0.19305511714998927 < 0.90`.
- Exp073CM remains historical resource/performance FAIL `+0/+0`.
- Wm_S3 angular authority remains absent.
- Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
