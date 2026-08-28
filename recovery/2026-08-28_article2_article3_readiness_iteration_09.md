# DSIR Article 2 / Article 3 readiness — iteration 09

**Date:** 2026-08-28

These percentages measure repository readiness for writing a complete, internally consistent and defensible article draft. They do not measure probability of publication and do not reward positive results over falsifications.

## Readiness

| Article | Iteration 08 | Iteration 09 | Change |
|---|---:|---:|---:|
| Article 2 | 93% | **95%** | +2 pp |
| Article 3 | 44% | **44%** | 0 pp |

## Article 2 — why readiness rises to 95%

Iteration 08 closed the empirical orientation/sign ambiguity with Exp071K/L. Iteration 09 converts that result into a coherent general DSIR geometry and removes the main internal wording inconsistency that remained in the Article-2 repository.

### 1. Ray / line / nuisance-subspace formalism

New method note:

`docs/DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md`

For metric `M`, oriented rays use

`cos(theta_ray) = r^T M n / (||r||_M ||n||_M)`.

For a two-sided scalar nuisance the correct line angle is

`theta_line = arccos(|r^T M n|/(||r||_M ||n||_M)) = min(theta_ray, pi-theta_ray)`.

For a nuisance basis `N`, the metric-orthogonal projector is

`P_N = N (N^T M N)^+ N^T M`,

with nuisance-orthogonal response

`r_perp = r - P_N r`

and surviving fraction

`eta_N = ||r_perp||_M / ||r||_M`.

This gives Article 3 a mathematically explicit future nuisance-quotient target without authorizing the quotient before its observational gates.

### 2. Internal numerical validation of line geometry

The Exp071J positive-K2 oriented angles were

- `166.4386944060 deg` to GDM cs2+;
- `164.9270967302 deg` to GDM cv2+.

Treating K2 correctly as a two-sided line predicts

- `13.5613055940 deg`;
- `15.0729032698 deg`.

The independent fresh Exp071L negative K2 run measured

- `13.5502602743 deg`;
- `15.0708844313 deg`.

Prediction-versus-fresh-run differences are only

- `0.0110453197 deg`;
- `0.0020188384 deg`.

Thus the new line interpretation is quantitatively validated by a genuinely fresh opposite-sign displacement rather than merely introduced post hoc.

### 3. Consolidated claim matrix v0.2

New authoritative consolidation:

`docs/ARTICLE2_CLAIM_MATRIX_V0_2_ORIENTATION_CONSOLIDATION.md`.

It revises the Exp071I interpretation and adds the following closed claims:

- A2-C14R: source-audited `t_tot` positive-K2 **oriented-ray** separation;
- A2-C15: amplitude-mode quotient robustness of that positive ray;
- A2-C16: all-24-ablation broad support of that positive ray;
- A2-C17: fresh two-sided K2 nuisance falsification;
- A2-C18: general ray/line/subspace DSIR geometry.

The new core narrative is

`static degeneracy -> oriented temporal/velocity separation -> amplitude/support robustness -> two-sided nuisance falsification -> ray/line/subspace geometry -> future observational nuisance-subspace test`.

This supersedes any older wording that can be read as saying the velocity channel generically removes the entire K2 nuisance.

## Article-2 remaining 5%

The remaining repository work is now mainly closure and presentation rather than repair of the central logic:

- propagate v0.2 wording into manuscript/abstract/figure captions;
- build the final ray-versus-line/subspace figure and compact comparison table;
- decide whether one genuinely independent known-sector nuisance family is needed as a final external specificity check, rather than repeating K2 variants;
- perform final claim/provenance audit after those edits.

No additional K2 sign or single-support test is required merely to support the current ray/line result.

## Article 3 — unchanged at 44%

Latest check of Exp073R1 run `33175886694`:

- `source-index`: SUCCESS;
- `metacal-map`: still `in_progress`;
- current step: `Sequentially stream authoritative metacal object and execute frozen mapper`;
- true reproduction assertion remains pending.

Therefore no new Article-3 readiness credit is permitted.

- G7 OPEN
- G8 OPEN
- G9 OPEN
- covariance/whitening NOT AUTHORIZED
- nuisance quotient NOT AUTHORIZED

The new ray/line/subspace result strengthens the **design** of the future nuisance quotient, but it does not close any Article-3 observational gate by itself.

## Current required percentages

**Article 2 repository readiness for writing: 95%.**

**Article 3 repository readiness for writing: 44%.**
