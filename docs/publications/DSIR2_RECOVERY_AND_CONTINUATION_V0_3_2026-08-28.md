# DSIR-2 recovery and continuation — v0.3

**Frozen:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Purpose:** allow a fresh chat/research session to reconstruct Article 2 without relying on prior conversation context.

## 1. Read these files first

1. `docs/publications/DSIR2_MANUSCRIPT_V0_3.md` — active integrated manuscript.
2. `docs/ARTICLE2_CLAIM_MATRIX_V0_3.md` — active claim boundary and status semantics.
3. `docs/publications/DSIR2_TABLE_T2_ANGLE_HIERARCHY_V0_1.md` — exact oriented vs line-angle table.
4. `docs/publications/DSIR2_METHODS_RESULTS_EXP071H_L_DRAFT_V0_1.md` — exact publication prose/provenance for the dynamic chain.
5. `docs/publications/DSIR2_DISCUSSION_DRAFT_V0_1.md` — publication-ready discussion source.
6. `docs/publications/DSIR2_FIGURE_SOURCE_MANIFEST_V0_1.md` — exact figure/data/provenance map.
7. `docs/publications/DSIR2_LITERATURE_SCAFFOLD_V0_1.md` — bibliography and novelty boundary.
8. `docs/ARTICLE2_TOTAL_VELOCITY_PROVIDER_CONTRACT_2026-08-28.md` — semantic contract for CLASS `t_tot`.
9. `docs/CHANNEL_CONDITIONAL_EQUIVALENCE_QUOTIENT_THEOREMS_2026-08-27.md` — formal channel-equivalence background.
10. `docs/publications/ARTICLE_SERIES_ROADMAP_V0_1.md` — boundary with DSIR-1/3/4.

Historical v0.1/v0.2 manuscript, claim-matrix and recovery files must remain available. They record real scientific narrowing and later geometric refinement rather than cosmetic revisions.

## 2. Current paper title

> **Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces**

## 3. Central result in one paragraph

K2 fixed-total-matter baryon/CDM redistribution falsifies a dark-specific interpretation of matter-only F30. Static Weyl/slip and matter+Weyl+slip channels add information but retain a GDM sound-speed-like K2 ambiguity. The preregistered **positive** K2 response is strongly separated from both tested positive GDM directions in finite-bin temporal and same-definition CLASS total-velocity transfer; positive velocity separation also survives amplitude projection and leave-one-k/z robustness. But a one-dimensional nuisance line is sign-invariant, with principal angle `acos(|u dot v|)`. Retrospectively, the positive projected-velocity K2 vector spans a line only `13.5613/15.0729 deg` from the GDM axes. Exp071L then validates this prospectively with a fresh negative K2 response: K2-/K2+ are `179.9078 deg` apart and K2- lies `13.5503/15.0709 deg` from the GDM axes. Thus robust positive-oriented separation is real but is not a sign-invariant mechanism discriminator.

## 4. New v0.3 geometric insight

For a normalized one-dimensional known-sector response direction `u` and comparator `v`, distinguish

`alpha_ori = acos(u dot v)`

from the nuisance-line principal angle

`alpha_line = acos(|u dot v|) = min(alpha_ori,180-alpha_ori)`.

This is **not** a retroactive change to preregistered classifications. It is a descriptive transformation when the physical nuisance object is the line `span(u)`.

Critical retrospective values:

- Exp071H temporal K2+ `138.1006/137.0973 deg` oriented -> `41.8994/42.9027 deg` line angles.
- Exp071I raw `t_tot` `165.9455/164.7113 deg` oriented -> `14.0545/15.2887 deg` line angles.
- Exp071J velocity shape `166.4387/164.9271 deg` oriented -> `13.5613/15.0729 deg` line angles.

Exp071L fresh K2- yields `13.5503/15.0709 deg`, agreeing with the Exp071J line prediction to only `0.0110/0.0020 deg`. This is an empirical validation of the one-dimensional line interpretation in velocity space, not a theorem that every finite negative parameter step is exactly antiparallel.

## 5. Scientific logic — preserve this order

1. DSIR-1 background: response equivalence is channel conditional.
2. Exp071C: K2 known-sector control passes F30 -> matter-only dark specificity FAIL.
3. GDM Weyl/slip regression: independent metric information exists.
4. Exp071D: scalar metric specificity FAIL.
5. Exp071E: static Weyl+slip retains K2~cs2 overlap.
6. Exp071F: adding matter power still retains K2~cs2 overlap.
7. Exp071H: K2+ finite-bin temporal response is an oriented PASS.
8. Retrospective line diagnostic: Exp071H line angle is below 45 deg; do not retroactively reclassify.
9. Exp071I: K2+ same-definition `t_tot` is an oriented PASS.
10. Exp071J: positive velocity separation survives constant-in-k amplitude removal.
11. Exp071K: positive velocity-shape separation is broad under leave-one-k/z deletion.
12. Line geometry already predicts small sign-invariant velocity angles.
13. Exp071L: fresh K2- validates the line geometry and gives prospective two-sided velocity FAIL.
14. Exp072/073: provider/theory support != observational admissibility.

Do not rewrite this into a success-only story. The change of conclusion under the stronger nuisance definition is the scientific result.

## 6. Exact core numbers

### Static

