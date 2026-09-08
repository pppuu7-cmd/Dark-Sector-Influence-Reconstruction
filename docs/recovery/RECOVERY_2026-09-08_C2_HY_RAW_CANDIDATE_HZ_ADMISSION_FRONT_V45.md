# DSIR Recovery V45 — Exp073HY raw candidate consumed; Exp073HZ admission front

Date: 2026-09-08 UTC.

## Authority reconciliation
Repository V44 remained the newest recovery authority before this iteration. No queued or in-progress workflow existed when HY was consumed. DSIR only; RTK/RQIR untouched.

## Exp073HY terminal consumption
Authoritative producer: run `34243515299`, head `ca3b6a1de8ff96dfc0525ef8485f1ad57e2976b8`. All nine tangent model-point jobs and the manifest verifier are terminal SUCCESS. Raw job logs show exact 28-request completion in z-major/k-minor order, pinned solver/source fingerprints, exact endpoint serialization and artifact upload.

Independent artifact-level verification downloaded all nine GitHub artifacts and verified: GitHub ZIP SHA256; exact receipt run/head/job/model/source bindings; exactly 28 packet files `z00k00..z06k03`, each 64 bytes; exact z-major/k-minor byte concatenation equals `aggregate.bin`; aggregate exactly 1792 bytes; contained and recomputed aggregate SHA256 agree. No decode, mapping or tangent derivative was performed.

HY classification is therefore `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`. It does not admit the tangent raw set and creates no scientific model authority.

Frozen aggregate SHA256 set:
- alpha_m1e4 `1aa24586b57116ac126d314c389e13f8d3159826cc20edea1c8220b1ef69e6ba`
- alpha_m1e3 `b4258528fffa8f115fa98ad9dedb29b8dc6ac8bd7b1710790dfde60776101797`
- alpha_m1e2 `383b4afbf91d8caa30ed546e562da79a5ddaa35e6725627901b6bd2ff5b9f1c2`
- beta_p1e4 `d3f852986d23e3c527ca6da389af2e1b63f51c4af19588d33be31bcdd2a01c4e`
- beta_m1e4 `13b80ab8f1d5c7d6a4402768c7a66a50376a7245b745cc76d55f7f63ecd2fe64`
- beta_p1e3 `77ef62e3d4e0670334245112612af043f38e0cd38262b14fd923e3446d94bc21`
- beta_m1e3 `0a06a4395e0050185790cecb6ee1091bb8249052b74125778bba1c0384fc284c`
- beta_p1e2 `cc21ed6c8989b1e05db1184de400b25e866285790ba8089658eb211c79f52c44`
- beta_m1e2 `cb9c076b54f8bc48a55f5a49a921e66021a9a59bba43be57aea07efc32d43954`

## Exp073HZ prospective admission
Preregistration was frozen first at commit `308a4acd0a4cc5dcc16175235dc2659a8c59cc37`, blob `a4be5047b2968e8b9bc844a3d2bdbd2bc3e6e966`. Hosted-only workflow was then bound at commit `edaa94d42b18f45a6e0659dc23399793e0228830` and launched as run `34248477503`, job `102136488451`.

HZ verifies the exact nine HY ZIP digests, exact receipts/source fingerprints, exact complete coordinate packet sets, exact 1792-byte reassembly and frozen aggregate SHA256 values. It performs no ABI decode, no `Delta_m` mapping, no tangent response, no prediction and creates no scientific authority.

Expected PASS token: `PASS_EXP073HZ_C2_TANGENT_RAW_SET_PROVENANCE_ADMISSION_V0_1`.

On PASS only: `tangent_raw_set_admitted=true`, while `decoded=false`, `mapped=false`, `tangent_response_ready=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Current process
- workflow/run: Exp073HZ / `34248477503`
- job: `102136488451`
- head: `edaa94d42b18f45a6e0659dc23399793e0228830`
- runner: GitHub-hosted ubuntu-24.04; home/self-hosted runner free
- state at note creation: IN_PROGRESS
- checkpoint namespace: N/A, hosted provenance-only admission
- last durable scientific payload: the nine validated HY artifacts above
- SUCCESS next action: consume raw HZ log; only then prospectively freeze separate deterministic tangent ABI decode gate
- FAIL next action: diagnose first causal infrastructure/provenance mismatch; do not alter frozen HY payload or scientific criteria
- BLOCKED next action: preserve HY candidate; do not decode or derive tangent response

No competing heavy run was created.