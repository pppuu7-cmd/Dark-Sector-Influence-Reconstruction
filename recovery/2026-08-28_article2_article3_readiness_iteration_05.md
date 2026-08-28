# DSIR Article 2 / Article 3 readiness — iteration 05

**Date:** 2026-08-28

This checkpoint uses the frozen scoring rule established in iteration 01. Percentages measure repository readiness for writing a complete, defensible article draft; they are not publication probabilities and do not predict whether an open science gate will PASS.

## Readiness

| Article | Previous fixed point | Iteration 05 | Change |
|---|---:|---:|---:|
| Article 2 | 84% | **86%** | +2 pp |
| Article 3 | 40% | **44%** | +4 pp |

## Article 2: why 86%

The increase is credited to a new prospectively frozen, independently executed, qualitatively independent temporal-response control, Exp071H.

### Exp071G fail-closed provenance diagnosis

The first finite-bin growth attempt, Exp071G v0.1, did not produce a science classification. Its integrity assertion detected that the frozen Exp040 C3 parents and the more recent Exp071E/F GDM parents are not the same tangent construction:

- Exp040 C3 uses averaged local tangents over `cs2,cv2 <= 1e-6` from the frozen comparison atlas;
- Exp071E/F uses specific `1e-7` GDM local responses from the immutable Weyl/slip parent artifact.

The observed GDM finite-bin-growth acute angle was `1.2926742378 deg` for the `1e-7` parents, while Exp040 records `1.3340128036 deg` for the averaged parents. The mismatch was therefore retained as a provenance-boundary result rather than hidden by relaxing the tolerance.

Exp071G v0.1 is **INVALID_FOR_SCIENCE** and contributes no readiness points.

### Exp071H frozen replacement

Exp071H was preregistered before execution with:

- the same finite-bin temporal operator inherited from Exp040,
- the same 45-degree directional separator inherited from Exp071E/F,
- primary GDM parents fixed to the `1e-7` construction for continuity with Exp071E/F,
- Exp040 averaged C3 parents retained only as a non-classifying provenance-sensitivity control,
- K2 bar1 as the primary point; bar2-bar5 only robustness diagnostics,
- no tracer-RSD, `f sigma_8`, whitening or observational interpretation authorized.

Provenance:

- preregistration commit: `93bd51867d90fa346ce644deebe228e6d0d45697`
- workflow run: `33179056348`
- job: `98875221176`
- execution conclusion: SUCCESS
- artifact: `9688888346`
- artifact ZIP SHA256: `60d582b9f0249329c323066f248cbdc33f3c149966eb30317ecb2f3f22cda0a5`
- terminal summary: `data/derived/exp071h_k2_finite_bin_growth_dual_provenance_summary_v0_1.json`

Primary result:

- K2 bar1 vs GDM `cs2(1e-7)`: `138.1005853262 deg`
- K2 bar1 vs GDM `cv2(1e-7)`: `137.0972592611 deg`

Classification:

`K2_FINITE_BIN_GROWTH_SEPARATED_FROM_BOTH_GDM_1E7_AXES_EXP071H`

This is a qualitative reversal relative to the static matter-power block, where Exp071F found approximately `19.2231 deg` and `19.0371 deg` to the two GDM axes.

The result is robust to the parent-tangent convention:

- K2 vs averaged Exp040 `cs2`: `138.1106737796 deg`
- K2 vs averaged Exp040 `cv2`: `137.0710795442 deg`
- parent-convention shifts: `+0.010088 deg` and `-0.026180 deg`.

Finite K2-step robustness is also strong:

- maximum growth-direction drift from bar1: `0.419572 deg`;
- centered K2 growth-family SVD first-mode variance fraction: `0.9999902495`.

### Article-2 scientific implication

The residual K2↔GDM sound-speed-like ambiguity seen in static matter/Weyl/slip coordinates is not a universal response equivalence. A finite-bin temporal derivative of the same matter response supplies a strongly separating direction even though the static matter tangent is close.

The supported paper claim is therefore channel-conditioned:

**static response similarity can coexist with strong temporal-response separation.**

This is not a tracer-RSD or survey distinguishability claim and does not establish unique microscopic identification.

## Article 3: why 44%

The frozen Article-3 scoring rule allocates 20 points to the exact DES-Y1 reproduction prerequisite (`Exp073R1`). Only part of that block is now closed.

Exp073R1 v0.5 Stage A has completed SUCCESS using no HTTP Range requests:

- run: `33175886694`
- source-index job: `98864259826`
- authoritative source bytes: `2738626560`
- exact rows: `136930995`
- authoritative source SHA256: `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`
- derived row-aligned source-index bytes: `273861990`
- derived index SHA256: `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`
- uploaded artifact: `9688707039`

The frozen assertions also explicitly confirmed:

- `selection_applied = false` at Stage A,
- `science_gate_scored = false`,
- `f_invalid_computed = false`,
- covariance not read,
- G8 not read,
- G7/G8/G9 all OPEN.

This closes a real transport/identity prerequisite and demonstrates that sequential whole-object transport is viable for the authoritative source catalog. It does **not** complete Exp073R1.

The downstream `metacal-map` job `98873808534` is currently executing the frozen mapper against the authoritative `84075649920`-byte metacal object through the same no-Range sequential strategy. No points are credited for active compute time; the +4 pp is solely for the completed Stage-A identity/index prerequisite.

## Gate state

- G7: **OPEN**
- G8: **OPEN**
- G9: **OPEN**
- covariance restriction: **NOT AUTHORIZED**
- nuisance SVD / quotient: **NOT AUTHORIZED**

## Next admissible work

1. Article 2: integrate Exp071H as a paper claim and construct the static-vs-temporal ablation figure/table. Before calling the temporal observable RSD-like, require a separate same-convention velocity/provider proof.
2. Article 3: use the terminal state of `metacal-map` as the next decision point. If full Exp073R1 reproduction PASSes, immediately bind its exact reconstruction artifact and proceed to the frozen physical-support classification before covariance. If it fails, diagnose only the failed prerequisite; do not score G7 and do not alter science thresholds.
3. Preserve G7/G8/G9 as OPEN until their explicit downstream gates are executed.
