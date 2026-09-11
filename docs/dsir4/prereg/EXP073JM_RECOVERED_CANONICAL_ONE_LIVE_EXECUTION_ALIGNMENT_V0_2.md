# Exp073JM — recovered canonical one-live execution alignment v0.2

Date frozen: 2026-09-11 while recovered Exp073JL retry `34544293038` is still in its frozen numerical step and before the terminal JL verdict is known. Scope: implementation/provenance alignment only. The scientific contract remains `EXP073JM_ARTICLE3_LAYERB_COMMON_GRID_FOURTH_REFINEMENT_CONVERGENCE_V0_1.md` unchanged.

## Activation — corrected to the original frozen preregistration

This implementation may execute only if a terminal recovered Exp073JL authority has already been independently verified and its exact classification is `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`.

Classification plus independent artifact verification is the activation condition. The v0.1 implementation's extra requirements `JL retained_after_layer_b == 107` and `JL unsupported_target_evaluations == 0` are removed from activation, exactly as required by the pre-verdict `EXP073JM_ACTIVATION_ALIGNMENT_AUDIT_V0_1.md`. Those support quantities remain part of the fresh JM run's own frozen checks and are not weakened.

If JL is CONVERGED, INVALID_INFRA, malformed, unverified or absent, JM must not run.

## Canonical grids — same mathematical rung, stronger provenance

The original JM preregistration fixed base 4096 -> 8192 with response-blind guard counts `(0,1)`, hence requested-node counts 4097 -> 8193. v0.2 consumes exact canonical byte streams for that same rung rather than regenerating them on the production host.

Coarse 4097 is exactly the already-authoritative Exp073JT fine/JL-4097 lattice:

- decoded `<f8` SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`;
- u64hex/text SHA256 `290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7`.

Fine 8193 was materialized response-blind while JL was unresolved, using a prospectively fixed anchor-selection rule. Six of eight replicas exactly reproduced the authoritative 4097 anchor, and all six produced byte-identical 8193 candidates. The committed canonical 8193 authority records:

- decoded `<f8` SHA256 `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`;
- u64hex/text SHA256 `90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6`;
- requested nodes 8193, guard counts `(0,1)`.

Observed host variants differ only at 1-ULP scale but are non-authoritative and must not be used in production.

## Recovered execution

Preserve the exact original JM scientific evaluation but schedule solver lifetimes using the already-audited recovered architecture:

- response-blind observational request plan remains the exact inherited 107-row plan: 377 nonempty DES calls/role, BOSS GL64 64 calls/role, fine-only GL128 128 calls/role, 441 coarse and 569 fine calls/role, 4040 total across eight roles;
- coarse model roles `reference`, `alpha_minus`, `beta_plus`, `beta_minus`, one CLASS lifetime at a time;
- fine roles in the same order, one CLASS lifetime at a time;
- exactly 8 CLASS constructions total, `max_live_instances=1`;
- raw finite-difference operands remain within one Python process;
- exact inherited JJ requested-node lookup and centered-cubic interpolation arithmetic are reused;
- exact Exp073IR request boundaries and 107-row accounting are replayed bit-identically;
- fine GL128 remains the inherited dense-z finite/nonzero/row-label stability control only.

The finite-difference estimator, `h=1e-4`, strict `REL_TOL=1e-3`, native kpd20, physical domain, masks, BOSS operators and Layer-B thresholds are unchanged.

## Infrastructure capacities — unchanged from JM preregistration

JM's pre-frozen infrastructure-only capacities remain `_MAX_NUMBER_OF_K_FILES_=9216` and `_ARGUMENT_LENGTH_MAX_=262144`, with exact one-replacement and pre/post SHA provenance. These capacities do not alter scientific arithmetic.

## Mandatory 8193 resource gate before production

Exp073JW proved eight-build/max-one-live feasibility through the canonical 4097 lattice, not the 8193 lattice. Therefore even after a hypothetical JL NOT_CONVERGED activation, JM production must not launch until a separate no-science/resource-only pilot demonstrates that the canonical 8193 lattice can complete four sequential model-role CLASS constructions under capacities 9216/262144 with one live solver, finite transfer responses, zero unsupported requested nodes on a fixed pilot target set and lookup mismatch `<=1e-12`.

That resource pilot must not compute or classify the full JM 107-row coarse-vs-fine convergence result and cannot select/alter the grid.

## Frozen JM classification — unchanged

A complete valid JM production run is `COMMON_GRID_FOURTH_REFINEMENT_CONVERGED_PLUS_0_PLUS_0` only if the original preregistered conditions all pass, including strict maximum relative component difference `<1e-3`, zero unsupported targets, no finite/nonzero-status change, no row-label change, no BOSS dense-z disagreement, invalid-row fraction `<=0.05`, retained dimension `>=15` and lookup mismatch `<=1e-12`.

Otherwise a structurally valid run is `COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Provenance/build/canonical-grid/lifecycle failures remain `INVALID_INFRA_PLUS_0_PLUS_0`. Every valid JM outcome remains support-only `+0/+0`.

## Static gate

Before any JM resource or production execution, a no-CLASS/no-science static audit must prove: activation contains no extra scientific predicates; exact canonical 4097/8193 identities are pinned; runtime `guarded_lattice`/`geomspace` is absent from production code; capacities are 9216/262144; exact estimator/interpolation/request-plan and 8/max-one lifecycle are preserved; the original JM result tokens/thresholds are unchanged.

Creating this alignment does not activate JM and does not change Article III readiness.
