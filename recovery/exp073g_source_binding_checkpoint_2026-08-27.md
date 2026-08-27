# DSIR recovery checkpoint — Exp073G source binding

**Date:** 2026-08-27

## Current scientific state

- Exp073E remains `C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E`.
- Exp073F is `PERTURBATIVE_OBSERVATIONAL_ROUTE_CANDIDATE_FOUND_EXP073F`.
- Primary Exp073F candidate: KiDS-1000 + BOSS 3x2pt with prospective BNT physical-scale localization.
- Exp073G exact physical-support audit is prospectively frozen.
- No Exp073G support value or retained dimension has yet been evaluated.

## Exact public source identity frozen

The KiDS-1000 release page directly links the public software/data repository `KiDS-WL/Cat_to_Obs_K1000_P1`.

Freeze repository commit:

`36676da44471979dacb779155d7e6e7212ae1f4f`

Tree:

`36932b9f499a5fd469890caebf62418f3f8bc40e`

The repository README identifies:

- `data/boss/Sanchez_etal_2017` as BOSS clustering data;
- `data/boss/nofz` as BOSS/2dFLenS redshift distributions for GGL;
- `data/kids/nofz` as KiDS source redshift distributions;
- `data/kids/fits*`, `data/kids/xipm`, and KiDS bandpower products as released weak-lensing data/operator inputs.

The source-binding record is:

`data/derived/g7/exp073g_kids_boss_bnt_source_binding_v0_1.json`.

No covariance values were read to make this binding.

## Frozen support remains unchanged

- `0.295 <= z <= 2.33`;
- `0.000704833374744468 <= k <= 0.06664762008318016 Mpc^-1`;
- positive-weight invalid fraction <= `0.05`;
- support PASS requires mm, signed Wm and WW retained channels and >=15 total retained observation coordinates.

## Next exact implementation work

Before any Exp073G support classification:

1. clone exactly `KiDS-WL/Cat_to_Obs_K1000_P1@36676da44471979dacb779155d7e6e7212ae1f4f`;
2. identify only the n(z), density/GGL and weak-lensing data/window objects needed for support geometry and compute their SHA256 digests;
3. do not read covariance values;
4. freeze the continuous-bin BNT matrix convention/implementation and test nulling algebra before support output;
5. freeze any BOSS/2dFLenS redshift selection strictly from the Exp073G geometric rules;
6. only then calculate transformed-kernel leakage and retained dimension.

G7 OPEN. G8 OPEN. G9 OPEN.
