# Layer-B response-blind canonical 16385 anchor materialization v0.1

Date frozen: 2026-09-11 while Exp073JO canonical-8193 resource pilot is active and before any Exp073JM 4097->8193 production response exists. Scope: DSIR Article III reproducibility infrastructure only; effect `+0/+0`.

## Authority
`docs/dsir4/methods/LAYERB_SEQUENTIAL_COMMON_GRID_REFINEMENT_LADDER_STANDARD_V0_1.md` already prospectively fixes that if a valid Exp073JM result is NOT_CONVERGED, the immediately next support rung is base 8192 -> 16384 with the same response-blind guard rule. This file does not activate that successor rung. It only permits materializing the already-determined new fine lattice before any JM scientific response is observed.

## Anchor-selection rule
The authoritative existing 8193 lattice is the anchor:
- committed file `docs/dsir4/canonical/EXP073JM_CANONICAL_FINE_8193_NODES_U64HEX_V0_1.txt`;
- decoded `<f8` SHA256 `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`;
- text/u64hex SHA256 `90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6`.

Run exactly eight independent GitHub-hosted replicas under NumPy 1.26.4. Each replica must, using the unchanged `guarded_lattice` rule inherited from Exp073JJ:
1. regenerate base 8192 and derive guards; only replicas whose complete 8193 bytes exactly match the authoritative anchor may vote;
2. independently generate base 16384 and derive its guard counts response-blind;
3. emit candidate u64hex bytes plus decoded/text SHA256 without reading any CLASS/scientific response.

At least four of eight replicas must exactly match the authoritative 8193 anchor. Among anchor-matched replicas, the 16384 guard counts, requested-node count, decoded candidate SHA, text SHA and bytes must all agree exactly. Host variants that fail the anchor match are retained diagnostically but do not vote.

## Boundaries
No CLASS solver may be imported or invoked. No Exp073JM result, partial result, convergence value or response artifact may be read. Branch activation must remain false. This materialization creates no scientific authority, does not authorize execution of the next rung, does not authorize covariance restriction and does not open Wm_S3.

If the quorum passes, the candidate may be committed as a dormant canonical next-rung byte stream. It may be used scientifically only if a future independently verified Exp073JM NOT_CONVERGED authority activates that exact deterministic successor and all required static/resource gates also pass.

Article III repository readiness remains 68%; funnel-freeze readiness remains 67%.
