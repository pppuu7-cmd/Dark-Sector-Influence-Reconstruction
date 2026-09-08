# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HO_EXACT_ENDPOINT_IDENTITY_BLOCK_V36.md` (creation commit `e8125e822069651f9001ed31930df705f5f8183c`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

All prior scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**. `WW_S3_S3` remains scientifically admitted by recovery-admission run `34218457380 / 102035691774`, consuming GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

C2 remains `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Preserved C2 support results

Exp073HM `34227557134 / 102065303554 SUCCESS` and Exp073HN `34228937213 / 102069878872 SUCCESS` remain raw-log validated support-only PASS results (`SUPPORT_PLUS_0_PLUS_0`). They create no scientific/model authority.

## Current C2 frontier — Exp073HO v0.1 blocked at exact endpoint identity

Frozen Exp073HO head `841e431d55aadbdc0ea972902be6da5ffa0125bf`, run `34229170304`, actual job `102070681656`, is terminal `FAILURE`. Frozen binding and exact post-HM solver/serializer build passed; the first frozen runtime request failed before aggregate, provenance receipt, artifact upload or raw-candidate boundary. No raw record set was created or admitted.

Hosted-only exact first-request diagnostic run `34229365325`, job `102071344339`, workflow creation commit `0d68fc61f58e5b7b9f46ca43f4ed32d7b4a34d92`, reproduced the failure without changing model/config/coordinates. Exact causal error is:

`dsir_c2_diag_arm_terminal: condition (tau != dsir_c2_diag_tau_target) is true; DSIR C2 terminal tau is not the exact background_tau_of_z endpoint`.

Classification is `BLOCKED_BY_FROZEN_IMPLEMENTATION_EXACT_ENDPOINT_IDENTITY +0/+0`; scientific FAIL contribution is `0`. This is an implementation/runtime failure before an admitted observation, not a physical/model rejection.

No tolerance, rounding, nearest-time, interpolation, altered z/k, modified baseline/p8, or weakened provenance rescue is permitted. Exp073HO v0.1 must not be rerun unchanged because the exact first request deterministically reproduces the same failure.

## Exact next transition

A further runtime attempt requires a **new prospectively versioned implementation contract/preregistration frozen before execution** that defines bit-exact terminal-time canonicalization while preserving the same physical endpoint, equations, solver tolerances, model point, z/k grid, baseline, p8 settings, 64-byte packet ABI, field order and provenance requirements.

The present guard explicitly forbids changing frozen contracts, so that prospective version transition is not performed here. Until it is independently authorized/frozen: `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Frozen boundaries

Global DSIR science boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
