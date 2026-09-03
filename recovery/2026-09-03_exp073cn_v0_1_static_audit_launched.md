# Recovery — Exp073CN v0.1 hosted static checkpoint/contract audit launched

Date: 2026-09-03
Scope: DSIR only.

Repository reconciliation at iteration start found no queued/in_progress DSIR Actions and confirmed default-branch authority remained at Exp073CM resource/performance FAIL plus the nuisance quotient research note. Previously chat-reported Exp073CN commits were not present on `main` and therefore were not treated as authority.

## New prospective chain
- preregistration: `preregistration/2026-09-03_exp073cn_wm_s3_8worker_band_checkpoint_resource_v0_1.md`, commit `7a4c47a52204570abb5efbc04b583d66a93c26bf`;
- execution driver: `ci/exp073cn_wm_s3_8worker_checkpoint_resource_v0_1.py`, commit `6cd0016d061df0156ef64b705fee339c55d5ed9f`;
- self-hosted resource workflow: `.github/workflows/exp073cn-wm-s3-8worker-checkpoint-resource-v0-1.yml`, commit `584b3544a4785594f3607d787368400a74709688`;
- binding: `experiments/073cn_wm_s3_8worker_checkpoint_resource_v0_1_binding.json`, commit `19526b27380da048b40d55a112f27ed6bed80e97`;
- hosted static audit workflow: `.github/workflows/exp073cn-static-checkpoint-contract-audit-v0-1.yml`, creation commit `e13dfc8d3e53564cd462b032645cc23856ee2840`;
- current-process ledger creation commit `fece3e1c28941dd4d91807e5d30b52b55109444a`;
- audit request/trigger head `fd481905e1de1d421e6806d64de79753a303346a`.

## Frozen architecture
Exactly eight outer worker processes dynamically consume 16 independent complete-band units, with all nested BLAS/OpenMP/MKL/OpenBLAS/BLIS/NumExpr thread counts fixed to one. Each completed band is canonical `<f8` and is pushed immediately through the proven fail-closed checkpoint transport to dedicated namespace `checkpoints/exp073cn-wm-s3-8worker-resource-v0-1`.

Expensive Wm_S3 PCL is not recomputed. The workflow restores exact Exp073CM checkpoint head `d405a7a934bbd8caf464cd2a4bcb6052b8d205cd` and validates PCL SHA `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d` plus reference `[0,8)` SHA `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf` before importing them into the new contract-bound checkpoint.

Resource acceptance remains exact-only: first eight dynamically computed rows must equal the frozen 1-thread reference exactly and reproduce the same canonical SHA; swap increase must be 0 KiB; process-tree CPU fraction must be >=0.90. PASS is `+0/+0` and does not itself create Wm_S3 angular authority.

## Live process
Hosted audit run `33709966197`, job `100507141843`, head `fd481905e1de1d421e6806d64de79753a303346a` was queued after the trigger. Expected token: `PASS_EXP073CN_STATIC_CHECKPOINT_CONTRACT_AUDIT_V0_1`.

No Exp073CN home launch marker exists. DSIR-HOME-PC remains FREE and NOT AUTHORIZED for Exp073CN until the hosted audit is terminal PASS and its raw artifact/provenance is consumed.

Article-3 readiness remains Verified 52.0% | Draft/data 54.6%. All work here is resource/checkpoint/static QA `+0/+0`.
