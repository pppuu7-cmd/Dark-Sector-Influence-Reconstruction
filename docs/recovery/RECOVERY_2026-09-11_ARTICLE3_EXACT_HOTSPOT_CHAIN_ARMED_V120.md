# DSIR authoritative recovery V120 — exact-hotspot active, fail-closed chain armed

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR.

## Scientific frontier
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. No 32769 execution is authorized; covariance restriction remains unauthorized; Wm_S3 remains unopened.

Broad localization is closed and support-only: raw max `1.5949311416969764e-10`, response max `0.00016265101390432733`, full plateau/broad response ratio about `76.75366`. Broad demonstrates response-construction amplification but does not reproduce the full plateau.

## Active heavy owner
Exact response-atom hotspot run/job `34592951737 / 103242180883`, head `5f202de811c07c020100055a63391b7225358670`, remains **IN_PROGRESS** in the frozen 441-call numerical execution. All prerequisite identity/build/data stages are PASS. It compares canonical 8193 vs 16385 on exactly 377 DES + 64 BOSS GL64 shared calls, 8 total role-major CLASS constructions, max one live, unchanged h/grid/interpolation. Do not inspect partial response and do not duplicate this heavy run.

## Exact-hotspot terminal validation already frozen
Exact-hotspot terminal validator blob `af90fc027ab25deab640cf88ca6ed07a70423f25` and its corrected static authority remain PASS 22/22. Armed `layerb-post-16385-exact-hotspot-terminal-consumer-v0-1` consumes only successful fixed source head `5f202de...`, requires full plateau reproduction within relative `1e-12`, and cannot launch science.

## Conditional top-1 cancellation decomposition
Preregistered deterministic follow-up remains `docs/dsir4/prereg/LAYERB_POST_16385_TOP1_ROLE_CANCELLATION_DECOMPOSITION_V0_1.md`, prereg blob `a75eccff06c410646c5a813f288a6cf78cb11577`, helper blob `76624d9a4b59d6e1ead02e22ead774135a799bbc`. Selection is exactly `source_result.top_64_response_atoms[0]`; no human/result-driven hotspot selection is allowed. Helper static authority is independently verified 18/18 PASS, durable authority commit `029db882c1d4162734c83f6086e413df84920877`.

GitHub-native conditional chain `.github/workflows/layerb-post-16385-top1-role-cancellation-chain-v0-1.yml` was created at commit `83da68f162f0677884ae485ad978b9e746b49c7f`, blob `8397a83527de93d53ec4077e04f998ff4bb1a537`. It can start only after successful exact-hotspot terminal-consumer completion, downloads fixed source run `34592951737`, revalidates exact PASS/441/377/64/lifecycle/plateau/downstream gates, then executes only the prospectively frozen top-1 decomposition. Chain static audit run/job/artifact `34600969744 / 103267891901 / 10264306857` is independently verified 20/20 PASS; ZIP SHA256 `c7e9686947399c318c766e66b8318668c368f1476670adf688abfe5d87b720a0`, static JSON SHA256 `d8e8d3f7825dbee1eacdb302cb00f5e8496075f9c8c5af7e73317dd052447d55`. Durable chain authority commit `723a92cec2a47a5fde5ef69008544cd1b5923b4a`.

## Decomposition terminal validation frozen before result
Terminal validator `ci/layerb_post_16385_top1_role_cancellation_terminal_validator_v0_1.py` was created at commit `ddbf3f639b67f761cf70b56d524c2e5544390851`, blob `af20444b44137e03a7b778835dc97305b8004769`, before any decomposition result exists. It requires deterministic selected-atom identity, two-lattice/four-role receipts, lifecycle 8/max1/final0, exact CLASS/capacity/history receipts, and primary-component reproduction of the source hotspot within relative `1e-12`.

Validator static audit run/job/artifact `34601271942 / 103268888189 / 10263469839` is independently verified 29/29 PASS; ZIP SHA256 `15b5d438b7b8802da0616a6ff131825381fea7aefab9a59f97c63cd662fbb07d`, static JSON SHA256 `cb664ed5af4d6f72646e5035bc4cba5b56636561d285b3cb2f20dcf0979271f1`. Durable static authority commit `ee9e27d73a7124f0ca4b8cef95432c491903002c`.

Armed terminal consumer `.github/workflows/layerb-post-16385-top1-role-cancellation-terminal-consumer-v0-1.yml` was created at commit `83dfd5072f7d92e6a25501e1824a6ebf2fa91709`, blob `11410edc681ee495d17614977d7aef1514620c46`. It can run only after successful decomposition-chain completion, downloads fixed source run `34592951737` plus the event decomposition artifact, runs the frozen terminal validator, requires PASS, and launches no successor science. Consumer static audit run/job/artifact `34601472047 / 103269550987 / 10264132832` is independently verified 18/18 PASS; ZIP SHA256 `a09203cc26a870ab995e13c762c7956f743ec9fc1e6c10639c1d4f431f57e613`, static JSON SHA256 `290a149c0ab4c361f56ea450a233504a80b219ae74d5d7a48949b856b3943faf`. Durable consumer static authority commit `5004a2efc44965d26f22efa1359a32670e2d1098`.

## Fail-closed chain state
The complete pre-result chain is now armed:
`exact-hotspot source -> exact-hotspot terminal validation -> deterministic top-1 four-role cancellation decomposition -> decomposition terminal validation`.
Each successor requires the prior workflow to conclude success and repeats frozen machine gates. No step authorizes 32769, covariance restriction, Wm_S3, or a new scientific classification. Any provenance mismatch or infrastructure failure stops the chain.

## Runner ownership
The only useful active heavy DSIR process is `34592951737 / 103242180883`. Do not duplicate it. Stale self-hosted `34550495778 / 103112190909` remains superseded and must not receive ownership. Independent static/control-plane work is already closed through the decomposition terminal-consumer.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%**. Control-plane readiness improved, but the stable scientific rubric does not move until a frozen scientific/support gate closes.

## Exact next action
1. Query `34592951737 / 103242180883`; do not inspect partial numerical response.
2. If terminal success, independently verify source artifact ZIP/result/capacity/history and the exact 441-call/lifecycle/downstream contract; the armed terminal-consumer will also validate provenance.
3. If exact-hotspot terminal validation PASS, allow the already-armed deterministic top-1 chain to proceed; do not manually select a hotspot.
4. Independently consume decomposition and terminal-validation artifacts when they exist.
5. Do not execute 32769 and do not alter h, grids, interpolation, masks, support or tolerance.
