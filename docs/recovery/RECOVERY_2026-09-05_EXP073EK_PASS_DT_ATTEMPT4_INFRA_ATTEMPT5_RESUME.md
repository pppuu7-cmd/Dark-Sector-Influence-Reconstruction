# DSIR immutable recovery note — Exp073EK PASS; Exp073DT attempt 4 infrastructure shutdown; attempt 5 resume

Date: 2026-09-05
Scope: DSIR only. RTK/RQIR excluded.

## Exp073EK terminal consumption

Exp073EK run/job `33988956806 / 101367596573` completed SUCCESS at head `51f8a7d7dd481e79b734ba174bffa29236f2fc0b`.

Frozen prereg blob: `8ace7b91e0607552cab2e2a9e6cf20c2c5e24621`.
Frozen implementation blob: `b3fcdf5acfe0d5818657bd1f2885c91c2903a877`.
Artifact `9976033816`; GitHub artifact ZIP digest `sha256:f39351cddec695559686126fc15e212556eea370fe3eeab73d5f20f80c288c06`.

Raw frozen token: `PASS_EXP073EK_DIRECT_PUBLIC_BPW_ADAPTER_EXACT_V0_1`.
Classification: `DIRECT_PUBLIC_BPW_ADAPTER_EXACT +0/+0`.
Science gate scored: false. WW authority created: false.

Exact checks all passed: distinct masks, finite payloads, full shape, selected shape, full SHA equality, full `numpy.array_equal`, selected SHA equality, selected `numpy.array_equal`, and explicit no-tolerance-rescue.

Full A/B SHA256: `aa883a13c305641e6e1aab5feca4692a8da1cdbcca16e8c124f12e601608d628`.
Selected `EE<-EE` A/B SHA256: `9e7a0e169d752e56d4a1f14244c58ac9a14a5c1a3782c27b3a6562a69cb0cf5e`.
PyMaster version: 2.7.

Interpretation is strictly support/readiness: direct serialized-workspace reload followed by public `NmtWorkspace.get_bandpower_windows()` is exact under the frozen hosted qualifier. This does not create `WW_S0_S1` authority and does not authorize Exp073DV until a separate prospectively frozen full-resolution resource/readiness gate and the prior `WW_S0_S0` authority/provenance closure pass.

## Exp073DT attempt 4 terminal classification

Authoritative science run `33940588308`, attempt 4, head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd` became terminal FAILURE. Hosted preflight `101288015425` was SUCCESS. Self-hosted job `101288014666` failed because the runner received a shutdown signal at `2026-09-05T20:43:43Z`, followed by operation cancellation. Before shutdown, live exclusivity passed, PyMaster 2.7 was verified, and `DSIR_OMP_TEAM=8` passed.

The first causal failure is external runner shutdown / runner loss, not scientific arithmetic. The terminal artifact upload step was skipped, so there is no terminal science artifact for attempt 4 and no scientific PASS/FAIL can be scored from this attempt. Classification: `INFRASTRUCTURE_RUNNER_SHUTDOWN +0/+0`.

No frozen scientific criterion, tolerance, arithmetic, domain, provenance rule, or checkpoint identity was changed.

The driver uses durable local checkpoint root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1/checkpoints` with fail-closed stage manifests. Because the shutdown occurred inside the driver before terminal artifact creation, any complete locally durable stage is to be reused only after normal manifest/SHA validation by the frozen driver; no expensive verified stage is intentionally recomputed.

## Resume action

A specific-job rerun was dispatched only after repository-wide live Actions reconciliation found `0 queued` and `0 in_progress` runs. The same run `33940588308` is now attempt 5, status QUEUED, with self-hosted job `101374976626`; hosted preflight job `101374977192` is already SUCCESS. Frozen head/source/contract remain unchanged.

`DSIR-HOME-PC` is RESERVED BY Exp073DT attempt 5. No competing self-hosted task may launch.

Exp073EB remains mandatory after a successful terminal DT result. Workflow success alone cannot create `WW_S0_S0` authority: raw A/B exact evidence and full six-stage checkpoint provenance must also pass.
