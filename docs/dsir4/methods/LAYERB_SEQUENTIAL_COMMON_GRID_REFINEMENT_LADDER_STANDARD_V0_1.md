# Layer-B sequential common-grid refinement ladder standard v0.1

Date prospectively frozen: 2026-09-11 while recovered Exp073JL retry `34544293038` is still running and before its terminal verdict is known. Scope: DSIR Article III numerical-convergence methodology. This standard does not alter any already-frozen JL/JM/JN threshold or result.

## Purpose

Remove the remaining researcher degree of freedom in choosing a denser common grid after a valid NOT_CONVERGED support result. Grid density must no longer be chosen in response to the observed numerical maximum.

## Deterministic refinement rule

For a support-convergence comparison whose coarse base lattice has `N` physical `np.geomspace(KMIN,KMAX,N,float64)` points, the immediately next sequential comparison is fixed to:

- coarse base `2N`;
- fine base `4N`;
- the same response-blind centered-cubic guard derivation inherited from Exp073JI;
- exact base-node identity preserved inside each guarded lattice;
- the same judged physical support, finite-difference estimator, interpolation, masks, row accounting and strict tolerance.

Equivalently, after every valid NOT_CONVERGED result, both members of the comparison shift one rung upward and base density doubles. No intermediate density, hand-picked density, random density or result-dependent density is allowed.

Existing rungs are therefore interpreted as one deterministic ladder:

- Exp073JL: base 2048 -> 4096, guarded requested counts 2049 -> 4097;
- conditional Exp073JM: base 4096 -> 8192, guarded requested counts 4097 -> 8193;
- if a valid JM result is NOT_CONVERGED, the next support rung is fixed in advance to base 8192 -> 16384 with guard counts derived by the same response-blind rule;
- further valid NOT_CONVERGED outcomes continue by the same doubling rule.

This standard fixes the density sequence, not an unlimited authorization to execute arbitrarily large jobs.

## Canonicalization rule

A support rung must never use execution-host regeneration as its scientific grid authority once a canonical byte stream exists.

Before any new rung executes:

1. any coarse grid already canonical from the previous rung must be reused byte-for-byte;
2. the new fine grid must be materialized response-blind before scientific response evaluation;
3. materialization must be anchored to an already-authoritative lower-rung grid so host binary64 variants cannot vote equally with the established lineage;
4. candidate selection must be based only on prior canonical identities and replica agreement, never on a scientific response;
5. canonical `<f8` payload and u64hex/text SHA256 must be committed before the new support run.

The Exp073JM 8193 work performed while JL was still unresolved is the first explicit application of this rule. The observed 1-ULP host variants are reproducibility diagnostics, not new scientific lattices.

## One-live execution rule

Every future ladder rung must preserve the recovered architecture rather than returning to historical multi-live `ResolutionSuite` execution:

- exactly four model roles per lattice: `reference`, `alpha_minus`, `beta_plus`, `beta_minus`;
- role-major sequential solver lifetimes;
- `max_live_instances=1`;
- raw finite-difference operands remain within one Python process;
- exact inherited observational request order is fixed response-blind before solver evaluation;
- responses are replayed through unchanged Exp073IR atom/row accounting;
- dense GL128 remains a status/stability control unless a separately prospectively frozen contract says otherwise.

The number of CLASS constructions for a two-lattice rung is therefore exactly eight. Larger lattice node counts may enlarge infrastructure capacities, memory or wall time only; they may not alter the scientific estimator.

## Frozen convergence decision

For every support rung, scientific-support convergence remains strict:

`max_atomic_coarse_vs_fine_relative_component_difference < 1e-3`

with `h=1e-4`, native CLASS `k_per_decade_for_pk=20`, requested-node lookup mismatch `<=1e-12`, unchanged centered-cubic interpolation, unchanged finite/nonzero and row-label checks, unchanged BOSS dense-z control, Layer-B invalid-row fraction `<=0.05`, retained dimension `>=15`, and no forbidden downstream reads.

Equality at `1e-3` is not convergence. No denominator floor, averaging, smoothing, clipping, rounding, atom/row dropping, effective coordinate, altered physical support or tolerance rescue is permitted.

## Stopping rule

The ladder stops only in one of three prospectively defined ways:

1. **CONVERGED:** a valid support rung satisfies the strict frozen convergence rule. The next allowed step is a separately frozen fresh science-authorizing closure run on that admitted canonical architecture; the support rung itself remains `+0/+0`.
2. **VALID NOT_CONVERGED:** advance exactly one deterministic doubling rung, subject to response-blind canonicalization and resource feasibility gates.
3. **RESOURCE/INFRASTRUCTURE BOUNDARY:** if the next deterministic rung cannot be executed reproducibly under an independently audited feasible architecture, report numerical resolution as unresolved at the available resource boundary. Do not replace the rung with a scientifically different estimator, looser tolerance or result-dependent density.

An infrastructure failure of an individual attempt is not itself the resource-boundary conclusion; minimal prospective execution repair must be exhausted first without changing science.

## Infrastructure feasibility

Capacity/parser enlargements and wall-time/resource changes for later rungs are infrastructure-only and must be prospectively audited. A future rung may not execute merely because this ladder names its density. It still requires canonical bytes, parser/capacity proof, one-live lifecycle/resource proof, static implementation audit and anti-duplication check.

## Branch relation

If recovered JL is CONVERGED, the ladder stops at JL and the pre-frozen JN science-closure branch is the next route after recovered implementation alignment. If JL is NOT_CONVERGED, JM is the next deterministic support rung after its already-identified implementation alignment. If JM later NOT_CONVERGED, its successor density is already fixed by this standard rather than chosen from JM's observed value.

`INVALID_INFRA_PLUS_0_PLUS_0` selects neither a scientific closure branch nor a denser rung until the infrastructure defect is resolved.

## Authority and readiness boundary

This standard creates no scientific result, does not authorize covariance restriction or Wm_S3, and does not change `ARTICLE3_REPOSITORY_READINESS=68%` or funnel-freeze readiness `=67%`. Its value is methodological: the convergence stopping/density rule is now frozen before the pending JL result.
