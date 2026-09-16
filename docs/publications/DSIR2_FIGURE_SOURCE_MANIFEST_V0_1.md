# DSIR-2 figure/source manifest v0.1

**Date:** 2026-08-28  
**Active manuscript:** `DSIR2_MANUSCRIPT_V0_2.md`  
**Purpose:** make every central figure/table reconstructible from repository-resident summaries or immutable workflow artifacts.

## Figure F1 — specificity/falsification ladder

Conceptual synthesis only. No fitted scientific quantity should be introduced in this schematic.

Required experiment sequence:

`Exp071C -> Exp071D/E/F -> Exp071H -> Exp071I -> Exp071J -> Exp071K -> Exp071L -> Exp072/073`.

Labels must distinguish:

- PASS descriptive/physical;
- FALSIFICATION;
- ROBUST ORIENTED;
- INVALID_FOR_SCIENCE;
- SUPPORT/APPLICABILITY boundary.

## Figure F2 — matter-only known-sector falsification

Primary source:

- Exp071C run `33020201997`
- artifact `9626235928`
- inherited F30 operator unchanged from the dark-family test.

Required message: K2 fixed-total-`omega_m` redistribution passes F30 and all leave-one-redshift gates; K1 primordial tilt does not. Do not plot or caption this as a dark-sector classifier.

## Figure F3 — static non-cure

### Exp071E

Repository source:

- `data/derived/exp071e_known_sector_joint_metric_direction_summary_v0_1.json`

Provenance:

- preregistration commit `220e73f6cd5b52746498731073bf7392f6917dd9`
- run `33177588360`
- artifact `9688299959`

Headline values:

- K2-bar1 vs GDM `cs2`: `18.9257 deg`
- K2-bar1 vs GDM `cv2`: `58.9127 deg`
- max K2 joint drift: `0.1240 deg`

### Exp071F

Repository source:

- `data/derived/exp071f_known_sector_matter_weyl_slip_direction_summary_v0_1.json`

Provenance:

- preregistration commit `85daeca416ce8ed1e691008fd4178fd6bbf94d15`
- run `33178154667`
- job `98872091411`
- artifact `9688506671`
- artifact SHA256 `e03e72251ab8ed9e0fa820bdae31342dc718349d78713db5fcac06bf00cc6779`

Headline values:

- static matter K2 vs `cs2`: `19.2231 deg`
- static matter K2 vs `cv2`: `19.0371 deg`
- equalized three-channel K2 vs `cs2`: `19.0749 deg`
- equalized three-channel K2 vs `cv2`: `50.1667 deg`
- max three-channel K2 drift: `0.11694 deg`

## Figure F4 — positive-tangent dynamic separation

### Exp071H — temporal

Repository source:

- `data/derived/exp071h_k2_finite_bin_growth_dual_provenance_summary_v0_1.json`

Provenance:

- preregistration commit `93bd51867d90fa346ce644deebe228e6d0d45697`
- run `33179056348`
- job `98875221176`
- artifact `9688888346`
- SHA256 `60d582b9f0249329c323066f248cbdc33f3c149966eb30317ecb2f3f22cda0a5`

Primary values:

- K2+ vs GDM `cs2(1e-7)`: `138.1005853262 deg`
- K2+ vs GDM `cv2(1e-7)`: `137.0972592611 deg`
- alternate-parent shifts: `+0.01008845 / -0.02617972 deg`

Mandatory caption caveat: positive/oriented K2 tangent only; no sign-invariant temporal claim before a dedicated negative-K2 temporal run.

### Exp071I — raw total velocity

Repository source:

- `data/derived/exp071i_k2_gdm_total_velocity_direction_summary_v0_1.json`

Provenance:

- original preregistration `30797f97f9ee4d295dcaf1905d3647230b6fa1cc`
- pre-execution vTk amendment `55ea3d6435767ecf570702b55d411a12eddd59b4`
- run `33181895623`
- job `98884913088`
- artifact `9690064470`
- ZIP SHA256 `ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14`

Primary values:

- parent P(k) max relative difference: `0.0` vs `1e-10`
- K2+ vs `cs2`: `165.9455 deg`
- K2+ vs `cv2`: `164.7113 deg`
- GDM `cs2` vs `cv2`: `2.3683 deg`

Mandatory caption caveat: CLASS total-velocity transfer, **not** tracer RSD or `f sigma_8`.

## Figure F5 — central two-sided velocity falsification

### Exp071J — amplitude-projected positive velocity shape

Repository source:

- `data/derived/exp071j_total_velocity_shape_projection_summary_v0_1.json`

Provenance:

- preregistration commit `306c19a4286ffc459fc2886097a8b70fa6df89e9`
- attempt-1 invalid recovery `306cdc1d2e5d60eaa5193367073656bbbe9ec99b`
- routing repair `f1b80167b5f8baa668aebbfba0270ab060008ed7`
- run `33182705074`
- job `98887703171`
- artifact `9690361647`
- ZIP SHA256 `e77409ac72f1a28ad0808afcb6b4f6fdcc983501b452b9ab286aa049380bd805`

Projection:

