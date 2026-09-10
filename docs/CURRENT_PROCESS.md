# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JO_PREFLIGHT_RUNNING_V81.md`, creation commit `7d72c0cd7dba95161d87ec6a18e867d2fe195e07`.

## Preserved scientific authority
- Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; exact native production-vs-dense convergence maximum `0.9998247463807295 > 1e-3`; retained 107; covariance unauthorized.
- Exp073JI remains validated support-only full-support feasibility with 107 retained, invalid fraction 0 and zero unsupported target evaluations.
- Exp073JJ remains validated support-only NOT_CONVERGED, maximum `0.037280144773915974`.
- Exp073JK remains validated support-only NOT_CONVERGED, maximum `0.016330535730270664`, authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`.
- Wm_S3 remains unopened.

## Closed process history — Exp073JL
Frozen Exp073JL science remains guarded N=2048->4096 (2049->4097 requested), native kpd=20 for both suites, centered-cubic ln(k), `h=1e-4`, `REL_TOL=1e-3`, exact Exp073IR support/traversal and frozen domain.

Run `34497160814` produced no valid scientific result in either attempt:
- attempt 1 / job `102938434376`: external GitHub-hosted runner shutdown during numerical step 10;
- attempt 2 / job `102944693569`: external GitHub-hosted runner shutdown during numerical step 10.
No JL result artifact exists from either attempt. Both are infrastructure/process `+0/+0`, neither CONVERGED nor NOT_CONVERGED. Blind monolithic rerun is forbidden.

## Current authoritative process — Exp073JO exact-build preflight
- workflow: `exp073jo-article3-jl-durable-response-checkpoint-preflight-v0-1`;
- run ID: `34504474368`;
- job ID: `102963111387`;
- branch/head: `main / 374184d1b2e9f31628ab930bc271951569ce2bf9`;
- preregistration commit: `af034787b0493e80e12a0faa4127a08a451ab5df`;
- implementation commit: `fb4cae4d4a407fe30faf1a9875d290887bcb822d`;
- checkpoint namespace reserved for successor: `checkpoints/exp073jo-jl-response-v0-1`;
- started: `2026-09-10T16:49:43Z`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- expected token: `PASS_EXP073JO_DURABLE_RESPONSE_CHECKPOINT_PREFLIGHT_V0_1`;
- latest live state: IN_PROGRESS;
- completed: prereg/static guard SUCCESS; frozen numerical/build stack SUCCESS; exact pinned CLASS-IV capacity/parser patch + build SUCCESS;
- current step: exact history-independence and cache round-trip controls;
- artifact: pending;
- scientific effect: process-only `+0/+0`; no Article-III numerical result is read.

## Independent non-biasing process audit while JO runs
The JO wrapper correctly uses inherited slot labels 10/20 only to distinguish coarse/fine shared grids; the underlying `class_params` keeps native CLASS `k_per_decade_for_pk=20` for both suites. No frozen arithmetic change was found.

One fail-closed provenance gap was identified in the prepared recovery path before activation: recovery validates the JJ source SHA from preflight authority, but the prepared recovered-JL workflow does not yet bind the complete scientific source/traversal bundle to an immutable reference commit. A future resume after unrelated main changes could therefore lack an explicit source-head/bundle identity guard even though request/node/response hashes remain checked. This is a process-only implementation alignment issue, not a scientific result.

Before the first checkpointed JL recovery launch, strengthen the prepared workflow with a prospective immutable scientific-bundle guard (at minimum exact JL/JJ/IR and frozen traversal/config/support-source identity against the preflight reference commit), without changing any science or checkpoint arithmetic. This strengthening does not inspect or tune JL numerical output.

## Exact next actions
1. Terminal-consume JO preflight `34504474368 / 102963111387`.
2. If valid PASS: independently verify raw log plus artifact ZIP/result/capacity hashes and commit preflight authority.
3. Before recovered JL activation, close the source-bundle provenance gap prospectively with a fail-closed static guard; do not change frozen scientific files.
4. Launch exactly one checkpointed recovered JL only after both preflight authority and bundle guard are valid.
5. Recovered JL CONVERGED -> only pre-frozen Exp073JN. Recovered JL NOT_CONVERGED -> only pre-frozen Exp073JM. Infrastructure/process invalid -> neither branch.

Known inactive JM implementation overconstraint remains: current code additionally checks JL retained=107/unsupported=0 although frozen JM prereg activation requires only a valid independently verified JL NOT_CONVERGED. Correct that implementation-only overconstraint before any JM science activation; do not amend JM prereg.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/clipping/effective-coordinate/fiducial-P rescue.
