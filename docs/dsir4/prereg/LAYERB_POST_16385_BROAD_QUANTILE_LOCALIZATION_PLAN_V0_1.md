# Layer-B post-16385 broad quantile localization plan V0.1

Status: prospectively frozen support-only diagnostic after V0.1 plateau/root-cause lanes completed. Scope: DSIR Article III only.

## Motivation fixed before execution
The first response-blind five-node probe found raw 8193-vs-16385 operand discrepancies far below the full-traversal plateau at its prospectively selected requests. That result justifies broader localization, but does not justify choosing points from observed scientific discrepancy. This plan therefore expands sampling using only canonical index geometry.

## Frozen selection
Use canonical 8193 interior indices exactly:
`[512,1024,1536,2048,2560,3072,3584,4096,4608,5120,5632,6144,6656,7168,7680]`.
These are uniform 1/16-grid interior quantiles, fixed without consulting the 107-row result or any partial discrepancy map.

Use exactly the same two previously frozen z anchors and the same four roles, h=1e-4, native kpd20, centered-cubic evaluation, pinned CLASS-IV/CAMB identities, capacity/parser compatibility patches and history-suppression execution patch as the validated V0.1 diagnostic. No alternative h, interpolation, tolerance, domain, mask, estimator, or scientific classifier is permitted.

## Independent lanes
1. `broad-raw`: evaluate raw operands at the 15 fixed k requests and two fixed z anchors on canonical 8193 and canonical 16385; report per-role/per-z values, hashes, requested-node lookup mismatch and cross-grid raw differences.
2. `broad-conditioning`: on the same fixed requests, compute only the already-frozen finite-difference numerators/responses and cancellation indicators at h=1e-4, and report cross-grid response differences.

Both lanes are +0/+0 support-only. They do not execute the full 107-row traversal and cannot authorize covariance restriction, Wm_S3, scientific PASS, altered stopping criteria, or a 32769 rung.

## Decision boundary
If broad fixed-geometry sampling still shows response differences orders of magnitude below 0.012484060640679777, deterministic non-nested sampling at ordinary interior requests is disfavored as a sufficient explanation and the next diagnostic must target another prospectively defined mechanism (for example z/row aggregation or edge/stencil structure) without reading partial science to tune locations. If broad sampling reveals a large deterministic hotspot, any follow-up localization must be separately preregistered before execution.

No outcome of this plan alone authorizes denser science.
