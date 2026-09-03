# DSIR current-process ledger

Updated: 2026-09-03

Repository state and immutable Actions/checkpoint authority outrank chat.

## Tracked process
- experiment: Exp073CN v0.1
- gate: hosted static checkpoint/contract audit before any self-hosted launch
- audit workflow: `.github/workflows/exp073cn-static-checkpoint-contract-audit-v0-1.yml`
- resource workflow: `.github/workflows/exp073cn-wm-s3-8worker-checkpoint-resource-v0-1.yml`
- resource workflow commit: `584b3544a4785594f3607d787368400a74709688`
- prereg commit: `7a4c47a52204570abb5efbc04b583d66a93c26bf`
- driver commit: `6cd0016d061df0156ef64b705fee339c55d5ed9f`
- binding commit: `19526b27380da048b40d55a112f27ed6bed80e97`
- checkpoint namespace: `checkpoints/exp073cn-wm-s3-8worker-resource-v0-1`
- inherited immutable checkpoint: `checkpoints/exp073cm-wm-s3-resource-v0-1@d405a7a934bbd8caf464cd2a4bcb6052b8d205cd`
- expected hosted audit token: `PASS_EXP073CN_STATIC_CHECKPOINT_CONTRACT_AUDIT_V0_1`
- expected eventual resource PASS token: `PASS_EXP073CN_WM_S3_8WORKER_BAND_CHECKPOINT_RESOURCE_V0_1`
- state: PREPARED_AWAITING_HOSTED_STATIC_AUDIT_TRIGGER
- current home-runner ownership: FREE / NOT AUTHORIZED FOR Exp073CN UNTIL AUDIT PASS
- last durable Exp073CN checkpoint: none; namespace prospectively new

## Frozen decision table
- hosted audit PASS with exact artifact/provenance: write activation binding with run/job/artifact/digest, recheck all live DSIR Actions, then create the dedicated launch marker only if no competing home job exists.
- hosted audit FAIL: no home launch; diagnose first causal static/contract defect, repair prospectively and rerun hosted audit.
- resource exact mismatch: numerical/resource-plan FAIL +0/+0, no tolerance rescue.
- resource CPU fraction <0.90 or swap increase >0: resource/performance FAIL +0/+0.
- resource infrastructure/checkpoint/transport failure before frozen classification: INFRASTRUCTURE_INCOMPLETE +0/+0; preserve valid complete-band checkpoints and repair/resume only missing work.
- resource PASS: +0/+0; authorizes 8-worker per-band architecture only, then prospectively preregister full Wm_S3 A/B scientific successor.

Article-3 readiness remains Verified 52.0% | Draft/data 54.6% unless a frozen ledger explicitly changes it.
