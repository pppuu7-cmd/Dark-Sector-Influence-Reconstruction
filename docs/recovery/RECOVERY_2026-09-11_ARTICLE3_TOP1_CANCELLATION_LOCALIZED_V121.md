# DSIR recovery V121 — ARTICLE3 top-1 cancellation localized

Date: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

## Scientific frontier preserved
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` are unchanged. No 32769 execution is authorized; covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Exact hotspot terminally closed
Exact 441-call hotspot source run/job/artifact `34592951737 / 103242180883 / 10266223990`, frozen head `5f202de811c07c020100055a63391b7225358670`, is terminal SUCCESS and independently consumed. Artifact ZIP SHA256 `c836ed5f8b7d6b8c954c99d25a561b0544b049263589d88e3f4fec2fd8297e23`; source result SHA256 `4023403aaae03481507f778ce4a85c119160cebd785c9c91a534260783049394`. The support-only result has exact 441 shared calls = 377 DES + 64 BOSS GL64, bitwise-identical shared plan, lifecycle 8/max1/final0, unsupported=0, lookup max `1.657034302538322e-16`, no 107-row replay and all downstream-closed flags. It reproduces the authoritative full-traversal maximum exactly: `0.012484060640679777`.

The deterministic maximum atom is DES call 204, target index 44, `k=0.01698756109424023` (`0x1.1652fed5ab075p-6`), `z=0.7475` (`0x1.7eb851eb851ecp-1`), component `abs_dDelta_m_dbeta_symmetric`, coarse `0.09512399628874846`, fine `0.09632654268898477`, relative difference `0.012484060640679777`.

## Top-1 role cancellation chain terminally closed
Prospectively frozen decomposition run/artifact `34608169257 / 10268078468` is independently consumed. ZIP SHA256 `c0363cb45a54ed9ff634548bd96c539d55757a646d014f83ddd74f10bf62ddb0`; decomposition SHA256 `6e041f201d0b2e4bec86deb7bbfc2e40b6b4cd51f73e1b45dd29665d516d838c`.

Terminal consumer run/job/artifact `34611473046 / 103302765790 / 10268761538` independently validates the decomposition. ZIP SHA256 `be49034720f5713b4c9de972e80038d2eb8fa56774db8af0afeb395078daacc5`; `validation.json` SHA256 `d2417d4bfe55f0c8cbf4567f781a479475ac9191ba6c1b79931f801894ddfca3`; classification `POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0`; primary reproduction error exactly `0.0`.

Durable authority: `docs/dsir4/authority/LAYERB_POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_AUTHORITY_V0_1.json`, completed identity commit `c7e4968fb13880fb2d7c7615d10a0821073b2243`.

### Root-cause localization supported, not scientific reclassification
At the frozen hotspot, cross-grid raw-role relative differences are tiny: alpha_minus `3.9076164816604525e-12`, beta_minus `6.885687402119481e-11`, beta_plus `5.324796659621718e-11`, reference `4.396252619143809e-11`. Nevertheless the beta finite-difference numerator/response cross-grid relative difference is exactly `0.012484060640679777`. The beta cancellation scale is only `9.658754418934927e-09` at 8193 and `9.780859258369292e-09` at 16385. Thus the full plateau is localized to deterministic cross-grid changes in nearly cancelling beta roles amplified by the frozen `h=1e-4` finite difference. This is support-only `+0/+0`; it does not change h, tolerance, grids, interpolation, masks, classifier, or downstream authority.

## Next support gate prospectively frozen and running
To test whether this cancellation mechanism is isolated or systematic, the complete ordered frozen `source_result.top_64_response_atoms` list is now preregistered in `docs/dsir4/prereg/LAYERB_POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_V0_1.md`, prereg blob `940a09d194fe9e68e6fc14271e7ab99b6aded3e4`. Helper blob `92f35f0f563fe5c5ba54b3984ae9a82e2abaf8e7` preserves exactly the same h/grids/solver/interpolation and uses 8 role-major constructions total.

Corrected response-blind static audit run/job/artifact `34613989460 / 103311217763 / 10270106208` is independently verified 24/24 PASS. Artifact ZIP SHA256 `23f6eb6102f7513c88a7b6ffc2017dae4da3b6ed81fec174fa6656650af913b4`; `static.json` SHA256 `2d87456ad13e95eeb40a5089438c38ed3759a7d2daa84c35caf14960d133cd77`. Durable static authority is `docs/dsir4/authority/LAYERB_POST_16385_TOP64_ROLE_CANCELLATION_STATIC_AUDIT_V0_2.json`, commit `717a15a615061cea441910d03fdda1f9a4a2b2c2`.

Exactly one support-only census is active: workflow/run/job `layerb-post-16385-top64-role-cancellation-census-v0-1 / 34614119149 / 103311649147`, launch head `6b684ac91c7a261e6b588da1a4922a411bd65614`, GitHub-hosted ubuntu-24.04. No duplicate is permitted. It must reproduce all 64 source primary discrepancies to relative error `<=1e-12`, preserve lifecycle 8/max1/final0, unsupported=0 and lookup `<=1e-12`, and remain downstream closed.

## Runner ownership
One useful GitHub-hosted DSIR lane is active: `34614119149 / 103311649147`. Stale superseded self-hosted run `34550495778 / 103112190909` remains queued and must not receive home-runner ownership.

## Readiness
`ARTICLE3_REPOSITORY_READINESS: 68%`. Funnel-freeze readiness: `67%`. These stable-rubric values do not advance from support-only root-cause diagnostics.

## Exact next actions
1. Do not duplicate `34614119149` and do not inspect partial census output.
2. When terminal, independently download/hash `census.json`, capacity/history receipts; verify exact source/provenance identities, 64/64 ordered atoms, 8/max1/final0, unsupported=0, lookup<=1e-12, max primary reproduction error<=1e-12 and all downstream-closed flags.
3. Classify the census only as support `+0/+0` or infrastructure FAIL according to the frozen contract.
4. Use the completed census only to decide a separately preregistered root-cause diagnostic. Do not execute 32769 or alter h/tolerance/grids/interpolation/masks/classifier.
