# DSIR-4 radial operator / payload provenance audit v0.1

Date: 2026-09-09. Scope: DSIR only.

Status: SUPPORT / BLOCKER-NARROWING AUDIT. This document does not pass `G_RADIAL_SUPPORT`, does not reserve an experiment label, and does not authorize numerical projection.

## Frozen upstream state

For `C2_IDE_LOCAL_TANGENT_CONE`:

- `G_DOMAIN_MAPPING=PASS`;
- `G_ANGULAR_AUTHORITY=PASS`;
- `G_ORDERED_JOIN=PASS`;
- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`.

The ordered join fixes four source labels `S0..S3` with `zbin_mcal=[0,1,2,3]`, four `Wm_Si` slots and ten symmetric `WW_Si_Sj` slots. It deliberately defers all radial multiplication and LOS projection to `G_RADIAL_SUPPORT`.

## Exact DES Y3 radial-payload candidate now immutably identified

Candidate file:

`likelihood/des-y3/2pt_NG_final_2ptunblind_02_24_21_wnz_covupdate.v2.fits`

Immutable public mirror:

- repository: `handley-lab/des_y3_data`;
- pinned commit: `9831e872211c2c213b0007bd9910f8accadc8200`;
- Git blob: `6b68824184045e689f4833d31d3253f9a62b1b49`;
- byte size: `26789760`;
- SHA256 recorded by the mirror README: `a72a8ee02fa72474ad859edab27d946991901e3d9a5bdc95cc9a961b244a32a6`.

Independent public code loading this exact DES-Y3 TwoPoint filename reads the `nz_source` extension and its `Z_MID`, `BIN1`, `BIN2`, `BIN3`, `BIN4` columns. Additional DES-Y3-facing code constructs a `twopoint.NumberDensity("nz_source", Z_LOW, Z_MID, Z_HIGH, ...)`, establishing that the source extension convention includes explicit low/mid/high redshift coordinates rather than only an effective redshift.

A separate DES-Y3 configuration at pinned commit `CosmoGridCollab/cosmogridv11@00c3e0242ea822ef060f7ea465fa5a39e9c0ed9e` binds `metacal1..metacal4` respectively to `desy3_nz_source_bin1.txt .. desy3_nz_source_bin4.txt`. This strongly supports the physical source-side interpretation and 1..4 ordering, but does not by itself prove that the already-frozen DSIR angular labels `zbin_mcal=0..3` came from exactly the same catalog/version. The zero-based-to-one-based identity therefore remains candidate-level until an authoritative bridge is located.

## WW operator candidate from pinned CosmoSIS projection code

Pinned projection implementation:

`cosmosis-developers/cosmosis-standard-library@9e3dd611fc20bf39489d43bf4afeb503d26b4e79`

Relevant files:

- `structure/projection/project_2d.py`;
- `structure/projection/projection_tools/kernel.py`.

The pinned code defines `ShearShear` with `kernel_types=("W","W")` and matter power. `TomoNzKernel` normalizes each source `n_i(z)`, converts it to `n_i(chi)`, and constructs a lensing efficiency kernel of the form

`W_i(chi) proportional to chi/a(chi) * integral_chi^chi_max dchi' n_i(chi') (chi'-chi)/chi'`,

with the cosmological lensing prefactor applied by the spectrum machinery.

Therefore the scientifically plausible WW radial structure is a product of two derived lensing kernels in the LOS projection, not a direct product `n_i(z)n_j(z)`. A future DSIR radial contract must not replace the actual lensing operator by a raw source-distribution multiplication.

This code is a candidate observation-model authority only until exact compatibility with the frozen DSIR WW semantics (`EE<-EE` angular authority and the precise DES data-chain convention used for those authorities) is proven prospectively.

## Wm remains unresolved

The repository freezes `Wm` angular semantics as `TE<-TE`, but that token is angular mixing semantics and does not uniquely specify the physical radial second field. No authoritative repository evidence located in this audit proves whether the radial partner is a number-density kernel, matter-shell kernel, CMB-lensing kernel, or another explicitly defined field/window.

Consequently no `Wm` LOS kernel may be guessed from the string `Wm` or from the `TE<-TE` angular operator.

## Current blocker decomposition

Resolved or materially advanced:

1. exact DES-Y3 source-payload filename: LOCATED;
2. immutable mirror commit/blob/size: LOCATED;
3. SHA256 for exact source-payload candidate: LOCATED;
4. source extension has four bins and redshift coordinate structure including `Z_LOW/Z_MID/Z_HIGH`: SUPPORTED;
5. DES-Y3 metacal1..4 -> source-bin1..4 ordering: STRONGLY SUPPORTED;
6. WW weak-lensing kernel functional form: CANDIDATE OPERATOR LOCATED.

Still fail-closed:

1. authoritative bridge from the exact DSIR `zbin_mcal=[0,1,2,3]` angular inputs to this exact Y3 `BIN1..BIN4` payload;
2. exact normalization/weighting semantics of the stored source distribution as used by the DSIR-compatible observation chain;
3. exact compatibility proof between the pinned CosmoSIS WW operator and the frozen DSIR WW authority convention;
4. physical identity and LOS/radial operator for Wm;
5. exact coordinate compatibility rule coupling the continuous radial kernel to the frozen C2 `(z,k)` prediction coordinates without forbidden interpolation/effective coordinates.

## Scientific state after audit

Unchanged:

- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`;
- `scientific_model_authority_created=false`;
- `overall_status=NOT_YET_TESTABLE`.

The reason is now narrower: source bytes/provenance and a plausible WW kernel are identifiable; the remaining critical uncertainty is exact semantic binding, especially Wm and the DSIR source-label provenance bridge.

## Next admissible action

Locate the exact provenance of the DSIR angular source maps/masks that produced `zbin_mcal=0..3` and bind it to the Y3 `nz_source` file/version. Separately locate the physical field definition underlying the frozen Wm slots and its production code/data window. Only after those two semantic bridges are frozen may a numerical `G_RADIAL_SUPPORT` preregistration be created.
