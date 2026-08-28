# DSIR Article 2 / Article 3 readiness — iteration 03

**Date:** 2026-08-28

This checkpoint is an evidence-based scientific-readiness score, not manuscript/editorial completion.

## Readiness

| Article | Previous fixed point | Iteration 03 | Change |
|---|---:|---:|---:|
| Article 2 | 80% | **82%** | +2 pp |
| Article 3 | 40% | **40%** | 0 pp |

## Why Article 2 increased to 82%

Exp071E is now prospectively frozen, independently executed in GitHub Actions, terminal, and paper-integrated.

Preregistration was committed **before** the Exp071E computation:

- prereg commit: `220e73f6cd5b52746498731073bf7392f6917dd9`
- run: `33177588360`
- job: `98870121386`
- artifact: `9688299959`
- artifact SHA256: `8547908fdb215a444d29abbb797c3175ef5e51064e02dd7f59cec3903584581c`
- workflow conclusion: SUCCESS

Frozen primary threshold: both K2-vs-GDM joint-direction angles must be `>=45 deg` for separation from both tested GDM axes.

Observed:

- K2 bar1 vs GDM `cs2`: `18.925666634781507 deg`
- K2 bar1 vs GDM `cv2`: `58.912673573574864 deg`

Therefore the preregistered science classification is:

`K2_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071E`

This is a useful falsification result. Adding the present equalized `(r_W, Delta_slip)` direction does not generically restore mechanism specificity: the K2 known-sector control remains close to the GDM sound-speed-like direction while separating from the viscosity-like direction.

The result is not a finite-step accident. Non-classifying robustness diagnostics give:

- max joint K2 drift from bar1 across bar1..bar5: `0.1240131053 deg`
- max `r_W` drift: `0.1240061744 deg`
- max `Delta_slip` drift: `2.5334424085 deg`
- first two centered joint-family SVD variance fractions: `0.96588693696` and `0.03409734882`.

The Article-2 claim matrix has been updated to make this negative boundary explicit. The durable terminal summary is stored at:

`data/derived/exp071e_known_sector_joint_metric_direction_summary_v0_1.json`

## Why Article 3 stays at 40%

Exp073R1 v0.5 sequential whole-object reconstruction is still nonterminal at this checkpoint. Run `33175886694`, source-index job `98864259826`, remains in Stage A:

`Stream authoritative source object once and derive exact row-aligned zbin index`

No transport or reconstruction PASS is credited before terminal identity checks and artifact creation. Therefore no Article-3 percentage is added merely for active compute time.

The previous Range-GET diagnosis remains unchanged: random range transport is unusable on the tested NCSA path, including the 40,239,104-byte repeated probe. v0.5 is a transport/reconstruction contingency, not a science-gate relaxation.

## Gate state

- G7: **OPEN**
- G8: **OPEN**
- G9: **OPEN**

No covariance/whitening, nuisance quotient, G7 relation/null, fresh G8 family, or G9 claim is authorized by Exp071E or by a nonterminal v0.5 source stream.

## Next scientific target

Exp071E localizes the residual Article-2 ambiguity to K2 vs the GDM `cs2`-like direction in the present Weyl+slip geometry. The next useful specificity test is therefore not another scalar statistic. It should add an independent matter-response direction on the same frozen `(z,k)` support and test whether a three-channel matter+Weyl+slip direction separates K2 from both tested GDM axes under a preregistered, non-K2-tuned channel equalization.

Article 3 next action remains conditional on terminal v0.5 Stage A / full reconstruction state.
