# DSIR authoritative recovery — latest

Updated: 2026-09-13. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Repository state, immutable DSIR4 contracts/authorities, validated GitHub Actions artifacts and this file are the recovery source of truth. Older recovery notes remain immutable history and must not be used to reopen already superseded Layer-B work.

## Current scientific frontier

The active Layer-B question is no longer the old V146 16385->32769 recovery. Subsequent prospectively frozen diagnostics localized the remaining beta-response instability to exact-target response conditioning rather than common-grid interpolation alone.

Frozen scientific boundaries remain unchanged unless a later explicit authority says otherwise: production `h=1e-4`, native `k_per_decade_for_pk=20`, strict relative tolerance `<1e-3`, exact-target lookup mismatch `<=1e-12`. Covariance restriction remains unauthorized. `Wm_S3` remains unopened. No global 65537 calculation is authorized by the current diagnostic chain.

## V0.5 — h-dependence diagnostic terminal

Authoritative run: `34717972131`.

Classification: `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`, effect `+0/+0`.

On the 23 previously failing exact-target coordinates, 20/23 (`0.8695652173913043`) have raw five-h spread `>=1e-3`; failure median spread `0.003260200828240146`, failure max `0.0336066731` (terminal artifact authority contains full precision). Control max spread `0.00022411578499927006` remains below the frozen threshold. Exact-target binding mismatch is of order `1e-16`. Production `h` was not changed.

This authorized only a prospectively frozen finite-difference repair diagnostic, not covariance, `Wm_S3`, a science gate, or a denser global grid.

## V0.6 — fourth-order finite-difference repair terminal

Terminal authority: `docs/dsir4/authority/LAYERB_BETA_FD_REPAIR_V0_6.json`, creation commit `4b62f4bf4057d34eff2b7cc1ceef98d63f8eafa7`.

Science run: `34719180791`, head `614b1dd660dbc2dbe53fb5597dbfb2cc5df3a106`. Domain jobs D/B completed successfully and covered all 46 unique coordinates. The original decision job failed before scientific classification because its environment lacked numpy; this was infrastructure only.

Decision-only recovery reused the already-frozen D/B/invariant artifacts and the unchanged frozen executor/thresholds. Final recovery run `34719364652`, job `103622254478`, terminal PASS as infrastructure and produced the scientific decision.

Classification: `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`, effect `+0/+0`.

Frozen Richardson repair `D4(h)=(4*D2(h/2)-D2(h))/3` recovered only 4 of the 20 preregistered h-unstable failure coordinates, recovery fraction `0.2`, below the frozen partial-support threshold `0.25`. Failure median raw h-spread `0.003260200828240146`; median repaired local spread `0.003198104008657432`; max repaired local spread `0.033194530500212684`. Control max raw spread `0.00022411578499927006`; control max repaired local spread `0.00032007918985608384`. Exact-target mismatch max `1.2517848722592053e-16`; invariants PASS.

Interpretation: ordinary fourth-order centered finite-difference truncation error is not supported as the dominant cause of the h-dependent failure set. The only authorized successor is an upstream response-solver conditioning audit.

## V0.7 — upstream response-solver conditioning audit active

Prospectively frozen contract: `docs/dsir4/contracts/LAYERB_BETA_SOLVER_CONDITIONING_AUDIT_V0_7.json`, creation commit `0d8fa43eb93d4879bdc91aa59a3e8a3fb06314e5`.

Executor: `ci/layerb_beta_solver_conditioning_v0_7.py`, creation commit `234d64345674ddd2f4d9793d7315460e26efefa9`, Git blob `efdc1899a00f3c490f9dec1de030b671f36d4705`.

Workflow: `.github/workflows/layerb-beta-solver-conditioning-v0-7.yml`, creation commit `abb7faf9aadba1ed4e143a75dc9309627d6d06e5`.

Launch commit: `419e109429f77cb233a01b99e80c82d1c504e700`.

Active run: `34719555760`.

The audit has ten independent hosted science lanes: five prospectively frozen precision profiles crossed with domains D/B, `fail-fast:false`, max parallelism 10:
- `TOL10`: `tol_perturb_integration=3e-11`;
- `TOL100`: `tol_perturb_integration=3e-12`;
- `SAMP2`: `perturb_sampling_stepsize=0.000175`;
- `SAMP4`: `perturb_sampling_stepsize=0.0000875`;
- `JOINT100_S4`: both aggressive settings.

Production precision is `tol_perturb_integration=3e-10`, `perturb_sampling_stepsize=0.00035`. All profiles retain the same pinned CLASS source, exact target-k insertion, production `h=1e-4`, five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`, and strict `1e-3` response-stability threshold.

At the latest recovery write, invariant-audit is terminal PASS and all ten D/B profile jobs have been picked up by hosted runners; scientific result inspection is deferred until each relevant lane is terminal. Do not inspect partial numerical output to retune the frozen decision rule.

Frozen V0.7 decision rule in brief: strong support requires all invariants/controls PASS, JOINT recovery >=75%, median reduction >=4x, monotonic improvement on at least one frozen single-knob axis and no pathological joint interaction. Partial support requires JOINT recovery >=25% or median reduction >=2x. Otherwise solver-conditioning support is not established. Exact definitions in the contract are authoritative.

## Exact next order

1. Continue only run `34719555760`; do not launch duplicate V0.7 profile calculations.
2. Consume only terminal profile artifacts/logs and distinguish numerical/scientific failure from infrastructure failure.
3. Apply the already frozen decision job after all ten profile lanes and invariant-audit complete.
4. If the decision job fails technically before classification, repair only the infrastructure and reuse valid immutable profile artifacts; do not change thresholds/profiles/science.
5. Promote a durable V0.7 authority only after independently checking terminal provenance and the frozen classifier output.
6. Launch only the successor named by the frozen V0.7 classification: stabilized-solver local common-grid validation (strong), localized knob isolation (partial), response-parameterization/model-regularity audit (not supported), or no scientific promotion if inconclusive.
7. Keep covariance, whitening/nuisance/relation-null, `Wm_S3`, global 65537 and any science gate closed unless a later separately frozen authority explicitly opens them.

## Publication/readiness locks

The last repository readiness values remain unchanged by V0.5/V0.6 diagnostic narrowing alone: `ARTICLE3_REPOSITORY_READINESS: 68%`; funnel-freeze/scientific frontier `67%`. Do not increase them merely for compute volume or a negative diagnostic; only a frozen readiness rubric closure may change them.

Article-II real cross-family G5 ACT×unWISE closure remains a separate publication-readiness requirement and is not implied by the Layer-B Article-III diagnostics.

## Automation / ownership

`DSIR Continuous Research` is currently disabled. `DSIR Auto-Research Guard` is also disabled. The account currently has five other enabled research automations occupying the active automation slots (QGR, MSQGR, KMQGB, RQIR-CG, ISQGR). Do not disable one of those automatically merely to create a DSIR slot unless the user explicitly reprioritizes them.

GitHub run `34719555760` is the active DSIR Layer-B computation. Its profile lanes are GitHub-hosted diagnostics, not a new self-hosted DSIR-HOME-PC heavy run.
