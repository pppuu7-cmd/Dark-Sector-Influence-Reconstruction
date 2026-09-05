# DSIR current-process ledger

Updated: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical negative/infrastructure results remain immutable. Current scientific target is `WW_S0_S0`.

## Authoritative heavy process — Exp073DT WW_S0_S0 attempt 5
- run `33940588308`, attempt `5`;
- hosted preflight job `101374977192`: SUCCESS;
- self-hosted science job `101374976626`: **QUEUED** at latest live reconciliation;
- head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`;
- source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1`, `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`;
- on SUCCESS: consume raw A/B exact evidence and Exp073EB six-stage provenance before any WW_S0_S0 authority;
- on scientific exact FAIL: preserve as negative science and move to next allowed branch;
- on runner/infrastructure failure: diagnose first causal failure and resume only from fail-closed verified durable checkpoints;
- **DSIR-HOME-PC RESERVED BY Exp073DT attempt 5**. No competing self-hosted heavy task may launch.

### Attempt 4 immutable outcome
Attempt 4 self-hosted job `101288014666` ended `INFRASTRUCTURE_RUNNER_SHUTDOWN +0/+0`: GitHub log records a runner shutdown signal at `2026-09-05T20:43:43Z`, then cancellation. Before shutdown, live exclusivity, PyMaster 2.7 and `DSIR_OMP_TEAM=8` checks passed. Terminal artifact upload was skipped; therefore no scientific result was scored. No science criterion was changed. Attempt 5 was dispatched only after live Actions reconciliation found zero queued and zero in-progress runs.

## Direct cross-workspace adapter closure — Exp073EK terminal PASS
Exp073EK run/job `33988956806 / 101367596573`, head `51f8a7d7dd481e79b734ba174bffa29236f2fc0b`, artifact `9976033816`, GitHub artifact ZIP digest `sha256:f39351cddec695559686126fc15e212556eea370fe3eeab73d5f20f80c288c06`.

Frozen token `PASS_EXP073EK_DIRECT_PUBLIC_BPW_ADAPTER_EXACT_V0_1`; classification `DIRECT_PUBLIC_BPW_ADAPTER_EXACT +0/+0`. Two independent reloads of the same serialized distinct S0->S1 PyMaster 2.7 workspace followed by only public `get_bandpower_windows()` were bitwise identical. Full A/B SHA `aa883a13c305641e6e1aab5feca4692a8da1cdbcca16e8c124f12e601608d628`; selected `EE<-EE` A/B SHA `9e7a0e169d752e56d4a1f14244c58ac9a14a5c1a3782c27b3a6562a69cb0cf5e`; full and selected `numpy.array_equal=true`; no tolerance rescue.

This is support/readiness only. It qualifies direct reload + public BPW as the sole currently exact cross-workspace adapter candidate. It does not create WW authority. A separate prospectively frozen full-resolution resource/readiness gate is still required before Exp073DV activation.

Exp073DV full-resolution `WW_S0_S1` remains `PREPARED_NOT_ACTIVATED`, additionally blocked on valid `WW_S0_S0` authority/provenance closure.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
