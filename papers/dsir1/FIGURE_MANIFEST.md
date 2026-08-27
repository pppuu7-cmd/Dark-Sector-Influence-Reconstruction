# DSIR-I publication figure manifest

**Date:** 2026-08-27  
**Rule:** every figure must be reproducible from frozen repository products without hand-edited scientific numbers. Plot aesthetics may change; scientific selections, masks, normalizations, thresholds, and orientation rules may not be changed after viewing the plot unless the change is explicitly versioned and justified.

## Build status

| Figure | Scientific role | Reproducible script | Status |
|---|---|---|---|
| 1 | operator/equivalence architecture | `papers/dsir1/figures/fig01_operator_architecture.py` | IMPLEMENTED; formal-source guarded |
| 2 | additive scale+time core failure | `papers/dsir1/figures/fig02_additive_core_failure.py` | IMPLEMENTED; recomputes decomposition and checks Exp045A |
| 3 | finite-amplitude nonseparability hierarchy | `papers/dsir1/figures/fig03_chiI_hierarchy.py` | IMPLEMENTED; Exp047A/B provenance guarded |
| 4 | channel-conditional degeneracy breaking | `papers/dsir1/figures/fig04_channel_conditional_degeneracy.py` | IMPLEMENTED; frozen discriminant-edge gates re-evaluated |
| 5 | curvature and mechanism localization | `papers/dsir1/figures/fig05_curvature_and_localization.py` | IMPLEMENTED; Exp047A/050B/053A provenance guarded |
| 6 | failure-resistant science chronology | planned | NOT YET IMPLEMENTED |

Generated binaries are intentionally produced by GitHub Actions rather than committed as opaque hand-made figures. Each implemented figure writes PDF/PNG/SVG plus a provenance JSON containing source paths, run/artifact identifiers where applicable, checks, interpretation boundaries, and output SHA256 hashes.

---

## Figure 1 — DSIR operator and equivalence architecture

**Purpose:** orient the reader before any numerical atlas result.

Show the map

`theory state r(theta) -> physical/window K_B -> covariance whitener W_B -> nuisance quotient Q_B -> signature s_B`

with

`A_B = Q_B W_B K_B`

and

`r1 ~_B r2 <=> A_B(r1-r2)=0`.

Also show compatible-channel stacking and the kernel relation

`ker A_(B+C) = ker A_B ∩ ker A_C`

under the explicitly stated compatible-quotient assumption.

**Source:** `docs/CHANNEL_CONDITIONAL_EQUIVALENCE_QUOTIENT_THEOREMS_2026-08-27.md`.

**Implementation:** `papers/dsir1/figures/fig01_operator_architecture.py`.

**Caption boundary:** joint nuisance refitting can violate the simple blockwise refinement argument; the diagram is an analysis architecture, not a statement that the full DSIR observational quotient is already complete. It is a formal identifiability construction, not a new physical law.

---

## Figure 2 — Failure of the additive scale+time core

**Purpose:** establish the negative result before presenting the hierarchy.

Implemented layout:

- panel A: normalized designer-f(R) response `R(z,k)`;
- panel B: recomputed additive projection `mu+T(k)+tau(z)`;
- panel C: recomputed irreducible `I(z,k)`;
- panel D: recomputed `chi_I` for all six frozen low-k directions.

The plotting script reconstructs the two-way additive projection directly from `local_response_tangents_v0_1.json` and requires its `chi_I` values to agree with Exp045A before a figure is written.

**Primary sources:**

- `data/derived/comparison_readiness/local_response_tangents_v0_1.json`;
- `data/derived/comparison_readiness/experiment_045a_core_G_T_tau_additive_projection_v0_1.json`.

**Hard context:** `FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1`, run `32883280742`, artifact `9576600500`, artifact digest `59839a27...28dd`.

**Implementation:** `papers/dsir1/figures/fig02_additive_core_failure.py`.

