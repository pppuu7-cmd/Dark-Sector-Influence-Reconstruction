# RECOVERY V137 — DSIR Article III parser-corrected full control plane

Date: 2026-09-12. Scope: **DSIR only**. This note supersedes V136 as the current recovery front; all older recovery notes remain immutable history.

## Scientific frontier — unchanged

Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`.

Frozen science remains unchanged: `REL_TOL=1e-3`, `h=1e-4`, native `k_per_decade_for_pk=20`, centered-cubic interpolation, same physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0, lookup mismatch `<=1e-12`.

No 16385->32769 scientific response has executed. `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`. No real durable resource authority exists. No actual one-live guard PASS or one-run authorization exists. Covariance restriction remains unauthorized. `Wm_S3` remains closed.

## Deviation discovered after V136

V136 correctly closed parser undercapacity and the V0.3 source/consumer static front, but its stated downstream chain was stale. The real event-chain still listened to V0.2 source, candidate-packaging/materialization still required the old parser/build identities, V133 promotion review still required the old chain, and one-live/authorization/scientific/terminal objects still pinned parser `524288` / old build identity.

This was an infrastructure/provenance identity migration gap, not a scientific change. The frozen scientific classifier, response construction, grid/domain/mask rules and stopping criterion were not altered.

## V137 closure A — parser-corrected V0.3 resource downstream chain

Current source workflow remains `.github/workflows/layerb-32769-isolated-highmem-resource-lifecycle-pilot-v0-3.yml`, Git blob `e55c0ab05c6b7eb0d622eadba25d7e20cdc4ce16`. It is dispatch-only, dedicated-label-only, parser `1048576`, point capacity `32769`, physical `MemTotal > 16373452 kB`.

Current independent event-chain workflow `.github/workflows/layerb-32769-resource-lifecycle-independent-consumer-v0-1.yml`, Git blob `7f6d31b2a208dd1c052286aa1f116963001f52ae`, now triggers on V0.3 and pins independent consumer V0.3 blob `cb9e83377f7f7c0498f0b2bfc3b8b06c2683d9ab`; invalid independent validation makes the workflow fail closed.

Parser-corrected candidate/materialization identities:
- candidate packaging contract V0.2: `71d77aa4d074bba1a2f53e7f9299a9db32e93ffc`;
- candidate packager V0.2: `c38bf9a0108ab3ef50f1abec513fa2f6ff0373a4`;
- materialization contract V0.2: `3e53992864ad10f23752df03a653f8073cc18ffa`;
- materializer V0.2: `8a4e03848694a59550460e9866d0aeaec747780e`;
- candidate-packaging workflow: `9977781cce13e84489203e89b4d11182a835a3a9`.

These reject old parser capacity, old source workflow, equality to the exhausted hosted memory threshold, synthetic materialization inputs and invalid provenance.

Parallel audit run `34654898436` passed event-chain, packager and materializer lanes. Its candidate-static lane failed only because the audit interpolated its own `${{ github.run_id }}` while testing for the literal expression in the target workflow; the target workflow blob itself had already passed. Efficient finalizer run `34654967676` reused the three valid prior artifacts, repaired only that static assertion and passed independent finalization.

Finalizer jobs: `103445258833` and `103445283173` SUCCESS. Final artifact `10284194979`, ZIP SHA256 `197e36310132b8acd2c1ceb485435f2f1c34536579d678a632a5c95e443b8cdc`, final receipt SHA256 `ad22d7c9096236934f05c66e852bd73b0bfb3be5018e187183dca83e4bdf7232`.

Durable authority: `docs/dsir4/authority/LAYERB_32769_V03_DOWNSTREAM_CHAIN_REPAIR_AUDIT_V0_1.json`, creation commit `ef06cdbe09cda68dbc5d5b4dec9e02161cbeca60`, Git blob `49e3ee100a4a24a2e26ea929e7c62285d70bef82`.

## V137 closure B — parser-corrected promotion and dormant science control plane

Promotion V0.2:
- contract blob `331cf499627a3673ce88c483e7afcfd4f731d105`;
- reviewer blob `36e0549b86436bcafe7c98f10c0a404b97eeebdc`;
- manual read-only workflow blob `5eb070db99f66c11a5fa108d2e1270020f42abb1`.

Promotion requires parser `1048576`, build authority blob `b5cd7304c110962dc3baef8d04ef67d5a8042e5f`, `MemTotal > 16373452 kB`, exact candidate bytes and the V137 downstream repair authority. It creates no repository authority and authorizes no science.

Parser-corrected dormant science-control identities:
- one-live guard contract V0.2 `9e20a5f3a6cb36c185edf48ad74857f20e8f62d8`;
- one-live guard V0.2 `ed703767e15a47bce8390fe7071f90968b9dacd0`;
- one-run authorization contract V0.2 `a4e8b58711f520946d1195f739f111225d840ef8`;
- one-run authorizer V0.2 `40717ac4a0131e6b2bb3af1a87070f1b7cbf5913`;
- terminal contract V0.2 `e441c54f8ad4a0590ad521710d4b9dbf37f111ba`;
- terminal consumer V0.2 `661e0a69b7110fb0c0fcbb27fd6413456bb01ae2`;
- scientific wrapper V0.2 `bee4fe7f9d78024410629627694cc69ea1d3cef7`;
- frozen parent scientific engine reused unchanged: `5ae2068d65dd45e0813c75fb795e55aa1bda1d5e`;
- dormant production workflow V0.2 `049f15ba4bb22fd8d9725263d88d54b3f2e7994a`.

The V0.2 scientific wrapper does **not** redefine `execute`; it changes only infrastructure identities/parser envelope and then calls the frozen V0.1 parent `main`. Terminal V0.2 keeps the V0.1 strict classifier, frozen constants, canonical lattices, request plan and lifecycle unchanged and reuses the V0.1 validator after parser/build identity prechecks.

Production workflow V0.2 is `workflow_dispatch`-only, `runs-on: [dsir-32769-highmem]`, builds exact CLASS point capacity `32769` / parser `1048576`, requires a real measured durable resource authority and current-run live guard/authorization, and has not been dispatched.

Control-plane parallel audit run `34655645739` passed all six independent prerequisite lanes plus final verifier:
- engine/production static `103447334398` SUCCESS;
- terminal static equivalence `103447334484` SUCCESS;
- guard synthetic `103447334539` SUCCESS;
- authorizer synthetic `103447334576` SUCCESS;
- promotion-workflow static `103447334579` SUCCESS;
- promotion synthetic `103447334599` SUCCESS;
- independent verifier `103447371129` SUCCESS.

Final artifact `10285690126`, ZIP SHA256 `8619d4ebca99f6f68977dc135d35e72c07b0b36d82f413f525bb7f6f58a06d17`, final receipt SHA256 `87990f857d741fb2a812a108e1d4e92d35f94543f999377bb9e82a87870a4ac4`.

Durable authority: `docs/dsir4/authority/LAYERB_32769_PARSER_CORRECTED_CONTROL_PLANE_AUDIT_V0_1.json`, creation commit `8fa88578828c3f6d52ecbe258b92863ffee1e14b`.

## Standard-hosted telemetry reconciliation

The later `beta_plus` lane of run `34649988416`, job `103429640191`, is terminal failure. No artifact was retained and job-log content was no longer available through the API at consumption time, so it is only qualitative corroboration of hosted-memory insufficiency and is not used as quantitative authority. The independently durable quantitative memory authority remains the reference lane from V136.

## Remaining true blockers

1. Attach/configure a real isolated high-memory runner with the frozen V135 configurator, unique name, `--no-default-labels`, exact custom label `dsir-32769-highmem`, physical `MemTotal > 16373452 kB`; 32 GiB remains preferred operational guidance only.
2. Dispatch exactly one V0.3 response-blind measured resource/lifecycle pilot and obtain a real PASS.
3. Automatic independent consumer V0.3 -> candidate packaging V0.2 -> materializer V0.2 must PASS on the real artifact.
4. Real candidate must pass parser-corrected promotion review V0.2, then reviewed bytes must be deliberately copied byte-for-byte to `docs/dsir4/authority/LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_V0_1.json`.
5. Only inside the first parser-corrected scientific production run may immediate one-live guard V0.2 and current-run-only one-run authorization V0.2 become real PASS.
6. Only then exactly one canonical 16385->32769 scientific run may execute, followed by terminal consumer V0.2 strict classification.

Old superseded run `34550495778` / job `103112190909` remains a generic self-hosted ownership hazard and must not receive the dedicated runner.

## Readiness

`ARTICLE3_REPOSITORY_READINESS: 68%` — unchanged.

Funnel-freeze/scientific frontier: `67%` — unchanged.

`WORKING_PLAN_COMPLETION: 87%` — operational increase only. V137 closes the parser-corrected real resource downstream chain, promotion path and dormant science-control/terminal path. Scientific convergence itself has not advanced.

## Exact next action

There is no remaining useful hosted-only parser-migration prerequisite that should substitute for the physical gate. Attach a qualifying isolated runner and dispatch exactly one current V0.3 response-blind resource lifecycle pilot. Do **not** dispatch production science V0.2 before the real measured resource authority exists.

`DSIR Continuous Research` remains enabled hourly. Repository state and live Actions ownership remain authoritative.
