# DSIR recovery V119 — broad closed, exact response-atom hotspot active

Updated: 2026-09-11. Scope: **DSIR only**. Never mix KMDSB, RTK or RQIR.

## Scientific frontier
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, full-traversal max relative component difference `0.012484060640679777` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged. 32769 remains unauthorized; covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Broad quantile localization CLOSED
Workflow/run `layerb-post-16385-broad-quantile-localization-v0-2 / 34585873905`, head `ef7f12195b4bc491c09f107fcba58e2bdf350881`, completed success on both independent hosted lanes.

- broad-raw `103219830602 / 10194625456`: ZIP SHA256 `5d140606a58a93b6627cb3c9211daf09e07a259ec480f0b084675bf6f3298845`; result SHA256 `eac77cb17ef76c5210da853a0d66c2a3b5f49f41e3fac9af981b2369eb72552f`; classification `POST_16385_BROAD_QUANTILE_RAW_LOCALIZATION_PASS_PLUS_0_PLUS_0`; max raw symmetric relative difference `1.5949311416969764e-10`.
- broad-conditioning `103219831011 / 10194530579`: ZIP SHA256 `425de58818167ac743a057881cc957ca85060fe68284b5554bf61253cb7ace29`; result SHA256 `5cc349fad1ac2ed2a82c37597d64df060be87e17aaa90764aa096b16c15a6de1`; classification `POST_16385_BROAD_QUANTILE_CONDITIONING_PASS_PLUS_0_PLUS_0`; max response symmetric relative difference `0.00016265101390432733`; max cancellation amplification indicator `3442722.6399590056`.
- broad response/full plateau ratio `0.01302869463596828`; full plateau/broad response `76.75366012795348`; raw/full plateau `1.2775740102541907e-8`.
- exact 15 frozen indices `[512,1024,1536,2048,2560,3072,3584,4096,4608,5120,5632,6144,6656,7168,7680]` and two frozen z anchors preserved.
- unsupported=0, lookup <=1e-12, 8 total constructions across each two-lattice lane, max one live; no alternative h, no 107-row scientific rerun, no downstream authority.

Durable authority: `docs/dsir4/authority/LAYERB_POST_16385_BROAD_QUANTILE_TERMINAL_V0_1.json`, current blob `9585e46b9e9ff43195ca042037bc229994cf1385`, correction commit `4d40c5678c94e55e99f5ea2531b1551785b3dd8b`.

GitHub-native broad terminal consumer `34588576533 / 103228282039 / 10194631718` independently validated both result SHAs. ZIP SHA256 `8373659fbd40ed65ebc57ae701f4290d5a2a42dc07b8f6118a0de053ec079ee5`, consumer SHA256 `684ea087a3e975b2ea56bbef443fff804cdc1985a3995e8136b6feb4fd38ecee`, classification `POST_16385_BROAD_QUANTILE_TERMINAL_ARTIFACTS_VALIDATED_PLUS_0_PLUS_0`. Durable authority `docs/dsir4/authority/LAYERB_POST_16385_BROAD_TERMINAL_CONSUMER_V0_1.json`, commit `0eceab162644a13ff27c4df7f7fb2b2f3c670b0f`, blob `e64c9b4f94bdccb4d1e923abb515f9a3e46adaab`.

Interpretation: raw grid mismatch is negligible (~1.6e-10). Frozen finite-difference response construction can amplify grid perturbations strongly, but the broad probe reaches only ~1.3% of the full plateau. Therefore broad localization does not reproduce/localize the full 1.2484% maximum; exact frozen request-plan atom localization is justified as a support-only next diagnostic.

## Exact hotspot preregistration and preconditions CLOSED PASS
Prospective contract: `docs/dsir4/prereg/LAYERB_POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_V0_1.md`, blob `66a84ab1492824cf4851a592d3e1d1bb2c29a2f0`. Corrected helper `ci/layerb_post_16385_exact_response_atom_hotspot_v0_1.py`, blob `6ee1243adf626a6e0f10883fcccef0f8b04141a3`.

Static audit v0.3: run/job/artifact `34587182733 / 103223992902 / 10194070784`, ZIP SHA256 `40b674c7c32a7de4f7363d91d2571dc4cb172e0e31c16e5a0e15c5baea8f1079`, 22/22 PASS; no CLASS/science/downstream authority.

Authority-binding audit: run/job/artifact `34587506106 / 103224995565 / 10194201493`, ZIP SHA256 `e1bef01f9071d6389ab365f4dc03e1d9ba15ea4592e5dba7796fe1b889d76dc8`, result SHA256 `8bbda3ef063e34d6cdb7710571d8b3269d5b5986558a09082827578a53ba370c`, 17/17 PASS. Durable authority `docs/dsir4/authority/LAYERB_POST_16385_EXACT_HOTSPOT_AUTHORITY_BINDING_AUDIT_V0_1.json`, commit `189cb8880978c39e15b032452aff22d6fd0979ab`, blob `b6d31c60d961a85679b3bbeb269869d187cc446e`.

## ACTIVE main process
Fresh anti-dup before launch: zero in-progress current hosted runs; only unrelated stale superseded self-hosted resource pilot remained queued.

Workflow `layerb-post-16385-exact-response-atom-hotspot-v0-1`, launch commit/head `5f202de811c07c020100055a63391b7225358670`.
Run/job: **`34592951737 / 103242180883`**, GitHub-hosted Ubuntu 24.04, timeout 240 min.

Latest verified state at V119 creation:
- checkout PASS;
- prospective activation/frozen identity gate PASS;
- frozen numerical/build stack installation IN_PROGRESS;
- CAMB, CLASS-IV build, exact data acquisition and numerical execution pending.

Frozen numerical execution, once reached:
- exact 441 shared request calls = 377 DES + 64 BOSS GL64;
- fine-only GL128 128 calls excluded from atom comparison exactly as preregistered;
- bitwise shared coarse/fine plan identity required before solver use;
- canonical 8193 and 16385 only;
- four roles per lattice, 8 total constructions, max one live;
- h=1e-4, native kpd20, centered cubic and lookup <=1e-12 unchanged;
- top-64 exact `(call,z,k,component)` response atoms and 441 per-call maxima recorded;
- support-only +0/+0; no 107-row rerun, no new scientific authority, no 32769/covariance/Wm_S3 authorization.

## Runner ownership / anti-dup
The exact-hotspot hosted job `34592951737 / 103242180883` owns the current heavy DSIR numerical process. Do not launch another exact-hotspot or full 8193->16385 run while it is active. Stale self-hosted `34550495778 / 103112190909` remains superseded and must not receive ownership.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%**.

## Exact next action
1. Query `34592951737 / 103242180883`; do not inspect partial numerical response.
2. If active, no duplicate heavy science; response-blind/static side work only.
3. If terminal, independently download artifact and verify ZIP/result/capacity/history hashes, 441-call plan identity, lifecycle 8/max1/final0, unsupported=0, lookup<=1e-12 and closed downstream flags.
4. Only after independent terminal validation inspect the top-64 atom coordinates and determine the next diagnostic under a separately prospective contract.
5. Do not execute 32769.