- per-redshift equal-weight constant-in-k subtraction.

Primary values:

- K2+ vs `cs2` shape: `166.4386944060 deg`
- K2+ vs `cv2` shape: `164.9270967302 deg`
- retained norm fractions: K2 `0.83187`, cs2 `0.82718`, cv2 `0.83724`
- GDM projected mutual angle: `2.51531 deg`

### Exp071L — two-sided test

Repository source:

- `data/derived/exp071l_two_sided_k2_velocity_shape_nuisance_summary_v0_1.json`

Provenance:

- preregistration commit `9927f46caefbcd991b2c2e7691f4923c6f7552f6`
- run `33184079909`
- job `98892438220`
- artifact `9690954372`
- SHA256 `6ec9cc4dfa7a94ecec8e4540cbecf034b19bfdc7b0c85b30ac92331b205f71d4`

Reference-integrity values:

- max relative parent P difference `0.0`
- max relative parent `t_tot` difference `0.0`
- threshold `1e-10`

Primary values:

- K2+ vs `cs2`: `166.4386944060 deg`
- K2+ vs `cv2`: `164.9270967302 deg`
- K2- vs `cs2`: `13.5502602743 deg`
- K2- vs `cv2`: `15.0708844313 deg`
- K2- vs K2+ mutual angle: `179.9078020829 deg`
- nonlinear antisymmetry error: `0.00299224934`
- primary minimum angle: `13.5502602743 deg`
- frozen threshold: `45 deg`
- classification: `K2_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071L`

Recommended graphical construction:

- show a 2D schematic/projection only if explicitly labeled as schematic; do not invent a PCA plane as quantitative evidence;
- quantitative panel should instead show signed/oriented angles and corresponding sign-invariant acute line angles;
- visually pair K2+ and K2- as the same nearly one-dimensional nuisance line with opposite arrows;
- emphasize that ~165-degree positive separation becomes ~14-degree line overlap when sign is treated physically.

## Figure F6 — positive velocity support robustness

Repository source:

- `data/derived/exp071k_velocity_shape_support_localization_summary_v0_1.json`

Provenance:

- preregistration commit `3910605e9b8f586ec8dcb8be045c37e83e5afdd3`
- run `33183729426`
- job `98891216832`
- artifact `9690784568`
- SHA256 `9ddf4c31219cad7b97f3aec569fcd50724b141404de8672daca7ab2606265948`

Primary values:

- full-support: `166.4387 / 164.9271 deg`
- leave-one-k minima: `158.1004 / 157.8212 deg`, both at deletion `k=0.1`
- leave-one-z minima: `165.4260 / 163.8526 deg`, both at deletion `z=0.706`
- global minimum across 24 primary angles: `157.8212319078 deg`
- all finite positive K2 steps above 45 degrees.

Mandatory caption caveat from source: broad support is established only for the preregistered **oriented positive-K2** velocity-shape direction.

## Figure F7 — provider and observational-support boundary

Sources: Exp071A, Exp072A/B/C, Exp073A-E.

Required values:

- common provider cells: `495/495`
- first ACT x unWISE retained observational dimension: `0` under frozen `5%` leakage
- joint support frontier: `z_min=0.0087345858`, `k_max=4.8182610974 Mpc^-1`
- tested linear GR-reference route remains ineligible through `Delta^2 <= 2`.

Do not interpret the frontier as a certified science region.

## Figure F8 — finite-operator applicability inventory

Sources: Exp073I/J/K/L support/operator chain.

Required contrast:

- finite BOSS true-k matrix: non-empty component `54/240` rows;
- examined KiDS finite-theta absolute-response route: non-normalizable/inadmissible under the frozen absolute-response criterion.

## Table T1 — condensed claim matrix

Source:

- `docs/ARTICLE2_CLAIM_MATRIX_V0_2.md`

Must visibly distinguish `ORIENTED`, `ROBUST ORIENTED`, `FALSIFICATION`, and `BOUNDARY`.

## Table T2 — static/temporal/velocity hierarchy

Minimum rows:

| Representation | K2 vs cs2 | K2 vs cv2 | Interpretation |
|---|---:|---:|---|
| static matter | 19.2231 | 19.0371 | overlap both |
| static matter+Weyl+slip | 19.0749 | 50.1667 | cs2 overlap remains |
| temporal, K2+ | 138.1006 | 137.0973 | oriented separation |
| raw `t_tot`, K2+ | 165.9455 | 164.7113 | oriented separation |
| projected `t_tot` shape, K2+ | 166.4387 | 164.9271 | robust oriented separation |
| projected `t_tot` shape, K2- | 13.5503 | 15.0709 | two-sided specificity FAIL |

All angles in degrees; 45-degree separator is preregistered test threshold, not universal physics.

## Table T3 — provenance ledger

Resolve each manuscript quantitative sentence to:

`experiment -> prereg commit -> run -> job -> artifact -> SHA256 -> repository summary`.

No number should enter the final manuscript solely from chat history.

## Open figure-source item

A two-sided negative-K2 temporal control matching Exp071H does not yet exist in this manifest. Until generated prospectively, do not create a figure implying temporal sign-invariant separation.
