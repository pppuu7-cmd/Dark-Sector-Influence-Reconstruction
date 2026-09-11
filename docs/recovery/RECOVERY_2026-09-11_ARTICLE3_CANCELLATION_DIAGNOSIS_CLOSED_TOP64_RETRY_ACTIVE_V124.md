# DSIR recovery V124 — cancellation diagnosis closed; top-64 unchanged retry active

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

This immutable note reconciles the concurrently created V123 recovery records and supersedes both for current-front recovery:
- automation V123: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_TOP1_ARITHMETIC_CLOSED_TOP64_RETRY_ACTIVE_V123.md`, creation commit `c4ae0ca37aafa643f05d69ff1f9ba9717c237edc`;
- parallel-support V123: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_TOP64_RETRY_AND_PARALLEL_CANCELLATION_SUPPORT_V123.md`, creation commit `005badca4ae952a824fd828d86d1806636087cef`.

Both V123 notes and all earlier notes remain immutable history.

## Scientific frontier — unchanged

Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`.

Frozen contract remains unchanged: `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup mismatch `<=1e-12`.

No 32769 execution is authorized. `covariance_restriction_authorized=false`. `Wm_S3_opened=false`.

## Exact hotspot / top-1 authority

The plateau remains localized to the frozen DES beta-response hotspot around call 204 / target 44 / z `0.7475` / k `0.01698756`, component `abs_dDelta_m_dbeta_symmetric`.

Durable top-1 terminal authority:
- `docs/dsir4/authority/LAYERB_POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_AUTHORITY_V0_1.json`
- Git blob `cb0b07bd75208619e681f02528fb0c761ddedabb`
- support-only `+0/+0`.

## Cancellation diagnosis package A — amplification, binary64 replay, ULP sensitivity

Three independent analysis-only jobs ran in parallel from the immutable top-1 authority; no CLASS solver was invoked.

Parallel source run `34624187060`, head `56f9152f4fa775439365a88ea5c2e7b502f1f5eb`.
Artifacts:
- amplification `10273825514`, ZIP SHA256 `5d5a3ef079bff829dcdbb37f6daab6c812e20491920d8d8a6083090cd6b09df8`;
- binary64 replay `10274180314`, ZIP SHA256 `63e8ea8c79c51a1ff6e5ea171c75999904a36c7dbc3e2eb7b88827bb2f03f41d`;
- ULP sensitivity `10274265218`, ZIP SHA256 `313aa832ece4f720bc3946515bab80da9e4310afbdf645223504fc84d8fb44bb`.

Independent terminal consumer `34624280381 / 103345478391`, terminal artifact `10273496144`, ZIP SHA256 `0bb033efea6350679c14d2e53c8e416be17c65633bbc602dda4499c8b3f22f84`.

Durable authority:
- `docs/dsir4/authority/LAYERB_POST_16385_TOP1_PARALLEL_SUPPORT_TERMINAL_AUTHORITY_V0_1.json`
- creation commit `d46ae6e2175502ed9b74444dc8f91fdc48cedb05`
- classification `POST_16385_TOP1_PARALLEL_SUPPORT_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0`.

Validated quantitative findings:
- beta-response relative cross-grid difference `0.012484060640679777`;
- max raw-role relative cross-grid shift `6.885687402119481e-11`;
- response/max-raw-role amplification `181304493.09733495`;
- response/min-raw-role amplification `3194801920.626294`;
- beta cancellation-scale relative difference `0.0124840605726825`;
- ±1 ULP endpoint-neighbor metric range `[0.01248406064067949, 0.012484060640680063]`;
- maximum metric shift from ±1 ULP endpoint perturbations `2.8622937353617317e-16`.

Therefore ordinary rounding of the already-rounded coarse/fine endpoint response values cannot explain the ~`1.248e-2` plateau.

## Cancellation diagnosis package B — subtraction conditioning, signed attribution, Decimal replay

Three independent arithmetic-only jobs ran in parallel from immutable top-1 decomposition artifact `10268078468` (source run `34608169257`, ZIP SHA256 `c0363cb45a54ed9ff634548bd96c539d55757a646d014f83ddd74f10bf62ddb0`); no CLASS solver was invoked.

