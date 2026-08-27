# DSIR recovery checkpoint — Exp072C result + Exp073A preregistration — 2026-08-27

## Current verified result

Exp072C completed as

`DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_FOUND_EXP072C`.

Immutable provenance:

- merge `b442cddd6ba032d1261a0994bc1c4f5cf899a9f7`;
- run `33031427090`;
- job `98384598473`;
- artifact `9630407069`;
- artifact digest `sha256:0e726d9f12b2b8951a4d2598b3723d54db1a14c09070d8e8770d5256773f2a71`;
- extracted JSON SHA256 `d0d8e6a19177f4a7b94d2f0b95d6fee3b5cd85078e8eadee06e7f0faaf5864c0`;
- all C1–C8 PASS.

Unique nondominated frontier:

- `z_min = 0.0087345857837422`;
- `k_max = 4.818261097432861 Mpc^-1`;
- route dimension = 15;
- Blue `gg=1,kg=4`;
- Green `gg=3,kg=7`.

Exp072A remains permanent scientific FAIL. Exp072B remains `DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B`.

## New persistent operating rule

`docs/RESEARCH_ITERATION_REPOSITORY_SYNC_POLICY_2026-08-27.md` records the owner requirement that the repository be brought up to date after every research iteration, including preregistration, immutable result provenance/classification, checkpoint, gate state and next admissible step where applicable.

## Current preregistered next experiment

`experiments/073a_gr_linear_perturbativity_eligibility_prereg_v0_1.md`

is frozen before any Exp073A perturbativity output.

Primary question: after imposing the unique Exp072C support rectangle, does the current linear/no-CLEFT ACT×unWISE route remain viable when cells with

`Delta2_m = k^3 P_mm^lin/(2*pi^2) > 1`

in the exact pinned GR CAMB reference are treated as physically ineligible?

Frozen primary rules:

- same Exp072C positive operator geometry;
- same full pair denominators;
- same 5% combined invalid-support threshold;
- same 26 coordinates / 64 coordinate-block pairs;
- same minimum route `>=15` plus Blue/Green gg/kg coverage;
- primary perturbativity threshold `Delta2_m<=1`;
- diagnostic only `Delta2_m<=0.5` and `<=2`;
- exact CAMB pin `fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- linear `delta_nonu x delta_nonu`, physical units, no extrapolation, no nonlinear corrections;
- exact unit-roundtrip control at `2e-8`;
- no covariance/nuisance/G7/G8/C3-extension/C5-extension input.

Allowed completed classifications:

- `ELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`;
- `INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`;
- `FAIL_EXP073A_REPRODUCTION_OR_PROVENANCE`.

Infrastructure-only interruption remains `INCOMPLETE_EXP073A` by interpretation.

## Next continuation

1. Merge this result/preregistration checkpoint to `main`.
2. Only then implement Exp073A.
3. Execute the frozen workflow and preserve its classification.
4. Update the repository immediately after that iteration with result provenance and the next preregistered step.
5. Do not extend C3/C5 providers to the Exp072C frontier unless Exp073A and a later prospective provider-certification path authorize it.

G7/G8/G9 remain OPEN.
