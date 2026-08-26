# Research checkpoint — Exp067D CAMB transfer precision mechanism

Date: 2026-08-26

## Result

Exp067D was preregistered before the first precision-mechanism calculation and returned:

`FLOAT32_TRANSFER_PRODUCT_CAUSALLY_CONFIRMED_V0_1`

Run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/32998129409

Artifact: `9617429413`, SHA256 `b0377ab357f751d4703526cfb4c9aa0e925dc58c3f9f4b19662fc662f932a6d9`.

The native official CAMB coherence defect on the Exp067C support is

\[
E_{off}=1.616012643701481\times10^{-7}.
\]

Using the exact same stored `float32` `delta_nonu` and `Weyl` transfer values and explicitly reproducing the first multiplication in float32 gives

\[
E_{32}=1.616012642591258\times10^{-7}.
\]

The maximum absolute difference between the full official and reconstructed residual fields is only

\[
6.661338147750939\times10^{-16}.
\]

The remaining common factor inferred independently from `P_mm/mm32`, `P_Wm/wm32`, and `P_WW/ww32` agrees to maximum relative spread

\[
4.440892098500626\times10^{-16}.
\]

When the same already-stored float32 transfer values are promoted to float64 before the first multiplication, the rank-one coherence residual is identically zero on the retained native cells at the precision reported by NumPy:

\[
E_{64}=0.
\]

## Causal chain

Pinned CAMB stores `MatterTransferData%TransferData` as default Fortran `real` and exposes it through Python as `c_float`. `Transfer_GetUnsplinedPower` multiplies two such transfer values and only then combines the product with double-precision factors and stores it in a `real(dl)` power array. Exp067D reproduces the official coherence residual from precisely this float32-first operation.

Therefore the `O(10^-7)` coherence floor that made Exp067B fail is a numerical product-rounding property of this pinned CAMB transfer/power path, not a spline artifact and not evidence of a physical failure of the Weyl/matter convention.

## Scientific boundary

Exp067B remains permanently `FAIL_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1`; its frozen `5e-8` raw-CAMB coherence requirement is not changed. Exp067D explains why that criterion was below the attainable numerical floor of the pinned implementation.

A new convention gate, if used, must be separately preregistered. It may require the causal precision signature to remain bounded/reproducible instead of pretending that raw CAMB power products can satisfy machine-precision rank-one coherence.

Top-level state remains: **G7 OPEN, G8 OPEN, G9 OPEN**. No fresh withheld dark-sector family has been selected.
