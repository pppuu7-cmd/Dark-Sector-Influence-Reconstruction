# Exp073JQ — Article III slot20 same-run causal discrimination v0.1

Date frozen: 2026-09-10. Scope: DSIR Article III process/support only.

Status: PROSPECTIVELY FROZEN AFTER independently verified JO v0.5 exact-negative authority and BEFORE any JQ numerical response output. Effect `+0/+0`.

## Purpose

JO v0.5 validly failed the preregistered exact cross-execution history-independence control. A post-result diagnostic also showed machine-epsilon exact variability between independent hosted executions of the same phase/model using the same canonical node bytes. Therefore JO v0.5 cannot by itself distinguish query-history statefulness from cross-run execution nondeterminism.

JQ is a causal discrimination gate only. It introduces no tolerance, does not reinterpret the JO negative, does not evaluate Layer-B convergence, and creates no scientific/covariance/Wm_S3 authority.

## Frozen inputs

- canonical 4097-node binary SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`;
- canonical hex SHA256 `98cd360d0764a884471cb09b4504b79583e2ffaea4423389ec473e98b8656c2a`;
- canonical authority blob `b70ede7f8ecdf0cc67a9f20d33cafc1708eee8e8`;
- pinned CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c` with the unchanged build compatibility and public `d_m` exposure patches;
- capacity 4608, parser capacity 131072, native `k_per_decade_for_pk=20`;
- `h=1e-4`, `REL_TOL=1e-3` retained as lineage metadata only; JQ decision remains exact-bit only;
- exact model roles: reference `(0,0)`, alpha-minus `(-1e-4,0)`, beta-plus `(0,+1e-4)`, beta-minus `(0,-1e-4)`;
- exact `pre_z=0x1.3851eb851eb85p-1`, `tail_z=0x1.1c28f5c28f5c3p+0`;
- pre targets `[0.0013,0.0047,0.013,0.041]`, tail targets `[0.0019,0.0073,0.021,0.057]` as float64;
- identical public `CLASS get_transfer(..., output_format='class')`, exact `d_m`, k-unit conversion, `requested_values`, centered-cubic interpolation, and `<f8` serialization semantics inherited from JO v0.5.

## Same-run triple-instance protocol

Run four independent hosted jobs, one per frozen model role. Within each single job and on the same runner/environment, execute three completely fresh CLASS instances **in the frozen order below**:

1. `fresh_A`: instantiate/compute the model and query only `tail_z` at the four frozen tail targets; destroy the instance.
2. `after_history`: instantiate/compute an otherwise identical model; query `pre_z` at the four frozen pre targets and then query `tail_z` at the four frozen tail targets on that same instance; destroy it.
3. `fresh_B`: instantiate/compute a third otherwise identical model and query only `tail_z`; destroy it.

All three instances must load the same committed canonical node bytes and must verify the exact canonical SHA before CLASS construction. OMP/OpenBLAS/MKL/NUMEXPR thread counts remain 1.

Each job records exact 32-byte `<f8` tail payloads and SHA256 for all three instances plus finite/positive masks and coordinate-recovery diagnostics. It must compare only exact bytes/`np.array_equal`; no approximate threshold is permitted in the JQ decision.

## Per-model causal classification

The decision order is frozen:

1. If `fresh_A` is not exactly equal to `fresh_B`, classify that model `SAME_RUN_FRESH_REEXECUTION_NOT_EXACT_PLUS_0_PLUS_0`. Query-history causality is unresolved for that model because fresh reexecution itself is not bitwise stable.
2. Else, if `fresh_A == fresh_B` exactly but `after_history` differs, classify `SAME_RUN_HISTORY_DEPENDENCE_CONFIRMED_PLUS_0_PLUS_0`.
3. Else, if all three are exactly equal, classify `SAME_RUN_HISTORY_INDEPENDENCE_PASS_PLUS_0_PLUS_0`.
4. Any identity/build/payload failure is `INVALID_INFRA_PLUS_0_PLUS_0` and has no causal interpretation.

## Aggregate classification

Aggregate requires all four valid model receipts with identical canonical/provenance identities.

- If any model is `SAME_RUN_FRESH_REEXECUTION_NOT_EXACT_PLUS_0_PLUS_0`, aggregate `SAME_RUN_SOLVER_REEXECUTION_NONDETERMINISM_DETECTED_PLUS_0_PLUS_0`.
- Else if any model is `SAME_RUN_HISTORY_DEPENDENCE_CONFIRMED_PLUS_0_PLUS_0`, aggregate `SAME_RUN_HISTORY_DEPENDENCE_CONFIRMED_PLUS_0_PLUS_0`.
- Else all four must be same-run exact history-independent and aggregate `SAME_RUN_HISTORY_INDEPENDENCE_PASS_PLUS_0_PLUS_0`.

No majority vote, tolerance, rounding, ULP allowance, smoothing or other rescue is permitted.

## Interpretation ceiling / next architecture

JQ is diagnostic and cannot authorize checkpointed JL replay by itself. Its result prospectively chooses only the next process-design branch:

- fresh reexecution nondeterminism -> design a self-contained same-run atomic comparison architecture so scientific comparison operands never cross runner/process boundaries;
- confirmed history dependence with stable fresh repeats -> design a fresh-instance-per-query atomic architecture, again keeping comparison operands on the same runner;
- same-run history independence PASS -> cross-runner last-bit variability remains the identified JO confounder, so design same-run atomic comparison architecture rather than cross-run checkpoint replay.

In all branches the original JL scientific metric/tolerance/grid sequence remains unchanged. Article III readiness and overall funnel readiness do not change from JQ alone.