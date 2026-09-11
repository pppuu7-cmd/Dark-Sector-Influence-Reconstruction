# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR or KMDSB.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_JM_ACTIVE_PARALLEL_TELEMETRY_V109.md`, creation commit `b6b0b5480a360f013aa0e550649641120af99d70`. Earlier notes remain immutable history.

## Scientific frontier
Recovered Exp073JL remains independently verified `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max canonical 2049->4097 relative difference `0.012273497268380687`, activating only Exp073JM. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting and lookup ceiling `1e-12` remain unchanged. Covariance restriction unauthorized; Wm_S3 unopened.

## Primary active run
Exactly one scientific-support run is authoritative: recovered Exp073JM 4097->8193, run/job `34548136827 / 103105092111`, head `ab9e29234781c94b80280aa0d7b16245a3e31804`, capacities 9216/262144, eight sequential role-major CLASS lifetimes/max-one-live and unchanged strict fourth-refinement classifier. All pre-compute gates passed; numerical execution remains active. Never duplicate or tune from partial responses.

## Pre-result terminal validator
Response-blind JM terminal validator `ci/exp073jm_terminal_result_validator_v0_1.py`, blob `8388199349d32a79e467bab940403570ddd3730e`, was frozen before JM result. Static run/job `34551348436 / 103114727756` independently passed 13 synthetic cases: exact `1e-3` is NOT_CONVERGED; invalid-row `0.05` and retained dimension `15` are inclusive; wrong grid/call/lifecycle/lookup/Wm receipts are rejected. Artifact `10180916352`, ZIP SHA256 `0f701f2311dec477d0939ed0a142366c00d35ff095c94c777c4994f8405c1581`; durable authority commit `b836f8d4a828144ba7802f49a15dc056ebdbd50f`.

Event-driven consumer `.github/workflows/exp073jm-terminal-auto-consumer-v0-1.yml`, corrected commit `a3a20b85ad574eea986d0273132774aaebd3908f`, is restricted to exact JM run/head and may only download/hash/validate/upload a terminal receipt. It cannot launch a downstream science branch.

## Parallel 16385 resource diagnostics
Dormant canonical 16385 decoded SHA256 `3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975`, text SHA256 `7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69`. Static resource contract and exact CLASS 18432/524288 build envelope PASS. 8193 and 16385 are not bitwise nested; response reuse is prohibited.

Two full hosted 16385 pilot attempts and all four first-generation single-role probes reached CLASS execution and were externally terminated by GitHub-hosted runner shutdowns. The beta_plus exit 143 is the same shutdown mode, not a CLASS/model failure. No 16385 resource PASS exists yet.

Active telemetry run `34551218708`, head `4132278b18fa8527a7c9ad8026119b8d35249b96`, executes four independent canonical-16385 single-role probes concurrently: alpha_minus `103114346998`, beta_minus `103114347191`, beta_plus `103114347209`, reference `103114347218`. Each passed build and is in execution with 10-second MemAvailable/RSS/VSZ/CPU telemetry. These jobs read no JM result and cannot create science authority.

Self-hosted full same-process 16385 pilot run `34550495778`, head `0eb93a45abe1d3431a1c6aa814108cb96aef5a28`, remains queued awaiting a repository self-hosted Linux/X64 runner.

## Pre-result branches
Both branches were frozen before JM verdict. CONVERGED -> only fresh canonical 4097->8193 Layer-B closure using the replacement dormant helper already independently static-audited (authority commit `42716d3a900ecac9cec6c1a77d3a1fd3bc02d1f6`). NOT_CONVERGED -> only canonical 8193->16385 next support rung after resource feasibility. Legacy Exp073JN is forbidden for post-JM closure.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** pending independently validated JM terminal science. Parallel/static/resource work remains `+0/+0`.

## Exact next action
Terminal-consume JM `34548136827` and telemetry `34551218708`. Independently verify JM artifact/validator receipt before branch activation. Analyze last memory telemetry before 16385 shutdown/success. No tolerance/grid/domain/mask/interpolation/estimator rescue; covariance restriction and Wm_S3 remain closed.
