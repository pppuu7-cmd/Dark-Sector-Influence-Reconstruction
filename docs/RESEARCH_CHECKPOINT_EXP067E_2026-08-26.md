# Research checkpoint — Exp067E CAMB↔CLASS out-of-sample physical power convention

Date: 2026-08-26

## Immutable lineage

Exp067B remains permanently `FAIL_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1` because its preregistered raw-CAMB rank-one coherence threshold was below the numerical floor of the pinned CAMB implementation. Exp067C localized that floor to native CAMB powers, and Exp067D causally reproduced it from float32-first transfer multiplication.

Exp067E was preregistered before the first R1/R2 CAMB↔CLASS comparison. It did not relax the failed Exp067B threshold. Instead it prospectively tests the corrected physical convention on two frozen out-of-sample LambdaCDM references while requiring the independently established CAMB precision signature to reproduce.

## First scientific run

Run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/32998659859

Job: `98274406590`

Artifact: `9617676816`

Artifact SHA256: `6e6419040b7295dfe4b1b4c126a5cfeaa6e1e24a76a7e29c05ccd7c706f65ee2`

Result:

`PASS_CAMB_CLASS_OUT_OF_SAMPLE_POWER_CONVENTION_V0_1`

## Spectral convention results

The frozen per-spectrum requirement is `max |Delta ln P| <= 0.03`.

Regression anchor R0:

- `D_mm = 0.009223043583295664`
- `D_WW = 0.00922303413236992`
- `D_Wm = 0.009222993947731269`

Fresh R1 (`h=0.72`, `omega_b=0.0220`, `omega_cdm=0.1050`, `A_s=2.00e-9`, `n_s=0.970`):

- `D_mm = 0.00881946838483925`
- `D_WW = 0.008819302225434025`
- `D_Wm = 0.008819398432905792`

Fresh R2 (`h=0.62`, `omega_b=0.0230`, `omega_cdm=0.1350`, `A_s=2.20e-9`, `n_s=0.960`):

- `D_mm = 0.008589973300161178`
- `D_WW = 0.00858999166527139`
- `D_Wm = 0.008589951688828657`

All cross-spectrum signs match on all frozen target cells.

CLASS built-in Weyl power versus the explicit `q_W^2 P_mm` construction stays at `6.66e-16` to `8.88e-16`, far below the frozen `1e-10` control.

## CAMB precision-signature control

The independent Exp067D mechanism reproduced on all three references.

- R0 official native coherence floor: `1.616012643701481e-7`; float32 reconstruction field match `6.66e-16`; promote-before-product residual `0`.
- R1 official native coherence floor: `1.6329542074089431e-7`; float32 reconstruction field match `6.66e-16`; promote-before-product residual `0`.
- R2 official native coherence floor: `1.6987003437218817e-7`; float32 reconstruction field match `6.66e-16`; promote-before-product residual `0`.

Common-factor reconstruction spread is at most `5.55e-16`, far below the frozen `5e-12` requirement.

The deliberately wrong missing-k^2 convention is rejected strongly for every reference: median absolute log discrepancy remains about `11.98`, versus the frozen minimum `5`.

## Scientific meaning

Exp067E prospectively certifies the corrected physical CAMB↔CLASS Weyl/matter power convention over the preregistered LambdaCDM reference envelope. This removes the physical power-normalization ambiguity that blocked use of CLASS-like solver outputs in the solver-neutral ACT projection interface.

It does **not** establish a dark-sector law, does not reclassify Exp067B, and does not close G7/G8/G9.

## Next required barrier

Before constructing a nuisance quotient or any G7 relation, perform a physical ACT×unWISE forward-operator reproduction gate on a pinned LambdaCDM reference using real CAMB spectra and real released tracer kernels. The test must compare the pinned upstream raw `gg` / `kappa g` projection against `src/dsir/act_unwise_projection.py` under one frozen linear/no-CLEFT contract. Only after that physical projection adapter is validated should the 26D nuisance tangent quotient be frozen.

Top-level state: **G7 OPEN, G8 OPEN, G9 OPEN**. No fresh withheld dark-sector family has been selected.
