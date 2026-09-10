# Exp073JR — Article III Layer-B same-run atomic architecture preflight v0.1

Date frozen: 2026-09-11. Scope: DSIR Article III process/support only.

Status: PROSPECTIVELY FROZEN AFTER independently verified Exp073JQ same-run history-independence PASS and BEFORE any Exp073JR numerical output. Effect `+0/+0`.

## Purpose

Exp073JO v0.5 showed exact cross-execution last-bit mismatch while Exp073JQ showed exact equality for `fresh_A -> after_history -> fresh_B` inside one hosted runner/job for all four finite-difference model roles. Therefore future Layer-B scientific comparison operands must not cross runner/process boundaries.

Exp073JR is an architecture preflight. It does not evaluate the full 107-row JL convergence gate, does not change any scientific arithmetic, and cannot authorize covariance restriction or Wm_S3. It tests whether a memory-safe sequential-instance implementation on one runner is exactly equivalent to the original same-process four-model ResponseSuite arithmetic for frozen sample requests on both JL lattices.

## Frozen authority and science identities

- JQ authority: `docs/dsir4/authority/EXP073JQ_ARTICLE3_SLOT20_SAME_RUN_HISTORY_INDEPENDENCE_V0_1.json`.
- JQ canonical 4097-node SHA256: `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`.
- Exp073JL prereg blob: `0c143dd5b3c1c38b24fbb5b529d03ff9a2afdc58`.
- Exp073JL implementation blob: `91723736fedd090fa1c81b1fcff4f1f3601d2ce2`.
- pinned CLASS-IV: `ac627d54e9ce196a08878d1ba33999819925d19c`.
- finite-difference models exactly `(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`; `h=1e-4`.
- native `k_per_decade_for_pk=20` for both suites.
- coarse guarded lattice: base N=2048 + one upper guard = 2049 requested nodes.
- fine guarded lattice: base N=4096 + one upper guard = 4097 requested nodes.
- centered-cubic interpolation in `ln(k)` with unchanged stencil `{j-2,j-1,j,j+1}`.
- coordinate recovery mismatch ceiling remains `1e-12`.
- frozen scientific convergence threshold remains `REL_TOL=1e-3`; it is lineage metadata only in JR and is not used to rescue exact equivalence.

## Frozen sample requests

JR uses two response-blind interior requests already inside the certified JI geometry envelope:

1. `z_A = float.fromhex('0x1.3851eb851eb85p-1')` with targets `[0.0013,0.0047,0.013,0.041] Mpc^-1`.
2. `z_B = float.fromhex('0x1.1c28f5c28f5c3p+0')` with targets `[0.0019,0.0073,0.021,0.057] Mpc^-1`.

No target may be changed after seeing JR output.

## Two implementations compared on each lattice

### Reference implementation

Instantiate the original four CLASS model instances together using the exact JL/JJ response engine semantics, query the frozen request, then form the two response columns exactly as JL/IR:

- alpha response `abs((alpha_minus-reference)/(-h))`;
- beta response `abs((beta_plus-beta_minus)/(2h))`.

### Candidate memory-safe implementation

On the same runner and inside the same Python process, instantiate only one CLASS model at a time in fixed order `reference -> alpha_minus -> beta_plus -> beta_minus`; for each model evaluate the exact same requested lattice nodes and frozen target request, serialize the target values locally as `<f8`, destroy the CLASS instance, then form the response columns with exactly the same NumPy expressions as the reference implementation.

No raw operand is imported from another job/run/process. BLAS/OpenMP/MKL/NUMEXPR threads are fixed to 1.

## Exact preflight decision

For both lattices and both frozen requests, candidate and reference must satisfy all of:

- exact node identity and expected requested counts 2049/4097;
- zero unsupported target evaluations;
- requested-node coordinate mismatch `<=1e-12`;
- exact equality of finite masks and positive masks;
- `np.array_equal(reference_response, sequential_response)` is true;
- bytewise `<f8` SHA256 equality of the response payloads.

PASS classification:
`SAME_RUN_SEQUENTIAL_RESPONSE_ENGINE_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0`.

Any valid numerical inequality is:
`SAME_RUN_SEQUENTIAL_RESPONSE_ENGINE_NOT_EXACT_PLUS_0_PLUS_0`.

Identity/build/parser/capacity/provenance failure is:
`INVALID_INFRA_PLUS_0_PLUS_0`.

No tolerance, ULP allowance, rounding, averaging, clipping, response renormalization or estimator substitution is permitted.

## Prospective next branch

- Exact PASS permits preregistration of a full recovered JL execution using fixed response-blind chunks. Within each chunk/job, coarse and fine suites are evaluated sequentially with one CLASS model resident at a time; each JL relative-component comparison is completed locally before the chunk artifact is emitted. Aggregate may combine only scalar maxima, finite/nonzero booleans, row atom counts/status summaries, support counters and provenance—not raw coarse/fine scientific operands.
- NOT_EXACT forbids that sequential architecture and requires a different same-run architecture preserving the original four-instance semantics.
- INVALID_INFRA permits only minimal infrastructure repair.

JR itself creates no scientific Layer-B authority. Article III readiness remains 68% and overall funnel-freeze readiness remains 67% regardless of JR outcome.
