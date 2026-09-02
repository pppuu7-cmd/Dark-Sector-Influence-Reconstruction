# Exp073CJ — Article-3 exact 14-window mixed-authority aggregator schema v0.2

**Frozen:** 2026-09-02 after Exp073CI v0.2 exact authority and Wm_S2 Track-A ledger admission, before any real 14-window aggregate using Wm_S2 v0.2 exists.

## Purpose

Exp073CJ is a hosted-only synthetic/governance successor to Exp073AG v0.1. It prospectively repairs one provenance-schema incompatibility created by legitimate new-version authority: Wm_S2 is no longer represented by the historical `exp073aa` route, but by the admitted composite `Exp073CF compact exact PASS -> Exp073CI v0.2 deterministic finalizer exact PASS`.

Exp073CJ changes no numerical science. It must not read real angular artifacts, compute an angular workspace, radial kernel, physical support, covariance, nuisance geometry, relation/null statistic, G7 result, or G8 result.

Classification for every Exp073CJ outcome is non-scientific governance/synthetic `+0/+0`.

## Frozen task order

Exactly once, exactly in this order:

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

## Frozen authority-class map

- `Wm_S0 -> canonical_exp073x2` only.
- `Wm_S2 -> exp073ci_v0_2` only.
- Every other task -> `exp073aa` only.

This is the sole intended semantic difference from Exp073AG v0.1.

The Wm_S2 class refers only to the new-version authority admitted in `docs/ARTICLE3_WM_S2_TRACK_A_ACCEPTANCE_2026-09-02.md`:

- Exp073CI run `33646799130`;
- comparator job `100304043991`;
- artifact `9853165664`;
- digest `sha256:fcfccb6768948ffe34d28e9ed32da64d3b1d071704028fe6f312c1ab8b440f57`;
- token `PASS_EXP073CI_WM_S2_DETERMINISTIC_FIXED_NEHALEM_FINALIZER_EXACT_V0_2`;
- selected W SHA `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087`.

Exp073CF v0.1 finalizer FAIL remains permanent historical authority and is never accepted as `exp073ci_v0_2`.

## Per-window schema retained

Every entry retains exactly:

- `task`;
- `authority_class`;
- positive integer `source_run`;
- positive integer `source_job`;
- positive integer `source_artifact_id`;
- `source_artifact_digest = sha256:<64 lowercase hex>`;
- `selected_window` exactly `{dtype:<f8, shape:[39,12288], sha256:<64 lowercase hex>}`.

The aggregate rejects duplicate/missing/reordered tasks, wrong authority class, malformed provenance, dtype/shape/hash drift, duplicate selected-window hashes, unknown fields, firewall activation, readiness drift, or G7/G8/G9 drift.

## Frozen science semantics

Unchanged from Exp073AG/Exp073AA:

- DES `NSIDE=4096`;
- true ell `0..12287`;
- 39 bands;
- canonical little-endian float64 `[39,12288]`;
- Wm `TE <- TE`;
- WW `EE <- EE`;
- no effective ell or scalar effective `(z,k)` replacement.

## Anti-leakage firewall

All remain false:

`radial_kernel_read`, `physical_k_computed`, `physical_support_evaluated`, `operator_f_invalid_computed`, `retained_coordinates_evaluated`, `fiducial_P_weighting_used`, `covariance_read`, `whitening_performed`, `nuisance_geometry_read`, `nuisance_svd_performed`, `relation_null_read`, `chi_square_read`, `p_value_read`, `G8_read`, `scientific_pass_claimed`.

Scientific authority readiness remains 52.0%; this schema adds zero. G7/G8/G9 remain OPEN.

## Required synthetic tests

At minimum:

1. exact valid mixed-authority fixture accepts;
2. Wm_S2=`exp073aa` rejects;
3. Wm_S2=`canonical_exp073x2` rejects;
4. Wm_S1=`exp073ci_v0_2` rejects;
5. Wm_S0 wrong class rejects;
6. task order drift rejects;
7. duplicate/missing tasks reject;
8. bad source identity/digest rejects;
9. dtype/shape/hash drift rejects;
10. duplicate selected-window SHA rejects;
11. unknown fields reject;
12. firewall/readiness/gate drift rejects;
13. canonical manifest hash remains insertion-order independent.

Required PASS token:

`PASS_EXP073CJ_EXACT_14WINDOW_MIXED_AUTHORITY_SCHEMA_SYNTHETIC_V0_2`

A PASS means only that the future 14-window provenance manifest can accept Wm_S2 v0.2 fail-closed without weakening any other authority rule. It grants no physical/support/G7/G8 claim and no readiness increment.
