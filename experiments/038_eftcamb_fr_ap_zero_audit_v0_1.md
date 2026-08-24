# Experiment 038 — H-EFTCAMB designer-f(R) AP-zero audit v0.1

**Date:** 2026-08-25  
**Status before successful hard scientific run:** protocol frozen; result pending  
**Scope:** C5 background/AP contract only

## Purpose

Experiment 036 left the C5 designer-f(R) AP geometry cell masked rather than assuming zero. The frozen C5 configs use `EFTwDE=0`, suggesting a Lambda-like background, but DSIR forbids converting that expectation into a zero-valued observation cell without an explicit source or numerical contract.

Experiment 038 therefore reruns the **same pinned high-precision H-EFTCAMB C5 configurations**, preserves their background files, verifies the pinned source-level LCDM expansion selection, and numerically tests whether changing `B0` alters `H(z)`, `D_M(z)`, or the validated Experiment 035 AP response.

A PASS allows the C5 **B0 direction** in the AP geometry block to be encoded as validated zero. A FAIL is retained as a scientific result and the nonzero response must be propagated instead.

## Immutable provenance

Pinned upstream:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Exact frozen C5 hard-production configuration artifact:

- source workflow run `32759477319`;
- artifact ID `9532245261`;
- artifact name `eftcamb-mgs1-hard-92350bb5087d17c874626c75b96779ae264dd1f6`;
- digest `sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`;
- preserved hard config lineage `dsir_mgs1_hp_*`.

The audit copies those exact INI files into a clean checkout/build of the pinned upstream solver. It does **not** reconstruct the C5 cosmology by hand.

## Source-level background contract

The pinned designer-f(R) source explicitly maps

`EFTwDE = 0`

to

`wDE_LCDM_parametrization_1D`.

The pinned neutral-parametrization source evaluates that function as

\[
w_{DE}(a)=-1
\]

exactly, with zero derivatives. The workflow greps these exact source statements at the pinned commit before the hard numerical audit.

Thus the expansion-history choice for this frozen designer branch is source-proven LCDM. The remaining numerical question is whether varying `B0` leaks into the saved background/AP outputs despite that design contract.

## Provenance / infrastructure corrections before scientific execution

Two non-scientific failures were encountered before any Experiment 038 hard script executed:

1. The first draft referenced older calibration filenames `dsir_mgs1_*`; inspection of the immutable hard artifact showed the production lineage is `dsir_mgs1_hp_*`.
2. A later workflow expected an EFT-specific `background.dat` for the standard `EFTflag=0` GR branch. All GR/designer solver runs completed and every designer run reported `EFTCAMB: theory stable`, but the EFT-specific writer does not provide that GR file through this execution path. The scientific script was skipped.

Neither failure inspected or changed the hard geometry tolerances below. Rather than modify upstream physics merely to instrument the GR path, the numerical audit now uses the exact designer `B0=0`, `EFTwDE=0` background as the same-branch numerical reference, while the source-level contract identifies that branch with LCDM expansion.

The frozen GR INI (`EFTflag=0`) is still rerun and its configuration contract is checked, preserving the original common-baseline lineage.

## Models

Frozen high-precision GR configuration:

`EFTflag=0`.

Designer family:

- `EFTflag=3`;
- `DesignerEFTmodel=1`;
- `EFTwDE=0`;
- `EFTB0={0,1e-7,1e-6,1e-5,1e-4,1e-3}`.

The hard script parses these values from each preserved INI and fails if the expected contract is not present.

## Numerical background reference and outputs

The numerical reference is

`dsir_mgs1_hp_b0_background.dat`,

namely the exact `B0=0` point on the same source-proven LCDM designer branch.

The pinned upstream background writer stores columns

`a z tau r Hz DL DA DV DM HzRs DAoRs DVoRs DMoRs`.

For each production `B0` the audit checks:

1. identical redshift sampling relative to designer `B0=0`;
2. relative `H(z)` response;
3. relative nonzero-row `D_M(z)` response;
4. full-table exact equality as a diagnostic;
5. AP response derived from the full same-solver `H(z)` history.

For the AP layer,

\[
r_E(z;B_0)=\ln\frac{H(z;B_0)}{H(z;B_0=0)},
\]

and the validated Experiment 035 operator gives

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

The target redshifts are the corrected ShapeFit geometry bins

`z=(0.51,0.71,0.92,1.32,1.49)`.

## Hard thresholds frozen before the first scientific CI output

H-EFTCAMB writes the background table with finite text precision. To remain comfortably above output rounding while still excluding any physically material geometry deformation, the thresholds were frozen **before a scientific hard-script result existed**:

- maximum redshift-grid mismatch `<=1e-10`;
- maximum relative `H(z)` mismatch `<=1e-8`;
- maximum relative `D_M(z)` mismatch over nonzero rows `<=1e-8`;
- maximum absolute `Delta ln(D_H/D_M)` at the five target redshifts `<=1e-8`;
- all frozen configuration contracts must pass;
- the pinned-source `EFTwDE=0 -> wDE_LCDM -> w=-1` contract must pass.

Full numeric-table bitwise equality is recorded only as a diagnostic and is **not** a PASS requirement.

No angular, rank, or significance threshold is defined.

## Scientific interpretation if PASS

A PASS establishes, for the frozen high-precision C5 designer-f(R) manifold,

\[
K_{AP}t_{B_0}=0
\]

to the hard numerical tolerance **on a source-proven LCDM expansion branch**, while the already established structure response is nonzero.

Together with Experiment 037 this would supply two qualitatively different hard examples — GDM closure physics and designer modified gravity — whose microscopic directions are background/AP-null but perturbation-active.

That would strengthen the DSIR notion of **channel null spaces / block-sparse influence**, but would not prove a universal law.

## Claim boundary

Experiment 038 cannot establish:

- zero background response for arbitrary f(R) or arbitrary modified gravity;
- zero perturbation response (C5 is already strongly nonzero there);
- parameter constraints or detection significance;
- intrinsic response rank;
- a new residual law or discovery.

G5 remains PARTIAL after this experiment unless all other family-complete observational kernels and robustness requirements are separately satisfied. G7 and G8 remain OPEN.
