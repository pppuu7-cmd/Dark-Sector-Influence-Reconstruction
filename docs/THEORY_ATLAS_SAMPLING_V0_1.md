# DSIR theory-atlas sampling v0.1

Date: 2026-08-24
Status: pilot sampling contract

## Why one representative per family is insufficient

DSIR treats a named theory family as a response manifold, not a label. A single wCDM point, one WDM mass, or one f(R) B0 can test plumbing but cannot define the intrinsic model-manifold rank. The atlas must sample each family explicitly and report the prior sensitivity of the inferred dimension.

## Prior decomposition

Let family f contain n_f model instances. A theory prior is decomposed into

\[
\pi(i)=\pi(f)\,\pi(i|f).
\]

The pilot default assigns equal *total* mass to each family,

\[
\pi(f)=1/N_{fam},
\]

not equal mass to every catalog row. Within-family sampling remains explicit and is never presented as uniquely objective.

`family_balanced_weights()` implements the equal-family layer while allowing an explicit positive `within_family_weights` vector. The identical row weights must be used in the null calibration for `R_model(pi)`.

## Pilot six-family axes

These are sampling directions, not observational priors and not final parameter bounds.

1. **C0 GR/LambdaCDM:** one intersection/baseline instance per solver lineage; baseline rows are not duplicated merely because many solvers can reproduce LambdaCDM.
2. **C1 smooth DE:** sample constant w with cs2=1. The LambdaCDM intersection w=-1 is retained as a boundary/control point; nontrivial samples should include several w>-1 values for the minimally coupled/quintessence-like branch. Phantom points, if used later, are a separate labeled subfamily rather than silently mixed.
3. **C2 interacting vacuum:** sample the pinned class_iv interaction coordinates alpha,beta only inside domains that pass stability and solver checks. The alpha=beta=0 intersection is mandatory. Do not assign an observational prior before a specific momentum-transfer prescription and viability audit are frozen.
4. **C3 GDM:** sample w, cs2 and cvis2 as distinct axes using the pinned GDM_CLASS closure. The exact zero closure is mandatory. A one-dimensional path is not allowed to stand in for the full three-function closure space.
5. **C4 thermal WDM:** sample thermal-relic mass/cutoff scale using the validated transfer convention. A practical pilot may contain multiple masses (for example 2, 3 and 5 keV), but these are response controls rather than claims that all points remain observationally viable.
6. **C5 designer f(R):** sample log B0 once MG-S0 passes. The initial clean-room calibration already spans 1e-2 to 1e-8; production manifold points must lie in a numerically stable, explicitly documented range and use full H-EFTCAMB responses on all frozen k nodes.

## Intersections and duplicate rows

Exact intersections such as w=-1, alpha=beta=0, zero GDM closure, B0->0, and the cold-WDM limit are scientifically important degeneracy anchors. However, numerically identical LambdaCDM rows from several family parametrizations must not be allowed to overweight the intersection. Store their equivalence-map metadata, but control their prior mass explicitly.

## Validity/missingness

Every instance follows `schemas/model_instance_v0_2.yaml` and the masked-response gate. Undefined theory/channel cells are NaN with an explicit validity mask. Ordinary global SVD uses only an exact common valid feature block. Pair/local blocks may be used for discriminant analysis but are not concatenated into a global rank without a separately validated masked-factor method.

## Required rank report

A production atlas must report at least:

- catalog-multiplicity prior;
- equal-family prior;
- at least one defensible alternative within-family coordinate/weighting;
- stratified bootstrap over model instances/families;
- singular spectra and noise edges under the same weights;
- which conclusions about R_model(pi) survive all tested priors.

No single prior is labelled the unique theory prior.

## Next implementation step

After full designer-f(R) MG-S0/S1, generate a first pilot manifest for all six families on the frozen v0.1.1 response grid. Then construct the common masked block, covariance-whiten it, and measure R_model(pi) before any G7 law search.
