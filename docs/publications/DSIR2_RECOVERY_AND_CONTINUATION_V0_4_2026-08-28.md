# DSIR-2 recovery and continuation — v0.4

**Frozen:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Purpose:** reconstruct Article 2 in a fresh chat/session after the Exp071M/N evidence-chain closure.

## 1. Start here

Read in this order:

1. `docs/publications/DSIR2_MANUSCRIPT_V0_4.md` — active integrated manuscript.
2. `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md` on `main` — canonical pointer.
3. `docs/ARTICLE2_CLAIM_MATRIX_V0_3_K1_REPRESENTATION_CONSOLIDATION.md` on `main` — authoritative Article-2 claim boundary after Exp071M/N.
4. `docs/ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main` — science-closure verdict.
5. `docs/ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` on `main` — final visual/table specification.
6. `docs/DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md` on `main` — metric-aware ray/line/subspace formalism.
7. `data/derived/exp071m_two_sided_k1_transfer_null_summary_v0_1.json` on `main`.
8. `data/derived/exp071n_two_sided_k1_velocity_power_shape_summary_v0_1.json` on `main`.
9. Historical publication files in `docs/publications/` for audit/provenance.

Do not use historical Article-2 v0.1/v0.2 claim matrices as current interpretations. Preserve them as provenance snapshots only.

## 2. Current scientific status

Canonical verdict:

`ARTICLE2_SCIENTIFIC_EVIDENCE_CHAIN_CLOSED_FOR_DECLARED_SCOPE_V0_1`

No additional K1/K2 or near-duplicate angle experiment is scientifically required before writing Article 2 unless a concrete defect is found in provenance, units, conventions, frozen thresholds or reproducibility.

This is not submission readiness. Remaining work is manuscript assembly, prior-art/novelty verification, bibliography, figures/tables and final release-candidate audit.

## 3. Central thesis

> Response equivalence is conditioned by the chosen representation, whether the relevant nuisance is resolved in that representation, the channel/operator and metric, and whether the physical nuisance freedom is an oriented ray, a two-sided line or a higher-dimensional subspace. K2 demonstrates false oriented separation after sign freedom is restored; K1 demonstrates a representation kernel in transfer-only space and renewed overlap after the missing primordial-power term is restored.

Compact hierarchy:

`representation -> resolvability -> ray/line/subspace -> channel-conditioned equivalence -> physical support -> observational quotient`.

## 4. Evidence sequence

1. **Exp071C:** K2 fixed-total-matter known-sector family passes F30; K1 tilt does not. Matter-only F30 is not generically dark-specific.
2. **Exp071D/E/F:** Weyl/slip and matter+Weyl+slip add information but retain K2~GDM-`cs2` overlap.
3. **Exp071H:** positive K2 finite-bin temporal ray is strongly separated (`138.1006/137.0973 deg`). Oriented-ray result only.
4. **Exp071I:** positive K2 source-audited `t_tot` ray is strongly separated (`165.9455/164.7113 deg`).
5. **Exp071J:** per-redshift constant-in-k removal preserves positive-ray separation (`166.4387/164.9271 deg`), retaining ~83% norm.
6. **Exp071K:** all 24 leave-one-k/z positive-ray tests remain >45 deg; minimum `157.8212 deg`.
7. **Exp071L:** fresh K2− lies `13.5503/15.0709 deg` from GDM and is `179.9078 deg` from K2+, falsifying two-sided K2 specificity.
8. **Exp071M:** K1 primordial tilt is exactly null in transfer-only `t_tot`; experiment stops `INVALID_FOR_SCIENCE_EXP071M`, with no angle defined.
9. **Exp071N:** physically complete `Delta ln P_R + 2 Delta ln|t_tot|` resolves K1, but its two-sided line overlaps GDM at `36.0622/37.8458 deg`, below 45 deg.
10. **Exp071A + Exp072/073:** provider-space completion does not imply observational admissibility.

## 5. Exp071M exact boundary

Preregistration commit: `e3c0c7315ccb78d0a292db765eda172113f664bd`  
Run: `33185652795`  
Job: `98897856253`  
Artifact: `9691596312`  
SHA256: `d0878a71adb7bbf97d7b00a67e306c0ae9c86b8b2e705cbafd00b354ede23b21`

Parameter points:

- `n_s ref = 0.965`
- `n_s plus = 0.970`
- `n_s minus = 0.960`

Both transfer-only responses are exactly zero on the frozen support. Scientific meaning: **representation kernel**, not absence of primordial-tilt physics.

Mandatory rule:

`||A r_nuisance|| > numerical_resolution_floor`

before normalized-angle geometry is allowed.

## 6. Exp071N exact result

