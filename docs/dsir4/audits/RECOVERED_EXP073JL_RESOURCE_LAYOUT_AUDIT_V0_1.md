# Recovered Exp073JL — resource-layout audit v0.1

Date: 2026-09-11. Scope: DSIR Article III implementation/resource preparation only. Effect `+0/+0`. This is not preregistration and does not authorize recovered Exp073JL execution. It was prepared while authoritative Exp073JW repeat `34540689350` was still running, without inspecting partial JW numerical output.

## Exact original construction count

The inherited common-grid `ResolutionSuite.__init__` constructs four CLASS instances and retains all four in `self.models` until `close()`.

The frozen Exp073IR parent creates that suite three separate times during the full traversal:

1. coarse/production suite for DES-2001 plus BOSS GL64;
2. fine/dense suite for DES-2001 plus BOSS GL64 direct coarse/fine comparison;
3. a second fine/dense suite for BOSS GL128 dense-z stability control.

Therefore the historical full-JL execution shape is **12 CLASS constructions total with up to 4 simultaneously live**. This is an execution/lifecycle fact only; it does not change the scientific contract.

The recovered one-live architecture can preserve all three scientific traversal phases with **8 CLASS constructions total** by evaluating role-major rather than request-major:

- coarse: 4 roles, each role traverses DES-2001 + BOSS GL64 before cleanup;
- fine: 4 roles, each role traverses DES-2001 + BOSS GL64 + BOSS GL128 before cleanup.

Thus GL128 must be folded into each already-live fine role, not implemented as a third four-build suite. This is necessary for the recovered run to use exactly the lifecycle tested by Exp073JW if JW passes.

## Response-local storage bound

A simple fail-closed implementation can use scratch memmaps rather than holding multiple CLASS instances. For an intentionally conservative full rectangular DES backing layout:

- one raw scalar role buffer: `2001 * 12288 * 8 = 196,706,304` bytes = 187.59375 MiB;
- four raw role buffers for the current lattice: `786,825,216` bytes = 750.375 MiB;
- coarse two-component response store needed for later fine comparison: `2001 * 12288 * 2 * 8 = 393,412,608` bytes = 375.1875 MiB;
- peak simple fine-stage scratch if the four fine raw-role buffers coexist with the retained coarse response store: `1,180,237,824` bytes = 1125.5625 MiB ≈ 1.099 GiB, excluding small BOSS/request-plan/metadata buffers.

This layout is deliberately conservative and response-blind. It is small enough that there is no scientific reason to compress, quantize, average, downsample or alter arithmetic. A more compact flattened union-target layout may be used only if its request-plan identity and replay equivalence are prospectively frozen and statically audited; compactness must never change which atoms are evaluated.

## Memory versus disk boundary

The four raw role operands may coexist as **scratch files/memmaps** after each role's CLASS instance has been cleaned up. `max_live_instances=1` refers to solver lifetimes, not to process-local storage of already-evaluated raw operands required by the frozen finite-difference estimator.

Raw role operand storage remains same-process only. It must not be uploaded, checkpointed for cross-process scientific combination, or consumed by a later GitHub job. Only the terminal classified result and non-scientific provenance/aggregate receipts may leave the process according to the eventual prospectively frozen recovered-JL contract.

## Arithmetic-preservation requirement

For each request payload, after all four role operands are locally available, recovered JL must preserve the inherited floating-point operation order exactly:

- alpha component: `abs((alpha_minus - reference) / (-H))`;
- beta component: `abs((beta_plus - beta_minus) / (2*H))`;
- components assembled with the same column order;
- coarse/fine comparison: finite/positive status first, then `abs(coarse-fine) / maximum(abs(coarse),abs(fine))`, aggregate by the same maximum operation.

The BOSS GL128 fine response is used only for the inherited dense-z validity control; it must not enter the coarse/fine maximum-relative-difference statistic.

## Pre-result implementation invariants

Any future recovered-JL helper should expose machine-checkable receipts for: exactly 8 solver constructions; maximum one live solver; exact role order on each lattice; exact request-plan identity per suite; fine GL128 included within the same four fine solver lifetimes; zero cross-process raw-operand combination; exact canonical-grid SHA identities; zero unsupported targets; lookup mismatch <= `1e-12`; and unchanged parent/accounting hashes.

## Readiness boundary

This audit closes only an implementation ambiguity: the recovered full traversal does not require 12 solver constructions and does not require four simultaneous solver lifetimes. It does **not** establish that eight-build execution is feasible; that question belongs exclusively to terminal, independently verified Exp073JW. It therefore does not increase `ARTICLE3_REPOSITORY_READINESS=68%` or funnel-freeze readiness `=67%`, does not authorize covariance restriction, and does not open Wm_S3.
