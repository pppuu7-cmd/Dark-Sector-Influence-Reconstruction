# DSIR-4 radial-support input requirements v0.1

Status: PROSPECTIVELY FROZEN SUPPORT PREREQUISITE. Scope: DSIR only. This document does **not** define or pass `G_RADIAL_SUPPORT`; it defines the minimum evidence required before that scientific gate can be preregistered without inventing source-bin radial information.

## Upstream authority
`G_ORDERED_JOIN=PASS` is admitted by `docs/dsir4/authority/EXP073IL_C2_ORDERED_JOIN_AUTHORITY_V0_1.json`.

The mandatory funnel defines `G_RADIAL_SUPPORT` as `radial multiplication / support construction`, after the structural ordered join and before physical-support admissibility. Therefore a radial-support gate must bind actual radial source information; angular masks or angular mixing matrices alone are insufficient.

## Required evidence before `G_RADIAL_SUPPORT` can be scientific/testable
For each source-basis element `S0,S1,S2,S3`, a future preregistration must bind an immutable source-radial authority with all of:

1. exact source-bin identity matching the frozen `zbin_mcal=[0,1,2,3]` labels;
2. the actual radial kernel or source redshift-distribution payload used by the observation model, not only an angular sky mask;
3. exact coordinate samples/edges and units for that payload;
4. exact normalization convention and any weighting convention needed to interpret the payload;
5. immutable provenance: repository/external dataset identity, version/release, file identity and cryptographic digest where obtainable;
6. the exact operator/equation by which the frozen C2 prediction-domain object is combined with that radial payload;
7. an explicit fail-closed rule for coordinate mismatch. Existing C2 restrictions continue to forbid interpolation, extrapolation, smoothing, rounding, effective z/k, or fiducial-P substitution unless a later prospective contract independently authorizes a mathematically exact operation without changing those frozen boundaries.

For WW pair slots, any two-source radial construction must be defined prospectively from the corresponding `Si,Sj` authorities. For Wm slots, the matter-side radial/line-of-sight factor required by the actual observable convention must likewise be explicitly bound; it may not be inferred from the angular TE authority alone.

## Evidence audit performed before freezing this requirement
The historical angular runner supporting the admitted angular authority explicitly records `class_ell_mapping_skipped=True`, `radial_kernel_read=False`, and `physical_k_computed=False`. The repository search performed before this contract did not locate a source `n(z)`/`dN/dz`, SOMPZ payload, source-window table, or equivalent radial-kernel dataset under the current DSIR data tree. Existing `zbin_mcal` references identify angular mask files and source labels, not a radial redshift-distribution authority.

Accordingly no numerical radial multiplication is scientifically permitted from the currently located repository evidence.

## Current status
Until all required source-radial evidence and the exact combination operator are bound prospectively:

- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`;
- this is not a scientific FAIL;
- it is not a resource/performance FAIL;
- no proxy support inferred from the seven C2 z samples, angular masks, historical 14-slot ordering, or nominal tomography labels may replace the missing radial authority;
- `scientific_model_authority_created=false` and overall C2 remains `NOT_YET_TESTABLE`.

## Exact next admissible action
Acquire or locate the authoritative source-bin radial/redshift-distribution inputs and their provenance for S0..S3 (plus any matter-side kernel required by Wm), freeze their identities and exact operator in a new prospective contract, then preregister a separate `G_RADIAL_SUPPORT` gate. No experiment label for the numerical gate is reserved by this requirements document.