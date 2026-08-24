# Experiment 038 — H-EFTCAMB designer-f(R) AP-zero audit v0.1

**Date:** 2026-08-25  
**Status:** **HARD PASS — `PASS_EFTCAMB_FR_AP_ZERO_AUDIT_V0_1`**  
**Scope:** C5 background/AP contract only

## Purpose

Experiment 036 left the C5 designer-f(R) AP geometry cell masked rather than assuming zero. The frozen C5 configs use `EFTwDE=0`, suggesting a Lambda-like background, but DSIR forbids converting that expectation into a zero-valued observation cell without an explicit source or numerical contract.

Experiment 038 reruns the **same pinned high-precision H-EFTCAMB C5 configurations**, preserves their background files, verifies the pinned source-level LCDM expansion selection, and tests whether changing `B0` alters `H(z)`, `D_M(z)`, or the validated Experiment 035 AP response.

## Immutable provenance

Pinned upstream:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Exact frozen C5 hard-production configuration artifact:

- source workflow run `32759477319`;
- artifact ID `9532245261`;
- artifact name `eftcamb-mgs1-hard-92350bb5087d17c874626c75b96779ae264dd1f6`;
- digest `sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`;
- hard config lineage `dsir_mgs1_hp_*`.

Successful Experiment 038 hard run:

- run `32785800977`;
- status `PASS_EFTCAMB_FR_AP_ZERO_AUDIT_V0_1`;
- result artifact ID `9541598468`;
- artifact SHA256 `24b7fa5951c06d4cea72e6c0bf6baad2d2174f2d86794ec0818cf57c309b81c8`;
- hard head SHA `e8e8b266e1f36bf6086100b156bd40d71ed4d8c2`;
- frozen repository summary `data/derived/observational_whitening/experiment_038_eftcamb_fr_ap_zero_audit_v0_1.json`.

## Source-level background contract

The pinned designer-f(R) source maps

`EFTwDE = 0`

to

`wDE_LCDM_parametrization_1D`.

The pinned neutral parametrization evaluates

\[
w_{DE}(a)=-1
\]

exactly, with zero derivatives. The workflow verifies those exact statements at the pinned commit before running the numerical hard audit.

Thus the frozen C5 `B0` manifold lives on a source-proven LCDM expansion branch.

## Provenance / infrastructure corrections before scientific execution

Several infrastructure assumptions were corrected before the first scientific hard-script result. **No scientific threshold was altered.**

1. The immutable hard artifact showed that the production lineage is `dsir_mgs1_hp_*`, not the older calibration names `dsir_mgs1_*`.
2. The standard `EFTflag=0` branch did not emit the EFT-specific background file through this execution path. Rather than modify upstream physics only for instrumentation, the numerical reference was changed to exact designer `B0=0`, while the pinned source establishes its LCDM background contract. The GR configuration is still rerun and checked as `EFTflag=0`.
3. CAMB appends `_` to a nonempty `output_root`; the frozen roots themselves already end in `_`. Therefore actual files use a double separator, e.g. `dsir_mgs1_hp_b0__background.dat`. This is the same naming convention already present in the frozen matter-power artifact.

These were provenance/file-path repairs only; the hard geometry tolerances below remained fixed.

## Models

Frozen high-precision GR control:

`EFTflag=0`.

Designer family:

- `EFTflag=3`;
- `DesignerEFTmodel=1`;
- `EFTwDE=0`;
- `EFTB0={0,1e-7,1e-6,1e-5,1e-4,1e-3}`.

The numerical background reference is

`dsir_mgs1_hp_b0__background.dat`,

namely exact designer `B0=0` on the same source-proven LCDM branch.

## Hard thresholds frozen before scientific output

- maximum redshift-grid mismatch `<=1e-10`;
- maximum relative `H(z)` mismatch `<=1e-8`;
- maximum relative `D_M(z)` mismatch over nonzero rows `<=1e-8`;
- maximum absolute `Delta ln(D_H/D_M)` at the five ShapeFit geometry redshifts `<=1e-8`;
- all frozen configuration contracts required;
- pinned-source `EFTwDE=0 -> wDE_LCDM -> w=-1` contract required.

Full numeric-table exact equality was diagnostic only, not a PASS requirement. No angular, rank, or significance threshold was defined.

## Hard result

For **every** audited point

\[
B_0\in\{0,10^{-7},10^{-6},10^{-5},10^{-4},10^{-3}\},
\]

the saved numerical background table is exactly equal to the `B0=0` table at saved solver precision. The aggregate diagnostics are

\[
\max |\Delta H/H|=0,
\]

\[
\max |\Delta D_M/D_M|=0,
\]

and

\[
\max_z |\Delta\ln(D_H/D_M)|=0
\]

at the five target redshifts `z=(0.51,0.71,0.92,1.32,1.49)`.

The redshift grids also match exactly and all configuration contracts pass.

Thus the result is not merely below the frozen `1e-8` tolerance; it is a **saved-solver exact zero** over the entire frozen production `B0` grid.

## Scientific interpretation

For the frozen high-precision C5 designer-f(R) manifold,

\[
\boxed{K_{AP}t_{B_0}=0}
\]

on the source-proven LCDM expansion branch, while the already validated C5 perturbation/structure response is nonzero.

Together with Experiment 037, DSIR now has two qualitatively different hard examples of channel-null/block-sparse influence:

1. **GDM closure physics:** `cs2/cv2` directions are background/AP-null but structure/metric-active.
2. **Designer modified gravity:** the `B0` direction is background/AP-null but structure-active.

This strengthens the working hypothesis that an influence trajectory may contain exact channel-null coordinates and that absence of an AP/background response does not imply proximity to the common physical origin in the full response space.

It is still not a universal law: both examples are deliberately constructed families with fixed background contracts, and future families may not share this sparsity.

## Claim boundary

Experiment 038 does **not** establish:

- zero background response for arbitrary f(R) or arbitrary modified gravity;
- zero perturbation response;
- a DESI likelihood or parameter constraint;
- intrinsic response rank;
- a residual law or discovery.

G5 remains **PARTIAL**. G7 and G8 remain **OPEN**.
