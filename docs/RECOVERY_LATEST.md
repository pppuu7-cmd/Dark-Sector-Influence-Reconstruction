# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HX_PLAN_PASS_HY_TANGENT_RUNTIME_FRONT_V44.md` (creation commit `df69e399d812a1da9f72349215318308e7ad59cc`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

No C2 scientific/model authority exists.

## C2 reference chain now validated

HT raw candidate, HU raw-set admission, HV exact ABI decode and HW reference `Delta_m` bridge are all raw-log/artifact validated. Latest reference authority is HW `34242852819 / 102117188431`, artifact `10062705321`, digest `sha256:7ea327f0d6e29e4b415c9f66201b266e9015d46a383e8867de94b05665517c00`, canonical bridge SHA256 `2b6eb07c99273292bcb2cf929295071e401e81ed51cfe3f4c3b19d5a395518fb`, authority blob `69d617ebfc5c8184b602718d3dbf1a0cec228e1e`.

C2 boundary remains `raw_record_set_admitted=true`, `decoded=true`, `mapped_reference_coordinate=true`, `tangent_response_ready=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Newly validated support — Exp073HX

HX run `34243153985 / 102118219475`, head `dd25da6aa9363c3a279e894595106b472b2375ad`, raw-log exact PASS `PASS_EXP073HX_C2_TANGENT_RUNTIME_PLAN_STATIC_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`. It freezes exactly 9 nonzero tangent points × 28 coordinates = 252 requests, reference not recomputed. HX runs no cosmology and creates no tangent/scientific authority.

## Current frontier — Exp073HY tangent raw runtime producer v0.1

- prereg `docs/dsir4/prereg/EXP073HY_C2_TANGENT_RAW_RUNTIME_PRODUCER_V0_1.md`, commit `7ab623edfaa1fc27c62d020fc93d0679844286e6`, blob `5b7f9d3ce989f524e1d9555a219b692e44793821`;
- workflow `.github/workflows/exp073hy-c2-tangent-raw-runtime-producer-v0-1.yml`, implementation commit `4a50791ce0493ee69084224a834ac2902f0580f5`, blob `93d476850f8c388d3e91f9f41283e7b436b99268`;
- binding/head commit `ca3b6a1de8ff96dfc0525ef8485f1ad57e2976b8`;
- run `34243515299`;
- GitHub-hosted 9-model matrix with `fail-fast:false`; self-hosted/home heavy owner none;
- at pointer update: tangent model jobs are queued/in_progress; final manifest verifier awaits all nine.

Each successful model job creates one complete durable 28-record artifact with 64-byte records, exact 1792-byte aggregate, SHA256 and run/job/head/model receipt. Reference `(0,0)` is never recomputed. HY ceiling is `TANGENT_RAW_RUNTIME_CANDIDATES_PLUS_0_PLUS_0`; tangent raw set remains non-admitted and no decode/mapping/derivative/prediction/science is allowed.

Expected terminal token: `PASS_EXP073HY_C2_TANGENT_RAW_RUNTIME_CANDIDATES_V0_1`.

## Exact next transition

On HY terminal, inspect all matrix jobs and manifest raw log. Preserve complete successful model artifacts. Only terminal PASS plus independent verification of all nine artifact digests/receipts/28×64-byte contents/1792-byte per-model aggregates permits a separate tangent raw-set provenance admission/decode/mapping pipeline. On a model failure, diagnose only its first causal defect and do not invalidate other completed units.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
