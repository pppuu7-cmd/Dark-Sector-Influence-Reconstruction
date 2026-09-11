# DSIR recovery V123 — top-64 retry + parallel cancellation-support closure

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

This immutable note supersedes V122 for current-front recovery. V122 and all earlier recovery notes remain immutable history.

## 1. Scientific frontier remains frozen

Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, with max relative component difference `0.012484060640679777` versus strict frozen `<1e-3`.

The scientific contract is unchanged: `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, frozen physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and requested-node lookup mismatch `<=1e-12`.

No 32769 execution is authorized. `covariance_restriction_authorized=false`. `Wm_S3_opened=false`.

## 2. Exact hotspot / top-1 support authority remains closed

The full plateau is localized to the frozen DES beta-response hotspot at call 204 / target 44 / z `0.7475` / k about `0.01698756`, component `abs_dDelta_m_dbeta_symmetric`.

Durable top-1 authority:
- `docs/dsir4/authority/LAYERB_POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_AUTHORITY_V0_1.json`
- Git blob `cb0b07bd75208619e681f02528fb0c761ddedabb`
- support-only `+0/+0`
- downstream science gates remain closed.

## 3. New parallel support package A — cancellation amplification / binary64 / ULP

Three independent analysis-only lanes were run in parallel from the immutable top-1 authority. No CLASS solver was invoked.

Source parallel run:
- workflow: `layerb-post-16385-top1-parallel-support-audits-v0-1`
- run: `34624187060`
- head: `56f9152f4fa775439365a88ea5c2e7b502f1f5eb`
- all three jobs terminal SUCCESS.

Artifacts:
- cancellation amplification: artifact `10273825514`, ZIP SHA256 `5d5a3ef079bff829dcdbb37f6daab6c812e20491920d8d8a6083090cd6b09df8`
- binary64 replay: artifact `10274180314`, ZIP SHA256 `63e8ea8c79c51a1ff6e5ea171c75999904a36c7dbc3e2eb7b88827bb2f03f41d`
- ULP sensitivity: artifact `10274265218`, ZIP SHA256 `313aa832ece4f720bc3946515bab80da9e4310afbdf645223504fc84d8fb44bb`.

Independent terminal consumer:
- run/job `34624280381 / 103345478391`
- head `9c462e3ba8308450a7103a0b0770992676090b19`
- terminal artifact `10273496144`
- ZIP SHA256 `0bb033efea6350679c14d2e53c8e416be17c65633bbc602dda4499c8b3f22f84`
- classification `POST_16385_TOP1_PARALLEL_SUPPORT_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0`.

Durable authority:
- `docs/dsir4/authority/LAYERB_POST_16385_TOP1_PARALLEL_SUPPORT_TERMINAL_AUTHORITY_V0_1.json`
- creation commit `d46ae6e2175502ed9b74444dc8f91fdc48cedb05`.

Validated quantitative findings:
- beta-response cross-grid relative difference = `0.012484060640679777`
- max raw-role relative cross-grid shift = `6.885687402119481e-11`
- response / max-raw-role amplification = `181304493.09733495`
- response / min-raw-role amplification = `3194801920.626294`
- beta cancellation-scale relative difference = `0.0124840605726825`
- ±1 ULP endpoint-neighbor metric range = `[0.01248406064067949, 0.012484060640680063]`
- max metric shift under ±1 ULP endpoints = `2.8622937353617317e-16`.

Interpretation is support-only: the plateau is not explained by ordinary endpoint binary64 rounding; very small raw-role cross-grid changes are strongly amplified by finite-difference cancellation.

## 4. New parallel support package B — subtraction conditioning / signed attribution / Decimal replay

Three further independent arithmetic-only lanes were run in parallel from the immutable prospectively frozen top-1 decomposition artifact. No CLASS solver was invoked.

Immutable decomposition source:
- run `34608169257`
- artifact `10268078468`
- ZIP SHA256 `c0363cb45a54ed9ff634548bd96c539d55757a646d014f83ddd74f10bf62ddb0`.

Parallel arithmetic run:
- workflow `layerb-post-16385-top1-parallel-decomposition-arithmetic-v0-1`
- run `34624525157`
- head `107b453d485a14f8a812539d04abbbf9c63d8885`
- all three jobs terminal SUCCESS.

Artifacts:
- subtraction condition: artifact `10274091055`, ZIP SHA256 `d5d196ebb2b63e86a5e750e26f75bc029de410b1c4bfe4725317ebf7a1d11f19`
- signed role attribution: artifact `10274026180`, ZIP SHA256 `946342a64a6ae041ac81d1aa85fef5fe7f6a1c2314d03f2dfad4544186b4ada4`
- Decimal subtraction replay: artifact `10274565598`, ZIP SHA256 `35a0ed4aeaab9e1ba7c8f3573e124249752716380960893b4e943bf1b17970c8`.

Independent terminal consumer:
- run/job `34624598782 / 103346512972`
- head `664c68b0e306e4e28518e73383a67d4dfb5afa46`
- terminal artifact `10273886027`
- ZIP SHA256 `72e2fb96df45ddb05d49bcd215618a366a08df62c5b386ca88c9ab6118593c26`
- classification `POST_16385_TOP1_DECOMPOSITION_ARITHMETIC_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0`.

Durable authority:
- `docs/dsir4/authority/LAYERB_POST_16385_TOP1_DECOMPOSITION_ARITHMETIC_TERMINAL_AUTHORITY_V0_1.json`
- creation commit `4392df8fe76680ee6e4bfed7e073263e4729e39f`.

Validated findings:
- beta finite-difference subtraction condition number is `>1e8` on both canonical 8193 and 16385 grids;
- exact Decimal replay from the binary64 role operands shows relative rounding error of the subtraction itself `<1e-12` on both grids;
- signed cross-grid role shifts recombine to the beta-numerator change inside the frozen fail-closed residual bound.

Interpretation is support-only: this strengthens the diagnosis of local ill-conditioning / cancellation amplification rather than ordinary floating-point subtraction error.

## 5. Top-64 census — single unchanged retry remains the only heavy owner

Attempt 1 of workflow/run `layerb-post-16385-top64-role-cancellation-census-v0-1 / 34614119149` failed its prospectively frozen exact-reproduction guard and remains classified infrastructure/numerical-reproducibility FAIL `+0/+0`, not scientific FAIL.

Exactly one unchanged retry is permitted and is active:
- run `34614119149`
- run attempt `2`
- launch head `6b684ac91c7a261e6b588da1a4922a411bd65614`
- execution checkout/static-authority head `717a15a615061cea441910d03fdda1f9a4a2b2c2`
- job `103331912096`
- latest checked state: **IN_PROGRESS** on GitHub-hosted ubuntu-24.04.

All pre-execution identity/source/numerical-stack/build guards had passed before the long frozen census step. No duplicate top-64 run is authorized.

Expected PASS token remains `POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0` with exact 64 ordered source atoms, lifecycle 8/max1/final0, unsupported=0, lookup<=1e-12 and every primary reproduction error<=1e-12.

If retry PASS: independently download/hash all artifacts, enforce exact source/provenance identity, exact 64 ordering, lifecycle, lookup, every per-atom reproduction guard and downstream-closed flags before recording support PASS `+0/+0`.

If retry repeats the reproduction failure: stop retries; do not relax the gate. Record top-64 census BLOCKED by hosted numerical reproducibility and freeze a separate support-only cross-VM reproducibility diagnostic.

## 6. Auto-research / anti-idle state

`DSIR Continuous Research` is enabled hourly and was rechecked in this iteration. Its prompt explicitly requires repository recovery first, continuous terminal-result consumption, anti-duplication, safe parallel runner utilization and fail-closed science. Chat and automation are therefore aligned on the same current front.

While the unique heavy top-64 retry remains active, independent support-only runners were productively filled with the six nonduplicating analyses above plus two independent terminal consumers. No second heavy science copy was launched.

Stale superseded self-hosted run `34550495778 / 103112190909` remains historical and must not receive home-runner ownership.

## 7. Readiness and exact next gate

**ARTICLE3_REPOSITORY_READINESS: 68%.**

Funnel-freeze readiness: **67%**.

Neither percentage changes because both new packages are support-only `+0/+0` and do not close the frozen Layer-B scientific gate.

Exact next action: continue tracking the one active top-64 retry. On terminal state, consume and independently verify its machine artifact in the same iteration. Do not execute 32769, covariance restriction or Wm_S3, and do not alter any frozen science setting to rescue the support census.
