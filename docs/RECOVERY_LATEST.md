# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-05
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Frozen science boundaries remain unchanged.

## Preserved scientific authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0` and original Exp073BU runner-loss infrastructure `+0/+0` remain historical and unchanged.

## Frozen successor frontier
`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

Current scientific target remains exactly `WW_S0_S0`.

## Closed WW support/readiness chain
- Exp073DP exact-equivalence PASS `+0/+0`: run/job `33938446310 / 101230897808`, artifact `9960969007`, ZIP SHA256 `e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8`.
- Exp073DQ durable A/B driver static PASS `+0/+0`: run/job `33938583879 / 101231302981`, artifact `9961000737`, driver SHA256 `0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b`.
- Exp073DR activation/resource PASS `+0/+0`: run/job `33938637212 / 101231459805`, artifact `9961019381`.
- Exp073DS v0.1 remains governance-invalid `+0/+0`.
- Exp073DS v0.2 readiness PASS `+0/+0`: run `33938789513` attempt 2, jobs `101233076119 / 101233097355`, artifact `9961211035`, ZIP SHA256 `d12693ce2b2ec17abfef7008e82eca2bf9f9a29b99f43b00c83e30b2313df53d`, token `PASS_EXP073DS_WW_S0_S0_HOME_READINESS_EXCLUSIVITY_V0_1`.

## Exp073DT attempts 1 and 2 — repeated external runner shutdown, no scientific score
Preregistration commit `946964121f12c67e053514109bf974050eeb0cc9`; frozen workflow/head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`; frozen source authority head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

Attempt 1 of run `33940588308`: hosted preflight job `101237102962` SUCCESS; self-hosted science job `101237118421` FAILURE because the runner received a shutdown signal at `2026-09-05T03:56:42Z`. Frozen science step CANCELLED; terminal evidence upload SKIPPED. Classification `INFRASTRUCTURE_INCOMPLETE +0/+0`.

Attempt 2 of the same frozen run: hosted preflight job `101244675822` SUCCESS; self-hosted science job `101244660215` FAILURE. Decoded raw log first causal failure is another external runner shutdown at `2026-09-05T07:49:54Z`, followed by operation cancellation. Frozen science step CANCELLED; terminal evidence upload SKIPPED. GitHub reports zero artifacts for run `33940588308`. Classification `INFRASTRUCTURE_INCOMPLETE +0/+0`, not scientific FAIL. `WW_S0_S0` authority remains absent.

Before each shutdown the continuous-flock execution passed the relevant runtime preconditions; attempt 2 explicitly passed live exclusivity, PyMaster 2.7 and runtime `DSIR_OMP_TEAM=8`. No numerical/scientific failure appears in the decoded log before the shutdown line.

Durable root remains `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`; frozen DQ namespaces remain `checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `checkpoints/exp073dq-ww-s0-s0-b-v0-1`. Only complete hash/identity-verified stages may be restored. Interrupted/incomplete stages must recompute. Missing, malformed or mismatched checkpoint state fails closed.

Immutable notes:
- `recovery/2026-09-05_exp073dt_runner_shutdown_infrastructure_resume.md`;
- `recovery/2026-09-05_exp073dt_attempt2_runner_shutdown_dispatch_block.md`.

## Current process / runner ownership
Latest live Actions reconciliation: `0 in_progress / 0 queued`. No competing DSIR heavy process owns the runner.

A narrowly scoped attempt to rerun only failed self-hosted job `101244660215` through the connected GitHub action interface was blocked by the connector/runtime before GitHub execution. No alternate workflow, competing control plane, duplicated heavy run, or changed science implementation was created. This dispatch-layer block is external infrastructure `+0/+0`.

The exact next permitted execution is therefore a retry of only the same frozen Exp073DT self-hosted failed job when the GitHub write path permits it, reusing the same durable checkpoint root and unchanged science identity.

Scientific PASS still requires exact SHA equality and `numpy.array_equal=true` in the frozen comparator plus independent terminal reread of both A/B selected `<f8 [39,12288]` `EE<-EE` payloads with valid provenance. Exact A/B inequality is scientific repeatability FAIL. Infrastructure/runtime/checkpoint/provenance/artifact failures are `+0/+0`.

## Independent preparation for the next frontier
Commit `2f9c2950dc118aa281b938d58f444fcfed3b8d18` adds Exp073DU, a small-NSIDE distinct-field `WW_S0_S1` cross-field production-adapter qualifier. It is explicitly support-only (`science_gate_scored=false`, `ww_s0_s1_authority_created=false`) and cannot modify or supersede Exp073DT. It tests ordered cross-field workspace construction against direct PyMaster and exact `EE<-EE` adapter extraction without tolerance rescue. It must not be used to bypass the open `WW_S0_S0` gate.

## Frozen science/execution boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gate
Resume the same frozen Exp073DT self-hosted job when dispatch is available. On terminal completion, consume raw artifact/digest, receipt, A/B payloads, comparator, replica receipts and checkpoint provenance in the same iteration. Only token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1` together with independently verified exact A/B equality may create `WW_S0_S0` authority. If another infrastructure/checkpoint failure occurs, diagnose the first cause and preserve verified stages; do not invent a new science route.
