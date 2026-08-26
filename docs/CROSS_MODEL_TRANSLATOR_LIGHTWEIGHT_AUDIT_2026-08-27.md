# DSIR cross-model translator lightweight audit — 2026-08-27

Status: **EXPLORATORY / DESCRIPTIVE ONLY**. This is a retrospective lightweight audit using already-frozen summary products. No new Boltzmann run, no preregistration, no G7/G8/G9 upgrade, and no observational-parameter precision claim.

## Question

Test whether current DSIR results already support the mechanics needed for a cross-model translator / model-of-models:

1. model parameter -> common response coordinates;
2. nearest equivalent region in another family;
3. cycle consistency;
4. local Jacobian/sensitivity differences;
5. information gain from complementary channels;
6. non-redundancy of amplitude, zero and transition coordinates.

## Inputs

- `experiment_047a_finite_amplitude_interaction_curvature_v0_1_summary.json`
- `experiment_048a_interaction_localization_geometry_v0_1_summary.json`
- `experiment_048b_finite_amplitude_localization_flow_v0_1_summary.json`
- `experiment_040_finite_bin_growth_response_v0_1.json`
- `block_aware_observability_atlas_v0_2.json`
- `block_aware_observability_atlas_c6_extension_v0_1.json`
- `data/derived/g7/exp067a_act_unwise_observational_covariance_whitening_v0_1_summary.json`
- `data/derived/g7/exp064a_shapefit_common_plane_null.json`

## 1. C3 GDM viscosity -> C5 designer-f(R) scale-localization translator

Use the finite-amplitude `k_geo` coordinate as a deliberately simple one-coordinate translator.

C3 GDM `cv2` grid:

`{1e-8,1e-7,1e-6,1e-5,1e-4}`

C5 designer-f(R) `B0` grid:

`{1e-6,1e-5,1e-4,1e-3}`.

Nearest `k_geo` matches:

| GDM cv2 | nearest f(R) B0 | relative k_geo mismatch | cycle back |
|---:|---:|---:|---:|
| 1e-8 | 1e-6 | +0.1969% | 1e-8 PASS |
| 1e-7 | 1e-6 | +0.2048% | 1e-8 many-to-one |
| 1e-6 | 1e-5 | -0.2016% | 1e-6 PASS |
| 1e-5 | 1e-5 | +0.7132% | 1e-6 many-to-one |
| 1e-4 | 1e-3 | -1.6920% | 1e-4 PASS |

**Result:** a useful cross-family equivalent map already exists in one response coordinate, and several sampled matches are sub-percent. It is not one-to-one: finite-grid scale translation is many-to-one.

## 2. Channel dependence of the translation

The same GDM points translated using temporal centroid `z_centroid` instead of `k_geo` all choose the largest sampled C5 value `B0=1e-3`. The same is true when using `chi_I` alone.

Therefore

`B0*(scale) != B0*(time) != B0*(interaction amplitude)`

in general.

**Result:** parameter translation is meaningful only after specifying the response subspace. This is evidence for partial observational equivalence, not a fundamental identity between `cv2` and `B0`.

## 3. Joint lightweight coordinate and cycle test

Define a purely exploratory pooled-standardized coordinate

`q = zscore[ ln(k_geo), z_centroid, ln(chi_I) ]`

using the sampled C3-cv2 + C5 points, and nearest-neighbor Euclidean matching.

Only 2/5 C3 grid points return to the same finite C3 point after `C3 -> C5 -> C3`; the other points collapse onto shared C5 representatives. Standardized nearest distances are about `2.15..2.69`.

**Result:** the current three-coordinate summary does not make C3 viscosity and C5 f(R) globally equivalent. Cycle failures expose degeneracy/information loss rather than invalidating the translator idea.

## 4. Local sensitivity / Jacobian sign test

Finite-difference sensitivities per `ln(parameter)` show different local tangent behavior.

For GDM `cv2`, the strongest sampled step has approximately

- `d ln k_geo / d ln cv2 = -0.0943`
- `d z_centroid / d ln cv2 = +0.0604`
- `d ln chi_I / d ln cv2 = -0.485`.

For designer f(R), sampled steps include

- `d ln k_geo / d ln B0 = -0.0021, -0.0171, -0.0877`
- `d z_centroid / d ln B0 = -0.0646, +0.0341, +0.0890`
- `d ln chi_I / d ln B0 = +0.0191, -0.0394, -0.2178`.

The sign reversal in the early f(R) temporal/amplitude tangent has no C3-viscosity analogue on the sampled ray.

**Result:** a Jacobian translator is feasible, but it must be local and multicoordinate; a single global proportionality is already disfavored.

## 5. Complementary-channel information gain proxy

For two normalized unit tangent directions with angle `theta`, the equal-weight 2x2 Gram condition number is

`kappa=(1+cos theta)/(1-cos theta)`.

Using existing hard DSIR angles for GDM `cs2/cv2`:

- density structure angle `0.322616 deg` -> `kappa ~ 1.26e5`;
- finite-bin temporal angle `1.334013 deg` -> `kappa ~ 7.38e3`;
- equalized density+slip acute angle `56.963212 deg` -> `kappa ~ 3.40`.

**Result:** in normalized theory geometry, adding an independent slip block changes the local inverse problem from almost singular to well conditioned. This is a strong proof-of-principle that complementary channels can greatly improve parameter identifiability.

Boundary: this is not an observational Fisher posterior; no covariance, nuisance projection or unequal response amplitude is included in this proxy.

## 6. Amplitude + zero + transition non-redundancy in C6 DCDM

Across the frozen `Gamma/H0=0.25..2` C6 family:

- response L2 grows `0.1254 -> 0.9095`, factor `~7.25`;
- preregistered temporal centroid moves `0.63046 -> 0.65624`, only `~+4.09%`;
- low-z (`z=0.295`) zero crossing moves `0.00268016 -> 0.00257060 h/Mpc`, `~-4.09%`;
- high-z (`z=2.33`) zero crossing changes only `~+0.028%`.

The zero therefore has strong redshift evolution but weak coupling dependence at high z, while amplitude changes strongly with coupling.

**Result:** amplitude, transition epoch and zero/sign geometry are demonstrably non-redundant coordinates on an existing DSIR family.

## 7. Observation-space readiness boundary

Exp067A has already certified an exact selected 26D ACT DR6 x unWISE covariance whitener, so covariance-weighted comparison is technically eligible. However Exp064A found no statistically nontrivial common `(AP,growth,shape)` plane (`p_lambda ~0.265`, `p_LOO ~0.361`). Therefore it is not yet valid to claim a real joint cosmological-parameter precision gain from the cross-model translator.

## Lightweight verdict

**PASS as a proof-of-concept architecture, with explicit limitations.** Current DSIR data already support:

- direct parameter -> response-coordinate maps;
- partial cross-family equivalent regions;
- local Jacobian/sensitivity construction;
- cycle-consistency diagnostics;
- strong complementarity of independent channels;
- joint use of amplitude/zero/transition coordinates;
- block-aware masking of missing domains.

Current DSIR data do **not** yet support:

- a unique one-to-one parameter identity across models;
- a universal scalar translator;
- a single common observational law;
- a claimed improvement of real cosmological parameter errors.

This audit should be treated as motivation for a preregistered `Cross-Model Translator v0.1`, not as G7/G8/G9 evidence.
