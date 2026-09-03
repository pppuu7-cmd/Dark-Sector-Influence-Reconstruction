# DSIR current-process ledger

Updated: 2026-09-03

## Authoritative running/queued process

- State: **NONE**
- GitHub Actions queued: 0 at last pre-write check.
- GitHub Actions in_progress: 0 at last pre-write check.
- DSIR-HOME-PC ownership: **FREE**.
- No self-hosted job is authorized solely by this ledger.

## Current frontier process/gate

- Experiment: `Exp073CN v0.2` prospective Wm_S3 8-core checkpointed resource qualification.
- Development branch: `exp073cn-8core-resource`.
- v0.1 disposition: `BLOCKED_PRE_EXECUTION_CHECKPOINT_CONTROL`, recovery commit `e1e5a191fba649a2a0c9fb89a4b794386fe44055`; no authorized v0.1 home execution exists.
- v0.2 preregistration commit: `32b3f7ff9bd6feebd36b169ec60ed97dd36860f5`.
- Checkpoint namespace reserved by preregistration: `checkpoints/exp073cn-wm-s3-8core-resource-v0-2`.
- Workflow/run/job: **not yet created/launched**.
- Activation/source head: **not yet frozen**.
- Start time: not applicable.
- Expected PASS token: `PASS_EXP073CN_WM_S3_8CORE_CHECKPOINTED_RESOURCE_V0_2`.
- Current state: **BLOCKED_PENDING_IMPLEMENTATION_AND_HOSTED_AUDIT**.
- Last durable checkpoint: none for v0.2; no v0.2 self-hosted compute has occurred.

## Exact next actions

### Before any home execution

1. Implement v0.2 execution/restore/checkpoint/reassembly/comparator chain without changing frozen Wm_S3 arithmetic.
2. Bind immutable input/reference identities and final execution/workflow/helper SHAs in an activation binding.
3. Add a hosted static/regression audit that checks the final chain, including restore-before-compute and per-complete-band durable remote checkpoint admission.
4. Run that hosted audit and consume its logs/artifact/token.
5. Only an exact audit PASS may authorize one noncompeting v0.2 self-hosted resource job, after another live queued/in_progress check.

### On resource SUCCESS

Record immutable run/job/artifact/digest/checkpoint provenance as `+0/+0`; freeze only the resource architecture explicitly authorized by the v0.2 contract; then prospectively preregister the full Wm_S3 A/B scientific successor. Do not claim Wm_S3 authority from resource PASS alone.

### On exact/resource FAIL

Record the corresponding frozen negative resource result `+0/+0`, with no tolerance rescue. Move to the next prospectively justified resource architecture; do not rewrite Exp073CM, Exp073CN v0.1, or frozen science.

### On infrastructure/BLOCKED

Diagnose the first causal failure, preserve every verified durable unit, prospectively repair only infrastructure/checkpoint/control code, re-audit hosted, and resume only missing work. Never recompute verified expensive stages unnecessarily.
