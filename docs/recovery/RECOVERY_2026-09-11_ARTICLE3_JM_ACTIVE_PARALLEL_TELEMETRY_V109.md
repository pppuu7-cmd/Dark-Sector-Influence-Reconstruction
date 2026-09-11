# DSIR Article III recovery — active JM with parallel 16385 telemetry V109

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR or KMDSB into this state.

## Preserved scientific frontier
Recovered Exp073JL remains independently verified `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, maximum canonical 2049->4097 relative component difference `0.012273497268380687`. This activates Exp073JM only. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, exact physical domain/masks/107-row accounting, request-plan identities and lookup ceiling `1e-12` remain unchanged. Covariance restriction remains unauthorized and Wm_S3 unopened.

## Primary authoritative scientific-support computation
Exactly one recovered Exp073JM canonical 4097->8193 run remains authoritative:
- workflow `exp073jm-article3-recovered-canonical-one-live-fourth-refinement-v0-2`;
- run/job `34548136827 / 103105092111`;
- head `ab9e29234781c94b80280aa0d7b16245a3e31804`;
- capacities 9216 / parser 262144;
- pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`;
- eight sequential role-major CLASS lifetimes, max one live;
- exact 441 coarse + 569 fine transfer calls per role, 4040 total;
- original strict fourth-refinement classifier unchanged.

All setup/build/input gates passed and the full execution step remains in progress at this recovery checkpoint. Do not duplicate this run and do not inspect partial scientific response values.

## Pre-result JM terminal validation is now frozen
A response-blind terminal validator was created before the JM result existed: `ci/exp073jm_terminal_result_validator_v0_1.py`, Git blob `8388199349d32a79e467bab940403570ddd3730e`, source creation commit `e3ea38cd93f1b845b6f4c9b4edc833e2eb83f0d9`.

Static audit run/job `34551348436 / 103114727756` independently verified 13 synthetic cases, including strict `1e-3` (equality is NOT_CONVERGED), inclusive Layer-B invalid-row bound `0.05`, inclusive retained-dimension bound `15`, and rejection of wrong grid/call/lifecycle/unsupported/lookup/Wm receipts. Artifact `10180916352`, ZIP SHA256 `0f701f2311dec477d0939ed0a142366c00d35ff095c94c777c4994f8405c1581`, static JSON SHA256 `669cebe98fcb3b16886632fd1717dd97f122007f5acdffc72336418f725535c2`. Durable authority commit `b836f8d4a828144ba7802f49a15dc056ebdbd50f`.

An event-driven consumer now exists at `.github/workflows/exp073jm-terminal-auto-consumer-v0-1.yml`, corrected guard commit `a3a20b85ad574eea986d0273132774aaebd3908f`. It is restricted to source run `34548136827`, source head `ab9e29234781c94b80280aa0d7b16245a3e31804`, exact validator/authority blobs, and source workflow success. It may download/hash/validate/upload a terminal validation receipt only. It cannot launch either downstream science branch.

## Canonical 16385 dormant next-rung diagnostics
Dormant canonical 16385 remains fixed at decoded SHA256 `3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975`, u64hex/text SHA256 `7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69`. Static resource contract and CLASS 18432/524288 build envelope passed. Canonical 8193 and 16385 are not bitwise nested, so response reuse is prohibited.

Two full hosted 16385 resource-pilot attempts and all four first-generation single-role probes reached CLASS execution but received external GitHub-hosted runner shutdown signals. The apparent beta_plus exit 143 is also an external shutdown, not a CLASS/model error. No valid 16385 resource PASS exists yet.

### Active parallel telemetry probes
Workflow `layerb-post-jm-16385-four-role-telemetry-probes-v0-1`, run `34551218708`, head `4132278b18fa8527a7c9ad8026119b8d35249b96`, runs four independent hosted single-role probes concurrently:
- alpha_minus job `103114346998`;
- beta_minus job `103114347191`;
- beta_plus job `103114347209`;
- reference job `103114347218`.

All four passed identity/install/build and entered CLASS execution. Each logs MemTotal/MemAvailable/free/cache/swap and top RSS/VSZ/CPU processes every 10 seconds. These jobs read no JM result, combine no cross-role operands and cannot activate a scientific branch. Their purpose is to distinguish real memory pressure from external hosted-runner termination.

A full same-process 16385 pilot on the repository self-hosted Linux/X64 runner is queued as run `34550495778`, head `0eb93a45abe1d3431a1c6aa814108cb96aef5a28`. It has not been assigned a runner at this checkpoint, so no self-hosted result exists.

## Pre-result branch preparation
Both post-JM branches were frozen before any JM verdict. CONVERGED permits only a fresh canonical 4097->8193 Layer-B science closure; NOT_CONVERGED permits only the canonical 8193->16385 support rung after its resource feasibility is established. Legacy Exp073JN is formally forbidden for post-JM closure.

A replacement dormant CONVERGED fresh-closure helper `ci/post_jm_converged_fresh_layerb_scientific_closure_v0_1.py` is response-blind and already independently static-audited. Its static authority commit is `42716d3a900ecac9cec6c1a77d3a1fd3bc02d1f6`. The dormant 8193->16385 support helper is also already generated and audited; no branch is active until validated JM terminal classification.

## Parallelization rule
Use as many independent hosted runners as useful for response-blind/static/resource/provenance/code-generation work. Do not parallelize solver lifetimes inside the active JM scientific-support comparison, and never combine raw finite-difference operands from separate processes when same-process/max-one-live is part of the frozen experiment.

## Stable readiness telemetry
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%**. Parallel diagnostics and static authorities are process/reproducibility `+0/+0`; only independently validated JM science may move the frontier.

## Exact next action
1. Terminal-consume JM run `34548136827`; if successful, independently verify its artifact and the event-driven validator receipt before branch activation.
2. Terminal-consume telemetry run `34551218708`; inspect the last memory/RSS telemetry immediately before any shutdown to classify the 16385 hosted limitation.
3. If JM is CONVERGED, run only the already frozen fresh 4097->8193 Layer-B closure. If JM is NOT_CONVERGED, continue only 8193->16385 after resource feasibility is solved. Infrastructure failure activates neither branch.
4. No tolerance/grid/domain/mask/interpolation/estimator rescue. Covariance restriction and Wm_S3 remain closed.
