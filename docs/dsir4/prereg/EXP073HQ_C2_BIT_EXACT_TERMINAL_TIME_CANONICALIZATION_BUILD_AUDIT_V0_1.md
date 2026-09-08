# Exp073HQ — C2 bit-exact terminal-time canonicalization build audit v0.1

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/AUDIT**. Scope: DSIR only; implementation support only.

## Motivation and frozen parent failure

Exp073HO `34229170304 / 102070681656` failed on the first unchanged runtime request. The authoritative hosted diagnostic `34229365325 / 102071344339` established the exact causal condition: accepted NDF15 terminal `tnew` is not bit-identical to the previously computed `background_tau_of_z` target, so the frozen diagnostic hook fails on `tau != dsir_c2_diag_tau_target`. This is implementation/runtime `+0/+0`, not scientific FAIL.

## Allowed canonicalization — and nothing else

Starting from the exact post-HM source chain over `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, HQ may change **only the diagnostic-only accepted-terminal hook arguments** in `tools/evolver_ndf15.c` when both `done==_TRUE_` and `dsir_c2_diag_enabled()!=0`:

- `dsir_c2_diag_arm_terminal(tnew,...)` -> `dsir_c2_diag_arm_terminal(tfinal,...)`;
- `(*derivs)(tnew,ynew+1,...)` -> `(*derivs)(tfinal,ynew+1,...)`;
- `dsir_c2_diag_commit_terminal(tnew,...)` -> `dsir_c2_diag_commit_terminal(tfinal,...)`.

The accepted state vector remains **exactly the already accepted `ynew`**. No integrator state, step size, error estimate, acceptance logic, tolerance, equation, initial condition, solver precision, model parameter, z/k coordinate, baseline, p8 setting, output ABI, field ordering or provenance criterion may change. Ordinary CLASS behavior when `DSIR_C2_EXACT_Z` is absent must remain byte-source-equivalent to the post-HM path except for this opt-in hook text.

The purpose is semantic canonicalization of the already-requested physical terminal coordinate: `tfinal` is the exact `dsir_tau_end` supplied from the literal-z `background_tau_of_z` target to the integrator. The patch must not introduce tolerance/rounding/nearest-time/interpolation. It must not alter `ynew`.

## Static/build PASS

A hosted audit may reconstruct the exact post-HM source, apply the HQ transform, prove exact anchor counts and a minimal diff restricted to the three hook call time arguments, build the full solver, and statically prove that the hook still executes only under `done==_TRUE_ && dsir_c2_diag_enabled()!=0` with `ynew` unchanged.

No cosmological request, endpoint observation, packet serialization or real payload is permitted in HQ.

Exact PASS token: `PASS_EXP073HQ_C2_BIT_EXACT_TERMINAL_TIME_CANONICALIZATION_BUILD_AUDIT_V0_1`.

Classification ceiling: `SUPPORT_PLUS_0_PLUS_0`; `cosmological_run_started=false`; `raw_record_set_admitted=false`; `scientific_model_authority_created=false`.

Only after raw-log HQ PASS may a separately versioned HO-v0.2 runtime contract bind the new source identity and rerun the unchanged 28-node reference producer.
