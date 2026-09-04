# DSIR-2 recovery and continuation — v0.2

**Frozen:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Purpose:** allow a fresh chat/research session to reconstruct Article 2 without relying on prior conversation context.

## 1. Read these files first

1. `docs/publications/DSIR2_MANUSCRIPT_V0_2.md` — active working manuscript.
2. `docs/ARTICLE2_CLAIM_MATRIX_V0_2.md` — active claim boundary.
3. `docs/publications/DSIR2_FIGURE_SOURCE_MANIFEST_V0_1.md` — exact figure/data/provenance map.
4. `docs/ARTICLE2_TOTAL_VELOCITY_PROVIDER_CONTRACT_2026-08-28.md` — semantic contract for CLASS `t_tot`.
5. `docs/CHANNEL_CONDITIONAL_EQUIVALENCE_QUOTIENT_THEOREMS_2026-08-27.md` — formal channel-equivalence background.
6. `docs/publications/ARTICLE_01_EVIDENCE_MAP_V0_1.md` — boundary with DSIR-1.
7. `docs/publications/ARTICLE_SERIES_ROADMAP_V0_1.md` — boundary with DSIR-3/4.

Historical files that must remain available but are superseded for active drafting:

- `docs/publications/DSIR2_MANUSCRIPT_V0_1.md`
- `docs/publications/DSIR2_RECOVERY_AND_CONTINUATION_2026-08-28.md`
- `docs/ARTICLE2_CLAIM_MATRIX_V0_1.md`

Do not delete them: the transition from v0.1 to v0.2 records a real scientific narrowing after a stronger falsification control.

## 2. Current paper title

> **Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces**

The previous title, “From Static Degeneracy to Dynamic Separation…”, became too strong after Exp071L.

## 3. Central result in one paragraph

The paper tests whether apparent response-space discriminants survive known-sector and stronger nuisance controls. K2 fixed-total-matter baryon/CDM redistribution falsifies a dark-specific interpretation of matter-only F30. Static Weyl/slip and matter+Weyl+slip channels add information but retain a GDM sound-speed-like K2 ambiguity. The preregistered **positive** K2 tangent is strongly separated from both tested GDM tangents in finite-bin temporal response and same-definition CLASS total-velocity transfer; the positive velocity result also survives amplitude projection and leave-one-k/z robustness. But Exp071L generates a fresh **negative** K2 displacement and shows it is nearly antiparallel to K2+ and only 13.55/15.07 degrees from the GDM velocity-shape axes. Thus positive-oriented separation is real but is not a sign-invariant discriminator of the physically two-sided K2 nuisance line.

## 4. Scientific logic — preserve this order

1. DSIR-1 background: response equivalence is channel conditional.
2. Exp071C: K2 known-sector control passes F30 -> matter-only dark specificity FAIL.
3. GDM Weyl/slip regression: independent metric information exists.
4. Exp071D: scalar metric specificity FAIL.
5. Exp071E: static Weyl+slip retains K2~cs2 overlap.
6. Exp071F: adding matter power still retains K2~cs2 overlap.
7. Exp071H: K2+ finite-bin temporal tangent strongly separates from both GDM axes.
8. Exp071I: K2+ same-definition `t_tot` tangent independently strongly separates.
9. Exp071J: positive velocity separation survives constant-in-k amplitude removal.
10. Exp071K: positive velocity-shape separation is broad under leave-one-k/z support deletion.
11. Exp071L: two-sided K2 nuisance line overlaps GDM -> sign-invariant specificity FAIL.
12. Exp072/073: provider/theory support != observational admissibility.

Do not rearrange the story into a success-only ladder. The failures are the scientific result.

## 5. Critical numbers

### Static

- Exp071E K2+ vs `cs2/cv2`: `18.9257 / 58.9127 deg`.
- Exp071F matter-only: `19.2231 / 19.0371 deg`.
- Exp071F equalized matter+Weyl+slip: `19.0749 / 50.1667 deg`.

### Temporal — Exp071H

- K2+ vs `cs2(1e-7)`: `138.1005853262 deg`.
- K2+ vs `cv2(1e-7)`: `137.0972592611 deg`.
- classification threshold: `45 deg`.
- IMPORTANT: no dedicated K2- temporal test is currently part of the evidence chain.

### Raw total velocity — Exp071I

