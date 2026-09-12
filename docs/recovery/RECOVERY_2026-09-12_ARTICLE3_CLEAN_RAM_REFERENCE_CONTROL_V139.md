# DSIR Article III recovery V139 — clean-RAM 32769 reference control prepared

Date: 2026-09-12. Scope: **DSIR only**. V138 and all earlier recovery notes remain immutable history.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`.

Frozen science remains unchanged: `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, same physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup mismatch `<=1e-12`.

No 16385->32769 scientific execution is authorized or has occurred. `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`. No real durable resource authority, actual live-guard PASS or current-run-only authorization exists. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Why V139 was opened
V138 tested standard GitHub-hosted parser-corrected 32769 resource probes with added swap. Those runs are valid only as infrastructure/resource evidence; added swap can create severe paging/thrashing and therefore cannot be used to infer that a sufficiently large physical-RAM machine would fail.

V139 narrows the interpretation and prospectively prepares a cleaner control: exactly one `reference` role, no scientific transfer-value readout, on an isolated high-memory runner with a nominal-64-GiB-class physical-RAM envelope and swap disabled before runner execution.

The 64-GiB-class envelope is **not** an inferred minimum-RAM claim. The machine-checkable guard is `MemTotal >= 62914560 kB` and `SwapTotal == 0` solely to remove the V138 swap confound with a large physical-RAM margin.

## Frozen clean-RAM control
Contract:
- `docs/dsir4/contracts/LAYERB_32769_CLEAN_RAM_REFERENCE_CONTROL_CONTRACT_V0_1.json`
- creation commit `07843216e14937952a920e11ffc68f9181c9f392`
- Git blob `eec2eed8dc9af0b1bf0320ef310fe362e8172910`.

Dormant manual workflow:
- `.github/workflows/layerb-32769-clean-ram-reference-control-v0-1.yml`
- creation commit `47d822d2429e04158b8fa620e023d8a9613a804d`
- Git blob `59dcf6886512f5f6a1076c9196801477c0642347`.

The workflow:
- routes only to `[dsir-32769-highmem]`;
- verifies the same frozen dedicated-runner registration receipt / `--no-default-labels` provenance used by the V137 route;
- requires `MemTotal >= 62914560 kB`;
- requires `SwapTotal == 0` before compute;
- does **not** execute `mkswap`, `swapon`, `swapoff`, create a swapfile or otherwise mutate swap;
- builds the pinned CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c` with point capacity `32769` and parser capacity `1048576` under the same frozen compatibility/public-exposure patches;
- executes exactly one `reference` call through frozen `ci/layerb_32769_parser_1mib_single_role_candidate_probe_v0_2.py`, Git blob `f8776ae1e9e0c325f1a3f5f01b4388e1c93ef7e2`;
- records memory telemetry only;
- reads no scientific transfer values and computes no convergence metric;
- cannot create high-memory lifecycle PASS, durable resource authority, successor authorization or scientific authority.

A clean-reference PASS is therefore only a resource-control result. A FAIL remains infrastructure/resource evidence only.

## Independent static/synthetic audit
Audit workflow:
- `.github/workflows/layerb-32769-clean-ram-reference-control-static-audit-v0-1.yml`
- Git blob `c0c924bb9e4ddbd4453fbc1941fee2a34ff2ca35`.

Run `34663080404` executed three independent hosted lanes in parallel and one barrier finalizer:
- contract/negative-gate audit job `103469460283`: SUCCESS;
- dormant workflow/no-swap-mutation audit job `103469460241`: SUCCESS;
- frozen probe identity/semantics audit job `103469460205`: SUCCESS;
- independent finalizer job `103469483188`: SUCCESS.

Artifact:
- ID `10287942224`;
- ZIP SHA256 `ff80beaa01c62fd5ae471255da38eca534f70e80f96366596804f2d7a1ae3161`;
- raw `summary.json` SHA256 `cdbbde5ea8d6ff6a534d8cd8fbd7ca0e0aa6795e3f75c54bba4868be894ff718`;
- classification `LAYERB_32769_CLEAN_RAM_REFERENCE_CONTROL_STATIC_AUDIT_PASS_PLUS_0_PLUS_0`.

The raw artifact was consumed after CI completion. It records all three prerequisite lanes `success`, requires a real runner, requires role `reference`, `required_min_memtotal_kb=62914560`, `required_swap_total_kb=0`, and explicitly keeps both `clean_reference_execution_authorized=false` and `scientific_execution_authorized=false`.

Durable authority:
- `docs/dsir4/authority/LAYERB_32769_CLEAN_RAM_REFERENCE_CONTROL_STATIC_AUDIT_V0_1.json`
- creation commit `b30cde8957583258e8cfa0cd9daf908352ee838e`
- Git blob `3ddf7095540129febcb0c5612f00970e32b214c2`.

## Correct interpretation of V138 after V139
V138 remains valid and immutable, but its scope is narrow:
- it rules out the specific tested standard-hosted +8/+12 GiB added-swap configurations as successful resource routes;
- it does not show that physical-RAM-only 32769 compute would fail;
- it does not establish an exact RAM threshold;
- it does not contribute a scientific response or convergence classification.

V139 therefore inserts a cleaner reference-only physical-RAM control before spending a qualifying high-memory machine on the full four-role V0.3 lifecycle.

## Remaining blockers and exact order
1. Attach/configure one real isolated runner with unique name, frozen configurator, `--no-default-labels`, exact label `dsir-32769-highmem`, `MemTotal >= 62914560 kB`, and `SwapTotal == 0` before runner start.
2. Dispatch **exactly one** dormant `layerb-32769-clean-ram-reference-control-v0-1` run.
3. Consume and independently classify its artifact. A PASS only establishes that parser-corrected 32769 `reference` can complete under clean high-physical-RAM conditions.
4. Only after that PASS may the project decide prospectively whether to dispatch the existing V0.3 four-role resource lifecycle on the same qualifying machine. The clean-reference result itself does not auto-authorize this.
5. The V137 downstream candidate/materialization/promotion/live-guard/authorizer/scientific/terminal chain remains frozen and dormant until a real four-role resource lifecycle PASS and durable resource authority exist.
6. Canonical 16385->32769 scientific execution remains forbidden until those gates are satisfied.

Old superseded run `34550495778` / job `103112190909` remains queued on generic `[self-hosted, Linux, X64]` and must not receive the dedicated runner.

## Readiness
`ARTICLE3_REPOSITORY_READINESS: 68%`.

Funnel-freeze/scientific frontier: `67%`.

`WORKING_PLAN_COMPLETION: 89%`.

The increase from V138 88% to V139 89% is operational only: the swap-confound concern has been converted into a prospectively frozen, independently audited clean-RAM reference control. No scientific convergence result has advanced.

## Exact next action
Do not run more standard-hosted swap experiments. Do not run the four-role lifecycle first. Attach a qualifying physical high-memory runner with swap disabled and execute exactly one clean-RAM `reference` control. Production science remains forbidden.
