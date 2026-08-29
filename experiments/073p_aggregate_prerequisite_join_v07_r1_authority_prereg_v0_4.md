# Exp073P aggregate prerequisite join — Exp073R1 v0.7 authority preregistration v0.4

**Frozen:** 2026-08-29, while Exp073R1 v0.7 run `33240490287`, attempt `3`, job `99142692261`, was `queued`, before any attempt-3 execution result or terminal artifact existed.

## Purpose and non-retroactivity

This preregistration creates a new prospective authority route for a possible genuine Exp073R1 v0.7 reproduction PASS from attempt 3. It does **not** modify, reinterpret, or repoint Exp073P aggregate join v0.1, v0.2, or v0.3.

The v0.3 authority remains permanently bound to Exp073R1 v0.7 run `33240490287`, attempt `2`, job `99080934021`. Attempt 2 terminated because the self-hosted runner received a shutdown signal during authoritative-object acquisition, producing `KeyboardInterrupt` / exit code `130` before exact-object identity, loopback replay, frozen mapper execution, genuine R1 assertion, or artifact publication. That event is classified as execution/infrastructure interruption, not a scientific FAIL. v0.3 therefore remains an immutable historical fail-closed route and must never accept attempt-3 evidence.

No scientific support coordinate, threshold, parent dataset, physical-validity definition, acceptance criterion, or downstream gate ordering is changed here.

## Sole admitted v0.7 R1 authority for v0.4

A future Exp073P aggregate prerequisite join v0.4 may admit R1 evidence only from all of the following exact authority coordinates:

- repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`;
- run ID: `33240490287`;
- run attempt: `3`;
- job ID: `99142692261`;
- job name: `transport-stabilized-replay`;
- head branch: `main`;
- head SHA: `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- event: `push`;
- workflow path: `.github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml`;
- workflow name: `Exp073R1 DESY1 transport-stabilized exact-byte replay v0.7`;
- workflow ID: `345172058`;
- unchanged frozen evaluator path: `ci/exp073r1_sequential_wholestream_v0_5.py`;
- unchanged frozen evaluator Git blob SHA1: `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- expected artifact name: `exp073r1-v07-transport-stabilized-9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- required terminal summary member: `exp073r1_desy1_transport_stabilized_replay_v0_7_summary.json`;
- required acquisition provenance member: `exp073r1_v0_7_remote_acquisition_provenance.json`;
- required runtime provenance member: `exp073r1_v0_7_runtime_provenance.txt`.

At freeze time live Actions metadata reported `run_attempt=3`, `status=queued`, `conclusion=null`; job `99142692261` was queued. No attempt-3 terminal result, R1 artifact, support quantity, retained dimension, covariance quantity, nuisance rank, relation/null quantity, or held-out information was observed or used to define this contract.

## Fail-closed live Actions metadata requirements

Actions `success` alone is insufficient. The v0.4 route must independently verify live GitHub Actions metadata with complete pagination and require at minimum:

1. exact repository, run ID, workflow ID/path/name, head SHA, head branch and event above;
2. `run_attempt == 3` exactly; attempts 1 and 2 are inadmissible;
3. run terminal `status == completed` and `conclusion == success`;
4. exactly job `99142692261` is terminal `completed/success` and has `run_attempt == 3`;
5. no ambiguity between latest-run job enumeration and the attempt-specific `/attempts/3/jobs` registry;
6. exactly one non-expired artifact with the frozen artifact name is admitted;
7. artifact ID and GitHub-reported digest are supplied explicitly and independently match the live artifact record;
8. missing, duplicate, expired, cancelled, skipped, neutral, stale-attempt, wrong-head, wrong-workflow, wrong-job, wrong-name, wrong-ID or wrong-digest evidence fails closed.

## Required internal v0.7 reproduction evidence

The admitted artifact is authoritative only if its internal evidence independently proves every frozen Exp073R1 condition already required by v0.3, including:

- summary status exactly `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`;
- exact metacal object size `84075649920` and SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- acquisition provenance has `authorized_for_replay=true`, `http_range_requests=0`, `whole_object_attempts_from_zero=true`, every internal acquisition attempt starts at byte zero and sends no Range header;
- exact source whole SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5` and source-index SHA256 `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`;
- source/metacal row counts both `136930995`;
- exact selection `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- mapper exactly `nside=4096`, RING, celestial `C`, `lonlat=True`;
- zero out-of-range pixels, four non-empty selected bins, repeatability controls true, and every frozen Exp073R0 parent check true;
- `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false` and `gate_state={G7: OPEN, G8: OPEN, G9: OPEN}`.

The frozen Exp073R1 v0.7 transport contract remains independently binding. No incomplete acquisition record, partial mask/pixel record, runner-shutdown record, or infrastructure-failure artifact is admissible.

## Remaining nine parent authorities

All non-R1 prerequisite parents and their frozen semantic/byte checks remain exactly those preregistered for Exp073P v0.1/v0.2/v0.3. v0.4 may supersede **only** the R1 authority coordinate. It must not weaken, replace, or recompute any other prerequisite parent.

## Implementation policy

Historical v0.1/v0.2/v0.3 preregistration, evaluator, metadata collector and workflow files remain byte-immutable.

The v0.4 implementation may reuse the byte-frozen v0.3 semantic validators and payload normalizer, but must add a new attempt-3 authority overlay and a new production workflow that:

- binds exactly run `33240490287`, attempt `3`, job `99142692261`;
- verifies both latest-attempt and explicit `/attempts/3/jobs` metadata agree exactly;
- rejects attempt 1, attempt 2 and any other job identity;
- preserves exact artifact ZIP digest verification and complete payload cross-binding;
- has a byte/hash firewall for the v0.4 preregistration and overlay;
- includes synthetic fail-closed tests for wrong attempt, wrong job, wrong head/workflow, wrong artifact identity, missing/non-authorized acquisition provenance, nonzero Range use, wrong final byte count/SHA256 and non-PASS R1 status;
- never authorizes the support executor from synthetic evidence.

## Receipt taxonomy and authorization boundary

The only real v0.4 aggregate receipt states may be:

- `PASS_EXP073P_PREREQUISITE_BINDING_V0_4`;
- `REJECTED_EXP073P_PREREQUISITE_BINDING_V0_4`;
- `INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_4`.

Only a genuine real v0.4 PASS may set `support_executor_authorized=true`. Such PASS authorizes only the already-preregistered Exp073P physical support-validity mask executor. It does not authorize covariance, whitening, nuisance SVD/rank, quotient/relation/null work, or G8.

An attempt-3 infrastructure failure, reproduction identity failure, or reproduction failure is **not** a G7 scientific FAIL and remains separately classified.

## Frozen scientific firewall and order

The existing scientific contract remains unchanged:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- positive absolute final-response support envelope while production `Wm` remains signed;
- invalid radial tails outside the rectangle;
- no crop-before-normalization, effective-ell, fiducial-P/model weighting or post-hoc cuts.

Required sequence remains exactly:

`validated physical forward/power-input bridges -> prerequisite authority join -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> only then fresh G8 withheld family`

At this freeze, `support_executor_authorized=false`; G7, G8 and G9 remain OPEN.