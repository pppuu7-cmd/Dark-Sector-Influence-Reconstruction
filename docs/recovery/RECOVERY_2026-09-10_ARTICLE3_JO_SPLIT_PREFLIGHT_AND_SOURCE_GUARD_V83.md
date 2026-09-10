# DSIR recovery V83 — Article III Exp073JO split preflight + source-bundle guard

Date: 2026-09-10. Scope: DSIR only. This note reconciles concurrent main-chat and DSIR Continuous Research process hardening; repository authority wins over stale chat state.

## Preserved scientific authority
- Exp073IR: `NUMERICALLY_UNRESOLVED_EXP073IR`, native-grid max `0.9998247463807295`.
- Exp073JI: full 107-row shared-grid support, invalid fraction 0, zero unsupported targets.
- Exp073JJ: support-only NOT_CONVERGED, max `0.037280144773915974`.
- Exp073JK: support-only NOT_CONVERGED, max `0.016330535730270664`, authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`.
- Covariance restriction unauthorized; Wm_S3 unopened.
- Frozen `REL_TOL=1e-3`, `h=1e-4`, masks, physical support, 107-row parent, and all anti-rescue rules unchanged.

## JL/JO infrastructure history
Original frozen JL run `34497160814` produced no result artifact in either hosted attempt: jobs `102938434376` and `102944693569` each received an external runner shutdown during numerical step 10. Both are infrastructure/process +0/+0.

JO prereg `af034787b0493e80e12a0faa4127a08a451ab5df` freezes response-call checkpoint/replay without changing JL science. Recovery wrapper implementation commit `fb4cae4d4a407fe30faf1a9875d290887bcb822d`, Git blob SHA `aa4c544c1e3e81137010fcdbd34f20567e1eb894`.

The first combined JO preflight run/job `34504474368 / 102963111387`, head `374184d1b2e9f31628ab930bc271951569ce2bf9`, passed static/environment/exact CLASS-IV build stages but received another external hosted-runner shutdown at `2026-09-10T17:03:11Z` during the combined live controls. No assertion failure/result JSON/artifact existed. Classification: `INVALID_INFRA_PLUS_0_PLUS_0`, not a negative cache/history result.

## Current active process: split JO preflight v0.2
Prospective process-only split amendment commit `9f8bb9df1215fe114ffaaa6403d47c0c913564c2`; helper implementation commit `9630487813533294dd7ec090916b289b78231b89`; workflow/head `f13c827bf265e1329e7d0502f1da12e2fa723d07`.

Run `34506027292` is the sole current JO preflight process. It contains three independent fail-fast-disabled exact-build jobs:
- `cache_roundtrip_slot10` job `102968324698`;
- `history_slot20` job `102968325017`;
- `history_slot10` job `102968325131`.

The exact already-frozen v0.1 controls are unchanged; only their hosted process is split. Aggregation may pass only if all three exact part artifacts pass. Heavy JL recovery remains forbidden until aggregate artifact verification and durable authority.

## Reconciled process hardening from DSIR Continuous Research
Autonomous commit `be1687db88b35951cf3e813c64dbdd017af2802e` strengthened the prepared JO heavy recovery with `SCIENCE_REFERENCE_COMMIT=374184d1b2e9f31628ab930bc271951569ce2bf9` and exact Git-blob equality across 16 scientific/traversal/config/authority/prereg files. This source-bundle guard is retained. It changes no science.

Current-process ledger reconciliation commit from the autonomous loop: `5c4bbe21868ba24634fadfcd53e45af6275595c8`. Earlier autonomous immutable source-bundle note `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JO_SOURCE_BUNDLE_GUARD_V82.md` remains valid historical process provenance.

Main-chat wrapper identity amendment commit `41b5026f90ff0f4ac9252abc81255fe60a0e6d89` additionally requires the recovery wrapper itself to remain blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894` or undergo a new exact-build preflight.

## Full traversal topology authority
Independent redownload/reverification of Exp073JK artifact `10160083225` reproduced ZIP SHA256 `a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99`. Its raw response-engine audit establishes invariant Exp073IR call topology:
- slot 10: exactly 441 complete calls and 83666 target evaluations;
- slot 20: exactly 569 complete calls and 121682 target evaluations;
- zero unsupported target evaluations.
Prospective topology amendment commit `4fcb6035c880418a74bec8537bc11b2795f20607` requires recovered JL to terminate at exactly 441/569 calls and the same target-evaluation totals; mismatch is `INVALID_INFRA_PLUS_0_PLUS_0`.

## Heavy recovery status
Prepared workflow `.github/workflows/exp073jo-article3-jl-durable-response-checkpoint-recovery-v0-1.yml` remains non-auto-triggered (`workflow_dispatch` only). Its autonomous source-bundle guard from `be1687db...` must be preserved. Before activation after a valid split-v0.2 preflight PASS, additionally bind the durable v0.2 preflight authority, wrapper blob SHA, and 441/569 topology guard. Exactly one heavy recovery may then run.

## Frozen post-JL branching
- valid independently verified recovered JL CONVERGED -> only Exp073JN fresh science-authorizing Layer-B rerun;
- valid independently verified recovered JL NOT_CONVERGED -> only Exp073JM 4097->8193 support-only refinement;
- infrastructure/process failure -> neither.
Known inactive JM implementation activation overconstraint must be corrected before any JM science run without changing its preregistration.

## Exact next action
Consume run `34506027292`: inspect each terminal part artifact and aggregate. If all exact controls pass, independently verify artifact ZIP/JSON hashes, part identities, frozen constants, wrapper identity and source lineage; commit durable JO v0.2 preflight authority; then harden+activate exactly one checkpointed JL recovery. If a part suffers external shutdown, preserve completed part artifacts and rerun/recover only the missing unchanged control rather than repeating successful parts where practical.
