# DSIR Article 2 / Article 3 readiness — iteration 08

**Date:** 2026-08-28

Percentages continue the frozen readiness rubric used in prior iterations. They measure **repository readiness for writing a complete, defensible article draft**, not probability of publication and not the strength of any single positive claim.

## Readiness

| Article | Iteration 07 | Iteration 08 | Change |
|---|---:|---:|---:|
| Article 2 | 90% | **93%** | +3 pp |
| Article 3 | 44% | **44%** | 0 pp |

## Why Article 2 rises to 93% despite a new negative result

This iteration closes two previously open falsification questions and therefore makes the eventual paper more defensible, even though the strongest velocity-specificity wording must be narrowed.

### Exp071K — broad support of the oriented positive-K2 result

Exp071K was preregistered before any ablation angle was evaluated and used only the immutable Exp071I artifact.

All 24 primary leave-one-support angles passed the inherited 45-degree separator:

- global minimum: `157.8212319078 deg`;
- leave-one-k minimum to GDM cs2: `158.1004089256 deg` after deleting `k=0.1 h/Mpc`;
- leave-one-k minimum to GDM cv2: `157.8212319078 deg` after deleting `k=0.1 h/Mpc`;
- leave-one-z minimum to GDM cs2: `165.4260431200 deg` after deleting `z=0.706`;
- leave-one-z minimum to GDM cv2: `163.8525879173 deg` after deleting `z=0.706`.

Finite-step bar2-bar5 diagnostics also retain minimum angles above `157.82 deg`.

Classification:

`K2_VELOCITY_SHAPE_BROAD_SUPPORT_PASS_EXP071K`.

This closes the loophole that Exp071J might be driven by a single k node or redshift slice.

### Exp071L — decisive two-sided nuisance falsification

The next audit identified a more fundamental issue: K2 is an interior known-sector nuisance and can move both signs around the reference point. The positive-oriented Exp071I/J/K comparison is therefore insufficient for a claim about the entire K2 nuisance line.

Exp071L prospectively froze and freshly evaluated the opposite physical K2 displacement:

- reference: `omega_b=0.0224`, `omega_cdm=0.1200`;
- negative K2: `omega_b=0.0220`, `omega_cdm=0.1204`.

Fresh official CLASS reference reproduction was exact:

- max relative P difference: `0.0`;
- max relative `t_tot` difference: `0.0`;
- frozen integrity threshold: `1e-10`.

Velocity-shape primary angles:

- K2(+) vs GDM cs2: `166.4386944060 deg`;
- K2(+) vs GDM cv2: `164.9270967302 deg`;
- K2(-) vs GDM cs2: **`13.5502602743 deg`**;
- K2(-) vs GDM cv2: **`15.0708844313 deg`**.

Classification:

`K2_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071L`.

The positive and negative K2 shapes are almost antiparallel:

`179.9078020829 deg`,

with antisymmetry error only

`0.0029922493`.

This is a genuine scientific falsification of the stronger claim “velocity shape generically removes the K2 known-sector nuisance.”

### New paper-ready boundary

The correct Article-2 result is now more precise:

> The positive-oriented K2 displacement is strongly separated from the tested positive GDM directions in temporal and velocity-shape response space and that oriented result is broad across the frozen support. However an interior K2 nuisance is physically two-sided; a fresh negative K2 displacement lies only about 13.6-15.1 degrees from the positive GDM velocity-shape directions. Therefore specificity must be defined relative to oriented rays versus two-sided nuisance lines/subspaces.

This distinction is scientifically stronger and publication-safer than the previous wording because it explicitly identifies where response-channel separation survives and where nuisance-sign freedom destroys it.

A dedicated claim-boundary note is stored at:

`docs/ARTICLE2_EXP071I_J_K_L_ORIENTATION_BOUNDARY_2026-08-28.md`.

Until the consolidated Article-2 claim matrix is rewritten, that note supersedes any generic interpretation of the Exp071I positive-direction claim.

## Article 3 — unchanged at 44%

Exp073R1 full metacal reconstruction remains active; only source/index Stage A is terminal PASS. Active compute time receives no readiness credit.

Therefore:

- G7 OPEN
- G8 OPEN
- G9 OPEN
- covariance/whitening NOT AUTHORIZED
- nuisance quotient NOT AUTHORIZED

The Exp071L result also sharpens the future Article-3 nuisance requirement: an observational nuisance quotient must project the **full signed nuisance span/subspace**, not a selected positive tangent orientation.

## Next Article-2 task

The next repository task is editorial/scientific consolidation rather than another near-duplicate K2 angle test:

1. revise the Article-2 claim matrix so Exp071I/J/K are explicitly labeled **oriented positive-K2** results;
2. promote Exp071L as the falsification that distinguishes rays from nuisance lines;
3. update the core narrative and figure plan around the hierarchy

`static degeneracy -> oriented temporal/velocity separation -> support robustness -> two-sided nuisance overlap -> ray/line/subspace geometry`;

4. only then decide whether a genuinely different known-sector nuisance family is needed for one final external specificity control.

## Current required percentages

**Article 2 repository readiness for writing: 93%.**

**Article 3 repository readiness for writing: 44%.**
