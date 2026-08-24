# Experiment 040 — finite-bin structure-growth response v0.1

**Date:** 2026-08-25  
**Status:** protocol frozen; hard run pending  
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

A preliminary derivative diagnostic suggested that GDM versus f(R) separation grows substantially when temporal evolution is retained. Experiment 040 deliberately replaces that interpolation-dependent derivative with an exact finite-bin operator on the already frozen response nodes. No new solver interpolation or smoothing scale enters.

## Hard controls frozen before pairwise interpretation

The hard gate tests only algebraic/operator properties, not scientifically interesting angles:

1. endpoint reconstruction:
   \[
   2\sum_i \Delta\bar f_{P,i}\,\Delta\ln a_i
   =r_\Delta(z_{lowest})-r_\Delta(z_{highest})
   \]
   for every k, with maximum absolute error `<=1e-12`;
2. a response constant in redshift is annihilated, maximum absolute output `<=1e-14`;
3. linearity `K(x+y)=Kx+Ky`, maximum absolute residual `<=1e-12`;
4. every admitted frozen direction produces finite nonzero output.

**No pairwise angular threshold is defined.** Pairwise angles are descriptive outputs computed only after the operator controls are frozen.

## Input

Use exactly

`data/derived/comparison_readiness/local_response_tangents_v0_1.json`.

This keeps the same source directions and solver provenance used by the first block-aware family comparison. The C5 vector is the minimum resolved `B0=1e-6` production ray, not falsely relabeled as a `B0->0` derivative; angular comparisons are invariant under positive rescaling, but amplitude comparisons across heterogeneous parameter units remain forbidden.

## Comparisons of highest interest

The hard run will report both raw-structure and finite-bin-growth angles for every available pair. In interpretation, prioritize:

- C3 GDM `cs2` versus `cv2`: does time evolution break their density-shape degeneracy?
- C3 GDM versus C5 designer f(R): does temporal evolution separate scale-shape lookalikes?
- C2 IDE negative-alpha versus beta: does temporal structure restore information lost in AP geometry?
- C1 smooth-w versus the scale-dependent families.

## Relation to Experiment 039

Experiment 039 defines the stricter ShapeFit/RSD representability contract, including the sound-horizon-rescaled `sigma_s8` convention and a density/velocity representability defect. Experiment 040 does **not** bypass that requirement.

Instead it answers a prior question: whether time evolution of the validated total-matter structure response contains useful discrimination worth carrying into the more expensive tracer/window-aware RSD layer.

## Claim boundary

Experiment 040 is not:

- a prediction of `f sigma_s8`;
- a tracer-velocity calculation;
- a DESI likelihood or covariance whitening;
- a parameter significance;
- an intrinsic-rank determination;
- a residual law or discovery.

A large temporal angle can motivate an observational growth operator, but cannot by itself establish survey distinguishability.
