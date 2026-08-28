# DSIR Article 2 / Article 3 readiness — iteration 06

**Date:** 2026-08-28

Percentages follow the frozen iteration-01 scoring rule and measure repository readiness for a complete defensible article draft. They are not publication probabilities and do not pre-judge open gates.

## Readiness

| Article | Iteration 05 | Iteration 06 | Change |
|---|---:|---:|---:|
| Article 2 | 86% | **88%** | +2 pp |
| Article 3 | 44% | **44%** | 0 pp |

## Article 2 — Exp071I closes a theory-velocity provider/specificity step

Exp071I was motivated by Exp071H but tests a genuinely different channel. Exp071H is a finite-bin temporal derivative of the matter-power response; Exp071I uses a source-audited, same-definition CLASS total-velocity transfer `t_tot`.

### Preregistration chronology

1. Original Exp071I preregistration: `30797f97f9ee4d295dcaf1905d3647230b6fa1cc`.
2. Before any Exp071I spectrum or statistic existed, parser audit established that `mTk` activates density transfers while `vTk` independently activates velocity transfers in both pinned solver branches.
3. A pre-execution I/O amendment was therefore committed as `55ea3d6435767ecf570702b55d411a12eddd59b4`.
4. The amendment changed only the requested solver output to `mPk,mTk,vTk`; it did not change any physical parameter, grid, primary observable, primary K2 point or 45-degree science separator.
5. Evaluator commit: `2858ec8c97111c02b140d86925343d7e4b603094`.
6. Workflow commit: `2951fa4b4a487dac75bea60d87e89346dd6b9ac5`.
7. First execution trigger: `49996b5053b6b15428a2ff936efb4fd21fac266c`.

### Exact execution provenance

- run: `33181895623`
- job: `98884913088`
- conclusion: SUCCESS
- artifact: `9690064470`
- artifact ZIP SHA256: `ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14`
- terminal repository summary: `data/derived/exp071i_k2_gdm_total_velocity_direction_summary_v0_1.json`
- source-level contract: `docs/ARTICLE2_TOTAL_VELOCITY_PROVIDER_CONTRACT_2026-08-28.md`

Pinned solvers:

- official CLASS `e85808324f51fc694d12e3ed7439552a3c3f9540`
- GDM_CLASS `4c87916aab5ca124a68f1dd16f31846fc13d1829`

Immutable parent binding:

- K2 run `33020201997`, artifact `9626235928`, digest `sha256:ed486effa593a409640577f8cdde614d5fddfc95653eb4ca78c56ae69a234e5e`
- GDM run `32774198185`, artifact `9537340616`, digest `sha256:1d8f5b8d3b31df45256daaf3b1a8071534e63518f0a56d77ddd56ed44f2a7eff`

### Reproduction integrity

The fresh `vTk`-enabled calculations reproduce the immutable parent matter-power spectra exactly at stored precision:

- K2 maximum relative difference: `0.0`
- GDM maximum relative difference: `0.0`
- preregistered integrity limit: `1e-10`

Thus the new result cannot be attributed to a changed cosmology or solver trajectory induced by the output extension.

### Primary science result

Observable:

`r_ttot = ln(abs(t_tot_model/t_tot_ref))`.

Primary K2 point: bar1.

Frozen 45-degree separator:

- K2 bar1 vs GDM `cs2=1e-7`: **165.945494 deg**
- K2 bar1 vs GDM `cv2=1e-7`: **164.711329 deg**

Classification:

`K2_TOTAL_VELOCITY_SEPARATED_FROM_BOTH_GDM_AXES_EXP071I`

Additional frozen/non-classifying diagnostics:

- GDM `cs2` vs `cv2` total-velocity angle: **2.368251 deg**
- maximum K2 bar1→bar2-5 total-velocity drift: **0.128423 deg**
- common baryon-transfer sensitivity: K2 vs `cs2` **80.993286 deg**, K2 vs `cv2` **76.225446 deg**
- all 35 sampled nodes preserve transfer sign and pass the denominator floor.

### Article-2 implication

The K2↔GDM similarity found in selected static matter/metric coordinates is not a full response equivalence. Two independent evolution-sensitive constructions now separate the same K2 direction from both GDM directions:

- Exp071H finite-bin temporal matter response: ~137–138 degrees;
- Exp071I same-definition total-velocity transfer response: ~165 degrees.

This supports a stronger but still channel-conditioned statement: **static response similarity can coexist with qualitatively different temporal and velocity response geometry.**

It does not establish tracer RSD, `f sigma_8`, survey distinguishability or unique microscopic identification.

## Article 3 — unchanged at 44%

Exp073R1 v0.5 Stage A remains the only newly completed part of the 20-point exact-reproduction prerequisite. The downstream `metacal-map` job is still executing the authoritative 84,075,649,920-byte object through sequential no-Range transport.

No readiness credit is assigned for active compute time.

- G7: OPEN
- G8: OPEN
- G9: OPEN
- covariance: NOT AUTHORIZED
- nuisance quotient: NOT AUTHORIZED

## Next falsification step

The large Exp071I oriented angles could in principle be driven primarily by a scale-independent velocity-response amplitude. The next admissible Article-2 test should therefore remove the per-redshift constant-in-k mode **after** freezing the projection rule, and ask whether K2 remains separated from both GDM axes in velocity-shape space. This must be preregistered as a follow-up motivated by Exp071I and must not retroactively alter Exp071I.
