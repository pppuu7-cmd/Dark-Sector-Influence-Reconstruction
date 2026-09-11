# Layer-B local-vs-global convergence synthesis v0.2

Date: 2026-09-11. Scope: DSIR Article III numerical-method interpretation. This document extends v0.1 with the validated canonical 8193->16385 frontier and the independently validated top-64 cancellation/confounder diagnostics. It does not modify v0.1 or any frozen scientific rule.

## Frozen scientific result
The canonical 8193->16385 support comparison remains `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0` under the frozen strict criterion

`max_atomic_coarse_vs_fine_relative_component_difference < 1e-3`.

The observed maximum relative component difference is `0.012484060640679777`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native CLASS `k_per_decade_for_pk=20`, centered-cubic interpolation, physical support/masks, 107-row accounting, invalid-row fraction `<=0.05`, retained dimension `>=15`, unsupported count `=0`, and requested-node lookup mismatch `<=1e-12` remain unchanged.

No 32769 execution is authorized by this synthesis. Covariance restriction remains unauthorized. Wm_S3 remains closed.

## What the earlier local-vs-global synthesis established
Version 0.1 showed that the full-support non-convergence could not be reduced to the two historical Exp073IR worst original-pair probes: the adopted centered-cubic local diagnostics were already below `1e-3` at those targeted probes while later full-support gates remained much larger. That required an explanation involving other atoms, argmax migration, response-scale effects, or a different full-support numerical regime.

## New population-level evidence
The single permitted unchanged top-64 census retry completed successfully as run `34614119149`, attempt 2, job `103331912096`. All 64 ordered atoms reproduced their primary values with maximum reproduction relative error `0.0`; `21/64` atoms are at or above the strict `1e-3` cross-grid discrepancy threshold.

The population association between minimum cancellation scale and cross-grid discrepancy is negative: full top-64 Spearman `rho=-0.5341210955390675`. This relation survives explicit confounder checks validated by source run `34628562363` and independent terminal consumer run `34628673923`:

- exact physical duplicate collapse: `64 -> 58` unique physical atoms, `19/58 >=1e-3`, Spearman changes only to `-0.5163800793626381`;
- DES-only block: `55` atoms, `18 >=1e-3`, Spearman `-0.5078643578643579`, so repeated BOSS_GL64 atoms do not generate the population association;
- cancellation-scale quartiles, from lowest to highest scale, contain `13/16`, `6/16`, `1/16`, `1/16` atoms at or above `1e-3`;
- median cancellation scale among `>=1e-3` atoms divided by that among `<1e-3` atoms is `0.13484119009229173`.

The durable terminal support authority is `docs/dsir4/authority/LAYERB_POST_16385_TOP64_CONFOUNDER_TERMINAL_AUTHORITY_V0_1.json`.

## Exploratory stress test and its boundary
A separate exact-duplicate-collapsed analysis on the 58 unique physical atoms was frozen in code before its workflow execution, but the test family itself was selected after inspecting the population structure. It is therefore explicitly post-hoc/exploratory rather than preregistered confirmatory inference.

Run `34628932658` gives:

- unique-atom Spearman `rho=-0.5163800793626381`;
- lowest cancellation-scale quartile versus the rest: table `[[12,3],[7,36]]`, odds ratio `20.571428571428573`, one-sided Fisher `p=1.6168593301143046e-05`;
- lower half versus upper half of cancellation scales: table `[[17,12],[2,27]]`, odds ratio `19.125`, one-sided Fisher `p=2.3321946203480245e-05`;
- median cancellation-scale ratio (`>=1e-3` / `<1e-3`) `0.12041078397110301`.

These values are descriptive robustness evidence. They must not be presented as a preregistered hypothesis test or used to replace the frozen convergence criterion.

## Updated interpretation
The residual non-convergence is no longer best described as an unexplained single-hotspot anomaly. The strongest validated interpretation is now a **population-distributed numerical-conditioning pattern consistent with finite-difference cancellation amplification**:

1. the maximum remains scientifically NOT_CONVERGED under the frozen gate;
2. the top-64 census shows many threshold exceedances rather than only one outlier;
3. smaller cancellation scales are systematically associated with larger cross-grid discrepancies;
4. that association survives exact duplicate collapse and DES-only stratification;
5. exceedances are strongly enriched in the lowest cancellation-scale quartiles.

This materially strengthens a numerical-conditioning diagnosis. It does **not** prove that cancellation is the unique causal mechanism, does not establish physical convergence, and does not authorize changing `h`, the tolerance, interpolation, masks, estimator, or atom set to make the gate pass.

## Article III manuscript-safe use
The evidence supports a methods/limitations statement of the following substance: the strict full-support convergence gate remains failed at the canonical 8193->16385 rung, while independent post-gate diagnostics localize the residual primarily to a distributed cancellation-sensitive numerical-conditioning regime rather than to duplicate bookkeeping or one observational block. The manuscript must preserve the distinction between **scientific gate result** (NOT_CONVERGED) and **diagnostic mechanism evidence** (support-only `+0/+0`).

Do not write that the model is converged, that the residual is physically negligible, or that the cancellation analysis rescues the failed gate.

## Repository-readiness blocker audit
The top-64 cancellation/confounder branch is support-complete for the present Article III cycle. Additional correlation/quartile variants are low-information unless a genuinely different alternative explanation is prospectively specified.

Remaining blocker classes are:

1. **Scientific frontier blocker — OPEN:** canonical 8193->16385 is still NOT_CONVERGED at `0.012484060640679777 > 1e-3`.
2. **Next-rung authorization/resource blocker — OPEN:** the deterministic ladder defines the next density in principle, but this synthesis creates no 32769 execution authority; canonicalization/resource/lifecycle feasibility and anti-duplication requirements remain binding before any such run.
3. **Downstream science blocker — OPEN by dependency:** covariance restriction and Wm_S3 remain prohibited while the scientific frontier is unresolved.
4. **Numerical-conditioning mechanism documentation — CLOSED for current cycle:** top-1, top-64, duplicate-collapse, block-stratified, quartile-enrichment, terminal-consumer and exploratory unique-atom evidence are now connected in one methods synthesis with explicit inference boundaries.
5. **Further same-family diagnostic proliferation — NOT A BLOCKER:** more variants of the already-closed population association are not required for Article III repository readiness unless they test a prospectively defined distinct confounder.

## Readiness consequence
This synthesis improves documentary integration but creates no new scientific gate result. Therefore `ARTICLE3_REPOSITORY_READINESS` remains `68%` and funnel-freeze readiness remains `67%`.
