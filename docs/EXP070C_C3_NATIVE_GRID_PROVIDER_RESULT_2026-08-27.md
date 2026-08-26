# Exp070C result — C3/GDM native-grid physical power provider

Date: 2026-08-27

## Scientific classification

`PASS_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1`

Exp070A remains permanently `FAIL_C3_GDM_READONLY_DM_PHYSICAL_POWER_BRIDGE_V0_1`. Exp070B remains the mechanism result `INTERPOLATION_DOMINATED`. Exp070C is the separately preregistered corrective provider and does not rewrite either earlier result.

## Immutable provenance

- PR: #79
- preregistration commit: `c66c7bd327a0f13ba8ef732c94482ca6d9ce0b9b`
- implementation/workflow head: `a1f0ce9e02f934acdf79c546abbcbfe76b7fcfbd`
- workflow run: `33017214292`
- artifact id: `9625032179`
- artifact digest: `sha256:34cf89f2207c72b4e3d669f7e4e6419753b6b046ed7de9e3a9fa7fb144b4c081`
- pinned solver: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`

## Frozen test results

All C1-C7 pass.

### C1 — native matter-power closure

Maximum relative provider-vs-native `pk_lin` errors:

- `cs2=0`: `2.6865230296491766e-14`
- `cs2=1e-6`: `2.8144898798669162e-14`
- `cs2=1e-5`: `2.6708846507060602e-14`

Frozen threshold: `1e-10`.

### C2 — native-grid alignment

Every case/redshift retains 33 native common nodes in `0.001 <= k/(h Mpc^-1) <= 0.1`.

Maximum source/transfer representation-level k mismatch:

`1.545552650407278e-16` relative.

All matches are unique and all redshift slices are nonempty.

### C3 — signed Weyl provider contract

All retained `D_m`, `phi`, `psi`, `W`, `q_W`, `P_mm`, signed `P_Wm`, `P_WW` and native `pk_lin` values are finite. `D_m` is nonzero, `P_mm>0`, `P_WW>0`, and `P_Wm!=0` everywhere on the frozen support.

### C4 — same-mode coherence

For all three cases:

`max |P_Wm^2/(P_WW*P_mm)-1| = 4.440892098500626e-16`.

Frozen threshold: `2e-10`.

### C5 — missing-k^2 software negative control

The deliberately wrong fixed-Mpc numerical operator without the variable `k^2` factor is strongly separated and is never promoted to a physical provider. This is an engineering/unit-convention negative control only; its numerical magnitude is not interpreted as a dimensionless physical observable and is not evidence for new physics.

### C6 — repeatability/no mutation

- repeated accessor reads: bitwise identical in every case;
- maximum native `pk_lin` control change after provider reads: `0.0`;
- frozen no-mutation threshold: `1e-12`.

### C7 — output boundary

Schema is complete, native-grid only, and performs no observational projection. The result explicitly keeps `G7=OPEN`, `G8=OPEN`, `G9=OPEN` and does not authorize a common support-validity mask.

## Scientific consequence

C3/GDM now has a validated native-grid physical input provider for

- `P_mm`,
- signed `P_Wm`,
- `P_WW`,

without interpolating `D_m` amplitudes. The earlier ~4.75% Exp070A defect is therefore localized to the rejected DSIR interpolation operator rather than the physical source normalization.

This closes the C3 provider prerequisite only. C5 remains independently unresolved after Exp069B until Exp069C and any justified corrective C5 bridge are completed. Only after both C3 and C5 providers are certified may DSIR preregister the common physical support-validity mask and proceed toward covariance whitening, nuisance SVD, and G7.
