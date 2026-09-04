# DSIR-2 figure visual audit — v0.1

**Date:** 2026-08-28  
**Input:** `DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json` and `make_dsir2_figures_v0_1.py`  
**Scientific numbers changed by this audit:** none.

## Execution result

The plotting logic was executed against the frozen numeric manifest and all four figures rendered successfully in a local publication check.

## Figure 1

**Status:** scientifically correct, publication revision recommended.

The v0.1 implementation joins categorical response constructions with continuous line segments. Because `matter`, `Weyl+slip`, temporal response, raw velocity response, projected velocity response, and nuisance-line geometry are distinct comparison constructions rather than samples along one continuously varying physical coordinate, connecting them can visually imply a trajectory that is not claimed by DSIR-2.

**Required v0.2 change:** use grouped point markers (or unconnected paired markers) for `cs2/cv2`, retain the frozen 45-degree line, and visually separate the static, oriented-ray, and line-geometry blocks. Preserve all numeric values.

## Figure 2

**Status:** scientifically correct, publication revision recommended.

The v0.1 top annotation is too dense and competes with the legend/45-degree line. The scientific point is simpler: Exp071M is an exact zero-response representation kernel, while Exp071N restores resolvability and yields K1 nuisance-line angles `36.06/37.85 deg`.

**Required v0.2 change:** reduce the annotation to a compact kernel callout, place the Exp071N response definition in a subtitle/footnote region, and label the two bars numerically. Preserve the explicit `INVALID_FOR_SCIENCE` distinction.

## Figure 3

**Status:** acceptable.

The support/admissibility ladder is readable and correctly distinguishes provider completion from finite-observation admissibility. Keep the bottom disclaimer that these are support/operator gates, not covariance-whitened likelihood results.

Minor v0.2 improvement: use boxed stages to emphasize that BOSS and KiDS are alternative finite-operator outcomes rather than a single monotonic sequence.

## Figure 4

**Status:** acceptable, minor revision recommended.

The Article-2/downstream boundary is visually clear. Improve the boundary label and use boxes or aligned stage labels so the hierarchy reads as a methodological flow rather than plain text.

## Scientific integrity checks

- no angle changed;
- no threshold changed;
- no Exp071 classification changed;
- Exp071H remains an oriented-ray result;
- Exp071M remains `INVALID_FOR_SCIENCE` with undefined angles;
- Exp071N remains a two-sided K1 overlap result;
- Figure 3 remains an admissibility/support figure, not an observational likelihood result;
- Figure 4 keeps covariance whitening and nuisance quotient downstream of Article 2.

## Verdict

`FIGURE_GENERATOR_V0_1_EXECUTES__PUBLICATION_LAYOUT_REVISION_REQUIRED_V0_1`
