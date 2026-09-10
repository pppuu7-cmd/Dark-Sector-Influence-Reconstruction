# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JO_SOURCE_BUNDLE_GUARD_V82.md`, creation commit `8f9c2dabb7c6c6ce8f1e135b93c4ebe2cd614231`. Earlier notes remain immutable history.

## Preserved authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR` with original native-grid maximum `0.9998247463807295 > REL_TOL=1e-3`. Exp073JI preserves all 107 retained rows with invalid fraction 0 and zero unsupported target evaluations. Exp073JJ remains valid support-only NOT_CONVERGED at `0.037280144773915974`. Exp073JK remains valid support-only NOT_CONVERGED at `0.016330535730270664`, authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Exp073JL process status
Frozen Exp073JL science remains guarded N=2048->4096 (2049->4097 requested), native kpd=20 for both suites, centered-cubic ln(k), `h=1e-4`, `REL_TOL=1e-3`, exact Exp073IR support/traversal and frozen domain.

Original run `34497160814` produced no scientific result in either attempt. Attempt 1/job `102938434376` and attempt 2/job `102944693569` both received external GitHub-hosted runner shutdown during numerical step 10 and produced no result artifact. Both are infrastructure/process `+0/+0`, neither CONVERGED nor NOT_CONVERGED. Do not perform another blind monolithic JL rerun.

## Current process — Exp073JO preflight
Exp073JO is a prospectively frozen process-only durable response-call checkpoint recovery for the exact JL calculation. Preregistration commit `af034787b0493e80e12a0faa4127a08a451ab5df`; implementation commit `fb4cae4d4a407fe30faf1a9875d290887bcb822d`.

Recovery semantics remain: only complete original `ResolutionSuite.response(z,targets)` calls may be persisted/replayed; global sequential call index per slot across suite-instance boundaries; exact binary64 z/target/node/response hashes; exact audit transition restoration; fail-closed prefix/provenance checks; at most 16 newly computed calls between durable pushes; dedicated branch/namespace `checkpoints/exp073jo-jl-response-v0-1`. Scientific JL arithmetic/result logic is unchanged.

Mandatory exact-build preflight run/job `34504474368 / 102963111387`, head `374184d1b2e9f31628ab930bc271951569ce2bf9`. Latest verified state: static prereg guard PASS; numerical/build stack PASS; exact pinned CLASS-IV capacity/parser patch + build PASS; exact history-independence/cache-roundtrip controls IN_PROGRESS; artifact pending. This preflight reads no JL Article-III numerical result.

## Newly hardened prepared recovery path
Independent audit found that the prepared recovery workflow bound the JJ response-engine source through preflight authority but did not explicitly bind the whole scientific/traversal/config source bundle to one immutable head for future resume.

Process-only repair commit `be1687db88b35951cf3e813c64dbdd017af2802e` adds `SCIENCE_REFERENCE_COMMIT=374184d1b2e9f31628ab930bc271951569ce2bf9` and an exact Git-blob identity guard over the 16 frozen scientific/traversal/config/authority/prereg files used by recovered JL. Any mismatch fails closed before checkpoint replay. Recovery-only code remains prospectively repairable. No numerical arithmetic, estimator, threshold, data domain or frozen science was changed.

Current-process ledger was reconciled to JO at commit `5c4bbe21868ba24634fadfcd53e45af6275595c8`.

## Frozen post-JL branches
Two mutually exclusive branches remain frozen before any valid JL numerical result:
- valid independently verified JL NOT_CONVERGED -> Exp073JM 4097->8193 support-only refinement;
- valid independently verified JL CONVERGED -> Exp073JN fresh science-authorizing repeat of admitted 2049->4097 architecture.
Any infrastructure/process failure activates neither branch.

Known inactive JM implementation overconstraint: current code additionally checks JL retained=107/unsupported=0 as activation, although frozen JM prereg activation requires only a valid independently verified JL NOT_CONVERGED. Correct this implementation-only overconstraint before any JM science run; do not amend JM prereg.

## Exact next action
Terminal-consume JO preflight `34504474368 / 102963111387`. Valid PASS -> independently verify artifact ZIP/result/capacity hashes, commit durable JO preflight authority, then validate the strengthened frozen-source-bundle guard and only after that activate exactly one prepared checkpointed JL recovery. Infrastructure FAIL -> diagnose first causal process defect; recovered JL remains forbidden. No tolerance rescue.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/clipping/effective-coordinate/fiducial-P rescue.
