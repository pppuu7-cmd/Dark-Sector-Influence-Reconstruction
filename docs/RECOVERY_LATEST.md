# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_IL_ORDERED_JOIN_PASS_RADIAL_SUPPORT_BLOCKED_V54.md` (creation commit `95fc6416b350e1a41ab1bca8fa50cd2c665024c9`). Earlier recovery notes remain immutable history.

## Preserved scientific authority
All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run/job `34218457380 / 102035691774`, source artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

C2 admitted tangent numerical authority remains Exp073ID `34249671091 / 102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`, base step `1e-4`. IF mapping admission `34250714613 / 102144147469` preserves `mapping_ready=true`; IG prediction admission `34251593341 / 102147045097` preserves `prediction_ready=true`; IH `34251721583 / 102147505217` preserves `G_DOMAIN_MAPPING=PASS`; IJ preserves `G_ANGULAR_AUTHORITY=PASS`.

## Newly admitted scientific gate — Exp073IL structural ordered join
Prospective definition `docs/dsir4/contracts/DSIR4_ORDERED_JOIN_DEFINITION_V0_1.md`, commit `a2d4db0c1a0763d064ca4a47cf73aa9e6a4ea376`, blob `b594579c9f95fdb5085f5e9ba09f4dbc383d719a`, defines the exact 14-slot structural/provenance join and explicitly performs no radial multiplication or projection.

Historical first run `34271889927 / 102215228801` is infrastructure/implementation `+0/+0`: its first causal failure was only a shell-style literal check against JSON authority syntax. Minimal repair commit `d13d6ab2f99a632b434c8e6ecad821ddf0aead3e` changed only those exact static checks; no science changed.

Valid admission run/job `34271954072 / 102215439354`, head `5bf6b492c3f4220a5c5aaf2276f6acd83507ad60`, has raw token `PASS_EXP073IL_C2_ORDERED_JOIN_STRUCTURAL_ADMISSION_V0_1`, `classification=SCIENTIFIC_GATE_PASS`, and exact state `G_ORDERED_JOIN=PASS`, `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`, `scientific_model_authority_created=false`, `overall_status=NOT_YET_TESTABLE`.

Artifact `10074157812`, name `exp073il-c2-ordered-join-structural-admission-v0-1`; independently verified ZIP SHA256 `acaaf9c00a3654b5e59c190470325a92818e8f2f94296ee45bce1ecfd27baa9e`. Durable authority: `docs/dsir4/authority/EXP073IL_C2_ORDERED_JOIN_AUTHORITY_V0_1.json`, creation commit `ad2768a11b306134129aca9f9f6639818b26d6f7`, blob `31bcde1737c782cbce16db2e447a76ab007d3bbb`.

## Authoritative C2 funnel state
- `G_DOMAIN_MAPPING=PASS`
- `G_ANGULAR_AUTHORITY=PASS`
- `G_ORDERED_JOIN=PASS`
- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`
- `G_PHYSICAL_SUPPORT=NOT_YET_TESTABLE`
- `G_COV_WHITENING=NOT_YET_TESTABLE`
- `G_NUISANCE_QUOTIENT=NOT_YET_TESTABLE`
- `G_RELATION_NULL=NOT_YET_TESTABLE`
- `G_FINAL_MODEL=NOT_YET_TESTABLE`
- `overall_status=NOT_YET_TESTABLE`
- `scientific_model_authority_created=false`.

This is not a complete C2/model PASS.

## Current frontier — radial-support prerequisite BLOCKED
The mandatory funnel defines `G_RADIAL_SUPPORT` as `radial multiplication / support construction`. Repository evidence audit found the historical angular runner explicitly has `class_ell_mapping_skipped=True`, `radial_kernel_read=False`, `physical_k_computed=False`. Current DSIR data/search did not locate authoritative source `n(z)`/`dN/dz`, SOMPZ/source-window payloads, or equivalent S0..S3 radial-kernel data; `zbin_mcal` references currently bind source labels/angular masks, not source-radial authority.

A support prerequisite was frozen without claiming PASS: `docs/dsir4/contracts/DSIR4_RADIAL_SUPPORT_INPUT_REQUIREMENTS_V0_1.md`, creation commit `9064b6e948e328df00439f31c54c6b08e8ea933e`, blob `3fa4a41b3c53f4d8e879a105f0f5621cc60a9f98`. It requires immutable S0..S3 radial payloads, exact coordinates/edges/units, normalization/weighting, provenance/digests, exact combination operator and fail-closed coordinate semantics, plus the matter-side radial/LOS factor required by Wm.

Until those inputs are acquired/located and prospectively bound, `G_RADIAL_SUPPORT` remains **BLOCKED / NOT_YET_TESTABLE**. No seven-z proxy, angular-mask proxy, interpolation/extrapolation, effective coordinate, smoothing, rounding or fiducial-P substitution is allowed.

Current Actions state at this update: no permitted computation is active; home/self-hosted runner ownership: none.

Exact next permitted action: acquire or locate the authoritative source-bin radial/redshift-distribution inputs for S0..S3 and any Wm matter-side kernel, bind immutable provenance plus exact coordinate/normalization semantics, then prospectively freeze the actual radial multiplication/support operator. Only then may a separate `G_RADIAL_SUPPORT` experiment be preregistered/launched.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.