**Caption boundary:** C4 WDM is not on this common low-k support and is absent rather than zero. `chi_I` is a representation diagnostic on the stated domain, not a fundamental dark-sector degree of freedom.

---

## Figure 3 — Finite-amplitude nonseparability hierarchy and grid robustness

**Purpose:** central quantitative figure for DSIR-I.

Panel A: log-scale finite-amplitude `chi_I` envelopes from Exp047A:

- IDE `1.4351e-11 .. 5.4945e-11`;
- smooth-w `1.080507e-3 .. 1.088059e-3`;
- GDM `1.301046e-2 .. 4.541027e-2`;
- designer-f(R) `1.733267e-1 .. 3.133258e-1`.

Panel B: leave-one-node ranges from Exp047B for representative individual directions; the class tier ordering is required to remain preserved in `12/12` deterministic deletions before plotting.

**Sources:**

- `data/derived/comparison_readiness/experiment_047a_finite_amplitude_interaction_curvature_v0_1_summary.json`;
- `data/derived/comparison_readiness/experiment_047b_interaction_leave_one_node_stability_v0_1.json`.

**Provenance:** runs `32900174734` and `32894616114`; artifacts `9582737965` and `9580724793`; digests are hard-checked by the script.

**Implementation:** `papers/dsir1/figures/fig03_chiI_hierarchy.py`.

**Caption boundary:** the ordering is descriptive on the sampled domains; no post-hoc scientific stability threshold was frozen. Smooth-w absolute `chi_I` is sensitive to the lowest-k node. Leave-one-node robustness is an internal grid-stability test, not independent-data confirmation.

---

## Figure 4 — Channel-conditional degeneracy breaking

**Purpose:** make the central identifiability idea visually immediate.

Panel A, GDM `cs2` versus `cv2`:

- low-k matter angle `0.322616 deg`;
- Weyl-amplitude angle `0.300746 deg`;
- metric-slip angle `137.943199 deg`;
- equalized Weyl+slip angle `56.963184 deg`.

Panel B, GDM versus designer-f(R):

- leading scale-mode angles `0.078132/0.101694 deg`;
- time-mode separation `25.1839/25.4937 deg`;
- oriented full-ray separation `154.8161/154.5063 deg`.

**Primary source:** `data/derived/comparison_readiness/discriminant_edges_v0_1.json`.

**Hard provenance:**

- Exp031 run `32774501126`, digest `sha256:3d7e8692...f7f0`;
- Exp032 run `32774501069`, digest `sha256:4197b928...1d0e`.

The script re-evaluates the original hard thresholds before plotting rather than trusting only stored PASS labels.

**Implementation:** `papers/dsir1/figures/fig04_channel_conditional_degeneracy.py`.

**Caption boundary:** these are frozen theory-response separators, not survey-level significance. The formal observational signature still requires `K_B`, covariance whitening, and nuisance quotient.

---

## Figure 5 — Curved trajectories and mechanism diversity

**Purpose:** show why response-space dimension must not be confused with microscopic parameter count, and why one common scale-time template is insufficient.

Implemented layout:

- panel A: maximum sampled normalized response-direction turn for smooth DE, GDM pressure, GDM viscosity, and designer-f(R);
- panel B: withheld thermal-WDM cutoff `k_0.1` versus mass, showing all frozen redshift traces;
- panel C: withheld DCDM temporal centroid `z_R` versus `Gamma/H0`.

**Sources:**

- Exp047A: `data/derived/comparison_readiness/experiment_047a_finite_amplitude_interaction_curvature_v0_1_summary.json`;
- Exp050B: `data/derived/comparison_readiness/experiment_050b_wdm_free_streaming_cutoff_withheld_v0_1_summary.json`;
- Exp053A: `data/derived/comparison_readiness/experiment_053a_dcdm_withheld_temporal_localization_v0_1_summary.json`.

**Hard / frozen values used:**

