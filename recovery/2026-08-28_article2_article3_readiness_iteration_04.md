# DSIR Article 2 / Article 3 readiness — iteration 04

**Date:** 2026-08-28

This checkpoint measures scientific readiness for writing the papers. It is not manuscript formatting/editorial completion.

## Readiness

| Article | Previous fixed point | Iteration 04 | Change |
|---|---:|---:|---:|
| Article 2 | 82% | **84%** | +2 pp |
| Article 3 | 40% | **40%** | 0 pp |

## Why Article 2 increased to 84%

Exp071F is now a completed prospectively frozen specificity control.

- preregistration file: `experiments/071f_k2_matter_weyl_slip_direction_control_prereg_v0_1.md`
- preregistration commit: `85daeca416ce8ed1e691008fd4178fd6bbf94d15`
- run: `33178154667`
- job: `98872091411`
- artifact: `9688506671`
- artifact ZIP SHA256: `e03e72251ab8ed9e0fa820bdae31342dc718349d78713db5fcac06bf00cc6779`
- execution conclusion: SUCCESS

Frozen primary rule: the three-channel K2 bar1 direction `(r_P,r_W,Delta_slip)` must be at least 45 degrees from **both** immutable GDM `cs2` and `cv2` local directions. Channel scales are determined only from the two GDM parents; K2 is forbidden from tuning the metric.

Terminal result:

- matter-only K2 bar1 vs GDM `cs2`: `19.223081503733017 deg`
- matter-only K2 bar1 vs GDM `cv2`: `19.037102938963482 deg`
- three-channel K2 bar1 vs GDM `cs2`: `19.07487721786906 deg`
- three-channel K2 bar1 vs GDM `cv2`: `50.16673498586107 deg`

Classification:

`K2_3CHANNEL_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071F`

The three-channel result is highly stable across the five finite K2 steps:

- max three-channel drift from bar1: `0.11693610730710657 deg`
- centered K2-family SVD variance fraction: first mode `0.9672058919`, first two modes cumulative `0.9999801012`.

### Scientific implication

The extra matter-power direction does not solve the residual K2↔GDM-`cs2` ambiguity. The angle changes only from the two-channel Exp071E value `18.9257 deg` to `19.0749 deg`, while the viscosity-like `cv2` direction remains separated (`50.1667 deg`).

Therefore the remaining ambiguity is not plausibly an artifact of omitting the matter-power direction from the metric block. It behaves as a local pressure/sound-speed-like response degeneracy. The next useful Article-2 discriminator should be qualitatively independent — growth/velocity/RSD-like if a common fail-closed provider can be constructed — rather than another correlated matter/metric coordinate.

Terminal evidence is persisted at:

`data/derived/exp071f_known_sector_matter_weyl_slip_direction_summary_v0_1.json`

The Article-2 claim matrix has been updated with A2-C12.

## Why Article 3 remains 40%

Exp073R1 v0.5 run `33175886694`, source-index job `98864259826`, remains nonterminal in Stage A:

`Stream authoritative source object once and derive exact row-aligned zbin index`

The v0.5 implementation uses:

- no HTTP Range requests;
- `Accept-Encoding: identity`;
- HTTP 200-only whole-object GET;
- expected `Content-Length = 2738626560` when supplied;
- socket/read timeout inherited from `urlopen(..., timeout=180)`;
- whole-object SHA256 requirement `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- exact row count `136930995`;
- progress output every 4,194,304 rows;
- outer Stage-A workflow timeout 100 minutes.

Because the job is still nonterminal and GitHub live-log retrieval currently does not expose a readable live blob, no transport PASS or failure is credited yet. The previous Range transport failure remains infrastructure-only, not a science result.

If Stage A terminates FAIL, the next route is identity-bound mirror/cache or another verified whole-object transport source; another random-Range retry is not justified. If it PASSes, the downstream 84,075,649,920-byte metacal whole-stream mapper may execute, but even a full reconstruction PASS is still a reconstruction prerequisite rather than G7.

## Gate state

- G7: **OPEN**
- G8: **OPEN**
- G9: **OPEN**

No covariance/whitening, nuisance quotient, frozen G7 relation/null, fresh G8 family, or G9 claim is authorized at this checkpoint.

## Next targets

Article 2: audit the existing growth/velocity/RSD machinery and determine whether K2 and the GDM `cs2/cv2` axes admit a common, same-grid, non-K2-tuned directional control. Only after that audit should a new preregistration be frozen.

Article 3: continue to use the terminal state of Exp073R1 v0.5 as the decision point for transport architecture; do not score active compute time.
