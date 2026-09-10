# Recovered Exp073JL — one-live implementation design audit v0.1

Date: 2026-09-11. Scope: DSIR Article III process/implementation preparation only. This document is **not** an Exp073JL preregistration, does not authorize execution, creates no scientific authority and does not change any frozen gate. It was written while authoritative Exp073JW repeat `34540689350` was still running and without using partial JW numerical output.

## Why the original JL execution architecture is resource-fragile

The unchanged scientific parent `ci/exp073ir_article3_real_layerb_common_response_v0_1.py` expects a `ResponseSuite` object and traverses the DES and BOSS requests first for the production/coarse suite, closes it, then traverses the dense/fine suite.

The inherited common-grid implementation in `ci/exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1.py` constructs all four finite-difference CLASS models in `ResolutionSuite.__init__` and retains them simultaneously in `self.models` until `close()`. Thus the original Exp073JL path can have four heavy fine-grid CLASS instances live at once even though the scientific estimator only needs four role operands, not four simultaneous solver lifetimes.

Exp073JQ/JR/JS/JT/JU/JV established the execution/canonicalization lineage needed to consider a sequential architecture. Exp073JW is the prospectively frozen resource pilot that must PASS before any recovered full-JL preregistration/launch is allowed.

## Non-negotiable frozen science

A recovered JL must preserve the original prospectively frozen scientific contract exactly:

