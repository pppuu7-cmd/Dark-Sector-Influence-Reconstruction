# Layer-B post-16385 top-1 role cancellation decomposition V0.1

Status: **PROSPECTIVELY FROZEN / CONDITIONAL / NOT YET EXECUTION-AUTHORIZED**. Frozen while exact 441-call hotspot run `34592951737` is still active and before any terminal hotspot response is read.

## Purpose
If and only if the independently validated exact-hotspot terminal result reproduces the authoritative full-traversal plateau, decompose the single objectively selected maximum response atom into the raw four finite-difference role values on canonical 8193 and canonical 16385. The sole purpose is to identify whether the already-observed grid sensitivity is created primarily in the one-sided alpha numerator, the symmetric beta numerator, or the division/cancellation scale; this is support-only root-cause work.

## Activation gate
Execution is permitted only after all of the following are independently verified:
1. source exact-hotspot classification `POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_PASS_PLUS_0_PLUS_0`;
2. terminal validator classification `POST_16385_EXACT_HOTSPOT_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0`;
3. `exact_hotspot_provenance_reproduced=true` with relative reproduction error `<=1e-12`;
4. source structural receipts: 441 shared calls, 377 DES, 64 BOSS GL64, shared plan bitwise-identical, 8 constructions/max-live1/final0, unsupported=0, lookup<=1e-12;
5. no duplicate active decomposition run.

If the hotspot terminal validator instead reports provenance mismatch or invalid infrastructure, this decomposition **must not run**. Only process/infrastructure diagnosis is then allowed.

## Deterministic atom selection
No human/result-driven choice is allowed. Select exactly `source_result.top_64_response_atoms[0]`. Freeze and replay its exact:
- `call_index` and `block`;
- binary64 `z` via `z_binary64_hex`;
- `target_index` and binary64 target `k` via `target_k_binary64_hex`;
- `component_index` / component name.

The selected atom must also equal `recomputed_shared_atom_global_max` and the maximum of all 441 call maxima. Any identity mismatch is infrastructure failure.

## Frozen numerical configuration
Use exactly the same scientific numerical settings as the authoritative 8193->16385 and exact-hotspot executions:
- canonical 8193 payload SHA256 `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`;
- canonical 16385 payload SHA256 `3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975`;
- CLASS-IV source commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- execution capacities 18432 / parser 524288 and the same execution-only history suppression/build compatibility/public d_m exposure;
- frozen `h=1e-4`, native `k_per_decade_for_pk=20`, centered-cubic interpolation and lookup tolerance `1e-12`;
- same baseline/precision and same four roles `reference`, `alpha_minus`, `beta_plus`, `beta_minus`;
- one live solver maximum; four constructions per lattice, eight total;
- no alternative h, no changed grids, no changed interpolation, no tolerance rescue.

## Receipts to record
For the selected atom and each lattice, record the raw centered-cubic `d_m` value for all four roles and exact finite-difference constituents:
- alpha one-sided numerator `alpha_minus - reference` and response `abs(numerator / -h)`;
- beta symmetric numerator `beta_plus - beta_minus` and response `abs(numerator / (2h))`;
- raw cross-grid relative differences for each of the four role values;
- cross-grid relative differences for each numerator and final response;
- absolute numerator magnitudes and cancellation scale ratios needed to quantify amplification;
- exact z/k binary64 identities, stencil validity and lookup receipts;
- lifecycle 8/max-live1/final0.

The selected component from the hotspot result determines which response is the primary target, but both alpha and beta decompositions are recorded at the same atom to avoid a second result-driven selection.

## Scientific authority
This diagnostic is support-only `+0/+0`. It does not rerun the 107-row scientific classification, cannot alter the already-authoritative NOT_CONVERGED result, cannot authorize canonical 32769, cannot authorize covariance restriction and cannot open Wm_S3. No next scientific branch may be inferred automatically from the numerical values; any follow-up must be separately prospectively frozen.
