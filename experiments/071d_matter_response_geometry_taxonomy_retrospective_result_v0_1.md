# Exp071D — matter-response geometry taxonomy retrospective result v0.1

**Date:** 2026-08-27  
**Status:** `DESCRIPTIVE_POST_UNBLINDING_ONLY`

## Provenance

This is not a preregistered discovery experiment. Every family/control used here had already been unblinded before the taxonomy metric was assembled.

The workflow reconstructs the result from immutable artifacts only:

- C3 GDM — run `32904158849`, artifact `9584180621`;
- C5 designer-f(R) — run `32907619613`, artifact `9585579947`;
- C7 IDM–DR — run `32920776596`, artifact `9589768992`;
- C8 IDM–photon — run `32926084015`, artifact `9591561317`;
- C9 IDM–baryon — run `32957427686`, artifact `9602537353`;
- K1/K2 known-sector control — run `33020203400`, artifact `9626238304`.

Reproduction run:

- run `33024722072`;
- artifact `9627946054`;
- digest `sha256:2805a5312cbbabbd408861e340426e5b7d02db5c5499cbbd3ae9d6b52b30b9f7`.

Key metrics are mirrored in
`data/derived/retrospective/exp071d_matter_response_geometry_taxonomy_key_metrics_v0_1.json`.

## Question

Does a nearly one-dimensional normalized matter-response trajectory imply a monotone/invertible microscopic-parameter coordinate, and can monotonicity rescue the dark specificity that Exp071C rejected for F30?

Because all families are already seen, this question is answered descriptively only. No threshold is promoted to G7/G8.

## Results

| family/control | PC1 fraction | path excess | endpoint progress monotone? | max adjacent tangent turn |
|---|---:|---:|---:|---:|
| C3 GDM | 99.8262% | 0.388% | yes | 7.80 deg |
| C5 f(R) | 99.7356% | 0.586% | yes | 6.72 deg |
| C7 IDM–DR | 99.5215% | 0.994% | yes | 9.95 deg |
| C8 IDM–photon | 90.7321% | 72.749% | **no** | **163.00 deg** |
| C9 IDM–baryon | 91.3942% | 23.672% | yes | 67.10 deg |
| K1 primordial tilt | 76.3637% | 90.304% | yes | 110.74 deg |
| K2 baryon fraction | **99.9044%** | 30.818% | **no** | **169.69 deg** |

The critical K2 endpoint-progress sequence is

`[0, 0.37237, 0.76865, 1.15138, 1.00000]`.

Thus K2 is almost perfectly one-dimensional by PC1 variance yet overshoots the endpoint and returns along nearly the same one-dimensional direction.

For dark C8 IDM–photon the endpoint-progress sequence is

`[0, 0.83152, 1.02908, 0.86787, 1.00000]`,

so this already-seen dark interaction family also backtracks strongly.

## Hard conceptual consequence

A low-dimensional response representation and an injective microscopic inverse are different properties.

A family can satisfy

`PC1 -> 1`

while its motion along that dominant axis reverses sign. Therefore one cannot infer

`response coordinate -> unique microscopic parameter`

from PCA/SVD dimensionality alone.

## Negative result: monotonicity does not rescue dark specificity

After Exp071C, one tempting post-hoc rescue would be to supplement the F30 normalized-path criterion with monotone endpoint progress so the ordinary K2 control fails.

Exp071D shows why that is scientifically invalid: C8 IDM–photon also violates that monotonicity property. Adding it now would split already-known dark interaction families as well as the known-sector control.

Therefore the data do **not** support a universal rule

`dark sector <=> low-dimensional monotone matter-response path`.

No such gate is introduced.

## Relation to the DSIR core concept

The result strengthens the channel-conditional interpretation:

- matter-only geometry is useful as a taxonomy of transfer/shape mechanisms;
- geometry can compress a family without making the inverse one-to-one;
- the same matter-space geometric behavior can arise from ordinary and dark mechanisms;
- stronger specificity must come from independent channels, especially slip/Weyl/lensing, under the same observational metric.

This is consistent with the formal operator picture

`A_B = Q_B W_B K_B`,

where equivalence is defined only after a particular channel/covariance/nuisance construction.

## Publication relevance

Exp071D is suitable as a **negative-control/result panel** in DSIR-1 because it prevents two overclaims:

1. `low representation dimension = one physical degree of freedom`;
2. `matter-trajectory regularity = dark-sector signature`.

It is not itself evidence for new physics.

## Gate state

- G7: `OPEN`;
- G8: `OPEN`;
- G9: `OPEN`.
