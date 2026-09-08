# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

All scientific authority preserved by V35 remains unchanged, including scientifically admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HO_RUNTIME_FAIL_HP_DIAGNOSTIC_FRONT_V36.md`, creation commit `f6c8979f6792d95a1cbab1bad7a1413e8a00c5f9`.

## Newly closed support/readiness

Exp073HM `34227557134 / 102065303554 SUCCESS` is terminal-consumed `SUPPORT_PLUS_0_PLUS_0`. Exp073HN `34228937213 / 102069878872 SUCCESS` is terminal-consumed `SUPPORT_PLUS_0_PLUS_0` with exact token `PASS_EXP073HN_C2_REFERENCE_RUNTIME_DRIVER_SERIALIZER_STATIC_AUDIT_V0_1`, exact 28-request z-major/k-minor plan and synthetic 64-byte serializer ABI; no cosmological run or payload occurred.

## Terminal Exp073HO result

Exp073HO run `34229170304`, job `102070681656`, terminal `FAILURE`. Binding verification and exact post-HM solver build passed. First failure was inside the first frozen solver invocation in `Execute frozen 28-request raw producer`; exit code 1 occurred before endpoint extraction/serialization/receipt/artifact. The original workflow redirected stdout/stderr to ephemeral files, so the causal solver diagnostic was not present in the terminal Actions log. No raw candidate artifact exists; raw admission remains false.

Classification: **infrastructure/runtime implementation FAIL `+0/+0`**, not scientific FAIL.

## Current process — Exp073HP first-request failure diagnostic

- prereg `docs/dsir4/prereg/EXP073HP_C2_HO_FIRST_REQUEST_FAILURE_DIAGNOSTIC_V0_1.md`;
- prereg blob `5b924127b67870a23f0e5aa055d26c12115a6d63`;
- prereg commit `4a528649f9cd6256239239b1d57315825900b662`;
- workflow blob `498d647e0aa783c410c2bd08652a95d7b5b36536`;
- binding/head commit `9b89d7b50fcac3f6f65aa1bd3ba1ecb560a081d8`;
- run `34229746056`;
- job `102072618086`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at ledger update: **IN_PROGRESS**;
- exact request unchanged from HO first node: model `(0,0)`, `z=0.295`, physical `k=0.00067 Mpc^-1`, same parent/post-HM source/baseline/p8;
- endpoint lines are filtered from diagnostic output;
- serialization, raw artifact, decoding, mapping and scientific authority are forbidden;
- expected classification `INFRASTRUCTURE_DIAGNOSTIC_PLUS_0_PLUS_0`.

### Exact next action

On HP terminal result consume the raw log immediately. If a deterministic parser/runtime/configuration defect is exposed, repair only that smallest causal defect prospectively and rebind/relaunch HO unchanged scientifically. If the exact first request unexpectedly succeeds, diagnose environment/execution differences before any HO rerun. Never change frozen model, z/k coordinates, baseline physics, p8 precision, ABI or admission criteria.

## Frozen boundaries

`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