Parallel run `34624525157`, head `107b453d485a14f8a812539d04abbbf9c63d8885`.
Artifacts:
- condition audit `10274091055`, ZIP SHA256 `d5d196ebb2b63e86a5e750e26f75bc029de410b1c4bfe4725317ebf7a1d11f19`;
- signed attribution `10274026180`, ZIP SHA256 `946342a64a6ae041ac81d1aa85fef5fe7f6a1c2314d03f2dfad4544186b4ada4`;
- Decimal replay `10274565598`, ZIP SHA256 `35a0ed4aeaab9e1ba7c8f3573e124249752716380960893b4e943bf1b17970c8`.

Independent terminal consumer `34624598782 / 103346512972`, terminal artifact `10273886027`, terminal ZIP SHA256 `72e2fb96df45ddb05d49bcd215618a366a08df62c5b386ca88c9ab6118593c26`, terminal payload SHA256 `0273ad038f5b5e13ab1f1598f7d84a829983ea474e379808342a5c2fb63449ef`.

Durable authority:
- `docs/dsir4/authority/LAYERB_POST_16385_TOP1_DECOMPOSITION_ARITHMETIC_TERMINAL_AUTHORITY_V0_1.json`
- creation commit `4392df8fe76680ee6e4bfed7e073263e4729e39f`
- classification `POST_16385_TOP1_DECOMPOSITION_ARITHMETIC_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0`.

Validated quantitative findings:
- beta subtraction condition number on 8193: `207066036.01189664`;
- beta subtraction condition number on 16385: `204481011.0632948`;
- Decimal replay of subtraction from exact stored binary64 operands has zero replay rounding-relative error in the validated terminal receipt;
- signed role shifts exactly recombine to the beta-numerator cross-grid shift, relative residual `0.0`.

Combined interpretation of packages A+B: the local top-1 plateau is strongly consistent with an ill-conditioned finite-difference/cancellation-amplification mechanism. It is not attributable to ordinary endpoint binary64 rounding or to the arithmetic rounding of the subtraction itself. This remains support-only `+0/+0`; it does not modify frozen science or authorize a new rung.

## Top-64 census — only active heavy owner

Attempt 1 of `layerb-post-16385-top64-role-cancellation-census-v0-1`, run `34614119149`, failed prospectively frozen atom-0 primary reproduction (`2.8125401822500933e-06` versus `<=1e-12`) and remains **infrastructure/numerical-reproducibility FAIL +0/+0**, not scientific FAIL.

Exactly one unchanged retry is permitted:
- run `34614119149`, run attempt 2;
- job `103331912096`;
- launch head `6b684ac91c7a261e6b588da1a4922a411bd65614`;
- frozen execution checkout/static-authority head `717a15a615061cea441910d03fdda1f9a4a2b2c2`;
- last rechecked status at V124 creation: **IN_PROGRESS** on GitHub-hosted ubuntu-24.04.

All pre-execution identity/source/hash/numerical-stack/pinned-build guards passed before the long frozen numerical census step. No duplicate top-64 execution is allowed.

Expected PASS token remains `POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0`, exact 64 ordered source atoms, lifecycle `8/max1/final0`, unsupported=0, lookup<=1e-12, every primary reproduction error<=1e-12 and downstream-closed flags.

If attempt 2 PASSes: independently consume/hash all artifacts and enforce the complete frozen machine contract before recording support PASS `+0/+0`.

If attempt 2 repeats the reproduction failure: stop retries; do not relax any threshold. Classify the census BLOCKED by hosted numerical reproducibility and prospectively freeze a separate support-only cross-VM hotspot reproducibility diagnostic.

## Auto-research / runner ownership

`DSIR Continuous Research` is enabled hourly and was explicitly checked during this iteration. It is repository-first, fail-closed, anti-duplicate and requires safe parallelization of independent jobs. Its automation-V123 was reconciled into this V124 rather than overwritten.

While the single top-64 heavy retry is active, six independent nonduplicating support jobs plus two terminal consumers have been run and independently validated, so useful hosted capacity was filled without duplicating the heavy science computation.

Stale superseded self-hosted run `34550495778 / 103112190909` remains historical and must not receive home-runner ownership.

## Readiness / exact next action

**ARTICLE3_REPOSITORY_READINESS: 68%.**

Funnel-freeze readiness: **67%**.

No increase is warranted because the new cancellation diagnosis is support-only and the frozen Layer-B scientific closure remains unresolved.

Exact next action: continue tracking only `34614119149 / 103331912096`. At terminal state, consume its artifact and enforce the original frozen 64-atom contract in the same iteration. Never execute 32769, covariance restriction or Wm_S3, and never alter frozen science to rescue the support census.
