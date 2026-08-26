# Research checkpoint — Exp067C CAMB native coherence localization

Date: 2026-08-26

## Frozen lineage

Exp067B remains the permanent result `FAIL_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1`. Its only failed preregistered criterion was CAMB rank-one coherence against `5e-8`; the three CAMB↔CLASS power comparisons themselves were all within 0.93% in max absolute log difference.

Exp067C was preregistered after Exp067B was merged and before the first native-grid diagnostic. It inherited the same CAMB pin, cosmology, variables, physical units, target cells, coherence definition and `5e-8` threshold.

## Exp067C result

Run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/32997216952

Artifact: `9617073194`, SHA256 `836c6f0306a34a52af3b4948d525b08e3cb892f5a2dc06b923fb1dc30c5d1bfa`.

Classification:

`NATIVE_CAMB_COHERENCE_DEFECT_V0_1`

For

\[
\rho^2=P_{Wm}^2/(P_{WW}P_{mm}),
\]

raw native CAMB powers on every native k node in `0.005 <= k <= 0.2 Mpc^-1` gave

\[
E_{native}=\max|\rho^2-1|=1.616012643701481\times10^{-7},
\]

at `z=2`, `k=0.12632564157247544 Mpc^-1`, signed residual `-1.616012643701481e-7`.

The CAMB `PkInterpolator` evaluated back on those same native knots gave `1.6160126170561284e-7`; its maximum reconstruction errors relative to raw powers were only `9.09e-15` (`P_mm`), `7.21e-15` (`P_Wm`) and `2.25e-14` (`P_WW`). Therefore interpolation is not the origin of the failed coherence criterion.

The original Exp067B target nodes were reproduced exactly in the scalar maximum: `9.253183930191256e-8`, with absolute reproduction difference `0`.

## Source-level mechanism clue

Pinned CAMB source now gives a concrete mechanism:

1. `CAMBdata_GetLinearMatterPower` calls `Transfer_GetUnsplinedPower`.
2. `Transfer_GetUnsplinedPower` constructs cross/auto powers from `M%TransferData(s1)*M%TransferData(s2)` times a common factor.
3. In `fortran/classes.f90`, `MatterTransferData%TransferData` is declared plain `real`, whereas the destination `PK` and later power structures use `real(dl)`.

Thus the first multiplication is performed from single-precision transfer values before promotion into the double-precision power output. An `O(1e-7)` rank-one defect is quantitatively plausible from float32 rounding and matches the measured scale.

This is not yet promoted from source diagnosis to causal proof. Exp067D must mechanically reconstruct the official native powers from float32 transfer products and compare them with a pre-multiplication float64 promotion control.

## Next experiment

Exp067D should be a precision-mechanism audit only, with no relaxed Exp067B threshold and no G7 law fit. It should establish whether:

- float32 transfer multiplication reproduces the official CAMB `rho^2-1` field;
- casting the same transfer values to float64 before multiplication restores rank-one coherence to near machine precision;
- the CAMB↔CLASS physical convention comparison remains conceptually valid even though Exp067B itself remains a frozen FAIL.

Top-level state: **G7 OPEN, G8 OPEN, G9 OPEN**.