- K2+ vs `cs2/cv2`: about `165.9455 / 164.7113 deg`.
- GDM `cs2/cv2` mutual angle: about `2.3683 deg`.
- parent P(k) reproduction max relative difference: `0.0` against `1e-10`.
- `t_tot` is NOT tracer RSD or `f sigma_8`.

### Velocity shape projection — Exp071J

- K2+ vs `cs2`: `166.4386944060 deg`.
- K2+ vs `cv2`: `164.9270967302 deg`.
- retained raw norm fractions ~`0.83`.

### Velocity support robustness — Exp071K

- global minimum over 24 primary leave-one-k/z angles: `157.8212319078 deg`.
- all remain above `45 deg`.
- explicit source boundary: this tests only the oriented positive K2 direction.

### Two-sided falsification — Exp071L

- K2+ vs `cs2/cv2`: `166.4386944060 / 164.9270967302 deg`.
- K2- vs `cs2/cv2`: `13.5502602743 / 15.0708844313 deg`.
- K2- vs K2+ mutual angle: `179.9078020829 deg`.
- fresh-reference max relative P difference: `0.0`.
- fresh-reference max relative `t_tot` difference: `0.0`.
- integrity threshold: `1e-10`.
- classification: `K2_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071L`.

## 6. Exact derived files

- `data/derived/exp071e_known_sector_joint_metric_direction_summary_v0_1.json`
- `data/derived/exp071f_known_sector_matter_weyl_slip_direction_summary_v0_1.json`
- `data/derived/exp071h_k2_finite_bin_growth_dual_provenance_summary_v0_1.json`
- `data/derived/exp071i_k2_gdm_total_velocity_direction_summary_v0_1.json`
- `data/derived/exp071j_total_velocity_shape_projection_summary_v0_1.json`
- `data/derived/exp071k_velocity_shape_support_localization_summary_v0_1.json`
- `data/derived/exp071l_two_sided_k2_velocity_shape_nuisance_summary_v0_1.json`

For Exp071C/D use the run/artifact provenance in `ARTICLE2_CLAIM_MATRIX_V0_2.md` and recover immutable artifacts if final panel-level values are needed.

## 7. Interpretation rules

### Allowed

- response specificity is channel-conditioned;
- oriented tangent and nuisance-subspace tests can give different answers;
- positive K2 temporal/velocity directions are strongly separated in the stated operators;
- positive velocity separation is robust to stated amplitude/support controls;
- the two-sided K2 velocity nuisance line overlaps the tested GDM axes;
- theory/provider separation is not observational distinguishability.

### Forbidden

- dark-sector detection;
- unique fingerprint;
- “velocity solves the degeneracy” without the orientation caveat;
- “temporal response is sign-invariantly specific” before a negative-K2 temporal test;
- tracer RSD or `f sigma_8` language for `t_tot`;
- survey detectability from response angles;
- G7/G8/G9 promotion.

## 8. Highest-value next scientific control

**Two-sided temporal Exp071H analogue.**

Freeze the exact Exp071H finite-bin temporal operator, normalization, parent convention and 45-degree rule. Generate a fresh negative K2 displacement at fixed total `omega_m`, with reference-integrity checks, and compare K2- to the same positive GDM `cs2/cv2` temporal axes.

Reason: after Exp071L, the current ~138-degree temporal result must be treated as oriented until this sign-invariant test is performed. Do not infer the negative-tangent result algebraically; compute it prospectively.

## 9. Highest-value manuscript work

1. Write full Methods for E/F/H/I/J/K/L from exact repository summaries.
2. Build central Figure F5: K2+ and K2- velocity-shape arrows/line with 166/165-degree oriented separation but 13.55/15.07-degree two-sided overlap.
3. Build Table T2 from the exact values in the figure-source manifest.
4. Update Article-2 novelty audit around “oriented tangent vs nuisance-subspace specificity” and related cosmological degeneracy literature.
5. Run a final claim-to-evidence audit before submission language.

## 10. Article boundaries

DSIR-1 owns broad response atlas/localization/curvature/characteristic-scale geometry. DSIR-2 only summarizes that background and focuses on specificity falsification.

DSIR-3 owns covariance whitening, nuisance tangent SVD, quotient-space reconstruction and G7 observational relation/null testing. Do not import those unfinished claims into DSIR-2.

## 11. Gate state

`G7=OPEN`  
`G8=OPEN`  
`G9=OPEN`