- Exp071E K2+ vs `cs2/cv2`: `18.9256666 / 58.9126736 deg`.
- Exp071F matter-only: `19.2230815 / 19.0371029 deg`.
- Exp071F equalized matter+Weyl+slip: `19.0748772 / 50.1667350 deg`.

### Temporal — Exp071H

- oriented K2+ vs `cs2/cv2`: `138.1005853 / 137.0972593 deg`.
- retrospective line angles: `41.8994147 / 42.9027407 deg`.
- frozen classification threshold: `45 deg`.
- dedicated fresh K2- temporal finite-displacement test still pending.

### Raw total velocity — Exp071I

- oriented K2+ vs `cs2/cv2`: `165.9454940 / 164.7113289 deg`.
- retrospective line angles: `14.0545060 / 15.2886711 deg`.
- GDM mutual angle: `2.3682515 deg`.
- parent `P(k)` reproduction max relative difference: `0.0` against `1e-10`.

### Velocity shape — Exp071J/K/L

- Exp071J oriented K2+ vs `cs2/cv2`: `166.4386944 / 164.9270967 deg`.
- Exp071J line angles: `13.5613056 / 15.0729033 deg`.
- retained projected norms: about `83%`.
- Exp071K global minimum across 24 primary leave-one-k/z angles: `157.8212319 deg`.
- Exp071L K2- vs `cs2/cv2`: `13.5502603 / 15.0708844 deg`.
- K2-/K2+ mutual angle: `179.9078021 deg`.
- nonlinear antisymmetry error: `0.00299225`.
- line-prediction vs fresh-K2- differences: `0.0110453 / 0.0020188 deg`.
- fresh-reference `P` and `t_tot` max relative differences: `0.0` against `1e-10`.

## 7. Exact derived evidence files

- `data/derived/exp071e_known_sector_joint_metric_direction_summary_v0_1.json`
- `data/derived/exp071f_known_sector_matter_weyl_slip_direction_summary_v0_1.json`
- `data/derived/exp071h_k2_finite_bin_growth_dual_provenance_summary_v0_1.json`
- `data/derived/exp071i_k2_gdm_total_velocity_direction_summary_v0_1.json`
- `data/derived/exp071j_total_velocity_shape_projection_summary_v0_1.json`
- `data/derived/exp071k_velocity_shape_support_localization_summary_v0_1.json`
- `data/derived/exp071l_two_sided_k2_velocity_shape_nuisance_summary_v0_1.json`

For Exp071C/D use provenance recorded in `ARTICLE2_CLAIM_MATRIX_V0_3.md` and immutable artifacts if panel-level values are needed.

## 8. Interpretation rules

### Allowed

- response specificity is channel/operator/comparison-object conditioned;
- oriented response and nuisance-line tests can give different answers;
- positive K2 temporal/velocity responses are strongly separated under their preregistered oriented tests;
- positive velocity separation is robust to stated amplitude/support controls;
- the line-principal diagnostic for H/I/J is retrospective and descriptive;
- Exp071L prospectively validates the nuisance-line picture for velocity;
- theory/provider separation is not observational distinguishability.

### Forbidden

- dark-sector detection;
- unique fingerprint;
- “velocity solves the degeneracy”;
- “temporal evolution sign-invariantly separates K2”;
- retroactively relabelling Exp071H as a preregistered FAIL because its line angle is <45 deg;
- assuming finite K2- temporal response without computation;
- tracer RSD or `f sigma8` language for `t_tot`;
- survey detectability from response angles;
- G7/G8/G9 promotion.

## 9. Highest-value next scientific control

**Fresh negative-K2 temporal analogue of Exp071H.**

Freeze the exact Exp071H finite-bin temporal operator, normalization, parent convention and 45-degree rule. Generate a fresh K2- displacement at fixed total `omega_m` and compare it with the same positive GDM `cs2/cv2` temporal axes.

Purpose is now sharper than in v0.2: the retrospective line diagnostic already predicts that a one-dimensional K2 line would lie at `41.90/42.90 deg`; the new experiment tests whether the finite K2- response actually realizes the near-antiparallel line approximation or displays meaningful curvature.

## 10. Highest-value manuscript work

1. Generate F4: oriented-angle vs line-principal-angle schematic.
2. Generate central F5 from Exp071J/L immutable data.
3. Generate F7 temporal oriented-vs-line warning panel.
4. Build T3 provenance ledger.
5. Run a deeper prior-art audit specifically for principal angles, nuisance tangent spaces and quotient geometry in cosmology.
6. Perform sentence-by-sentence claim-to-evidence audit before submission language.

## 11. Literature boundary

Use `DSIR2_LITERATURE_SCAFFOLD_V0_1.md` as the starting point. Current safe references include Hu (1998), Kopp/Skordis/Thomas (2016), Thomas/Kopp/Skordis (2016), Kunz/Nesseris/Sawicki (2016), CLASS overview, and a 2026 Euclid-like GDM forecast for downstream observational context.

Do **not** claim priority for `oriented tangent vs nuisance-subspace specificity` until the targeted prior-art search is complete.

## 12. Article boundaries

DSIR-1 owns the broad response atlas/localization/curvature/characteristic-scale geometry. DSIR-2 focuses on specificity falsification.

DSIR-3 owns covariance whitening, nuisance tangent SVD, quotient-space reconstruction and G7 observational relation/null testing.

## 13. Gate state

`G7=OPEN`  
`G8=OPEN`  
`G9=OPEN`