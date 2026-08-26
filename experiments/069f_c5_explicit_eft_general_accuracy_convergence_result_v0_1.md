# Exp069F — C5 explicit-EFT general-accuracy convergence result v0.1

**Date:** 2026-08-27  
**Execution status:** `COMPLETE_C5_EXPLICIT_EFT_GENERAL_ACCURACY_CONVERGENCE_V0_1`  
**Scientific classification:** `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`

## Frozen provenance

The prospective specification was committed as `43ef913645a43f091e728623291bc21642a56ab9` before any `q>1` solver execution.

Execution used merge head `30706773a0069b6bbe3144443debeeffa6fba328` and pinned upstream

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

GitHub Actions:

- run: `33023027901`;
- immutable artifact: `9627458877`;
- artifact digest: `sha256:d8e1a42bf813d5ae105ea33e723868d454ff7584424373ecfe4594a2dfe49358`.

The full raw case products remain in that immutable artifact. Repository key metrics are mirrored in
`data/derived/g7/exp069f_c5_explicit_eft_general_accuracy_convergence_v0_1_key_metrics.json`.

## Frozen primary result

The frozen paired accuracy ladder was

`q = AccuracyBoost = lAccuracyBoost = [1,2,3,4]`

with `lSampleBoost=1`, `DoLateRadTruncation=True`, unchanged physics, unchanged `k_per_logint=320`, and the unchanged target-grid GR-limit criterion

`M_q <= 5e-6`.

| q | target `M_q` | raw same-node `R_q` | frozen target criterion |
|---:|---:|---:|---|
| 1 | `5.302921926164412e-6` | `9.938162077359033e-6` | FAIL |
| 2 | `2.904403568550871e-6` | `5.400555774622087e-6` | **PASS** |
| 3 | `1.7011186858522977e-6` | `2.8421302380756537e-6` | **PASS** |
| 4 | `1.3107890273503598e-6` | `1.5177816179258466e-6` | **PASS** |

Therefore the exact preregistered primary classification is

`GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`,

and the first passing accuracy in the pre-frozen ascending ladder is `q=2`.

No threshold was changed after output inspection.

## Convergence diagnostics

Both target and raw discrepancies decrease monotonically over the complete frozen ladder:

- `M_q/M_1 = [1, 0.5476987233, 0.3207889367, 0.2471824111]`;
- `R_q/R_1` also decreases monotonically;
- q=1 residual morphology remains strongly correlated with the higher-accuracy residuals, although the correlation weakens as their amplitude becomes smaller.

Target residual correlations relative to q=1 are approximately:

- q=2: `0.9781 / 0.9813 / 0.9821` for `mm/Wm/WW`;
- q=3: `0.9565 / 0.9564 / 0.9485`;
- q=4: `0.8725 / 0.8749 / 0.8896`.

The three blocks remain mutually close at every q: maximum differences between signed block residual fields are only a few `1e-7`.

A retrospective log-log fit gives an approximately inverse-accuracy decrease of the target maximum (`M ~ q^-1.03`, descriptive only). This was not preregistered and is **not** promoted to a law or acceptance criterion.

## Background/transfer localization

For every paired q:

- public `H(z)` values agree exactly on the frozen redshift grid;
- public conformal-time values agree exactly;
- returned `zstar`, `rstar`, `thetastar`, `DAstar`, `zdrag`, `rdrag`, `keq` and the other common numerical derived quantities agree exactly within each GR/designer-zero pair;
- Return-to-GR moves the effective EFT perturbation turn-on to `a=1.1` for the zero case.

Together with Exp069E, this materially narrows the old 5.3-ppm discrepancy: it is not explained by a physical-size background EFT residue and it converges downward under paired ordinary CAMB integration/hierarchy accuracy. The evidence is consistent with a numerical explicit-EFT/ordinary-GR transfer-integration mismatch rather than a physical designer-f(R) zero-limit signal.

This is a mechanism conclusion, not a dark-sector detection.

## Important raw-grid observation

The preregistered primary criterion was defined on the frozen target grid, so q=2 is the formal first Exp069F PASS.

However, the stored solver-native grids are exactly equal within every pair, and the same-node q=2 maximum is

`R_2 = 5.400555774622087e-6`,

slightly above `5e-6`. q=3 is the first tested setting for which **both** target and raw same-node maxima are below `5e-6`.

This does **not** change the Exp069F classification. It is a post-Exp069F provider-design fact that can be used prospectively when choosing the next independently certified C5 provider route. It must not be retroactively inserted into Exp069F's frozen criterion.

## Integrity controls

All frozen integrity controls passed:

- all eight paired case processes completed;
- all case analyses completed;
- pinned solver SHA before/after;
- exact raw grid equality inside every pair;
- linear-only / `NonLinear_none`;
- exact accuracy readback;
- exact designer branch readback;
- no upstream source modification;
- no floor subtraction, normalization fit, smoothing, jitter or threshold retuning.

## Historical failure semantics

Exp069B remains permanently

`FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.

Exp069F does not rewrite that experiment. The result instead demonstrates that a **new**, higher-accuracy unmodified-upstream route is scientifically eligible for separate prospective certification.

## Gate boundary

Exp069F itself does **not** certify C5.

- C5 physical provider: `NOT CERTIFIED`;
- common support-validity mask: `NOT AUTHORIZED`;
- covariance/nuisance G7 advance: `NOT AUTHORIZED`;
- G7: `OPEN`;
- G8: `OPEN`;
- G9: `OPEN`.

The next C5 experiment must satisfy the already-frozen Exp069G minimum provider contract independently.