- canonical coarse 2049 and fine 4097 node architectures representing the original C2048/F4096 plus one upper guard;
- exact committed canonical u64hex lattices from Exp073JT, never host-regenerated `np.geomspace` grids;
- pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`;
- native `k_per_decade_for_pk=20` for both suites;
- finite-difference `h=1e-4`;
- alpha-left `(alpha_minus-reference)/(-h)` and beta-symmetric `(beta_plus-beta_minus)/(2h)` estimator with the same `abs` and `column_stack` arithmetic/order;
- centered-cubic interpolation in `ln(k)` with stencil `{j-2,j-1,j,j+1}`;
- requested-node lookup mismatch ceiling `1e-12`;
- same Exp073IR parent identity, 53 DES + 54 BOSS retained coordinates, DES/BOSS geometry, radial/angular authorities, BOSS dense-z logic, atom traversal, finite/nonzero logic, row-label accounting, Layer-B invalid-row fraction and retained-dimension rules;
- exact original BOSS control structure: coarse and fine both use GL64 for the direct coarse/fine comparison, while fine additionally uses GL128 for the dense-z stability/row-label control;
- convergence criterion strictly `max_atomic_coarse_vs_fine_relative_component_difference < 1e-3`;
- no tolerance, averaging, smoothing, clipping, masking, effective-coordinate, fiducial-P, support-domain or estimator rescue;
- covariance restriction remains unauthorized and Wm_S3 remains unopened by support-only JL.

## Required execution inversion

The recovered implementation should invert only the solver/request loop nesting while leaving the frozen mathematical operations unchanged.

### 1. Compile a response-blind request plan

Before any CLASS response is inspected, deterministically reconstruct the same Exp073IR inputs and traversal geometry and compile immutable request plans containing the exact sequence/identity of all solver evaluations needed by the 107 retained rows:

- DES z grid and, for each z, the exact union target-k coordinates that the unchanged angular/radial masks request;
- row-to-active-target mappings needed to replay `update_summary` exactly;
- BOSS GL64 z nodes, exact needed target-k coordinates and row masks for both coarse and fine;
- BOSS GL128 z nodes, the same frozen needed target-k coordinates and row masks for the fine suite only, exactly as in the original parent dense-z control;
- stable offsets/shapes for flattening every request payload, with suite/phase identity explicit so GL64 comparison payloads cannot be confused with GL128 dense-z-control payloads.

The plans are derived solely from already-authorized geometry/selection inputs, not from CLASS response values. Their canonical identities should be recorded by SHA256 over explicit binary/JSON manifests before solver evaluation.

### 2. Role-major one-live evaluation

For each lattice independently, use model order exactly:

`reference -> alpha_minus -> beta_plus -> beta_minus`.

For each role:

1. construct exactly one CLASS instance using the frozen baseline/precision and the committed canonical lattice;
2. evaluate every request in that suite's immutable request plan in the same target order;
3. recover exact requested shared-grid nodes and apply the unchanged centered-cubic interpolation;
4. write only the interpolated raw role operands into process-local temporary storage indexed by the frozen request-plan offsets;
5. record lookup/provenance receipts;
6. call solver cleanup before constructing the next role.

At every instant `max_live_instances` must be 1. Across both lattices the full run therefore performs exactly eight CLASS constructions, matching the lifecycle proven by JW if JW passes. The fine role traversals must include both their GL64 comparison requests and GL128 dense-z-control requests before that role's solver is cleaned up; this preserves eight total builds rather than creating extra GL128-only solver constructions.

Raw role operands must remain inside the same Python process. They may be process-local NumPy arrays or local scratch memmaps used as memory backing, but must never be uploaded, transferred to another run/process, or treated as independent scientific artifacts.

### 3. Form the unchanged estimator after local role completion

After all four role operand buffers for a lattice exist locally, form responses using the exact inherited expressions and operation order. Do not substitute algebraically equivalent formulas if they change floating-point evaluation order.

The recovered code should preferably call one shared frozen estimator function used by the existing common-grid lineage or duplicate it byte-for-byte with a static source/hash guard.

### 4. Replay unchanged Exp073IR accounting

Using the response-blind plans' row/target mappings, replay the same row summaries and Layer-B accounting as Exp073IR. The implementation must reproduce:

- atom counts;
- finite/nonzero status;
- row labels;
- direct coarse-vs-fine comparison over DES and BOSS GL64 only;
- BOSS GL128 dense-z control on the fine suite and the resulting `boss_dense_z_disagreement` comparison against coarse/production labels;
- parent retained identity/order;
- invalid-row fraction and retained count.

For the coarse suite, retain only the data needed for the later exact coarse/fine atomic comparison. After fine GL64 responses are formed, compute the original relative-component diagnostic with the same arithmetic and aggregate maximum. Fine GL128 outputs are not part of that relative-component maximum; they serve only the inherited dense-z stability/row-label control, exactly as in Exp073IR.

### 5. Result classification remains original JL

The recovered execution wrapper must emit the original two valid scientific-support classifications only:

- `COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0`, or
- `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`.

Infrastructure/provenance/lifecycle/request-plan/canonical-grid failures remain `INVALID_INFRA_PLUS_0_PLUS_0` (or a prospectively equivalent infrastructure-only label that cannot be confused with scientific non-convergence). The prior failed hosted JL attempts remain historical infrastructure failures and are never reclassified.

## Pre-launch implementation checks required after JW PASS

A valid independently verified JW PASS may authorize preregistration/launch preparation, but before the recovered JL numerical result is trusted the implementation should fail closed on at least these checks:

1. committed coarse/fine text and decoded-node SHA identities match Exp073JT authority;
2. valid JV/JW authority identity and artifact provenance are enforced;
3. request-plan identities are produced before solver response evaluation;
4. exactly 8 solver constructions and `max_live_instances=1` are machine-counted;
5. every role for a suite visits the exact same plan offsets/shapes, including fine GL128 offsets;
6. unsupported-target count is zero and max requested-node mismatch <= `1e-12`;
7. estimator source/hash or exact arithmetic audit is frozen;
8. parent retained-ID/full-order hashes match Exp073IR authority;
9. GL64-only direct comparison and fine-only GL128 dense-z control are separated exactly as in the parent;
10. all forbidden downstream reads (`covariance`, `whitening`, `nuisance`, `relation/null`) remain false;
11. no raw role-operand scientific combination crosses a Python process boundary.

## Resource shape and implementation implication

The safest recovered architecture is not a drop-in `ResponseSuite.response()` that creates/tears down four solvers per call. Exp073IR invokes response evaluation across 2001 DES redshifts plus BOSS quadrature requests, so such a design would multiply solver constructions far beyond the frozen eight-build lifecycle and would test a different resource problem.

Instead, the recovered helper should own the traversal, compile the response-blind plans once, evaluate them role-major once per solver, and replay the existing Exp073IR accounting. This changes execution scheduling only; it must not change what physical atoms are evaluated or how their responses are classified.

## Authority boundary

At creation of this audit, Exp073JW repeat `34540689350 / job 103082427124` had passed identity/authorization, stack install and pinned CLASS-IV build and was inside its exact numerical eight-build resource step. No partial JW numerical output was inspected or used here.

This design audit has effect `+0/+0`. It cannot increase `ARTICLE3_REPOSITORY_READINESS` (68%) or funnel-freeze readiness (67%). Only terminal, independently verified gate results can change the scientific frontier according to the frozen ledger.