Preregistration commit: `cfaf9d14fa734e155cab5dca028bc1a14d0afd46`  
Run: `33186048775`  
Job: `98899204160`  
Artifact: `9691720131`  
SHA256: `19ce8623c64faf2e9ebd1d38ce2db5eb394d0a941457b18a8b59508d558d00eb`

Representation:

`r_vv = Delta ln P_R(k) + 2 Delta ln|t_tot|`.

Angles:

- K1+ vs GDM `cs2`: `36.0622372504 deg`;
- K1+ vs GDM `cv2`: `37.8458122995 deg`;
- K1− vs GDM `cs2`: `143.9377627496 deg`;
- K1− vs GDM `cv2`: `142.1541877005 deg`;
- K1+/K1− mutual: `179.9999991462 deg`;
- antisymmetry error: `0.0`.

Line angles:

- `36.0622372504 deg` to `cs2`;
- `37.8458122995 deg` to `cv2`.

Classification:

`K1_TWO_SIDED_VELOCITY_POWER_SHAPE_OVERLAPS_GDM_EXP071N`.

Retained projected norm fractions:

- K1: `0.6255351`;
- GDM `cs2`: `0.8271832`;
- GDM `cv2`: `0.8372387`.

Fresh reference maximum relative differences in parent `P` and `t_tot`: `0.0` against `1e-10`.

Diagnostic correction: original non-classifying validation mixed a line angle with an oriented negative-branch angle. Correct branch-to-line discrepancies are only `~2e-14 deg` and `~1e-14 deg`. Frozen primary classification is unchanged.

## 7. Ray / line / subspace formalism

Metric norm:

`||x||_M = sqrt(x^T M x)`.

Oriented ray angle:

`cos(theta_ray) = (r^T M n)/(||r||_M ||n||_M)`.

Two-sided nuisance-line angle:

`theta_line = acos(|r^T M n|/(||r||_M ||n||_M))`.

Multi-nuisance projector:

`P_N = N (N^T M N)^+ N^T M`.

Nuisance-orthogonal fraction:

`eta_N = ||r - P_N r||_M / ||r||_M`.

Do not set `M=C^-1` for an observational claim until the relevant physical support and covariance gates are terminal.

## 8. What supersedes v0.3 recovery

The v0.3 note treated a fresh negative-K2 temporal experiment as the highest-value unresolved Article-2 control. The later canonical science-closure audit supersedes that requirement.

Current rule:

- Exp071H remains only an **oriented-ray** result.
- A negative-K2 temporal extension could test finite-step curvature, but it is **not required** for the declared Article-2 scientific scope.
- Do not delay manuscript assembly waiting for it.

## 9. Final figures/tables

Use `docs/ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` on `main`.

- **Figure 1:** static ambiguity -> positive temporal/velocity rays -> K2 nuisance-line reversal.
- **Figure 2:** K1 transfer-only representation kernel -> velocity-power recovery -> K1 line overlap.
- **Figure 3:** provider support vs observational finite-operator admissibility.
- **Figure 4:** full DSIR hierarchy schematic.
- **Table 1:** terminal comparison matrix.
- **Table 2:** provenance ledger.

## 10. Mandatory claim boundaries

Never claim:

- unique dark-sector fingerprint;
- generic known-sector specificity of velocity or velocity-power shape;
- that positive K2 ray separation implies K2 nuisance-line separation;
- that K1 has no physical effect because transfer-only `t_tot` is zero;
- tracer RSD or `f sigma_8` for `t_tot` or the velocity-power proxy;
- survey distinguishability;
- covariance-whitened/nuisance-marginalized separation;
- G7/G8/G9 closure.

Allowed:

- representation-specific nulls;
- resolvability as a prerequisite for geometry;
- ray/line/subspace-conditioned equivalence;
- positive-ray separation as explicitly oriented;
- K2 and K1 two-sided overlap in the tested representations;
- physical/provider support distinct from observational admissibility.

## 11. Remaining work

Scientific evidence is closed. Continue with:

1. targeted novelty/prior-art audit;
2. verified bibliography;
3. final Figures 1–4 from immutable data;
4. Tables 1–2 with exact provenance;
5. claim-to-evidence audit;
6. exact release-candidate reproducibility audit;
7. journal formatting and language edit.

## 12. Article-3 handoff

Article 3 must build nuisance directions only after they are resolved in the final observation representation, then construct the full signed nuisance subspace under the valid covariance metric.

Ordering:

`finite observation reconstruction -> physical support -> covariance restriction -> whitening -> resolved signed nuisance basis -> metric nuisance projector -> G7 test`.

`G7=OPEN`  
`G8=OPEN`  
`G9=OPEN`
