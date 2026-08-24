# Experiment 040 — finite-bin structure-growth response v0.1

**Date:** 2026-08-25  
**Status:** **HARD PASS — `PASS_FINITE_BIN_GROWTH_RESPONSE_V0_1`**  
**Scope:** theory-response temporal operator on the frozen low-k atlas

## Motivation

The frozen comparisons have repeatedly shown that scale shape alone can erase mechanism information. In particular, GDM and designer f(R) have leading scale modes separated by only about `0.08-0.10 deg`, while their time modes differ by about `25 deg`. Experiment 036 independently showed that IDE alpha/beta directions become nearly degenerate in AP geometry (`9.04 deg` acute) despite a much larger structure separation.

Before constructing a tracer-specific RSD/ShapeFit growth operator, DSIR therefore isolates the part of the frozen structure response carried by **time evolution itself**.

This is a theory-space operator, not an observational growth measurement.

## Definition

For the production structure response

\[
r_\Delta(k,z)=\ln\frac{P_{\Delta,model}(k,z)}{P_{\Delta,ref}(k,z)},
\]

and two frozen nodes with `z_early > z_late`, define

\[
\boxed{
\Delta\bar f_P(k;early\to late)
=\frac{r_\Delta(k,z_{late})-r_\Delta(k,z_{early})}
{2\,[\ln a_{late}-\ln a_{early}]}
}.
\]

Because `ln P = 2 ln D + const` for a scale-independent growing mode, this equals the interval-average change in logarithmic power-growth rate relative to the reference in that limit. More generally it remains a well-defined finite temporal derivative of the power response even when growth is scale dependent.

The frozen seven-node grid gives six adjacent time intervals and five k nodes, hence a 30-component temporal response per direction.

## Why finite bins instead of a numerical derivative

A preliminary derivative diagnostic suggested that temporal evolution can materially alter cross-family geometry. Experiment 040 replaces that interpolation-dependent derivative with an exact finite-bin operator on the already frozen response nodes. No new solver interpolation or smoothing scale enters.

## Hard controls frozen before pairwise interpretation

The hard gate tests only algebraic/operator properties, not scientifically interesting angles:

1. endpoint reconstruction tolerance `<=1e-12`;
2. constant-in-redshift response annihilation `<=1e-14`;
3. linearity residual `<=1e-12`;
4. every admitted frozen direction finite and nonzero.

**No pairwise angular threshold is defined.** Pairwise angles are descriptive outputs computed only after the operator controls were frozen.

Successful hard run `32785987735` produced:

- endpoint reconstruction max absolute error `1.1102230246251565e-16`;
- constant-mode residual `0`;
- linearity residual `9.769962616701378e-15`;
- failures `[]`.

Hard result artifact:

- artifact ID `9541462864`;
- SHA256 `0457823510fead4ff56e8e29843e39de47805f8fbfda86f4d9d33585be556ac9`;
- frozen summary `data/derived/comparison_readiness/experiment_040_finite_bin_growth_response_v0_1.json`.

## Hard comparison findings

### IDE alpha/beta: temporal structure partially restores information lost by AP

For the C2 physical directions:

- corrected-DESI AP acute angle from Experiment 036: `9.0379006 deg`;
- Experiment 040 finite-bin growth acute angle: `29.3978236 deg`;
- full frozen structure acute angle: `58.9337977 deg`.

Thus the temporal structure block restores a substantial fraction of the mechanism separation erased by AP, but not all of the full `(k,z)` structure information.

### Smooth-w versus IDE alpha: a new channel-dependent reversal

Smooth-w versus the physical IDE negative-alpha ray gives:

- AP acute angle: `72.8034931 deg`;
- full frozen structure acute angle: `52.1942934 deg`;
- finite-bin growth acute angle: only `10.3105847 deg`.

Therefore the same two directions that are well separated by geometry become nearly degenerate after the finite-bin temporal-growth operator. This is an especially clean example that degeneracy belongs to `(physical direction, observation/response operator)`, not to a model pair alone.

Smooth-w versus IDE beta shows the same tendency more moderately: raw structure `80.5208665 deg`, finite-bin growth `26.8292000 deg`; AP from Experiment 036 was `64.1510936 deg`.

### GDM pressure versus viscosity: time evolution helps only weakly

GDM `cs2/cv2` changes from raw low-k structure angle `0.3226164 deg` to finite-bin growth `1.3340128 deg`. Time evolution increases the angle by roughly a factor four but leaves the two directions strongly collinear. It therefore does **not** replace metric slip as the established separator.

### GDM versus designer f(R): temporal information separates scale-shape lookalikes

The previously established leading **scale-only** modes differ by only about `0.078-0.102 deg`. Experiment 040 finite-bin growth gives:

- GDM `cs2` versus f(R): `16.0522115 deg` acute (`163.9477885 deg` oriented);
- GDM `cv2` versus f(R): `17.2842773 deg` acute (`162.7157227 deg` oriented).

The full raw `(k,z)` structure angles are still larger, about `25.18-25.49 deg` acute. Therefore finite-bin growth isolates a real temporal separator relative to scale-only compression, while confirming that retaining the complete structure history is more informative than growth-only compression.

### IDE alpha versus GDM: temporal operator increases separation

IDE negative-alpha versus GDM changes from about `24.8-24.9 deg` acute in full raw structure direction geometry to about `60.9 deg` in finite-bin growth. This identifies another pair for which time evolution is a particularly informative coordinate.

## Input

Use exactly

`data/derived/comparison_readiness/local_response_tangents_v0_1.json`.

This keeps the same source directions and solver provenance used by the first block-aware family comparison. The C5 vector is the minimum resolved `B0=1e-6` production ray, not falsely relabeled as a `B0->0` derivative; angular comparisons are invariant under positive rescaling, but amplitude comparisons across heterogeneous parameter units remain forbidden.

## Relation to Experiment 039

Experiment 039 defines the stricter ShapeFit/RSD representability contract, including the sound-horizon-rescaled `sigma_s8` convention and a density/velocity representability defect. Experiment 040 does **not** bypass that requirement.

Instead it establishes which temporal features are valuable enough to preserve when constructing the more expensive tracer/window-aware RSD layer.

## Claim boundary

Experiment 040 is not:

- a prediction of `f sigma_s8`;
- a tracer-velocity calculation;
- a DESI likelihood or covariance whitening;
- a parameter significance;
- an intrinsic-rank determination;
- a residual law or discovery.

A large temporal angle can motivate an observational growth operator, but cannot by itself establish survey distinguishability.
