# DSIR recovery V111 — canonical 8193→16385 support active

Date: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR or KMDSB.

## Scientific frontier
Exp073JM is independently verified `COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0` on canonical 4097→8193 with max relative component difference `0.01070806986822778`, 10.70806986822778× the frozen strict tolerance `1e-3`. Parent/support accounting remains clean: 107 retained, invalid fraction 0, unsupported target evaluations 0, 8 sequential solver constructions, max one live, 4040 transfer calls. Durable JM authority: `docs/dsir4/authority/EXP073JM_ARTICLE3_RECOVERED_CANONICAL_ONE_LIVE_FOURTH_REFINEMENT_NOT_CONVERGED_V0_2.json`, creation commit `24b55a087b3bc81c406978511e9ad47c90431a27`.

Frozen science remains unchanged: `REL_TOL=1e-3` with strict `<`; `h=1e-4`; native kpd20; centered-cubic interpolation; exact physical domain/masks/107-row accounting; lookup ceiling `1e-12`; covariance restriction unauthorized; Wm_S3 closed.

## 16385 memory/resource recovery closed
Unpatched canonical-16385 CLASS-IV runs exhaust GitHub-hosted memory because `k_output_values` activates full perturbation-history storage. A minimal execution-only patch changes exactly one callback assignment in pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`: `perhaps_print_variables = perturb_print_variables;` -> `perhaps_print_variables = NULL;`. Canonical k insertion remains active and scientific parameters are unchanged.

Two independent canonical-8193 equivalence replicas, run `34551841749`, reproduced all eight raw operand SHA and both pilot-response SHA exactly against the old authoritative JO while reducing peak RSS to about 4.54 GB. The exact patch blob is `e20687e933d665973c3be40598180587701fa8e0`.

Two independent patched canonical-16385 resource replicas, run `34552645551`, jobs `103118559536` and `103118559274`, both PASS the resource gate with four constructions/max-one-live/final-live-zero, unsupported=0 and lookup `1.657034302538322e-16`. Their peak RSS values are 8,975,032 kB and 9,231,552 kB. Resource artifact IDs/digests are `10181859106 / 1c1eb4fa591eb5d868aacdd7c7885f4780015b671942a6727ffc343eb26515e7` and `10181735051 / 8c18af5e4f022600764153dde74cd52bbf0ca75a2b21e5d21ae355851289b4c2`.

Their resource-pilot response hashes differ across hosted VMs and are explicitly **not scientific evidence**. Durable resource authority `docs/dsir4/authority/CLASSIV_HISTORY_SUPPRESSED_16385_DUAL_RESOURCE_PILOT_V0_1.json`, creation commit `b105e546dad7d114399e5cbfca229e6d4a33be4a`, permits only a fresh full 8193→16385 support computation in one process.

## Pre-result terminal interpretation frozen
Validator `ci/post_jm_next_support_terminal_validator_v0_1.py`, blob `d8eece64d6b2b7ab162fc3a4e6a9981bde604e08`, was frozen before the full 8193→16385 result. Static synthetic run `34554969959` independently passed 13/13 cases. Artifact `10182188577`, ZIP SHA256 `cfe031d5b2b389ae6f933d3285af2b878ff4cd5c69645f80b9c9d85c6cadf4f0`, `static.json` SHA256 `66e730683bc88be80afff4588f8b1417f48f5c3fd53229466630ebc6962912f2`. Durable authority commit `3e23fa7a686921f83c83a95d7383bb4581fbca83`. Exact `1e-3` is NOT_CONVERGED; `<1e-3` is CONVERGED; invalid fraction 0.05 and retained 15 are inclusive boundaries.

## Active scientific-support run
Exactly one authoritative full canonical 8193→16385 support run is active: workflow `post-jm-next-support-canonical-8193-to-16385-v0-1`, run/job `34555022975 / 103125734913`, launch/head commit `c56940a0093fc6769b9a48cb3d5056b70075130c`. It guards all authorities, uses canonical 8193 and 16385 node payloads, exact request-plan hashes, eight sequential one-live solver lifetimes, pinned CAMB/CLASS-IV, capacity 18432/parser 524288, and the proven history-suppression patch. It must recompute fresh operands and then apply the frozen terminal validator. Do not duplicate it and do not inspect partial scientific response values for tuning.

Event-driven terminal consumer `.github/workflows/post-jm-next-support-terminal-auto-consumer-v0-1.yml`, creation commit `1abaac0e88b66af4cea2496b79f2f87a9ac84dea`, is restricted to exact source run `34555022975` and exact source head. On source success it downloads/hash-verifies the terminal artifact and re-runs the frozen validator. It cannot launch downstream science.

## Outcome preparation
Repository search found no prospectively frozen 32769 successor. Do not invent one after a NOT_CONVERGED result. A previously frozen dormant fresh-closure helper exists for direct `JM CONVERGED`, but its activation token is specifically the fourth-refinement JM token and therefore it cannot automatically consume a future `COMMON_GRID_NEXT_REFINEMENT_CONVERGED_PLUS_0_PLUS_0` result without a separate prospective compatibility/activation audit and adapter. Prepare only response-blind/static compatibility work while the 8193→16385 run is active.

## Descriptive convergence context — interpretation only
Validated maxima are `0.037280144773915974 → 0.016330535730270664 → 0.012273497268380687 → 0.01070806986822778`. Effective reduction order weakens strongly; latest three-point Aitken estimate is near `0.00972`, around 9.7× tolerance. This is descriptive evidence consistent with a plateau but is not a classifier and may not alter the frozen 8193→16385 decision.

## Readiness
`ARTICLE3_REPOSITORY_READINESS = 68%` and funnel-freeze readiness `=67%` until the current canonical 8193→16385 result is independently validated and an allowed downstream transition is established.

## Exact next action
1. Keep run `34555022975` singular and active; consume only its terminal artifact.
2. Independently verify the event-driven consumer receipt against the pre-result validator authority.
3. In parallel, finish response-blind/static outcome-compatibility audits that cannot depend on partial science.
4. If terminal classification is CONVERGED, prospectively bind a fresh closure implementation to the new next-refinement authority before any closure science.
5. If terminal classification is NOT_CONVERGED, do not invent a 32769 rescue. Perform the already response-blind numerical-plateau/root-cause decision audit or freeze a new hypothesis only prospectively with independent scientific justification.
