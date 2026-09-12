# DSIR recovery V143 — canonical 32769 chunk method PASS

Date: 2026-09-12. Scope: **DSIR only**.

## Scientific frontier remains unchanged

Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, with max relative component difference `0.012484060640679777` against the frozen strict `<1e-3` gate.

No 16385->32769 convergence metric has yet been computed. Covariance restriction remains unauthorized. `Wm_S3` remains unopened.

## New V143 result — exact 32769 partition invariance

Prospectively frozen contract: `docs/dsir4/contracts/LAYERB_32769_BLINDED_PARTITION_INVARIANCE_CONTRACT_V0_1.json`, blob `8f6d84afef41e594c4e4845f4e44abd4a31fd530`, creation commit `456cb482fe38c4b2b917e990328c1787da8b77d6`.

Workflow run `34667606794` at launch commit `73e6c5bffd8fb365f163422c41979daf71a129c0` completed successfully: static audit `103482605453`; roles reference `103482625030`, alpha_minus `103482625087`, beta_plus `103482625067`, beta_minus `103482625085`; independent finalizer `103486143091`.

Two materially different, predeclared partitions of the same canonical 32769 lattice were evaluated under the unchanged `<=1e-12` numerical-method gate:

- A: 8 contiguous 4096-ish chunks;
- B: 9 contiguous 3641-node chunks.

For every one of the four frozen roles and all six frozen z probes:

- coordinate order exact = true;
- all response values finite = true;
- max requested-node coordinate relative mismatch = `1.656870599154541e-16`;
- max normalized response difference = `0.0`;
- max absolute response difference = `0.0`;
- exact binary64 fraction = `1.0`.

Aggregate artifact `10290710129`, ZIP SHA256 `518927ed71c9acac5fe75d071697f2aafe589c7e213758fdbb59956726cd22d5`, consumed `aggregate.json` SHA256 `d7dbd640feb5ae173d2fa7bf4cad79a3776369b6c32bb68762aff21558076a2a`.

Role artifacts and independently consumed comparison hashes:

- reference: artifact `10289956389`, ZIP `899f8ff79119e489941a407a6f7eafec1c0f47879a2cec7b710c4a0da535573d`, comparison SHA256 `b594a8a8098f2ec959dee05ac02a3a7114acbb43266267e89fbe3a91663f8a35`;
- alpha_minus: artifact `10290615775`, ZIP `516af4e4abf6689f77983091f508e583d94ecbf47ec7a2eebc69b81dc15d3f43`, comparison SHA256 `0534c88a6580dbab9ea5612f7eaf82c6939f1d45340bc6f9c204c6200239d8e9`;
- beta_plus: artifact `10289009891`, ZIP `f62d2449d2391a74d611b3c9667f48146baea79446b78d3104e1d4b054b338ae`, comparison SHA256 `c453a66fd6a592133d0f754da1c639437e669ecd8abb8ea4df2b253e459f6bce`;
- beta_minus: artifact `10290145832`, ZIP `03cc1c0d31a6f20f9ad3dfe8b742ae5a970ed7001801409ec6a1e30e9835035e`, comparison SHA256 `68d3509f88a0e2108a1f30e40fee4b43d5b53052302e63291d3e83c79826f85b`.

Scientific response vectors were transient inside the role jobs, were not uploaded or committed, and were deleted before artifact upload. No 16385 comparison or convergence classifier ran.

Durable authority: `docs/dsir4/authority/LAYERB_32769_BLINDED_PARTITION_INVARIANCE_V0_1.json`, creation commit `419d3c49294dabde48d9e3994acc6ebef18f621e`.

## Interpretation

This is strong `+0/+0` numerical-method evidence: at canonical 32769 the requested-node transfer response is invariant, bit-for-bit in the tested probes, to two materially different chunk partitions. Together with V141 exact 8193 monolithic-vs-chunk equivalence and V142 all-eight chunk resource PASS, the tested chunk acquisition route has closed its resource and partition-method blockers.

It does **not** by itself authorize or reveal the physical 16385->32769 convergence result.

## Minimal scientific delta for the successor

The frozen parent production engine already separates response acquisition from the scientific replay/classifier. The minimal successor must therefore preserve the old request-plan traversal, the same canonical 16385 and 32769 lattices, same four roles, `h=1e-4`, native kpd20, centered-cubic interpolation, same 107-row parent accounting, unsupported=0, lookup `<=1e-12`, invalid fraction `<=0.05`, retained `>=15`, and strict `max_relative_component_difference < 1e-3`.

Only the fine-lattice acquisition layer may change: instead of one monolithic 32769 CLASS instance per role, assemble the exact full canonical requested-node transfer table from the prospectively frozen low-capacity chunks, then apply the same interpolation/request replay and unchanged classifier.

Before production, freeze a current-run-only chunk-science authorization binding V141 + V142 + V143 and statically audit that no scientific threshold or downstream covariance/Wm_S3 rule changes.

## Readiness

`ARTICLE3_REPOSITORY_READINESS: 68%`.

Funnel-freeze/scientific frontier: `67%`.

`WORKING_PLAN_COMPLETION: 93%`.

The +1 point is operational/methodological only. Scientific readiness remains unchanged until the first authorized 16385->32769 convergence result is independently classified.

## Automation

`DSIR Continuous Research` remains disabled because the account already has five active automations; an enable attempt returned the five-task limit. GitHub Actions/repository state is the active DSIR compute mechanism.
