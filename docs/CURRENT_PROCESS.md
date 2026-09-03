# DSIR current-process ledger

Updated: 2026-09-03

Repository/immutable Actions/checkpoints are authoritative.

## Active process
- experiment: Exp073CO hosted static checkpoint contract audit v0.1
- workflow run: `33713552822`
- job: `100517906229`
- branch/head: `main` / `5e5f618f39e2767f75f8c9a0b89ffa07287ce26b`
- checkpoint namespace under audit: `checkpoints/exp073co-wm-s3-full39-resource-v0-1`
- start state at last reconciliation: `queued`
- expected gate/token: `PASS_EXP073CO_STATIC_CHECKPOINT_CONTRACT_AUDIT_V0_1`
- home runner ownership: FREE; no self-hosted Exp073CO job is authorized or active
- exact next action on PASS: inspect audit artifact/digest and raw result; if valid, create activation authority only after rechecking all queued/in_progress DSIR Actions, then launch exactly one checkpointed Exp073CO home resource run
- exact next action on FAIL: diagnose first static/contract defect, repair prospectively, rerun a NEW post-repair hosted audit; no home launch
- exact next action on BLOCKED/infrastructure failure: preserve current implementation/binding, diagnose first causal failure, repair only infrastructure/control path, then rerun hosted audit

## Most recently consumed process
- experiment: Exp073CN Wm_S3 8-worker per-band checkpoint resource v0.1
- workflow run: `33710044833`
- authorize job: `100507373744` SUCCESS
- self-hosted job: `100507407911` terminal at frozen final classification
- branch/head: `main` / `8eb042e206497a1579877bffe0a588ed8ec15870`
- checkpoint namespace: `checkpoints/exp073cn-wm-s3-8worker-resource-v0-1`
- last durable checkpoint: `71e4602212cb2056bc178dfed104bcacf388489c`
- authority artifact: `9876628517`
- artifact digest: `sha256:76c5817e01cf60c96ebf796e67c7dda866d6290405e1d557a2512d35416807b1`
- exact first-8: PASS
- swap safety: PASS
- CPU fraction: `0.19305511714998927 < 0.90`
- observed terminal status: `FAIL_EXP073CN_WM_S3_8WORKER_CPU_TARGET_V0_1`
- classification: resource/performance FAIL `+0/+0`, not scientific arithmetic FAIL

## Exp073CO frozen chain so far
- preregistration commit: `95133fc97b9cc013a58c82aed583ee79f7737979`
- driver commit: `0d0c6032f8af0def02f9e2c15abc3c22bfd049e0`
- execution workflow commit: `eefb6767ab9452d2c74a1fa36f6f59a42bdb1ca9`
- binding commit: `b84f4df108b6015c2909d8a00953df1fd0a43eb8`
- static-audit workflow commit: `10ea8a67f9caef843d4dfb02c9f3d9b7c01344dc`
- audit launch marker/head: `5e5f618f39e2767f75f8c9a0b89ffa07287ce26b`
- home execution authorized: NO
