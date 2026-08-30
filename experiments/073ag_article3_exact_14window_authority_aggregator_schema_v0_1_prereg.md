# Exp073AG — Article 3 exact 14-window authority aggregator schema v0.1

**Frozen:** 2026-08-30 while both real Exp073X2 chains P (`33300997298`) and Q (`33301058260`) are still in progress, before any canonical X2 result exists, before any of the remaining 13 Exp073AA production tasks is released, and before any complete 14-window authority exists.

## Purpose

Exp073AG is a **non-scientific exact-authority aggregation schema/firewall gate**. It freezes how the future canonical `Wm_S0` X2 authority and the remaining 13 Exp073AA angular authorities must be assembled into one immutable ordered 14-window authority before Exp073AE may perform the real pre-support join.

This v0.1 gate performs synthetic schema QA only. It must not read real X2/Exp073AA artifacts, must not compute any angular workspace, radial kernel, physical support, covariance, nuisance geometry, relation/null quantity or G8 statistic.

Hosted synthetic PASS contributes **0 scientific-readiness points**. Strict Article-3 scientific repository readiness remains **52%** and G7/G8/G9 remain OPEN.

## Frozen upstream governance

The future real aggregator is subordinate to:

1. `docs/ARTICLE3_EXP073X2_PARALLEL_AUTHORITY_SELECTION_2026-08-30.md`;
2. `docs/ARTICLE3_DES_ANGULAR_14_TASK_MANIFEST_X2_SUCCESSION_AMENDMENT_2026-08-30.md`;
3. `experiments/073af_article3_x2_to_exp073aa_release_control_v0_1_prereg.md`;
4. `experiments/073aa_article3_des_angular_task_runner_v0_1_prereg.md` for unchanged one-task angular semantics.

Exp073AG cannot itself decide P/Q authority; it only accepts a previously valid immutable `canonical_exp073x2` Wm_S0 authority receipt.

## Frozen exact task order

The aggregate must contain exactly once and in exactly this order:

1. `Wm_S0`
2. `Wm_S1`
3. `Wm_S2`
4. `Wm_S3`
5. `WW_S0_S0`
6. `WW_S0_S1`
7. `WW_S0_S2`
8. `WW_S0_S3`
9. `WW_S1_S1`
10. `WW_S1_S2`
11. `WW_S1_S3`
12. `WW_S2_S2`
13. `WW_S2_S3`
14. `WW_S3_S3`

## Frozen per-window authority schema

Every entry must contain exactly:

- `task` — frozen task identity;
- `authority_class` — `canonical_exp073x2` only for `Wm_S0`, `exp073aa` for all other 13;
- `source_run` — positive integer hosted workflow run identity;
- `source_job` — positive integer hosted job identity;
- `source_artifact_id` — positive integer artifact identity;
- `source_artifact_digest` — `sha256:` + 64 lowercase hex;
- `selected_window` containing exactly:
  - `dtype: "<f8"`;
  - `shape: [39,12288]`;
  - `sha256` — 64 lowercase hex.

The future real aggregate must reject:

- duplicate/missing/reordered tasks;
- wrong authority class;
- non-hosted/missing source identities;
- malformed artifact digest or selected-window SHA;
- dtype/shape drift;
- duplicate selected-window SHA across different task identities;
- unknown top-level or nested fields.

The no-duplicate-window-SHA rule is a provenance sanity check: distinct frozen task identities must not silently alias the same serialized selected window. A genuine future equality would require a new prospective scientific/provenance review rather than automatic acceptance.

## Frozen aggregate identity

The aggregate receipt must compute a deterministic manifest SHA256 from canonical UTF-8 JSON serialization of the ordered 14 metadata entries using sorted object keys and compact separators, with no timestamps, paths, mutable URLs or runner-local fields included in the hashed payload.

The manifest hash certifies metadata/provenance identity only; it is not a hash of concatenated numerical arrays and is not a scientific statistic.

## Frozen angular semantics retained

Every selected window remains:

- PyMaster/NaMaster 2.7 lineage;
- `NSIDE=4096`;
- true ell axis `0..12287`;
- 39 frozen bandpowers;
- canonical little-endian float64 shape `[39,12288]`;
- Wm selected component `TE <- TE`;
- WW selected component `EE <- EE`;
- no effective ell or scalar effective `(z,k)` replacement.

Exp073AG does not recompute these quantities; the future real aggregator validates the authority receipts only.

## Anti-leakage firewall

The aggregate receipt must retain all of the following exactly false:

- `radial_kernel_read`;
- `physical_k_computed`;
- `physical_support_evaluated`;
- `operator_f_invalid_computed`;
- `retained_coordinates_evaluated`;
- `fiducial_P_weighting_used`;
- `covariance_read`;
- `whitening_performed`;
- `nuisance_geometry_read`;
- `nuisance_svd_performed`;
- `relation_null_read`;
- `chi_square_read`;
- `p_value_read`;
- `G8_read`;
- `scientific_pass_claimed`.

Readiness remains exactly `52`; `readiness_increment=0`; G7/G8/G9 remain `OPEN`.

## Hosted synthetic test matrix

At minimum:

1. exact valid synthetic 14-entry manifest -> accepted;
2. task order drift -> reject;
3. duplicate task -> reject;
4. missing task -> reject;
5. `Wm_S0` wrong authority class -> reject;
6. non-Wm_S0 wrong authority class -> reject;
7. malformed/zero source run/job/artifact identity -> reject;
8. malformed artifact digest -> reject;
9. dtype drift -> reject;
10. shape drift -> reject;
11. malformed selected-window SHA -> reject;
12. duplicate selected-window SHA across tasks -> reject;
13. unknown top-level field -> reject;
14. unknown nested field -> reject;
15. firewall activation -> reject;
16. readiness drift -> reject;
17. G7/G8/G9 drift -> reject;
18. deterministic manifest hash reproducibility under dictionary insertion-order changes -> pass.

## Required hosted synthetic QA token

`PASS_EXP073AG_EXACT_14WINDOW_AUTHORITY_AGGREGATOR_SCHEMA_SYNTHETIC_V0_1`

This token means only that the future 14-window authority aggregation schema is fail-closed and deterministic. It is not a real angular authority, not a scientific PASS, not Layer A, and does not authorize any readiness increase.
