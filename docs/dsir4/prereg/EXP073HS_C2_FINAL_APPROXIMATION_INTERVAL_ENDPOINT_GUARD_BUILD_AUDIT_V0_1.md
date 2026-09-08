# Exp073HS — C2 final-approximation-interval endpoint guard build audit v0.1

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/AUDIT**. Scope: DSIR only; implementation support only.

## Frozen causal finding

Exp073HR `34230309394 / 102074480794` retained the accepted `ynew` and changed the diagnostic hook time argument to exact per-evolver `tfinal`, yet the first request still failed with `tau != dsir_c2_diag_tau_target`. Static reconciliation with `perturb_solve` shows why: `generic_evolver` is invoked once for each approximation interval, and the diagnostic hook executes at `done==_TRUE_` for every such invocation. Therefore non-final approximation intervals have a legitimate `tfinal=interval_limit[index_interval+1]` that is not the overall literal-z target. This is an implementation-control-flow defect, not a scientific/numerical failure.

## Allowed repair and exact semantics

Starting from the exact post-HQ chain, HS may add one diagnostic-only predicate in `source/perturbations.c`:

`dsir_c2_diag_is_exact_terminal_target(double tau)` returns true if and only if diagnostic mode is enabled **and** `tau == dsir_c2_diag_tau_target` by exact binary64 equality.

In `tools/evolver_ndf15.c`, the existing opt-in terminal hook condition may change only from:

`done==_TRUE_ && dsir_c2_diag_enabled()!=0`

to:

`done==_TRUE_ && dsir_c2_diag_is_exact_terminal_target(tfinal)!=0`.

The already frozen HQ hook body remains exactly on `tfinal` with the already accepted `ynew`. No tolerance, rounding, nearest-time test, interpolation, changed state, altered step, error estimate, acceptance logic, equation, IC, solver precision, model parameter, z/k coordinate, baseline, p8 setting, packet ABI, field order, or provenance rule may change.

This predicate is not an acceptance tolerance: it fail-closes by allowing the observation hook only on an approximation interval whose exact evolver endpoint equals the exact literal-z target. Earlier approximation intervals are ignored by the observation hook rather than misclassified as terminal endpoints.

## Static/build PASS

Hosted audit must reconstruct the exact post-HQ source, apply HS exactly once, prove a minimal diff restricted to the new predicate/declaration/condition, prove the hook body still uses `tfinal` and accepted `ynew`, and build full CLASS. No cosmological request or raw packet may be produced in HS.

Exact token: `PASS_EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1`.

Classification ceiling: `SUPPORT_PLUS_0_PLUS_0`; `cosmological_run_started=false`; `raw_record_set_admitted=false`; `scientific_model_authority_created=false`.

Only raw-log HS PASS may authorize a new separately versioned raw-runtime producer with the unchanged frozen `(0,0)` model/grid/config/ABI.
