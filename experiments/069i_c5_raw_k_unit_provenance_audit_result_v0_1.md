# Exp069I — C5 raw-k unit provenance audit result v0.1

**Date:** 2026-08-27  
**Execution status:** COMPLETE  
**Scientific classification:** `PASS_C5_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1`

## Immutable provenance

- preregistration commit: `6b12a22e6b1bfe91f8863b5705b479dbcd640c83`;
- implementation merge/head: `fa32b651d0c05042a6743e71e373ea13d91c9aa7`;
- workflow run: `33026608144`;
- artifact: `9628710949`;
- artifact digest: `sha256:1eccd4fffc16842ebbf9c61a7f4103dd190da94de9ad9c2b901c6536f4edb71c`;
- pinned upstream: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

No acceptance condition was changed after execution.

## U1 — default accessor semantics: PASS

For `mm`, signed `Wm`, and `WW`, the historical call with omitted `k_hunit` is exactly array-identical to explicit `k_hunit=True` for

- returned k coordinates;
- returned redshifts;
- returned power arrays.

Therefore the pinned runtime confirms that the omitted argument uses the CAMB default `k_hunit=True`.

## U2 — physical-k conversion: PASS

The frozen cosmology has

`h = H0/100 = 0.67`.

For every raw node in all three blocks,

`k_default * h = k_physical`

with maximum measured relative discrepancy

`0.0`

against the frozen representation guard

`64*eps(float64) = 1.4210854715202004e-14`.

The explicit `k_hunit=False` raw support spans, identically for all three blocks,

`2.356798031541985e-6 <= k/(Mpc^-1) <= 0.30060546547174455`.

The historical/default coordinate spans

`3.51760900230147e-6 .. 0.4486648738384247`,

which is the corresponding `k/h` coordinate.

Power arrays are exactly unchanged by this coordinate-unit choice.

## U3 — target-grid immunity: PASS

The Exp069H target interpolator explicitly used `k_hunit=False`.

Every frozen target node

`k = [0.003,0.01,0.03,0.10,0.20] Mpc^-1`

lies inside the explicit physical raw support for `mm`, `Wm`, and `WW`.

Therefore the historical raw-coordinate label issue does not affect Exp069H target-grid acceptance metrics.

## U4 — historical label classification

Frozen classification:

`HISTORICAL_LABEL_INCORRECT_VALUES_ARE_K_OVER_H`.

The old immutable Exp069F/H JSON field named `raw_k_Mpc^-1` is a metadata-label error: its values came from the default `k_hunit=True` accessor and represent the CAMB `k/h` coordinate. The immutable artifacts are not rewritten.

Future provider products must request `k_hunit=False` explicitly whenever the coordinate is labelled `Mpc^-1`.

## U5 — preserved science classifications

Unchanged:

- Exp069B: `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`;
- Exp069F: `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`;
- Exp069H: `PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`.

The reason Exp069H remains valid is exactly the preregistered one: target-grid metrics already used physical `k_hunit=False`, while raw closure/repeatability metrics compare powers on identical native nodes and are invariant under the common coordinate rescaling.

## Consequence

Exp069I removes the unit/provenance barrier to **preregistering/evaluating the physical provider-support intersection** using explicit physical k coordinates.

It does not itself define an observational angular-coordinate validity mask and does not authorize a G7 relation fit.

## Gate state

- C3 provider: certified;
- C5 provider: certified;
- raw-k unit provenance: certified;
- G7: `OPEN`;
- G8: `OPEN`;
- G9: `OPEN`.
