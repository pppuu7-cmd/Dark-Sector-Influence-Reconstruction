# DSIR recovery V81 — Article III Exp073JO preflight running

Date: 2026-09-10. Scope: DSIR only.

## Preserved scientific authority
- Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`, native-grid maximum `0.9998247463807295 > REL_TOL=1e-3`.
- Exp073JI preserves complete shared-grid support on all 107 retained rows with invalid fraction 0 and zero unsupported evaluations.
- Exp073JJ remains support-only NOT_CONVERGED at `0.037280144773915974`.
- Exp073JK remains support-only NOT_CONVERGED at `0.016330535730270664`, authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`.
- Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Exp073JL process history
Frozen Exp073JL science remains exactly: guarded base N=2048 (2049 requested) versus N=4096 (4097 requested), native kpd=20 for both suites, centered-cubic interpolation in ln(k), finite-difference h=1e-4, REL_TOL=1e-3, exact Exp073IR traversal/support and frozen domain.

Original JL workflow run `34497160814` produced no valid numerical result in either attempt:
- attempt 1 job `102938434376`: external GitHub-hosted runner shutdown during numerical step 10; no result artifact;
- attempt 2 job `102944693569`: external GitHub-hosted runner shutdown at 2026-09-10T16:10:29Z during numerical step 10; no result artifact.

Both are infrastructure/process `+0/+0`, neither CONVERGED nor NOT_CONVERGED. A third blind monolithic rerun is not authorized while process recovery is available.

## Exp073JO process-only recovery
Prospective preregistration: `docs/dsir4/prereg/EXP073JO_ARTICLE3_JL_DURABLE_RESPONSE_CHECKPOINT_RECOVERY_V0_1.md`, commit `af034787b0493e80e12a0faa4127a08a451ab5df`.

Frozen JO rules:
- scientific JL implementation/result logic unchanged;
- intercept only complete original `ResolutionSuite.response(z, targets)` calls;
- durable unit = one fully completed response call;
- key binds slot/global call index, z.hex(), exact target-stream SHA256/count, guarded-node SHA256/count, response shape/dtype/nbytes/SHA256, exact audit before/after and k-key state;
- exact sequential-prefix replay only; corrupt/mismatched/non-prefix cache fails closed;
- flush cadence at most 16 newly computed response calls, plus suite-close and successful completion;
- dedicated branch/namespace `checkpoints/exp073jo-jl-response-v0-1`;
- mandatory exact history-independence control on pinned CLASS-IV and frozen JL grids;
- mandatory exact cache byte/audit round-trip regression;
- JO itself is process-only +0/+0 and cannot authorize covariance or Wm_S3.

Implementation: `ci/exp073jo_article3_jl_durable_response_checkpoint_recovery_v0_1.py`, commit `fb4cae4d4a407fe30faf1a9875d290887bcb822d`.

## Current active process
Exp073JO exact-build preflight workflow head/commit `374184d1b2e9f31628ab930bc271951569ce2bf9`.
Run/job: `34504474368 / 102963111387`.
Latest verified state: prereg/static guard PASS; frozen numerical/build stack PASS; exact pinned CLASS-IV capacity/parser patch and build PASS; exact history-independence + cache round-trip step IN_PROGRESS; artifact pending.

No Article-III numerical response result is read by this preflight.

## Prepared but inactive successor
Recovery workflow file `.github/workflows/exp073jo-article3-jl-durable-response-checkpoint-recovery-v0-1.yml` prepared at commit `a2ea07ff5a5bd4060cb3c7b7230b398dde202f08` with `workflow_dispatch` only. It is intentionally not auto-triggerable before a durable independently verified JO preflight PASS authority exists.

If preflight is valid PASS: independently verify artifact ZIP/result/capacity hashes, commit durable JO preflight authority, then prospectively enable one push trigger for the prepared recovery workflow. If preflight is infrastructure FAIL: diagnose first causal defect and repair only process code; do not run recovered JL.

## Post-JL branches remain frozen
- Valid recovered JL CONVERGED -> only already-frozen Exp073JN fresh science-authorizing Layer-B rerun.
- Valid recovered JL NOT_CONVERGED -> only already-frozen Exp073JM next refinement 4097->8193.
- Any infrastructure/process failure -> neither branch.

The JM implementation currently contains one known pre-result alignment issue: activation code additionally requires JL retained=107/unsupported=0 although the JM prereg activation condition requires only a valid independently verified JL NOT_CONVERGED. This is an implementation-only overconstraint and must be corrected before any JM science activation; it does not affect current JO/JL mathematics.

## Independent interpretation result
Existing JF/JG local diagnostics show the historical Exp073IR worst probes are already below 1e-3 on the adopted centered-cubic shared-grid architecture (`alpha ~1.21e-7`, `beta ~1.61e-4` at JG), while full-support JJ/JK remain much larger. Therefore the global full-support convergence maximum has migrated away from the original worst pair or is dominated by another response-scale regime. No threshold or denominator rule is changed by this observation.

## Frozen global boundaries
`0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/clipping/effective-coordinate/fiducial-P rescue.
