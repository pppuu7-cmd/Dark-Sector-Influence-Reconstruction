# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_16385_REPRO_DIAGNOSTICS_V113.md`, creation commit `0b782e2e45c35d4abac7ce7b6faa9fb7c996f635`. V112 and all earlier recovery notes remain immutable history; V113 supersedes them for current-front recovery.

## Scientific frontier
Exp073JM canonical 4097->8193 remains independently verified `COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.01070806986822778` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` are unchanged. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Current authoritative process
Exactly one full canonical 8193->16385 scientific-support run remains active:
- workflow `post-jm-next-support-canonical-8193-to-16385-v0-1`;
- run/job `34555022975 / 103125734913`;
- head `c56940a0093fc6769b9a48cb3d5056b70075130c`;
- state at latest live check: `IN_PROGRESS` in `Execute frozen canonical 8193 to 16385 support refinement with telemetry` after all identity, stack, CAMB/CLASS-IV build and DES/Layer-A/BOSS input gates passed.

Do not duplicate this run or tune from partial output. The event-driven terminal consumer remains restricted to hashing/revalidation/receipt creation and cannot launch downstream science.

## Newly closed +0/+0 diagnostics
Durable combined authority: `docs/dsir4/authority/LAYERB_16385_REPRO_AND_NOISE_DIAGNOSTICS_V0_1.json`, creation commit `12aa3d29aef760b5bcf2ae50520e75d2e0b07781`.

- Cross-VM canonical-16385 reproducibility: run `34556173778`, compare job `103133339788`, artifact `10183110033`, ZIP SHA256 `169c5d03f5dceeba444c87f830a99d24ffeda845c65344db51f4a96a44309be1`. Sampled raw role operands differed only at ~`1e-15` symmetric relative; pilot derivative responses at at most `3.285358946556587e-11` symmetric relative. Classification `LAYERB_16385_CROSS_VM_NUMERIC_REPRO_DIAGNOSTIC_PASS_PLUS_0_PLUS_0`.
- Intra-VM role repeatability: source run `34557144684`; aggregate run/job/artifact `34557921258 / 103134458183 / 10183242971`, ZIP SHA256 `b063651e237ac5954cdcf95670c4cb913199c8ef8c70bebb71108c77dcb56eaf`. All four roles were bitwise repeatable, global differences exactly zero. Classification `LAYERB_16385_INTRA_VM_REPEATABILITY_AGGREGATE_DIAGNOSTIC_PASS_PLUS_0_PLUS_0`.
- Pre-result finite-difference/noise budget: run `34557228533`; artifacts `10182994471` and `10182995486`, ZIP SHA256 `cc9aa2908fa94b849c2edf51e241ca39786ae998bb3ce2aef8b6cf5ea8b208c7` / `c387ccb94f6ab62e606ab06db554c77efe59ab9963029f6df4e3760520d509c2`. Both are interpretation-only PASS +0/+0 and do not read the current 16385 science.

Joint interpretation: ordinary cross-VM nondeterminism is strongly disfavored as the dominant explanation for the historical ~1e-2 adjacent-grid plateau, because measured sampled operand variability is orders of magnitude smaller. Finite-difference conditioning at frozen `h=1e-4` can amplify larger structured raw discrepancies, so a structured grid-to-grid/solver mechanism remains plausible if the active frozen classifier is NOT_CONVERGED. None of these diagnostics changes the stopping rule or authorizes 32769.

## Closed resource/execution authorities retained
Canonical-8193 history-suppression exact-equivalence dual PASS: run `34551841749`, durable authority commit `600c5567f8fe3f42901e7034372b8e3849050eb0`.

Patched canonical-16385 resource dual PASS: run `34552645551`, jobs `103118559536` and `103118559274`, durable authority commit `b105e546dad7d114399e5cbfca229e6d4a33be4a`.

Frozen terminal validator: run `34554969959`, artifact `10182188577`, 13/13 synthetic PASS, durable authority commit `3e23fa7a686921f83c83a95d7383bb4581fbca83`. Exact `1e-3` is NOT_CONVERGED.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** pending independently validated terminal 8193->16385 science and a permitted downstream transition.

## Exact next action
Keep `34555022975` singular and terminal-consume its raw artifact plus validator receipt immediately on completion. If CONVERGED, activate only the prospectively frozen/static-audited fresh closure adapter. If NOT_CONVERGED, do not invent 32769; enter a separately frozen numerical plateau/root-cause decision stage using the response-blind diagnostics only as interpretation inputs. If infrastructure-invalid, repair only the first causal execution/provenance defect.
