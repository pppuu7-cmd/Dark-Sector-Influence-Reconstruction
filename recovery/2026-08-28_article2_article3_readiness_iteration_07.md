# DSIR Article 2 / Article 3 readiness — iteration 07

**Date:** 2026-08-28

Percentages continue the frozen iteration-01 readiness rubric. They measure repository readiness for a complete, defensible article draft; they are not publication probabilities and do not pre-judge open gates.

## Readiness

| Article | Iteration 06 | Iteration 07 | Change |
|---|---:|---:|---:|
| Article 2 | 88% | **90%** | +2 pp |
| Article 3 | 44% | **44%** | 0 pp |

## Article 2 — Exp071J closes the raw-amplitude loophole for Exp071I

Exp071I established strong K2/GDM separation in the same-definition CLASS total-velocity-transfer channel, but a raw oriented-vector angle could in principle have been dominated by a scale-independent response amplitude. Exp071J was preregistered after Exp071I and before any projected angle was calculated to test exactly that loophole.

### Frozen primary projection

For each 7x5 velocity tangent matrix `R(z,k)`, Exp071J removes the complete constant-in-k mode independently at every redshift:

`R_shape(z,k) = R(z,k) - mean_k R(z,k)`.

The five frozen k nodes receive equal weights. No covariance, fitted weights, survey window, or model-dependent scaling enters the primary projection.

Primary K2 point remains bar1 and the 45-degree separator is inherited unchanged from Exp071E/F/H/I.

### Attempt-1 integrity failure

Run `33182476372` did not calculate a projected angle. The evaluator incorrectly looked for GDM files under the K2 artifact subdirectory and failed with:

`no tk.dat files for prefix=cs1em7_ under inputs/exp071i/fresh/k2`.

This was recorded as **INVALID_FOR_SCIENCE**, not a scientific FAIL:

- recovery commit `306cdc1d2e5d60eaa5193367073656bbbe9ec99b`;
- no projection or threshold was changed;
- repair commit `f1b80167b5f8baa668aebbfba0270ab060008ed7` changed only K2/GDM root routing.

### Authoritative attempt 2

- preregistration: `306c19a4286ffc459fc2886097a8b70fa6df89e9`
- run: `33182705074`
- job: `98887703171`
- conclusion: SUCCESS
- artifact: `9690361647`
- artifact ZIP SHA256: `e77409ac72f1a28ad0808afcb6b4f6fdcc983501b452b9ab286aa049380bd805`
- terminal summary: `data/derived/exp071j_total_velocity_shape_projection_summary_v0_1.json`

The evaluator first reproduced the immutable Exp071I raw angles:

- K2 bar1 vs GDM cs2: `165.9454940018 deg`
- K2 bar1 vs GDM cv2: `164.7113289163 deg`

Then the frozen per-redshift shape projection gave:

- K2 bar1 vs GDM cs2 shape: **166.4386944060 deg**
- K2 bar1 vs GDM cv2 shape: **164.9270967302 deg**

Classification:

`K2_VELOCITY_SHAPE_SEPARATED_FROM_BOTH_GDM_AXES_EXP071J`

### Projection is well resolved

Retained shape norm fractions are large:

- K2 bar1: `0.8318697314`
- GDM cs2: `0.8271831839`
- GDM cv2: `0.8372386500`

Thus the primary result is not an angle of a numerically vanishing residual.

The two GDM projected velocity-shape directions remain mutually close:

- `2.5153074440 deg`.

K2 finite-step stability remains strong:

- maximum projected bar1→bar2-5 drift: `0.1429477782 deg`.

### Independent non-classifying projections

All frozen diagnostics preserve strong K2/GDM separation:

- remove one global scalar mean: `163.2376 / 162.0059 deg`;
- remove the temporal mean independently at every k: `158.9454 / 156.2728 deg`;
- per-redshift shape projection of common baryon-velocity transfer `t_b`: `130.2543 / 129.9816 deg`.

The GDM cs2/cv2 projected `t_b` directions are only `0.5320 deg` apart.

### Scientific implication

The Exp071I velocity separation is not solely a scale-independent velocity-amplitude effect on the frozen support. K2 and GDM remain nearly oppositely oriented after quotienting the entire constant-in-k mode independently at each redshift, and the conclusion is stable under several independently frozen projection diagnostics.

The strongest safe Article-2 statement is now:

**A known-sector K2 direction that is close to GDM in selected static matter/metric coordinates is strongly separated from both tested GDM axes in temporal response, total-velocity response, and velocity-shape response after removing scale-independent amplitude modes.**

This remains theory-space response geometry, not tracer RSD, a survey likelihood, observational nuisance quotient, covariance whitening, or unique microscopic identification.

## Article 3 — unchanged at 44%

Exp073R1 v0.5 source Stage A remains PASS, while the downstream full 84,075,649,920-byte metacal sequential mapper remains active. No readiness credit is assigned for active compute time.

- G7 OPEN
- G8 OPEN
- G9 OPEN
- covariance NOT AUTHORIZED
- nuisance quotient NOT AUTHORIZED

## Next admissible Article-2 falsification

Use the immutable Exp071I artifact and the unchanged Exp071J primary projection to perform support-localization ablations:

- leave one frozen k node out, recompute the per-redshift constant-in-k quotient on the remaining four nodes;
- leave one frozen redshift slice out;
- require all preregistered ablations to remain above the inherited 45-degree separator for a strong broad-support classification.

This tests whether Exp071J is driven by a single scale or redshift rather than changing the projection or adding new model freedom.