- GDM `cv2` max response turn `7.1765129 deg`;
- designer-f(R) max response turn `12.1366589 deg`;
- WDM `k_0.1(z=0.295) = 8.386656, 12.192829, 14.230131, 16.473743 h/Mpc` for `2.5, 3.5, 4.0, 4.5 keV`;
- DCDM `z_R = 0.6304573, 0.6343830, 0.6419613, 0.6562403` for `Gamma/H0 = 0.25, 0.5, 1, 2`.

Before plotting, the script requires the WDM cutoff to retain its frozen positive monotonic mass steps and the DCDM centroid to retain the preregistered `>1e-3` consecutive motion.

**Implementation:** `papers/dsir1/figures/fig05_curvature_and_localization.py`.

**Caption boundary:** the three panels are deliberately not collapsed to one universal scalar law. WDM is a withheld interpolation inside an existing mechanism family. DCDM is a genuinely withheld mechanism for a preregistered characteristic-epoch motion prediction, but it does not formally close G8 because no model-independent universal G7 law had been frozen.

---

## Figure 6 — Failure-resistant science: PASS and FAIL chronology

**Purpose:** distinguish DSIR's validation protocol from success-only model atlases.

Planned layout:

- panel A, C3 provider chain: `Exp070A FAIL (~4.75% target-grid defect) -> Exp070B interpolation-dominated mechanism audit -> Exp070C native-grid provider PASS (~2.81e-14 closure)`;
- panel B, C5 provider chain: `Exp069B q=1 FAIL (5.306e-6 > frozen 5e-6) -> Exp069F prospective accuracy ladder -> Exp069H q=3 provider PASS`;
- panel C, universality falsification: `C3/C5 calibration -> frozen positive common-centroid slope interval -> withheld C7/IDM-DR Exp054C slopes all negative -> FAIL`.

**Sources:**

- `data/derived/g7/exp070a_c3_gdm_readonly_dm_power_bridge_v0_1_result.json`;
- `recovery/exp070c_provider_checkpoint_2026-08-27.md`;
- `data/derived/g7/exp069b_c5_explicit_eft_python_power_bridge_v0_1_result.json`;
- `recovery/exp069h_c5_provider_certification_checkpoint_2026-08-27.md`;
- `docs/SCIENTIFIC_FINDING_F27_COMMON_RESPONSE_CENTROID_WITHHELD_FAILURE.md`.

**Caption boundary:** later PASS contracts do not reclassify earlier FAIL contracts; the prospectively tested common-centroid law remains falsified.

---

## Supplementary figures

### S1 — Pairwise interaction localization

Plot `eta_I` with total angle beside it, emphasizing the GDM `cs2/cv2` counterexample where `eta_I~0.73` accompanies a tiny total matter angle. Source: Exp046/047B.

### S2 — Leave-one-node sensitivity atlas

Show all 12 reduced-grid `chi_I` values for each direction rather than only min/max. This is useful for exposing the smooth-w `k=0.001` sensitivity. Source: full Exp047B artifact.

### S3 — WDM high-k time atlas

Heatmaps or response curves for 2/3/5 keV from Exp050A, preserving its distinct high-k support.

### S4 — Prospective prediction ledger

Timeline/table including within-family PASS, withheld-family PASS, and prospective FAIL results. Do not omit failures.

---

## Figure acceptance checklist

A figure is manuscript-eligible only if all of the following hold:

1. every scientific input is read from a frozen repository product or immutable artifact;
2. no missing theory/channel cell is zero-imputed;
3. no family-specific normalization is chosen after viewing the plot unless it is purely display-only and clearly stated;
4. oriented versus acute angles are labeled correctly;
5. theory-response metrics are not labeled as observational significance;
6. PASS/FAIL status and the applicable frozen threshold are stated where relevant;
7. any withheld point is identified as within-family interpolation or withheld mechanism, as appropriate;
8. the plotting script and output-data checksum are retained with the paper branch.
