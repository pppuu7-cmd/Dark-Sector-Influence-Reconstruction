# DSIR Article 2 — claim matrix v0.2 orientation consolidation

**Consolidated:** 2026-08-28

## Status and precedence

This document is the authoritative consolidation for the Exp071H-L part of Article 2 and **supersedes the interpretation of A2-C14 in `ARTICLE2_CLAIM_MATRIX_V0_1.md` wherever v0.1 can be read as generic separation from the entire K2 nuisance direction**.

All earlier provider, physical-support and finite-operator claims A2-C1 through A2-C13 remain unchanged unless explicitly modified below.

The central correction is geometric:

- positive one-sided model deformations may be compared as **oriented rays**;
- an ordinary interior nuisance with both signs allowed is a **line**;
- several nuisances form a **subspace**.

## Revised / new claims

| ID | Status | Paper-ready claim | Evidence | Forbidden stronger claim |
|---|---|---|---|---|
| A2-C14R | ✅ oriented-ray result | In a source-audited same-definition CLASS `t_tot` channel, the **positive K2 response ray** is nearly opposite both tested positive GDM rays: `165.9455° / 164.7113°`. Fresh I/O-extended runs reproduce immutable matter-power parents exactly before scoring. | Exp071I run `33181895623`, artifact `9690064470`; source contract and terminal summary. | “The full two-sided K2 nuisance is separated from GDM.” |
| A2-C15 | ✅ oriented-ray robustness | Removing the entire scale-independent constant-in-k velocity mode independently at every redshift does not remove the positive-ray separation: `166.4387° / 164.9271°`, with roughly 83% of each response norm retained. | Exp071J run `33182705074`, artifact `9690361647`. | “Amplitude quotient establishes nuisance-line specificity.” |
| A2-C16 | ✅ support robustness | The positive-oriented K2 velocity-shape result is not carried by one frozen k node or one redshift slice. All 24 preregistered leave-one-k / leave-one-z angles exceed 45°; the global minimum is `157.8212°`. | Exp071K prereg `3910605e...`; run `33183729426`; artifact `9690784568`; summary `data/derived/exp071k_velocity_shape_support_localization_summary_v0_1.json`. | “Broad support implies robustness to sign reversal or to an arbitrary nuisance subspace.” |
| A2-C17 | ✅ falsification | The positive-ray result **does not establish separation from a two-sided K2 nuisance line**. A fresh physically allowed negative K2 displacement gives only `13.5503° / 15.0709°` to the positive GDM velocity-shape directions, far below the frozen 45° separator. | Exp071L prereg `9927f46c...`; run `33184079909`; artifact `9690954372`; exact fresh-reference P and `t_tot` reproduction. | “Velocity shape generically removes the K2 known-sector nuisance.” |
| A2-C18 | ✅ methodological synthesis | DSIR specificity is conditioned not only on channel but on the geometric class of the comparison object: **ray, line, or nuisance subspace**. For a two-sided scalar nuisance the correct line angle is `arccos(|u·v|/(||u||||v||)) = min(theta,180°-theta)`. For multiple nuisances the target must be projected against the full signed nuisance span. | `docs/DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md`; Exp071J/L agreement of ideal line-angle prediction with fresh negative displacement. | “An oriented tangent angle is universally the correct specificity measure.” |

## Quantitative closure of the orientation issue

For Exp071J positive K2 velocity shape:

- oriented ray angle to GDM `cs2+`: `166.4386944060°`;
- oriented ray angle to GDM `cv2+`: `164.9270967302°`.

If K2 is treated correctly as a two-sided nuisance line, the same vectors imply

- line angle to `cs2+`: `13.5613055940°`;
- line angle to `cv2+`: `15.0729032698°`.

Exp071L independently realizes the opposite physical K2 displacement and measures

- `13.5502602743°` to `cs2+`;
- `15.0708844313°` to `cv2+`.

Difference between line-angle prediction and fresh negative-displacement measurement:

- `0.0110453197°` for `cs2`;
- `0.0020188384°` for `cv2`.

The K2 positive and negative shapes are mutually separated by `179.9078020829°`, with finite-step antisymmetry error `0.0029922493`.

This validates the line interpretation rather than merely asserting it algebraically.

## Revised Article-2 core narrative

The strongest defensible scientific narrative is now:

1. static matter morphology is informative but fails generic known-sector specificity;
2. adding correlated static metric/slip coordinates does not automatically remove the K2↔GDM sound-speed-like ambiguity;
3. temporal and total-velocity channels reveal a large **oriented** difference between the tested positive K2 and positive GDM deformations;
4. that positive-ray difference survives amplitude-mode removal and all frozen single-support ablations;
5. however K2 is an interior two-sided nuisance, and its negative physical displacement lies close to the positive GDM velocity-shape rays;
6. therefore apparent “separation” or “equivalence” must specify both the **observable channel** and whether the physical comparison object is a **ray, line, or subspace**;
7. observational specificity can only be assessed after projecting the target response against the full signed nuisance subspace in a valid observational metric.

Compact form:

`static degeneracy -> oriented temporal/velocity separation -> amplitude/support robustness -> two-sided nuisance falsification -> ray/line/subspace geometry -> observational nuisance-subspace test`.

## Revised abstract/discussion language

Safe text:

> Matter-response geometry is informative but not generically mechanism-specific under known-sector controls. Temporal and source-audited total-velocity responses can sharply distinguish selected **oriented** model deformations that remain close in static response space, and the positive K2 velocity-shape separation is robust to amplitude-mode removal and single-support ablations. However a prospective sign-reversal test shows that the physically two-sided K2 nuisance line approaches the tested positive GDM velocity-shape rays to about 13.6-15.1 degrees. Response specificity is therefore conditioned jointly on observable channel and geometric parameter class: oriented rays, two-sided nuisance lines, and higher-dimensional nuisance subspaces are not interchangeable comparison objects.

Do not use:

- “velocity removes the K2 nuisance”;
- “unique fingerprint”;
- “dark-sector detection”;
- “RSD detection”;
- “observational distinguishability”;
- “G7 closed”.

## Figure / table consolidation

The Article-2 figure plan should now include:

- static matter / three-channel ambiguity (~19°);
- temporal positive-ray separation (~137-138°);
- total-velocity / velocity-shape positive-ray separation (~165-166°);
- Exp071K support-ablation envelope, global minimum `157.82°`;
- a **ray-versus-line panel** showing `166.44°` oriented angle but `13.56°` K2-line angle;
- fresh Exp071L negative K2 confirmation at `13.55° / 15.07°`;
- schematic extension from line to multi-dimensional nuisance subspace.

A compact paper table should distinguish columns:

`channel | comparison object | orientation/sign freedom | angle/statistic | interpretation`.

## Bridge to Article 3

Article 3 must not build a nuisance quotient from selected positive nuisance tangents. Once the physical-support and covariance gates are valid, the nuisance basis must span every preregistered signed local nuisance direction, and the response surviving the nuisance span should be measured with the metric-aware projector defined in

`docs/DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md`.

G7/G8/G9 remain OPEN.
