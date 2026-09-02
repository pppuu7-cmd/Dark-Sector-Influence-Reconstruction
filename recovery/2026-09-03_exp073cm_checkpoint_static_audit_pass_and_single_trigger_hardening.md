# Exp073CM checkpoint static audit PASS + single-trigger hardening

**Date:** 2026-09-03

Repository state and immutable GitHub Actions evidence are authoritative.

## Universal checkpoint audit authority

The hardened Exp073CM self-hosted resource chain is prospectively frozen as:

- preregistration `preregistration/2026-09-03_exp073cm_wm_s3_universal_checkpoint_direct8_resource_v0_1.md`, commit `914a57e45ee98b6ebbb8830a524ec59bfef0c78b`;
- universal checkpoint policy `docs/SELF_HOSTED_CHECKPOINT_POLICY.md`, commit `f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427`;
- PCL helper `ci/exp073cm_memory_stable_wm_s3_pcl_v0_1.py`, commit `8a5f9f5e0341d24ee843f3097199075c50ab2d02`;
- checkpointed resource driver `ci/exp073cm_checkpointed_wm_s3_resource_v0_1.py`, commit `585999ec149cb1f5774eb909cbedcdc19f48e6b9`;
- robust checkpoint transport `ci/dsir_checkpoint_git_sync_v0_2.sh`, commit `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`;
- frozen range helper commit `fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22`;
- hardened workflow `.github/workflows/exp073cm-wm-s3-universal-checkpoint-resource-v0-1.yml`, commit `90b6d128a0a9e44cdbe4d76b9c134e31cda6cc7f`;
- binding `experiments/073cm_wm_s3_universal_checkpoint_resource_v0_1_binding.json`, commit `ee4524903b50966163299b0a9cab4fc7f82bbaa4`;
- activation `ci/exp073cm_wm_s3_universal_checkpoint_resource_v0_1.activation.json`, commit `612aa53b48bf61d98c4e3c4a7d2acb70ad8aaba2`.

Hosted checkpoint static audit v0.2 run `33688716047`, job `100442221208`, completed `success`. Authority artifact `9869146766`, name `exp073cm-checkpoint-static-audit-v0-2-2c06bf7c5983e0e757c39813347594360e3c6d9a`, digest `sha256:9ded96b2a75dc6cf9c8c7a53b77cba7ca1f8ba9c91213afcd5490df9cda51270`.

The audit verified fail-closed semantics for: restore-before-actual-compute; four durable remote push boundaries (`pcl`, `reference`, `target`, `final`); completed-stage push before the next expensive stage; no direct DES-server fetch on home; original dtype validation; payload SHA/receipt binding; exact final recomputation from restored reference+target; and contract-tamper rejection. Audit result is checkpoint/infrastructure QA `+0/+0`.

Earlier hosted audit attempts were infrastructure/audit-harness incomplete only: run `33688373062` job `100441135624` lacked NumPy; run `33688456119` job `100441400558` had a false-positive whole-YAML ordering assertion; run `33688598762` job `100441853698` had a syntax error in the v0.2 audit harness before execution. None scheduled or executed self-hosted science and none classify resource/scientific repeatability.

## Single-trigger hardening

A non-authoritative duplicate workflow `.github/workflows/exp073cm-wm-s3-universal-checkpoint-direct8-resource-v0-1.yml` shared the same launch marker and could have produced duplicate Exp073CM home jobs. It was retired before scientific resource dispatch at commit `d1cd0da8588482afecb25a983e3525c1d335bfab`.

The sole permitted Exp073CM resource workflow is now `.github/workflows/exp073cm-wm-s3-universal-checkpoint-resource-v0-1.yml` at frozen path-history commit `90b6d128a0a9e44cdbe4d76b9c134e31cda6cc7f` with binding/activation above. The duplicate helper/binding debris is non-authoritative and must not be used as dispatch authority.

The old launch attempt at head `db7257356d7450d002942078cd5d78e48fac468c` produced only fail-closed hosted authorization failures before any self-hosted scheduling. It creates no scientific/resource authority.

## Frozen numerical/resource question

Unchanged: Wm_S3 means source bin 3; signature `(0,2,0,2)`; NSIDE=4096; `L=12288`; 39 bands; Wm `TE <- TE`; canonical `<f8`; benchmark bands `[0,8)`; threads 1 versus 8; exact `np.array_equal` plus canonical SHA; target swap increase `0 KiB`; process CPU fraction of 8 CPUs `>=0.90`; no tolerance/ULP/rounding/averaging/smoothing rescue.

The dedicated durable remote namespace is `checkpoints/exp073cm-wm-s3-resource-v0-1`. Stages are `pcl -> reference -> target -> final`. The PCL stage is atomic and may repeat only itself if interrupted before its durable push.

## Readiness and next gate

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%** (exact Draft/data `54.57142857142857%`). Checkpoint/resource QA gives `+0/+0`.

Exact next gate: after re-reading current repository authority and confirming zero queued/in-progress DSIR runs, dispatch only the hardened Exp073CM resource workflow. Hosted authorization must PASS before the self-hosted checkpointed-resource job may schedule. Once self-hosted is queued/in-progress, DSIR-HOME-PC is exclusively owned by that run and no competing self-hosted task or unnecessary push is permitted.
