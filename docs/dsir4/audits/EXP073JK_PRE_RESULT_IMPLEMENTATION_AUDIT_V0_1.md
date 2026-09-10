# Exp073JK pre-result implementation audit v0.1

Date: 2026-09-10. Scope: DSIR Article 3 / Exp073JK implementation and infrastructure only.

Status: completed while authoritative Exp073JK run 34495159732 / job 102931623100 was still IN_PROGRESS at the frozen numerical step. No Exp073JK response result or partial numerical output was inspected. This audit is +0/+0 and cannot alter the frozen Exp073JK decision rule.

## Contract/implementation checks

- Prospectively frozen preregistration remains `docs/dsir4/prereg/EXP073JK_ARTICLE3_LAYERB_COMMON_GRID_SECOND_REFINEMENT_CONVERGENCE_V0_1.md`.
- Exp073JK inherits the exact Exp073IR atom traversal/accounting and uses Exp073JJ `ResolutionSuite` only as a deterministic common-grid response wrapper.
- Inherited suite slot `10` maps to guarded base N=1024 (1025 requested nodes); inherited slot `20` maps to guarded base N=2048 (2049 requested nodes).
- CLASS native `k_per_decade_for_pk` remains exactly 20.0 for both slots. Therefore the inherited slot names are not reinterpreted as native kpd and the prior native-kpd confound is not reintroduced.
- Guard construction remains response-blind from the frozen JI target extrema; both grids require lower guard count 0 and upper guard count 1.
- The centered-cubic Lagrange interpolation rule in x=ln(k), finite-difference h=1e-4, REL_TOL=1e-3, physical domain, masks and support criteria are unchanged.
- JJ authority identity and independently verified artifact SHA are enforced before execution; JI geometry identity is also enforced.
- Forbidden downstream covariance/whitening/nuisance/relation-null reads are explicitly rejected before classification.

## Capacity audit

The exact binary64 geometric grids and the same `.17g` comma-separated serialization used by `class_params` were reproduced without evaluating any physical response.

- guarded N=1024: 1025 requested nodes; serialized `k_output_values` length = 22489 characters.
- guarded N=2048: 2049 requested nodes; serialized `k_output_values` length = 44961 characters.
- Frozen Exp073JK parser capacity `_ARGUMENT_LENGTH_MAX_=65536` therefore has positive margin for both current suites.
- Frozen Exp073JK `_MAX_NUMBER_OF_K_FILES_=2304` exceeds the maximum requested count 2049.

Thus the active Exp073JK architecture is not expected to fail merely because of either frozen input-capacity limit.

## Conditional future infrastructure bound

This is NOT a preregistration of a later scientific gate. It is only an infrastructure warning derived without Exp073JK response output.

If a later sequential base N=4096 refinement is scientifically authorized after consuming Exp073JK, the analogous guarded grid would contain 4097 requested nodes and its `.17g` serialized `k_output_values` string is approximately 89918 characters. Therefore the current JK capacities would be insufficient for that hypothetical future step. Any such later gate must prospectively enlarge both limits before execution, e.g. `_MAX_NUMBER_OF_K_FILES_` above 4097 and `_ARGUMENT_LENGTH_MAX_` above 89918, with exact provenance and no change to physics or thresholds.

This finding must never be used to infer the Exp073JK numerical result or to tune the acceptance criterion.
