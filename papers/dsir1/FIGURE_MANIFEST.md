# DSIR-I publication figure manifest

**Date:** 2026-08-27  
**Rule:** every figure must be reproducible from frozen repository products without hand-edited scientific numbers. Plot aesthetics may change; scientific selections, masks, normalizations, thresholds, and orientation rules may not be changed after viewing the plot unless the change is explicitly versioned and justified.

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

**Status:** schematic/formal; no numerical data.

**Caption boundary:** joint nuisance refitting can violate the simple blockwise refinement argument; the diagram is an analysis architecture, not a statement that the full DSIR observational quotient is already complete.

---

## Figure 2 — Failure of the additive scale+time core

**Purpose:** establish the negative result before presenting the hierarchy.

Preferred layout:

- panel A: representative normalized response `R(z,k)`;
- panel B: additive projection `mu+T(k)+tau(z)`;
- panel C: irreducible `I(z,k)`;
- panel D: fraction `chi_I` for the six frozen low-k directions.

Use representative families that make the contrast clear without post-hoc selection: IDE beta, GDM `cs2`, and designer-f(R), plus smooth-w as an intermediate reference if space allows.

**Primary source:** `data/derived/comparison_readiness/experiment_045a_core_G_T_tau_additive_projection_v0_1.json` and its immutable parent response arrays.

**Hard context:** `FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1`, run `32883280742`, artifact `9576600500`.

**Caption boundary:** C4 WDM is not on this common low-k support and is absent rather than zero.

---

## Figure 3 — Finite-amplitude nonseparability hierarchy and grid robustness

**Purpose:** central quantitative figure for DSIR-I.

Panel A: log-scale finite-amplitude `chi_I` envelopes from Exp047A:

- IDE `1.4351e-11 .. 5.4945e-11`;
- smooth-w `1.080507e-3 .. 1.088059e-3`;
- GDM `1.301046e-2 .. 4.541027e-2`;
- designer-f(R) `1.733267e-1 .. 3.133258e-1`.

Panel B: leave-one-node ranges from Exp047B for representative individual directions; mark that the class tier ordering is preserved in `12/12` deterministic deletions.

**Sources:**

- `data/derived/comparison_readiness/experiment_047a_finite_amplitude_interaction_curvature_v0_1_summary.json`;
- `data/derived/comparison_readiness/experiment_047b_interaction_leave_one_node_stability_v0_1.json`.

**Provenance:** runs `32900174734` and `32894616114`; artifacts `9582737965` and `9580724793`.

**Caption boundary:** the ordering is hard descriptive on the sampled domains but no post-hoc scientific stability threshold was frozen; smooth-w absolute `chi_I` is sensitive to the lowest-k node.

**Implementation:** `papers/dsir1/figures/fig03_chiI_hierarchy.py`.

---

## Figure 4 — Channel-conditional degeneracy breaking

**Purpose:** make the central identifiability idea visually immediate.

Panel A, GDM `cs2` versus `cv2`:

- low-k matter angle `0.3226 deg`;
- Weyl-amplitude angle `0.3007 deg`;
- metric-slip angle `137.9432 deg`;
- equalized Weyl+slip angle `56.9632 deg`.

Panel B, GDM versus designer-f(R):

- leading scale-mode angles `0.07813/0.10169 deg`;
- time/full structure separation `~25.18/25.49 deg`;
- oriented full ray separation `154.82/154.51 deg`.

**Sources:** Exp031/032 hard runs and `docs/GATES.md`.

**Provenance:**

- Exp031 run `32774501126`, artifact `9537418753`, digest `3d7e8692...f7f0`;
- Exp032 run `32774501069`, artifact `9537445668`, digest `4197b928...1d0e`.

**Caption boundary:** these are frozen theory-response separators, not survey-level significance. The formal observational signature requires `K_B`, covariance whitening, and nuisance quotient.

---

## Figure 5 — Curved trajectories and mechanism diversity

**Purpose:** show why response-space dimension must not be confused with microscopic parameter count, and why one common scale-time template is insufficient.

Preferred layout:

- panel A: GDM viscosity `chi_I` versus `cv2` with response-direction turning;
- panel B: designer-f(R) `chi_I` versus `B0` with turning;
- panel C: WDM `k_0.1` versus withheld mass at one reference redshift plus redshift consistency band;
- panel D: DCDM temporal centroid `z_R` versus `Gamma/H0`.

**Sources:** Exp047A, Exp050B, Exp053A.

**Hard values:**

- GDM `cv2` max response turn `7.1765 deg`;
- f(R) max response turn `12.1367 deg`;
- WDM `k_0.1(z=0.295) = 8.38666,12.19283,14.23013,16.47374 h/Mpc` for `2.5,3.5,4.0,4.5 keV`;
- DCDM `z_R = 0.6304573,0.6343830,0.6419613,0.6562403` for `Gamma/H0=0.25,0.5,1,2`.

**Caption boundary:** WDM is withheld interpolation inside an existing family; DCDM is a genuinely withheld mechanism for a broad directional idea but not a formal G8 relation test.

---

## Figure 6 — Failure-resistant science: PASS and FAIL chronology

**Purpose:** distinguish DSIR's validation protocol from success-only model atlases.

Panel A: C3 provider chain

`Exp070A FAIL (4.75% target-grid defect) -> Exp070B interpolation-dominated mechanism audit -> Exp070C native-grid provider PASS (2.81e-14 closure)`.

Panel B: C5 provider chain

`Exp069B q=1 FAIL (5.306e-6 > frozen 5e-6) -> Exp069F prospective accuracy ladder -> Exp069H q=3 provider PASS (1.701e-6 target / 2.842e-6 raw zero closure)`.

Panel C: universality falsification

`C3/C5 calibration -> frozen positive common-centroid slope interval -> withheld C7/IDM-DR Exp054C slopes all negative -> FAIL`.

**Sources:**

- `data/derived/g7/exp070a_c3_gdm_readonly_dm_power_bridge_v0_1_result.json`;
- `recovery/exp070c_provider_checkpoint_2026-08-27.md`;
- `data/derived/g7/exp069b_c5_explicit_eft_python_power_bridge_v0_1_result.json`;
- `recovery/exp069h_c5_provider_certification_checkpoint_2026-08-27.md`;
- `docs/SCIENTIFIC_FINDING_F27_COMMON_RESPONSE_CENTROID_WITHHELD_FAILURE.md`.

**Caption boundary:** later PASS contracts do not reclassify earlier FAIL contracts; the common-centroid law remains falsified.

---

## Supplementary figures

### S1 — Pairwise interaction localization

Plot `eta_I` with total angle beside it, emphasizing the GDM `cs2/cv2` counterexample where `eta_I~0.73` accompanies a tiny total matter angle.

Source: Exp046/047B.

### S2 — Leave-one-node sensitivity atlas

Show all 12 reduced-grid `chi_I` values for each direction rather than only min/max. This is useful for exposing the smooth-w `k=0.001` sensitivity.

Source: full Exp047B artifact.

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
