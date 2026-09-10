# Exp073JO — Article 3 Exp073JL durable response-checkpoint recovery v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / process recovery only.

Status: PROSPECTIVELY FROZEN AFTER TWO EXP073JL HOSTED-RUNNER SHUTDOWNS AND BEFORE ANY VALID EXP073JL NUMERICAL RESULT EXISTS.

## Triggering process failures
The prospectively frozen Exp073JL science is unchanged: guarded base N=2048 (2049 requested) versus base N=4096 (4097 requested), one response-blind upper guard each, native CLASS `k_per_decade_for_pk=20` for both suites, centered-cubic Lagrange interpolation in `ln(k)`, finite-difference `h=1e-4`, `REL_TOL=1e-3`, exact Exp073IR support/traversal and frozen domain.

Original JL workflow run `34497160814` was interrupted twice during numerical step 10 by GitHub-hosted runner shutdown signals. Attempt 1 job `102938434376` and attempt 2 job `102944693569` produced no JL numerical result artifact. These are process/infrastructure `+0/+0`, neither CONVERGED nor NOT_CONVERGED.

Exp073JO is not a new scientific gate. It is an execution-only recovery architecture for the exact frozen JL computation.

## Frozen science identity
Exp073JO MUST execute the exact existing JL implementation `ci/exp073jl_article3_layerb_common_grid_third_refinement_convergence_v0_1.py` under its frozen preregistration and authority inputs. It may intercept only calls to the existing `ResolutionSuite.response(z, targets)` interface to persist/replay already completed response arrays.

It MUST NOT change:
- any CLASS-IV/CAMB source identity or physics patch;
- base or guarded k nodes;
- native kpd=20;
- interpolation arithmetic or stencil;
- finite-difference models or `h=1e-4`;
- DES/BOSS target geometry, masks, traversal order or row accounting;
- `REL_TOL=1e-3` or any physical-support threshold;
- the JL result schema/classification logic;
- covariance/Wm_S3 authorization state.

The output scientific result must be the ordinary frozen Exp073JL result; JO contributes only a process receipt.

## Atomic checkpoint unit
A durable unit is one fully completed original `ResolutionSuite.response(z, targets)` invocation. No partial CLASS model or partial response call may be admitted.

For every cached response call, bind at least:
- fixed recovery contract ID `EXP073JO_ARTICLE3_JL_DURABLE_RESPONSE_CHECKPOINT_RECOVERY_V0_1`;
- suite slot 10 or 20 and its monotonically increasing call index within that slot;
- binary64 `z.hex()`;
- SHA256 of exact contiguous little-endian float64 target stream and target count;
- SHA256 of exact contiguous little-endian float64 guarded-node stream for that suite;
- exact response shape `(target_count,2)`, dtype `<f8`, nbytes and SHA256 of response bytes;
- response-call audit state needed to reproduce the original mutable suite audit: response-call count, target-evaluation count, unsupported-target increment, requested-node coordinate-mismatch cumulative maximum, and k-key state.

Cache replay is permitted only when every key/provenance/hash/shape/dtype/index check succeeds. Corrupt, non-prefix, mismatched or ambiguous cache content must fail closed; it may never be silently accepted.

## Sequential-prefix rule
Within each suite slot, durable cache entries must be consumed in the exact original response-call order. The stored slot call index must equal the next expected call index. This prevents an accidentally matching `(z,targets)` payload from being replayed at a different traversal position.

Durable pushes may batch multiple complete calls for efficiency, but only complete files are committed. The dedicated checkpoint namespace is frozen as `checkpoints/exp073jo-jl-response-v0-1`; checkpoint commits must be CI-skipping/process-only and must not modify main scientific files.

Flush cadence is prospectively fixed to at most 16 newly computed response calls between durable pushes, plus a forced flush when a suite closes and at successful wrapper completion. A runner loss may therefore discard at most the unpushed suffix; previously pushed complete response calls remain reusable.

## Replay audit semantics
On a cache miss, execute the unmodified parent `ResolutionSuite.response`, then persist its exact returned response and the corresponding audit transition.

On a cache hit, do not recompute the response; restore the exact `<f8` response bytes and apply only the previously recorded original audit transition/state needed to make the parent JL aggregation identical. Cache replay MUST NOT synthesize a better coordinate mismatch, remove unsupported targets, or change k-key provenance.

## Mandatory live history-independence control
Before scientific recovery execution, use the exact pinned CLASS-IV build and frozen JL grid to prove that skipping earlier read-only transfer queries does not change a later response result. Prospectively choose a small fixed response-blind sequence of valid physical targets and redshifts. Compare a trailing response computed after earlier queries with the same trailing response computed by a fresh otherwise identical suite without those earlier queries. Require exact array equality (bitwise float64 equality) and identical finite/nonzero pattern. If exact equality fails, Exp073JO is `INVALID_INFRA_PLUS_0_PLUS_0` and cache replay is forbidden.

A local cache round-trip regression must additionally prove exact response-byte identity and exact audit restoration on replay.

## Frozen result interpretation
If Exp073JO completes and the original frozen JL implementation emits a valid JL result, classify that JL result exactly against the already-frozen Exp073JL contract. The JO process receipt must state cache hits/misses, durable pushes, final checkpoint commit, contract fingerprint and live-control result.

A valid recovered JL CONVERGED result activates only the already-frozen Exp073JN branch. A valid recovered JL NOT_CONVERGED result activates only the already-frozen Exp073JM branch. JO itself remains process-only `+0/+0` and cannot authorize covariance restriction or Wm_S3.

Any checkpoint/hash/order/history-independence/git-durability failure is `INVALID_INFRA_PLUS_0_PLUS_0` and creates no JL authority.

## Anti-rescue rule
Checkpointing is execution persistence only. No tolerance change, density change, estimator change, denominator floor, rounding, smoothing, averaging, clipping, extrapolation, atom/row removal, altered mask/domain, effective-coordinate substitution or fiducial-P shortcut is allowed.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`.
