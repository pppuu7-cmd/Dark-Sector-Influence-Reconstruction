# DSIR Article III recovery — request-plan packaging repaired, recovered JL retry active V102

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved science
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; Exp073JI support feasible; Exp073JJ/JK support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`. Recovered Exp073JL v0.2 preserves the prospectively frozen original third-refinement science exactly: canonical 2049->4097, strict `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, same physical domain/masks/107-row traversal/accounting, GL64 direct comparison and fine-only GL128 dense-z control. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Attempt 1 terminal classification — infrastructure only
Recovered JL run/job `34542500814 / 103087994556`, head `f672c41aba5cf32fad006705647e8118915fe54d`, passed workflow identity, stack, CAMB, CLASS build/patch, DES, Layer-A/angular/Exp073IM and BOSS gates. The frozen helper then stopped at its pre-solver durable request-plan authority validation with `INVALID_INFRA_PLUS_0_PLUS_0` / `RuntimeError: invalid response-blind plan authority` before the first CLASS construction.

Artifact `10177843001` was independently consumed: ZIP SHA256 `4b6dd852cc927b3266e60ce0406373900be3136c2d8445e217b87003e1c7ae67`; `result.json` SHA256 `05650c874fda789ed80799bc668b130c0900fa06c8e511b72f33d72a02bb7b98`; `capacity_patch.json` SHA256 `e1af249ccdfd393b9b0f1020ffa1b70d953fa457ca2212aa3ab29be01f74b66a`. No scientific response was read and no scientific terminal classification was created. Durable attempt authority: `docs/dsir4/authority/EXP073JL_RECOVERED_V0_2_ATTEMPT1_INVALID_INFRA_AUTHORITY_V0_1.json`, creation commit `34d322281b961a3e92b63364b6a61b3611f1d8cd`.

## Root cause and lossless packaging repair
The independently verified source request-plan artifact from run/job `34541423516 / 103084699643`, artifact `10177436665`, contains a BOSS object with exact values `retained_rows=54`, `target_scalar_count_per_request=297`, `gl64_z_count=64`, `gl128_z_count_fine_only=128`. The first durable authority transcription V0.1 accidentally omitted that object (and the explicit `class_solver_invoked=false` receipt), causing the recovered JL helper to fail closed before science.

A new immutable packaging-only authority was created rather than rewriting V0.1 history: `docs/dsir4/authority/RECOVERED_EXP073JL_RESPONSE_BLIND_REQUEST_PLAN_V0_2.json`, creation commit `1a82920b717411f23b3b1994164e08843374211c`, Git blob `5992faa10b6d25d1503b287c19456fb36756caa4`. It restores the exact source-artifact BOSS object and `class_solver_invoked=false` while leaving all plan/science values unchanged.

A dedicated no-science packaging regression then re-downloaded the original artifact and exact-compared the durable V0.2 transcription. Run/job `34544077209 / 103092804354`, head `b49d13ab5880f4d89f286a6e0f98713ff2d80d5d`, completed SUCCESS. Artifact `10178350773`; independently verified ZIP SHA256 `4db74cb7ad6a2247e6ac762201f720f826d736de5db754612ddbbc819da31ba8`; `packaging_audit.json` SHA256 `12fe87319459f4aa978fce03f24e4e6b5a0d1eb20e86e56e8c676722e29c96dd`. Classification `REQUEST_PLAN_AUTHORITY_V0_2_LOSSLESS_TRANSCRIPTION_PASS_PLUS_0_PLUS_0`; 18 exact source fields compared, BOSS restored, no CLASS invocation and no scientific response read. Durable audit authority: `docs/dsir4/authority/RECOVERED_EXP073JL_REQUEST_PLAN_AUTHORITY_PACKAGING_AUDIT_V0_1.json`, creation commit `323fe24085bf553570397034f853cff053250f14`.

## Retry workflow — process-only change
Immediately before retry, repository Actions checks returned zero queued and zero in-progress runs. Workflow-only repair commit `417ec30eb0acd2896068f7ed3d5eeb3d47cedbbf` changes only the durable request-plan authority input from V0.1 to independently verified V0.2 and adds the packaging-audit PASS as an explicit prerequisite/identity guard. Frozen helper blob `5f8475b961db20bef5f4b8a2eb7c99d9f7c722e2`, prereg blob `a6ba32cb5b9ebe73bd6e3cd03a22d3f51f8aa2ca`, canonical grids, CLASS commit/patches, `h`, `REL_TOL`, native kpd20, estimator, masks, physical domain and 107-row traversal are unchanged.

Current authoritative process:
- workflow `exp073jl-article3-canonical-one-live-recovered-third-refinement-v0-2`;
- retry run/job `34544293038 / 103093458667`;
- head `417ec30eb0acd2896068f7ed3d5eeb3d47cedbbf`;
- GitHub-hosted Ubuntu 24.04, no self-hosted ownership;
- timeout 110 minutes;
- authority/identity gate PASS;
- frozen numerical/build stack PASS;
- latest V102 observed step: exact frozen CAMB checkout/install in progress.

No partial JL scientific values may be used for tuning or branch choice. This is the only authorized heavy recovered-JL process.

## Downstream response-blind preparation status
The already-frozen JM non-convergence branch has a known activation-alignment defect: its current helper adds two activation predicates not present in its preregistration, so JM is not execution-ready until a prereg-alignment-only repair/regression is made if JL ultimately returns verified NOT_CONVERGED.

The already-frozen JN convergence branch preregistration remains valid in intent, but its current helper still expects the historical JL authority shape and historical regenerated/multi-live response architecture. If JL ultimately returns verified CONVERGED, JN must first receive a response-blind recovered-authority/canonical-one-live implementation alignment without changing its frozen scientific contract.

Neither branch is selected before the JL terminal verdict.

## Stable readiness telemetry
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** while recovered JL remains unresolved. Attempt1 infra failure, packaging repair and retry launch are process work only and do not change scientific readiness.

## Exact next action
Do not duplicate retry `34544293038 / 103093458667`. While it runs, perform only response-blind independent downstream/static preparation. On terminal completion, consume the artifact and independently verify ZIP/result/capacity hashes, canonical grids, live request-plan receipt, exactly 8 constructions/max one live, 4040 transfer calls, unsupported=0, lookup<=1e-12, parent identity/107-row accounting and frozen terminal classifier. Only independently verified `COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0` or `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0` may move the scientific frontier or select JN/JM. `INVALID_INFRA_PLUS_0_PLUS_0` activates neither. No science rescue.
