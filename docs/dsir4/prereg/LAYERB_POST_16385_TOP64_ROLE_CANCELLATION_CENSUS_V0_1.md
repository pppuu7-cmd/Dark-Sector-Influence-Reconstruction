# LAYERB post-16385 top-64 role-cancellation census v0.1

Status: prospectively frozen after independent terminal consumption of the exact-hotspot/top-1 decomposition chain and before any top-64 role-level recomputation.

## Purpose
Test whether the deterministic cancellation mechanism localized at the global hotspot is isolated or systematic across the already-frozen `top_64_response_atoms` ranking from the exact 441-call hotspot artifact. This is a support-only root-cause diagnostic (`+0/+0`). It cannot create scientific authority, authorize a denser grid, authorize covariance restriction, or open Wm_S3.

## Frozen source and selection
- Exact-hotspot source run: `34592951737`, artifact `10266223990`, source head `5f202de811c07c020100055a63391b7225358670`.
- Source artifact ZIP SHA256: `c836ed5f8b7d6b8c954c99d25a561b0544b049263589d88e3f4fec2fd8297e23`.
- Source `result.json` SHA256: `4023403aaae03481507f778ce4a85c119160cebd785c9c91a534260783049394`.
- Terminal top-1 authority: `docs/dsir4/authority/LAYERB_POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_AUTHORITY_V0_1.json`.
- Atom selection is exactly the complete ordered `source_result.top_64_response_atoms` list. No atom may be added, removed, reordered, threshold-selected, or manually chosen after seeing role-level output.

## Frozen numerics
Preserve exactly the current canonical 8193 and 16385 node payloads, CLASS-IV source `ac627d54e9ce196a08878d1ba33999819925d19c`, execution-only input-capacity and history-suppression patches, `h=1e-4`, native kpd20, centered-cubic interpolation, baseline/precision inputs, lookup tolerance `<=1e-12`, and 8 role-major constructions total (4 per grid, max one live). Do not evaluate alternative h, tolerance, grids, masks, interpolation, estimator, or solver parameters.

For each of the 64 frozen atoms, measure the four raw roles (`reference`, `alpha_minus`, `beta_plus`, `beta_minus`) on both canonical grids and derive the same alpha/beta numerators and responses as the top-1 decomposition. The atom's primary component is fixed by its source `component_index`.

## Frozen outputs
For every atom record:
- source block/call/target/z/k/component identity;
- source response discrepancy;
- cross-grid relative difference for each raw role;
- alpha and beta numerator/response cross-grid relative differences;
- alpha/beta cancellation scales on each grid;
- primary-component recomputed discrepancy and reproduction error relative to the source atom.

Aggregate only prospectively defined summaries: exact 64/64 identity count, maximum/median primary reproduction error, maximum raw-role relative discrepancy, minimum cancellation scale, count of source atoms with response discrepancy >=1e-3, and Spearman rank correlation between `log10(cancellation scale)` and `log10(primary response discrepancy)` for finite positive values. Correlation is descriptive only and has no acceptance threshold.

## Fail-closed validity gate
PASS `POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0` requires: exact source/provenance identities; exact 64 ordered atoms; 8/max1/final0 lifecycle; all selected evaluations valid; unsupported=0; max lookup<=1e-12; bitwise z/k reconstruction from stored binary64 hex; and each recomputed primary response discrepancy reproduces its frozen source discrepancy to relative error <=1e-12 (absolute zero-to-zero accepted). Any structural/provenance/evaluation mismatch is infrastructure FAIL `+0/+0`, not a scientific result.

## Downstream closure
Regardless of outcome: `scientific_authority_created=false`, `scientific_107_row_replay_executed=false`, `next_rung_authorized=false`, `covariance_restriction_authorized=false`, `Wm_S3_opened=false`. No 32769 execution is authorized by this census.
