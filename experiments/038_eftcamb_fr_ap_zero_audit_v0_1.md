# Experiment 038 — H-EFTCAMB designer-f(R) AP-zero audit v0.1

**Date:** 2026-08-25  
**Status before hard run:** protocol frozen; result pending  
**Scope:** C5 background/AP contract only

## Purpose

Experiment 036 left the C5 designer-f(R) AP geometry cell masked rather than assuming zero. The frozen C5 configs use `EFTwDE=0`, suggesting a Lambda-like background, but DSIR forbids converting that expectation into a zero-valued observation cell without an explicit analytic or numerical contract.

Experiment 038 therefore reruns the **same pinned high-precision H-EFTCAMB C5 configurations** and preserves the background files that the earlier hard MG-S1 artifact did not upload. It compares the full saved background geometry with the same-solver GR reference and maps `H(z)` through the validated Experiment 035 AP operator.

A PASS allows the C5 AP geometry cell to be encoded as validated zero. A FAIL is retained as a scientific result and the nonzero background response must be propagated instead.

## Immutable provenance

Pinned upstream:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Exact frozen C5 hard-production configuration artifact:

- source workflow run `32759477319`;
- artifact ID `9532245261`;
- artifact name `eftcamb-mgs1-hard-92350bb5087d17c874626c75b96779ae264dd1f6`;
- digest `sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`;
- preserved hard config lineage `dsir_mgs1_hp_*`.

The audit copies those `dsir_mgs1_hp_*.ini` files from the immutable artifact into a clean checkout/build of the pinned upstream solver. It does **not** reconstruct the C5 cosmology by hand.

## Provenance correction before scientific execution

The first draft of the Experiment 038 workflow referenced the older calibration filenames `dsir_mgs1_*`. Inspection of the exact frozen hard artifact showed that the production lineage is instead `dsir_mgs1_hp_*`. This was corrected before accepting any scientific result from Experiment 038. The AP formulas and pre-frozen numerical thresholds below were unchanged. Any run that fails only because the old filenames do not exist is infrastructure/provenance failure, not a scientific gate result.

## Why a new run is necessary

The pinned upstream source `fortran/eftcamb/10_EFTCAMB_background_output.f90` implements

`CreateFile(TRIM(outroot)//'background.dat')`

when background output is enabled. The frozen `dsir_mgs1_hp_base.ini` has `EFTCAMB_write_background = T`, so the solver is configured to write background files. The previous hard MG-S1 artifact preserved matter-power files and configs but omitted `*background.dat`. Therefore no model redefinition is required; only preservation and audit of the existing upstream output type is missing.

## Models

Same-solver high-precision GR reference:

`EFTflag=0`.

Designer family:

- `EFTflag=3`;
- `DesignerEFTmodel=1`;
- `EFTwDE=0`;
- `EFTB0={0,1e-7,1e-6,1e-5,1e-4,1e-3}`.

The hard script parses these values from each preserved INI and fails if the expected contract is not present.

## Background outputs

The pinned upstream background writer stores columns

`a z tau r Hz DL DA DV DM HzRs DAoRs DVoRs DMoRs`.

The audit checks at minimum:

1. identical redshift sampling against the GR reference;
2. relative `H(z)` response;
3. relative nonzero-row `D_M(z)` response;
4. full-table exact equality as a diagnostic;
5. AP response derived from the full same-solver `H(z)` history.

For the AP layer,

\[
r_E(z)=\ln\frac{H_{f(R)}(z)}{H_{GR}(z)},
\]

and the validated Experiment 035 operator gives

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

The target redshifts are the corrected ShapeFit geometry bins

`z=(0.51,0.71,0.92,1.32,1.49)`.

## Hard thresholds frozen before the first scientific CI output

H-EFTCAMB writes the background table with `ES20.10` numerical formatting. To remain comfortably above text-output rounding while still excluding any physically material geometry deformation, freeze:

- maximum redshift-grid mismatch `<=1e-10`;
- maximum relative `H(z)` mismatch `<=1e-8`;
- maximum relative `D_M(z)` mismatch over nonzero rows `<=1e-8`;
- maximum absolute `Delta ln(D_H/D_M)` at the five target redshifts `<=1e-8`;
- all configuration contracts must pass.

Full numeric-table bitwise equality is recorded only as a diagnostic and is **not** a PASS requirement.

No angular, rank, or significance threshold is defined.

## Scientific interpretation if PASS

A PASS would establish, for the frozen high-precision C5 designer-f(R) manifold,

\[
K_{AP}t_{B_0}=0
\]

to the hard numerical tolerance, while the already established structure response is nonzero. Together with Experiment 037 this would show that both a dark-fluid perturbation family and a modified-gravity family can contain directions that are background/AP-null but perturbation-active.

This would strengthen the DSIR notion of **channel null spaces / block-sparse influence**, but would not prove a universal law.

## Claim boundary

Experiment 038 cannot establish:

- zero background response for arbitrary f(R) or arbitrary modified gravity;
- zero perturbation response (C5 is already strongly nonzero there);
- parameter constraints or detection significance;
- intrinsic response rank;
- a new residual law or discovery.

G5 remains PARTIAL after this experiment unless all other family-complete observational kernels and robustness requirements are separately satisfied. G7 and G8 remain OPEN.
