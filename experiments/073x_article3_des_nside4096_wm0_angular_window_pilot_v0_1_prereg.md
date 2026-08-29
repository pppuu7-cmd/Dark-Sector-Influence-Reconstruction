# Exp073X — Article 3 exact DES nside=4096 Wm source-bin-0 angular-window pilot v0.1

**Frozen:** 2026-08-30, after Exp073W PASS and before any Exp073X numerical output.

## Purpose

Exp073X is a **real-data, exact-resolution, non-classifying angular-operator pilot** for Article-3 Layer A. It asks one narrow question before launching the full 14-workspace DES build:

> Can the exact pinned Cosmotheka / NaMaster 2.7 Wm angular bandpower response be reproduced at classifying `nside=4096` from the already-authoritative survey masks alone, without re-reading signal values from the 84-GB metacal catalog?

This pilot evaluates **no physical `(z,k)` support fraction**, produces no retained/rejected observation coordinates, and cannot change Article-3 scientific readiness by itself. It is an execution/provenance prerequisite for the full DES broad operator.

## Scientific reason the signal catalog is not a direct Layer-A angular input

The pinned Cosmotheka code separates map/mask construction from the NaMaster workspace. In `Cl._compute_workspace`, the coupling matrix is determined by NaMaster fields, masks, spins and the frozen binning. NaMaster 2.7 supports a mask-only field with an explicitly supplied spin. The Article-3 Layer-A operator requires the survey **window response**, not measured shear/density amplitudes.

For DES source masks, pinned `MapperDESY1wl._get_mask()` is exactly the HEALPix count map of the selected source catalog. Genuine hosted Exp073R1 v0.8 already read and checksum-bound the full 84,075,649,920-byte metacal object and emitted the exact selected source HEALPix pixel-index sequence for each tomographic bin. Therefore the source count mask can be reconstructed deterministically from that already-frozen derived authority without re-downloading the 84-GB signal catalog.

Exp073X must not claim that the 84-GB catalog is scientifically irrelevant. It remains the upstream provenance of the source-mask authority. The claim is only that it need not be a **direct repeated input** to the mask-only angular workspace.

## Frozen authorities

### Cosmotheka / NaMaster

- Cosmotheka commit: `7bde066626f66cd7bbe79cc46224d2342840e463`;
- exact bandpower edges:
  `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`;
- NaMaster lineage: `pymaster==2.7`;
- Wm component order already verified by Exp073T: spin-0 × spin-2 = `[TE,TB]`;
- Wm physical signal component: output `TE` response to input `TE`;
- classifying resolution: `nside=4096`;
- no Toeplitz approximation: use the exact default coupling calculation corresponding to frozen `l_toeplitz=-1`, `l_exact=-1`, `dl_band=-1`.

### Lens mask

Use the exact public DES-Y1 redMaGiC mask:

`https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redmagic/DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`

Frozen byte count and SHA256 from the earlier immutable preflight:

- bytes: `104595840`;
- SHA256: `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

Apply the pinned mapper semantics exactly:

1. read RING HEALPix map;
2. `UNSEEN -> 0`;
3. no coordinate rotation (`C -> C`);
4. no nside change (4096 -> 4096);
5. threshold: pixels `<=0.5` are set to zero; values above 0.5 retain their original mask weight.

All five DESgc tomographic bins use this same angular mask; Exp073X uses it only once.

### Source-bin-0 count mask

Bind to genuine hosted Exp073R1 v0.8:

- run `33270843577`;
- job `99148916507`;
- head `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- artifact `9720335366`;
- artifact digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- exact full metacal bytes `84075649920`;
- exact full metacal SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- source-bin-0 selected rows `7705486`;
- source-bin-0 pixel-record bytes `30821944`;
- source-bin-0 pixel-record SHA256 `5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15`;
- source-bin-0 binary occupancy SHA256 `b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32`.

The count mask is reconstructed as the exact dense equivalent of

`numpy.bincount(pixel_indices, minlength=12*4096^2)`

in canonical float64 values. The total count must equal 7,705,486. The nonzero-pixel count and occupancy fingerprint must agree with the frozen R1/Exp073S authority.

## Frozen mask-only NaMaster construction

Construct

- lens field: `NmtField(lens_mask, None, spin=0)`;
- source field: `NmtField(source_count_mask, None, spin=2)`;
- binning: `NmtBin.from_edges(frozen_edges[:-1], frozen_edges[1:])`;
- workspace: exact `NmtWorkspace.compute_coupling_matrix(lens_field, source_field, binning)`;
- bandpower windows: `workspace.get_bandpower_windows()`.

Do not use signal maps, measured C_ell, noise, covariance, fiducial P(k), nuisance vectors, relation/null outputs or G7/G8/G9 information.

## Frozen expected structural output

Fail closed unless:

1. NaMaster reports the already-verified spin0×spin2 response structure with two output/input components;
2. there are exactly 39 bandpowers;
3. the unbinned ell axis has exactly `3*nside = 12288` multipoles (`ell=0..12287`) consistent with the frozen binning endpoint;
4. the TE-output / TE-input response matrix has logical shape `[39,12288]`;
5. every TE response value is finite;
6. every band has finite strictly positive absolute-response normalization `sum_ell abs(W_TE,TE[b,ell])`;
7. a second independent workspace computation from copied masks produces the same canonical TE-window SHA256. If resource limits make the second full workspace impossible, the run is incomplete/invalid rather than allowed to waive repeatability post hoc.

Canonical TE windows are little-endian float64 `[39,12288]`, and authority is their logical-array SHA256, not FITS/NPZ container metadata.

## Runtime/resource semantics

A hosted out-of-memory, timeout, package-install failure or transport failure is `INCOMPLETE_EXP073X_INFRASTRUCTURE`, not a scientific support result. It may justify a new frozen execution architecture (for example one exact workspace per runner or the already configured self-hosted machine) but may not change masks, nside, bandpower edges or window semantics.

## Required positive token

`PASS_EXP073X_DES_N4096_WM0_MASK_ONLY_ANGULAR_WINDOW_V0_1`

## Scientific accounting

Even on PASS:

- physical support evaluated: `false`;
- real Layer A classified: `false`;
- retained coordinate set frozen: `false`;
- covariance authorized: `false`;
- G7/G8/G9: OPEN;
- strict Article-3 scientific readiness: **52%**.

A PASS authorizes expansion to the remaining unique DES angular workspaces: 3 additional Wm source masks plus the 10 source-source WW mask pairs, followed by exact redshift-kernel binding and the real `(z,k)` Layer-A calculation.
