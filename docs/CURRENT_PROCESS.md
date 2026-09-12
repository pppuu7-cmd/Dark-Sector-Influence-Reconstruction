# DSIR current-process ledger

Updated: 2026-09-13. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Active frontier — Layer-B beta solver conditioning V0.7

The authoritative active Layer-B run is GitHub Actions `34719555760`, launched by commit `419e109429f77cb233a01b99e80c82d1c504e700` from prospectively frozen contract `docs/dsir4/contracts/LAYERB_BETA_SOLVER_CONDITIONING_AUDIT_V0_7.json` (creation commit `0d8fa43eb93d4879bdc91aa59a3e8a3fb06314e5`).

V0.7 tests whether the h-dependent exact-target beta-response instability is materially reduced by upstream CLASS perturbation-solver precision rather than by ordinary finite-difference truncation. Five frozen precision profiles are crossed with D/B domains for ten independent hosted science jobs with `fail-fast:false` and max parallelism 10.

Frozen profiles: `TOL10` (`tol_perturb_integration=3e-11`), `TOL100` (`3e-12`), `SAMP2` (`perturb_sampling_stepsize=0.000175`), `SAMP4` (`0.0000875`), and `JOINT100_S4` (both aggressive settings). Production remains `3e-10` / `0.00035`.

Frozen science remains production `h=1e-4`, five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`, native kpd20, exact target-k insertion, strict relative tolerance `<1e-3`, exact target mismatch `<=1e-12`, same 46 probe/control coordinates. No global 65537, covariance, whitening/nuisance/relation-null, `Wm_S3` or science gate is authorized.

At the latest update, invariant-audit is terminal PASS and all ten profile/domain jobs have been picked up by hosted runners. Do not inspect partial science output. Consume only terminal artifacts and apply the pre-registered decision after the full barrier.

## Closed parent — V0.6 finite-difference repair NOT SUPPORTED

Authority: `docs/dsir4/authority/LAYERB_BETA_FD_REPAIR_V0_6.json`, commit `4b62f4bf4057d34eff2b7cc1ceef98d63f8eafa7`.

Science run `34719180791` successfully generated all D/B domain data. Its original decision step had an infrastructure-only missing-numpy failure. Decision-only recovery preserved immutable domain artifacts and the frozen executor/criteria; recovery run `34719364652`, job `103622254478`, then completed.

Terminal classification: `FOURTH_ORDER_FD_REPAIR_NOT_SUPPORTED`, effect `+0/+0`.

The preregistered fourth-order Richardson repair recovered 4/20 h-unstable parent failure coordinates (`0.2`), below the frozen partial-support threshold `0.25`. Failure median raw spread `0.003260200828240146`; median repaired local spread `0.003198104008657432`; failure max repaired local spread `0.033194530500212684`; control max repaired local spread `0.00032007918985608384`; exact-target mismatch max `1.2517848722592053e-16`; invariants PASS. Production h unchanged.

This negative diagnostic is a scientific/numerical result: ordinary centered finite-difference truncation is not supported as the dominant source of the instability. It authorized only V0.7 upstream response-solver conditioning.

## Closed parent — V0.5 h-dependence strongly supported

Run `34717972131` classified `H_DEPENDENT_CONDITIONING_STRONGLY_SUPPORTED`, effect `+0/+0`: exactly 20/23 failing exact-target coordinates have five-h spread `>=1e-3`, while control max spread is `0.00022411578499927006`. This is the frozen 20-coordinate parent-unstable subset reused by V0.6/V0.7.

## V0.7 frozen decision barrier

Strong solver-conditioning support requires: all invariants and controls PASS in all profiles, `JOINT100_S4` recovery >=75% of the frozen 20-coordinate subset, median h-spread reduction >=4x, monotonic improvement on at least one frozen single-knob axis, and non-pathological joint interaction.

Partial support requires all invariants PASS and either JOINT recovery >=25% or median reduction >=2x. If neither holds, the classifier returns not-supported. Invariant/control/keyset failures or preregistered pathological profile interaction produce inconclusive. The exact JSON contract is authoritative; do not reinterpret after seeing results.

## Next actions after the full V0.7 barrier

- `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_STRONGLY_SUPPORTED` -> prospectively freeze a stabilized-solver-profile local common-grid validation.
- `...PARTIALLY_SUPPORTED` -> prospectively freeze localized solver-knob isolation.
- `...NOT_SUPPORTED` -> prospectively freeze a response-parameterization/model-regularity audit.
- `SOLVER_CONDITIONING_AUDIT_INCONCLUSIVE` -> no scientific promotion; diagnose only the failed invariant/profile interaction prospectively.

No branch above directly opens covariance or `Wm_S3`.

## Anti-duplication / runner ownership

Do not launch another V0.7 profile run while `34719555760` is queued/in-progress. Ten hosted profile/domain lanes already provide the intended parallelism. They are not a self-hosted/home heavy-science run.

If a V0.7 lane fails technically, diagnose the first causal failure and repair the smallest infrastructure defect without changing the frozen profiles, h ladder, target coordinates or decision thresholds. Reuse valid immutable artifacts whenever possible instead of recomputing expensive domains.

## Recovery/readiness

`docs/RECOVERY_LATEST.md` was refreshed by commit `cf25d621ebf20c963b530e8d3a83882c9b4510d1` to point at V0.6/V0.7 rather than the superseded V146 active state.

Last frozen repository-readiness values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; diagnostic compute volume alone does not change them.

## Automation

`DSIR Continuous Research` and `DSIR Auto-Research Guard` are disabled. Five other enabled research automations currently occupy the active automation slots: QGR, MSQGR, KMQGB, RQIR-CG, and ISQGR. Do not silently disable another project to free a slot; explicit reprioritization is required.
