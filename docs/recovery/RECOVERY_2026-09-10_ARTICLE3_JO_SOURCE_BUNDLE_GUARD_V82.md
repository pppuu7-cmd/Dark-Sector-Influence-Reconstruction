# DSIR recovery V82 — Article III Exp073JO source-bundle guard added

Date: 2026-09-10. Scope: DSIR only.

## Preserved scientific authority
- Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`, native-grid maximum `0.9998247463807295 > REL_TOL=1e-3`.
- Exp073JI remains validated support-only full-support feasible with all 107 retained rows, invalid fraction 0 and zero unsupported target evaluations.
- Exp073JJ remains support-only NOT_CONVERGED at `0.037280144773915974`.
- Exp073JK remains support-only NOT_CONVERGED at `0.016330535730270664`, authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`.
- Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Exp073JL process history
Frozen JL science is unchanged: guarded base N=2048 versus 4096 (2049 versus 4097 requested), native CLASS kpd=20 for both suites, centered-cubic ln(k), `h=1e-4`, `REL_TOL=1e-3`, exact Exp073IR support/traversal and frozen physical domain.

Run `34497160814` attempts 1/job `102938434376` and 2/job `102944693569` both suffered external GitHub-hosted runner shutdown during the numerical step and produced no JL result artifact. Both remain infrastructure/process `+0/+0`; neither JM nor JN is activated.

## Current active process — Exp073JO exact-build preflight
Prospective JO preregistration commit `af034787b0493e80e12a0faa4127a08a451ab5df`; implementation commit `fb4cae4d4a407fe30faf1a9875d290887bcb822d`.

Run/job `34504474368 / 102963111387`, preflight head `374184d1b2e9f31628ab930bc271951569ce2bf9` remains IN_PROGRESS at the exact history-independence and cache round-trip controls. Earlier prereg/static, numerical/build stack and exact pinned CLASS-IV capacity/parser build steps are SUCCESS. No Article-III numerical result is read by this preflight.

## Independent non-biasing audit and process repair
While preflight remained active, the durable checkpoint wrapper and prepared recovery workflow were audited without inspecting any partial JL numerical output.

The slot mapping is correct: inherited slot labels 10/20 select coarse/fine guarded shared lattices, while the actual CLASS calls keep `NATIVE_KPD=20` for both suites. No frozen arithmetic or scientific acceptance rule is changed.

A process provenance gap was found before the first recovered-JL activation: preflight authority explicitly binds the JJ response-engine source hash, but the prepared recovery workflow did not yet bind the complete scientific/traversal/config source bundle to an immutable reference commit. That could leave a future resume without an explicit fail-closed source-head/bundle drift check even though checkpoint request/node/response hashes themselves are exact.

The smallest prospective process-only repair was applied to `.github/workflows/exp073jo-article3-jl-durable-response-checkpoint-recovery-v0-1.yml`, commit `be1687db88b35951cf3e813c64dbdd017af2802e`.

The recovery workflow now sets `SCIENCE_REFERENCE_COMMIT=374184d1b2e9f31628ab930bc271951569ce2bf9`, fetches that exact preflight head, and requires exact Git blob identity for 16 scientific/traversal/config/authority/prereg files before any recovery computation or checkpoint replay. Mismatch emits `FROZEN_SOURCE_BUNDLE_MISMATCH` and fails closed. Recovery-only code remains prospectively repairable; scientific source identity is frozen. This change does not inspect JL output, alter checkpoint payload arithmetic, or change any threshold/domain/estimator.

Current-process ledger was reconciled to JO at commit `5c4bbe21868ba24634fadfcd53e45af6275595c8`.

## Exact next action
Terminal-consume JO preflight `34504474368 / 102963111387`.

Valid PASS -> independently verify raw log and artifact ZIP/result/capacity hashes; commit durable JO preflight authority; then run a hosted/static validation of the new frozen-source-bundle guard and only after it passes activate exactly one checkpointed JL recovery.

Infrastructure FAIL -> diagnose first causal process defect and repair only process code; recovered JL remains forbidden.

Recovered valid JL CONVERGED -> only pre-frozen Exp073JN. Recovered valid JL NOT_CONVERGED -> only pre-frozen Exp073JM. Infrastructure/process failure -> neither branch.

Known inactive JM implementation overconstraint remains to be corrected before any JM science activation: current code additionally requires JL retained=107/unsupported=0 although the frozen JM prereg activation condition requires only a valid independently verified JL NOT_CONVERGED.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/clipping/effective-coordinate/fiducial-P rescue.
