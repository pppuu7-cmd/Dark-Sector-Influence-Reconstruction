# Exp069I — C5 raw-k unit provenance audit result

Date: 2026-08-27

Scientific classification: `PASS_C5_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1`.

## Provenance

- workflow run: `33026608144`
- execution head: `fa32b651d0c05042a6743e71e373ea13d91c9aa7`
- artifact: `9628710949`
- artifact digest: `sha256:1eccd4fffc16842ebbf9c61a7f4103dd190da94de9ad9c2b901c6536f4edb71c`
- pinned EFTCAMB: `16d9c4e9f85751e30efd0a53b177941713078904`

## Frozen criteria

All three preregistered unit/provenance criteria passed for `mm`, signed `Wm`, and `WW`:

- U1: the historical default accessor is exactly identical to explicit `k_hunit=True`;
- U2: multiplying historical/default k by `h=0.67` reproduces explicit physical k with maximum relative discrepancy `0.0` in the audited arrays;
- U3: every frozen target node remains inside explicit physical raw support.

The explicit physical raw support in the audited ordinary-GR provider is approximately `[2.3567980315e-6, 0.30060546547] Mpc^-1`.

## Metadata correction boundary

Historical Exp069F/H fields labelled `raw_k_Mpc^-1` are classified as

`HISTORICAL_LABEL_INCORRECT_VALUES_ARE_K_OVER_H`.

The historical immutable artifacts are not rewritten. Their raw coordinate values are interpreted as `k/h`. Future products that carry a `Mpc^-1` label must request `k_hunit=False` explicitly.

This is a coordinate-label correction only. No power amplitude, interpolation, normalization, tolerance, or target-grid value is changed.

## Preserved science

- Exp069B remains permanent `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.
- Exp069F remains `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`.
- Exp069H remains `PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`.

The reason Exp069H is preserved is that its raw acceptance compares powers at identical native nodes, while its target-grid criteria already used explicit physical `k_hunit=False` semantics.

## Gate consequence

Both C3 and C5 physical providers are now certified and the C5 raw-coordinate provenance issue is resolved. The already frozen common physical support-validity-mask preregistration may now be executed.

G7 remains `OPEN`; covariance restriction/whitening, nuisance SVD, quotient/relation/null control, G8, and G9 remain blocked until their required predecessors pass.
